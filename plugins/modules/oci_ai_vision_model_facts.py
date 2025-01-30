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
module: oci_ai_vision_model_facts
short_description: Fetches details about one or multiple Model resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Model resources in Oracle Cloud Infrastructure
    - Returns a list of models in a compartment.
    - If I(model_id) is specified, the details of a single Model will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    model_id:
        description:
            - A unique model identifier.
            - Required to get a specific model.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    project_id:
        description:
            - The ID of the project for which to list the objects.
        type: str
    lifecycle_state:
        description:
            - The filter to match models with the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. The default order for timeCreated is descending. The default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific model
  oci_ai_vision_model_facts:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"

- name: List models
  oci_ai_vision_model_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
models:
    description:
        - List of Model resources
    returned: on success
    type: complex
    contains:
        is_quick_mode:
            description:
                - Set to true when experimenting with a new model type or dataset, so model training is quick, with a predefined low number of passes through
                  the training data.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        max_training_duration_in_hours:
            description:
                - The maximum model training duration in hours, expressed as a decimal fraction.
                - Returned for get operation
            returned: on success
            type: float
            sample: 1.2
        trained_duration_in_hours:
            description:
                - The total hours actually used for model training.
                - Returned for get operation
            returned: on success
            type: float
            sample: 1.2
        recall:
            description:
                - Recall of the trained model.
                - Returned for get operation
            returned: on success
            type: float
            sample: 3.4
        average_precision:
            description:
                - The mean average precision of the trained model.
                - Returned for get operation
            returned: on success
            type: float
            sample: 3.4
        confidence_threshold:
            description:
                - The intersection over the union threshold used for calculating precision and recall.
                - Returned for get operation
            returned: on success
            type: float
            sample: 3.4
        total_image_count:
            description:
                - The number of images in the dataset used to train, validate, and test the model.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        test_image_count:
            description:
                - The number of images set aside for evaluating model performance metrics after training.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        metrics:
            description:
                - The complete set of per-label metrics for successfully trained models.
                - Returned for get operation
            returned: on success
            type: str
            sample: metrics_example
        id:
            description:
                - A unique identifier that is immutable after creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A human-friendly name for the model, which can be changed.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - An optional description of the model.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The compartment identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        model_type:
            description:
                - What type of Vision model this is.
            returned: on success
            type: str
            sample: IMAGE_CLASSIFICATION
        model_version:
            description:
                - The version of the model.
            returned: on success
            type: str
            sample: model_version_example
        project_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project that contains the model.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - When the model was created, as an RFC3339 datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - When the model was updated, as an RFC3339 datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the model.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail, that can provide actionable information if training failed.
            returned: on success
            type: str
            sample: lifecycle_details_example
        precision:
            description:
                - The precision of the trained model.
            returned: on success
            type: float
            sample: 3.4
        training_dataset:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                dataset_id:
                    description:
                        - OCID of the Data Labeling dataset.
                    returned: on success
                    type: str
                    sample: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
                dataset_type:
                    description:
                        - The dataset type, based on where it is stored.
                    returned: on success
                    type: str
                    sample: DATA_SCIENCE_LABELING
                namespace_name:
                    description:
                        - The namespace name of the Object Storage bucket that contains the input data file.
                    returned: on success
                    type: str
                    sample: namespace_name_example
                bucket_name:
                    description:
                        - The name of the Object Storage bucket that contains the input data file.
                    returned: on success
                    type: str
                    sample: bucket_name_example
                object_name:
                    description:
                        - The object name of the input data file.
                    returned: on success
                    type: str
                    sample: object_name_example
        testing_dataset:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                dataset_id:
                    description:
                        - OCID of the Data Labeling dataset.
                    returned: on success
                    type: str
                    sample: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
                dataset_type:
                    description:
                        - The dataset type, based on where it is stored.
                    returned: on success
                    type: str
                    sample: DATA_SCIENCE_LABELING
                namespace_name:
                    description:
                        - The namespace name of the Object Storage bucket that contains the input data file.
                    returned: on success
                    type: str
                    sample: namespace_name_example
                bucket_name:
                    description:
                        - The name of the Object Storage bucket that contains the input data file.
                    returned: on success
                    type: str
                    sample: bucket_name_example
                object_name:
                    description:
                        - The object name of the input data file.
                    returned: on success
                    type: str
                    sample: object_name_example
        validation_dataset:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                dataset_id:
                    description:
                        - OCID of the Data Labeling dataset.
                    returned: on success
                    type: str
                    sample: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
                dataset_type:
                    description:
                        - The dataset type, based on where it is stored.
                    returned: on success
                    type: str
                    sample: DATA_SCIENCE_LABELING
                namespace_name:
                    description:
                        - The namespace name of the Object Storage bucket that contains the input data file.
                    returned: on success
                    type: str
                    sample: namespace_name_example
                bucket_name:
                    description:
                        - The name of the Object Storage bucket that contains the input data file.
                    returned: on success
                    type: str
                    sample: bucket_name_example
                object_name:
                    description:
                        - The object name of the input data file.
                    returned: on success
                    type: str
                    sample: object_name_example
        freeform_tags:
            description:
                - "A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
                  For example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  For example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "is_quick_mode": true,
        "max_training_duration_in_hours": 1.2,
        "trained_duration_in_hours": 1.2,
        "recall": 3.4,
        "average_precision": 3.4,
        "confidence_threshold": 3.4,
        "total_image_count": 56,
        "test_image_count": 56,
        "metrics": "metrics_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "model_type": "IMAGE_CLASSIFICATION",
        "model_version": "model_version_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "precision": 3.4,
        "training_dataset": {
            "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
            "dataset_type": "DATA_SCIENCE_LABELING",
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example",
            "object_name": "object_name_example"
        },
        "testing_dataset": {
            "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
            "dataset_type": "DATA_SCIENCE_LABELING",
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example",
            "object_name": "object_name_example"
        },
        "validation_dataset": {
            "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
            "dataset_type": "DATA_SCIENCE_LABELING",
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example",
            "object_name": "object_name_example"
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.ai_vision import AIServiceVisionClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiVisionModelFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "model_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model, model_id=self.module.params.get("model_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "project_id",
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_models, **optional_kwargs
        )


AiVisionModelFactsHelperCustom = get_custom_class("AiVisionModelFactsHelperCustom")


class ResourceFactsHelper(AiVisionModelFactsHelperCustom, AiVisionModelFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            model_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            project_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="model",
        service_client_class=AIServiceVisionClient,
        namespace="ai_vision",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(models=result)


if __name__ == "__main__":
    main()
