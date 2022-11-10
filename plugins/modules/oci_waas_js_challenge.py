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
module: oci_waas_js_challenge
short_description: Manage a JsChallenge resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a JsChallenge resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        aliases: ["id"]
        required: true
    is_enabled:
        description:
            - Enables or disables the JavaScript challenge Web Application Firewall feature.
        type: bool
        required: true
    action:
        description:
            - The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.
            - This parameter is updatable.
        type: str
        choices:
            - "DETECT"
            - "BLOCK"
    failure_threshold:
        description:
            - The number of failed requests before taking action. If unspecified, defaults to `10`.
            - This parameter is updatable.
        type: int
    action_expiration_in_seconds:
        description:
            - The number of seconds between challenges from the same IP address. If unspecified, defaults to `60`.
            - This parameter is updatable.
        type: int
    set_http_header:
        description:
            - Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the `action` is set to
              `DETECT`.
            - This parameter is updatable.
        type: dict
        suboptions:
            name:
                description:
                    - The name of the header.
                    - This parameter is updatable.
                type: str
                required: true
            value:
                description:
                    - The value of the header.
                    - This parameter is updatable.
                type: str
                required: true
    challenge_settings:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            block_action:
                description:
                    - The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to `SHOW_ERROR_PAGE`.
                    - This parameter is updatable.
                type: str
                choices:
                    - "SET_RESPONSE_CODE"
                    - "SHOW_ERROR_PAGE"
                    - "SHOW_CAPTCHA"
            block_response_code:
                description:
                    - "The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or `SHOW_ERROR_PAGE`, and
                      the request is blocked. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`,
                      `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`,
                      `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`."
                    - This parameter is updatable.
                type: int
            block_error_page_message:
                description:
                    - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is
                      blocked. If unspecified, defaults to `Access to the website is blocked`.
                    - This parameter is updatable.
                type: str
            block_error_page_description:
                description:
                    - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request
                      is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
                    - This parameter is updatable.
                type: str
            block_error_page_code:
                description:
                    - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and the request is
                      blocked. If unspecified, defaults to `403`.
                    - This parameter is updatable.
                type: str
            captcha_title:
                description:
                    - The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request
                      is blocked. If unspecified, defaults to `Are you human?`
                    - This parameter is updatable.
                type: str
            captcha_header:
                description:
                    - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`,
                      and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts to access this webapp. To help
                      us keep this webapp secure, please let us know that you are not a robot by entering the text from captcha below.`
                    - This parameter is updatable.
                type: str
            captcha_footer:
                description:
                    - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`,
                      and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in image above`.
                    - This parameter is updatable.
                type: str
            captcha_submit_label:
                description:
                    - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set to
                      `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
                    - This parameter is updatable.
                type: str
    are_redirects_challenged:
        description:
            - When enabled, redirect responses from the origin will also be challenged. This will change HTTP 301/302 responses from origin to HTTP 200 with an
              HTML body containing JavaScript page redirection.
            - This parameter is updatable.
        type: bool
    criteria:
        description:
            - When defined, the JavaScript Challenge would be applied only for the requests that matched all the listed conditions.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            condition:
                description:
                    - "The criteria the access rule and JavaScript Challenge uses to determine if action should be taken on a request.
                      - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value` field. URL must start
                        with a `/`.
                      - **URL_IS_NOT:** Matches if the concatenation of request URL path and query is not identical to the contents of the `value` field. URL
                        must start with a `/`.
                      - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value` field. URL must
                        start with a `/`.
                      - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value` field.
                      - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value` field.
                      - **URL_REGEX:** Matches if the concatenation of request URL path and query is described by the regular expression in the value field. The
                        value must be a valid regular expression recognized by the PCRE library in Nginx (https://www.pcre.org).
                      - **URL_DOES_NOT_MATCH_REGEX:** Matches if the concatenation of request URL path and query is not described by the regular expression in
                        the `value` field. The value must be a valid regular expression recognized by the PCRE library in Nginx (https://www.pcre.org).
                      - **URL_DOES_NOT_START_WITH:** Matches if the concatenation of request URL path and query does not start with the contents of the `value`
                        field.
                      - **URL_PART_DOES_NOT_CONTAIN:** Matches if the concatenation of request URL path and query does not contain the contents of the `value`
                        field.
                      - **URL_PART_DOES_NOT_END_WITH:** Matches if the concatenation of request URL path and query does not end with the contents of the `value`
                        field.
                      - **IP_IS:** Matches if the request originates from one of the IP addresses contained in the defined address list. The `value` in this
                        case is string with one or multiple IPs or CIDR notations separated by new line symbol \\\\n
                      *Example:* \\"1.1.1.1\\\\n1.1.1.2\\\\n1.2.2.1/30\\"
                      - **IP_IS_NOT:** Matches if the request does not originate from any of the IP addresses contained in the defined address list. The `value`
                        in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \\\\n
                      *Example:* \\"1.1.1.1\\\\n1.1.1.2\\\\n1.2.2.1/30\\"
                      - **IP_IN_LIST:** Matches if the request originates from one of the IP addresses contained in the referenced address list. The `value` in
                        this case is OCID of the address list.
                      - **IP_NOT_IN_LIST:** Matches if the request does not originate from any IP address contained in the referenced address list. The `value`
                        field in this case is OCID of the address list.
                      - **HTTP_HEADER_CONTAINS:** The HTTP_HEADER_CONTAINS criteria is defined using a compound value separated by a colon: a header field name
                        and a header field value. `host:test.example.com` is an example of a criteria value where `host` is the header field name and
                        `test.example.com` is the header field value. A request matches when the header field name is a case insensitive match and the header
                        field value is a case insensitive, substring match.
                      *Example:* With a criteria value of `host:test.example.com`, where `host` is the name of the field and `test.example.com` is the value of
                      the host field, a request with the header values, `Host: www.test.example.com` will match, where as a request with header values of `host:
                      www.example.com` or `host: test.sub.example.com` will not match.
                      - **HTTP_METHOD_IS:** Matches if the request method is identical to one of the values listed in field. The `value` in this case is string
                        with one or multiple HTTP methods separated by new line symbol \\\\n The list of available methods: `GET`, `HEAD`, `POST`, `PUT`,
                        `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`"
                    - "*Example:* \\"GET\\\\nPOST\\""
                    - "- **HTTP_METHOD_IS_NOT:** Matches if the request is not identical to any of the contents of the `value` field. The `value` in this case
                      is string with one or multiple HTTP methods separated by new line symbol \\\\n The list of available methods: `GET`, `HEAD`, `POST`,
                      `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`"
                    - "*Example:* \\"GET\\\\nPOST\\""
                    - "- **COUNTRY_IS:** Matches if the request originates from one of countries in the `value` field. The `value` in this case is string with
                      one or multiple countries separated by new line symbol \\\\n Country codes are in ISO 3166-1 alpha-2 format. For a list of codes, see
                      L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                      *Example:* \\"AL\\\\nDZ\\\\nAM\\"
                      - **COUNTRY_IS_NOT:** Matches if the request does not originate from any of countries in the `value` field. The `value` in this case is
                        string with one or multiple countries separated by new line symbol \\\\n Country codes are in ISO 3166-1 alpha-2 format. For a list of
                        codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                      *Example:* \\"AL\\\\nDZ\\\\nAM\\"
                      - **USER_AGENT_IS:** Matches if the requesting user agent is identical to the contents of the `value` field.
                      *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`
                      - **USER_AGENT_IS_NOT:** Matches if the requesting user agent is not identical to the contents of the `value` field.
                      *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`"
                    - This parameter is updatable.
                type: str
                choices:
                    - "URL_IS"
                    - "URL_IS_NOT"
                    - "URL_STARTS_WITH"
                    - "URL_PART_ENDS_WITH"
                    - "URL_PART_CONTAINS"
                    - "URL_REGEX"
                    - "URL_DOES_NOT_MATCH_REGEX"
                    - "URL_DOES_NOT_START_WITH"
                    - "URL_PART_DOES_NOT_CONTAIN"
                    - "URL_PART_DOES_NOT_END_WITH"
                    - "IP_IS"
                    - "IP_IS_NOT"
                    - "IP_IN_LIST"
                    - "IP_NOT_IN_LIST"
                    - "HTTP_HEADER_CONTAINS"
                    - "HTTP_METHOD_IS"
                    - "HTTP_METHOD_IS_NOT"
                    - "COUNTRY_IS"
                    - "COUNTRY_IS_NOT"
                    - "USER_AGENT_IS"
                    - "USER_AGENT_IS_NOT"
                required: true
            value:
                description:
                    - The criteria value.
                    - This parameter is updatable.
                type: str
                required: true
            is_case_sensitive:
                description:
                    - When enabled, the condition will be matched with case-sensitive rules.
                    - This parameter is updatable.
                type: bool
    is_nat_enabled:
        description:
            - When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking visitors with
              shared IP addresses.
            - This parameter is updatable.
        type: bool
    state:
        description:
            - The state of the JsChallenge.
            - Use I(state=present) to update an existing a JsChallenge.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update js_challenge
  oci_waas_js_challenge:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"
    is_enabled: true

    # optional
    action: DETECT
    failure_threshold: 56
    action_expiration_in_seconds: 56
    set_http_header:
      # required
      name: name_example
      value: value_example
    challenge_settings:
      # optional
      block_action: SET_RESPONSE_CODE
      block_response_code: 56
      block_error_page_message: block_error_page_message_example
      block_error_page_description: block_error_page_description_example
      block_error_page_code: block_error_page_code_example
      captcha_title: captcha_title_example
      captcha_header: captcha_header_example
      captcha_footer: captcha_footer_example
      captcha_submit_label: captcha_submit_label_example
    are_redirects_challenged: true
    criteria:
    - # required
      condition: URL_IS
      value: value_example

      # optional
      is_case_sensitive: true
    is_nat_enabled: true

"""

RETURN = """
js_challenge:
    description:
        - Details of the JsChallenge resource acted upon by the current operation
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
            type: str
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
                - Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the `action` is set
                  to `DETECT`.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the header.
                    returned: on success
                    type: str
                    sample: name_example
                value:
                    description:
                        - The value of the header.
                    returned: on success
                    type: str
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
                    type: str
                    sample: SET_RESPONSE_CODE
                block_response_code:
                    description:
                        - "The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or `SHOW_ERROR_PAGE`,
                          and the request is blocked. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`,
                          `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`,
                          `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`."
                    returned: on success
                    type: int
                    sample: 56
                block_error_page_message:
                    description:
                        - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is
                          blocked. If unspecified, defaults to `Access to the website is blocked`.
                    returned: on success
                    type: str
                    sample: block_error_page_message_example
                block_error_page_description:
                    description:
                        - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                          request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
                    returned: on success
                    type: str
                    sample: block_error_page_description_example
                block_error_page_code:
                    description:
                        - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and the request is
                          blocked. If unspecified, defaults to `403`.
                    returned: on success
                    type: str
                    sample: block_error_page_code_example
                captcha_title:
                    description:
                        - The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the
                          request is blocked. If unspecified, defaults to `Are you human?`
                    returned: on success
                    type: str
                    sample: captcha_title_example
                captcha_header:
                    description:
                        - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                          `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts to access
                          this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the text from captcha below.`
                    returned: on success
                    type: str
                    sample: captcha_header_example
                captcha_footer:
                    description:
                        - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                          `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in image
                          above`.
                    returned: on success
                    type: str
                    sample: captcha_footer_example
                captcha_submit_label:
                    description:
                        - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set to
                          `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
                    returned: on success
                    type: str
                    sample: captcha_submit_label_example
        are_redirects_challenged:
            description:
                - When enabled, redirect responses from the origin will also be challenged. This will change HTTP 301/302 responses from origin to HTTP 200 with
                  an HTML body containing JavaScript page redirection.
            returned: on success
            type: bool
            sample: true
        criteria:
            description:
                - When defined, the JavaScript Challenge would be applied only for the requests that matched all the listed conditions.
            returned: on success
            type: complex
            contains:
                condition:
                    description:
                        - "The criteria the access rule and JavaScript Challenge uses to determine if action should be taken on a request.
                          - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value` field. URL must
                            start with a `/`.
                          - **URL_IS_NOT:** Matches if the concatenation of request URL path and query is not identical to the contents of the `value` field.
                            URL must start with a `/`.
                          - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value` field. URL
                            must start with a `/`.
                          - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value` field.
                          - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value` field.
                          - **URL_REGEX:** Matches if the concatenation of request URL path and query is described by the regular expression in the value field.
                            The value must be a valid regular expression recognized by the PCRE library in Nginx (https://www.pcre.org).
                          - **URL_DOES_NOT_MATCH_REGEX:** Matches if the concatenation of request URL path and query is not described by the regular expression
                            in the `value` field. The value must be a valid regular expression recognized by the PCRE library in Nginx (https://www.pcre.org).
                          - **URL_DOES_NOT_START_WITH:** Matches if the concatenation of request URL path and query does not start with the contents of the
                            `value` field.
                          - **URL_PART_DOES_NOT_CONTAIN:** Matches if the concatenation of request URL path and query does not contain the contents of the
                            `value` field.
                          - **URL_PART_DOES_NOT_END_WITH:** Matches if the concatenation of request URL path and query does not end with the contents of the
                            `value` field.
                          - **IP_IS:** Matches if the request originates from one of the IP addresses contained in the defined address list. The `value` in this
                            case is string with one or multiple IPs or CIDR notations separated by new line symbol \\\\n
                          *Example:* \\"1.1.1.1\\\\n1.1.1.2\\\\n1.2.2.1/30\\"
                          - **IP_IS_NOT:** Matches if the request does not originate from any of the IP addresses contained in the defined address list. The
                            `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \\\\n
                          *Example:* \\"1.1.1.1\\\\n1.1.1.2\\\\n1.2.2.1/30\\"
                          - **IP_IN_LIST:** Matches if the request originates from one of the IP addresses contained in the referenced address list. The `value`
                            in this case is OCID of the address list.
                          - **IP_NOT_IN_LIST:** Matches if the request does not originate from any IP address contained in the referenced address list. The
                            `value` field in this case is OCID of the address list.
                          - **HTTP_HEADER_CONTAINS:** The HTTP_HEADER_CONTAINS criteria is defined using a compound value separated by a colon: a header field
                            name and a header field value. `host:test.example.com` is an example of a criteria value where `host` is the header field name and
                            `test.example.com` is the header field value. A request matches when the header field name is a case insensitive match and the
                            header field value is a case insensitive, substring match.
                          *Example:* With a criteria value of `host:test.example.com`, where `host` is the name of the field and `test.example.com` is the value
                          of the host field, a request with the header values, `Host: www.test.example.com` will match, where as a request with header values of
                          `host: www.example.com` or `host: test.sub.example.com` will not match.
                          - **HTTP_METHOD_IS:** Matches if the request method is identical to one of the values listed in field. The `value` in this case is
                            string with one or multiple HTTP methods separated by new line symbol \\\\n The list of available methods: `GET`, `HEAD`, `POST`,
                            `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`"
                        - "*Example:* \\"GET\\\\nPOST\\""
                        - "- **HTTP_METHOD_IS_NOT:** Matches if the request is not identical to any of the contents of the `value` field. The `value` in this
                          case is string with one or multiple HTTP methods separated by new line symbol \\\\n The list of available methods: `GET`, `HEAD`,
                          `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`"
                        - "*Example:* \\"GET\\\\nPOST\\""
                        - "- **COUNTRY_IS:** Matches if the request originates from one of countries in the `value` field. The `value` in this case is string
                          with one or multiple countries separated by new line symbol \\\\n Country codes are in ISO 3166-1 alpha-2 format. For a list of codes,
                          see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                          *Example:* \\"AL\\\\nDZ\\\\nAM\\"
                          - **COUNTRY_IS_NOT:** Matches if the request does not originate from any of countries in the `value` field. The `value` in this case
                            is string with one or multiple countries separated by new line symbol \\\\n Country codes are in ISO 3166-1 alpha-2 format. For a
                            list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                          *Example:* \\"AL\\\\nDZ\\\\nAM\\"
                          - **USER_AGENT_IS:** Matches if the requesting user agent is identical to the contents of the `value` field.
                          *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`
                          - **USER_AGENT_IS_NOT:** Matches if the requesting user agent is not identical to the contents of the `value` field.
                          *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`"
                    returned: on success
                    type: str
                    sample: URL_IS
                value:
                    description:
                        - The criteria value.
                    returned: on success
                    type: str
                    sample: value_example
                is_case_sensitive:
                    description:
                        - When enabled, the condition will be matched with case-sensitive rules.
                    returned: on success
                    type: bool
                    sample: true
        is_nat_enabled:
            description:
                - When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking visitors with
                  shared IP addresses.
            returned: on success
            type: bool
            sample: true
    sample: {
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
        },
        "are_redirects_challenged": true,
        "criteria": [{
            "condition": "URL_IS",
            "value": "value_example",
            "is_case_sensitive": true
        }],
        "is_nat_enabled": true
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.waas import WaasClient
    from oci.waas.models import JsChallenge

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class JsChallengeHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_possible_entity_types(self):
        return super(JsChallengeHelperGen, self).get_possible_entity_types() + [
            "jschallenge",
            "jschallenges",
            "waasjschallenge",
            "waasjschallenges",
            "jschallengeresource",
            "jschallengesresource",
            "waas",
        ]

    def get_module_resource_id_param(self):
        return "waas_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("waas_policy_id")

    def get_get_fn(self):
        return self.client.get_js_challenge

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_js_challenge,
            waas_policy_id=self.module.params.get("waas_policy_id"),
        )

    def get_update_model_class(self):
        return JsChallenge

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_js_challenge,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                update_js_challenge_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


JsChallengeHelperCustom = get_custom_class("JsChallengeHelperCustom")


class ResourceHelper(JsChallengeHelperCustom, JsChallengeHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            waas_policy_id=dict(aliases=["id"], type="str", required=True),
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
            are_redirects_challenged=dict(type="bool"),
            criteria=dict(
                type="list",
                elements="dict",
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
                            "URL_DOES_NOT_MATCH_REGEX",
                            "URL_DOES_NOT_START_WITH",
                            "URL_PART_DOES_NOT_CONTAIN",
                            "URL_PART_DOES_NOT_END_WITH",
                            "IP_IS",
                            "IP_IS_NOT",
                            "IP_IN_LIST",
                            "IP_NOT_IN_LIST",
                            "HTTP_HEADER_CONTAINS",
                            "HTTP_METHOD_IS",
                            "HTTP_METHOD_IS_NOT",
                            "COUNTRY_IS",
                            "COUNTRY_IS_NOT",
                            "USER_AGENT_IS",
                            "USER_AGENT_IS_NOT",
                        ],
                    ),
                    value=dict(type="str", required=True),
                    is_case_sensitive=dict(type="bool"),
                ),
            ),
            is_nat_enabled=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="js_challenge",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
