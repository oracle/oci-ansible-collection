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
module: oci_waas_access_rules_facts
short_description: Fetches details about one or multiple AccessRules resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AccessRules resources in Oracle Cloud Infrastructure
    - Gets the currently configured access rules for the Web Application Firewall configuration of a specified WAAS policy.
      The order of the access rules is important. The rules will be checked in the order they are specified and the first matching rule will be used.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List access_rules
  oci_waas_access_rules_facts:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
access_rules:
    description:
        - List of AccessRules resources
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
                value:
                    description:
                        - A header field value that conforms to RFC 7230.
                        - "Example: `example_value`"
                    returned: on success
                    type: str
                    sample: value_example
    sample: [{
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
            "action": "EXTEND_HTTP_RESPONSE_HEADER",
            "header": "header_example",
            "value": "value_example"
        }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.waas import WaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AccessRulesFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "waas_policy_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_access_rules,
            waas_policy_id=self.module.params.get("waas_policy_id"),
            **optional_kwargs
        )


AccessRulesFactsHelperCustom = get_custom_class("AccessRulesFactsHelperCustom")


class ResourceFactsHelper(AccessRulesFactsHelperCustom, AccessRulesFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(waas_policy_id=dict(type="str", required=True), name=dict(type="str"),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="access_rules",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(access_rules=result)


if __name__ == "__main__":
    main()
