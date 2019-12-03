#!/usr/bin/python
# Copyright (c) 2017, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_waas_policy_facts
short_description: Fetches details about one or multiple WaasPolicy resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple WaasPolicy resources in Oracle Cloud Infrastructure
    - Gets a list of WAAS policies.
    - If I(waas_policy_id) is specified, the details of a single WaasPolicy will be returned.
version_added: "2.5"
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
            - Required to get a specific waas_policy.
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment. This number is generated when the
              compartment is created.
            - Required to list multiple waas_policies.
    sort_by:
        description:
            - The value by which policies are sorted in a paginated 'List' call.  If unspecified, defaults to `timeCreated`.
        choices:
            - "id"
            - "displayName"
            - "timeCreated"
    sort_order:
        description:
            - The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.
        choices:
            - "ASC"
            - "DESC"
    id:
        description:
            - Filter policies using a list of policy OCIDs.
        type: list
    display_name:
        description:
            - Filter policies using a list of display names.
        type: list
        aliases: ["name"]
    lifecycle_state:
        description:
            - Filter policies using a list of lifecycle states.
        type: list
    time_created_greater_than_or_equal_to:
        description:
            - A filter that matches policies created on or after the specified date and time.
    time_created_less_than:
        description:
            - A filter that matches policies created before the specified date-time.
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: List waas_policies
  oci_waas_policy_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific waas_policy
  oci_waas_policy_facts:
    waas_policy_id: ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
