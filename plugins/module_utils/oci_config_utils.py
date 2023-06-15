# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_version,
    oci_log_utils,
)
import os
import logging

try:

    import oci
    from oci.exceptions import (
        InvalidConfig,
        InvalidPrivateKey,
        MissingPrivateKeyPassphrase,
        ConfigFileNotFound,
    )
    from oci.auth.signers.resource_principals_signer import (
        get_resource_principals_signer,
    )
    from oci.identity.identity_client import IdentityClient
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

agent_name = "Oracle-Ansible/"
inventory_agent_name = "Oracle-Ansible-Inv/"

logger = logging.getLogger(__name__)


def get_oci_config(module, service_client_class=None):
    """Return the OCI configuration to use for all OCI API calls. The effective OCI configuration is derived by merging
    any overrides specified for configuration attributes through Ansible module options or environment variables. The
    order of precedence for deriving the effective configuration dict is:
    1. If a config file is provided, use that to setup the initial config dict.
    2. If a config profile is specified, use that config profile to setup the config dict.
    3. For each authentication attribute, check if an override is provided either through
        a. Ansible Module option
        b. Environment variable
        and override the value in the config dict in that order."""
    config = {}

    config_file = module.params.get("config_file_location")
    if not config_file:
        if "OCI_CONFIG_FILE" in os.environ and os.environ["OCI_CONFIG_FILE"]:
            config_file = os.environ["OCI_CONFIG_FILE"]
        else:
            config_file = "~/.oci/config"

    config_profile = module.params.get("config_profile_name")
    if not config_profile:
        if "OCI_CONFIG_PROFILE" in os.environ and os.environ["OCI_CONFIG_PROFILE"]:
            config_profile = os.environ["OCI_CONFIG_PROFILE"]
        else:
            config_profile = "DEFAULT"
    try:
        config = oci.config.from_file(
            file_location=config_file, profile_name=config_profile
        )
    except (
        ConfigFileNotFound,
        InvalidConfig,
        InvalidPrivateKey,
        MissingPrivateKeyPassphrase,
    ) as ex:
        if (
            not _is_instance_principal_auth(module)
            and not _is_delegation_token_auth(module)
            and not _is_resource_principal_auth(module)
        ):
            # When auth_type is not instance_principal, config file is required
            module.fail_json(msg=str(ex))

    config["additional_user_agent"] = agent_name + oci_version.__version__
    # Merge any overrides through other IAM options
    _merge_auth_option(
        config,
        module,
        module_option_name="api_user",
        env_var_name="OCI_USER_ID",
        config_attr_name="user",
    )
    _merge_auth_option(
        config,
        module,
        module_option_name="api_user_fingerprint",
        env_var_name="OCI_USER_FINGERPRINT",
        config_attr_name="fingerprint",
    )
    _merge_auth_option(
        config,
        module,
        module_option_name="api_user_key_file",
        env_var_name="OCI_USER_KEY_FILE",
        config_attr_name="key_file",
    )
    _merge_auth_option(
        config,
        module,
        module_option_name="api_user_key_pass_phrase",
        env_var_name="OCI_USER_KEY_PASS_PHRASE",
        config_attr_name="pass_phrase",
    )
    _merge_auth_option(
        config,
        module,
        module_option_name="tenancy",
        env_var_name="OCI_TENANCY",
        config_attr_name="tenancy",
    )
    _merge_auth_option(
        config,
        module,
        module_option_name="region",
        env_var_name="OCI_REGION",
        config_attr_name="region",
    )
    log_level = oci_log_utils.get_log_level(module._verbosity)
    if log_level == logging.DEBUG:
        # enabling request logging in oci-python-sdk
        config["log_requests"] = True

    return config


def set_db_test_flag(service_client):
    # This flag helps in quickly testing the Database
    if (
        isinstance(service_client, DatabaseClient)
        and os.environ.get("OCI_DB_MOCK") is not None
        and os.environ.get("OCI_DB_MOCK").lower() in ["true", "1"]
    ):
        logger.debug("Adding mock db flag")
        service_client.base_client.session.headers.update(
            {"opc-host-serial": "FAKEHOSTSERIAL"}
        )


