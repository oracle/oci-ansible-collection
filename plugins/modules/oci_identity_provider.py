#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_identity_provider
short_description: Manage Identity Providers in OCI
description:
    - This module allows the user to create, delete and update identity providers in OCI.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of your tenancy.
        type: str
    description:
        description: The description you assign to the IdentityProvider during creation. Does not have to be unique,
                     and it's changeable.
        type: str
    freeform_attributes:
        description: Extra name value pairs associated with this identity provider.
        type: dict
    metadata:
        description: The XML that contains the information required for federating.
        type: str
    metadata_url:
        description: The URL for retrieving the identity provider's metadata, which contains information required
                     for federating.
        type: str
    name:
        description: The name you assign to the IdentityProvider during creation. The name must be unique across all
                     IdentityProvider objects in the tenancy and cannot be changed.
        type: str
    product_type:
        description: The identity provider service or product. Supported identity providers are Oracle Identity Cloud
                     Service (IDCS) and Microsoft Active Directory Federation Services (ADFS).
        type: str
        choices:
            - IDCS
            - ADFS
    protocol:
        description: The protocol used for federation.
        type: str
        choices:
            - SAML2
        default: SAML2
    state:
        description: Create or update an identity provider with I(state=present). Use I(state=absent) to delete
                     an identity provider.
        type: str
        default: present
        choices: ['present', 'absent']
    identity_provider_id:
        description: The OCID of the identity provider. Required when deleting the identity provider with
                     I(state=absent) or updating the identity provider with I(state=present). This option is mutually
                     exclusive with I(compartment_id).
        type: str
        aliases: [ 'id' ]
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create an identity provider
  oci_identity_provider:
    compartment_id: 'ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx'
    description: test identity provider
    freeform_attributes:
        clientId: app_sf3kdjf3
    metadata_url: https://myidpserver/FederationMetadata/2007-06/FederationMetadata.xml
    name: mytestidentityprovider
    product_type: ADFS
    protocol: SAML2

- name: Update description of an identity provider
  oci_identity_provider:
    identity_provider_id: ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxx
    description: updated description

- name: Delete the specified identity provider
  oci_identity_provider:
    identity_provider_id: ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
identity_provider:
    description: Information about the identity provider
    returned: On successful create and update operation
    type: dict
    sample: {
            "cidr_block": "10.0.0.0/16",
            compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "default_dhcp_options_id": "ocid1.dhcpoptions.oc1.phx.xxxxxEXAMPLExxxxx",
            "default_route_table_id": "ocid1.routetable.oc1.phx.xxxxxEXAMPLExxxxx",
            "default_security_list_id": "ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx",
            "display_name": "ansible_vcn",
            "dns_label": "ansiblevcn",
            "id": "ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx",
            "lifecycle_state": "AVAILABLE",
            "time_created": "2017-11-13T20:22:40.626000+00:00",
            "vcn_domain_name": "ansiblevcn.oraclevcn.com"
            }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.identity.models import (
        CreateSaml2IdentityProviderDetails,
        UpdateSaml2IdentityProviderDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

RESOURCE_TYPE = "identity_provider"


def delete_identity_provider(identity_client, module):
    result = oci_utils.delete_and_wait(
        resource_type=RESOURCE_TYPE,
        client=identity_client,
        get_fn=identity_client.get_identity_provider,
        kwargs_get={"identity_provider_id": module.params["identity_provider_id"]},
        delete_fn=identity_client.delete_identity_provider,
        kwargs_delete={"identity_provider_id": module.params["identity_provider_id"]},
        module=module,
    )
    return result


def update_identity_provider(identity_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type=RESOURCE_TYPE,
        client=identity_client,
        get_fn=identity_client.get_identity_provider,
        kwargs_get={"identity_provider_id": module.params["identity_provider_id"]},
        update_fn=identity_client.update_identity_provider,
        primitive_params_update=["identity_provider_id"],
        kwargs_non_primitive_update={
            UpdateSaml2IdentityProviderDetails: "update_identity_provider_details"
        },
        module=module,
        update_attributes=UpdateSaml2IdentityProviderDetails().attribute_map.keys(),
    )
    return result


def create_identity_provider(identity_client, module):
    create_identity_provider_details = CreateSaml2IdentityProviderDetails()
    for attribute in create_identity_provider_details.attribute_map.keys():
        if attribute in module.params:
            setattr(
                create_identity_provider_details, attribute, module.params[attribute]
            )

    result = oci_utils.create_and_wait(
        resource_type=RESOURCE_TYPE,
        create_fn=identity_client.create_identity_provider,
        kwargs_create={
            "create_identity_provider_details": create_identity_provider_details
        },
        client=identity_client,
        get_fn=identity_client.get_identity_provider,
        get_param="identity_provider_id",
        module=module,
    )
    return result


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            description=dict(type="str"),
            freeform_attributes=dict(type="dict"),
            metadata=dict(type="str"),
            metadata_url=dict(type="str"),
            name=dict(type="str"),
            product_type=dict(type="str", choices=["IDCS", "ADFS"]),
            protocol=dict(type="str", choices=["SAML2"], default="SAML2"),
            state=dict(type="str", default="present", choices=["absent", "present"]),
            identity_provider_id=dict(type="str", aliases=["id"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[["compartment_id", "identity_provider_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    exclude_attributes = {}
    state = module.params["state"]
    identity_provider_id = module.params.get("identity_provider_id")

    if state == "absent":
        if identity_provider_id:
            result = delete_identity_provider(identity_client, module)
        else:
            module.fail_json(
                msg="Specify identity_provider_id with state as 'absent' to delete the identity provider."
            )

    else:
        if identity_provider_id:
            result = update_identity_provider(identity_client, module)
        elif module.params.get("compartment_id"):
            result = oci_utils.check_and_create_resource(
                resource_type="identity_provider",
                create_fn=create_identity_provider,
                kwargs_create={"identity_client": identity_client, "module": module},
                list_fn=identity_client.list_identity_providers,
                kwargs_list={
                    "protocol": module.params.get("protocol"),
                    "compartment_id": module.params["compartment_id"],
                },
                module=module,
                model=CreateSaml2IdentityProviderDetails(),
                exclude_attributes=exclude_attributes,
            )
        else:
            module.fail_json(
                msg="Either provide identity_provider_id to update an existing identity provider or "
                "compartment_id to create a new identity provider."
            )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
