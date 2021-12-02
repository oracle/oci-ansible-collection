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
module: oci_waf_web_app_firewall_policy
short_description: Manage a WebAppFirewallPolicy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a WebAppFirewallPolicy resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new WebAppFirewallPolicy.
    - "This resource has the following action operations in the M(oracle.oci.oci_waf_web_app_firewall_policy_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - WebAppFirewallPolicy display name, can be renamed.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    actions:
        description:
            - Predefined actions for use in multiple different rules. Not all actions are supported in every module.
              Some actions terminate further execution of modules and rules in a module and some do not.
              Actions names must be unique within this array.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            type:
                description:
                    - "* **CHECK** is a non-terminating action that does not stop the execution of rules in current module,
                        just emits a log message documenting result of rule execution."
                    - "* **ALLOW** is a non-terminating action which upon matching rule skips all remaining rules in the current module."
                    - "* **RETURN_HTTP_RESPONSE** is a terminating action which is executed immediately, returns a defined HTTP response."
                type: str
                choices:
                    - "RETURN_HTTP_RESPONSE"
                    - "ALLOW"
                    - "CHECK"
                required: true
            name:
                description:
                    - Action name. Can be used to reference the action.
                type: str
                required: true
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
                    - Required when type is 'RETURN_HTTP_RESPONSE'
                type: int
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
                    - Applicable when type is 'RETURN_HTTP_RESPONSE'
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - The name of the header field.
                            - Required when type is 'RETURN_HTTP_RESPONSE'
                        type: str
                        required: true
                    value:
                        description:
                            - The value of the header field.
                            - Required when type is 'RETURN_HTTP_RESPONSE'
                        type: str
                        required: true
            body:
                description:
                    - ""
                    - Applicable when type is 'RETURN_HTTP_RESPONSE'
                type: dict
                suboptions:
                    type:
                        description:
                            - Type of HttpResponseBody.
                        type: str
                        choices:
                            - "STATIC_TEXT"
                        required: true
                    text:
                        description:
                            - Static response body text.
                        type: str
                        required: true
    request_access_control:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            default_action_name:
                description:
                    - "References an default Action to take if no AccessControlRule was matched. Allowed action types:"
                    - "* **ALLOW** continues execution of other modules and their rules."
                    - "* **RETURN_HTTP_RESPONSE** terminates further execution of modules and rules and returns defined HTTP response."
                type: str
                required: true
            rules:
                description:
                    - Ordered list of AccessControlRules. Rules are executed in order of appearance in this array.
                type: list
                elements: dict
                suboptions:
                    type:
                        description:
                            - Type of WebAppFirewallPolicyRule.
                        type: str
                        choices:
                            - "ACCESS_CONTROL"
                            - "PROTECTION"
                            - "REQUEST_RATE_LIMITING"
                        required: true
                    name:
                        description:
                            - Rule name. Must be unique within the module.
                        type: str
                        required: true
                    condition_language:
                        description:
                            - "The language used to parse condition from field `condition`. Available languages:"
                            - "* **JMESPATH** an extended JMESPath language syntax."
                        type: str
                        choices:
                            - "JMESPATH"
                    condition:
                        description:
                            - An expression that determines whether or not the rule action should be executed.
                        type: str
                    action_name:
                        description:
                            - References action by name from actions defined in WebAppFirewallPolicy.
                        type: str
                        required: true
    request_rate_limiting:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            rules:
                description:
                    - Ordered list of RequestRateLimitingRules. Rules are executed in order of appearance in this array.
                type: list
                elements: dict
                suboptions:
                    type:
                        description:
                            - Type of WebAppFirewallPolicyRule.
                        type: str
                        choices:
                            - "ACCESS_CONTROL"
                            - "PROTECTION"
                            - "REQUEST_RATE_LIMITING"
                        required: true
                    name:
                        description:
                            - Rule name. Must be unique within the module.
                        type: str
                        required: true
                    condition_language:
                        description:
                            - "The language used to parse condition from field `condition`. Available languages:"
                            - "* **JMESPATH** an extended JMESPath language syntax."
                        type: str
                        choices:
                            - "JMESPATH"
                    condition:
                        description:
                            - An expression that determines whether or not the rule action should be executed.
                        type: str
                    action_name:
                        description:
                            - References action by name from actions defined in WebAppFirewallPolicy.
                        type: str
                        required: true
                    configurations:
                        description:
                            - Rate Limiting Configurations.
                              Each configuration counts requests towards its own `requestsLimit`.
                        type: list
                        elements: dict
                        required: true
                        suboptions:
                            period_in_seconds:
                                description:
                                    - Evaluation period in seconds.
                                type: int
                                required: true
                            requests_limit:
                                description:
                                    - Requests allowed per evaluation period.
                                type: int
                                required: true
                            action_duration_in_seconds:
                                description:
                                    - Duration of block action application in seconds when `requestsLimit` is reached. Optional and can be 0 (no block
                                      duration).
                                type: int
    request_protection:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            rules:
                description:
                    - Ordered list of ProtectionRules. Rules are executed in order of appearance in this array.
                      ProtectionRules in this array can only use protection cCapabilities of REQUEST_PROTECTION_CAPABILITY type.
                type: list
                elements: dict
                suboptions:
                    type:
                        description:
                            - Type of WebAppFirewallPolicyRule.
                        type: str
                        choices:
                            - "ACCESS_CONTROL"
                            - "PROTECTION"
                            - "REQUEST_RATE_LIMITING"
                        required: true
                    name:
                        description:
                            - Rule name. Must be unique within the module.
                        type: str
                        required: true
                    condition_language:
                        description:
                            - "The language used to parse condition from field `condition`. Available languages:"
                            - "* **JMESPATH** an extended JMESPath language syntax."
                        type: str
                        choices:
                            - "JMESPATH"
                    condition:
                        description:
                            - An expression that determines whether or not the rule action should be executed.
                        type: str
                    action_name:
                        description:
                            - References action by name from actions defined in WebAppFirewallPolicy.
                        type: str
                        required: true
                    protection_capabilities:
                        description:
                            - An ordered list that references OCI-managed protection capabilities.
                              Referenced protection capabilities are executed in order of appearance.
                              The array cannot contain entries with the same pair of capability key and version more than once.
                        type: list
                        elements: dict
                        required: true
                        suboptions:
                            key:
                                description:
                                    - Unique key of referenced protection capability.
                                type: str
                                required: true
                            version:
                                description:
                                    - Version of referenced protection capability.
                                type: int
                                required: true
                            exclusions:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    request_cookies:
                                        description:
                                            - "List of HTTP request cookie values (by cookie name) to exclude from inspecting.
                                              Example: If we have cookie 'cookieName=cookieValue' and requestCookies=['cookieName'], both 'cookieName' and
                                              'cookieValue' will not be inspected."
                                        type: list
                                        elements: str
                                    args:
                                        description:
                                            - "List of URL query parameter values from form-urlencoded XML, JSON, AMP, or POST payloads to exclude from
                                              inspecting.
                                              Example: If we have query parameter 'argumentName=argumentValue' and args=['argumentName'], both 'argumentName'
                                              and 'argumentValue' will not be inspected."
                                        type: list
                                        elements: str
                            action_name:
                                description:
                                    - Override action to take if capability was triggered, defined in Protection Rule for this capability.
                                      Only actions of type CHECK are allowed.
                                type: str
                            collaborative_action_threshold:
                                description:
                                    - The minimum sum of weights of associated collaborative protection capabilities that have triggered which
                                      must be reached in order for _this_ capability to trigger.
                                      This field is ignored for non-collaborative capabilities.
                                type: int
                            collaborative_weights:
                                description:
                                    - Explicit weight values to use for associated collaborative protection capabilities.
                                type: list
                                elements: dict
                                suboptions:
                                    key:
                                        description:
                                            - Unique key of collaborative capability for which weight will be overridden.
                                        type: str
                                        required: true
                                    weight:
                                        description:
                                            - The value of weight to set.
                                        type: int
                                        required: true
                    protection_capability_settings:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            max_number_of_arguments:
                                description:
                                    - "Maximum number of arguments allowed. Used in protection capability 920380: Number of Arguments Limits."
                                type: int
                            max_single_argument_length:
                                description:
                                    - "Maximum allowed length of a single argument. Used in protection capability 920370: Limit argument value length."
                                type: int
                            max_total_argument_length:
                                description:
                                    - "Maximum allowed total length of all arguments. Used in protection capability 920390: Limit arguments total length."
                                type: int
                            max_http_request_headers:
                                description:
                                    - "Maximum number of headers allowed in an HTTP request. Used in protection capability 9200014: Limit Number of Request
                                      Headers."
                                type: int
                            max_http_request_header_length:
                                description:
                                    - "Maximum allowed length of headers in an HTTP request. Used in protection capability: 9200024: Limit length of request
                                      header size."
                                type: int
                            allowed_http_methods:
                                description:
                                    - "List of allowed HTTP methods. Each value as a RFC7230 formated token string.
                                      Used in protection capability 911100: Restrict HTTP Request Methods."
                                type: list
                                elements: str
    response_access_control:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            rules:
                description:
                    - Ordered list of AccessControlRules. Rules are executed in order of appearance in this array.
                type: list
                elements: dict
                suboptions:
                    type:
                        description:
                            - Type of WebAppFirewallPolicyRule.
                        type: str
                        choices:
                            - "ACCESS_CONTROL"
                            - "PROTECTION"
                            - "REQUEST_RATE_LIMITING"
                        required: true
                    name:
                        description:
                            - Rule name. Must be unique within the module.
                        type: str
                        required: true
                    condition_language:
                        description:
                            - "The language used to parse condition from field `condition`. Available languages:"
                            - "* **JMESPATH** an extended JMESPath language syntax."
                        type: str
                        choices:
                            - "JMESPATH"
                    condition:
                        description:
                            - An expression that determines whether or not the rule action should be executed.
                        type: str
                    action_name:
                        description:
                            - References action by name from actions defined in WebAppFirewallPolicy.
                        type: str
                        required: true
    response_protection:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            rules:
                description:
                    - Ordered list of ProtectionRules. Rules are executed in order of appearance in this array.
                      ProtectionRules in this array can only use protection capabilities of RESPONSE_PROTECTION_CAPABILITY type.
                type: list
                elements: dict
                suboptions:
                    type:
                        description:
                            - Type of WebAppFirewallPolicyRule.
                        type: str
                        choices:
                            - "ACCESS_CONTROL"
                            - "PROTECTION"
                            - "REQUEST_RATE_LIMITING"
                        required: true
                    name:
                        description:
                            - Rule name. Must be unique within the module.
                        type: str
                        required: true
                    condition_language:
                        description:
                            - "The language used to parse condition from field `condition`. Available languages:"
                            - "* **JMESPATH** an extended JMESPath language syntax."
                        type: str
                        choices:
                            - "JMESPATH"
                    condition:
                        description:
                            - An expression that determines whether or not the rule action should be executed.
                        type: str
                    action_name:
                        description:
                            - References action by name from actions defined in WebAppFirewallPolicy.
                        type: str
                        required: true
                    protection_capabilities:
                        description:
                            - An ordered list that references OCI-managed protection capabilities.
                              Referenced protection capabilities are executed in order of appearance.
                              The array cannot contain entries with the same pair of capability key and version more than once.
                        type: list
                        elements: dict
                        required: true
                        suboptions:
                            key:
                                description:
                                    - Unique key of referenced protection capability.
                                type: str
                                required: true
                            version:
                                description:
                                    - Version of referenced protection capability.
                                type: int
                                required: true
                            exclusions:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    request_cookies:
                                        description:
                                            - "List of HTTP request cookie values (by cookie name) to exclude from inspecting.
                                              Example: If we have cookie 'cookieName=cookieValue' and requestCookies=['cookieName'], both 'cookieName' and
                                              'cookieValue' will not be inspected."
                                        type: list
                                        elements: str
                                    args:
                                        description:
                                            - "List of URL query parameter values from form-urlencoded XML, JSON, AMP, or POST payloads to exclude from
                                              inspecting.
                                              Example: If we have query parameter 'argumentName=argumentValue' and args=['argumentName'], both 'argumentName'
                                              and 'argumentValue' will not be inspected."
                                        type: list
                                        elements: str
                            action_name:
                                description:
                                    - Override action to take if capability was triggered, defined in Protection Rule for this capability.
                                      Only actions of type CHECK are allowed.
                                type: str
                            collaborative_action_threshold:
                                description:
                                    - The minimum sum of weights of associated collaborative protection capabilities that have triggered which
                                      must be reached in order for _this_ capability to trigger.
                                      This field is ignored for non-collaborative capabilities.
                                type: int
                            collaborative_weights:
                                description:
                                    - Explicit weight values to use for associated collaborative protection capabilities.
                                type: list
                                elements: dict
                                suboptions:
                                    key:
                                        description:
                                            - Unique key of collaborative capability for which weight will be overridden.
                                        type: str
                                        required: true
                                    weight:
                                        description:
                                            - The value of weight to set.
                                        type: int
                                        required: true
                    protection_capability_settings:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            max_number_of_arguments:
                                description:
                                    - "Maximum number of arguments allowed. Used in protection capability 920380: Number of Arguments Limits."
                                type: int
                            max_single_argument_length:
                                description:
                                    - "Maximum allowed length of a single argument. Used in protection capability 920370: Limit argument value length."
                                type: int
                            max_total_argument_length:
                                description:
                                    - "Maximum allowed total length of all arguments. Used in protection capability 920390: Limit arguments total length."
                                type: int
                            max_http_request_headers:
                                description:
                                    - "Maximum number of headers allowed in an HTTP request. Used in protection capability 9200014: Limit Number of Request
                                      Headers."
                                type: int
                            max_http_request_header_length:
                                description:
                                    - "Maximum allowed length of headers in an HTTP request. Used in protection capability: 9200024: Limit length of request
                                      header size."
                                type: int
                            allowed_http_methods:
                                description:
                                    - "List of allowed HTTP methods. Each value as a RFC7230 formated token string.
                                      Used in protection capability 911100: Restrict HTTP Request Methods."
                                type: list
                                elements: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    system_tags:
        description:
            - "Usage of system tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            - This parameter is updatable.
        type: dict
    web_app_firewall_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WebAppFirewallPolicy.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the WebAppFirewallPolicy.
            - Use I(state=present) to create or update a WebAppFirewallPolicy.
            - Use I(state=absent) to delete a WebAppFirewallPolicy.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create web_app_firewall_policy
  oci_waf_web_app_firewall_policy:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    actions:
    - # required
      type: RETURN_HTTP_RESPONSE
      name: name_example
      code: 200

      # optional
      headers:
      - # required
        name: name_example
        value: value_example
      body:
        # required
        type: STATIC_TEXT
        text: text_example
    request_access_control:
      # required
      default_action_name: default_action_name_example

      # optional
      rules:
      - # required
        type: ACCESS_CONTROL
        name: name_example
        action_name: action_name_example

        # optional
        condition_language: JMESPATH
        condition: condition_example
    request_rate_limiting:
      # optional
      rules:
      - # required
        type: REQUEST_RATE_LIMITING
        name: name_example
        action_name: action_name_example
        configurations:
        - # required
          period_in_seconds: 56
          requests_limit: 56

          # optional
          action_duration_in_seconds: 56

        # optional
        condition_language: JMESPATH
        condition: condition_example
    request_protection:
      # optional
      rules:
      - # required
        type: PROTECTION
        name: name_example
        action_name: action_name_example
        protection_capabilities:
        - # required
          key: key_example
          version: 56

          # optional
          exclusions:
            # optional
            request_cookies: [ "null" ]
            args: [ "null" ]
          action_name: action_name_example
          collaborative_action_threshold: 56
          collaborative_weights:
          - # required
            key: key_example
            weight: 56

        # optional
        condition_language: JMESPATH
        condition: condition_example
        protection_capability_settings:
          # optional
          max_number_of_arguments: 56
          max_single_argument_length: 56
          max_total_argument_length: 56
          max_http_request_headers: 56
          max_http_request_header_length: 56
          allowed_http_methods: [ "null" ]
    response_access_control:
      # optional
      rules:
      - # required
        type: ACCESS_CONTROL
        name: name_example
        action_name: action_name_example

        # optional
        condition_language: JMESPATH
        condition: condition_example
    response_protection:
      # optional
      rules:
      - # required
        type: PROTECTION
        name: name_example
        action_name: action_name_example
        protection_capabilities:
        - # required
          key: key_example
          version: 56

          # optional
          exclusions:
            # optional
            request_cookies: [ "null" ]
            args: [ "null" ]
          action_name: action_name_example
          collaborative_action_threshold: 56
          collaborative_weights:
          - # required
            key: key_example
            weight: 56

        # optional
        condition_language: JMESPATH
        condition: condition_example
        protection_capability_settings:
          # optional
          max_number_of_arguments: 56
          max_single_argument_length: 56
          max_total_argument_length: 56
          max_http_request_headers: 56
          max_http_request_header_length: 56
          allowed_http_methods: [ "null" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Update web_app_firewall_policy
  oci_waf_web_app_firewall_policy:
    # required
    web_app_firewall_policy_id: "ocid1.webappfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    actions:
    - # required
      type: RETURN_HTTP_RESPONSE
      name: name_example
      code: 200

      # optional
      headers:
      - # required
        name: name_example
        value: value_example
      body:
        # required
        type: STATIC_TEXT
        text: text_example
    request_access_control:
      # required
      default_action_name: default_action_name_example

      # optional
      rules:
      - # required
        type: ACCESS_CONTROL
        name: name_example
        action_name: action_name_example

        # optional
        condition_language: JMESPATH
        condition: condition_example
    request_rate_limiting:
      # optional
      rules:
      - # required
        type: REQUEST_RATE_LIMITING
        name: name_example
        action_name: action_name_example
        configurations:
        - # required
          period_in_seconds: 56
          requests_limit: 56

          # optional
          action_duration_in_seconds: 56

        # optional
        condition_language: JMESPATH
        condition: condition_example
    request_protection:
      # optional
      rules:
      - # required
        type: PROTECTION
        name: name_example
        action_name: action_name_example
        protection_capabilities:
        - # required
          key: key_example
          version: 56

          # optional
          exclusions:
            # optional
            request_cookies: [ "null" ]
            args: [ "null" ]
          action_name: action_name_example
          collaborative_action_threshold: 56
          collaborative_weights:
          - # required
            key: key_example
            weight: 56

        # optional
        condition_language: JMESPATH
        condition: condition_example
        protection_capability_settings:
          # optional
          max_number_of_arguments: 56
          max_single_argument_length: 56
          max_total_argument_length: 56
          max_http_request_headers: 56
          max_http_request_header_length: 56
          allowed_http_methods: [ "null" ]
    response_access_control:
      # optional
      rules:
      - # required
        type: ACCESS_CONTROL
        name: name_example
        action_name: action_name_example

        # optional
        condition_language: JMESPATH
        condition: condition_example
    response_protection:
      # optional
      rules:
      - # required
        type: PROTECTION
        name: name_example
        action_name: action_name_example
        protection_capabilities:
        - # required
          key: key_example
          version: 56

          # optional
          exclusions:
            # optional
            request_cookies: [ "null" ]
            args: [ "null" ]
          action_name: action_name_example
          collaborative_action_threshold: 56
          collaborative_weights:
          - # required
            key: key_example
            weight: 56

        # optional
        condition_language: JMESPATH
        condition: condition_example
        protection_capability_settings:
          # optional
          max_number_of_arguments: 56
          max_single_argument_length: 56
          max_total_argument_length: 56
          max_http_request_headers: 56
          max_http_request_header_length: 56
          allowed_http_methods: [ "null" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Update web_app_firewall_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_waf_web_app_firewall_policy:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    actions:
    - # required
      type: RETURN_HTTP_RESPONSE
      name: name_example
      code: 200

      # optional
      headers:
      - # required
        name: name_example
        value: value_example
      body:
        # required
        type: STATIC_TEXT
        text: text_example
    request_access_control:
      # required
      default_action_name: default_action_name_example

      # optional
      rules:
      - # required
        type: ACCESS_CONTROL
        name: name_example
        action_name: action_name_example

        # optional
        condition_language: JMESPATH
        condition: condition_example
    request_rate_limiting:
      # optional
      rules:
      - # required
        type: REQUEST_RATE_LIMITING
        name: name_example
        action_name: action_name_example
        configurations:
        - # required
          period_in_seconds: 56
          requests_limit: 56

          # optional
          action_duration_in_seconds: 56

        # optional
        condition_language: JMESPATH
        condition: condition_example
    request_protection:
      # optional
      rules:
      - # required
        type: PROTECTION
        name: name_example
        action_name: action_name_example
        protection_capabilities:
        - # required
          key: key_example
          version: 56

          # optional
          exclusions:
            # optional
            request_cookies: [ "null" ]
            args: [ "null" ]
          action_name: action_name_example
          collaborative_action_threshold: 56
          collaborative_weights:
          - # required
            key: key_example
            weight: 56

        # optional
        condition_language: JMESPATH
        condition: condition_example
        protection_capability_settings:
          # optional
          max_number_of_arguments: 56
          max_single_argument_length: 56
          max_total_argument_length: 56
          max_http_request_headers: 56
          max_http_request_header_length: 56
          allowed_http_methods: [ "null" ]
    response_access_control:
      # optional
      rules:
      - # required
        type: ACCESS_CONTROL
        name: name_example
        action_name: action_name_example

        # optional
        condition_language: JMESPATH
        condition: condition_example
    response_protection:
      # optional
      rules:
      - # required
        type: PROTECTION
        name: name_example
        action_name: action_name_example
        protection_capabilities:
        - # required
          key: key_example
          version: 56

          # optional
          exclusions:
            # optional
            request_cookies: [ "null" ]
            args: [ "null" ]
          action_name: action_name_example
          collaborative_action_threshold: 56
          collaborative_weights:
          - # required
            key: key_example
            weight: 56

        # optional
        condition_language: JMESPATH
        condition: condition_example
        protection_capability_settings:
          # optional
          max_number_of_arguments: 56
          max_single_argument_length: 56
          max_total_argument_length: 56
          max_http_request_headers: 56
          max_http_request_header_length: 56
          allowed_http_methods: [ "null" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Delete web_app_firewall_policy
  oci_waf_web_app_firewall_policy:
    # required
    web_app_firewall_policy_id: "ocid1.webappfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete web_app_firewall_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_waf_web_app_firewall_policy:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
web_app_firewall_policy:
    description:
        - Details of the WebAppFirewallPolicy resource acted upon by the current operation
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
                    sample: 200
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
    sample: {
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
            "code": 200,
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
    from oci.waf import WafClient
    from oci.waf.models import CreateWebAppFirewallPolicyDetails
    from oci.waf.models import UpdateWebAppFirewallPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WebAppFirewallPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "web_app_firewall_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("web_app_firewall_policy_id")

    def get_get_fn(self):
        return self.client.get_web_app_firewall_policy

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_web_app_firewall_policy,
            web_app_firewall_policy_id=self.module.params.get(
                "web_app_firewall_policy_id"
            ),
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
        return oci_common_utils.list_all_resources(
            self.client.list_web_app_firewall_policies, **kwargs
        )

    def get_create_model_class(self):
        return CreateWebAppFirewallPolicyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_web_app_firewall_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(create_web_app_firewall_policy_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateWebAppFirewallPolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_web_app_firewall_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                web_app_firewall_policy_id=self.module.params.get(
                    "web_app_firewall_policy_id"
                ),
                update_web_app_firewall_policy_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_web_app_firewall_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                web_app_firewall_policy_id=self.module.params.get(
                    "web_app_firewall_policy_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


WebAppFirewallPolicyHelperCustom = get_custom_class("WebAppFirewallPolicyHelperCustom")


class ResourceHelper(WebAppFirewallPolicyHelperCustom, WebAppFirewallPolicyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            compartment_id=dict(type="str"),
            actions=dict(
                type="list",
                elements="dict",
                options=dict(
                    type=dict(
                        type="str",
                        required=True,
                        choices=["RETURN_HTTP_RESPONSE", "ALLOW", "CHECK"],
                    ),
                    name=dict(type="str", required=True),
                    code=dict(type="int"),
                    headers=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str", required=True),
                            value=dict(type="str", required=True),
                        ),
                    ),
                    body=dict(
                        type="dict",
                        options=dict(
                            type=dict(
                                type="str", required=True, choices=["STATIC_TEXT"]
                            ),
                            text=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            request_access_control=dict(
                type="dict",
                options=dict(
                    default_action_name=dict(type="str", required=True),
                    rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "ACCESS_CONTROL",
                                    "PROTECTION",
                                    "REQUEST_RATE_LIMITING",
                                ],
                            ),
                            name=dict(type="str", required=True),
                            condition_language=dict(type="str", choices=["JMESPATH"]),
                            condition=dict(type="str"),
                            action_name=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            request_rate_limiting=dict(
                type="dict",
                options=dict(
                    rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "ACCESS_CONTROL",
                                    "PROTECTION",
                                    "REQUEST_RATE_LIMITING",
                                ],
                            ),
                            name=dict(type="str", required=True),
                            condition_language=dict(type="str", choices=["JMESPATH"]),
                            condition=dict(type="str"),
                            action_name=dict(type="str", required=True),
                            configurations=dict(
                                type="list",
                                elements="dict",
                                required=True,
                                options=dict(
                                    period_in_seconds=dict(type="int", required=True),
                                    requests_limit=dict(type="int", required=True),
                                    action_duration_in_seconds=dict(type="int"),
                                ),
                            ),
                        ),
                    )
                ),
            ),
            request_protection=dict(
                type="dict",
                options=dict(
                    rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "ACCESS_CONTROL",
                                    "PROTECTION",
                                    "REQUEST_RATE_LIMITING",
                                ],
                            ),
                            name=dict(type="str", required=True),
                            condition_language=dict(type="str", choices=["JMESPATH"]),
                            condition=dict(type="str"),
                            action_name=dict(type="str", required=True),
                            protection_capabilities=dict(
                                type="list",
                                elements="dict",
                                required=True,
                                options=dict(
                                    key=dict(type="str", required=True, no_log=True),
                                    version=dict(type="int", required=True),
                                    exclusions=dict(
                                        type="dict",
                                        options=dict(
                                            request_cookies=dict(
                                                type="list", elements="str"
                                            ),
                                            args=dict(type="list", elements="str"),
                                        ),
                                    ),
                                    action_name=dict(type="str"),
                                    collaborative_action_threshold=dict(type="int"),
                                    collaborative_weights=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            key=dict(
                                                type="str", required=True, no_log=True
                                            ),
                                            weight=dict(type="int", required=True),
                                        ),
                                    ),
                                ),
                            ),
                            protection_capability_settings=dict(
                                type="dict",
                                options=dict(
                                    max_number_of_arguments=dict(type="int"),
                                    max_single_argument_length=dict(type="int"),
                                    max_total_argument_length=dict(type="int"),
                                    max_http_request_headers=dict(type="int"),
                                    max_http_request_header_length=dict(type="int"),
                                    allowed_http_methods=dict(
                                        type="list", elements="str"
                                    ),
                                ),
                            ),
                        ),
                    )
                ),
            ),
            response_access_control=dict(
                type="dict",
                options=dict(
                    rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "ACCESS_CONTROL",
                                    "PROTECTION",
                                    "REQUEST_RATE_LIMITING",
                                ],
                            ),
                            name=dict(type="str", required=True),
                            condition_language=dict(type="str", choices=["JMESPATH"]),
                            condition=dict(type="str"),
                            action_name=dict(type="str", required=True),
                        ),
                    )
                ),
            ),
            response_protection=dict(
                type="dict",
                options=dict(
                    rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "ACCESS_CONTROL",
                                    "PROTECTION",
                                    "REQUEST_RATE_LIMITING",
                                ],
                            ),
                            name=dict(type="str", required=True),
                            condition_language=dict(type="str", choices=["JMESPATH"]),
                            condition=dict(type="str"),
                            action_name=dict(type="str", required=True),
                            protection_capabilities=dict(
                                type="list",
                                elements="dict",
                                required=True,
                                options=dict(
                                    key=dict(type="str", required=True, no_log=True),
                                    version=dict(type="int", required=True),
                                    exclusions=dict(
                                        type="dict",
                                        options=dict(
                                            request_cookies=dict(
                                                type="list", elements="str"
                                            ),
                                            args=dict(type="list", elements="str"),
                                        ),
                                    ),
                                    action_name=dict(type="str"),
                                    collaborative_action_threshold=dict(type="int"),
                                    collaborative_weights=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            key=dict(
                                                type="str", required=True, no_log=True
                                            ),
                                            weight=dict(type="int", required=True),
                                        ),
                                    ),
                                ),
                            ),
                            protection_capability_settings=dict(
                                type="dict",
                                options=dict(
                                    max_number_of_arguments=dict(type="int"),
                                    max_single_argument_length=dict(type="int"),
                                    max_total_argument_length=dict(type="int"),
                                    max_http_request_headers=dict(type="int"),
                                    max_http_request_header_length=dict(type="int"),
                                    allowed_http_methods=dict(
                                        type="list", elements="str"
                                    ),
                                ),
                            ),
                        ),
                    )
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            system_tags=dict(type="dict"),
            web_app_firewall_policy_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="web_app_firewall_policy",
        service_client_class=WafClient,
        namespace="waf",
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
