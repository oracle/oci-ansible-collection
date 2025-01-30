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
module: oci_ai_anomaly_detection_model_actions
short_description: Perform actions on a Model resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Model resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a Model resource from one compartment to another. When provided, If-Match is checked against ETag values of the
      resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    model_id:
        description:
            - The OCID of the Model.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
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
  oci_ai_anomaly_detection_model_actions:
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
                algorithm_hint:
                    description:
                        - User can choose specific algorithm for training.
                    returned: on success
                    type: str
                    sample: MULTIVARIATE_MSET
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
                window_size:
                    description:
                        - This value would determine the window size of the training algorithm.
                    returned: on success
                    type: int
                    sample: 56
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
                algorithm:
                    description:
                        - Actual algorithm used to train the model
                    returned: on success
                    type: str
                    sample: MULTIVARIATE_MSET
                window_size:
                    description:
                        - Window size defined during training or deduced by the algorithm.
                    returned: on success
                    type: int
                    sample: 56
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
                  Example: `{ \\"orcl-cloud\\": { \\"free-tier-retained\\": \\"true\\" } }`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "model_training_details": {
            "algorithm_hint": "MULTIVARIATE_MSET",
            "target_fap": 3.4,
            "training_fraction": 3.4,
            "window_size": 56,
            "data_asset_ids": []
        },
        "model_training_results": {
            "fap": 3.4,
            "multivariate_fap": 3.4,
            "algorithm": "MULTIVARIATE_MSET",
            "window_size": 56,
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
    from oci.ai_anomaly_detection import AnomalyDetectionClient
    from oci.ai_anomaly_detection.models import ChangeModelCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ModelActionsHelperGen(OCIActionsHelperBase):
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


ModelActionsHelperCustom = get_custom_class("ModelActionsHelperCustom")


class ResourceHelper(ModelActionsHelperCustom, ModelActionsHelperGen):
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
        service_client_class=AnomalyDetectionClient,
        namespace="ai_anomaly_detection",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
