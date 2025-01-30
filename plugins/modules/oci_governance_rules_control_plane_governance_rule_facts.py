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
module: oci_governance_rules_control_plane_governance_rule_facts
short_description: Fetches details about one or multiple GovernanceRule resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple GovernanceRule resources in Oracle Cloud Infrastructure
    - List governance rules. Either compartment id or governance rule id must be supplied.
      An optional lifecycle state, display name or a governance rule type can also be supplied.
    - If I(governance_rule_id) is specified, the details of a single GovernanceRule will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    governance_rule_id:
        description:
            - Unique governance rule identifier.
            - Required to get a specific governance_rule.
        type: str
        aliases: ["id"]
    lifecycle_state:
        description:
            - A filter to return only resources whose lifecycle state matches the given lifecycle state.
        type: str
        choices:
            - "ACTIVE"
            - "DELETED"
    display_name:
        description:
            - A filter to return only resources that match the entire name given.
        type: str
        aliases: ["name"]
    governance_rule_type:
        description:
            - A filter to return only resources that match the type given.
        type: str
        choices:
            - "QUOTA"
            - "TAG"
            - "ALLOWED_REGIONS"
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
- name: Get a specific governance_rule
  oci_governance_rules_control_plane_governance_rule_facts:
    # required
    governance_rule_id: "ocid1.governancerule.oc1..xxxxxxEXAMPLExxxxxx"

- name: List governance_rules
  oci_governance_rules_control_plane_governance_rule_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    governance_rule_id: "ocid1.governancerule.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: ACTIVE
    display_name: display_name_example
    governance_rule_type: QUOTA
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
governance_rules:
    description:
        - List of GovernanceRule resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - Description of the governance rule.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
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
        related_resource_id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the resource, which was used as a template
                  to create this governance rule.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the governance rule.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the root compartment containing the
                  governance rule.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Display name of the governance rule.
            returned: on success
            type: str
            sample: display_name_example
        type:
            description:
                - Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.
                - "Example: `QUOTA`"
            returned: on success
            type: str
            sample: QUOTA
        creation_option:
            description:
                - The type of option used to create the governance rule, could be one of TEMPLATE or CLONE.
                - "Example: `TEMPLATE`"
            returned: on success
            type: str
            sample: TEMPLATE
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
        lifecycle_state:
            description:
                - The current state of the governance rule.
            returned: on success
            type: str
            sample: ACTIVE
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
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
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "description": "description_example",
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
        "related_resource_id": "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "type": "QUOTA",
        "creation_option": "TEMPLATE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
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
    from oci.governance_rules_control_plane import GovernanceRuleClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GovernanceRuleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "governance_rule_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_governance_rule,
            governance_rule_id=self.module.params.get("governance_rule_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "governance_rule_id",
            "lifecycle_state",
            "display_name",
            "governance_rule_type",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_governance_rules, **optional_kwargs
        )


GovernanceRuleFactsHelperCustom = get_custom_class("GovernanceRuleFactsHelperCustom")


class ResourceFactsHelper(
    GovernanceRuleFactsHelperCustom, GovernanceRuleFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            governance_rule_id=dict(aliases=["id"], type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED"]),
            display_name=dict(aliases=["name"], type="str"),
            governance_rule_type=dict(
                type="str", choices=["QUOTA", "TAG", "ALLOWED_REGIONS"]
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="governance_rule",
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

    module.exit_json(governance_rules=result)


if __name__ == "__main__":
    main()
