#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_identity_idp_group_mapping_facts
short_description: Fetches details about one or multiple IdpGroupMapping resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple IdpGroupMapping resources in Oracle Cloud Infrastructure
    - Lists the group mappings for the specified identity provider.
    - If I(mapping_id) is specified, the details of a single IdpGroupMapping will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    identity_provider_id:
        description:
            - The OCID of the identity provider.
        type: str
        required: true
    mapping_id:
        description:
            - The OCID of the group mapping.
            - Required to get a specific idp_group_mapping.
        type: str
        aliases: ["id"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List idp_group_mappings
  oci_identity_idp_group_mapping_facts:
    identity_provider_id: "ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific idp_group_mapping
  oci_identity_idp_group_mapping_facts:
    identity_provider_id: "ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx"
    mapping_id: "ocid1.mapping.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
idp_group_mappings:
    description:
        - List of IdpGroupMapping resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the `IdpGroupMapping`.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        idp_id:
            description:
                - The OCID of the `IdentityProvider` this mapping belongs to.
            returned: on success
            type: string
            sample: "ocid1.idp.oc1..xxxxxxEXAMPLExxxxxx"
        idp_group_name:
            description:
                - The name of the IdP group that is mapped to the IAM Service group.
            returned: on success
            type: string
            sample: idp_group_name_example
        group_id:
            description:
                - The OCID of the IAM Service group that is mapped to the IdP group.
            returned: on success
            type: string
            sample: "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the tenancy containing the `IdentityProvider`.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Date and time the mapping was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        lifecycle_state:
            description:
                - The mapping's current state.  After creating a mapping object, make sure its `lifecycleState` changes
                  from CREATING to ACTIVE before using it.
            returned: on success
            type: string
            sample: CREATING
        inactive_status:
            description:
                - The detailed status of INACTIVE lifecycleState.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "idp_id": "ocid1.idp.oc1..xxxxxxEXAMPLExxxxxx",
        "idp_group_name": "idp_group_name_example",
        "group_id": "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z",
        "lifecycle_state": "CREATING",
        "inactive_status": 56
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IdpGroupMappingFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "identity_provider_id",
            "mapping_id",
        ]

    def get_required_params_for_list(self):
        return [
            "identity_provider_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_idp_group_mapping,
            identity_provider_id=self.module.params.get("identity_provider_id"),
            mapping_id=self.module.params.get("mapping_id"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_idp_group_mappings,
            identity_provider_id=self.module.params.get("identity_provider_id"),
            **optional_kwargs
        )


IdpGroupMappingFactsHelperCustom = get_custom_class("IdpGroupMappingFactsHelperCustom")


class ResourceFactsHelper(
    IdpGroupMappingFactsHelperCustom, IdpGroupMappingFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            identity_provider_id=dict(type="str", required=True),
            mapping_id=dict(aliases=["id"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="idp_group_mapping",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(idp_group_mappings=result)


if __name__ == "__main__":
    main()
