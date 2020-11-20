#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_dns_steering_policy
short_description: Manage a SteeringPolicy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a SteeringPolicy resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new steering policy in the specified compartment. For more information on
      creating policies with templates, see L(Traffic Management API
      Guide,https://docs.cloud.oracle.com/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm).
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment containing the steering policy.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - A user-friendly name for the steering policy. Does not have to be unique and can be changed.
              Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    ttl:
        description:
            - The Time To Live (TTL) for responses from the steering policy, in seconds.
              If not specified during creation, a value of 30 seconds will be used.
            - This parameter is updatable.
        type: int
    health_check_monitor_id:
        description:
            - The OCID of the health check monitor providing health data about the answers of the
              steering policy. A steering policy answer with `rdata` matching a monitored endpoint
              will use the health data of that endpoint. A steering policy answer with `rdata` not
              matching any monitored endpoint will be assumed healthy.
            - "**Note:** To use the Health Check monitoring feature in a steering policy, a monitor
              must be created using the Health Checks service first. For more information on how to
              create a monitor, please see L(Managing Health Checks,https://docs.cloud.oracle.com/iaas/Content/HealthChecks/Tasks/managinghealthchecks.htm)."
            - This parameter is updatable.
        type: str
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
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "FAILOVER"
            - "LOAD_BALANCE"
            - "ROUTE_BY_GEO"
            - "ROUTE_BY_ASN"
            - "ROUTE_BY_IP"
            - "CUSTOM"
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "**Example:** `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "**Example:** `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    answers:
        description:
            - The set of all answers that can potentially issue from the steering policy.
            - This parameter is updatable.
        type: list
        suboptions:
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
                type: str
                required: true
            rtype:
                description:
                    - The type of DNS record, such as A or CNAME. Only A, AAAA, and CNAME are supported. For more
                      information, see L(Supported DNS Resource Record Types,https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm).
                type: str
                required: true
            rdata:
                description:
                    - The record's data, as whitespace-delimited tokens in
                      type-specific presentation format. All RDATA is normalized and the
                      returned presentation of your RDATA may differ from its initial input.
                      For more information about RDATA, see L(Supported DNS Resource Record
                      Types,https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm).
                type: str
                required: true
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
                type: str
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
                type: bool
    rules:
        description:
            - The series of rules that will be processed in sequence to reduce the pool of answers
              to a response for any given request.
            - The first rule receives a shuffled list of all answers, and every other rule receives
              the list of answers emitted by the one preceding it. The last rule populates the
              response.
            - This parameter is updatable.
        type: list
        suboptions:
            description:
                description:
                    - A user-defined description of the rule's purpose or behavior.
                type: str
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
                type: str
                choices:
                    - "FILTER"
                    - "WEIGHTED"
                    - "LIMIT"
                    - "HEALTH"
                    - "PRIORITY"
                required: true
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
                type: list
                suboptions:
                    case_condition:
                        description:
                            - "An expression that uses conditions at the time of a DNS query to indicate
                              whether a case matches. Conditions may include the geographical location, IP
                              subnet, or ASN the DNS query originated. **Example:** If you have an
                              office that uses the subnet `192.0.2.0/24` you could use a `caseCondition`
                              expression `query.client.subnet in ('192.0.2.0/24')` to define a case that
                              matches queries from that office."
                        type: str
                    answer_data:
                        description:
                            - An array of `SteeringPolicyFilterAnswerData` objects.
                            - Applicable when rule_type is one of ['FILTER', 'WEIGHTED', 'PRIORITY']
                        type: list
                        suboptions:
                            answer_condition:
                                description:
                                    - An expression that is used to select a set of answers that match a condition. For example, answers with matching pool
                                      properties.
                                    - Applicable when rule_type is one of ['FILTER', 'WEIGHTED', 'PRIORITY']
                                type: str
                            should_keep:
                                description:
                                    - Keeps the answer only if the value is `true`.
                                    - Applicable when rule_type is 'FILTER'
                                type: bool
                            value:
                                description:
                                    - The weight assigned to the set of selected answers. Answers with a higher weight will be served
                                      more frequently. Answers can be given a value between `0` and `255`.
                                    - Required when rule_type is one of ['WEIGHTED', 'PRIORITY']
                                type: int
                    count:
                        description:
                            - "The number of answers allowed to remain after the limit rule has been processed, keeping only the
                              first of the remaining answers in the list. Example: If the `count` property is set to `2` and
                              four answers remain before the limit rule is processed, only the first two answers in the list will
                              remain after the limit rule has been processed."
                            - Required when rule_type is 'LIMIT'
                        type: int
            default_answer_data:
                description:
                    - Defines a default set of answer conditions and values that are applied to an answer when
                      `cases` is not defined for the rule, or a matching case does not have any matching
                      `answerCondition`s in its `answerData`. `defaultAnswerData` is not applied if `cases` is
                      defined and there are no matching cases. In this scenario, the next rule will be processed.
                    - Applicable when rule_type is one of ['FILTER', 'WEIGHTED', 'PRIORITY']
                type: list
                suboptions:
                    answer_condition:
                        description:
                            - An expression that is used to select a set of answers that match a condition. For example, answers with matching pool properties.
                            - Applicable when rule_type is one of ['FILTER', 'WEIGHTED', 'PRIORITY']
                        type: str
                    should_keep:
                        description:
                            - Keeps the answer only if the value is `true`.
                            - Applicable when rule_type is 'FILTER'
                        type: bool
                    value:
                        description:
                            - The weight assigned to the set of selected answers. Answers with a higher weight will be served
                              more frequently. Answers can be given a value between `0` and `255`.
                            - Required when rule_type is one of ['WEIGHTED', 'PRIORITY']
                        type: int
            default_count:
                description:
                    - "Defines a default count if `cases` is not defined for the rule or a matching case does
                      not define `count`. `defaultCount` is **not** applied if `cases` is defined and there
                      are no matching cases. In this scenario, the next rule will be processed. If no rules
                      remain to be processed, the answer will be chosen from the remaining list of answers."
                    - Applicable when rule_type is 'LIMIT'
                type: int
    scope:
        description:
            - Specifies to operate only on resources that have a matching DNS scope.
            - This parameter is updatable.
        type: str
        choices:
            - "GLOBAL"
            - "PRIVATE"
    steering_policy_id:
        description:
            - The OCID of the target steering policy.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    if_unmodified_since:
        description:
            - The `If-Unmodified-Since` header field makes the request method
              conditional on the selected representation's last modification date being
              earlier than or equal to the date provided in the field-value.  This
              field accomplishes the same purpose as If-Match for cases where the user
              agent does not have an entity-tag for the representation.
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the SteeringPolicy.
            - Use I(state=present) to create or update a SteeringPolicy.
            - Use I(state=absent) to delete a SteeringPolicy.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create steering_policy
  oci_dns_steering_policy:
    compartment_id: ocid1.compartment.oc1..
    display_name: failover between endpoints
    ttl: 30
    health_check_monitor_id: ocid1.httpmonitor.oc1..
    template: FAILOVER
    answers:
    - name: server-primary
      rtype: A
      rdata: 192.0.2.0
      pool: primary
    - name: server-secondary
      rtype: A
      rdata: 192.0.4.6
      pool: secondary
    rules:
    - rule_type: FILTER
      default_answer_data:
      - answer_condition: answer.isDisabled != true
        should_keep: true
    - rule_type: HEALTH
    - rule_type: PRIORITY
      default_answer_data:
      - answer_condition: answer.pool == 'primary'
        value: 1
      - answer_condition: answer.pool == 'secondary'
        value: 99
    - rule_type: LIMIT
      default_count: 1

- name: Update steering_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_dns_steering_policy:
    compartment_id: ocid1.compartment.oc1..
    display_name: LA data center failover
    ttl: 30
    health_check_monitor_id: ocid1.httpmonitor.oc1..
    template: FAILOVER
    answers:
    - name: server-primary
      rtype: A
      rdata: 192.0.2.0
      pool: primary
    - name: server-secondary
      rtype: A
      rdata: 192.0.4.1
      pool: secondary
    rules:
    - rule_type: FILTER
      default_answer_data:
      - answer_condition: answer.isDisabled != true
        should_keep: true
    - rule_type: HEALTH
    - rule_type: PRIORITY
      default_answer_data:
      - answer_condition: answer.pool == 'primary'
        value: 1
      - answer_condition: answer.pool == 'secondary'
        value: 99
    - rule_type: LIMIT
      default_count: 1

- name: Update steering_policy
  oci_dns_steering_policy:
    steering_policy_id: ocid1.steeringpolicy.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete steering_policy
  oci_dns_steering_policy:
    steering_policy_id: ocid1.steeringpolicy.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete steering_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_dns_steering_policy:
    compartment_id: ocid1.compartment.oc1..
    display_name: failover between endpoints
    state: absent

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
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - A user-friendly name for the steering policy. Does not have to be unique and can be changed.
                  Avoid entering confidential information.
            returned: on success
            type: string
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
            type: string
            sample: ocid1.healthcheckmonitor.oc1..xxxxxxEXAMPLExxxxxx
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
            type: string
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
                    type: string
                    sample: name_example
                rtype:
                    description:
                        - The type of DNS record, such as A or CNAME. Only A, AAAA, and CNAME are supported. For more
                          information, see L(Supported DNS Resource Record
                          Types,https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm).
                    returned: on success
                    type: string
                    sample: rtype_example
                rdata:
                    description:
                        - The record's data, as whitespace-delimited tokens in
                          type-specific presentation format. All RDATA is normalized and the
                          returned presentation of your RDATA may differ from its initial input.
                          For more information about RDATA, see L(Supported DNS Resource Record
                          Types,https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm).
                    returned: on success
                    type: string
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
                    type: string
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
                description:
                    description:
                        - A user-defined description of the rule's purpose or behavior.
                    returned: on success
                    type: string
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
                    type: string
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
                            type: string
                            sample: query.client.address in (subnet '198.51.100.0/24')
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
                                    type: string
                                    sample: answer.pool == 'A'
                                should_keep:
                                    description:
                                        - Keeps the answer only if the value is `true`.
                                    returned: on success
                                    type: bool
                                    sample: true
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
                            type: string
                            sample: answer.pool == 'A'
                        should_keep:
                            description:
                                - Keeps the answer only if the value is `true`.
                            returned: on success
                            type: bool
                            sample: true
                default_count:
                    description:
                        - "Defines a default count if `cases` is not defined for the rule or a matching case does
                          not define `count`. `defaultCount` is **not** applied if `cases` is defined and there
                          are no matching cases. In this scenario, the next rule will be processed. If no rules
                          remain to be processed, the answer will be chosen from the remaining list of answers."
                    returned: on success
                    type: int
                    sample: 56
        _self:
            description:
                - The canonical absolute URL of the resource.
            returned: on success
            type: string
            sample: _self_example
        id:
            description:
                - The OCID of the resource.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The date and time the resource was created, expressed in RFC 3339 timestamp format.
                - "**Example:** `2016-07-22T17:23:59:60Z`"
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the resource.
            returned: on success
            type: string
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
            "description": "description_example",
            "rule_type": "FILTER",
            "cases": [{
                "case_condition": "query.client.address in (subnet '198.51.100.0/24')",
                "answer_data": [{
                    "answer_condition": "answer.pool == 'A'",
                    "should_keep": true
                }]
            }],
            "default_answer_data": [{
                "answer_condition": "answer.pool == 'A'",
                "should_keep": true
            }],
            "default_count": 56
        }],
        "_self": "_self_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE"
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
    from oci.dns import DnsClient
    from oci.dns.models import CreateSteeringPolicyDetails
    from oci.dns.models import UpdateSteeringPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SteeringPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name", "scope"]
            if self._use_name_as_identifier()
            else ["display_name", "health_check_monitor_id", "template", "scope"]
        )

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
        return oci_common_utils.list_all_resources(
            self.client.list_steering_policies, **kwargs
        )

    def get_create_model_class(self):
        return CreateSteeringPolicyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_steering_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_steering_policy_details=create_details,
                scope=self.module.params.get("scope"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateSteeringPolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_steering_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                steering_policy_id=self.module.params.get("steering_policy_id"),
                update_steering_policy_details=update_details,
                if_unmodified_since=self.module.params.get("if_unmodified_since"),
                scope=self.module.params.get("scope"),
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
            call_fn=self.client.delete_steering_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                steering_policy_id=self.module.params.get("steering_policy_id"),
                if_unmodified_since=self.module.params.get("if_unmodified_since"),
                scope=self.module.params.get("scope"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


SteeringPolicyHelperCustom = get_custom_class("SteeringPolicyHelperCustom")


class ResourceHelper(SteeringPolicyHelperCustom, SteeringPolicyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            ttl=dict(type="int"),
            health_check_monitor_id=dict(type="str"),
            template=dict(
                type="str",
                choices=[
                    "FAILOVER",
                    "LOAD_BALANCE",
                    "ROUTE_BY_GEO",
                    "ROUTE_BY_ASN",
                    "ROUTE_BY_IP",
                    "CUSTOM",
                ],
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            answers=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    rtype=dict(type="str", required=True),
                    rdata=dict(type="str", required=True),
                    pool=dict(type="str"),
                    is_disabled=dict(type="bool"),
                ),
            ),
            rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    description=dict(type="str"),
                    rule_type=dict(
                        type="str",
                        required=True,
                        choices=["FILTER", "WEIGHTED", "LIMIT", "HEALTH", "PRIORITY"],
                    ),
                    cases=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            case_condition=dict(type="str"),
                            answer_data=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    answer_condition=dict(type="str"),
                                    should_keep=dict(type="bool"),
                                    value=dict(type="int"),
                                ),
                            ),
                            count=dict(type="int"),
                        ),
                    ),
                    default_answer_data=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            answer_condition=dict(type="str"),
                            should_keep=dict(type="bool"),
                            value=dict(type="int"),
                        ),
                    ),
                    default_count=dict(type="int"),
                ),
            ),
            scope=dict(type="str", choices=["GLOBAL", "PRIVATE"]),
            steering_policy_id=dict(aliases=["id"], type="str"),
            if_unmodified_since=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="steering_policy",
        service_client_class=DnsClient,
        namespace="dns",
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
