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
module: oci_waf_web_app_firewall_policy_facts
short_description: Fetches details about one or multiple WebAppFirewallPolicy resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple WebAppFirewallPolicy resources in Oracle Cloud Infrastructure
    - Gets a list of all WebAppFirewallPolicies in a compartment.
    - If I(web_app_firewall_policy_id) is specified, the details of a single WebAppFirewallPolicy will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    web_app_firewall_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WebAppFirewallPolicy.
            - Required to get a specific web_app_firewall_policy.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
            - Required to list multiple web_app_firewall_policies.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycleState.
        type: list
        elements: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
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
            - The field to sort by. Only one sort order may be provided.
              Default order for timeCreated is descending.
              Default order for displayName is ascending.
              If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific web_app_firewall_policy
  oci_waf_web_app_firewall_policy_facts:
    # required
    web_app_firewall_policy_id: "ocid1.webappfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"

- name: List web_app_firewall_policies
  oci_waf_web_app_firewall_policy_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: [ "lifecycle_state_example" ]
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
web_app_firewall_policies:
    description:
        - List of WebAppFirewallPolicy resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WebAppFirewallPolicy.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - WebAppFirewallPolicy display name, can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the WebAppFirewallPolicy was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the WebAppFirewallPolicy was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the WebAppFirewallPolicy.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a resource in FAILED state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        actions:
            description:
                - Predefined actions for use in multiple different rules. Not all actions are supported in every module.
                  Some actions terminate further execution of modules and rules in a module and some do not.
                  Actions names must be unique within this array.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - "* **CHECK** is a non-terminating action that does not stop the execution of rules in current module,
                            just emits a log message documenting result of rule execution."
                        - "* **ALLOW** is a non-terminating action which upon matching rule skips all remaining rules in the current module."
                        - "* **RETURN_HTTP_RESPONSE** is a terminating action which is executed immediately, returns a defined HTTP response."
                    returned: on success
                    type: str
                    sample: CHECK
                name:
                    description:
                        - Action name. Can be used to reference the action.
                    returned: on success
                    type: str
                    sample: name_example
                code:
                    description:
                        - Response code.
                        - "The following response codes are valid values for this property:"
                        - "* 2xx"
                        -   200 OK
                            201 Created
                            202 Accepted
                            206 Partial Content
                        - "* 3xx"
                        -   300 Multiple Choices
                            301 Moved Permanently
                            302 Found
                            303 See Other
                            307 Temporary Redirect
                        - "* 4xx"
                        -   400 Bad Request
                            401 Unauthorized
                            403 Forbidden
                            404 Not Found
                            405 Method Not Allowed
                            408 Request Timeout
                            409 Conflict
                            411 Length Required
                            412 Precondition Failed
                            413 Payload Too Large
                            414 URI Too Long
                            415 Unsupported Media Type
                            416 Range Not Satisfiable
                            422 Unprocessable Entity
                            494 Request Header Too Large
                            495 Cert Error
                            496 No Cert
                            497 HTTP to HTTPS
                        - "* 5xx"
                        -   500 Internal Server Error
                            501 Not Implemented
                            502 Bad Gateway
                            503 Service Unavailable
                            504 Gateway Timeout
                            507 Insufficient Storage
                        - "Example: `200`"
                    returned: on success
                    type: int
                    sample: 56
                headers:
                    description:
                        - Adds headers defined in this array for HTTP response.
                        - "Hop-by-hop headers are not allowed to be set:"
                        - "* Connection
                          * Keep-Alive
                          * Proxy-Authenticate
                          * Proxy-Authorization
                          * TE
                          * Trailer
                          * Transfer-Encoding
                          * Upgrade"
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The name of the header field.
                            returned: on success
                            type: str
                            sample: name_example
                        value:
                            description:
                                - The value of the header field.
                            returned: on success
                            type: str
                            sample: value_example
                body:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - Type of HttpResponseBody.
                            returned: on success
                            type: str
                            sample: STATIC_TEXT
                        text:
                            description:
                                - Static response body text.
                            returned: on success
                            type: str
                            sample: text_example
        request_access_control:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                default_action_name:
                    description:
                        - "References an default Action to take if no AccessControlRule was matched. Allowed action types:"
                        - "* **ALLOW** continues execution of other modules and their rules."
                        - "* **RETURN_HTTP_RESPONSE** terminates further execution of modules and rules and returns defined HTTP response."
                    returned: on success
                    type: str
                    sample: default_action_name_example
                rules:
                    description:
                        - Ordered list of AccessControlRules. Rules are executed in order of appearance in this array.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - Type of WebAppFirewallPolicyRule.
                            returned: on success
                            type: str
                            sample: ACCESS_CONTROL
                        name:
                            description:
                                - Rule name. Must be unique within the module.
                            returned: on success
                            type: str
                            sample: name_example
                        condition_language:
                            description:
                                - "The language used to parse condition from field `condition`. Available languages:"
                                - "* **JMESPATH** an extended JMESPath language syntax."
                            returned: on success
                            type: str
                            sample: JMESPATH
                        condition:
                            description:
                                - An expression that determines whether or not the rule action should be executed.
                            returned: on success
                            type: str
                            sample: condition_example
                        action_name:
                            description:
                                - References action by name from actions defined in WebAppFirewallPolicy.
                            returned: on success
                            type: str
                            sample: action_name_example
        request_rate_limiting:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                rules:
                    description:
                        - Ordered list of RequestRateLimitingRules. Rules are executed in order of appearance in this array.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - Type of WebAppFirewallPolicyRule.
                            returned: on success
                            type: str
                            sample: ACCESS_CONTROL
                        name:
                            description:
                                - Rule name. Must be unique within the module.
                            returned: on success
                            type: str
                            sample: name_example
                        condition_language:
                            description:
                                - "The language used to parse condition from field `condition`. Available languages:"
                                - "* **JMESPATH** an extended JMESPath language syntax."
                            returned: on success
                            type: str
                            sample: JMESPATH
                        condition:
                            description:
                                - An expression that determines whether or not the rule action should be executed.
                            returned: on success
                            type: str
                            sample: condition_example
                        action_name:
                            description:
                                - References action by name from actions defined in WebAppFirewallPolicy.
                            returned: on success
                            type: str
                            sample: action_name_example
                        configurations:
                            description:
                                - Rate Limiting Configurations.
                                  Each configuration counts requests towards its own `requestsLimit`.
                            returned: on success
                            type: complex
                            contains:
                                period_in_seconds:
                                    description:
                                        - Evaluation period in seconds.
                                    returned: on success
                                    type: int
                                    sample: 56
                                requests_limit:
                                    description:
                                        - Requests allowed per evaluation period.
                                    returned: on success
                                    type: int
                                    sample: 56
                                action_duration_in_seconds:
                                    description:
                                        - Duration of block action application in seconds when `requestsLimit` is reached. Optional and can be 0 (no block
                                          duration).
                                    returned: on success
                                    type: int
                                    sample: 56
        request_protection:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                rules:
                    description:
                        - Ordered list of ProtectionRules. Rules are executed in order of appearance in this array.
                          ProtectionRules in this array can only use protection cCapabilities of REQUEST_PROTECTION_CAPABILITY type.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - Type of WebAppFirewallPolicyRule.
                            returned: on success
                            type: str
                            sample: ACCESS_CONTROL
                        name:
                            description:
                                - Rule name. Must be unique within the module.
                            returned: on success
                            type: str
                            sample: name_example
                        condition_language:
                            description:
                                - "The language used to parse condition from field `condition`. Available languages:"
                                - "* **JMESPATH** an extended JMESPath language syntax."
                            returned: on success
                            type: str
                            sample: JMESPATH
                        condition:
                            description:
                                - An expression that determines whether or not the rule action should be executed.
                            returned: on success
                            type: str
                            sample: condition_example
                        action_name:
                            description:
                                - References action by name from actions defined in WebAppFirewallPolicy.
                            returned: on success
                            type: str
                            sample: action_name_example
                        protection_capabilities:
                            description:
                                - An ordered list that references OCI-managed protection capabilities.
                                  Referenced protection capabilities are executed in order of appearance.
                                  The array cannot contain entries with the same pair of capability key and version more than once.
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - Unique key of referenced protection capability.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                version:
                                    description:
                                        - Version of referenced protection capability.
                                    returned: on success
                                    type: int
                                    sample: 56
                                exclusions:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        request_cookies:
                                            description:
                                                - "List of HTTP request cookie values (by cookie name) to exclude from inspecting.
                                                  Example: If we have cookie 'cookieName=cookieValue' and requestCookies=['cookieName'], both 'cookieName' and
                                                  'cookieValue' will not be inspected."
                                            returned: on success
                                            type: list
                                            sample: []
                                        args:
                                            description:
                                                - "List of URL query parameter values from form-urlencoded XML, JSON, AMP, or POST payloads to exclude from
                                                  inspecting.
                                                  Example: If we have query parameter 'argumentName=argumentValue' and args=['argumentName'], both
                                                  'argumentName' and 'argumentValue' will not be inspected."
                                            returned: on success
                                            type: list
                                            sample: []
                                action_name:
                                    description:
                                        - Override action to take if capability was triggered, defined in Protection Rule for this capability.
                                          Only actions of type CHECK are allowed.
                                    returned: on success
                                    type: str
                                    sample: action_name_example
                                collaborative_action_threshold:
                                    description:
                                        - The minimum sum of weights of associated collaborative protection capabilities that have triggered which
                                          must be reached in order for _this_ capability to trigger.
                                          This field is ignored for non-collaborative capabilities.
                                    returned: on success
                                    type: int
                                    sample: 56
                                collaborative_weights:
                                    description:
                                        - Explicit weight values to use for associated collaborative protection capabilities.
                                    returned: on success
                                    type: complex
                                    contains:
                                        key:
                                            description:
                                                - Unique key of collaborative capability for which weight will be overridden.
                                            returned: on success
                                            type: str
                                            sample: key_example
                                        weight:
                                            description:
                                                - The value of weight to set.
                                            returned: on success
                                            type: int
                                            sample: 56
                        protection_capability_settings:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                max_number_of_arguments:
                                    description:
                                        - "Maximum number of arguments allowed. Used in protection capability 920380: Number of Arguments Limits."
                                    returned: on success
                                    type: int
                                    sample: 56
                                max_single_argument_length:
                                    description:
                                        - "Maximum allowed length of a single argument. Used in protection capability 920370: Limit argument value length."
                                    returned: on success
                                    type: int
                                    sample: 56
                                max_total_argument_length:
                                    description:
                                        - "Maximum allowed total length of all arguments. Used in protection capability 920390: Limit arguments total length."
                                    returned: on success
                                    type: int
                                    sample: 56
                                max_http_request_headers:
                                    description:
                                        - "Maximum number of headers allowed in an HTTP request. Used in protection capability 9200014: Limit Number of Request
                                          Headers."
                                    returned: on success
                                    type: int
                                    sample: 56
                                max_http_request_header_length:
                                    description:
                                        - "Maximum allowed length of headers in an HTTP request. Used in protection capability: 9200024: Limit length of request
                                          header size."
                                    returned: on success
                                    type: int
                                    sample: 56
                                allowed_http_methods:
                                    description:
                                        - "List of allowed HTTP methods. Each value as a RFC7230 formated token string.
                                          Used in protection capability 911100: Restrict HTTP Request Methods."
                                    returned: on success
                                    type: list
                                    sample: []
        response_access_control:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                rules:
                    description:
                        - Ordered list of AccessControlRules. Rules are executed in order of appearance in this array.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - Type of WebAppFirewallPolicyRule.
                            returned: on success
                            type: str
                            sample: ACCESS_CONTROL
                        name:
                            description:
                                - Rule name. Must be unique within the module.
                            returned: on success
                            type: str
                            sample: name_example
                        condition_language:
                            description:
                                - "The language used to parse condition from field `condition`. Available languages:"
                                - "* **JMESPATH** an extended JMESPath language syntax."
                            returned: on success
                            type: str
                            sample: JMESPATH
                        condition:
                            description:
                                - An expression that determines whether or not the rule action should be executed.
                            returned: on success
                            type: str
                            sample: condition_example
                        action_name:
                            description:
                                - References action by name from actions defined in WebAppFirewallPolicy.
                            returned: on success
                            type: str
                            sample: action_name_example
        response_protection:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                rules:
                    description:
                        - Ordered list of ProtectionRules. Rules are executed in order of appearance in this array.
                          ProtectionRules in this array can only use protection capabilities of RESPONSE_PROTECTION_CAPABILITY type.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - Type of WebAppFirewallPolicyRule.
                            returned: on success
                            type: str
                            sample: ACCESS_CONTROL
                        name:
                            description:
                                - Rule name. Must be unique within the module.
                            returned: on success
                            type: str
                            sample: name_example
                        condition_language:
                            description:
                                - "The language used to parse condition from field `condition`. Available languages:"
                                - "* **JMESPATH** an extended JMESPath language syntax."
                            returned: on success
                            type: str
                            sample: JMESPATH
                        condition:
                            description:
                                - An expression that determines whether or not the rule action should be executed.
                            returned: on success
                            type: str
                            sample: condition_example
                        action_name:
                            description:
                                - References action by name from actions defined in WebAppFirewallPolicy.
                            returned: on success
                            type: str
                            sample: action_name_example
                        protection_capabilities:
                            description:
                                - An ordered list that references OCI-managed protection capabilities.
                                  Referenced protection capabilities are executed in order of appearance.
                                  The array cannot contain entries with the same pair of capability key and version more than once.
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - Unique key of referenced protection capability.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                version:
                                    description:
                                        - Version of referenced protection capability.
                                    returned: on success
                                    type: int
                                    sample: 56
                                exclusions:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        request_cookies:
                                            description:
                                                - "List of HTTP request cookie values (by cookie name) to exclude from inspecting.
                                                  Example: If we have cookie 'cookieName=cookieValue' and requestCookies=['cookieName'], both 'cookieName' and
                                                  'cookieValue' will not be inspected."
                                            returned: on success
                                            type: list
                                            sample: []
                                        args:
                                            description:
                                                - "List of URL query parameter values from form-urlencoded XML, JSON, AMP, or POST payloads to exclude from
                                                  inspecting.
                                                  Example: If we have query parameter 'argumentName=argumentValue' and args=['argumentName'], both
                                                  'argumentName' and 'argumentValue' will not be inspected."
                                            returned: on success
                                            type: list
                                            sample: []
                                action_name:
                                    description:
                                        - Override action to take if capability was triggered, defined in Protection Rule for this capability.
                                          Only actions of type CHECK are allowed.
                                    returned: on success
                                    type: str
                                    sample: action_name_example
                                collaborative_action_threshold:
                                    description:
                                        - The minimum sum of weights of associated collaborative protection capabilities that have triggered which
                                          must be reached in order for _this_ capability to trigger.
                                          This field is ignored for non-collaborative capabilities.
                                    returned: on success
                                    type: int
                                    sample: 56
                                collaborative_weights:
                                    description:
                                        - Explicit weight values to use for associated collaborative protection capabilities.
                                    returned: on success
                                    type: complex
                                    contains:
                                        key:
                                            description:
                                                - Unique key of collaborative capability for which weight will be overridden.
                                            returned: on success
                                            type: str
                                            sample: key_example
                                        weight:
                                            description:
                                                - The value of weight to set.
                                            returned: on success
                                            type: int
                                            sample: 56
                        protection_capability_settings:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                max_number_of_arguments:
                                    description:
                                        - "Maximum number of arguments allowed. Used in protection capability 920380: Number of Arguments Limits."
                                    returned: on success
                                    type: int
                                    sample: 56
                                max_single_argument_length:
                                    description:
                                        - "Maximum allowed length of a single argument. Used in protection capability 920370: Limit argument value length."
                                    returned: on success
                                    type: int
                                    sample: 56
                                max_total_argument_length:
                                    description:
                                        - "Maximum allowed total length of all arguments. Used in protection capability 920390: Limit arguments total length."
                                    returned: on success
                                    type: int
                                    sample: 56
                                max_http_request_headers:
                                    description:
                                        - "Maximum number of headers allowed in an HTTP request. Used in protection capability 9200014: Limit Number of Request
                                          Headers."
                                    returned: on success
                                    type: int
                                    sample: 56
                                max_http_request_header_length:
                                    description:
                                        - "Maximum allowed length of headers in an HTTP request. Used in protection capability: 9200024: Limit length of request
                                          header size."
                                    returned: on success
                                    type: int
                                    sample: 56
                                allowed_http_methods:
                                    description:
                                        - "List of allowed HTTP methods. Each value as a RFC7230 formated token string.
                                          Used in protection capability 911100: Restrict HTTP Request Methods."
                                    returned: on success
                                    type: list
                                    sample: []
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
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "actions": [{
            "type": "CHECK",
            "name": "name_example",
            "code": 56,
            "headers": [{
                "name": "name_example",
                "value": "value_example"
            }],
            "body": {
                "type": "STATIC_TEXT",
                "text": "text_example"
            }
        }],
        "request_access_control": {
            "default_action_name": "default_action_name_example",
            "rules": [{
                "type": "ACCESS_CONTROL",
                "name": "name_example",
                "condition_language": "JMESPATH",
                "condition": "condition_example",
                "action_name": "action_name_example"
            }]
        },
        "request_rate_limiting": {
            "rules": [{
                "type": "ACCESS_CONTROL",
                "name": "name_example",
                "condition_language": "JMESPATH",
                "condition": "condition_example",
                "action_name": "action_name_example",
                "configurations": [{
                    "period_in_seconds": 56,
                    "requests_limit": 56,
                    "action_duration_in_seconds": 56
                }]
            }]
        },
        "request_protection": {
            "rules": [{
                "type": "ACCESS_CONTROL",
                "name": "name_example",
                "condition_language": "JMESPATH",
                "condition": "condition_example",
                "action_name": "action_name_example",
                "protection_capabilities": [{
                    "key": "key_example",
                    "version": 56,
                    "exclusions": {
                        "request_cookies": [],
                        "args": []
                    },
                    "action_name": "action_name_example",
                    "collaborative_action_threshold": 56,
                    "collaborative_weights": [{
                        "key": "key_example",
                        "weight": 56
                    }]
                }],
                "protection_capability_settings": {
                    "max_number_of_arguments": 56,
                    "max_single_argument_length": 56,
                    "max_total_argument_length": 56,
                    "max_http_request_headers": 56,
                    "max_http_request_header_length": 56,
                    "allowed_http_methods": []
                }
            }]
        },
        "response_access_control": {
            "rules": [{
                "type": "ACCESS_CONTROL",
                "name": "name_example",
                "condition_language": "JMESPATH",
                "condition": "condition_example",
                "action_name": "action_name_example"
            }]
        },
        "response_protection": {
            "rules": [{
                "type": "ACCESS_CONTROL",
                "name": "name_example",
                "condition_language": "JMESPATH",
                "condition": "condition_example",
                "action_name": "action_name_example",
                "protection_capabilities": [{
                    "key": "key_example",
                    "version": 56,
                    "exclusions": {
                        "request_cookies": [],
                        "args": []
                    },
                    "action_name": "action_name_example",
                    "collaborative_action_threshold": 56,
                    "collaborative_weights": [{
                        "key": "key_example",
                        "weight": 56
                    }]
                }],
                "protection_capability_settings": {
                    "max_number_of_arguments": 56,
                    "max_single_argument_length": 56,
                    "max_total_argument_length": 56,
                    "max_http_request_headers": 56,
                    "max_http_request_header_length": 56,
                    "allowed_http_methods": []
                }
            }]
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.waf import WafClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WebAppFirewallPolicyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "web_app_firewall_policy_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_web_app_firewall_policy,
            web_app_firewall_policy_id=self.module.params.get(
                "web_app_firewall_policy_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
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
            self.client.list_web_app_firewall_policies,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


WebAppFirewallPolicyFactsHelperCustom = get_custom_class(
    "WebAppFirewallPolicyFactsHelperCustom"
)


class ResourceFactsHelper(
    WebAppFirewallPolicyFactsHelperCustom, WebAppFirewallPolicyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            web_app_firewall_policy_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(type="list", elements="str"),
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
        resource_type="web_app_firewall_policy",
        service_client_class=WafClient,
        namespace="waf",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(web_app_firewall_policies=result)


if __name__ == "__main__":
    main()
