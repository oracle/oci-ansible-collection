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
module: oci_waas_access_rules
short_description: Manage an AccessRules resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an AccessRules resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        aliases: ["id"]
        required: true
    access_rules:
        description:
            - ""
        type: list
        elements: dict
        required: true
        suboptions:
            name:
                description:
                    - The unique name of the access rule.
                    - This parameter is updatable.
                type: str
                required: true
            criteria:
                description:
                    - The list of access rule criteria. The rule would be applied only for the requests that matched all the listed conditions.
                type: list
                elements: dict
                required: true
                suboptions:
                    condition:
                        description:
                            - "The criteria the access rule and JavaScript Challenge uses to determine if action should be taken on a request.
                              - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value` field. URL
                                must start with a `/`.
                              - **URL_IS_NOT:** Matches if the concatenation of request URL path and query is not identical to the contents of the `value`
                                field. URL must start with a `/`.
                              - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value` field.
                                URL must start with a `/`.
                              - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value` field.
                              - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value` field.
                              - **URL_REGEX:** Matches if the concatenation of request URL path and query is described by the regular expression in the value
                                field. The value must be a valid regular expression recognized by the PCRE library in Nginx (https://www.pcre.org).
                              - **URL_DOES_NOT_MATCH_REGEX:** Matches if the concatenation of request URL path and query is not described by the regular
                                expression in the `value` field. The value must be a valid regular expression recognized by the PCRE library in Nginx
                                (https://www.pcre.org).
                              - **URL_DOES_NOT_START_WITH:** Matches if the concatenation of request URL path and query does not start with the contents of the
                                `value` field.
                              - **URL_PART_DOES_NOT_CONTAIN:** Matches if the concatenation of request URL path and query does not contain the contents of the
                                `value` field.
                              - **URL_PART_DOES_NOT_END_WITH:** Matches if the concatenation of request URL path and query does not end with the contents of the
                                `value` field.
                              - **IP_IS:** Matches if the request originates from one of the IP addresses contained in the defined address list. The `value` in
                                this case is string with one or multiple IPs or CIDR notations separated by new line symbol \\\\n
                              *Example:* \\"1.1.1.1\\\\n1.1.1.2\\\\n1.2.2.1/30\\"
                              - **IP_IS_NOT:** Matches if the request does not originate from any of the IP addresses contained in the defined address list. The
                                `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \\\\n
                              *Example:* \\"1.1.1.1\\\\n1.1.1.2\\\\n1.2.2.1/30\\"
                              - **IP_IN_LIST:** Matches if the request originates from one of the IP addresses contained in the referenced address list. The
                                `value` in this case is OCID of the address list.
                              - **IP_NOT_IN_LIST:** Matches if the request does not originate from any IP address contained in the referenced address list. The
                                `value` field in this case is OCID of the address list.
                              - **HTTP_HEADER_CONTAINS:** The HTTP_HEADER_CONTAINS criteria is defined using a compound value separated by a colon: a header
                                field name and a header field value. `host:test.example.com` is an example of a criteria value where `host` is the header field
                                name and `test.example.com` is the header field value. A request matches when the header field name is a case insensitive match
                                and the header field value is a case insensitive, substring match.
                              *Example:* With a criteria value of `host:test.example.com`, where `host` is the name of the field and `test.example.com` is the
                              value of the host field, a request with the header values, `Host: www.test.example.com` will match, where as a request with header
                              values of `host: www.example.com` or `host: test.sub.example.com` will not match.
                              - **HTTP_METHOD_IS:** Matches if the request method is identical to one of the values listed in field. The `value` in this case is
                                string with one or multiple HTTP methods separated by new line symbol \\\\n The list of available methods: `GET`, `HEAD`,
                                `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`"
                            - "*Example:* \\"GET\\\\nPOST\\""
                            - "- **HTTP_METHOD_IS_NOT:** Matches if the request is not identical to any of the contents of the `value` field. The `value` in
                              this case is string with one or multiple HTTP methods separated by new line symbol \\\\n The list of available methods: `GET`,
                              `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`"
                            - "*Example:* \\"GET\\\\nPOST\\""
                            - "- **COUNTRY_IS:** Matches if the request originates from one of countries in the `value` field. The `value` in this case is
                              string with one or multiple countries separated by new line symbol \\\\n Country codes are in ISO 3166-1 alpha-2 format. For a
                              list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                              *Example:* \\"AL\\\\nDZ\\\\nAM\\"
                              - **COUNTRY_IS_NOT:** Matches if the request does not originate from any of countries in the `value` field. The `value` in this
                                case is string with one or multiple countries separated by new line symbol \\\\n Country codes are in ISO 3166-1 alpha-2 format.
                                For a list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
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
            action:
                description:
                    - The action to take when the access criteria are met for a rule. If unspecified, defaults to `ALLOW`.
                    - "- **ALLOW:** Takes no action, just logs the request."
                    - "- **DETECT:** Takes no action, but creates an alert for the request."
                    - "- **BLOCK:** Blocks the request by returning specified response code or showing error page."
                    - "- **BYPASS:** Bypasses some or all challenges."
                    - "- **REDIRECT:** Redirects the request to the specified URL. These fields are required when `REDIRECT` is selected: `redirectUrl`,
                      `redirectResponseCode`."
                    - "- **SHOW_CAPTCHA:** Show a CAPTCHA Challenge page instead of the requested page."
                    - Regardless of action, no further rules are processed once a rule is matched.
                    - This parameter is updatable.
                type: str
                choices:
                    - "ALLOW"
                    - "DETECT"
                    - "BLOCK"
                    - "BYPASS"
                    - "REDIRECT"
                    - "SHOW_CAPTCHA"
                required: true
            block_action:
                description:
                    - The method used to block requests if `action` is set to `BLOCK` and the access criteria are met. If unspecified, defaults to
                      `SET_RESPONSE_CODE`.
                    - This parameter is updatable.
                type: str
                choices:
                    - "SET_RESPONSE_CODE"
                    - "SHOW_ERROR_PAGE"
            block_response_code:
                description:
                    - "The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the access criteria
                      are met. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`,
                      `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`,
                      `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`."
                    - This parameter is updatable.
                type: int
            block_error_page_message:
                description:
                    - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria
                      are met. If unspecified, defaults to 'Access to the website is blocked.'
                    - This parameter is updatable.
                type: str
            block_error_page_code:
                description:
                    - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access
                      criteria are met. If unspecified, defaults to 'Access rules'.
                    - This parameter is updatable.
                type: str
            block_error_page_description:
                description:
                    - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access
                      criteria are met. If unspecified, defaults to 'Access blocked by website owner. Please contact support.'
                    - This parameter is updatable.
                type: str
            bypass_challenges:
                description:
                    - The list of challenges to bypass when `action` is set to `BYPASS`. If unspecified or empty, all challenges are bypassed.
                    - "- **JS_CHALLENGE:** Bypasses JavaScript Challenge."
                    - "- **DEVICE_FINGERPRINT_CHALLENGE:** Bypasses Device Fingerprint Challenge."
                    - "- **HUMAN_INTERACTION_CHALLENGE:** Bypasses Human Interaction Challenge."
                    - "- **CAPTCHA:** Bypasses CAPTCHA Challenge."
                    - This parameter is updatable.
                type: list
                elements: str
                choices:
                    - "JS_CHALLENGE"
                    - "DEVICE_FINGERPRINT_CHALLENGE"
                    - "HUMAN_INTERACTION_CHALLENGE"
                    - "CAPTCHA"
            redirect_url:
                description:
                    - The target to which the request should be redirected, represented as a URI reference. Required when `action` is `REDIRECT`.
                    - This parameter is updatable.
                type: str
            redirect_response_code:
                description:
                    - The response status code to return when `action` is set to `REDIRECT`.
                    - "- **MOVED_PERMANENTLY:** Used for designating the permanent movement of a page (numerical code - 301)."
                    - "- **FOUND:** Used for designating the temporary movement of a page (numerical code - 302)."
                    - This parameter is updatable.
                type: str
                choices:
                    - "MOVED_PERMANENTLY"
                    - "FOUND"
            captcha_title:
                description:
                    - The title used when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.
                    - This parameter is updatable.
                type: str
            captcha_header:
                description:
                    - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.
                    - This parameter is updatable.
                type: str
            captcha_footer:
                description:
                    - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.
                    - This parameter is updatable.
                type: str
            captcha_submit_label:
                description:
                    - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `SHOW_CAPTCHA` and the request is challenged.
                    - This parameter is updatable.
                type: str
            response_header_manipulation:
                description:
                    - An object that represents an action to apply to an HTTP response headers if all rule criteria will be matched regardless of `action`
                      value.
                type: list
                elements: dict
                suboptions:
                    action:
                        description:
                            - ""
                            - This parameter is updatable.
                        type: str
                        choices:
                            - "EXTEND_HTTP_RESPONSE_HEADER"
                            - "ADD_HTTP_RESPONSE_HEADER"
                            - "REMOVE_HTTP_RESPONSE_HEADER"
                        required: true
                    header:
                        description:
                            - A header field name that conforms to RFC 7230.
                            - "Example: `example_header_name`"
                            - This parameter is updatable.
                        type: str
                        required: true
                    value:
                        description:
                            - A header field value that conforms to RFC 7230.
                            - "Example: `example_value`"
                            - This parameter is updatable.
                            - Required when action is one of ['ADD_HTTP_RESPONSE_HEADER', 'EXTEND_HTTP_RESPONSE_HEADER']
                        type: str
    state:
        description:
            - The state of the AccessRules.
            - Use I(state=present) to update an existing an AccessRules.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update access_rules
  oci_waas_access_rules:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"
    access_rules:
    - # required
      name: name_example
      criteria:
      - # required
        condition: URL_IS
        value: value_example

        # optional
        is_case_sensitive: true
      action: ALLOW

      # optional
      block_action: SET_RESPONSE_CODE
      block_response_code: 56
      block_error_page_message: block_error_page_message_example
      block_error_page_code: block_error_page_code_example
      block_error_page_description: block_error_page_description_example
      bypass_challenges: [ "JS_CHALLENGE" ]
      redirect_url: redirect_url_example
      redirect_response_code: MOVED_PERMANENTLY
      captcha_title: captcha_title_example
      captcha_header: captcha_header_example
      captcha_footer: captcha_footer_example
      captcha_submit_label: captcha_submit_label_example
      response_header_manipulation:
      - # required
        action: EXTEND_HTTP_RESPONSE_HEADER
        header: header_example
        value: value_example

"""

RETURN = """
access_rules:
    description:
        - Details of the AccessRules resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The unique name of the access rule.
            returned: on success
            type: str
            sample: name_example
        criteria:
            description:
                - The list of access rule criteria. The rule would be applied only for the requests that matched all the listed conditions.
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
        action:
            description:
                - The action to take when the access criteria are met for a rule. If unspecified, defaults to `ALLOW`.
                - "- **ALLOW:** Takes no action, just logs the request."
                - "- **DETECT:** Takes no action, but creates an alert for the request."
                - "- **BLOCK:** Blocks the request by returning specified response code or showing error page."
                - "- **BYPASS:** Bypasses some or all challenges."
                - "- **REDIRECT:** Redirects the request to the specified URL. These fields are required when `REDIRECT` is selected: `redirectUrl`,
                  `redirectResponseCode`."
                - "- **SHOW_CAPTCHA:** Show a CAPTCHA Challenge page instead of the requested page."
                - Regardless of action, no further rules are processed once a rule is matched.
            returned: on success
            type: str
            sample: ALLOW
        block_action:
            description:
                - The method used to block requests if `action` is set to `BLOCK` and the access criteria are met. If unspecified, defaults to
                  `SET_RESPONSE_CODE`.
            returned: on success
            type: str
            sample: SET_RESPONSE_CODE
        block_response_code:
            description:
                - "The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the access criteria are
                  met. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`,
                  `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`,
                  `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`."
            returned: on success
            type: int
            sample: 56
        block_error_page_message:
            description:
                - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are
                  met. If unspecified, defaults to 'Access to the website is blocked.'
            returned: on success
            type: str
            sample: block_error_page_message_example
        block_error_page_code:
            description:
                - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria
                  are met. If unspecified, defaults to 'Access rules'.
            returned: on success
            type: str
            sample: block_error_page_code_example
        block_error_page_description:
            description:
                - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access
                  criteria are met. If unspecified, defaults to 'Access blocked by website owner. Please contact support.'
            returned: on success
            type: str
            sample: block_error_page_description_example
        bypass_challenges:
            description:
                - The list of challenges to bypass when `action` is set to `BYPASS`. If unspecified or empty, all challenges are bypassed.
                - "- **JS_CHALLENGE:** Bypasses JavaScript Challenge."
                - "- **DEVICE_FINGERPRINT_CHALLENGE:** Bypasses Device Fingerprint Challenge."
                - "- **HUMAN_INTERACTION_CHALLENGE:** Bypasses Human Interaction Challenge."
                - "- **CAPTCHA:** Bypasses CAPTCHA Challenge."
            returned: on success
            type: list
            sample: []
        redirect_url:
            description:
                - The target to which the request should be redirected, represented as a URI reference. Required when `action` is `REDIRECT`.
            returned: on success
            type: str
            sample: redirect_url_example
        redirect_response_code:
            description:
                - The response status code to return when `action` is set to `REDIRECT`.
                - "- **MOVED_PERMANENTLY:** Used for designating the permanent movement of a page (numerical code - 301)."
                - "- **FOUND:** Used for designating the temporary movement of a page (numerical code - 302)."
            returned: on success
            type: str
            sample: MOVED_PERMANENTLY
        captcha_title:
            description:
                - The title used when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.
            returned: on success
            type: str
            sample: captcha_title_example
        captcha_header:
            description:
                - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.
            returned: on success
            type: str
            sample: captcha_header_example
        captcha_footer:
            description:
                - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.
            returned: on success
            type: str
            sample: captcha_footer_example
        captcha_submit_label:
            description:
                - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `SHOW_CAPTCHA` and the request is challenged.
            returned: on success
            type: str
            sample: captcha_submit_label_example
        response_header_manipulation:
            description:
                - An object that represents an action to apply to an HTTP response headers if all rule criteria will be matched regardless of `action` value.
            returned: on success
            type: complex
            contains:
                value:
                    description:
                        - A header field value that conforms to RFC 7230.
                        - "Example: `example_value`"
                    returned: on success
                    type: str
                    sample: value_example
                action:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: EXTEND_HTTP_RESPONSE_HEADER
                header:
                    description:
                        - A header field name that conforms to RFC 7230.
                        - "Example: `example_header_name`"
                    returned: on success
                    type: str
                    sample: header_example
    sample: {
        "name": "name_example",
        "criteria": [{
            "condition": "URL_IS",
            "value": "value_example",
            "is_case_sensitive": true
        }],
        "action": "ALLOW",
        "block_action": "SET_RESPONSE_CODE",
        "block_response_code": 56,
        "block_error_page_message": "block_error_page_message_example",
        "block_error_page_code": "block_error_page_code_example",
        "block_error_page_description": "block_error_page_description_example",
        "bypass_challenges": [],
        "redirect_url": "redirect_url_example",
        "redirect_response_code": "MOVED_PERMANENTLY",
        "captcha_title": "captcha_title_example",
        "captcha_header": "captcha_header_example",
        "captcha_footer": "captcha_footer_example",
        "captcha_submit_label": "captcha_submit_label_example",
        "response_header_manipulation": [{
            "value": "value_example",
            "action": "EXTEND_HTTP_RESPONSE_HEADER",
            "header": "header_example"
        }]
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
    from oci.waas import WaasClient
    from oci.waas.models import AccessRule

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AccessRulesHelperGen(OCIResourceHelperBase):
    """Supported operations: update and list"""

    def get_possible_entity_types(self):
        return super(AccessRulesHelperGen, self).get_possible_entity_types() + [
            "accessrules",
            "accessrule",
            "waasaccessrules",
            "waasaccessrule",
            "accessrulesresource",
            "accessruleresource",
            "waas",
        ]

    def get_module_resource_id_param(self):
        return "waas_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("waas_policy_id")

    def get_resource(self):
        resources = self.list_resources()
        for resource in resources:
            if self.get_module_resource_id() == resource.id:
                return oci_common_utils.get_default_response_from_resource(resource)

        oci_common_utils.raise_does_not_exist_service_error()

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "waas_policy_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_access_rules, **kwargs
        )

    def get_update_model_class(self):
        return AccessRule

    def get_update_model(self):
        if self.module.params.get("access_rules"):
            return [
                oci_common_utils.convert_input_data_to_model_class(
                    resource, self.get_update_model_class()
                )
                for resource in self.module.params["access_rules"]
            ]
        return []

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_access_rules,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                access_rules=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AccessRulesHelperCustom = get_custom_class("AccessRulesHelperCustom")


class ResourceHelper(AccessRulesHelperCustom, AccessRulesHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            waas_policy_id=dict(aliases=["id"], type="str", required=True),
            access_rules=dict(
                type="list",
                elements="dict",
                required=True,
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
                    action=dict(
                        type="str",
                        required=True,
                        choices=[
                            "ALLOW",
                            "DETECT",
                            "BLOCK",
                            "BYPASS",
                            "REDIRECT",
                            "SHOW_CAPTCHA",
                        ],
                    ),
                    block_action=dict(
                        type="str", choices=["SET_RESPONSE_CODE", "SHOW_ERROR_PAGE"]
                    ),
                    block_response_code=dict(type="int"),
                    block_error_page_message=dict(type="str"),
                    block_error_page_code=dict(type="str"),
                    block_error_page_description=dict(type="str"),
                    bypass_challenges=dict(
                        type="list",
                        elements="str",
                        choices=[
                            "JS_CHALLENGE",
                            "DEVICE_FINGERPRINT_CHALLENGE",
                            "HUMAN_INTERACTION_CHALLENGE",
                            "CAPTCHA",
                        ],
                        no_log=True,
                    ),
                    redirect_url=dict(type="str"),
                    redirect_response_code=dict(
                        type="str", choices=["MOVED_PERMANENTLY", "FOUND"]
                    ),
                    captcha_title=dict(type="str"),
                    captcha_header=dict(type="str"),
                    captcha_footer=dict(type="str"),
                    captcha_submit_label=dict(type="str"),
                    response_header_manipulation=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            action=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "EXTEND_HTTP_RESPONSE_HEADER",
                                    "ADD_HTTP_RESPONSE_HEADER",
                                    "REMOVE_HTTP_RESPONSE_HEADER",
                                ],
                            ),
                            header=dict(type="str", required=True),
                            value=dict(type="str"),
                        ),
                    ),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="access_rules",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
