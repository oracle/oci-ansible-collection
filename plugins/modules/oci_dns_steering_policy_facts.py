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
module: oci_dns_steering_policy_facts
short_description: Fetches details about one or multiple SteeringPolicy resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SteeringPolicy resources in Oracle Cloud Infrastructure
    - Gets a list of all steering policies in the specified compartment.
    - If I(steering_policy_id) is specified, the details of a single SteeringPolicy will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    steering_policy_id:
        description:
            - The OCID of the target steering policy.
            - Required to get a specific steering_policy.
        type: str
        aliases: ["id"]
    if_modified_since:
        description:
            - The `If-Modified-Since` header field makes a GET or HEAD request method
              conditional on the selected representation's modification date being more
              recent than the date provided in the field-value.  Transfer of the
              selected representation's data is avoided if that data has not changed.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment the resource belongs to.
            - Required to list multiple steering_policies.
        type: str
    display_name:
        description:
            - The displayName of a resource.
        type: str
        aliases: ["name"]
    display_name_contains:
        description:
            - The partial displayName of a resource. Will match any resource whose name
              (case-insensitive) contains the provided value.
        type: str
    health_check_monitor_id:
        description:
            - Search by health check monitor OCID.
              Will match any resource whose health check monitor ID matches the provided value.
        type: str
    time_created_greater_than_or_equal_to:
        description:
            - An L(RFC 3339,https://www.ietf.org/rfc/rfc3339.txt) timestamp that states
              all returned resources were created on or after the indicated time.
        type: str
    time_created_less_than:
        description:
            - An L(RFC 3339,https://www.ietf.org/rfc/rfc3339.txt) timestamp that states
              all returned resources were created before the indicated time.
        type: str
    template:
        description:
            - Search by steering template type.
              Will match any resource whose template type matches the provided value.
        type: str
    lifecycle_state:
        description:
            - The state of a resource.
        type: str
        choices:
            - "ACTIVE"
            - "CREATING"
            - "DELETED"
            - "DELETING"
    sort_by:
        description:
            - The field by which to sort steering policies. If unspecified, defaults to `timeCreated`.
        type: str
        choices:
            - "displayName"
            - "timeCreated"
            - "template"
    sort_order:
        description:
            - The order to sort the resources.
        type: str
        choices:
            - "ASC"
            - "DESC"
    scope:
        description:
            - Specifies to operate only on resources that have a matching DNS scope.
        type: str
        choices:
            - "GLOBAL"
            - "PRIVATE"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific steering_policy
  oci_dns_steering_policy_facts:
    # required
    steering_policy_id: "ocid1.steeringpolicy.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    if_modified_since: if_modified_since_example
    scope: GLOBAL

- name: List steering_policies
  oci_dns_steering_policy_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    display_name_contains: display_name_contains_example
    health_check_monitor_id: "ocid1.healthcheckmonitor.oc1..xxxxxxEXAMPLExxxxxx"
    time_created_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_created_less_than: 2013-10-20T19:20:30+01:00
    template: template_example
    lifecycle_state: ACTIVE
    sort_by: displayName
    sort_order: ASC
    scope: GLOBAL

"""

RETURN = """
steering_policies:
    description:
        - List of SteeringPolicy resources
    returned: on success
    type: complex
    contains:
        answers:
            description:
                - The set of all answers that can potentially issue from the steering policy.
                - Returned for get operation
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
                - Returned for get operation
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
                                  expression `query.client.subnet in ('192.0.2.0/24')` to define a case that
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
    sample: [{
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
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "ttl": 56,
        "health_check_monitor_id": "ocid1.healthcheckmonitor.oc1..xxxxxxEXAMPLExxxxxx",
        "template": "FAILOVER",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "_self": "_self_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.dns import DnsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SteeringPolicyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "steering_policy_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "if_modified_since",
            "scope",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_steering_policy,
            steering_policy_id=self.module.params.get("steering_policy_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "display_name_contains",
            "health_check_monitor_id",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
            "template",
            "lifecycle_state",
            "sort_by",
            "sort_order",
            "scope",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_steering_policies,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SteeringPolicyFactsHelperCustom = get_custom_class("SteeringPolicyFactsHelperCustom")


class ResourceFactsHelper(
    SteeringPolicyFactsHelperCustom, SteeringPolicyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            steering_policy_id=dict(aliases=["id"], type="str"),
            if_modified_since=dict(type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            display_name_contains=dict(type="str"),
            health_check_monitor_id=dict(type="str"),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
            template=dict(type="str"),
            lifecycle_state=dict(
                type="str", choices=["ACTIVE", "CREATING", "DELETED", "DELETING"]
            ),
            sort_by=dict(
                type="str", choices=["displayName", "timeCreated", "template"]
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            scope=dict(type="str", choices=["GLOBAL", "PRIVATE"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="steering_policy",
        service_client_class=DnsClient,
        namespace="dns",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(steering_policies=result)


if __name__ == "__main__":
    main()
