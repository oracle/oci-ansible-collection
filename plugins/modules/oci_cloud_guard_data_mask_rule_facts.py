#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_cloud_guard_data_mask_rule_facts
short_description: Fetches details about one or multiple DataMaskRule resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DataMaskRule resources in Oracle Cloud Infrastructure
    - Returns a list of all Data Mask Rules in the root 'compartmentId' passed.
    - If I(data_mask_rule_id) is specified, the details of a single DataMaskRule will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    data_mask_rule_id:
        description:
            - OCID of dataMaskRule
            - Required to get a specific data_mask_rule.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple data_mask_rules.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    access_level:
        description:
            - Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`.
              Setting this to `ACCESSIBLE` returns only those compartments for which the
              user has INSPECT permissions directly or indirectly (permissions can be on a
              resource in a subcompartment).
              When set to `RESTRICTED` permissions are checked and no partial results are displayed.
        type: str
        choices:
            - "RESTRICTED"
            - "ACCESSIBLE"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    data_mask_rule_status:
        description:
            - The status of the dataMaskRule.
        type: str
        choices:
            - "ENABLED"
            - "DISABLED"
    target_id:
        description:
            - OCID of target
        type: str
    iam_group_id:
        description:
            - OCID of iamGroup
        type: str
    target_type:
        description:
            - Type of target
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific data_mask_rule
  oci_cloud_guard_data_mask_rule_facts:
    # required
    data_mask_rule_id: "ocid1.datamaskrule.oc1..xxxxxxEXAMPLExxxxxx"

- name: List data_mask_rules
  oci_cloud_guard_data_mask_rule_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    lifecycle_state: CREATING
    access_level: RESTRICTED
    sort_order: ASC
    sort_by: timeCreated
    data_mask_rule_status: ENABLED
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    iam_group_id: "ocid1.iamgroup.oc1..xxxxxxEXAMPLExxxxxx"
    target_type: target_type_example

"""

RETURN = """
data_mask_rules:
    description:
        - List of DataMaskRule resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Data Mask Rule Identifier, can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier where the resource is created.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - The data mask rule description.
            returned: on success
            type: str
            sample: description_example
        iam_group_id:
            description:
                - IAM Group id associated with the data mask rule
            returned: on success
            type: str
            sample: "ocid1.iamgroup.oc1..xxxxxxEXAMPLExxxxxx"
        target_selected:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                kind:
                    description:
                        - Target selection.
                    returned: on success
                    type: str
                    sample: ALL
                values:
                    description:
                        - Ids of Target
                    returned: on success
                    type: list
                    sample: []
        data_mask_categories:
            description:
                - Data Mask Categories
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The date and time the target was created. Format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the target was updated. Format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        data_mask_rule_status:
            description:
                - The status of the dataMaskRule.
            returned: on success
            type: str
            sample: ENABLED
        lifecycle_state:
            description:
                - The current state of the DataMaskRule.
            returned: on success
            type: str
            sample: CREATING
        lifecyle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecyle_details_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
                - Avoid entering confidential information.
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - System tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  System tags can be viewed by users, but can only be created by the system.
                - "Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "iam_group_id": "ocid1.iamgroup.oc1..xxxxxxEXAMPLExxxxxx",
        "target_selected": {
            "kind": "ALL",
            "values": []
        },
        "data_mask_categories": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "data_mask_rule_status": "ENABLED",
        "lifecycle_state": "CREATING",
        "lifecyle_details": "lifecyle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.cloud_guard import CloudGuardClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataMaskRuleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "data_mask_rule_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_mask_rule,
            data_mask_rule_id=self.module.params.get("data_mask_rule_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "lifecycle_state",
            "access_level",
            "sort_order",
            "sort_by",
            "data_mask_rule_status",
            "target_id",
            "iam_group_id",
            "target_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_data_mask_rules,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataMaskRuleFactsHelperCustom = get_custom_class("DataMaskRuleFactsHelperCustom")


class ResourceFactsHelper(DataMaskRuleFactsHelperCustom, DataMaskRuleFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            data_mask_rule_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            access_level=dict(type="str", choices=["RESTRICTED", "ACCESSIBLE"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            data_mask_rule_status=dict(type="str", choices=["ENABLED", "DISABLED"]),
            target_id=dict(type="str"),
            iam_group_id=dict(type="str"),
            target_type=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="data_mask_rule",
        service_client_class=CloudGuardClient,
        namespace="cloud_guard",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(data_mask_rules=result)


if __name__ == "__main__":
    main()
