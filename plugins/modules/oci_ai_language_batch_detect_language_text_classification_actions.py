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
module: oci_ai_language_batch_detect_language_text_classification_actions
short_description: Perform actions on a BatchDetectLanguageTextClassification resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a BatchDetectLanguageTextClassification resource in Oracle Cloud Infrastructure
    - For I(action=batch_detect_language_text_classification), make a detect call to text classification from the pre-deployed model.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    documents:
        description:
            - List of Documents for detect text classification.
        type: list
        elements: dict
        required: true
        suboptions:
            key:
                description:
                    - Document Unique Identifier.
                type: str
                required: true
            text:
                description:
                    - Document text for detect text classification.
                type: str
                required: true
            language_code:
                description:
                    - Language code as per L(ISO 639-1,https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) standard.
                type: str
    action:
        description:
            - The action to perform on the BatchDetectLanguageTextClassification.
        type: str
        required: true
        choices:
            - "batch_detect_language_text_classification"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action batch_detect_language_text_classification on batch_detect_language_text_classification
  oci_ai_language_batch_detect_language_text_classification_actions:
    # required
    documents:
    - # required
      key: key_example
      text: text_example

      # optional
      language_code: language_code_example
    action: batch_detect_language_text_classification

"""

RETURN = """
batch_detect_language_text_classification_result:
    description:
        - Details of the BatchDetectLanguageTextClassification resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        documents:
            description:
                - List of succeeded document response.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Document Unique Identifier.
                    returned: on success
                    type: str
                    sample: key_example
                text_classification:
                    description:
                        - List of detected text classes.
                    returned: on success
                    type: complex
                    contains:
                        label:
                            description:
                                - Label of the the given text.
                            returned: on success
                            type: str
                            sample: label_example
                        score:
                            description:
                                - "Score or confidence of extracted text label.
                                  Example: `0.9999856066867399`"
                            returned: on success
                            type: float
                            sample: 1.2
                language_code:
                    description:
                        - Language code as per L(ISO 639-1,https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) standard.
                    returned: on success
                    type: str
                    sample: language_code_example
        errors:
            description:
                - List of failed document response.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Unique Document Identifier.
                    returned: on success
                    type: str
                    sample: key_example
                error:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        code:
                            description:
                                - A short error code that defines the error, meant for programmatic parsing.
                            returned: on success
                            type: str
                            sample: code_example
                        message:
                            description:
                                - A human-readable error string.
                            returned: on success
                            type: str
                            sample: message_example
    sample: {
        "documents": [{
            "key": "key_example",
            "text_classification": [{
                "label": "label_example",
                "score": 1.2
            }],
            "language_code": "language_code_example"
        }],
        "errors": [{
            "key": "key_example",
            "error": {
                "code": "code_example",
                "message": "message_example"
            }
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
    from oci.ai_language.models import BatchDetectLanguageTextClassificationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BatchDetectLanguageTextClassificationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        batch_detect_language_text_classification
    """

    def batch_detect_language_text_classification(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, BatchDetectLanguageTextClassificationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.batch_detect_language_text_classification,
            call_fn_args=(),
            call_fn_kwargs=dict(
                batch_detect_language_text_classification_details=action_details,
            ),
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


BatchDetectLanguageTextClassificationActionsHelperCustom = get_custom_class(
    "BatchDetectLanguageTextClassificationActionsHelperCustom"
)


class ResourceHelper(
    BatchDetectLanguageTextClassificationActionsHelperCustom,
    BatchDetectLanguageTextClassificationActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            documents=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    key=dict(type="str", required=True, no_log=True),
                    text=dict(type="str", required=True),
                    language_code=dict(type="str"),
                ),
            ),
            action=dict(
                type="str",
                required=True,
                choices=["batch_detect_language_text_classification"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="batch_detect_language_text_classification",
        service_client_class=AIServiceLanguageClient,
        namespace="ai_language",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
