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
module: oci_ai_vision_image_job_actions
short_description: Perform actions on an ImageJob resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an ImageJob resource in Oracle Cloud Infrastructure
    - For I(action=cancel), cancel an image batch job.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    image_job_id:
        description:
            - Image job id.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the ImageJob.
        type: str
        required: true
        choices:
            - "cancel"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action cancel on image_job
  oci_ai_vision_image_job_actions:
    # required
    image_job_id: "ocid1.imagejob.oc1..xxxxxxEXAMPLExxxxxx"
    action: cancel

"""

RETURN = """
image_job:
    description:
        - Details of the ImageJob resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The job id
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
                - The image job display name.
            returned: on success
            type: str
            sample: display_name_example
        features:
            description:
                - The list of requested document analysis types.
            returned: on success
            type: complex
            contains:
                max_results:
                    description:
                        - The maximum number of results to return.
                    returned: on success
                    type: int
                    sample: 56
                model_id:
                    description:
                        - The custom model ID.
                    returned: on success
                    type: str
                    sample: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
                feature_type:
                    description:
                        - "The type of image analysis requested.
                          The allowed values are:
                          - `IMAGE_CLASSIFICATION`: Label the image.
                          - `OBJECT_DETECTION`: Identify objects in the image with bounding boxes.
                          - `TEXT_DETECTION`: Recognize text in the image."
                    returned: on success
                    type: str
                    sample: IMAGE_CLASSIFICATION
                language:
                    description:
                        - The language of the document image, abbreviated according to ISO 639-2.
                    returned: on success
                    type: str
                    sample: ENG
        input_location:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                source_type:
                    description:
                        - "The type of input location.
                          The allowed values are:
                          - `OBJECT_LIST_INLINE_INPUT_LOCATION`: A list of object locations in Object Storage."
                    returned: on success
                    type: str
                    sample: OBJECT_LIST_INLINE_INPUT_LOCATION
                object_locations:
                    description:
                        - The list of ObjectLocations.
                    returned: on success
                    type: complex
                    contains:
                        namespace_name:
                            description:
                                - The Object Storage namespace name.
                            returned: on success
                            type: str
                            sample: namespace_name_example
                        bucket_name:
                            description:
                                - The Object Storage bucket name.
                            returned: on success
                            type: str
                            sample: bucket_name_example
                        object_name:
                            description:
                                - The Object Storage object name.
                            returned: on success
                            type: str
                            sample: object_name_example
        time_accepted:
            description:
                - The job acceptance time.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_started:
            description:
                - The job start time.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_finished:
            description:
                - The job finish time.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        percent_complete:
            description:
                - How much progress the operation has made, compared to the total amount of work to be performed.
            returned: on success
            type: float
            sample: 3.4
        output_location:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                namespace_name:
                    description:
                        - The Object Storage namespace.
                    returned: on success
                    type: str
                    sample: namespace_name_example
                bucket_name:
                    description:
                        - The Object Storage bucket name.
                    returned: on success
                    type: str
                    sample: bucket_name_example
                prefix:
                    description:
                        - The Object Storage folder name.
                    returned: on success
                    type: str
                    sample: prefix_example
        lifecycle_state:
            description:
                - The current state of the batch image job.
            returned: on success
            type: str
            sample: SUCCEEDED
        lifecycle_details:
            description:
                - The detailed status of FAILED state.
            returned: on success
            type: str
            sample: PARTIALLY_SUCCEEDED
        is_zip_output_enabled:
            description:
                - Whether or not to generate a ZIP file containing the results.
            returned: on success
            type: bool
            sample: true
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "features": [{
            "max_results": 56,
            "model_id": "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx",
            "feature_type": "IMAGE_CLASSIFICATION",
            "language": "ENG"
        }],
        "input_location": {
            "source_type": "OBJECT_LIST_INLINE_INPUT_LOCATION",
            "object_locations": [{
                "namespace_name": "namespace_name_example",
                "bucket_name": "bucket_name_example",
                "object_name": "object_name_example"
            }]
        },
        "time_accepted": "2013-10-20T19:20:30+01:00",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "percent_complete": 3.4,
        "output_location": {
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example",
            "prefix": "prefix_example"
        },
        "lifecycle_state": "SUCCEEDED",
        "lifecycle_details": "PARTIALLY_SUCCEEDED",
        "is_zip_output_enabled": true
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

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiVisionImageJobActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel
    """

    @staticmethod
    def get_module_resource_id_param():
        return "image_job_id"

    def get_module_resource_id(self):
        return self.module.params.get("image_job_id")

    def get_get_fn(self):
        return self.client.get_image_job

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_image_job,
            image_job_id=self.module.params.get("image_job_id"),
        )

    def cancel(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_image_job,
            call_fn_args=(),
            call_fn_kwargs=dict(image_job_id=self.module.params.get("image_job_id"),),
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


AiVisionImageJobActionsHelperCustom = get_custom_class(
    "AiVisionImageJobActionsHelperCustom"
)


class ResourceHelper(
    AiVisionImageJobActionsHelperCustom, AiVisionImageJobActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            image_job_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["cancel"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="image_job",
        service_client_class=AIServiceVisionClient,
        namespace="ai_vision",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
