#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
    - "For I(action=batch_detect_language_text_classification), the API automatically classifies text into a set of pre-determined classes and sub-classes. A
      single class/subclass is returned for each record classified.
      It supports passing a batch of records.
      Learn more about text classification L(here,https://docs.cloud.oracle.com/iaas/language/using/pretrain-models.htm#text-class).
      Limitations:
      - A batch may have up to 100 records.
      - A record may be up to 5000 characters long.
      - The total of characters to process in a request can be up to 20,000 characters."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that calls the API, inference will be served
              from pre trained model
        type: str
    endpoint_id:
        description:
            - The endpoint which have to be used for inferencing. If endpointId and compartmentId is provided, then inference will be served from custom model
              which is mapped to this Endpoint.
        type: str
    documents:
        description:
            - List of Documents for detect text classification.
        type: list
        elements: dict
        required: true
        suboptions:
            key:
                description:
                    - Document unique identifier defined by the user.
                type: str
                required: true
            text:
                description:
                    - Document text for language service call.
                type: str
                required: true
            language_code:
                description:
                    - Language code of the document. Please refer to respective model L(API
                      documentation,https://docs.cloud.oracle.com/iaas/language/using/overview.htm) for supported languages.
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

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    endpoint_id: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"

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
                        - Document unique identifier defined by the user.
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
                        - "Language code supported
                          - auto : Automatically detect language
                          - ar : Arabic
                          - pt-BR : Brazilian Portuguese
                          - cs : Czech
                          - da : Danish
                          - nl : Dutch
                          - en : English
                          - fi : Finnish
                          - fr : French
                          - fr-CA : Canadian French
                          - de : German
                          - it : Italian
                          - ja : Japanese
                          - ko : Korean
                          - no : Norwegian
                          - pl : Polish
                          - ro : Romanian
                          - zh-CN : Simplified Chinese
                          - es : Spanish
                          - sv : Swedish
                          - zh-TW : Traditional Chinese
                          - tr : Turkish
                          - el : Greek
                          - he : Hebrew"
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
                        - Document unique identifier defined by the user.
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


class AiLanguageBatchDetectLanguageTextClassificationActionsHelperGen(
    OCIActionsHelperBase
):
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


AiLanguageBatchDetectLanguageTextClassificationActionsHelperCustom = get_custom_class(
    "AiLanguageBatchDetectLanguageTextClassificationActionsHelperCustom"
)


class ResourceHelper(
    AiLanguageBatchDetectLanguageTextClassificationActionsHelperCustom,
    AiLanguageBatchDetectLanguageTextClassificationActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            endpoint_id=dict(type="str"),
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
