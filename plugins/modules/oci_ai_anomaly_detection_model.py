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
module: oci_ai_anomaly_detection_model
short_description: Manage a Model resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Model resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Model.
    - "This resource has the following action operations in the M(oracle.oci.oci_ai_anomaly_detection_model_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID for the ai model's compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    model_training_details:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            target_fap:
                description:
                    - A target model accuracy metric user provides as their requirement
                type: float
            training_fraction:
                description:
                    - Fraction of total data that is used for training the model. The remaining is used for validation of the model.
                type: float
            data_asset_ids:
                description:
                    - The list of OCIDs of the data assets to train the model. The dataAssets have to be in the same project where the ai model would reside.
                type: list
                elements: str
                required: true
    project_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the model.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A short description of the ai model.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    model_id:
        description:
            - The OCID of the Model.
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
  oci_ai_anomaly_detection_model:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    model_training_details:
      # required
      data_asset_ids: [ "data_asset_ids_example" ]

      # optional
      target_fap: 3.4
      training_fraction: 3.4
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update model
  oci_ai_anomaly_detection_model:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update model using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_ai_anomaly_detection_model:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete model
  oci_ai_anomaly_detection_model:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete model using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_ai_anomaly_detection_model:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
                - The OCID of the model that is immutable on creation.
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
                - The OCID for the model's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        model_training_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                target_fap:
                    description:
                        - A target model accuracy metric user provides as their requirement
                    returned: on success
                    type: float
                    sample: 3.4
                training_fraction:
                    description:
                        - Fraction of total data that is used for training the model. The remaining is used for validation of the model.
                    returned: on success
                    type: float
                    sample: 3.4
                data_asset_ids:
                    description:
                        - The list of OCIDs of the data assets to train the model. The dataAssets have to be in the same project where the ai model would
                          reside.
                    returned: on success
                    type: list
                    sample: []
        model_training_results:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                fap:
                    description:
                        - The final-achieved model accuracy metric on individual value level
                    returned: on success
                    type: float
                    sample: 3.4
                multivariate_fap:
                    description:
                        - The model accuracy metric on timestamp level.
                    returned: on success
                    type: float
                    sample: 3.4
                is_training_goal_achieved:
                    description:
                        - A boolean value to indicate if train goal/targetFap is achieved for trained model
                    returned: on success
                    type: bool
                    sample: true
                warning:
                    description:
                        - A warning message to explain the reason when targetFap cannot be achieved for trained model
                    returned: on success
                    type: str
                    sample: warning_example
                signal_details:
                    description:
                        - The list of signal details.
                    returned: on success
                    type: complex
                    contains:
                        signal_name:
                            description:
                                - The name of a signal.
                            returned: on success
                            type: str
                            sample: signal_name_example
                        mvi_ratio:
                            description:
                                - The ratio of missing values in a signal filled/imputed by the IDP algorithm.
                            returned: on success
                            type: float
                            sample: 1.2
                        is_quantized:
                            description:
                                - A boolean value to indicate if a signal is quantized or not.
                            returned: on success
                            type: bool
                            sample: true
                        fap:
                            description:
                                - Accuracy metric for a signal.
                            returned: on success
                            type: float
                            sample: 3.4
                        min:
                            description:
                                - Min value within a signal.
                            returned: on success
                            type: float
                            sample: 1.2
                        max:
                            description:
                                - Max value within a signal.
                            returned: on success
                            type: float
                            sample: 1.2
                        std:
                            description:
                                - Standard deviation of values within a signal.
                            returned: on success
                            type: float
                            sample: 1.2
                        status:
                            description:
                                - "Status of the signal:
                                   * ACCEPTED - the signal is used for training the model
                                   * DROPPED - the signal does not meet requirement, and is dropped before training the model.
                                   * OTHER - placeholder for other status"
                            returned: on success
                            type: str
                            sample: ACCEPTED
                        details:
                            description:
                                - detailed information for a signal.
                            returned: on success
                            type: str
                            sample: details_example
                row_reduction_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_reduction_enabled:
                            description:
                                - A boolean value to indicate if row reduction is applied
                            returned: on success
                            type: bool
                            sample: true
                        reduction_percentage:
                            description:
                                - A percentage to reduce data size down to on top of original data
                            returned: on success
                            type: float
                            sample: 1.2
                        reduction_method:
                            description:
                                - "Method for row reduction:
                                    * DELETE_ROW - delete rows with equal intervals
                                    * AVERAGE_ROW - average multiple rows to one row"
                            returned: on success
                            type: str
                            sample: DELETE_ROW
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
        time_created:
            description:
                - The time the the Model was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the Model was updated. An RFC3339 formatted datetime string.
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
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
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
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "model_training_details": {
            "target_fap": 3.4,
            "training_fraction": 3.4,
            "data_asset_ids": []
        },
        "model_training_results": {
            "fap": 3.4,
            "multivariate_fap": 3.4,
            "is_training_goal_achieved": true,
            "warning": "warning_example",
            "signal_details": [{
                "signal_name": "signal_name_example",
                "mvi_ratio": 1.2,
                "is_quantized": true,
                "fap": 3.4,
                "min": 1.2,
                "max": 1.2,
                "std": 1.2,
                "status": "ACCEPTED",
                "details": "details_example"
            }],
            "row_reduction_details": {
                "is_reduction_enabled": true,
                "reduction_percentage": 1.2,
                "reduction_method": "DELETE_ROW"
            }
        },
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "DELETING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.ai_anomaly_detection import AnomalyDetectionClient
    from oci.ai_anomaly_detection.models import CreateModelDetails
    from oci.ai_anomaly_detection.models import UpdateModelDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ModelHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ModelHelperGen, self).get_possible_entity_types() + [
            "model",
            "models",
            "aiAnomalyDetectionmodel",
            "aiAnomalyDetectionmodels",
            "modelresource",
            "modelsresource",
            "aianomalydetection",
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
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["project_id", "display_name"]

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


ModelHelperCustom = get_custom_class("ModelHelperCustom")


class ResourceHelper(ModelHelperCustom, ModelHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            model_training_details=dict(
                type="dict",
                options=dict(
                    target_fap=dict(type="float"),
                    training_fraction=dict(type="float"),
                    data_asset_ids=dict(type="list", elements="str", required=True),
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

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="model",
        service_client_class=AnomalyDetectionClient,
        namespace="ai_anomaly_detection",
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
