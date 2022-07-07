#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_governance_rules_control_plane_enforced_governance_rule_facts
short_description: Fetches details about one or multiple EnforcedGovernanceRule resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple EnforcedGovernanceRule resources in Oracle Cloud Infrastructure
    - List enforced governance rules. Either compartment id or enforced governance rule id must be supplied.
      An optional governance rule type or a display name can also be supplied.
    - If I(enforced_governance_rule_id) is specified, the details of a single EnforcedGovernanceRule will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    enforced_governance_rule_id:
        description:
            - Unique enforced governance rule identifier.
            - Required to get a specific enforced_governance_rule.
        type: str
        aliases: ["id"]
    governance_rule_type:
        description:
            - A filter to return only resources that match the type given.
        type: str
        choices:
            - "QUOTA"
            - "TAG"
            - "ALLOWED_REGIONS"
    display_name:
        description:
            - A filter to return only resources that match the entire name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific enforced_governance_rule
  oci_governance_rules_control_plane_enforced_governance_rule_facts:
    # required
    enforced_governance_rule_id: "ocid1.enforcedgovernancerule.oc1..xxxxxxEXAMPLExxxxxx"

- name: List enforced_governance_rules
  oci_governance_rules_control_plane_enforced_governance_rule_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    enforced_governance_rule_id: "ocid1.enforcedgovernancerule.oc1..xxxxxxEXAMPLExxxxxx"
    governance_rule_type: QUOTA
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
enforced_governance_rules:
    description:
        - List of EnforcedGovernanceRule resources
    returned: on success
    type: complex
    contains:
        template:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                regions:
                    description:
                        - List of allowed regions.
                    returned: on success
                    type: list
                    sample: []
                display_name:
                    description:
                        - Display name of the allowed region resource.
                    returned: on success
                    type: str
                    sample: display_name_example
                statements:
                    description:
                        - List of quota statements.
                    returned: on success
                    type: list
                    sample: []
                type:
                    description:
                        - Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.
                        - "Example: `QUOTA`"
                    returned: on success
                    type: str
                    sample: QUOTA
                name:
                    description:
                        - The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.
                    returned: on success
                    type: str
                    sample: name_example
                description:
                    description:
                        - Description of the allowed region resource.
                    returned: on success
                    type: str
                    sample: description_example
                tags:
                    description:
                        - Represents an array of tags for tag namespace.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The name you assign to the tag during creation. This is the tag key definition.
                                  The name must be unique within the tag namespace and cannot be changed.
                            returned: on success
                            type: str
                            sample: name_example
                        description:
                            description:
                                - The description assigned to the tag during creation.
                            returned: on success
                            type: str
                            sample: description_example
                        is_cost_tracking:
                            description:
                                - Indicates whether the tag is enabled for cost tracking.
                            returned: on success
                            type: bool
                            sample: true
                        validator:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                validator_type:
                                    description:
                                        - "Specifies the type of validation: a static value (no validation) or a list."
                                    returned: on success
                                    type: str
                                    sample: ENUM
                                values:
                                    description:
                                        - The list of allowed values for a definedTag value.
                                    returned: on success
                                    type: list
                                    sample: []
                tag_defaults:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        tag_name:
                            description:
                                - The name of the tag. The tag default will always assign a default value for this tag name.
                            returned: on success
                            type: str
                            sample: tag_name_example
                        value:
                            description:
                                - The default value for the tag name. This will be applied to all new resources created in the compartment.
                            returned: on success
                            type: str
                            sample: value_example
                        is_required:
                            description:
                                - If you specify that a value is required, a value is set during resource creation (either by
                                  the user creating the resource or another tag default). If no value is set, resource
                                  creation is blocked.
                                - "* If the `isRequired` flag is set to \\"true\\", the value is set during resource creation.
                                  * If the `isRequired` flag is set to \\"false\\", the value you enter is set during resource creation."
                                - "Example: `false`"
                            returned: on success
                            type: bool
                            sample: true
        id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the enforced governance rule.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the child's root compartment to which the
                  governance rule is attached.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        governance_rule_display_name:
            description:
                - Display name of the governance rule.
            returned: on success
            type: str
            sample: governance_rule_display_name_example
        type:
            description:
                - Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.
                - "Example: `QUOTA`"
            returned: on success
            type: str
            sample: QUOTA
        lifecycle_state:
            description:
                - The current state of the governance rule.
            returned: on success
            type: str
            sample: ACTIVE
        time_created:
            description:
                - Date and time the governance rule was created. An RFC3339 formatted datetime string.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Date and time the governance rule was updated. An RFC3339 formatted datetime string.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "template": {
            "regions": [],
            "display_name": "display_name_example",
            "statements": [],
            "type": "QUOTA",
            "name": "name_example",
            "description": "description_example",
            "tags": [{
                "name": "name_example",
                "description": "description_example",
                "is_cost_tracking": true,
                "validator": {
                    "validator_type": "ENUM",
                    "values": []
                }
            }],
            "tag_defaults": [{
                "tag_name": "tag_name_example",
                "value": "value_example",
                "is_required": true
            }]
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "governance_rule_display_name": "governance_rule_display_name_example",
        "type": "QUOTA",
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.governance_rules_control_plane import GovernanceRuleClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EnforcedGovernanceRuleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "enforced_governance_rule_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_enforced_governance_rule,
            enforced_governance_rule_id=self.module.params.get(
                "enforced_governance_rule_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "enforced_governance_rule_id",
            "governance_rule_type",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_enforced_governance_rules, **optional_kwargs
        )


EnforcedGovernanceRuleFactsHelperCustom = get_custom_class(
    "EnforcedGovernanceRuleFactsHelperCustom"
)


class ResourceFactsHelper(
    EnforcedGovernanceRuleFactsHelperCustom, EnforcedGovernanceRuleFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            enforced_governance_rule_id=dict(aliases=["id"], type="str"),
            governance_rule_type=dict(
                type="str", choices=["QUOTA", "TAG", "ALLOWED_REGIONS"]
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="enforced_governance_rule",
        service_client_class=GovernanceRuleClient,
        namespace="governance_rules_control_plane",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(enforced_governance_rules=result)


if __name__ == "__main__":
    main()
