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
module: oci_ai_language_model_actions
short_description: Perform actions on a Model resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Model resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a Model into a different compartment. When provided, If-Match is checked against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    model_id:
        description:
            - unique model OCID.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Model.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on model
  oci_ai_language_model_actions:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
model:
    description:
        - Details of the Model resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier model OCID of a model that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)  for the model's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        project_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the model.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - A short description of the Model.
            returned: on success
            type: str
            sample: description_example
        model_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                version:
                    description:
                        - Optional if nothing specified latest base model will be used for training. Supported versions can be found at /modelTypes/{modelType}
                    returned: on success
                    type: str
                    sample: version_example
                language_code:
                    description:
                        - supported language default value is en
                    returned: on success
                    type: str
                    sample: language_code_example
                model_type:
                    description:
                        - Model type
                    returned: on success
                    type: str
                    sample: NAMED_ENTITY_RECOGNITION
                classification_mode:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        classification_mode:
                            description:
                                - classification Modes
                            returned: on success
                            type: str
                            sample: MULTI_CLASS
                        version:
                            description:
                                - Optional if nothing specified latest base model will be used for training. Supported versions can be found at
                                  /modelTypes/{modelType}
                            returned: on success
                            type: str
                            sample: version_example
        time_created:
            description:
                - The time the the model was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the model was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The state of the model.
            returned: on success
            type: str
            sample: DELETING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        training_dataset:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                dataset_id:
                    description:
                        - Data Science Labelling Service OCID
                    returned: on success
                    type: str
                    sample: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
                dataset_type:
                    description:
                        - Possible data sets
                    returned: on success
                    type: str
                    sample: OBJECT_STORAGE
                location_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        location_type:
                            description:
                                - Possible object storage location types
                            returned: on success
                            type: str
                            sample: OBJECT_LIST
                        namespace_name:
                            description:
                                - Object storage namespace
                            returned: on success
                            type: str
                            sample: namespace_name_example
                        bucket_name:
                            description:
                                - Object storage bucket name
                            returned: on success
                            type: str
                            sample: bucket_name_example
                        object_names:
                            description:
                                - Array of files which need to be processed in the bucket
                            returned: on success
                            type: list
                            sample: []
        evaluation_results:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                entity_metrics:
                    description:
                        - List of entity metrics
                    returned: on success
                    type: complex
                    contains:
                        label:
                            description:
                                - Entity label
                            returned: on success
                            type: str
                            sample: label_example
                        f1:
                            description:
                                - F1-score, is a measure of a model's accuracy on a dataset
                            returned: on success
                            type: float
                            sample: 3.4
                        precision:
                            description:
                                - Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true
                                  positives plus the number of false positives)
                            returned: on success
                            type: float
                            sample: 3.4
                        recall:
                            description:
                                - Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what
                                  was actually tagged. The recall metric reveals how many of the predicted classes are correct.
                            returned: on success
                            type: float
                            sample: 3.4
                model_type:
                    description:
                        - Model type
                    returned: on success
                    type: str
                    sample: NAMED_ENTITY_RECOGNITION
                metrics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        micro_f1:
                            description:
                                - F1-score, is a measure of a model's accuracy on a dataset
                            returned: on success
                            type: float
                            sample: 3.4
                        micro_precision:
                            description:
                                - Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true
                                  positives plus the number of false positives)
                            returned: on success
                            type: float
                            sample: 3.4
                        micro_recall:
                            description:
                                - Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what
                                  was actually tagged. The recall metric reveals how many of the predicted classes are correct.
                            returned: on success
                            type: float
                            sample: 3.4
                        macro_f1:
                            description:
                                - F1-score, is a measure of a model's accuracy on a dataset
                            returned: on success
                            type: float
                            sample: 3.4
                        macro_precision:
                            description:
                                - Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true
                                  positives plus the number of false positives)
                            returned: on success
                            type: float
                            sample: 3.4
                        macro_recall:
                            description:
                                - Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what
                                  was actually tagged. The recall metric reveals how many of the predicted classes are correct.
                            returned: on success
                            type: float
                            sample: 3.4
                        weighted_f1:
                            description:
                                - F1-score, is a measure of a model's accuracy on a dataset
                            returned: on success
                            type: float
                            sample: 3.4
                        weighted_precision:
                            description:
                                - Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true
                                  positives plus the number of false positives)
                            returned: on success
                            type: float
                            sample: 3.4
                        weighted_recall:
                            description:
                                - Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what
                                  was actually tagged. The recall metric reveals how many of the predicted classes are correct.
                            returned: on success
                            type: float
                            sample: 3.4
                        accuracy:
                            description:
                                - The fraction of the labels that were correctly recognised .
                            returned: on success
                            type: float
                            sample: 3.4
                class_metrics:
                    description:
                        - List of text classification metrics
                    returned: on success
                    type: complex
                    contains:
                        label:
                            description:
                                - Text classification label
                            returned: on success
                            type: str
                            sample: label_example
                        f1:
                            description:
                                - F1-score, is a measure of a model's accuracy on a dataset
                            returned: on success
                            type: float
                            sample: 3.4
                        precision:
                            description:
                                - Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true
                                  positives plus the number of false positives)
                            returned: on success
                            type: float
                            sample: 3.4
                        recall:
                            description:
                                - Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what
                                  was actually tagged. The recall metric reveals how many of the predicted classes are correct.
                            returned: on success
                            type: float
                            sample: 3.4
                        support:
                            description:
                                - number of samples in the test set
                            returned: on success
                            type: float
                            sample: 3.4
                confusion_matrix:
                    description:
                        - class level confusion matrix
                    returned: on success
                    type: complex
                    contains:
                        matrix:
                            description:
                                - confusion matrix data
                            returned: on success
                            type: dict
                            sample: {}
                labels:
                    description:
                        - labels
                    returned: on success
                    type: list
                    sample: []
        test_strategy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                strategy_type:
                    description:
                        - This information will define the test strategy
                          different datasets for test and validation(optional) dataset.
                    returned: on success
                    type: str
                    sample: TEST_AND_VALIDATION_DATASET
                testing_dataset:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        dataset_id:
                            description:
                                - Data Science Labelling Service OCID
                            returned: on success
                            type: str
                            sample: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
                        dataset_type:
                            description:
                                - Possible data sets
                            returned: on success
                            type: str
                            sample: OBJECT_STORAGE
                        location_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                location_type:
                                    description:
                                        - Possible object storage location types
                                    returned: on success
                                    type: str
                                    sample: OBJECT_LIST
                                namespace_name:
                                    description:
                                        - Object storage namespace
                                    returned: on success
                                    type: str
                                    sample: namespace_name_example
                                bucket_name:
                                    description:
                                        - Object storage bucket name
                                    returned: on success
                                    type: str
                                    sample: bucket_name_example
                                object_names:
                                    description:
                                        - Array of files which need to be processed in the bucket
                                    returned: on success
                                    type: list
                                    sample: []
                validation_dataset:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        dataset_id:
                            description:
                                - Data Science Labelling Service OCID
                            returned: on success
                            type: str
                            sample: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
                        dataset_type:
                            description:
                                - Possible data sets
                            returned: on success
                            type: str
                            sample: OBJECT_STORAGE
                        location_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                location_type:
                                    description:
                                        - Possible object storage location types
                                    returned: on success
                                    type: str
                                    sample: OBJECT_LIST
                                namespace_name:
                                    description:
                                        - Object storage namespace
                                    returned: on success
                                    type: str
                                    sample: namespace_name_example
                                bucket_name:
                                    description:
                                        - Object storage bucket name
                                    returned: on success
                                    type: str
                                    sample: bucket_name_example
                                object_names:
                                    description:
                                        - Array of files which need to be processed in the bucket
                                    returned: on success
                                    type: list
                                    sample: []
        version:
            description:
                - "For pre trained models this will identify model type version used for model creation
                  For custom identifying the model by model id is difficult. This param provides ease of use for end customer.
                  <<service>>::<<service-name>>_<<model-type-version>>::<<custom model on which this training has to be done>>
                  ex: ai-lang::NER_V1::CUSTOM-V0"
            returned: on success
            type: str
            sample: version_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{ \\"orcl-cloud\\": { \\"free-tier-retained\\": \\"true\\" } }`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "model_details": {
            "version": "version_example",
            "language_code": "language_code_example",
            "model_type": "NAMED_ENTITY_RECOGNITION",
            "classification_mode": {
                "classification_mode": "MULTI_CLASS",
                "version": "version_example"
            }
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "DELETING",
        "lifecycle_details": "lifecycle_details_example",
        "training_dataset": {
            "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
            "dataset_type": "OBJECT_STORAGE",
            "location_details": {
                "location_type": "OBJECT_LIST",
                "namespace_name": "namespace_name_example",
                "bucket_name": "bucket_name_example",
                "object_names": []
            }
        },
        "evaluation_results": {
            "entity_metrics": [{
                "label": "label_example",
                "f1": 3.4,
                "precision": 3.4,
                "recall": 3.4
            }],
            "model_type": "NAMED_ENTITY_RECOGNITION",
            "metrics": {
                "micro_f1": 3.4,
                "micro_precision": 3.4,
                "micro_recall": 3.4,
                "macro_f1": 3.4,
                "macro_precision": 3.4,
                "macro_recall": 3.4,
                "weighted_f1": 3.4,
                "weighted_precision": 3.4,
                "weighted_recall": 3.4,
                "accuracy": 3.4
            },
            "class_metrics": [{
                "label": "label_example",
                "f1": 3.4,
                "precision": 3.4,
                "recall": 3.4,
                "support": 3.4
            }],
            "confusion_matrix": {
                "matrix": {}
            },
            "labels": []
        },
        "test_strategy": {
            "strategy_type": "TEST_AND_VALIDATION_DATASET",
            "testing_dataset": {
                "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
                "dataset_type": "OBJECT_STORAGE",
                "location_details": {
                    "location_type": "OBJECT_LIST",
                    "namespace_name": "namespace_name_example",
                    "bucket_name": "bucket_name_example",
                    "object_names": []
                }
            },
            "validation_dataset": {
                "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
                "dataset_type": "OBJECT_STORAGE",
                "location_details": {
                    "location_type": "OBJECT_LIST",
                    "namespace_name": "namespace_name_example",
                    "bucket_name": "bucket_name_example",
                    "object_names": []
                }
            }
        },
        "version": "version_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.ai_language.models import ChangeModelCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiLanguageModelActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "model_id"

    def get_module_resource_id(self):
        return self.module.params.get("model_id")

    def get_get_fn(self):
        return self.client.get_model

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model, model_id=self.module.params.get("model_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeModelCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_model_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_id=self.module.params.get("model_id"),
                change_model_compartment_details=action_details,
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


AiLanguageModelActionsHelperCustom = get_custom_class(
    "AiLanguageModelActionsHelperCustom"
)


class ResourceHelper(
    AiLanguageModelActionsHelperCustom, AiLanguageModelActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            model_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="model",
        service_client_class=AIServiceLanguageClient,
        namespace="ai_language",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
