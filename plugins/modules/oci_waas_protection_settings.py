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
module: oci_waas_protection_settings
short_description: Manage a ProtectionSettings resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a ProtectionSettings resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        aliases: ["id"]
        required: true
    block_action:
        description:
            - If `action` is set to `BLOCK`, this specifies how the traffic is blocked when detected as malicious by a protection rule. If unspecified, defaults
              to `SET_RESPONSE_CODE`.
            - This parameter is updatable.
        type: str
        choices:
            - "SHOW_ERROR_PAGE"
            - "SET_RESPONSE_CODE"
    block_response_code:
        description:
            - "The response code returned when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the traffic is detected as malicious
              by a protection rule. If unspecified, defaults to `403`. The list of available response codes: `400`, `401`, `403`, `405`, `409`, `411`, `412`,
              `413`, `414`, `415`, `416`, `500`, `501`, `502`, `503`, `504`, `507`."
            - This parameter is updatable.
        type: int
    block_error_page_message:
        description:
            - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as
              malicious by a protection rule. If unspecified, defaults to 'Access to the website is blocked.'
            - This parameter is updatable.
        type: str
    block_error_page_code:
        description:
            - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected
              as malicious by a protection rule. If unspecified, defaults to `403`.
            - This parameter is updatable.
        type: str
    block_error_page_description:
        description:
            - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is
              detected as malicious by a protection rule. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
            - This parameter is updatable.
        type: str
    max_argument_count:
        description:
            - "The maximum number of arguments allowed to be passed to your application before an action is taken. Arguements are query parameters or body
              parameters in a PUT or POST request. If unspecified, defaults to `255`. This setting only applies if a corresponding protection rule is enabled,
              such as the \\"Number of Arguments Limits\\" rule (key: 960335)."
            - "Example: If `maxArgumentCount` to `2` for the Max Number of Arguments protection rule (key: 960335), the following requests would be blocked:
              `GET /myapp/path?query=one&query=two&query=three`
              `POST /myapp/path` with Body `{\\"argument1\\":\\"one\\",\\"argument2\\":\\"two\\",\\"argument3\\":\\"three\\"}`"
            - This parameter is updatable.
        type: int
    max_name_length_per_argument:
        description:
            - "The maximum length allowed for each argument name, in characters. Arguements are query parameters or body parameters in a PUT or POST request. If
              unspecified, defaults to `400`. This setting only applies if a corresponding protection rule is enabled, such as the \\"Values Limits\\" rule
              (key: 960208)."
            - This parameter is updatable.
        type: int
    max_total_name_length_of_arguments:
        description:
            - "The maximum length allowed for the sum of the argument name and value, in characters. Arguements are query parameters or body parameters in a PUT
              or POST request. If unspecified, defaults to `64000`. This setting only applies if a corresponding protection rule is enabled, such as the
              \\"Total Arguments Limits\\" rule (key: 960341)."
            - This parameter is updatable.
        type: int
    recommendations_period_in_days:
        description:
            - The length of time to analyze traffic traffic, in days. After the analysis period, `WafRecommendations` will be populated. If unspecified,
              defaults to `10`.
            - Use `GET /waasPolicies/{waasPolicyId}/wafRecommendations` to view WAF recommendations.
            - This parameter is updatable.
        type: int
    is_response_inspected:
        description:
            - Inspects the response body of origin responses. Can be used to detect leakage of sensitive data. If unspecified, defaults to `false`.
            - "**Note:** Only origin responses with a Content-Type matching a value in `mediaTypes` will be inspected."
            - This parameter is updatable.
        type: bool
    max_response_size_in_ki_b:
        description:
            - The maximum response size to be fully inspected, in binary kilobytes (KiB). Anything over this limit will be partially inspected. If unspecified,
              defaults to `1024`.
            - This parameter is updatable.
        type: int
    allowed_http_methods:
        description:
            - "The list of allowed HTTP methods. If unspecified, default to `[OPTIONS, GET, HEAD, POST]`. This setting only applies if a corresponding
              protection rule is enabled, such as the \\"Restrict HTTP Request Methods\\" rule (key: 911100)."
            - This parameter is updatable.
        type: list
        elements: str
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
            - This parameter is updatable.
        type: list
        elements: str
    state:
        description:
            - The state of the ProtectionSettings.
            - Use I(state=present) to update an existing a ProtectionSettings.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update protection_settings
  oci_waas_protection_settings:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    block_action: SHOW_ERROR_PAGE
    block_response_code: 56
    block_error_page_message: block_error_page_message_example
    block_error_page_code: block_error_page_code_example
    block_error_page_description: block_error_page_description_example
    max_argument_count: 56
    max_name_length_per_argument: 56
    max_total_name_length_of_arguments: 56
    recommendations_period_in_days: 56
    is_response_inspected: true
    max_response_size_in_ki_b: 56
    allowed_http_methods: [ "OPTIONS" ]
    media_types: [ "media_types_example" ]

"""

RETURN = """
protection_settings:
    description:
        - Details of the ProtectionSettings resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        block_action:
            description:
                - If `action` is set to `BLOCK`, this specifies how the traffic is blocked when detected as malicious by a protection rule. If unspecified,
                  defaults to `SET_RESPONSE_CODE`.
            returned: on success
            type: str
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
            type: str
            sample: block_error_page_message_example
        block_error_page_code:
            description:
                - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is
                  detected as malicious by a protection rule. If unspecified, defaults to `403`.
            returned: on success
            type: str
            sample: block_error_page_code_example
        block_error_page_description:
            description:
                - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is
                  detected as malicious by a protection rule. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
            returned: on success
            type: str
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
    from oci.waas.models import ProtectionSettings

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProtectionSettingsHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_module_resource_id_param(self):
        return "waas_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("waas_policy_id")

    def get_get_fn(self):
        return self.client.get_protection_settings

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_protection_settings,
            waas_policy_id=self.module.params.get("waas_policy_id"),
        )

    def get_update_model_class(self):
        return ProtectionSettings

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_protection_settings,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                update_protection_settings_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ProtectionSettingsHelperCustom = get_custom_class("ProtectionSettingsHelperCustom")


class ResourceHelper(ProtectionSettingsHelperCustom, ProtectionSettingsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            waas_policy_id=dict(aliases=["id"], type="str", required=True),
            block_action=dict(
                type="str", choices=["SHOW_ERROR_PAGE", "SET_RESPONSE_CODE"]
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
                elements="str",
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
            media_types=dict(type="list", elements="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="protection_settings",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
