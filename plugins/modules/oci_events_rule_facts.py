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
module: oci_events_rule_facts
short_description: Fetches details about one or multiple Rule resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Rule resources in Oracle Cloud Infrastructure
    - Lists rules for this compartment.
    - If I(rule_id) is specified, the details of a single Rule will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    rule_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this rule.
            - Required to get a specific rule.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to which this rule belongs.
            - Required to list multiple rules.
        type: str
    lifecycle_state:
        description:
            - A filter to return only rules that match the lifecycle state in this parameter.
            - "Example: `Creating`"
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only rules with descriptions that match the displayName string
              in this parameter.
            - "Example: `\\"This rule sends a notification upon completion of DbaaS backup.\\"`"
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - Specifies the attribute with which to sort the rules.
            - "Default: `timeCreated`"
            - "* **TIME_CREATED:** Sorts by timeCreated.
              * **DISPLAY_NAME:** Sorts by displayName.
              * **ID:** Sorts by id."
        type: str
        choices:
            - "TIME_CREATED"
            - "ID"
            - "DISPLAY_NAME"
    sort_order:
        description:
            - Specifies sort order.
            - "* **ASC:** Ascending sort order.
              * **DESC:** Descending sort order."
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific rule
  oci_events_rule_facts:
    # required
    rule_id: "ocid1.rule.oc1..xxxxxxEXAMPLExxxxxx"

- name: List rules
  oci_events_rule_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_by: TIME_CREATED
    sort_order: ASC

"""

RETURN = """
rules:
    description:
        - List of Rule resources
    returned: on success
    type: complex
    contains:
        actions:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                actions:
                    description:
                        - A list of one or more Action objects.
                    returned: on success
                    type: complex
                    contains:
                        function_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a Function hosted by Oracle
                                  Functions Service.
                            returned: on success
                            type: str
                            sample: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
                        topic_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the topic to which messages are
                                  delivered.
                            returned: on success
                            type: str
                            sample: "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx"
                        action_type:
                            description:
                                - The action to perform if the condition in the rule matches an event.
                                - "* **ONS:** Send to an Oracle Notification Service topic.
                                  * **OSS:** Send to a stream from Oracle Streaming Service.
                                  * **FAAS:** Send to an Oracle Functions Service endpoint."
                            returned: on success
                            type: str
                            sample: ONS
                        id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the action.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        lifecycle_message:
                            description:
                                - A message generated by the Events service about the current state of this action.
                            returned: on success
                            type: str
                            sample: lifecycle_message_example
                        lifecycle_state:
                            description:
                                - The current state of the rule.
                            returned: on success
                            type: str
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
                            type: str
                            sample: description_example
                        stream_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stream to which messages are
                                  delivered.
                            returned: on success
                            type: str
                            sample: "ocid1.stream.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_message:
            description:
                - A message generated by the Events service about the current state of this rule.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecycle_message_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this rule.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A string that describes the rule. It does not have to be unique, and you can change it. Avoid entering
                  confidential information.
                - "Example: `\\"This rule sends a notification upon completion of DbaaS backup.\\"`"
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A string that describes the details of the rule. It does not have to be unique, and you can change it. Avoid entering
                  confidential information.
            returned: on success
            type: str
            sample: description_example
        lifecycle_state:
            description:
                - The current state of the rule.
            returned: on success
            type: str
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
            type: str
            sample: condition_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to which this rule belongs.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        is_enabled:
            description:
                - Whether or not this rule is currently enabled.
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The time this rule was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2018-09-12T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
    sample: [{
        "actions": {
            "actions": [{
                "function_id": "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx",
                "topic_id": "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx",
                "action_type": "ONS",
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "lifecycle_message": "lifecycle_message_example",
                "lifecycle_state": "CREATING",
                "is_enabled": true,
                "description": "description_example",
                "stream_id": "ocid1.stream.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        },
        "lifecycle_message": "lifecycle_message_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "lifecycle_state": "CREATING",
        "condition": "condition_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_enabled": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.events import EventsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RuleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "rule_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rule, rule_id=self.module.params.get("rule_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_rules,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


RuleFactsHelperCustom = get_custom_class("RuleFactsHelperCustom")


class ResourceFactsHelper(RuleFactsHelperCustom, RuleFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            rule_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIME_CREATED", "ID", "DISPLAY_NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="rule",
        service_client_class=EventsClient,
        namespace="events",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(rules=result)


if __name__ == "__main__":
    main()
