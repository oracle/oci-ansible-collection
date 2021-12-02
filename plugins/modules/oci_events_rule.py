#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_events_rule
short_description: Manage a Rule resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Rule resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new rule.
    - "This resource has the following action operations in the M(oracle.oci.oci_events_rule_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - A string that describes the rule. It does not have to be unique, and you can change it. Avoid entering
              confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A string that describes the details of the rule. It does not have to be unique, and you can change it. Avoid entering
              confidential information.
            - This parameter is updatable.
        type: str
    is_enabled:
        description:
            - Whether or not this rule is currently enabled.
            - "Example: `true`"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: bool
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
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to which this rule belongs.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    actions:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            actions:
                description:
                    - A list of one or more ActionDetails objects.
                type: list
                elements: dict
                required: true
                suboptions:
                    action_type:
                        description:
                            - The action to perform if the condition in the rule matches an event.
                            - "* **ONS:** Send to an Oracle Notification Service topic.
                              * **OSS:** Send to a stream from Oracle Streaming Service.
                              * **FAAS:** Send to an Oracle Functions Service endpoint."
                        type: str
                        choices:
                            - "OSS"
                            - "FAAS"
                            - "ONS"
                        required: true
                    is_enabled:
                        description:
                            - Whether or not this action is currently enabled.
                            - "Example: `true`"
                        type: bool
                        required: true
                    description:
                        description:
                            - A string that describes the details of the action. It does not have to be unique, and you can change it. Avoid entering
                              confidential information.
                        type: str
                    stream_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stream to which messages are
                              delivered.
                            - Required when action_type is 'OSS'
                        type: str
                    function_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a Function hosted by Oracle Functions
                              Service.
                            - Applicable when action_type is 'FAAS'
                        type: str
                    topic_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the topic to which messages are
                              delivered.
                            - Applicable when action_type is 'ONS'
                        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-compatibility
              only.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    rule_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this rule.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Rule.
            - Use I(state=present) to create or update a Rule.
            - Use I(state=absent) to delete a Rule.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create rule
  oci_events_rule:
    # required
    display_name: example_rule
    is_enabled: true
    condition: {"eventType": "com.oraclecloud.databaseservice.autonomous.database.backup.end"}
    compartment_id: "ocid.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    actions:
      # required
      actions:
      - # required
        action_type: ONS
        is_enabled: true
        stream_id: "ocid1.stream.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        description: description_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update rule
  oci_events_rule:
    # required
    rule_id: "ocid1.rule.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: example_rule
    description: description_example
    is_enabled: true
    condition: {"eventType": "com.oraclecloud.databaseservice.autonomous.database.backup.end"}
    actions:
      # required
      actions:
      - # required
        action_type: ONS
        is_enabled: true
        stream_id: "ocid1.stream.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update rule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_events_rule:
    # required
    display_name: example_rule
    compartment_id: "ocid.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    is_enabled: true
    condition: {"eventType": "com.oraclecloud.databaseservice.autonomous.database.backup.end"}
    actions:
      # required
      actions:
      - # required
        action_type: ONS
        is_enabled: true
        stream_id: "ocid1.stream.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete rule
  oci_events_rule:
    # required
    rule_id: "ocid1.rule.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete rule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_events_rule:
    # required
    display_name: example_rule
    compartment_id: "ocid.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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
            type: str
            sample: This rule sends a notification upon completion of DbaaS backup.
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
                        stream_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stream to which messages are
                                  delivered.
                            returned: on success
                            type: str
                            sample: "ocid1.stream.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this rule.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time this rule was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2018-09-12T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2018-09-12T22:47:12.613Z"
        lifecycle_message:
            description:
                - A message generated by the Events service about the current state of this rule.
            returned: on success
            type: str
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.events import EventsClient
    from oci.events.models import CreateRuleDetails
    from oci.events.models import UpdateRuleDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RuleHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "rule_id"

    def get_module_resource_id(self):
        return self.module.params.get("rule_id")

    def get_get_fn(self):
        return self.client.get_rule

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rule, rule_id=self.module.params.get("rule_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_rules, **kwargs)

    def get_create_model_class(self):
        return CreateRuleDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(create_rule_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateRuleDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                rule_id=self.module.params.get("rule_id"),
                update_rule_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(rule_id=self.module.params.get("rule_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


RuleHelperCustom = get_custom_class("RuleHelperCustom")


class ResourceHelper(RuleHelperCustom, RuleHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            is_enabled=dict(type="bool"),
            condition=dict(type="str"),
            compartment_id=dict(type="str"),
            actions=dict(
                type="dict",
                options=dict(
                    actions=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            action_type=dict(
                                type="str",
                                required=True,
                                choices=["OSS", "FAAS", "ONS"],
                            ),
                            is_enabled=dict(type="bool", required=True),
                            description=dict(type="str"),
                            stream_id=dict(type="str"),
                            function_id=dict(type="str"),
                            topic_id=dict(type="str"),
                        ),
                    )
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            rule_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
