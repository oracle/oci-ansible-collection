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
module: oci_ai_anomaly_detection_detect_anomaly_job_actions
short_description: Perform actions on a DetectAnomalyJob resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DetectAnomalyJob resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a asynchronous anomaly detect job resource from one compartment to another. When provided, If-Match is checked
      against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    detect_anomaly_job_id:
        description:
            - Unique asynchronous job identifier.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              the resource should be moved to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the DetectAnomalyJob.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on detect_anomaly_job
  oci_ai_anomaly_detection_detect_anomaly_job_actions:
    # required
    detect_anomaly_job_id: "ocid1.detectanomalyjob.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
detect_anomaly_job:
    description:
        - Details of the DetectAnomalyJob resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Id of the job.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that starts the job.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Detect anomaly job display name.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Detect anomaly job description.
            returned: on success
            type: str
            sample: description_example
        model_id:
            description:
                - The OCID of the trained model.
            returned: on success
            type: str
            sample: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
        project_id:
            description:
                - The OCID of the project.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        sensitivity:
            description:
                - The value that customer can adjust to control the sensitivity of anomaly detection
            returned: on success
            type: float
            sample: 3.4
        are_all_estimates_required:
            description:
                - Flag to enable the service to return estimates for all data points rather than just the anomalous data points
            returned: on success
            type: bool
            sample: true
        input_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                message:
                    description:
                        - Inline input details.
                    returned: on success
                    type: str
                    sample: message_example
                input_type:
                    description:
                        - "The type of input location
                          Allowed values are:
                          - `INLINE`: Inline input data.
                          - `OBJECT_LIST`: Object store output location."
                    returned: on success
                    type: str
                    sample: INLINE
                object_locations:
                    description:
                        - List of ObjectLocations.
                    returned: on success
                    type: complex
                    contains:
                        namespace_name:
                            description:
                                - Object Storage namespace name.
                            returned: on success
                            type: str
                            sample: namespace_name_example
                        bucket_name:
                            description:
                                - Object Storage bucket name.
                            returned: on success
                            type: str
                            sample: bucket_name_example
                        object_name:
                            description:
                                - Object Storage object name.
                            returned: on success
                            type: str
                            sample: object_name_example
        output_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                output_type:
                    description:
                        - "The type of output location
                          Allowed values are:
                          - `OBJECT_STORAGE`: Object store output location."
                    returned: on success
                    type: str
                    sample: OBJECT_STORAGE
                namespace_name:
                    description:
                        - Object Storage namespace.
                    returned: on success
                    type: str
                    sample: namespace_name_example
                bucket_name:
                    description:
                        - Object Storage bucket name.
                    returned: on success
                    type: str
                    sample: bucket_name_example
                prefix:
                    description:
                        - Object Storage folder name.
                    returned: on success
                    type: str
                    sample: prefix_example
        time_accepted:
            description:
                - Job accepted time
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_started:
            description:
                - Job started time
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_finished:
            description:
                - Job finished time
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the batch document job.
            returned: on success
            type: str
            sample: SUCCEEDED
        lifecycle_state_details:
            description:
                - The current state details of the batch document job.
            returned: on success
            type: str
            sample: lifecycle_state_details_example
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
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "model_id": "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "sensitivity": 3.4,
        "are_all_estimates_required": true,
        "input_details": {
            "message": "message_example",
            "input_type": "INLINE",
            "object_locations": [{
                "namespace_name": "namespace_name_example",
                "bucket_name": "bucket_name_example",
                "object_name": "object_name_example"
            }]
        },
        "output_details": {
            "output_type": "OBJECT_STORAGE",
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example",
            "prefix": "prefix_example"
        },
        "time_accepted": "2013-10-20T19:20:30+01:00",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "SUCCEEDED",
        "lifecycle_state_details": "lifecycle_state_details_example",
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
    from oci.ai_anomaly_detection.models import ChangeDetectAnomalyJobCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DetectAnomalyJobActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "detect_anomaly_job_id"

    def get_module_resource_id(self):
        return self.module.params.get("detect_anomaly_job_id")

    def get_get_fn(self):
        return self.client.get_detect_anomaly_job

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_detect_anomaly_job,
            detect_anomaly_job_id=self.module.params.get("detect_anomaly_job_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDetectAnomalyJobCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_detect_anomaly_job_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                detect_anomaly_job_id=self.module.params.get("detect_anomaly_job_id"),
                change_detect_anomaly_job_compartment_details=action_details,
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


DetectAnomalyJobActionsHelperCustom = get_custom_class(
    "DetectAnomalyJobActionsHelperCustom"
)


class ResourceHelper(
    DetectAnomalyJobActionsHelperCustom, DetectAnomalyJobActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            detect_anomaly_job_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="detect_anomaly_job",
        service_client_class=AnomalyDetectionClient,
        namespace="ai_anomaly_detection",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
