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
module: oci_ai_anomaly_detection_detect_anomaly_job_facts
short_description: Fetches details about one or multiple DetectAnomalyJob resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DetectAnomalyJob resources in Oracle Cloud Infrastructure
    - Returns a list of all the Anomaly Detection jobs in the specified compartment.
    - If I(detect_anomaly_job_id) is specified, the details of a single DetectAnomalyJob will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple detect_anomaly_jobs.
        type: str
    model_id:
        description:
            - The ID of the trained model for which to list the resources.
        type: str
    project_id:
        description:
            - The ID of the project for which to list the objects.
        type: str
    detect_anomaly_job_id:
        description:
            - Unique asynchronous job identifier.
            - Required to get a specific detect_anomaly_job.
        type: str
        aliases: ["id"]
    lifecycle_state:
        description:
            - <b>Filter</b> results by the specified lifecycle state. Must be a valid
              state for the resource type.
        type: str
        choices:
            - "SUCCEEDED"
            - "PARTIALLY_SUCCEEDED"
            - "FAILED"
            - "ACCEPTED"
            - "CANCELED"
            - "IN_PROGRESS"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific detect_anomaly_job
  oci_ai_anomaly_detection_detect_anomaly_job_facts:
    # required
    detect_anomaly_job_id: "ocid1.detectanomalyjob.oc1..xxxxxxEXAMPLExxxxxx"

- name: List detect_anomaly_jobs
  oci_ai_anomaly_detection_detect_anomaly_job_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    detect_anomaly_job_id: "ocid1.detectanomalyjob.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: SUCCEEDED
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
detect_anomaly_jobs:
    description:
        - List of DetectAnomalyJob resources
    returned: on success
    type: complex
    contains:
        sensitivity:
            description:
                - The value that customer can adjust to control the sensitivity of anomaly detection
                - Returned for get operation
            returned: on success
            type: float
            sample: 3.4
        are_all_estimates_required:
            description:
                - Flag to enable the service to return estimates for all data points rather than just the anomalous data points
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        input_details:
            description:
                - ""
                - Returned for get operation
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
                - Returned for get operation
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
    sample: [{
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "model_id": "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "time_accepted": "2013-10-20T19:20:30+01:00",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "SUCCEEDED",
        "lifecycle_state_details": "lifecycle_state_details_example",
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
    from oci.ai_anomaly_detection import AnomalyDetectionClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DetectAnomalyJobFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "detect_anomaly_job_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_detect_anomaly_job,
            detect_anomaly_job_id=self.module.params.get("detect_anomaly_job_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "model_id",
            "project_id",
            "detect_anomaly_job_id",
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
            self.client.list_detect_anomaly_jobs,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DetectAnomalyJobFactsHelperCustom = get_custom_class(
    "DetectAnomalyJobFactsHelperCustom"
)


class ResourceFactsHelper(
    DetectAnomalyJobFactsHelperCustom, DetectAnomalyJobFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            model_id=dict(type="str"),
            project_id=dict(type="str"),
            detect_anomaly_job_id=dict(aliases=["id"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "SUCCEEDED",
                    "PARTIALLY_SUCCEEDED",
                    "FAILED",
                    "ACCEPTED",
                    "CANCELED",
                    "IN_PROGRESS",
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
        resource_type="detect_anomaly_job",
        service_client_class=AnomalyDetectionClient,
        namespace="ai_anomaly_detection",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(detect_anomaly_jobs=result)


if __name__ == "__main__":
    main()
