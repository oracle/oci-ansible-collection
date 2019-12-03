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
module: oci_waas_policy
short_description: Manage a WaasPolicy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a WaasPolicy resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Web Application Acceleration and Security (WAAS) policy in the specified compartment. A WAAS policy must be
      established before creating Web Application Firewall (WAF) rules. To use WAF rules, your web application's origin servers must defined in the `WaasPolicy`
      schema.
    - A domain name must be specified when creating a WAAS policy. The domain name should be different from the origins specified in your `WaasPolicy`. Once
      domain name is entered and stored, it is unchangeable.
    - Use the record data returned in the `cname` field of the `WaasPolicy` object to create a CNAME record in your DNS configuration that will direct your
      domain's traffic through the WAF.
    - For the purposes of access control, you must provide the OCID of the compartment where you want the service to reside. For information about access
      control and compartments, see L(Overview of the IAM Service,https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
    - You must specify a display name and domain for the WAAS policy. The display name does not have to be unique and can be changed. The domain name should be
      different from every origin specified in `WaasPolicy`.
    - All Oracle Cloud Infrastructure resources, including WAAS policies, receive a unique, Oracle-assigned ID called an Oracle Cloud Identifier (OCID). When a
      resource is created, you can find its OCID in the response. You can also retrieve a resource's OCID by using a list API operation for that resource type,
      or by viewing the resource in the Console. Fore more information, see L(Resource
      Identifiers,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    - "**Note:** After sending the POST request, the new object's state will temporarily be `CREATING`. Ensure that the resource's state has changed to `ACTIVE`
      before use."
    - "This resource has the following action operations in the M(oci_waas_policy_actions) module: accept_recommendations."
version_added: "2.5"
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which to create the WAAS policy.
            - Required for create using I(state=present).
    display_name:
        description:
            - A user-friendly name for the WAAS policy. The name is can be changed and does not need to be unique.
        aliases: ["name"]
    domain:
        description:
            - The web application domain that the WAAS policy protects.
            - Required for create using I(state=present).
    additional_domains:
        description:
            - An array of additional domains for the specified web application.
        type: list
    origins:
        description:
            - A map of host to origin for the web application. The key should be a customer friendly name for the host, ex. primary, secondary, etc.
        type: dict
        suboptions:
            uri:
                description:
                    - The URI of the origin. Does not support paths. Port numbers should be specified in the `httpPort` and `httpsPort` fields.
                required: true
            http_port:
                description:
                    - The HTTP port on the origin that the web application listens on. If unspecified, defaults to `80`.
                type: int
            https_port:
                description:
                    - The HTTPS port on the origin that the web application listens on. If unspecified, defaults to `443`.
                type: int
            custom_headers:
                description:
                    - A list of HTTP headers to forward to your origin.
                type: list
                suboptions:
                    name:
                        description:
                            - The name of the header.
                        required: true
                    value:
                        description:
                            - The value of the header.
                        required: true
    policy_config:
        description:
            - ""
        type: dict
        suboptions:
            certificate_id:
                description:
                    - The OCID of the SSL certificate to use if HTTPS is supported.
            is_https_enabled:
                description:
                    - Enable or disable HTTPS support. If true, a `certificateId` is required. If unspecified, defaults to `false`.
                type: bool
            is_https_forced:
                description:
                    - Force HTTP to HTTPS redirection. If unspecified, defaults to `false`.
                type: bool
    waf_config:
        description:
            - ""
        type: dict
        suboptions:
            access_rules:
                description:
                    - The access rules applied to the Web Application Firewall. Used for defining custom access policies with the combination of `ALLOW`,
                      `DETECT`, and `BLOCK` rules, based on different criteria.
                type: list
                suboptions:
                    name:
                        description:
                            - The unique name of the access rule.
                        required: true
                    criteria:
                        description:
                            - The list of access rule criteria.
                        type: list
                        required: true
                        suboptions:
                            condition:
                                description:
                                    - The criteria the access rule uses to determine if action should be taken on a request.
                                    - "- **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value`
                                      field.
                                      - **URL_IS_NOT:** Matches if the concatenation of request URL path and query is not identical to the contents of the
                                        `value` field.
                                      - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value`
                                        field.
                                      - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value`
                                        field.
                                      - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value`
                                        field.
                                      - **URL_REGEX:** Matches if the request is described by the regular expression in the `value` field.
                                      - **IP_IS:** Matches if the request originates from an IP address in the `value` field.
                                      - **IP_IS_NOT:** Matches if the request does not originate from an IP address in the `value` field.
                                      - **HTTP_HEADER_CONTAINS:** Matches if the request includes an HTTP header field whose name and value correspond to data
                                        specified in the `value` field with a separating colon. **Example:** `host:test.example.com` where `host` is the name of
                                        the field and `test.example.com` is the value of the host field. Comparison is independently applied to every header
                                        field whose name is a case insensitive match, and the value is required to be case-sensitive identical.
                                      - **COUNTRY_IS:** Matches if the request originates from a country in the `value` field. Country codes are in ISO 3166-1
                                        alpha-2 format. For a list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                                      - **COUNTRY_IS_NOT:** Matches if the request does not originate from a country in the `value` field. Country codes are in
                                        ISO 3166-1 alpha-2 format. For a list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                                      - **USER_AGENT_IS:** Matches if the requesting user agent is identical to the contents of the `value` field. Example:
                                        `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`
                                      - **USER_AGENT_IS_NOT:** Matches if the requesting user agent is not identical to the contents of the `value` field.
                                        Example: `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`"
                                choices:
                                    - "URL_IS"
                                    - "URL_IS_NOT"
                                    - "URL_STARTS_WITH"
                                    - "URL_PART_ENDS_WITH"
                                    - "URL_PART_CONTAINS"
                                    - "URL_REGEX"
                                    - "IP_IS"
                                    - "IP_IS_NOT"
                                    - "HTTP_HEADER_CONTAINS"
                                    - "COUNTRY_IS"
                                    - "COUNTRY_IS_NOT"
                                    - "USER_AGENT_IS"
                                    - "USER_AGENT_IS_NOT"
                                required: true
                            value:
                                description:
                                    - The criteria value.
                                required: true
                    action:
                        description:
                            - The action to take when the access criteria are met for a rule. If unspecified, defaults to `ALLOW`.
                        choices:
                            - "ALLOW"
                            - "DETECT"
                            - "BLOCK"
                        required: true
                    block_action:
                        description:
                            - The method used to block requests if `action` is set to `BLOCK` and the access criteria are met. If unspecified, defaults to
                              `SET_RESPONSE_CODE`.
                        choices:
                            - "SET_RESPONSE_CODE"
                            - "SHOW_ERROR_PAGE"
                    block_response_code:
                        description:
                            - The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the access
                              criteria are met. If unspecified, defaults to `403`.
                        type: int
                    block_error_page_message:
                        description:
                            - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access
                              criteria are met. If unspecified, defaults to 'Access to the website is blocked.'
                    block_error_page_code:
                        description:
                            - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                              access criteria are met. If unspecified, defaults to 'Access rules'.
                    block_error_page_description:
                        description:
                            - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                              access criteria are met. If unspecified, defaults to 'Access blocked by website owner. Please contact support.'
            address_rate_limiting:
                description:
                    - The IP address rate limiting settings used to limit the number of requests from an address.
                type: dict
                suboptions:
                    is_enabled:
                        description:
                            - Enables or disables the address rate limiting Web Application Firewall feature.
                        type: bool
                        required: true
                    allowed_rate_per_address:
                        description:
                            - The number of allowed requests per second from one IP address. If unspecified, defaults to `1`.
                        type: int
                    max_delayed_count_per_address:
                        description:
                            - The maximum number of requests allowed to be queued before subsequent requests are dropped. If unspecified, defaults to `10`.
                        type: int
                    block_response_code:
                        description:
                            - The response status code returned when a request is blocked. If unspecified, defaults to `503`.
                        type: int
            captchas:
                description:
                    - A list of CAPTCHA challenge settings. These are used to challenge requests with a CAPTCHA to block bots.
                type: list
                suboptions:
                    url:
                        description:
                            - The unique URL path at which to show the CAPTCHA challenge.
                        required: true
                    session_expiration_in_seconds:
                        description:
                            - The amount of time before the CAPTCHA expires, in seconds. If unspecified, defaults to `300`.
                        type: int
                        required: true
                    title:
                        description:
                            - The title used when displaying a CAPTCHA challenge. If unspecified, defaults to `Are you human?`
                        required: true
                    header_text:
                        description:
                            - The text to show in the header when showing a CAPTCHA challenge. If unspecified, defaults to 'We have detected an increased number
                              of attempts to access this website. To help us keep this site secure, please let us know that you are not a robot by entering the
                              text from the image below.'
                    footer_text:
                        description:
                            - The text to show in the footer when showing a CAPTCHA challenge. If unspecified, defaults to 'Enter the letters and numbers as
                              they are shown in the image above.'
                    failure_message:
                        description:
                            - The text to show when incorrect CAPTCHA text is entered. If unspecified, defaults to `The CAPTCHA was incorrect. Try again.`
                        required: true
                    submit_label:
                        description:
                            - The text to show on the label of the CAPTCHA challenge submit button. If unspecified, defaults to `Yes, I am human`.
                        required: true
            device_fingerprint_challenge:
                description:
                    - The device fingerprint challenge settings. Used to detect unique devices based on the device fingerprint information collected in order to
                      block bots.
                type: dict
                suboptions:
                    is_enabled:
                        description:
                            - Enables or disables the device fingerprint challenge Web Application Firewall feature.
                        type: bool
                        required: true
                    action:
                        description:
                            - The action to take on requests from detected bots. If unspecified, defaults to `DETECT`.
                        choices:
                            - "DETECT"
                            - "BLOCK"
                    failure_threshold:
                        description:
                            - The number of failed requests allowed before taking action. If unspecified, defaults to `10`.
                        type: int
                    action_expiration_in_seconds:
                        description:
                            - The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.
                        type: int
                    failure_threshold_expiration_in_seconds:
                        description:
                            - The number of seconds before the failure threshold resets. If unspecified, defaults to `60`.
                        type: int
                    max_address_count:
                        description:
                            - The maximum number of IP addresses permitted with the same device fingerprint. If unspecified, defaults to `20`.
                        type: int
                    max_address_count_expiration_in_seconds:
                        description:
                            - The number of seconds before the maximum addresses count resets. If unspecified, defaults to `60`.
                        type: int
                    challenge_settings:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            block_action:
                                description:
                                    - The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to
                                      `SHOW_ERROR_PAGE`.
                                choices:
                                    - "SET_RESPONSE_CODE"
                                    - "SHOW_ERROR_PAGE"
                                    - "SHOW_CAPTCHA"
                            block_response_code:
                                description:
                                    - The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or
                                      `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`.
                                type: int
                            block_error_page_message:
                                description:
                                    - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                                      request is blocked. If unspecified, defaults to `Access to the website is blocked`.
                            block_error_page_description:
                                description:
                                    - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`,
                                      and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
                            block_error_page_code:
                                description:
                                    - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and
                                      the request is blocked. If unspecified, defaults to `403`.
                            captcha_title:
                                description:
                                    - The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`,
                                      and the request is blocked. If unspecified, defaults to `Are you human?`
                            captcha_header:
                                description:
                                    - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                      `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts
                                      to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the
                                      text from captcha below.`
                            captcha_footer:
                                description:
                                    - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                      `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in
                                      image above`.
                            captcha_submit_label:
                                description:
                                    - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set
                                      to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
            human_interaction_challenge:
                description:
                    - The human interaction challenge settings. Used to look for natural human interactions such as mouse movements, time on site, and page
                      scrolling to identify bots.
                type: dict
                suboptions:
                    is_enabled:
                        description:
                            - Enables or disables the human interaction challenge Web Application Firewall feature.
                        type: bool
                        required: true
                    action:
                        description:
                            - The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.
                        choices:
                            - "DETECT"
                            - "BLOCK"
                    failure_threshold:
                        description:
                            - The number of failed requests before taking action. If unspecified, defaults to `10`.
                        type: int
                    action_expiration_in_seconds:
                        description:
                            - The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.
                        type: int
                    failure_threshold_expiration_in_seconds:
                        description:
                            - The number of seconds before the failure threshold resets. If unspecified, defaults to  `60`.
                        type: int
                    interaction_threshold:
                        description:
                            - The number of interactions required to pass the challenge. If unspecified, defaults to `3`.
                        type: int
                    recording_period_in_seconds:
                        description:
                            - The number of seconds to record the interactions from the user. If unspecified, defaults to `15`.
                        type: int
                    set_http_header:
                        description:
                            - Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the
                              `action` is set to `DETECT`.
                        type: dict
                        suboptions:
                            name:
                                description:
                                    - The name of the header.
                                required: true
                            value:
                                description:
                                    - The value of the header.
                                required: true
                    challenge_settings:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            block_action:
                                description:
                                    - The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to
                                      `SHOW_ERROR_PAGE`.
                                choices:
                                    - "SET_RESPONSE_CODE"
                                    - "SHOW_ERROR_PAGE"
                                    - "SHOW_CAPTCHA"
                            block_response_code:
                                description:
                                    - The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or
                                      `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`.
                                type: int
                            block_error_page_message:
                                description:
                                    - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                                      request is blocked. If unspecified, defaults to `Access to the website is blocked`.
                            block_error_page_description:
                                description:
                                    - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`,
                                      and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
                            block_error_page_code:
                                description:
                                    - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and
                                      the request is blocked. If unspecified, defaults to `403`.
                            captcha_title:
                                description:
                                    - The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`,
                                      and the request is blocked. If unspecified, defaults to `Are you human?`
                            captcha_header:
                                description:
                                    - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                      `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts
                                      to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the
                                      text from captcha below.`
                            captcha_footer:
                                description:
                                    - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                      `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in
                                      image above`.
                            captcha_submit_label:
                                description:
                                    - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set
                                      to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
            js_challenge:
                description:
                    - The JavaScript challenge settings. Used to challenge requests with a JavaScript challenge and take the action if a browser has no
                      JavaScript support in order to block bots.
                type: dict
                suboptions:
                    is_enabled:
                        description:
                            - Enables or disables the JavaScript challenge Web Application Firewall feature.
                        type: bool
                        required: true
                    action:
                        description:
                            - The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.
                        choices:
                            - "DETECT"
                            - "BLOCK"
                    failure_threshold:
                        description:
                            - The number of failed requests before taking action. If unspecified, defaults to `10`.
                        type: int
                    action_expiration_in_seconds:
                        description:
                            - The number of seconds between challenges from the same IP address. If unspecified, defaults to `60`.
                        type: int
                    set_http_header:
                        description:
                            - Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the
                              `action` is set to `DETECT`.
                        type: dict
                        suboptions:
                            name:
                                description:
                                    - The name of the header.
                                required: true
                            value:
                                description:
                                    - The value of the header.
                                required: true
                    challenge_settings:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            block_action:
                                description:
                                    - The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to
                                      `SHOW_ERROR_PAGE`.
                                choices:
                                    - "SET_RESPONSE_CODE"
                                    - "SHOW_ERROR_PAGE"
                                    - "SHOW_CAPTCHA"
                            block_response_code:
                                description:
                                    - The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or
                                      `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`.
                                type: int
                            block_error_page_message:
                                description:
                                    - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                                      request is blocked. If unspecified, defaults to `Access to the website is blocked`.
                            block_error_page_description:
                                description:
                                    - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`,
                                      and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
                            block_error_page_code:
                                description:
                                    - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and
                                      the request is blocked. If unspecified, defaults to `403`.
                            captcha_title:
                                description:
                                    - The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`,
                                      and the request is blocked. If unspecified, defaults to `Are you human?`
                            captcha_header:
                                description:
                                    - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                      `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts
                                      to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the
                                      text from captcha below.`
                            captcha_footer:
                                description:
                                    - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                      `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in
                                      image above`.
                            captcha_submit_label:
                                description:
                                    - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set
                                      to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
            origin:
                description:
                    - The key in the map of origins referencing the origin used for the Web Application Firewall. The origin must already be included in
                      `Origins`. Required when creating the `WafConfig` resource, but not on update.
            protection_settings:
                description:
                    - The settings to apply to protection rules.
                type: dict
                suboptions:
                    block_action:
                        description:
                            - If `action` is set to `BLOCK`, this specifies how the traffic is blocked when detected as malicious by a protection rule. If
                              unspecified, defaults to `SET_RESPONSE_CODE`.
                        choices:
                            - "SHOW_ERROR_PAGE"
                            - "SET_RESPONSE_CODE"
                    block_response_code:
                        description:
                            - The response code returned when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the traffic is
                              detected as malicious by a protection rule. If unspecified, defaults to `403`.
                        type: int
                    block_error_page_message:
                        description:
                            - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic
                              is detected as malicious by a protection rule. If unspecified, defaults to 'Access to the website is blocked.'
                    block_error_page_code:
                        description:
                            - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                              traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`.
                    block_error_page_description:
                        description:
                            - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                              traffic is detected as malicious by a protection rule. If unspecified, defaults to `Access blocked by website owner. Please
                              contact support.`
                    max_argument_count:
                        description:
                            - The maximum number of arguments allowed to be passed to your application before an action is taken. If unspecified, defaults to
                              `255`.
                        type: int
                    max_name_length_per_argument:
                        description:
                            - The maximum length allowed for each argument name, in characters. If unspecified, defaults to `400`.
                        type: int
                    max_total_name_length_of_arguments:
                        description:
                            - The maximum length allowed for the sum of all argument names, in characters. If unspecified, defaults to `64000`.
                        type: int
                    recommendations_period_in_days:
                        description:
                            - The length of time to analyze traffic traffic, in days. After the analysis period, `WafRecommendations` will be populated. If
                              unspecified, defaults to `10`.
                            - Use `GET /waasPolicies/{waasPolicyId}/wafRecommendations` to view WAF recommendations.
                        type: int
                    is_response_inspected:
                        description:
                            - Inspects the response body of origin responses. Can be used to detect leakage of sensitive data. If unspecified, defaults to
                              `false`.
                            - "**Note:** Only origin responses with a Content-Type matching a value in `mediaTypes` will be inspected."
                        type: bool
                    max_response_size_in_ki_b:
                        description:
                            - The maximum response size to be fully inspected, in binary kilobytes (KiB). Anything over this limit will be partially inspected.
                              If unspecified, defaults to `1024`.
                        type: int
                    allowed_http_methods:
                        description:
                            - The list of allowed HTTP methods. If unspecified, default to `[OPTIONS, GET, HEAD, POST]`.
                        type: list
                        choices:
                            - "OPTIONS"
                            - "GET"
                            - "HEAD"
                            - "POST"
                            - "PUT"
                            - "DELETE"
                            - "TRACE"
                            - "CONNECT"
                            - "PATCH"
                            - "PROPFIND"
                    media_types:
                        description:
                            - The list of media types to allow for inspection, if `isResponseInspected` is enabled. Only responses with MIME types in this list
                              will be inspected. If unspecified, defaults to `[`text/html`, `text/plain`, `text/xml`]`.
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
                        type: list
            whitelists:
                description:
                    - A list of IP addresses that bypass the Web Application Firewall.
                type: list
                suboptions:
                    name:
                        description:
                            - The unique name of the whitelist.
                        required: true
                    addresses:
                        description:
                            - A set of IP addresses or CIDR notations to include in the whitelist.
                        type: list
                        required: true
            good_bots:
                description:
                    - A list of bots allowed to access the web application.
                type: list
                suboptions:
                    key:
                        description:
                            - The unique key for the bot.
                        required: true
                    name:
                        description:
                            - The bot name.
                    is_enabled:
                        description:
                            - Enables or disables the bot.
                        type: bool
                        required: true
                    description:
                        description:
                            - The description of the bot.
            protection_rules:
                description:
                    - A list of the protection rules and their details.
                type: list
                suboptions:
                    key:
                        description:
                            - The unique key of the protection rule.
                    mod_security_rule_ids:
                        description:
                            - The list of the ModSecurity rule IDs that apply to this protection rule. For more information about ModSecurity's open source WAF
                              rules, see L(Mod Security's documentation,https://www.modsecurity.org/CRS/Documentation/index.html).
                        type: list
                    name:
                        description:
                            - The name of the protection rule.
                    description:
                        description:
                            - The description of the protection rule.
                    action:
                        description:
                            - The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.
                        choices:
                            - "OFF"
                            - "DETECT"
                            - "BLOCK"
                    labels:
                        description:
                            - The list of labels for the protection rule.
                            - "**Note:** Protection rules with a `ResponseBody` label will have no effect unless `isResponseInspected` is true."
                        type: list
                    exclusions:
                        description:
                            - ""
                        type: list
                        suboptions:
                            target:
                                description:
                                    - The target of the exclusion.
                                choices:
                                    - "REQUEST_COOKIES"
                                    - "REQUEST_COOKIE_NAMES"
                                    - "ARGS"
                                    - "ARGS_NAMES"
                            exclusions:
                                description:
                                    - ""
                                type: list
            threat_feeds:
                description:
                    - A list of threat intelligence feeds and the actions to apply to known malicious traffic based on internet intelligence.
                type: list
                suboptions:
                    key:
                        description:
                            - The unique key of the threat intelligence feed.
                    name:
                        description:
                            - The name of the threat intelligence feed.
                    action:
                        description:
                            - The action to take when traffic is flagged as malicious by data from the threat intelligence feed. If unspecified, defaults to
                              `OFF`.
                        choices:
                            - "OFF"
                            - "DETECT"
                            - "BLOCK"
                    description:
                        description:
                            - The description of the threat intelligence feed.
    freeform_tags:
        description:
            - A simple key-value pair without any defined schema.
        type: dict
    defined_tags:
        description:
            - A key-value pair with a defined schema that restricts the values of tags. These predefined keys are scoped to namespaces.
        type: dict
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
            - Required for update using I(state=present), I(state=absent).
        aliases: ["id"]
    state:
        description:
            - The state of the WaasPolicy.
            - Use I(state=present) to create or update a WaasPolicy.
            - Use I(state=absent) to delete a WaasPolicy.
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
- name: Create waas_policy
  oci_waas_policy:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    domain: domain_example

- name: Update waas_policy
  oci_waas_policy:
    display_name: display_name_example
    origins:
      uri: uri_example
    waas_policy_id: ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete waas_policy
  oci_waas_policy:
    waas_policy_id: ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
waas_policy:
    description:
        - Details of the WaasPolicy resource acted upon by the current operation
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
    sample: {
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
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.waas import WaasClient
    from oci.waas.models import CreateWaasPolicyDetails
    from oci.waas.models import UpdateWaasPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WaasPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    @staticmethod
    def get_module_resource_id_param():
        return "waas_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("waas_policy_id")

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_waas_policy,
            waas_policy_id=self.module.params.get("waas_policy_id"),
        )

    def list_resources(self):
        required_list_method_params = ["compartment_id"]

        optional_list_method_params = ["display_name"]

        required_kwargs = dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

        return oci_common_utils.list_all_resources(
            self.client.list_waas_policies, **kwargs
        )

    def get_create_model_class(self):
        return CreateWaasPolicyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_common_utils.call_with_backoff(
            self.client.create_waas_policy, create_waas_policy_details=create_details
        )

    def get_update_model_class(self):
        return UpdateWaasPolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_common_utils.call_with_backoff(
            self.client.update_waas_policy,
            waas_policy_id=self.module.params.get("waas_policy_id"),
            update_waas_policy_details=update_details,
        )

    def delete_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.delete_waas_policy,
            waas_policy_id=self.module.params.get("waas_policy_id"),
        )


WaasPolicyHelperCustom = get_custom_class("WaasPolicyHelperCustom")


class ResourceHelper(WaasPolicyHelperCustom, WaasPolicyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            domain=dict(type="str"),
            additional_domains=dict(type="list"),
            origins=dict(type="dict"),
            policy_config=dict(
                type="dict",
                options=dict(
                    certificate_id=dict(type="str"),
                    is_https_enabled=dict(type="bool"),
                    is_https_forced=dict(type="bool"),
                ),
            ),
            waf_config=dict(
                type="dict",
                options=dict(
                    access_rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str", required=True),
                            criteria=dict(
                                type="list",
                                elements="dict",
                                required=True,
                                options=dict(
                                    condition=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "URL_IS",
                                            "URL_IS_NOT",
                                            "URL_STARTS_WITH",
                                            "URL_PART_ENDS_WITH",
                                            "URL_PART_CONTAINS",
                                            "URL_REGEX",
                                            "IP_IS",
                                            "IP_IS_NOT",
                                            "HTTP_HEADER_CONTAINS",
                                            "COUNTRY_IS",
                                            "COUNTRY_IS_NOT",
                                            "USER_AGENT_IS",
                                            "USER_AGENT_IS_NOT",
                                        ],
                                    ),
                                    value=dict(type="str", required=True),
                                ),
                            ),
                            action=dict(
                                type="str",
                                required=True,
                                choices=["ALLOW", "DETECT", "BLOCK"],
                            ),
                            block_action=dict(
                                type="str",
                                choices=["SET_RESPONSE_CODE", "SHOW_ERROR_PAGE"],
                            ),
                            block_response_code=dict(type="int"),
                            block_error_page_message=dict(type="str"),
                            block_error_page_code=dict(type="str"),
                            block_error_page_description=dict(type="str"),
                        ),
                    ),
                    address_rate_limiting=dict(
                        type="dict",
                        options=dict(
                            is_enabled=dict(type="bool", required=True),
                            allowed_rate_per_address=dict(type="int"),
                            max_delayed_count_per_address=dict(type="int"),
                            block_response_code=dict(type="int"),
                        ),
                    ),
                    captchas=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            url=dict(type="str", required=True),
                            session_expiration_in_seconds=dict(
                                type="int", required=True
                            ),
                            title=dict(type="str", required=True),
                            header_text=dict(type="str"),
                            footer_text=dict(type="str"),
                            failure_message=dict(type="str", required=True),
                            submit_label=dict(type="str", required=True),
                        ),
                    ),
                    device_fingerprint_challenge=dict(
                        type="dict",
                        options=dict(
                            is_enabled=dict(type="bool", required=True),
                            action=dict(type="str", choices=["DETECT", "BLOCK"]),
                            failure_threshold=dict(type="int"),
                            action_expiration_in_seconds=dict(type="int"),
                            failure_threshold_expiration_in_seconds=dict(type="int"),
                            max_address_count=dict(type="int"),
                            max_address_count_expiration_in_seconds=dict(type="int"),
                            challenge_settings=dict(
                                type="dict",
                                options=dict(
                                    block_action=dict(
                                        type="str",
                                        choices=[
                                            "SET_RESPONSE_CODE",
                                            "SHOW_ERROR_PAGE",
                                            "SHOW_CAPTCHA",
                                        ],
                                    ),
                                    block_response_code=dict(type="int"),
                                    block_error_page_message=dict(type="str"),
                                    block_error_page_description=dict(type="str"),
                                    block_error_page_code=dict(type="str"),
                                    captcha_title=dict(type="str"),
                                    captcha_header=dict(type="str"),
                                    captcha_footer=dict(type="str"),
                                    captcha_submit_label=dict(type="str"),
                                ),
                            ),
                        ),
                    ),
                    human_interaction_challenge=dict(
                        type="dict",
                        options=dict(
                            is_enabled=dict(type="bool", required=True),
                            action=dict(type="str", choices=["DETECT", "BLOCK"]),
                            failure_threshold=dict(type="int"),
                            action_expiration_in_seconds=dict(type="int"),
                            failure_threshold_expiration_in_seconds=dict(type="int"),
                            interaction_threshold=dict(type="int"),
                            recording_period_in_seconds=dict(type="int"),
                            set_http_header=dict(
                                type="dict",
                                options=dict(
                                    name=dict(type="str", required=True),
                                    value=dict(type="str", required=True),
                                ),
                            ),
                            challenge_settings=dict(
                                type="dict",
                                options=dict(
                                    block_action=dict(
                                        type="str",
                                        choices=[
                                            "SET_RESPONSE_CODE",
                                            "SHOW_ERROR_PAGE",
                                            "SHOW_CAPTCHA",
                                        ],
                                    ),
                                    block_response_code=dict(type="int"),
                                    block_error_page_message=dict(type="str"),
                                    block_error_page_description=dict(type="str"),
                                    block_error_page_code=dict(type="str"),
                                    captcha_title=dict(type="str"),
                                    captcha_header=dict(type="str"),
                                    captcha_footer=dict(type="str"),
                                    captcha_submit_label=dict(type="str"),
                                ),
                            ),
                        ),
                    ),
                    js_challenge=dict(
                        type="dict",
                        options=dict(
                            is_enabled=dict(type="bool", required=True),
                            action=dict(type="str", choices=["DETECT", "BLOCK"]),
                            failure_threshold=dict(type="int"),
                            action_expiration_in_seconds=dict(type="int"),
                            set_http_header=dict(
                                type="dict",
                                options=dict(
                                    name=dict(type="str", required=True),
                                    value=dict(type="str", required=True),
                                ),
                            ),
                            challenge_settings=dict(
                                type="dict",
                                options=dict(
                                    block_action=dict(
                                        type="str",
                                        choices=[
                                            "SET_RESPONSE_CODE",
                                            "SHOW_ERROR_PAGE",
                                            "SHOW_CAPTCHA",
                                        ],
                                    ),
                                    block_response_code=dict(type="int"),
                                    block_error_page_message=dict(type="str"),
                                    block_error_page_description=dict(type="str"),
                                    block_error_page_code=dict(type="str"),
                                    captcha_title=dict(type="str"),
                                    captcha_header=dict(type="str"),
                                    captcha_footer=dict(type="str"),
                                    captcha_submit_label=dict(type="str"),
                                ),
                            ),
                        ),
                    ),
                    origin=dict(type="str"),
                    protection_settings=dict(
                        type="dict",
                        options=dict(
                            block_action=dict(
                                type="str",
                                choices=["SHOW_ERROR_PAGE", "SET_RESPONSE_CODE"],
                            ),
                            block_response_code=dict(type="int"),
                            block_error_page_message=dict(type="str"),
                            block_error_page_code=dict(type="str"),
                            block_error_page_description=dict(type="str"),
                            max_argument_count=dict(type="int"),
                            max_name_length_per_argument=dict(type="int"),
                            max_total_name_length_of_arguments=dict(type="int"),
                            recommendations_period_in_days=dict(type="int"),
                            is_response_inspected=dict(type="bool"),
                            max_response_size_in_ki_b=dict(type="int"),
                            allowed_http_methods=dict(
                                type="list",
                                choices=[
                                    "OPTIONS",
                                    "GET",
                                    "HEAD",
                                    "POST",
                                    "PUT",
                                    "DELETE",
                                    "TRACE",
                                    "CONNECT",
                                    "PATCH",
                                    "PROPFIND",
                                ],
                            ),
                            media_types=dict(type="list"),
                        ),
                    ),
                    whitelists=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str", required=True),
                            addresses=dict(type="list", required=True),
                        ),
                    ),
                    good_bots=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            key=dict(type="str", required=True),
                            name=dict(type="str"),
                            is_enabled=dict(type="bool", required=True),
                            description=dict(type="str"),
                        ),
                    ),
                    protection_rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            key=dict(type="str"),
                            mod_security_rule_ids=dict(type="list"),
                            name=dict(type="str"),
                            description=dict(type="str"),
                            action=dict(type="str", choices=["OFF", "DETECT", "BLOCK"]),
                            labels=dict(type="list"),
                            exclusions=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    target=dict(
                                        type="str",
                                        choices=[
                                            "REQUEST_COOKIES",
                                            "REQUEST_COOKIE_NAMES",
                                            "ARGS",
                                            "ARGS_NAMES",
                                        ],
                                    ),
                                    exclusions=dict(type="list"),
                                ),
                            ),
                        ),
                    ),
                    threat_feeds=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            key=dict(type="str"),
                            name=dict(type="str"),
                            action=dict(type="str", choices=["OFF", "DETECT", "BLOCK"]),
                            description=dict(type="str"),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            waas_policy_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module, resource_type="waas_policy", service_client_class=WaasClient
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