def create_service_client(
    module, service_client_class, config=None, client_kwargs=None
):
    """
    Creates a service client using the common module options provided by the user.
    :param module: An AnsibleModule that represents user provided options for a Task
    :param service_client_class: A class that represents a client to an OCI Service
    :param client_kwargs: kwargs that would be passed to the client class
    :return: A fully configured client
    """
    config = config or get_oci_config(module, service_client_class)
    kwargs = client_kwargs or {}

    if "service_endpoint" in module.params.keys():
        kwargs["service_endpoint"] = module.params.get("service_endpoint")

    if _is_instance_principal_auth(module):
        kwargs["signer"] = _create_instance_principal_signer(module)

    if _is_delegation_token_auth(module):
        delegation_token_location = config.get("delegation_token_file")
        kwargs["signer"] = _create_instance_principal_signer(
            module, delegation_token_location
        )

    if _is_resource_principal_auth(module):
        kwargs["signer"] = _create_resource_principal_signer()

    if _is_security_token_auth(module):
        security_token_file = config.get("security_token_file")
        if not security_token_file:
            raise ValueError("security_token_file is required for security_token auth")
        key_file = config.get("key_file")
        if not key_file:
            raise ValueError("key_file is required for security_token auth")
        kwargs["signer"] = _create_security_token_signer(security_token_file, key_file)

    # XXX: Validate configuration -- this may be redundant, as all Client constructors perform a validation
    try:
        oci.config.validate_config(config, **kwargs)
    except oci.exceptions.InvalidConfig as ic:
        module.fail_json(
            msg="Invalid OCI configuration. Exception: {0}".format(str(ic))
        )

    # Create service client class (optionally with signer)
    client = service_client_class(config, **kwargs)

    # Enable/Disable realm specific endpoint template.
    # By Default, realm specific endpoint template is disabled.
    realm_specific_endpoint_template_enabled = get_realm_specific_endpoint_template_enabled(
        module
    )

    if realm_specific_endpoint_template_enabled is not None:
        client.base_client.client_level_realm_specific_endpoint_template_enabled = (
            realm_specific_endpoint_template_enabled
        )

    if not _is_instance_principal_auth(module) and not _is_delegation_token_auth(
        module
    ):
        cert_bundle = get_cert_bundle(module)
        if cert_bundle is not None:
            client.base_client.session.verify = cert_bundle

    # Redirect calls to home region for IAM service.
    do_not_redirect = module.params.get(
        "do_not_redirect_to_home_region", False
    ) or os.environ.get("OCI_IDENTITY_DO_NOT_REDIRECT_TO_HOME_REGION")

    if service_client_class == IdentityClient and not do_not_redirect:

        if "tenancy" in config:
            tenancy_id = config["tenancy"]
        elif hasattr(kwargs.get("signer"), "tenancy_id"):
            # the instance principals signer has the tenancy ID from the certificate from the
            # local metadata service
            tenancy_id = kwargs.get("signer").tenancy_id
        else:
            module.fail_json(
                msg="Could not identify tenancy OCID from config or local metadata service"
            )

        region_subscriptions = oci_common_utils.call_with_backoff(
            client.list_region_subscriptions, tenancy_id=tenancy_id
        ).data

        # Replace the region for the client with the home region.
        home_regions = [
            rs.region_name for rs in region_subscriptions if rs.is_home_region is True
        ]
        if len(home_regions) == 0:
            module.fail_json(msg="Could not identify home region for this tenancy")

        home_region = home_regions[0]

        client.base_client.set_region(home_region)

    set_db_test_flag(client)

    return client


def get_realm_specific_endpoint_template_enabled(module):
    # check if realm specific endpoint template is overridden via module params
    client_configuration = module.params.get("realm_specific_endpoint_template_enabled")

    if client_configuration is not None:
        return client_configuration

    return None


