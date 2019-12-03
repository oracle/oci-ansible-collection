#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019 Oracle and/or its affiliates.
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
module: oci_idp_group_mapping_facts
short_description: Retrieve details of all Identity Provider (IdP) group mappings for a given Identity Provider.
description:
    - This module retrieves details of all Identity Provider (IdP) group mappings for a given Identity Provier.
version_added: "2.5"
options:
    identity_provider_id:
        description: The identifier of the identity provider to fetch group mappings for.
        required: true
        type: str
    mapping_id:
        description: The identifier of the group mapping to fetch the details of.
        aliases: ['id']
        type: str

author: "Mike Ross (@mikeross)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get details of all IdP group mappings for a given identity provider
  oci_idp_group_mapping_facts:
    identity_provider_id: 'ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxxbn4q4eq'

- name: Get the details of a single IdP group mapping
  oci_idp_group_mapping_facts:
    identity_provider_id: 'ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxxbn4q4eq'
    mapping_id: 'ocid1.idpgroupmapping.oc1..xxxxxEXAMPLExxxxxbnmfuwba'
"""

RETURN = """
idp_group_mappings:
    description: Information about one or more IdP group mappings
    returned: on success
    type: complex
    contains:
        id:
            description: The identifier of the IdpGroupMapping.
            returned: always
            type: string
            sample: ocid1.idpgroupmapping.oc1..xxxxxEXAMPLExxxxxbnmfuwba
        idp_id:
            description: The identifier of the Identity Provider this mapping belongs to.
            returned: always
            type: string
            sample: ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxxbn4q4eq
        idp_group_name:
            description: The name of the IdP group that is mapped to the IAM Service group.
            returned: always
            type: string
            sample: IdPGroupName
        group_id:
            description: The identifier of the IAM Service group that is mapped to the IdP group.
            returned: always
            type: string
            sample: ocid1.group.oc1..xxxxxEXAMPLExxxxxsdxbsfda
        compartment_id:
            description: The identifier of the tenancy containing the Identity Provider.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx..6glmkwq
        time_created:
            description: Date and time the mapping was created.
            returned: always
            type: datetime
            sample: 2016-08-25T21:10:29.600Z
        lifecycle_state:
            description: The mapping's current state.  After creating a mapping object, make sure its lifecycle_state changes
                from CREATING to ACTIVE before using it.
            returned: always
            type: string
            sample: ACTIVE
        inactive_status:
            description: The detailed status of INACTIVE lifecycle_state.
            returned: always
            type: int
            sample: 0
    sample: [{
                "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx..6glmkwq",
                "group_id": "ocid1.group.oc1..xxxxxEXAMPLExxxxxsdxbsfda",
                "id": "ocid1.idpgroupmapping.oc1..xxxxxEXAMPLExxxxxbnmfuwba",
                "idp_group_name": "IdPGroupName",
                "idp_id": "ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxxbn4q4eq",
                "inactive_status": null,
                "lifecycle_state": "ACTIVE",
                "time_created": "2016-08-25T21:10:29.600Z"
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


def list_idp_group_mappings(identity_client, module):
    try:
        idp_id = module.params["identity_provider_id"]
        idp_group_mapping_id = module.params["mapping_id"]

        if idp_group_mapping_id:
            idp_group_mappings = [
                oci_utils.call_with_backoff(
                    identity_client.get_idp_group_mapping,
                    identity_provider_id=idp_id,
                    mapping_id=idp_group_mapping_id,
                ).data
            ]
        else:
            idp_group_mappings = oci_utils.list_all_resources(
                identity_client.list_idp_group_mappings, identity_provider_id=idp_id
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    return to_dict(idp_group_mappings)


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            identity_provider_id=dict(type="str", required=True, aliases=["id"]),
            mapping_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    result = list_idp_group_mappings(identity_client, module)
    module.exit_json(idp_group_mappings=result)


if __name__ == "__main__":
    main()