waas_policies:
    description:
        - List of WaasPolicy resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy's compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The user-friendly name of the WAAS policy. The name can be changed and does not need to be unique.
            returned: on success
            type: string
            sample: display_name_example
        domain:
            description:
                - The web application domain that the WAAS policy protects.
            returned: on success
            type: string
            sample: domain_example
        additional_domains:
            description:
                - An array of additional domains for this web application.
            returned: on success
            type: list
            sample: []
        cname:
            description:
                - The CNAME record to add to your DNS configuration to route traffic for the domain, and all additional domains, through the WAF.
            returned: on success
            type: string
            sample: cname_example
        lifecycle_state:
            description:
                - The current lifecycle state of the WAAS policy.
            returned: on success
            type: string
            sample: CREATING
        time_created:
            description:
                - The date and time the policy was created, expressed in RFC 3339 timestamp format.
            returned: on success
            type: string
            sample: 2018-11-16T21:10:29Z
        origins:
            description:
                - A map of host to origin for the web application. The key should be a customer friendly name for the host, ex. primary, secondary, etc.
            returned: on success
            type: complex
            contains:
                uri:
                    description:
                        - The URI of the origin. Does not support paths. Port numbers should be specified in the `httpPort` and `httpsPort` fields.
                    returned: on success
                    type: string
                    sample: uri_example
                http_port:
                    description:
                        - The HTTP port on the origin that the web application listens on. If unspecified, defaults to `80`.
                    returned: on success
                    type: int
                    sample: 56
                https_port:
                    description:
                        - The HTTPS port on the origin that the web application listens on. If unspecified, defaults to `443`.
                    returned: on success
                    type: int
                    sample: 56
                custom_headers:
                    description:
                        - A list of HTTP headers to forward to your origin.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The name of the header.
                            returned: on success
                            type: string
                            sample: name_example
                        value:
                            description:
                                - The value of the header.
                            returned: on success
                            type: string
                            sample: value_example
        policy_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                certificate_id:
                    description:
                        - The OCID of the SSL certificate to use if HTTPS is supported.
                    returned: on success
                    type: string
                    sample: ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx
                is_https_enabled:
                    description:
                        - Enable or disable HTTPS support. If true, a `certificateId` is required. If unspecified, defaults to `false`.
                    returned: on success
                    type: bool
                    sample: true
                is_https_forced:
                    description:
                        - Force HTTP to HTTPS redirection. If unspecified, defaults to `false`.
                    returned: on success
                    type: bool
                    sample: true
        waf_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                access_rules:
                    description:
                        - The access rules applied to the Web Application Firewall. Used for defining custom access policies with the combination of `ALLOW`,
                          `DETECT`, and `BLOCK` rules, based on different criteria.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The unique name of the access rule.
                            returned: on success
                            type: string
                            sample: name_example
                        criteria:
                            description:
                                - The list of access rule criteria.
                            returned: on success
                            type: complex
                            contains:
                                condition:
                                    description:
                                        - The criteria the access rule uses to determine if action should be taken on a request.
                                        - "- **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value`
                                          field.
                                          - **URL_IS_NOT:** Matches if the concatenation of request URL path and query is not identical to the contents of the
                                            `value` field.
                                          - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the
                                            `value` field.
                                          - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the
                                            `value` field.
                                          - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the
                                            `value` field.
                                          - **URL_REGEX:** Matches if the request is described by the regular expression in the `value` field.
                                          - **IP_IS:** Matches if the request originates from an IP address in the `value` field.
                                          - **IP_IS_NOT:** Matches if the request does not originate from an IP address in the `value` field.
                                          - **HTTP_HEADER_CONTAINS:** Matches if the request includes an HTTP header field whose name and value correspond to
                                            data specified in the `value` field with a separating colon. **Example:** `host:test.example.com` where `host` is
                                            the name of the field and `test.example.com` is the value of the host field. Comparison is independently applied to
                                            every header field whose name is a case insensitive match, and the value is required to be case-sensitive identical.
                                          - **COUNTRY_IS:** Matches if the request originates from a country in the `value` field. Country codes are in ISO
                                            3166-1 alpha-2 format. For a list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                                          - **COUNTRY_IS_NOT:** Matches if the request does not originate from a country in the `value` field. Country codes are
                                            in ISO 3166-1 alpha-2 format. For a list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                                          - **USER_AGENT_IS:** Matches if the requesting user agent is identical to the contents of the `value` field. Example:
                                            `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`
                                          - **USER_AGENT_IS_NOT:** Matches if the requesting user agent is not identical to the contents of the `value` field.
                                            Example: `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`"
                                    returned: on success
                                    type: string
                                    sample: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0
                                value:
                                    description:
                                        - The criteria value.
                                    returned: on success
                                    type: string
                                    sample: value_example
                        action:
                            description:
                                - The action to take when the access criteria are met for a rule. If unspecified, defaults to `ALLOW`.
                            returned: on success
                            type: string
                            sample: ALLOW
                        block_action:
                            description:
                                - The method used to block requests if `action` is set to `BLOCK` and the access criteria are met. If unspecified, defaults to
                                  `SET_RESPONSE_CODE`.
                            returned: on success
                            type: string
                            sample: SET_RESPONSE_CODE
                        block_response_code:
                            description:
                                - The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the
                                  access criteria are met. If unspecified, defaults to `403`.
                            returned: on success
                            type: int
                            sample: 56
                        block_error_page_message:
                            description:
                                - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                                  access criteria are met. If unspecified, defaults to 'Access to the website is blocked.'
                            returned: on success
                            type: string
                            sample: block_error_page_message_example
                        block_error_page_code:
                            description:
                                - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                                  access criteria are met. If unspecified, defaults to 'Access rules'.
                            returned: on success
                            type: string
                            sample: block_error_page_code_example
                        block_error_page_description:
                            description:
                                - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and
                                  the access criteria are met. If unspecified, defaults to 'Access blocked by website owner. Please contact support.'
                            returned: on success
                            type: string
                            sample: block_error_page_description_example
                address_rate_limiting:
                    description:
                        - The IP address rate limiting settings used to limit the number of requests from an address.
                    returned: on success
                    type: complex
                    contains:
                        is_enabled:
                            description:
                                - Enables or disables the address rate limiting Web Application Firewall feature.
                            returned: on success
                            type: bool
                            sample: true
                        allowed_rate_per_address:
                            description:
                                - The number of allowed requests per second from one IP address. If unspecified, defaults to `1`.
                            returned: on success
                            type: int
                            sample: 56
                        max_delayed_count_per_address:
                            description:
                                - The maximum number of requests allowed to be queued before subsequent requests are dropped. If unspecified, defaults to `10`.
                            returned: on success
                            type: int
                            sample: 56
                        block_response_code:
                            description:
                                - The response status code returned when a request is blocked. If unspecified, defaults to `503`.
                            returned: on success
                            type: int
                            sample: 56
                captchas:
                    description:
                        - A list of CAPTCHA challenge settings. These are used to challenge requests with a CAPTCHA to block bots.
                    returned: on success
                    type: complex
                    contains:
                        url:
                            description:
                                - The unique URL path at which to show the CAPTCHA challenge.
                            returned: on success
                            type: string
                            sample: url_example
                        session_expiration_in_seconds:
                            description:
                                - The amount of time before the CAPTCHA expires, in seconds. If unspecified, defaults to `300`.
                            returned: on success
                            type: int
                            sample: 56
                        title:
                            description:
                                - The title used when displaying a CAPTCHA challenge. If unspecified, defaults to `Are you human?`
                            returned: on success
                            type: string
                            sample: title_example
                        header_text:
                            description:
                                - The text to show in the header when showing a CAPTCHA challenge. If unspecified, defaults to 'We have detected an increased
                                  number of attempts to access this website. To help us keep this site secure, please let us know that you are not a robot by
                                  entering the text from the image below.'
                            returned: on success
                            type: string
                            sample: header_text_example
                        footer_text:
                            description:
                                - The text to show in the footer when showing a CAPTCHA challenge. If unspecified, defaults to 'Enter the letters and numbers as
                                  they are shown in the image above.'
                            returned: on success
                            type: string
                            sample: footer_text_example
                        failure_message:
                            description:
                                - The text to show when incorrect CAPTCHA text is entered. If unspecified, defaults to `The CAPTCHA was incorrect. Try again.`
                            returned: on success
                            type: string
                            sample: failure_message_example
                        submit_label:
                            description:
                                - The text to show on the label of the CAPTCHA challenge submit button. If unspecified, defaults to `Yes, I am human`.
                            returned: on success
                            type: string
                            sample: submit_label_example
                device_fingerprint_challenge:
                    description:
                        - The device fingerprint challenge settings. Used to detect unique devices based on the device fingerprint information collected in
                          order to block bots.
                    returned: on success
                    type: complex
                    contains:
                        is_enabled:
                            description:
                                - Enables or disables the device fingerprint challenge Web Application Firewall feature.
                            returned: on success
                            type: bool
                            sample: true
                        action:
                            description:
                                - The action to take on requests from detected bots. If unspecified, defaults to `DETECT`.
                            returned: on success
                            type: string
                            sample: DETECT
                        failure_threshold:
                            description:
                                - The number of failed requests allowed before taking action. If unspecified, defaults to `10`.
                            returned: on success
                            type: int
                            sample: 56
                        action_expiration_in_seconds:
                            description:
                                - The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.
                            returned: on success
                            type: int
                            sample: 56
                        failure_threshold_expiration_in_seconds:
                            description:
                                - The number of seconds before the failure threshold resets. If unspecified, defaults to `60`.
                            returned: on success
                            type: int
                            sample: 56
                        max_address_count:
                            description:
                                - The maximum number of IP addresses permitted with the same device fingerprint. If unspecified, defaults to `20`.
                            returned: on success
                            type: int
                            sample: 56
                        max_address_count_expiration_in_seconds:
                            description:
                                - The number of seconds before the maximum addresses count resets. If unspecified, defaults to `60`.
                            returned: on success
                            type: int
                            sample: 56
                        challenge_settings:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                block_action:
                                    description:
                                        - The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to
                                          `SHOW_ERROR_PAGE`.
                                    returned: on success
                                    type: string
                                    sample: SET_RESPONSE_CODE
                                block_response_code:
                                    description:
                                        - The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or
                                          `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`.
                                    returned: on success
                                    type: int
                                    sample: 56
                                block_error_page_message:
                                    description:
                                        - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and
                                          the request is blocked. If unspecified, defaults to `Access to the website is blocked`.
                                    returned: on success
                                    type: string
                                    sample: block_error_page_message_example
                                block_error_page_description:
                                    description:
                                        - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to
                                          `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please
                                          contact support.`
                                    returned: on success
                                    type: string
                                    sample: block_error_page_description_example
                                block_error_page_code:
                                    description:
                                        - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`
                                          and the request is blocked. If unspecified, defaults to `403`.
                                    returned: on success
                                    type: string
                                    sample: block_error_page_code_example
                                captcha_title:
                                    description:
                                        - The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                          `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Are you human?`
                                    returned: on success
                                    type: string
                                    sample: captcha_title_example
                                captcha_header:
                                    description:
                                        - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set
                                          to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of
                                          attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by
                                          entering the text from captcha below.`
                                    returned: on success
                                    type: string
                                    sample: captcha_header_example
                                captcha_footer:
                                    description:
                                        - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set
                                          to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are
                                          shown in image above`.
                                    returned: on success
                                    type: string
                                    sample: captcha_footer_example
                                captcha_submit_label:
                                    description:
                                        - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is
                                          set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
                                    returned: on success
                                    type: string
                                    sample: captcha_submit_label_example
                good_bots:
                    description:
                        - A list of bots allowed to access the web application.
                    returned: on success
                    type: complex
                    contains:
                        key:
                            description:
                                - The unique key for the bot.
                            returned: on success
                            type: string
                            sample: key_example
                        name:
                            description:
                                - The bot name.
                            returned: on success
                            type: string
                            sample: name_example
                        is_enabled:
                            description:
                                - Enables or disables the bot.
                            returned: on success
                            type: bool
                            sample: true
                        description:
                            description:
                                - The description of the bot.
                            returned: on success
                            type: string
                            sample: description_example
                human_interaction_challenge:
                    description:
                        - The human interaction challenge settings. Used to look for natural human interactions such as mouse movements, time on site, and page
                          scrolling to identify bots.
                    returned: on success
                    type: complex
                    contains:
                        is_enabled:
                            description:
                                - Enables or disables the human interaction challenge Web Application Firewall feature.
                            returned: on success
                            type: bool
                            sample: true
                        action:
                            description:
                                - The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.
                            returned: on success
                            type: string
                            sample: DETECT
                        failure_threshold:
                            description:
                                - The number of failed requests before taking action. If unspecified, defaults to `10`.
                            returned: on success
                            type: int
                            sample: 56
                        action_expiration_in_seconds:
                            description:
                                - The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.
                            returned: on success
                            type: int
                            sample: 56
                        failure_threshold_expiration_in_seconds:
                            description:
                                - The number of seconds before the failure threshold resets. If unspecified, defaults to  `60`.
                            returned: on success
                            type: int
                            sample: 56
                        interaction_threshold:
                            description:
                                - The number of interactions required to pass the challenge. If unspecified, defaults to `3`.
                            returned: on success
                            type: int
                            sample: 56
                        recording_period_in_seconds:
                            description:
                                - The number of seconds to record the interactions from the user. If unspecified, defaults to `15`.
                            returned: on success
                            type: int
                            sample: 56
                        set_http_header:
                            description:
                                - Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the
                                  `action` is set to `DETECT`.
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - The name of the header.
                                    returned: on success
                                    type: string
                                    sample: name_example
                                value:
                                    description:
                                        - The value of the header.
                                    returned: on success
                                    type: string
                                    sample: value_example
                        challenge_settings:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                block_action:
                                    description:
                                        - The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to
                                          `SHOW_ERROR_PAGE`.
                                    returned: on success
                                    type: string
                                    sample: SET_RESPONSE_CODE
                                block_response_code:
                                    description:
                                        - The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or
                                          `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`.
                                    returned: on success
                                    type: int
                                    sample: 56
                                block_error_page_message:
                                    description:
                                        - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and
                                          the request is blocked. If unspecified, defaults to `Access to the website is blocked`.
                                    returned: on success
                                    type: string
                                    sample: block_error_page_message_example
                                block_error_page_description:
                                    description:
                                        - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to
                                          `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please
                                          contact support.`
                                    returned: on success
                                    type: string
                                    sample: block_error_page_description_example
                                block_error_page_code:
                                    description:
                                        - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`
                                          and the request is blocked. If unspecified, defaults to `403`.
                                    returned: on success
                                    type: string
                                    sample: block_error_page_code_example
                                captcha_title:
                                    description:
                                        - The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                          `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Are you human?`
                                    returned: on success
                                    type: string
                                    sample: captcha_title_example
                                captcha_header:
                                    description:
                                        - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set
                                          to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of
                                          attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by
                                          entering the text from captcha below.`
                                    returned: on success
                                    type: string
                                    sample: captcha_header_example
                                captcha_footer:
                                    description:
                                        - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set
                                          to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are
                                          shown in image above`.
                                    returned: on success
                                    type: string
                                    sample: captcha_footer_example
                                captcha_submit_label:
                                    description:
                                        - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is
                                          set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
                                    returned: on success
                                    type: string
                                    sample: captcha_submit_label_example
                js_challenge:
                    description:
                        - The JavaScript challenge settings. Used to challenge requests with a JavaScript challenge and take the action if a browser has no
                          JavaScript support in order to block bots.
                    returned: on success
                    type: complex
                    contains:
                        is_enabled:
                            description:
                                - Enables or disables the JavaScript challenge Web Application Firewall feature.
                            returned: on success
                            type: bool
                            sample: true
                        action:
                            description:
                                - The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.
                            returned: on success
                            type: string
                            sample: DETECT
                        failure_threshold:
                            description:
                                - The number of failed requests before taking action. If unspecified, defaults to `10`.
                            returned: on success
                            type: int
                            sample: 56
                        action_expiration_in_seconds:
                            description:
                                - The number of seconds between challenges from the same IP address. If unspecified, defaults to `60`.
                            returned: on success
                            type: int
                            sample: 56
                        set_http_header:
                            description:
                                - Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the
                                  `action` is set to `DETECT`.
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - The name of the header.
                                    returned: on success
                                    type: string
                                    sample: name_example
                                value:
                                    description:
                                        - The value of the header.
                                    returned: on success
                                    type: string
                                    sample: value_example
                        challenge_settings:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                block_action:
                                    description:
                                        - The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to
                                          `SHOW_ERROR_PAGE`.
                                    returned: on success
                                    type: string
                                    sample: SET_RESPONSE_CODE
                                block_response_code:
                                    description:
                                        - The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or
                                          `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`.
                                    returned: on success
                                    type: int
                                    sample: 56
                                block_error_page_message:
                                    description:
                                        - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and
                                          the request is blocked. If unspecified, defaults to `Access to the website is blocked`.
                                    returned: on success
                                    type: string
                                    sample: block_error_page_message_example
                                block_error_page_description:
                                    description:
                                        - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to
                                          `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please
                                          contact support.`
                                    returned: on success
                                    type: string
                                    sample: block_error_page_description_example
                                block_error_page_code:
                                    description:
                                        - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`
                                          and the request is blocked. If unspecified, defaults to `403`.
                                    returned: on success
                                    type: string
                                    sample: block_error_page_code_example
                                captcha_title:
                                    description:
                                        - The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                          `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Are you human?`
                                    returned: on success
                                    type: string
                                    sample: captcha_title_example
                                captcha_header:
                                    description:
                                        - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set
                                          to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of
                                          attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by
                                          entering the text from captcha below.`
                                    returned: on success
                                    type: string
                                    sample: captcha_header_example
                                captcha_footer:
                                    description:
                                        - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set
                                          to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are
                                          shown in image above`.
                                    returned: on success
                                    type: string
                                    sample: captcha_footer_example
                                captcha_submit_label:
                                    description:
                                        - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is
                                          set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
                                    returned: on success
                                    type: string
                                    sample: captcha_submit_label_example
                origin:
                    description:
                        - The key in the map of origins referencing the origin used for the Web Application Firewall. The origin must already be included in
                          `Origins`. Required when creating the `WafConfig` resource, but not on update.
                    returned: on success
                    type: string
                    sample: origin_example
                protection_rules:
                    description:
                        - A list of the protection rules and their details.
                    returned: on success
                    type: complex
                    contains:
                        key:
                            description:
                                - The unique key of the protection rule.
                            returned: on success
                            type: string
                            sample: key_example
                        mod_security_rule_ids:
                            description:
                                - The list of the ModSecurity rule IDs that apply to this protection rule. For more information about ModSecurity's open source
                                  WAF rules, see L(Mod Security's documentation,https://www.modsecurity.org/CRS/Documentation/index.html).
                            returned: on success
                            type: list
                            sample: []
                        name:
                            description:
                                - The name of the protection rule.
                            returned: on success
                            type: string
                            sample: name_example
                        description:
                            description:
                                - The description of the protection rule.
                            returned: on success
                            type: string
                            sample: description_example
                        action:
                            description:
                                - The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.
                            returned: on success
                            type: string
                            sample: OFF
                        labels:
                            description:
                                - The list of labels for the protection rule.
                                - "**Note:** Protection rules with a `ResponseBody` label will have no effect unless `isResponseInspected` is true."
                            returned: on success
                            type: list
                            sample: []
                        exclusions:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                target:
                                    description:
                                        - The target of the exclusion.
                                    returned: on success
                                    type: string
                                    sample: REQUEST_COOKIES
                                exclusions:
                                    description:
                                        - ""
                                    returned: on success
                                    type: list
                                    sample: []
                protection_settings:
                    description:
                        - The settings to apply to protection rules.
                    returned: on success
                    type: complex
                    contains:
                        block_action:
                            description:
                                - If `action` is set to `BLOCK`, this specifies how the traffic is blocked when detected as malicious by a protection rule. If
                                  unspecified, defaults to `SET_RESPONSE_CODE`.
                            returned: on success
                            type: string
                            sample: SHOW_ERROR_PAGE
                        block_response_code:
                            description:
                                - The response code returned when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the traffic is
                                  detected as malicious by a protection rule. If unspecified, defaults to `403`.
                            returned: on success
                            type: int
                            sample: 56
                        block_error_page_message:
                            description:
                                - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                                  traffic is detected as malicious by a protection rule. If unspecified, defaults to 'Access to the website is blocked.'
                            returned: on success
                            type: string
                            sample: block_error_page_message_example
                        block_error_page_code:
                            description:
                                - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                                  traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`.
                            returned: on success
                            type: string
                            sample: block_error_page_code_example
                        block_error_page_description:
                            description:
                                - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and
                                  the traffic is detected as malicious by a protection rule. If unspecified, defaults to `Access blocked by website owner.
                                  Please contact support.`
                            returned: on success
                            type: string
                            sample: block_error_page_description_example
                        max_argument_count:
                            description:
                                - The maximum number of arguments allowed to be passed to your application before an action is taken. If unspecified, defaults
                                  to `255`.
                            returned: on success
                            type: int
                            sample: 56
                        max_name_length_per_argument:
                            description:
                                - The maximum length allowed for each argument name, in characters. If unspecified, defaults to `400`.
                            returned: on success
                            type: int
                            sample: 56
                        max_total_name_length_of_arguments:
                            description:
                                - The maximum length allowed for the sum of all argument names, in characters. If unspecified, defaults to `64000`.
                            returned: on success
                            type: int
                            sample: 56
                        recommendations_period_in_days:
                            description:
                                - The length of time to analyze traffic traffic, in days. After the analysis period, `WafRecommendations` will be populated. If
                                  unspecified, defaults to `10`.
                                - Use `GET /waasPolicies/{waasPolicyId}/wafRecommendations` to view WAF recommendations.
                            returned: on success
                            type: int
                            sample: 56
                        is_response_inspected:
                            description:
                                - Inspects the response body of origin responses. Can be used to detect leakage of sensitive data. If unspecified, defaults to
                                  `false`.
                                - "**Note:** Only origin responses with a Content-Type matching a value in `mediaTypes` will be inspected."
                            returned: on success
                            type: bool
                            sample: true
                        max_response_size_in_ki_b:
                            description:
                                - The maximum response size to be fully inspected, in binary kilobytes (KiB). Anything over this limit will be partially
                                  inspected. If unspecified, defaults to `1024`.
                            returned: on success
                            type: int
                            sample: 56
                        allowed_http_methods:
                            description:
                                - The list of allowed HTTP methods. If unspecified, default to `[OPTIONS, GET, HEAD, POST]`.
                            returned: on success
                            type: list
                            sample: []
                        media_types:
                            description:
                                - The list of media types to allow for inspection, if `isResponseInspected` is enabled. Only responses with MIME types in this
                                  list will be inspected. If unspecified, defaults to `[`text/html`, `text/plain`, `text/xml`]`.
                                - "   Supported MIME types include:"
                                - "   - text/html
                                      - text/plain
                                      - text/asp
                                      - text/css
                                      - text/x-script
                                      - application/json
                                      - text/webviewhtml
                                      - text/x-java-source
                                      - application/x-javascript
                                      - application/javascript
                                      - application/ecmascript
                                      - text/javascript
                                      - text/ecmascript
                                      - text/x-script.perl
                                      - text/x-script.phyton
                                      - application/plain
                                      - application/xml
                                      - text/xml"
                            returned: on success
                            type: list
                            sample: []
                threat_feeds:
                    description:
                        - A list of threat intelligence feeds and the actions to apply to known malicious traffic based on internet intelligence.
                    returned: on success
                    type: complex
                    contains:
                        key:
                            description:
                                - The unique key of the threat intelligence feed.
                            returned: on success
                            type: string
                            sample: key_example
                        name:
                            description:
                                - The name of the threat intelligence feed.
                            returned: on success
                            type: string
                            sample: name_example
                        action:
                            description:
                                - The action to take when traffic is flagged as malicious by data from the threat intelligence feed. If unspecified, defaults to
                                  `OFF`.
                            returned: on success
                            type: string
                            sample: OFF
                        description:
                            description:
                                - The description of the threat intelligence feed.
                            returned: on success
                            type: string
                            sample: description_example
                whitelists:
                    description:
                        - A list of IP addresses that bypass the Web Application Firewall.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The unique name of the whitelist.
                            returned: on success
                            type: string
                            sample: name_example
                        addresses:
                            description:
                                - A set of IP addresses or CIDR notations to include in the whitelist.
                            returned: on success
                            type: list
                            sample: []
        freeform_tags:
            description:
                - A simple key-value pair without any defined schema.
            returned: on success
            type: dict
            sample: {Department: Finance}
        defined_tags:
            description:
                - A key-value pair with a defined schema that restricts the values of tags. These predefined keys are scoped to namespaces.
            returned: on success
            type: dict
            sample: {Operations: {CostCenter: US}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "domain": "domain_example",
        "additional_domains": [],
        "cname": "cname_example",
        "lifecycle_state": "CREATING",
        "time_created": "2018-11-16T21:10:29Z",
        "origins": {
            "uri": "uri_example",
            "http_port": 56,
            "https_port": 56,
            "custom_headers": [{
                "name": "name_example",
                "value": "value_example"
            }]
        },
        "policy_config": {
            "certificate_id": "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx",
            "is_https_enabled": true,
            "is_https_forced": true
        },
        "waf_config": {
            "access_rules": [{
                "name": "name_example",
                "criteria": [{
                    "condition": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0",
                    "value": "value_example"
                }],
                "action": "ALLOW",
                "block_action": "SET_RESPONSE_CODE",
                "block_response_code": 56,
                "block_error_page_message": "block_error_page_message_example",
                "block_error_page_code": "block_error_page_code_example",
                "block_error_page_description": "block_error_page_description_example"
            }],
            "address_rate_limiting": {
                "is_enabled": true,
                "allowed_rate_per_address": 56,
                "max_delayed_count_per_address": 56,
                "block_response_code": 56
            },
            "captchas": [{
                "url": "url_example",
                "session_expiration_in_seconds": 56,
                "title": "title_example",
                "header_text": "header_text_example",
                "footer_text": "footer_text_example",
                "failure_message": "failure_message_example",
                "submit_label": "submit_label_example"
            }],
            "device_fingerprint_challenge": {
                "is_enabled": true,
                "action": "DETECT",
                "failure_threshold": 56,
                "action_expiration_in_seconds": 56,
                "failure_threshold_expiration_in_seconds": 56,
                "max_address_count": 56,
                "max_address_count_expiration_in_seconds": 56,
                "challenge_settings": {
                    "block_action": "SET_RESPONSE_CODE",
                    "block_response_code": 56,
                    "block_error_page_message": "block_error_page_message_example",
                    "block_error_page_description": "block_error_page_description_example",
                    "block_error_page_code": "block_error_page_code_example",
                    "captcha_title": "captcha_title_example",
                    "captcha_header": "captcha_header_example",
                    "captcha_footer": "captcha_footer_example",
                    "captcha_submit_label": "captcha_submit_label_example"
                }
            },
            "good_bots": [{
                "key": "key_example",
                "name": "name_example",
                "is_enabled": true,
                "description": "description_example"
            }],
            "human_interaction_challenge": {
                "is_enabled": true,
                "action": "DETECT",
                "failure_threshold": 56,
                "action_expiration_in_seconds": 56,
                "failure_threshold_expiration_in_seconds": 56,
                "interaction_threshold": 56,
                "recording_period_in_seconds": 56,
                "set_http_header": {
                    "name": "name_example",
                    "value": "value_example"
                },
                "challenge_settings": {
                    "block_action": "SET_RESPONSE_CODE",
                    "block_response_code": 56,
                    "block_error_page_message": "block_error_page_message_example",
                    "block_error_page_description": "block_error_page_description_example",
                    "block_error_page_code": "block_error_page_code_example",
                    "captcha_title": "captcha_title_example",
                    "captcha_header": "captcha_header_example",
                    "captcha_footer": "captcha_footer_example",
                    "captcha_submit_label": "captcha_submit_label_example"
                }
            },
            "js_challenge": {
                "is_enabled": true,
                "action": "DETECT",
                "failure_threshold": 56,
                "action_expiration_in_seconds": 56,
                "set_http_header": {
                    "name": "name_example",
                    "value": "value_example"
                },
                "challenge_settings": {
                    "block_action": "SET_RESPONSE_CODE",
                    "block_response_code": 56,
                    "block_error_page_message": "block_error_page_message_example",
                    "block_error_page_description": "block_error_page_description_example",
                    "block_error_page_code": "block_error_page_code_example",
                    "captcha_title": "captcha_title_example",
                    "captcha_header": "captcha_header_example",
                    "captcha_footer": "captcha_footer_example",
                    "captcha_submit_label": "captcha_submit_label_example"
                }
            },
            "origin": "origin_example",
            "protection_rules": [{
                "key": "key_example",
                "mod_security_rule_ids": [],
                "name": "name_example",
                "description": "description_example",
                "action": "OFF",
                "labels": [],
                "exclusions": [{
                    "target": "REQUEST_COOKIES",
                    "exclusions": []
                }]
            }],
            "protection_settings": {
                "block_action": "SHOW_ERROR_PAGE",
                "block_response_code": 56,
                "block_error_page_message": "block_error_page_message_example",
                "block_error_page_code": "block_error_page_code_example",
                "block_error_page_description": "block_error_page_description_example",
                "max_argument_count": 56,
                "max_name_length_per_argument": 56,
                "max_total_name_length_of_arguments": 56,
                "recommendations_period_in_days": 56,
                "is_response_inspected": true,
                "max_response_size_in_ki_b": 56,
                "allowed_http_methods": [],
                "media_types": []
            },
            "threat_feeds": [{
                "key": "key_example",
                "name": "name_example",
                "action": "OFF",
                "description": "description_example"
            }],
            "whitelists": [{
                "name": "name_example",
                "addresses": []
            }]
        },
        "freeform_tags": {Department: Finance},
        "defined_tags": {Operations: {CostCenter: US}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.waas import WaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WaasPolicyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return ["waas_policy_id"]

    def get_required_params_for_list(self):
        return ["compartment_id"]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_waas_policy,
            waas_policy_id=self.module.params.get("waas_policy_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "id",
            "display_name",
            "lifecycle_state",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_waas_policies,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


WaasPolicyFactsHelperCustom = get_custom_class("WaasPolicyFactsHelperCustom")


class ResourceFactsHelper(WaasPolicyFactsHelperCustom, WaasPolicyFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            waas_policy_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["id", "displayName", "timeCreated"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            id=dict(type="list"),
            display_name=dict(aliases=["name"], type="list"),
            lifecycle_state=dict(type="list"),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module, resource_type="waas_policy", service_client_class=WaasClient
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(waas_policies=result)


if __name__ == "__main__":
    main()
