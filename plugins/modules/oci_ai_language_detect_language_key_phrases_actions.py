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
module: oci_ai_language_detect_language_key_phrases_actions
short_description: Perform actions on a DetectLanguageKeyPhrases resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DetectLanguageKeyPhrases resource in Oracle Cloud Infrastructure
    - For I(action=detect_language_key_phrases), make a detect call to the keyPhrase pre-deployed model.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    text:
        description:
            - Document text for detect keyPhrases.
        type: str
        required: true
    action:
        description:
            - The action to perform on the DetectLanguageKeyPhrases.
        type: str
        required: true
        choices:
            - "detect_language_key_phrases"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action detect_language_key_phrases on detect_language_key_phrases
  oci_ai_language_detect_language_key_phrases_actions:
    # required
    text: text_example
    action: detect_language_key_phrases

"""

RETURN = """
detect_language_key_phrases_result:
    description:
        - Details of the DetectLanguageKeyPhrases resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        key_phrases:
            description:
                - List of detected keyPhrases.
            returned: on success
            type: complex
            contains:
                text:
                    description:
                        - Key phrase exreacted from given text.
                    returned: on success
                    type: str
                    sample: text_example
                score:
                    description:
                        - "Score or confidence of the key phrase.
                          Example: `0.9999856066867399`"
                    returned: on success
                    type: float
                    sample: 1.2
    sample: {
        "key_phrases": [{
            "text": "text_example",
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
    from oci.ai_language.models import DetectLanguageKeyPhrasesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DetectLanguageKeyPhrasesActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        detect_language_key_phrases
    """

    def detect_language_key_phrases(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetectLanguageKeyPhrasesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detect_language_key_phrases,
            call_fn_args=(),
            call_fn_kwargs=dict(detect_language_key_phrases_details=action_details,),
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


DetectLanguageKeyPhrasesActionsHelperCustom = get_custom_class(
    "DetectLanguageKeyPhrasesActionsHelperCustom"
)


class ResourceHelper(
    DetectLanguageKeyPhrasesActionsHelperCustom,
    DetectLanguageKeyPhrasesActionsHelperGen,
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
                type="str", required=True, choices=["detect_language_key_phrases"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="detect_language_key_phrases",
        service_client_class=AIServiceLanguageClient,
        namespace="ai_language",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
