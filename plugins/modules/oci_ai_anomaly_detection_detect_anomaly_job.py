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
module: oci_ai_anomaly_detection_detect_anomaly_job
short_description: Manage a DetectAnomalyJob resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DetectAnomalyJob resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a job to perform anomaly detection.
    - "This resource has the following action operations in the M(oracle.oci.oci_ai_anomaly_detection_detect_anomaly_job_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment that starts the job.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    model_id:
        description:
            - The OCID of the trained model.
            - Required for create using I(state=present).
        type: str
    sensitivity:
        description:
            - The value that customer can adjust to control the sensitivity of anomaly detection
        type: float
    are_all_estimates_required:
        description:
            - Flag to enable the service to return estimates for all data points rather than just the anomalous data points.
        type: bool
    input_details:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            content_type:
                description:
                    - ""
                    - Required when input_type is 'BASE64_ENCODED'
                type: str
                choices:
                    - "CSV"
                    - "JSON"
            content:
                description:
                    - ""
                    - Required when input_type is 'BASE64_ENCODED'
                type: str
            object_locations:
                description:
                    - List of ObjectLocations.
                    - Required when input_type is 'OBJECT_LIST'
                type: list
                elements: dict
                suboptions:
                    namespace_name:
                        description:
                            - Object Storage namespace name.
                            - Required when input_type is 'OBJECT_LIST'
                        type: str
                        required: true
                    bucket_name:
                        description:
                            - Object Storage bucket name.
                            - Required when input_type is 'OBJECT_LIST'
                        type: str
                        required: true
                    object_name:
                        description:
                            - Object Storage object name.
                            - Required when input_type is 'OBJECT_LIST'
                        type: str
                        required: true
            input_type:
                description:
                    - Type of request. This parameter is automatically populated by classes generated
                      by the SDK. For raw curl requests, you must provide this field.
                type: str
                choices:
                    - "BASE64_ENCODED"
                    - "OBJECT_LIST"
                    - "INLINE"
                required: true
            signal_names:
                description:
                    - List of signal names.
                    - Required when input_type is 'INLINE'
                type: list
                elements: str
            data:
                description:
                    - Array containing data.
                    - Required when input_type is 'INLINE'
                type: list
                elements: dict
                suboptions:
                    timestamp:
                        description:
                            - Nullable string representing timestamp.
                            - Applicable when input_type is 'INLINE'
                        type: str
                    values:
                        description:
                            - Array of double precision values.
                            - Required when input_type is 'INLINE'
                        type: list
                        elements: double
                        required: true
    output_details:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            output_type:
                description:
                    - "The type of output location.
                      Allowed values are:
                      - `OBJECT_STORAGE`: Object store output location."
                type: str
                choices:
                    - "OBJECT_STORAGE"
                required: true
            namespace_name:
                description:
                    - Object Storage namespace.
                type: str
                required: true
            bucket_name:
                description:
                    - Object Storage bucket name.
                type: str
                required: true
            prefix:
                description:
                    - Object Storage folder name.
                type: str
    description:
        description:
            - A short description of the detect anomaly job.
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - Detect anomaly job display name.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    detect_anomaly_job_id:
        description:
            - Unique asynchronous job identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DetectAnomalyJob.
            - Use I(state=present) to create or update a DetectAnomalyJob.
            - Use I(state=absent) to delete a DetectAnomalyJob.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create detect_anomaly_job
  oci_ai_anomaly_detection_detect_anomaly_job:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
    input_details:
      # required
      content_type: CSV
      content: content_example
      input_type: BASE64_ENCODED
    output_details:
      # required
      output_type: OBJECT_STORAGE
      namespace_name: namespace_name_example
      bucket_name: bucket_name_example

      # optional
      prefix: prefix_example

    # optional
    sensitivity: 3.4
    are_all_estimates_required: true
    description: description_example
    display_name: display_name_example

