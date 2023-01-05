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
module: oci_ai_speech_transcription_task_actions
short_description: Perform actions on a TranscriptionTask resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a TranscriptionTask resource in Oracle Cloud Infrastructure
    - For I(action=cancel), cancel Transcription Task
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    transcription_job_id:
        description:
            - Unique Transcription Job identifier.
        type: str
        required: true
    transcription_task_id:
        description:
            - Unique Transcription Task identifier.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the TranscriptionTask.
        type: str
        required: true
        choices:
            - "cancel"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action cancel on transcription_task
  oci_ai_speech_transcription_task_actions:
    # required
    transcription_job_id: "ocid1.transcriptionjob.oc1..xxxxxxEXAMPLExxxxxx"
    transcription_task_id: "ocid1.transcriptiontask.oc1..xxxxxxEXAMPLExxxxxx"
    action: cancel

"""

RETURN = """
transcription_task:
    description:
        - Details of the TranscriptionTask resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the task.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the task.
            returned: on success
            type: str
            sample: display_name_example
        time_started:
            description:
                - Task started time.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_finished:
            description:
                - Task finished time.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        percent_complete:
            description:
                - How much progress the operation has made, vs the total amount of work that must be performed.
            returned: on success
            type: int
            sample: 56
        ttl_in_days:
            description:
                - Time to live duration in days for tasks. Task will be available till max 90 days.
            returned: on success
            type: int
            sample: 56
        model_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                domain:
                    description:
                        - Domain for input files.
                    returned: on success
                    type: str
                    sample: GENERIC
                language_code:
                    description:
                        - "Locale value as per given in [https://datatracker.ietf.org/doc/html/rfc5646].
                          - en-US: English - United States
                          - es-ES: Spanish - Spain
                          - pt-BR: Portuguese - Brazil
                          - en-GB: English - Great Britain
                          - en-AU: English - Australia
                          - en-IN: English - India
                          - hi-IN: Hindi - India
                          - fr-FR: French - France
                          - de-DE: German - Germany
                          - it-IT: Italian - Italy"
                    returned: on success
                    type: str
                    sample: en-US
        audio_format_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                format:
                    description:
                        - "Input file format. Example - WAV."
                    returned: on success
                    type: str
                    sample: format_example
                number_of_channels:
                    description:
                        - Input file number of channels.
                    returned: on success
                    type: int
                    sample: 56
                encoding:
                    description:
                        - "Input file encoding. Example - PCM."
                    returned: on success
                    type: str
                    sample: encoding_example
                sample_rate_in_hz:
                    description:
                        - "Input file sampleRate. Example - 16000"
                    returned: on success
                    type: int
                    sample: 56
        file_size_in_bytes:
            description:
                - Size of input file in Bytes.
            returned: on success
            type: int
            sample: 56
        file_duration_in_seconds:
            description:
                - Duration of input file in Seconds.
            returned: on success
            type: int
            sample: 56
        processing_duration_in_seconds:
            description:
                - Task proccessing duration, which excludes waiting time in the system.
            returned: on success
            type: int
            sample: 56
        input_location:
            description:
                - ""
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
                object_names:
                    description:
                        - Object Storage object names.
                    returned: on success
                    type: list
                    sample: []
        output_location:
            description:
                - ""
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
                object_names:
                    description:
                        - Object Storage object names.
                    returned: on success
                    type: list
                    sample: []
        lifecycle_state:
            description:
                - The current state of the Task.
            returned: on success
            type: str
            sample: ACCEPTED
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "percent_complete": 56,
        "ttl_in_days": 56,
        "model_details": {
            "domain": "GENERIC",
            "language_code": "en-US"
        },
        "audio_format_details": {
            "format": "format_example",
            "number_of_channels": 56,
            "encoding": "encoding_example",
            "sample_rate_in_hz": 56
        },
        "file_size_in_bytes": 56,
        "file_duration_in_seconds": 56,
        "processing_duration_in_seconds": 56,
        "input_location": {
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example",
            "object_names": []
        },
        "output_location": {
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example",
            "object_names": []
        },
        "lifecycle_state": "ACCEPTED",
        "lifecycle_details": "lifecycle_details_example"
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
    from oci.ai_speech import AIServiceSpeechClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TranscriptionTaskActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel
    """

    @staticmethod
    def get_module_resource_id_param():
        return "transcription_task_id"

    def get_module_resource_id(self):
        return self.module.params.get("transcription_task_id")

    def get_get_fn(self):
        return self.client.get_transcription_task

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transcription_task,
            transcription_job_id=self.module.params.get("transcription_job_id"),
            transcription_task_id=self.module.params.get("transcription_task_id"),
        )

    def cancel(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_transcription_task,
            call_fn_args=(),
            call_fn_kwargs=dict(
                transcription_job_id=self.module.params.get("transcription_job_id"),
                transcription_task_id=self.module.params.get("transcription_task_id"),
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


TranscriptionTaskActionsHelperCustom = get_custom_class(
    "TranscriptionTaskActionsHelperCustom"
)


class ResourceHelper(
    TranscriptionTaskActionsHelperCustom, TranscriptionTaskActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            transcription_job_id=dict(type="str", required=True),
            transcription_task_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["cancel"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="transcription_task",
        service_client_class=AIServiceSpeechClient,
        namespace="ai_speech",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