def _create_instance_principal_signer(module, delegation_token_location=None):
    signer = None
    cert_bundle = get_cert_bundle(module)
    try:
        if delegation_token_location:  # instance_obo_user
            signer_kwargs = {}
            delegation_token = None
            # expand file location
            expanded_location = os.path.expanduser(delegation_token_location)
            if not os.path.exists(expanded_location):
                raise IOError(
                    "ERROR: delegation_token_file not found at {0}".format(
                        expanded_location
                    )
                )
            # read from file
            with open(expanded_location, "r") as delegation_token_file:
                delegation_token = delegation_token_file.read().strip()
            # check if token is there
            if delegation_token is None:
                raise ValueError("ERROR: delegation_token was not provided.")
            # fill up kwarg
            signer_kwargs["delegation_token"] = delegation_token
            if cert_bundle is not None:
                signer_kwargs["federation_client_cert_bundle_verify"] = cert_bundle
            # create instance_principal_delegation_auth signer
            signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(
                **signer_kwargs
            )
        else:
            signer_kwargs = {}
            if _is_instance_principal_auth_purpose(module):
                signer_kwargs["purpose"] = "service_principal"
            if cert_bundle is not None:
                signer_kwargs["federation_client_cert_bundle_verify"] = cert_bundle
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner(
                **signer_kwargs
            )
    except (ValueError, IOError) as ex:
        message = "Exception: {0}".format(str(ex))
        module.fail_json(msg=message)
    except Exception as ex:
        message = (
            "Failed retrieving certificates from localhost. Instance principal based authentication is only"
            "possible from within OCI compute instances. Exception: {0}".format(str(ex))
        )
        module.fail_json(msg=message)

    return signer


def _create_resource_principal_signer():
    return get_resource_principals_signer()


def _create_security_token_signer(security_token_file, key_file):
    signer_kwargs = {}
    token_file_expanded_location = os.path.expanduser(security_token_file)
    with open(token_file_expanded_location, "r") as token_file:
        signer_kwargs["token"] = token_file.read().strip()
    signer_kwargs["private_key"] = oci.signer.load_private_key_from_file(key_file)
    signer = oci.auth.signers.SecurityTokenSigner(**signer_kwargs)
    return signer


def _is_instance_principal_auth_purpose(module):
    # check if auth purpose is overridden via module params
    instance_principal_auth_purpose = (
        "auth_purpose" in module.params
        and module.params["auth_purpose"] == "service_principal"
    )
    return instance_principal_auth_purpose


def _is_instance_principal_auth(module):
    # check if auth type is overridden via module params
    instance_principal_auth = (
        "auth_type" in module.params
        and module.params["auth_type"] == "instance_principal"
    )
    if not instance_principal_auth:
        instance_principal_auth = (
            "OCI_ANSIBLE_AUTH_TYPE" in os.environ
            and os.environ["OCI_ANSIBLE_AUTH_TYPE"] == "instance_principal"
        )
    return instance_principal_auth


def get_cert_bundle(module):
    # check if cert bundle is overridden via module params
    cert_bundle = module.params.get("cert_bundle")
    if cert_bundle:
        cert_bundle = os.path.expanduser(cert_bundle)
    else:
        if "OCI_ANSIBLE_CERT_BUNDLE" in os.environ:
            cert_bundle = os.path.expanduser(
                os.path.expandvars(os.environ.get("OCI_ANSIBLE_CERT_BUNDLE"))
            )
    return cert_bundle


def _merge_auth_option(
    config, module, module_option_name, env_var_name, config_attr_name
):
    """Merge the values for an authentication attribute from ansible module options and
    environment variables with the values specified in a configuration file"""

    auth_attribute = module.params.get(module_option_name)
    if not auth_attribute:
        if env_var_name in os.environ:
            auth_attribute = os.environ[env_var_name]

    # An authentication attribute has been provided through an env-variable or an ansible
    # option and must override the corresponding attribute's value specified in the
    # config file [profile].
    if auth_attribute:
        config.update({config_attr_name: auth_attribute})


def _is_delegation_token_auth(module):  # instance_obo_user / delegation token
    # check if auth type is overridden via module params
    delegation_token_auth = (
        "auth_type" in module.params
        and module.params["auth_type"] == "instance_obo_user"
    )
    if not delegation_token_auth:
        delegation_token_auth = (
            "OCI_ANSIBLE_AUTH_TYPE" in os.environ
            and os.environ["OCI_ANSIBLE_AUTH_TYPE"] == "instance_obo_user"
        )
    return delegation_token_auth


def _is_resource_principal_auth(module):
    if (
        "auth_type" in module.params
        and module.params["auth_type"] == "resource_principal"
    ):
        return True
    if (
        "OCI_ANSIBLE_AUTH_TYPE" in os.environ
        and os.environ["OCI_ANSIBLE_AUTH_TYPE"] == "resource_principal"
    ):
        return True
    return False


def _is_security_token_auth(module):
    if "auth_type" in module.params and module.params["auth_type"] == "security_token":
        return True
    if (
        "OCI_ANSIBLE_AUTH_TYPE" in os.environ
        and os.environ["OCI_ANSIBLE_AUTH_TYPE"] == "security_token"
    ):
        return True
    return False
