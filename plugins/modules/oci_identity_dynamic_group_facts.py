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
module: oci_identity_dynamic_group_facts
short_description: Fetches details about one or multiple DynamicGroup resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DynamicGroup resources in Oracle Cloud Infrastructure
    - Lists the dynamic groups in your tenancy. You must specify your tenancy's OCID as the value for
      the compartment ID (remember that the tenancy is simply the root compartment).
      See L(Where to Get the Tenancy's OCID and User's OCID,https://docs.cloud.oracle.com/Content/API/Concepts/apisigningkey.htm#five).
    - If I(dynamic_group_id) is specified, the details of a single DynamicGroup will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    dynamic_group_id:
        description:
            - The OCID of the dynamic group.
            - Required to get a specific dynamic_group.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment (remember that the tenancy is simply the root compartment).
            - Required to list multiple dynamic_groups.
        type: str
    name:
        description:
            - A filter to only return resources that match the given name exactly.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for NAME is ascending. The NAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by Availability Domain if the scope of the resource type is within a
              single Availability Domain. If you call one of these \\"List\\" operations without specifying
              an Availability Domain, the resources are grouped by Availability Domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "NAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List dynamic_groups
  oci_identity_dynamic_group_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific dynamic_group
  oci_identity_dynamic_group_facts:
    dynamic_group_id: "ocid1.dynamicgroup.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
dynamic_groups:
    description:
        - List of DynamicGroup resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the group.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the tenancy containing the group.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name you assign to the group during creation. The name must be unique across all groups in
                  the tenancy and cannot be changed.
            returned: on success
            type: string
            sample: name_example
        description:
            description:
                - The description you assign to the group. Does not have to be unique, and it's changeable.
            returned: on success
            type: string
            sample: description_example
        matching_rule:
            description:
                - A rule string that defines which instance certificates will be matched.
                  For syntax, see L(Managing Dynamic Groups,https://docs.cloud.oracle.com/Content/Identity/Tasks/managingdynamicgroups.htm).
            returned: on success
            type: string
            sample: matching_rule_example
        time_created:
            description:
                - Date and time the group was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        lifecycle_state:
            description:
                - The group's current state. After creating a group, make sure its `lifecycleState` changes from CREATING to
                  ACTIVE before using it.
            returned: on success
            type: string
            sample: CREATING
        inactive_status:
            description:
                - The detailed status of INACTIVE lifecycleState.
            returned: on success
            type: int
            sample: 56
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "matching_rule": "matching_rule_example",
        "time_created": "2016-08-25T21:10:29.600Z",
        "lifecycle_state": "CREATING",
        "inactive_status": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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


class DynamicGroupFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "dynamic_group_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dynamic_group,
            dynamic_group_id=self.module.params.get("dynamic_group_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_dynamic_groups,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DynamicGroupFactsHelperCustom = get_custom_class("DynamicGroupFactsHelperCustom")


class ResourceFactsHelper(DynamicGroupFactsHelperCustom, DynamicGroupFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dynamic_group_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="dynamic_group",
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

    module.exit_json(dynamic_groups=result)


if __name__ == "__main__":
    main()
