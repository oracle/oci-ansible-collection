#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_ai_language_batch_detect_language_sentiments_actions
short_description: Perform actions on a BatchDetectLanguageSentiments resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a BatchDetectLanguageSentiments resource in Oracle Cloud Infrastructure
    - "For I(action=batch_detect_language_sentiments), the API extracts aspect-based and sentence level sentiment in text records.
      For aspect-based sentiment analysis, a set of aspects and their respective sentiment is returned for each record. Similarly, for sentence-level sentiment
      analysis, the sentiment is returned at the sentence level.
      For sentiment analysis, confidence scores are provided for each of the classes (positive, negative, neutral and mixed).
      Learn more about sentiment analysis L(here,https://docs.cloud.oracle.com/iaas/language/using/pretrain-models.htm#sentiment).
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
    documents:
        description:
            - List of Documents for detect sentiments.
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
    level:
        description:
            - "Set this parameter for sentence and aspect level sentiment analysis.
              Allowed values are:
                 - ASPECT
                 - SENTENCE"
        type: list
        elements: str
        choices:
            - "ASPECT"
            - "SENTENCE"
    action:
        description:
            - The action to perform on the BatchDetectLanguageSentiments.
        type: str
        required: true
        choices:
            - "batch_detect_language_sentiments"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action batch_detect_language_sentiments on batch_detect_language_sentiments
  oci_ai_language_batch_detect_language_sentiments_actions:
    # required
    documents:
    - # required
      key: key_example
      text: text_example

      # optional
      language_code: language_code_example
    action: batch_detect_language_sentiments

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    level: [ "ASPECT" ]

"""

RETURN = """
batch_detect_language_sentiments_result:
    description:
        - Details of the BatchDetectLanguageSentiments resource acted upon by the current operation
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
                document_sentiment:
                    description:
                        - Document level sentiment.
                    returned: on success
                    type: str
                    sample: document_sentiment_example
                document_scores:
                    description:
                        - "Scores for each sentiment.
                          Example: {\\"positive\\": 1.0, \\"negative\\": 0.0}"
                    returned: on success
                    type: dict
                    sample: {}
                aspects:
                    description:
                        - List of detected aspects sentiment.
                    returned: on success
                    type: complex
                    contains:
                        offset:
                            description:
                                - The number of Unicode code points preceding this entity in the submitted text.
                            returned: on success
                            type: int
                            sample: 56
                        length:
                            description:
                                - Length of aspect text.
                            returned: on success
                            type: int
                            sample: 56
                        text:
                            description:
                                - Aspect text.
                            returned: on success
                            type: str
                            sample: text_example
                        sentiment:
                            description:
                                - The highest-score sentiment for the aspect text.
                            returned: on success
                            type: str
                            sample: sentiment_example
                        scores:
                            description:
                                - "Scores or confidences for each sentiment.
                                  Example: `{\\"positive\\": 1.0, \\"negative\\": 0.0}`"
                            returned: on success
                            type: dict
                            sample: {}
                sentences:
                    description:
                        - List of detected sentences sentiment.
                    returned: on success
                    type: complex
                    contains:
                        offset:
                            description:
                                - The number of Unicode code points preceding this entity in the submitted text.
                            returned: on success
                            type: int
                            sample: 56
                        length:
                            description:
                                - Length of sentence text.
                            returned: on success
                            type: int
                            sample: 56
                        text:
                            description:
                                - Sentence text.
                            returned: on success
                            type: str
                            sample: text_example
                        sentiment:
                            description:
                                - The highest-score sentiment for the sentence text.
                            returned: on success
                            type: str
                            sample: sentiment_example
                        scores:
                            description:
                                - "Scores or confidences for each sentiment.
                                  Example: `{\\"positive\\": 1.0, \\"negative\\": 0.0}`"
                            returned: on success
                            type: dict
                            sample: {}
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
            "document_sentiment": "document_sentiment_example",
            "document_scores": {},
            "aspects": [{
                "offset": 56,
                "length": 56,
                "text": "text_example",
                "sentiment": "sentiment_example",
                "scores": {}
            }],
            "sentences": [{
                "offset": 56,
                "length": 56,
                "text": "text_example",
                "sentiment": "sentiment_example",
                "scores": {}
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
    from oci.ai_language.models import BatchDetectLanguageSentimentsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiLanguageBatchDetectLanguageSentimentsActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        batch_detect_language_sentiments
    """

    def batch_detect_language_sentiments(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, BatchDetectLanguageSentimentsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.batch_detect_language_sentiments,
            call_fn_args=(),
            call_fn_kwargs=dict(
                batch_detect_language_sentiments_details=action_details,
                level=self.module.params.get("level"),
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


AiLanguageBatchDetectLanguageSentimentsActionsHelperCustom = get_custom_class(
    "AiLanguageBatchDetectLanguageSentimentsActionsHelperCustom"
)


class ResourceHelper(
    AiLanguageBatchDetectLanguageSentimentsActionsHelperCustom,
    AiLanguageBatchDetectLanguageSentimentsActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
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
            level=dict(type="list", elements="str", choices=["ASPECT", "SENTENCE"]),
            action=dict(
                type="str", required=True, choices=["batch_detect_language_sentiments"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="batch_detect_language_sentiments",
        service_client_class=AIServiceLanguageClient,
        namespace="ai_language",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