- name: Update detect_anomaly_job
  oci_ai_anomaly_detection_detect_anomaly_job:
    # required
    detect_anomaly_job_id: "ocid1.detectanomalyjob.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example

- name: Update detect_anomaly_job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_ai_anomaly_detection_detect_anomaly_job:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example

- name: Delete detect_anomaly_job
  oci_ai_anomaly_detection_detect_anomaly_job:
    # required
    detect_anomaly_job_id: "ocid1.detectanomalyjob.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete detect_anomaly_job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_ai_anomaly_detection_detect_anomaly_job:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.ai_anomaly_detection import AnomalyDetectionClient
    from oci.ai_anomaly_detection.models import CreateDetectAnomalyJobDetails
    from oci.ai_anomaly_detection.models import UpdateDetectAnomalyJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DetectAnomalyJobHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DetectAnomalyJobHelperGen, self).get_possible_entity_types() + [
            "detectanomalyjob",
            "detectanomalyjobs",
            "aiAnomalyDetectiondetectanomalyjob",
            "aiAnomalyDetectiondetectanomalyjobs",
            "detectanomalyjobresource",
            "detectanomalyjobsresource",
            "aianomalydetection",
        ]

    def get_module_resource_id_param(self):
        return "detect_anomaly_job_id"

    def get_module_resource_id(self):
        return self.module.params.get("detect_anomaly_job_id")

    def get_get_fn(self):
        return self.client.get_detect_anomaly_job

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_detect_anomaly_job, detect_anomaly_job_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_detect_anomaly_job,
            detect_anomaly_job_id=self.module.params.get("detect_anomaly_job_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "model_id",
            "detect_anomaly_job_id",
            "display_name",
        ]

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
        return oci_common_utils.list_all_resources(
            self.client.list_detect_anomaly_jobs, **kwargs
        )

    def get_create_model_class(self):
        return CreateDetectAnomalyJobDetails

    def get_exclude_attributes(self):
        return [
            "input_details.data",
            "input_details.content_type",
            "input_details.content",
            "input_details.signal_names",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_detect_anomaly_job,
            call_fn_args=(),
            call_fn_kwargs=dict(create_detect_anomaly_job_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateDetectAnomalyJobDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_detect_anomaly_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                detect_anomaly_job_id=self.module.params.get("detect_anomaly_job_id"),
                update_detect_anomaly_job_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_detect_anomaly_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                detect_anomaly_job_id=self.module.params.get("detect_anomaly_job_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DetectAnomalyJobHelperCustom = get_custom_class("DetectAnomalyJobHelperCustom")


class ResourceHelper(DetectAnomalyJobHelperCustom, DetectAnomalyJobHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            model_id=dict(type="str"),
            sensitivity=dict(type="float"),
            are_all_estimates_required=dict(type="bool"),
            input_details=dict(
                type="dict",
                options=dict(
                    content_type=dict(type="str", choices=["CSV", "JSON"]),
                    content=dict(type="str"),
                    object_locations=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            namespace_name=dict(type="str", required=True),
                            bucket_name=dict(type="str", required=True),
                            object_name=dict(type="str", required=True),
                        ),
                    ),
                    input_type=dict(
                        type="str",
                        required=True,
                        choices=["BASE64_ENCODED", "OBJECT_LIST", "INLINE"],
                    ),
                    signal_names=dict(type="list", elements="str"),
                    data=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            timestamp=dict(type="str"),
                            values=dict(type="list", elements="double", required=True),
                        ),
                    ),
                ),
            ),
            output_details=dict(
                type="dict",
                options=dict(
                    output_type=dict(
                        type="str", required=True, choices=["OBJECT_STORAGE"]
                    ),
                    namespace_name=dict(type="str", required=True),
                    bucket_name=dict(type="str", required=True),
                    prefix=dict(type="str"),
                ),
            ),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            detect_anomaly_job_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
