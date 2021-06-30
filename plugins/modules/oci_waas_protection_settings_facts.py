#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_waas_protection_settings_facts
short_description: Fetches details about a ProtectionSettings resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ProtectionSettings resource in Oracle Cloud Infrastructure
    - Gets the protection settings in the Web Application Firewall configuration for a WAAS policy.
version_added: "2.9"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific protection_settings
  oci_waas_protection_settings_facts:
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
protection_settings:
    description:
        - ProtectionSettings resource
    returned: on success
    type: complex
    contains:
        block_action:
            description:
                - If `action` is set to `BLOCK`, this specifies how the traffic is blocked when detected as malicious by a protection rule. If unspecified,
                  defaults to `SET_RESPONSE_CODE`.
            returned: on success
            type: string
            sample: SHOW_ERROR_PAGE
        block_response_code:
            description:
                - "The response code returned when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the traffic is detected as
                  malicious by a protection rule. If unspecified, defaults to `403`. The list of available response codes: `400`, `401`, `403`, `405`, `409`,
                  `411`, `412`, `413`, `414`, `415`, `416`, `500`, `501`, `502`, `503`, `504`, `507`."
            returned: on success
            type: int
            sample: 56
        block_error_page_message:
            description:
                - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected
                  as malicious by a protection rule. If unspecified, defaults to 'Access to the website is blocked.'
            returned: on success
            type: string
            sample: block_error_page_message_example
        block_error_page_code:
            description:
                - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is
                  detected as malicious by a protection rule. If unspecified, defaults to `403`.
            returned: on success
            type: string
            sample: block_error_page_code_example
        block_error_page_description:
            description:
                - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is
                  detected as malicious by a protection rule. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
            returned: on success
            type: string
            sample: block_error_page_description_example
        max_argument_count:
            description:
                - "The maximum number of arguments allowed to be passed to your application before an action is taken. Arguements are query parameters or body
                  parameters in a PUT or POST request. If unspecified, defaults to `255`. This setting only applies if a corresponding protection rule is
                  enabled, such as the \\"Number of Arguments Limits\\" rule (key: 960335)."
                - "Example: If `maxArgumentCount` to `2` for the Max Number of Arguments protection rule (key: 960335), the following requests would be blocked:
                  `GET /myapp/path?query=one&query=two&query=three`
                  `POST /myapp/path` with Body `{\\"argument1\\":\\"one\\",\\"argument2\\":\\"two\\",\\"argument3\\":\\"three\\"}`"
            returned: on success
            type: int
            sample: 56
        max_name_length_per_argument:
            description:
                - "The maximum length allowed for each argument name, in characters. Arguements are query parameters or body parameters in a PUT or POST
                  request. If unspecified, defaults to `400`. This setting only applies if a corresponding protection rule is enabled, such as the \\"Values
                  Limits\\" rule (key: 960208)."
            returned: on success
            type: int
            sample: 56
        max_total_name_length_of_arguments:
            description:
                - "The maximum length allowed for the sum of the argument name and value, in characters. Arguements are query parameters or body parameters in a
                  PUT or POST request. If unspecified, defaults to `64000`. This setting only applies if a corresponding protection rule is enabled, such as the
                  \\"Total Arguments Limits\\" rule (key: 960341)."
            returned: on success
            type: int
            sample: 56
        recommendations_period_in_days:
            description:
                - The length of time to analyze traffic traffic, in days. After the analysis period, `WafRecommendations` will be populated. If unspecified,
                  defaults to `10`.
                - Use `GET /waasPolicies/{waasPolicyId}/wafRecommendations` to view WAF recommendations.
            returned: on success
            type: int
            sample: 56
        is_response_inspected:
            description:
                - Inspects the response body of origin responses. Can be used to detect leakage of sensitive data. If unspecified, defaults to `false`.
                - "**Note:** Only origin responses with a Content-Type matching a value in `mediaTypes` will be inspected."
            returned: on success
            type: bool
            sample: true
        max_response_size_in_ki_b:
            description:
                - The maximum response size to be fully inspected, in binary kilobytes (KiB). Anything over this limit will be partially inspected. If
                  unspecified, defaults to `1024`.
            returned: on success
            type: int
            sample: 56
        allowed_http_methods:
            description:
                - "The list of allowed HTTP methods. If unspecified, default to `[OPTIONS, GET, HEAD, POST]`. This setting only applies if a corresponding
                  protection rule is enabled, such as the \\"Restrict HTTP Request Methods\\" rule (key: 911100)."
            returned: on success
            type: list
            sample: []
        media_types:
            description:
                - "The list of media types to allow for inspection, if `isResponseInspected` is enabled. Only responses with MIME types in this list will be
                  inspected. If unspecified, defaults to `[\\"text/html\\", \\"text/plain\\", \\"text/xml\\"]`."
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
    sample: {
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
    }
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


class ProtectionSettingsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "waas_policy_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_protection_settings,
            waas_policy_id=self.module.params.get("waas_policy_id"),
        )


ProtectionSettingsFactsHelperCustom = get_custom_class(
    "ProtectionSettingsFactsHelperCustom"
)


class ResourceFactsHelper(
    ProtectionSettingsFactsHelperCustom, ProtectionSettingsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(waas_policy_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="protection_settings",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(protection_settings=result)


if __name__ == "__main__":
    main()
