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
module: oci_events_rule_actions
short_description: Perform actions on a Rule resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Rule resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a rule into a different compartment within the same tenancy. For information about moving
      resources between compartments, see L(Moving Resources to a Different
      Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9"
author: Oracle (@oracle)
options:
    rule_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this rule.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Rule.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on rule
  oci_events_rule_actions:
    rule_id: "ocid1.rule.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
rule:
    description:
        - Details of the Rule resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - A string that describes the rule. It does not have to be unique, and you can change it. Avoid entering
                  confidential information.
                - "Example: `\\"This rule sends a notification upon completion of DbaaS backup.\\"`"
            returned: on success
            type: string
            sample: This rule sends a notification upon completion of DbaaS backup.
        description:
            description:
                - A string that describes the details of the rule. It does not have to be unique, and you can change it. Avoid entering
                  confidential information.
            returned: on success
            type: string
            sample: description_example
        lifecycle_state:
            description:
                - The current state of the rule.
            returned: on success
            type: string
            sample: CREATING
        condition:
            description:
                - "A filter that specifies the event that will trigger actions associated with this rule. A few
                  important things to remember about filters:"
                - "* Fields not mentioned in the condition are ignored. You can create a valid filter that matches
                  all events with two curly brackets: `{}`"
                - " For more examples, see
                  L(Matching Events with Filters,https://docs.cloud.oracle.com/iaas/Content/Events/Concepts/filterevents.htm).
                  * For a condition with fields to match an event, the event must contain all the field names
                  listed in the condition. Field names must appear in the condition with the same nesting
                  structure used in the event."
                - " For a list of reference events, see
                  L(Services that Produce Events,https://docs.cloud.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm).
                  * Rules apply to events in the compartment in which you create them and any child compartments.
                  This means that a condition specified by a rule only matches events emitted from resources in
                  the compartment or any of its child compartments.
                  * Wildcard matching is supported with the asterisk (*) character."
                -   For examples of wildcard matching, see
                  L(Matching Events with Filters,https://docs.cloud.oracle.com/iaas/Content/Events/Concepts/filterevents.htm)
                - "Example: `\\\\\\"eventType\\\\\\": \\\\\\"com.oraclecloud.databaseservice.autonomous.database.backup.end\\\\\\"`"
            returned: on success
            type: string
            sample: condition_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to which this rule belongs.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        is_enabled:
            description:
                - Whether or not this rule is currently enabled.
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-
                  compatibility only.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        actions:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                actions:
                    description:
                        - A list of one or more Action objects.
                    returned: on success
                    type: complex
                    contains:
                        action_type:
                            description:
                                - The action to perform if the condition in the rule matches an event.
                                - "* **ONS:** Send to an Oracle Notification Service topic.
                                  * **OSS:** Send to a stream from Oracle Streaming Service.
                                  * **FAAS:** Send to an Oracle Functions Service endpoint."
                            returned: on success
                            type: string
                            sample: ONS
                        id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the action.
                            returned: on success
                            type: string
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        lifecycle_message:
                            description:
                                - A message generated by the Events service about the current state of this action.
                            returned: on success
                            type: string
                            sample: lifecycle_message_example
                        lifecycle_state:
                            description:
                                - The current state of the rule.
                            returned: on success
                            type: string
                            sample: CREATING
                        is_enabled:
                            description:
                                - Whether or not this action is currently enabled.
                                - "Example: `true`"
                            returned: on success
                            type: bool
                            sample: true
                        description:
                            description:
                                - A string that describes the details of the action. It does not have to be unique, and you can change it. Avoid entering
                                  confidential information.
                            returned: on success
                            type: string
                            sample: description_example
                        function_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a Function hosted by Oracle
                                  Functions Service.
                            returned: on success
                            type: string
                            sample: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
                        topic_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the topic to which messages are
                                  delivered.
                            returned: on success
                            type: string
                            sample: "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx"
                        stream_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stream to which messages are
                                  delivered.
                            returned: on success
                            type: string
                            sample: "ocid1.stream.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this rule.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time this rule was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2018-09-12T22:47:12.613Z`"
            returned: on success
            type: string
            sample: 2018-09-12T22:47:12.613Z
        lifecycle_message:
            description:
                - A message generated by the Events service about the current state of this rule.
            returned: on success
            type: string
            sample: lifecycle_message_example
    sample: {
        "display_name": "This rule sends a notification upon completion of DbaaS backup.",
        "description": "description_example",
        "lifecycle_state": "CREATING",
        "condition": "condition_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_enabled": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "actions": {
            "actions": [{
                "action_type": "ONS",
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "lifecycle_message": "lifecycle_message_example",
                "lifecycle_state": "CREATING",
                "is_enabled": true,
                "description": "description_example",
                "function_id": "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx",
                "topic_id": "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx",
                "stream_id": "ocid1.stream.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2018-09-12T22:47:12.613Z",
        "lifecycle_message": "lifecycle_message_example"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.events import EventsClient
    from oci.events.models import ChangeRuleCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RuleActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "rule_id"

    def get_module_resource_id(self):
        return self.module.params.get("rule_id")

    def get_get_fn(self):
        return self.client.get_rule

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rule, rule_id=self.module.params.get("rule_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeRuleCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_rule_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                rule_id=self.module.params.get("rule_id"),
                change_rule_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


RuleActionsHelperCustom = get_custom_class("RuleActionsHelperCustom")


class ResourceHelper(RuleActionsHelperCustom, RuleActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            rule_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="rule",
        service_client_class=EventsClient,
        namespace="events",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
