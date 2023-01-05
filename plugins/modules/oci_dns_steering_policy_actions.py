#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_dns_steering_policy_actions
short_description: Perform actions on a SteeringPolicy resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a SteeringPolicy resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a steering policy into a different compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    steering_policy_id:
        description:
            - The OCID of the target steering policy.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the steering policy should be moved.
        type: str
        required: true
    scope:
        description:
            - Specifies to operate only on resources that have a matching DNS scope.
        type: str
        choices:
            - "GLOBAL"
            - "PRIVATE"
    action:
        description:
            - The action to perform on the SteeringPolicy.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on steering_policy
  oci_dns_steering_policy_actions:
    # required
    steering_policy_id: "ocid1.steeringpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    scope: GLOBAL

"""

RETURN = """
steering_policy:
    description:
        - Details of the SteeringPolicy resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment containing the steering policy.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name for the steering policy. Does not have to be unique and can be changed.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        ttl:
            description:
                - The Time To Live (TTL) for responses from the steering policy, in seconds.
                  If not specified during creation, a value of 30 seconds will be used.
            returned: on success
            type: int
            sample: 56
        health_check_monitor_id:
            description:
                - The OCID of the health check monitor providing health data about the answers of the
                  steering policy. A steering policy answer with `rdata` matching a monitored endpoint
                  will use the health data of that endpoint. A steering policy answer with `rdata` not
                  matching any monitored endpoint will be assumed healthy.
                - "**Note:** To use the Health Check monitoring feature in a steering policy, a monitor
                  must be created using the Health Checks service first. For more information on how to
                  create a monitor, please see L(Managing Health
                  Checks,https://docs.cloud.oracle.com/iaas/Content/HealthChecks/Tasks/managinghealthchecks.htm)."
            returned: on success
            type: str
            sample: "ocid1.healthcheckmonitor.oc1..xxxxxxEXAMPLExxxxxx"
        template:
            description:
                - A set of predefined rules based on the desired purpose of the steering policy. Each
                  template utilizes Traffic Management's rules in a different order to produce the desired
                  results when answering DNS queries.
                - "**Example:** The `FAILOVER` template determines answers by filtering the policy's answers
                  using the `FILTER` rule first, then the following rules in succession: `HEALTH`, `PRIORITY`,
                  and `LIMIT`. This gives the domain dynamic failover capability."
                - "It is **strongly recommended** to use a template other than `CUSTOM` when creating
                  a steering policy."
                - All templates require the rule order to begin with an unconditional `FILTER` rule that keeps
                  answers contingent upon `answer.isDisabled != true`, except for `CUSTOM`. A defined
                  `HEALTH` rule must follow the `FILTER` rule if the policy references a `healthCheckMonitorId`.
                  The last rule of a template must must be a `LIMIT` rule. For more information about templates
                  and code examples, see L(Traffic Management API
                  Guide,https://docs.cloud.oracle.com/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm).
                - "**Template Types**"
                - "* `FAILOVER` - Uses health check information on your endpoints to determine which DNS answers
                  to serve. If an endpoint fails a health check, the answer for that endpoint will be removed
                  from the list of available answers until the endpoint is detected as healthy."
                - "* `LOAD_BALANCE` - Distributes web traffic to specified endpoints based on defined weights."
                - "* `ROUTE_BY_GEO` - Answers DNS queries based on the query's geographic location. For a list of geographic
                  locations to route by, see L(Traffic Management Geographic
                  Locations,https://docs.cloud.oracle.com/iaas/Content/TrafficManagement/Reference/trafficmanagementgeo.htm)."
                - "* `ROUTE_BY_ASN` - Answers DNS queries based on the query's originating ASN."
                - "* `ROUTE_BY_IP` - Answers DNS queries based on the query's IP address."
                - "* `CUSTOM` - Allows a customized configuration of rules."
            returned: on success
            type: str
            sample: FAILOVER
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "**Example:** `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "**Example:** `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        answers:
            description:
                - The set of all answers that can potentially issue from the steering policy.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - A user-friendly name for the answer, unique within the steering policy.
                          An answer's `name` property can be referenced in `answerCondition` properties
                          of rules using `answer.name`.
                        - "**Example:**"
                        - |
                          " \\"rules\\": [
                              {
                                \\"ruleType\\": \\"FILTER\\",
                                \\"defaultAnswerData\\":  [
                                  {
                                    \\"answerCondition\\": \\"answer.name == 'server 1'\\",
                                    \\"shouldKeep\\": true
                                  }
                                ]
                              }
                            ]"
                    returned: on success
                    type: str
                    sample: name_example
                rtype:
                    description:
                        - The type of DNS record, such as A or CNAME. Only A, AAAA, and CNAME are supported. For more
                          information, see L(Supported DNS Resource Record
                          Types,https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm).
                    returned: on success
                    type: str
                    sample: rtype_example
                rdata:
                    description:
                        - The record's data, as whitespace-delimited tokens in
                          type-specific presentation format. All RDATA is normalized and the
                          returned presentation of your RDATA may differ from its initial input.
                          For more information about RDATA, see L(Supported DNS Resource Record
                          Types,https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm).
                    returned: on success
                    type: str
                    sample: rdata_example
                pool:
                    description:
                        - "The freeform name of a group of one or more records in which this record is included,
                          such as \\"LAX data center\\". An answer's `pool` property can be referenced in `answerCondition`
                          properties of rules using `answer.pool`."
                        - "**Example:**"
                        - |
                          " \\"rules\\": [
                              {
                                \\"ruleType\\": \\"FILTER\\",
                                \\"defaultAnswerData\\":  [
                                  {
                                    \\"answerCondition\\": \\"answer.pool == 'US East Servers'\\",
                                    \\"shouldKeep\\": true
                                  }
                                ]
                              }
                            ]"
                    returned: on success
                    type: str
                    sample: pool_example
                is_disabled:
                    description:
                        - Set this property to `true` to indicate that the answer is administratively disabled,
                          such as when the corresponding server is down for maintenance. An answer's `isDisabled`
                          property can be referenced in `answerCondition` properties in rules using `answer.isDisabled`.
                        - |
                          "**Example:**
                            \\"rules\\": [
                              {
                                \\"ruleType\\": \\"FILTER\\",
                                \\"defaultAnswerData\\": [
                                  {
                                    \\"answerCondition\\": \\"answer.isDisabled != true\\",
                                    \\"shouldKeep\\": true
                                  }
                                ]
                              },"
                    returned: on success
                    type: bool
                    sample: true
        rules:
            description:
                - The series of rules that will be processed in sequence to reduce the pool of answers
                  to a response for any given request.
                - The first rule receives a shuffled list of all answers, and every other rule receives
                  the list of answers emitted by the one preceding it. The last rule populates the
                  response.
            returned: on success
            type: complex
            contains:
                default_count:
                    description:
                        - "Defines a default count if `cases` is not defined for the rule or a matching case does
                          not define `count`. `defaultCount` is **not** applied if `cases` is defined and there
                          are no matching cases. In this scenario, the next rule will be processed. If no rules
                          remain to be processed, the answer will be chosen from the remaining list of answers."
                    returned: on success
                    type: int
                    sample: 56
                description:
                    description:
                        - A user-defined description of the rule's purpose or behavior.
                    returned: on success
                    type: str
                    sample: description_example
                rule_type:
                    description:
                        - "The type of a rule determines its sorting/filtering behavior.
                          * `FILTER` - Filters the list of answers based on their defined boolean data. Answers remain
                            only if their `shouldKeep` value is `true`."
                        - "* `HEALTH` - Removes answers from the list if their `rdata` matches a target in the
                            health check monitor referenced by the steering policy and the target is reported down."
                        - "* `WEIGHTED` - Uses a number between 0 and 255 to determine how often an answer will be served
                            in relation to other answers. Anwers with a higher weight will be served more frequently."
                        - "* `PRIORITY` - Uses a defined rank value of answers to determine which answer to serve,
                            moving those with the lowest values to the beginning of the list without changing the
                            relative order of those with the same value. Answers can be given a value between `0` and `255`."
                        - "* `LIMIT` - Filters answers that are too far down the list. Parameter `defaultCount`
                            specifies how many answers to keep. **Example:** If `defaultCount` has a value of `2` and
                            there are five answers left, when the `LIMIT` rule is processed, only the first two answers
                            will remain in the list."
                    returned: on success
                    type: str
                    sample: FILTER
                cases:
                    description:
                        - An array of `caseConditions`. A rule may optionally include a sequence of cases defining alternate
                          configurations for how it should behave during processing for any given DNS query. When a rule has
                          no sequence of `cases`, it is always evaluated with the same configuration during processing. When
                          a rule has an empty sequence of `cases`, it is always ignored during processing. When a rule has a
                          non-empty sequence of `cases`, its behavior during processing is configured by the first matching
                          `case` in the sequence. When a rule has no matching cases the rule is ignored. A rule case with no
                          `caseCondition` always matches. A rule case with a `caseCondition` matches only when that expression
                          evaluates to true for the given query.
                    returned: on success
                    type: complex
                    contains:
                        case_condition:
                            description:
                                - "An expression that uses conditions at the time of a DNS query to indicate
                                  whether a case matches. Conditions may include the geographical location, IP
                                  subnet, or ASN the DNS query originated. **Example:** If you have an
                                  office that uses the subnet `192.0.2.0/24` you could use a `caseCondition`
                                  expression `query.client.address in ('192.0.2.0/24')` to define a case that
                                  matches queries from that office."
                            returned: on success
                            type: str
                            sample: case_condition_example
                        answer_data:
                            description:
                                - An array of `SteeringPolicyFilterAnswerData` objects.
                            returned: on success
                            type: complex
                            contains:
                                answer_condition:
                                    description:
                                        - An expression that is used to select a set of answers that match a condition. For example, answers with matching pool
                                          properties.
                                    returned: on success
                                    type: str
                                    sample: answer_condition_example
                                should_keep:
                                    description:
                                        - Keeps the answer only if the value is `true`.
                                    returned: on success
                                    type: bool
                                    sample: true
                                value:
                                    description:
                                        - The rank assigned to the set of answers that match the expression in `answerCondition`.
                                          Answers with the lowest values move to the beginning of the list without changing the
                                          relative order of those with the same value. Answers can be given a value between `0` and `255`.
                                    returned: on success
                                    type: int
                                    sample: 56
                        count:
                            description:
                                - "The number of answers allowed to remain after the limit rule has been processed, keeping only the
                                  first of the remaining answers in the list. Example: If the `count` property is set to `2` and
                                  four answers remain before the limit rule is processed, only the first two answers in the list will
                                  remain after the limit rule has been processed."
                            returned: on success
                            type: int
                            sample: 56
                default_answer_data:
                    description:
                        - Defines a default set of answer conditions and values that are applied to an answer when
                          `cases` is not defined for the rule, or a matching case does not have any matching
                          `answerCondition`s in its `answerData`. `defaultAnswerData` is not applied if `cases` is
                          defined and there are no matching cases. In this scenario, the next rule will be processed.
                    returned: on success
                    type: complex
                    contains:
                        answer_condition:
                            description:
                                - An expression that is used to select a set of answers that match a condition. For example, answers with matching pool
                                  properties.
                            returned: on success
                            type: str
                            sample: answer_condition_example
                        should_keep:
                            description:
                                - Keeps the answer only if the value is `true`.
                            returned: on success
                            type: bool
                            sample: true
                        value:
                            description:
                                - The rank assigned to the set of answers that match the expression in `answerCondition`.
                                  Answers with the lowest values move to the beginning of the list without changing the
                                  relative order of those with the same value. Answers can be given a value between `0` and `255`.
                            returned: on success
                            type: int
                            sample: 56
        _self:
            description:
                - The canonical absolute URL of the resource.
            returned: on success
            type: str
            sample: _self_example
        id:
            description:
                - The OCID of the resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the resource was created, expressed in RFC 3339 timestamp format.
                - "**Example:** `2016-07-22T17:23:59:60Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the resource.
            returned: on success
            type: str
            sample: ACTIVE
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "ttl": 56,
        "health_check_monitor_id": "ocid1.healthcheckmonitor.oc1..xxxxxxEXAMPLExxxxxx",
        "template": "FAILOVER",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "answers": [{
            "name": "name_example",
            "rtype": "rtype_example",
            "rdata": "rdata_example",
            "pool": "pool_example",
            "is_disabled": true
        }],
        "rules": [{
            "default_count": 56,
            "description": "description_example",
            "rule_type": "FILTER",
            "cases": [{
                "case_condition": "case_condition_example",
                "answer_data": [{
                    "answer_condition": "answer_condition_example",
                    "should_keep": true,
                    "value": 56
                }],
                "count": 56
            }],
            "default_answer_data": [{
                "answer_condition": "answer_condition_example",
                "should_keep": true,
                "value": 56
            }]
        }],
        "_self": "_self_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.dns import DnsClient
    from oci.dns.models import ChangeSteeringPolicyCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SteeringPolicyActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "steering_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("steering_policy_id")

    def get_get_fn(self):
        return self.client.get_steering_policy

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_steering_policy,
            steering_policy_id=self.module.params.get("steering_policy_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeSteeringPolicyCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_steering_policy_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                steering_policy_id=self.module.params.get("steering_policy_id"),
                change_steering_policy_compartment_details=action_details,
                scope=self.module.params.get("scope"),
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


SteeringPolicyActionsHelperCustom = get_custom_class(
    "SteeringPolicyActionsHelperCustom"
)


class ResourceHelper(SteeringPolicyActionsHelperCustom, SteeringPolicyActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            steering_policy_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            scope=dict(type="str", choices=["GLOBAL", "PRIVATE"]),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="steering_policy",
        service_client_class=DnsClient,
        namespace="dns",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
