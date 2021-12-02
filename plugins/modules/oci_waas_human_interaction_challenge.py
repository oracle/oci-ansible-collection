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
module: oci_waas_human_interaction_challenge
short_description: Manage a HumanInteractionChallenge resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a HumanInteractionChallenge resource in Oracle Cloud Infrastructure
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
            - Enables or disables the human interaction challenge Web Application Firewall feature.
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
            - The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.
            - This parameter is updatable.
        type: int
    failure_threshold_expiration_in_seconds:
        description:
            - The number of seconds before the failure threshold resets. If unspecified, defaults to  `60`.
            - This parameter is updatable.
        type: int
    interaction_threshold:
        description:
            - The number of interactions required to pass the challenge. If unspecified, defaults to `3`.
            - This parameter is updatable.
        type: int
    recording_period_in_seconds:
        description:
            - The number of seconds to record the interactions from the user. If unspecified, defaults to `15`.
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
    is_nat_enabled:
        description:
            - When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking visitors with
              shared IP addresses.
            - This parameter is updatable.
        type: bool
    state:
        description:
            - The state of the HumanInteractionChallenge.
            - Use I(state=present) to update an existing a HumanInteractionChallenge.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update human_interaction_challenge
  oci_waas_human_interaction_challenge:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"
    is_enabled: false

    # optional
    action: BLOCK
    failure_threshold: 100
    action_expiration_in_seconds: 600
    failure_threshold_expiration_in_seconds: 600
    interaction_threshold: 3
    recording_period_in_seconds: 15
    set_http_header:
      # required
      name: name_example
      value: value_example
    challenge_settings:
      # optional
      block_action: SHOW_ERROR_PAGE
      block_response_code: 403
      block_error_page_message: Access to the website is blocked.
      block_error_page_description: Access blocked by website owner. Please contact support.
      block_error_page_code: HIC
      captcha_title: Are you human?
      captcha_header: please let us know that you are not a robot by entering the text from the image below.
      captcha_footer: Enter the letters and numbers as they are shown in image above.
      captcha_submit_label: Yes, I am human.
    is_nat_enabled: true

"""

RETURN = """
human_interaction_challenge:
    description:
        - Details of the HumanInteractionChallenge resource acted upon by the current operation
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
        },
        "is_nat_enabled": true
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
    from oci.waas.models import HumanInteractionChallenge

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HumanInteractionChallengeHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_module_resource_id_param(self):
        return "waas_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("waas_policy_id")

    def get_get_fn(self):
        return self.client.get_human_interaction_challenge

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_human_interaction_challenge,
            waas_policy_id=self.module.params.get("waas_policy_id"),
        )

    def get_update_model_class(self):
        return HumanInteractionChallenge

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_human_interaction_challenge,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                update_human_interaction_challenge_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


HumanInteractionChallengeHelperCustom = get_custom_class(
    "HumanInteractionChallengeHelperCustom"
)


class ResourceHelper(
    HumanInteractionChallengeHelperCustom, HumanInteractionChallengeHelperGen
):
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
            is_nat_enabled=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="human_interaction_challenge",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
