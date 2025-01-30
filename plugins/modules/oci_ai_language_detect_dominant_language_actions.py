#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_ai_language_detect_dominant_language_actions
short_description: Perform actions on a DetectDominantLanguage resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DetectDominantLanguage resource in Oracle Cloud Infrastructure
    - "For I(action=detect_dominant_language), this API will be retired on Monday, 10 Oct 2023 00:00:00 GMT
      The API returns the detected language and a related confidence score (between 0 and 1).
      L(List of supported languages.,https://docs.cloud.oracle.com/iaas/language/using/pretrain-models.htm#lang-detect)
      Limitations:
      - A record may be up to 1000 characters long."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    text:
        description:
            - Document text for detect language.
        type: str
        required: true
    action:
        description:
            - The action to perform on the DetectDominantLanguage.
        type: str
        required: true
        choices:
            - "detect_dominant_language"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action detect_dominant_language on detect_dominant_language
  oci_ai_language_detect_dominant_language_actions:
    # required
    text: text_example
    action: detect_dominant_language

"""

RETURN = """
detect_dominant_language_result:
    description:
        - Details of the DetectDominantLanguage resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        languages:
            description:
                - List of detected languages with results sorted in descending order of the scores. Most likely language is on top.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - "Full language name.
                          Example: `English, Hindi, and so on`"
                    returned: on success
                    type: str
                    sample: name_example
                code:
                    description:
                        - "Detected language code as per L(ISO 639-1,https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) standard.
                          Example: `en, fr, hi etc`."
                    returned: on success
                    type: str
                    sample: code_example
                score:
                    description:
                        - "Score or confidence of detected language code.
                          Example: `0.9999856066867399`"
                    returned: on success
                    type: float
                    sample: 1.2
    sample: {
        "languages": [{
            "name": "name_example",
            "code": "code_example",
            "score": 1.2
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.ai_language import AIServiceLanguageClient
    from oci.ai_language.models import DetectDominantLanguageDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiLanguageDetectDominantLanguageActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        detect_dominant_language
    """

    def detect_dominant_language(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetectDominantLanguageDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detect_dominant_language,
            call_fn_args=(),
            call_fn_kwargs=dict(detect_dominant_language_details=action_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


AiLanguageDetectDominantLanguageActionsHelperCustom = get_custom_class(
    "AiLanguageDetectDominantLanguageActionsHelperCustom"
)


class ResourceHelper(
    AiLanguageDetectDominantLanguageActionsHelperCustom,
    AiLanguageDetectDominantLanguageActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            text=dict(type="str", required=True),
            action=dict(
                type="str", required=True, choices=["detect_dominant_language"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="detect_dominant_language",
        service_client_class=AIServiceLanguageClient,
        namespace="ai_language",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
