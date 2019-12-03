#!/usr/bin/python
# Copyright (c) 2019, Oracle and/or its affiliates.
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
module: oci_identity_provider_facts
short_description: Retrieve details about published App Catalog listings in OCI Compute Service
description:
    - This module retrieves information of a specified app catalog listing or lists all the app catalog listings
      in the tenancy.
version_added: "2.5"
options:
    identity_provider_id:
        description: The OCID of the identity provider. Required to get information of a specific identity provider.
        type: str
        aliases: ["id"]
    protocol:
        description: The protocol used for federation.
        type: str
        choices: ["SAML2"]
        default: "SAML2"
    compartment_id:
        description: The OCID of the tenancy (remember that the tenancy is simply the root compartment).
        type: str
    name:
        description: Filter the identity providers with given name.
        type: str
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Get all identity providers of given protocol in the tenancy
  oci_identity_provider_facts:
    protocol: SAML2
    compartment_id: ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx

- name: Get a specific identity provider using its OCID
  oci_identity_provider_facts:
    identity_provider_id: ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxx
"""

RETURN = """
identity_providers:
    description: List of identity provider details
    returned: on success
    type: complex
    contains:
        compartment_id:
            description: The OCID of the tenancy containing the IdentityProvider.
            returned: success
            type: str
            sample: ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx
        defined_tags:
            description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: success
            type: str
            sample: {"Operations": {"CostCenter": "42"}}
        description:
            description: The description you assign to the IdentityProvider during creation.
            returned: success
            type: str
            sample: Test identity provider
        freeform_tags:
            description: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                         type, or namespace.
            returned: success
            type: str
            sample: {"Department": "Finance"}
        id:
            description: The OCID of the IdentityProvider.
            returned: success
            type: str
            sample: ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxx
        inactive_status:
            description: The detailed status of INACTIVE lifecycleState.
            returned: success
            type: str
            sample: null
        lifecycle_state:
            description: The current state. After creating an IdentityProvider, make sure its lifecycleState changes
                         from CREATING to ACTIVE before using it.
            returned: success
            type: str
            sample: ACTIVE
        metadata_url:
            description: The URL for retrieving the identity provider's metadata, which contains information required
                         for federating.
            returned: success
            type: str
            sample: https://idcs-31ddf5c2bxxxxxxx429d5c2c927.identity.oraclecloud.com
        name:
            description: The name you assign to the IdentityProvider during creation. The name must be unique across
                         all IdentityProvider objects in the tenancy and cannot be changed. This is the name federated
                         users see when choosing which identity provider to use when signing in to the
                         Oracle Cloud Infrastructure Console.
            returned: success
            type: str
            sample: TEST_IDENTITY_PROVDER
        product_type:
            description: The identity provider service or product. Supported identity providers are Oracle Identity
                         Cloud Service (IDCS) and Microsoft Active Directory Federation Services (ADFS).
            returned: success
            type: str
            sample: ADFS
        protocol:
            description: The protocol used for federation.
            returned: success
            type: str
            sample: SAML2
        redirect_url:
            description: The URL to redirect federated users to for authentication with the identity provider.
            returned: success
            type: str
            sample: https://idpinstance.ansibletest.com/adfs/ls/
        signing_certificate:
            description: The identity provider's signing certificate used by the IAM Service to validate the SAML2
                         token.
            returned: success
            type: str
            sample: null
        time_created:
            description: Date and time the IdentityProvider was created, in the format defined by RFC3339.
            returned: success
            type: str
            sample: 2016-08-25T21:10:29.600Z
    sample: [{
                "compartment_id": "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx",
                "defined_tags": {},
                "description": "Test Identity Provider",
                "freeform_attributes": {},
                "freeform_tags": {},
                "id": "ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxx",
                "inactive_status": null,
                "lifecycle_state": "ACTIVE",
                "metadata_url": null,
                "name": "TEST_IDENTITY_PROVDER",
                "product_type": "ADFS",
                "protocol": "SAML2",
                "redirect_url": "https://testidp.oracletest.com/adfs/ls/",
                "signing_certificate": null,
                "time_created": "2019-04-01T21:49:41.934000+00:00"
            }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def list_identity_providers(identity_client, module):
    optional_list_method_params = ["name"]
    optional_kwargs = dict(
        (param, module.params[param])
        for param in optional_list_method_params
        if module.params.get(param) is not None
    )
    return to_dict(
        oci_utils.list_all_resources(
            identity_client.list_identity_providers,
            protocol=module.params.get("protocol"),
            compartment_id=module.params.get("compartment_id"),
            **optional_kwargs
        )
    )


def get_identity_provider(identity_client, module):
    return to_dict(
        [
            oci_utils.call_with_backoff(
                identity_client.get_identity_provider,
                identity_provider_id=module.params.get("identity_provider_id"),
            ).data
        ]
    )


def main():
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_name=True)
    module_args.update(
        dict(
            identity_provider_id=dict(type="str", aliases=["id"]),
            protocol=dict(type="str", choices=["SAML2"], default="SAML2"),
            compartment_id=dict(type="str"),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[
            ["identity_provider_id", "compartment_id"],
            ["identity_provider_id", "protocol"],
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    try:
        if module.params.get("identity_provider_id"):
            result = get_identity_provider(identity_client, module)
        elif module.params.get("compartment_id"):
            result = list_identity_providers(identity_client, module)
        else:
            module.fail_json(
                msg="Specify compartment_id and protocol to get all the identity providers of the given protocol "
                "in the compartment or identity_provider_id to retrieve a specific identity provider."
            )
    except ServiceError as se:
        module.fail_json(msg=se.message)

    module.exit_json(identity_providers=result)


if __name__ == "__main__":
    main()
