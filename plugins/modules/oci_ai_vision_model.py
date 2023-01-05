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
module: oci_ai_vision_model
short_description: Manage a Model resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Model resource in Oracle Cloud Infrastructure
    - For I(state=present), create a new model.
    - "This resource has the following action operations in the M(oracle.oci.oci_ai_vision_model_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    model_version:
        description:
            - The model version
        type: str
    model_type:
        description:
            - Which type of Vision model this is.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The compartment identifier.
            - Required for create using I(state=present).
        type: str
    is_quick_mode:
        description:
            - Set to true when experimenting with a new model type or dataset, so the model training is quick, with a predefined low number of passes through
              the training data.
        type: bool
    max_training_duration_in_hours:
        description:
            - The maximum model training duration in hours, expressed as a decimal fraction.
        type: float
    training_dataset:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            dataset_id:
                description:
                    - OCID of the Data Labeling dataset.
                    - Applicable when dataset_type is 'DATA_SCIENCE_LABELING'
                type: str
            dataset_type:
                description:
                    - The dataset type, based on where it is stored.
                type: str
                choices:
                    - "DATA_SCIENCE_LABELING"
                    - "OBJECT_STORAGE"
                required: true
            namespace_name:
                description:
                    - The namespace name of the Object Storage bucket that contains the input data file.
                    - Applicable when dataset_type is 'OBJECT_STORAGE'
                type: str
            bucket_name:
                description:
                    - The name of the Object Storage bucket that contains the input data file.
                    - Applicable when dataset_type is 'OBJECT_STORAGE'
                type: str
            object_name:
                description:
                    - The object name of the input data file.
                    - Applicable when dataset_type is 'OBJECT_STORAGE'
                type: str
    testing_dataset:
        description:
            - ""
        type: dict
        suboptions:
            dataset_id:
                description:
                    - OCID of the Data Labeling dataset.
                    - Applicable when dataset_type is 'DATA_SCIENCE_LABELING'
                type: str
            dataset_type:
                description:
                    - The dataset type, based on where it is stored.
                type: str
                choices:
                    - "DATA_SCIENCE_LABELING"
                    - "OBJECT_STORAGE"
                required: true
            namespace_name:
                description:
                    - The namespace name of the Object Storage bucket that contains the input data file.
                    - Applicable when dataset_type is 'OBJECT_STORAGE'
                type: str
            bucket_name:
                description:
                    - The name of the Object Storage bucket that contains the input data file.
                    - Applicable when dataset_type is 'OBJECT_STORAGE'
                type: str
            object_name:
                description:
                    - The object name of the input data file.
                    - Applicable when dataset_type is 'OBJECT_STORAGE'
                type: str
    validation_dataset:
        description:
            - ""
        type: dict
        suboptions:
            dataset_id:
                description:
                    - OCID of the Data Labeling dataset.
                    - Applicable when dataset_type is 'DATA_SCIENCE_LABELING'
                type: str
            dataset_type:
                description:
                    - The dataset type, based on where it is stored.
                type: str
                choices:
                    - "DATA_SCIENCE_LABELING"
                    - "OBJECT_STORAGE"
                required: true
            namespace_name:
                description:
                    - The namespace name of the Object Storage bucket that contains the input data file.
                    - Applicable when dataset_type is 'OBJECT_STORAGE'
                type: str
            bucket_name:
                description:
                    - The name of the Object Storage bucket that contains the input data file.
                    - Applicable when dataset_type is 'OBJECT_STORAGE'
                type: str
            object_name:
                description:
                    - The object name of the input data file.
                    - Applicable when dataset_type is 'OBJECT_STORAGE'
                type: str
    project_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project that contains the model.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - A human-friendly name for the model, which can be changed.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - An optional description of the model.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
              For example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    model_id:
        description:
            - A unique model identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Model.
            - Use I(state=present) to create or update a Model.
            - Use I(state=absent) to delete a Model.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create model
  oci_ai_vision_model:
    # required
    model_type: model_type_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    training_dataset:
      # required
      dataset_type: DATA_SCIENCE_LABELING

      # optional
      dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    model_version: model_version_example
    is_quick_mode: true
    max_training_duration_in_hours: 3.4
    testing_dataset:
      # required
      dataset_type: DATA_SCIENCE_LABELING

      # optional
      dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
    validation_dataset:
      # required
      dataset_type: DATA_SCIENCE_LABELING

      # optional
      dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update model
  oci_ai_vision_model:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update model using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_ai_vision_model:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete model
  oci_ai_vision_model:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete model using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_ai_vision_model:
    # required
    display_name: display_name_example
    state: absent

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
        is_quick_mode:
            description:
                - Set to true when experimenting with a new model type or dataset, so model training is quick, with a predefined low number of passes through
                  the training data.
            returned: on success
            type: bool
            sample: true
        max_training_duration_in_hours:
            description:
                - The maximum model training duration in hours, expressed as a decimal fraction.
            returned: on success
            type: float
            sample: 1.2
        trained_duration_in_hours:
            description:
                - The total hours actually used for model training.
            returned: on success
            type: float
            sample: 1.2
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
        recall:
            description:
                - Recall of the trained model.
            returned: on success
            type: float
            sample: 3.4
        average_precision:
            description:
                - The mean average precision of the trained model.
            returned: on success
            type: float
            sample: 3.4
        confidence_threshold:
            description:
                - The intersection over the union threshold used for calculating precision and recall.
            returned: on success
            type: float
            sample: 3.4
        total_image_count:
            description:
                - The number of images in the dataset used to train, validate, and test the model.
            returned: on success
            type: int
            sample: 56
        test_image_count:
            description:
                - The number of images set aside for evaluating model performance metrics after training.
            returned: on success
            type: int
            sample: 56
        metrics:
            description:
                - The complete set of per-label metrics for successfully trained models.
            returned: on success
            type: str
            sample: metrics_example
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "model_type": "IMAGE_CLASSIFICATION",
        "is_quick_mode": true,
        "max_training_duration_in_hours": 1.2,
        "trained_duration_in_hours": 1.2,
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
        "model_version": "model_version_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "precision": 3.4,
        "recall": 3.4,
        "average_precision": 3.4,
        "confidence_threshold": 3.4,
        "total_image_count": 56,
        "test_image_count": 56,
        "metrics": "metrics_example",
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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.ai_vision import AIServiceVisionClient
    from oci.ai_vision.models import CreateModelDetails
    from oci.ai_vision.models import UpdateModelDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiVisionModelHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(AiVisionModelHelperGen, self).get_possible_entity_types() + [
            "model",
            "models",
            "aiVisionmodel",
            "aiVisionmodels",
            "modelresource",
            "modelsresource",
            "aivision",
        ]

    def get_module_resource_id_param(self):
        return "model_id"

    def get_module_resource_id(self):
        return self.module.params.get("model_id")

    def get_get_fn(self):
        return self.client.get_model

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_model, model_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model, model_id=self.module.params.get("model_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "project_id", "display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_models, **kwargs)

    def get_create_model_class(self):
        return CreateModelDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_model,
            call_fn_args=(),
            call_fn_kwargs=dict(create_model_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateModelDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_model,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_id=self.module.params.get("model_id"),
                update_model_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_model,
            call_fn_args=(),
            call_fn_kwargs=dict(model_id=self.module.params.get("model_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AiVisionModelHelperCustom = get_custom_class("AiVisionModelHelperCustom")


class ResourceHelper(AiVisionModelHelperCustom, AiVisionModelHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            model_version=dict(type="str"),
            model_type=dict(type="str"),
            compartment_id=dict(type="str"),
            is_quick_mode=dict(type="bool"),
            max_training_duration_in_hours=dict(type="float"),
            training_dataset=dict(
                type="dict",
                options=dict(
                    dataset_id=dict(type="str"),
                    dataset_type=dict(
                        type="str",
                        required=True,
                        choices=["DATA_SCIENCE_LABELING", "OBJECT_STORAGE"],
                    ),
                    namespace_name=dict(type="str"),
                    bucket_name=dict(type="str"),
                    object_name=dict(type="str"),
                ),
            ),
            testing_dataset=dict(
                type="dict",
                options=dict(
                    dataset_id=dict(type="str"),
                    dataset_type=dict(
                        type="str",
                        required=True,
                        choices=["DATA_SCIENCE_LABELING", "OBJECT_STORAGE"],
                    ),
                    namespace_name=dict(type="str"),
                    bucket_name=dict(type="str"),
                    object_name=dict(type="str"),
                ),
            ),
            validation_dataset=dict(
                type="dict",
                options=dict(
                    dataset_id=dict(type="str"),
                    dataset_type=dict(
                        type="str",
                        required=True,
                        choices=["DATA_SCIENCE_LABELING", "OBJECT_STORAGE"],
                    ),
                    namespace_name=dict(type="str"),
                    bucket_name=dict(type="str"),
                    object_name=dict(type="str"),
                ),
            ),
            project_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            model_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="model",
        service_client_class=AIServiceVisionClient,
        namespace="ai_vision",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
