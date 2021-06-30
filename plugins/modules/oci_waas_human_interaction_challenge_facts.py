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
module: oci_waas_human_interaction_challenge_facts
short_description: Fetches details about a HumanInteractionChallenge resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a HumanInteractionChallenge resource in Oracle Cloud Infrastructure
    - Gets the human interaction challenge settings in the Web Application Firewall configuration for a WAAS policy.
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
- name: Get a specific human_interaction_challenge
  oci_waas_human_interaction_challenge_facts:
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
human_interaction_challenge:
    description:
        - HumanInteractionChallenge resource
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
                - Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the `action` is set
                  to `DETECT`.
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
                    type: string
                    sample: block_error_page_message_example
                block_error_page_description:
                    description:
                        - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                          request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
                    returned: on success
                    type: string
                    sample: block_error_page_description_example
                block_error_page_code:
                    description:
                        - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and the request is
                          blocked. If unspecified, defaults to `403`.
                    returned: on success
                    type: string
                    sample: block_error_page_code_example
                captcha_title:
                    description:
                        - The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the
                          request is blocked. If unspecified, defaults to `Are you human?`
                    returned: on success
                    type: string
                    sample: captcha_title_example
                captcha_header:
                    description:
                        - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                          `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts to access
                          this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the text from captcha below.`
                    returned: on success
                    type: string
                    sample: captcha_header_example
                captcha_footer:
                    description:
                        - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                          `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in image
                          above`.
                    returned: on success
                    type: string
                    sample: captcha_footer_example
                captcha_submit_label:
                    description:
                        - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set to
                          `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
                    returned: on success
                    type: string
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


class HumanInteractionChallengeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "waas_policy_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_human_interaction_challenge,
            waas_policy_id=self.module.params.get("waas_policy_id"),
        )


HumanInteractionChallengeFactsHelperCustom = get_custom_class(
    "HumanInteractionChallengeFactsHelperCustom"
)


class ResourceFactsHelper(
    HumanInteractionChallengeFactsHelperCustom, HumanInteractionChallengeFactsHelperGen
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
        resource_type="human_interaction_challenge",
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

    module.exit_json(human_interaction_challenge=result)


if __name__ == "__main__":
    main()
