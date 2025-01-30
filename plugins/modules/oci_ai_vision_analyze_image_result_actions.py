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
module: oci_ai_vision_analyze_image_result_actions
short_description: Perform actions on an AnalyzeImageResult resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AnalyzeImageResult resource in Oracle Cloud Infrastructure
    - For I(action=analyze_image), perform different types of image analysis.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    features:
        description:
            - The types of image analysis.
        type: list
        elements: dict
        required: true
        suboptions:
            language:
                description:
                    - The language of the document image, abbreviated according to ISO 639-2.
                    - Applicable when feature_type is 'TEXT_DETECTION'
                type: str
                choices:
                    - "ENG"
                    - "CES"
                    - "DAN"
                    - "NLD"
                    - "FIN"
                    - "FRA"
                    - "DEU"
                    - "ELL"
                    - "HUN"
                    - "ITA"
                    - "NOR"
                    - "POL"
                    - "POR"
                    - "RON"
                    - "RUS"
                    - "SLK"
                    - "SPA"
                    - "SWE"
                    - "TUR"
                    - "ARA"
                    - "CHI_SIM"
                    - "HIN"
                    - "JPN"
                    - "KOR"
                    - "OTHERS"
            feature_type:
                description:
                    - "The type of image analysis requested.
                      The allowed values are:
                      - `IMAGE_CLASSIFICATION`: Label the image.
                      - `OBJECT_DETECTION`: Identify objects in the image with bounding boxes.
                      - `TEXT_DETECTION`: Recognize text in the image."
                type: str
                choices:
                    - "TEXT_DETECTION"
                    - "OBJECT_DETECTION"
                    - "IMAGE_CLASSIFICATION"
                required: true
            max_results:
                description:
                    - The maximum number of results to return.
                    - Applicable when feature_type is one of ['IMAGE_CLASSIFICATION', 'OBJECT_DETECTION']
                type: int
            model_id:
                description:
                    - The custom model ID.
                    - Applicable when feature_type is one of ['IMAGE_CLASSIFICATION', 'OBJECT_DETECTION']
                type: str
    image:
        description:
            - ""
        type: dict
        required: true
        suboptions:
            namespace_name:
                description:
                    - The Object Storage namespace.
                    - Required when source is 'OBJECT_STORAGE'
                type: str
            bucket_name:
                description:
                    - The Object Storage bucket name.
                    - Required when source is 'OBJECT_STORAGE'
                type: str
            object_name:
                description:
                    - The Object Storage object name.
                    - Required when source is 'OBJECT_STORAGE'
                type: str
            source:
                description:
                    - "The location of the image data.
                      The allowed values are:
                      - `INLINE`: The data is included directly in the request payload.
                      - `OBJECT_STORAGE`: The image is in OCI Object Storage."
                type: str
                choices:
                    - "OBJECT_STORAGE"
                    - "INLINE"
                required: true
            data:
                description:
                    - Raw image data.
                    - Required when source is 'INLINE'
                type: str
    compartment_id:
        description:
            - The OCID of the compartment that calls the API.
        type: str
    action:
        description:
            - The action to perform on the AnalyzeImageResult.
        type: str
        required: true
        choices:
            - "analyze_image"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action analyze_image on analyze_image_result
  oci_ai_vision_analyze_image_result_actions:
    # required
    features:
    - # required
      feature_type: TEXT_DETECTION

      # optional
      language: ENG
    image:
      # required
      namespace_name: namespace_name_example
      bucket_name: bucket_name_example
      object_name: object_name_example
      source: OBJECT_STORAGE
    action: analyze_image

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
analyze_image_result:
    description:
        - Details of the AnalyzeImageResult resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        image_objects:
            description:
                - The detected objects.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The object category name. Every value returned by the pre-deployed model is in English.
                    returned: on success
                    type: str
                    sample: name_example
                confidence:
                    description:
                        - The confidence score, between 0 and 1.
                    returned: on success
                    type: float
                    sample: 3.4
                bounding_polygon:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        normalized_vertices:
                            description:
                                - "An array of normalized points defining the polygon's perimeter, with an implicit segment between subsequent points and
                                  between the first and last point.
                                  Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0}, {\\"x\\": 1,
                                  \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an image."
                            returned: on success
                            type: complex
                            contains:
                                x:
                                    description:
                                        - The X-axis normalized coordinate.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                y:
                                    description:
                                        - The Y-axis normalized coordinate.
                                    returned: on success
                                    type: float
                                    sample: 1.2
        labels:
            description:
                - The image classification labels.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The classification catagory label name.
                    returned: on success
                    type: str
                    sample: name_example
                confidence:
                    description:
                        - The confidence score between 0 and 1.
                    returned: on success
                    type: float
                    sample: 3.4
        ontology_classes:
            description:
                - The ontologyClasses of image labels.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The label name.
                    returned: on success
                    type: str
                    sample: name_example
                parent_names:
                    description:
                        - The label parents.
                    returned: on success
                    type: list
                    sample: []
                synonym_names:
                    description:
                        - The label synonyms.
                    returned: on success
                    type: list
                    sample: []
        image_text:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                words:
                    description:
                        - The words recognized in an image.
                    returned: on success
                    type: complex
                    contains:
                        text:
                            description:
                                - The string of text characters in the word.
                            returned: on success
                            type: str
                            sample: text_example
                        confidence:
                            description:
                                - the confidence score between 0 and 1.
                            returned: on success
                            type: float
                            sample: 3.4
                        bounding_polygon:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                normalized_vertices:
                                    description:
                                        - "An array of normalized points defining the polygon's perimeter, with an implicit segment between subsequent points
                                          and between the first and last point.
                                          Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0}, {\\"x\\":
                                          1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an image."
                                    returned: on success
                                    type: complex
                                    contains:
                                        x:
                                            description:
                                                - The X-axis normalized coordinate.
                                            returned: on success
                                            type: float
                                            sample: 1.2
                                        y:
                                            description:
                                                - The Y-axis normalized coordinate.
                                            returned: on success
                                            type: float
                                            sample: 1.2
                lines:
                    description:
                        - The lines of text recognized in an image.
                    returned: on success
                    type: complex
                    contains:
                        text:
                            description:
                                - The text recognized.
                            returned: on success
                            type: str
                            sample: text_example
                        confidence:
                            description:
                                - The confidence score between 0 and 1.
                            returned: on success
                            type: float
                            sample: 3.4
                        bounding_polygon:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                normalized_vertices:
                                    description:
                                        - "An array of normalized points defining the polygon's perimeter, with an implicit segment between subsequent points
                                          and between the first and last point.
                                          Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0}, {\\"x\\":
                                          1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an image."
                                    returned: on success
                                    type: complex
                                    contains:
                                        x:
                                            description:
                                                - The X-axis normalized coordinate.
                                            returned: on success
                                            type: float
                                            sample: 1.2
                                        y:
                                            description:
                                                - The Y-axis normalized coordinate.
                                            returned: on success
                                            type: float
                                            sample: 1.2
                        word_indexes:
                            description:
                                - The array of words.
                            returned: on success
                            type: list
                            sample: []
        image_classification_model_version:
            description:
                - The image classification model version.
            returned: on success
            type: str
            sample: image_classification_model_version_example
        object_detection_model_version:
            description:
                - The object detection model version.
            returned: on success
            type: str
            sample: object_detection_model_version_example
        text_detection_model_version:
            description:
                - The text detection model version.
            returned: on success
            type: str
            sample: text_detection_model_version_example
        errors:
            description:
                - The errors encountered during image analysis.
            returned: on success
            type: complex
            contains:
                code:
                    description:
                        - The error code.
                    returned: on success
                    type: str
                    sample: code_example
                message:
                    description:
                        - The error message.
                    returned: on success
                    type: str
                    sample: message_example
    sample: {
        "image_objects": [{
            "name": "name_example",
            "confidence": 3.4,
            "bounding_polygon": {
                "normalized_vertices": [{
                    "x": 1.2,
                    "y": 1.2
                }]
            }
        }],
        "labels": [{
            "name": "name_example",
            "confidence": 3.4
        }],
        "ontology_classes": [{
            "name": "name_example",
            "parent_names": [],
            "synonym_names": []
        }],
        "image_text": {
            "words": [{
                "text": "text_example",
                "confidence": 3.4,
                "bounding_polygon": {
                    "normalized_vertices": [{
                        "x": 1.2,
                        "y": 1.2
                    }]
                }
            }],
            "lines": [{
                "text": "text_example",
                "confidence": 3.4,
                "bounding_polygon": {
                    "normalized_vertices": [{
                        "x": 1.2,
                        "y": 1.2
                    }]
                },
                "word_indexes": []
            }]
        },
        "image_classification_model_version": "image_classification_model_version_example",
        "object_detection_model_version": "object_detection_model_version_example",
        "text_detection_model_version": "text_detection_model_version_example",
        "errors": [{
            "code": "code_example",
            "message": "message_example"
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
    from oci.ai_vision import AIServiceVisionClient
    from oci.ai_vision.models import AnalyzeImageDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiVisionAnalyzeImageResultActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        analyze_image
    """

    def analyze_image(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AnalyzeImageDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.analyze_image,
            call_fn_args=(),
            call_fn_kwargs=dict(analyze_image_details=action_details,),
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


AiVisionAnalyzeImageResultActionsHelperCustom = get_custom_class(
    "AiVisionAnalyzeImageResultActionsHelperCustom"
)


class ResourceHelper(
    AiVisionAnalyzeImageResultActionsHelperCustom,
    AiVisionAnalyzeImageResultActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            features=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    language=dict(
                        type="str",
                        choices=[
                            "ENG",
                            "CES",
                            "DAN",
                            "NLD",
                            "FIN",
                            "FRA",
                            "DEU",
                            "ELL",
                            "HUN",
                            "ITA",
                            "NOR",
                            "POL",
                            "POR",
                            "RON",
                            "RUS",
                            "SLK",
                            "SPA",
                            "SWE",
                            "TUR",
                            "ARA",
                            "CHI_SIM",
                            "HIN",
                            "JPN",
                            "KOR",
                            "OTHERS",
                        ],
                    ),
                    feature_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "TEXT_DETECTION",
                            "OBJECT_DETECTION",
                            "IMAGE_CLASSIFICATION",
                        ],
                    ),
                    max_results=dict(type="int"),
                    model_id=dict(type="str"),
                ),
            ),
            image=dict(
                type="dict",
                required=True,
                options=dict(
                    namespace_name=dict(type="str"),
                    bucket_name=dict(type="str"),
                    object_name=dict(type="str"),
                    source=dict(
                        type="str", required=True, choices=["OBJECT_STORAGE", "INLINE"]
                    ),
                    data=dict(type="str"),
                ),
            ),
            compartment_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["analyze_image"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="analyze_image_result",
        service_client_class=AIServiceVisionClient,
        namespace="ai_vision",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
