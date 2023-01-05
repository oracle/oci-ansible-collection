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
module: oci_ai_speech_transcription_task_facts
short_description: Fetches details about one or multiple TranscriptionTask resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TranscriptionTask resources in Oracle Cloud Infrastructure
    - Returns a list of Transcription Tasks.
    - If I(transcription_task_id) is specified, the details of a single TranscriptionTask will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    transcription_task_id:
        description:
            - Unique Transcription Task identifier.
            - Required to get a specific transcription_task.
        type: str
        aliases: ["id"]
    transcription_job_id:
        description:
            - Unique Transcription Job identifier.
        type: str
        required: true
    lifecycle_state:
        description:
            - A filter to return only resources whose lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "ACCEPTED"
            - "IN_PROGRESS"
            - "SUCCEEDED"
            - "FAILED"
            - "CANCELED"
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
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific transcription_task
  oci_ai_speech_transcription_task_facts:
    # required
    transcription_task_id: "ocid1.transcriptiontask.oc1..xxxxxxEXAMPLExxxxxx"
    transcription_job_id: "ocid1.transcriptionjob.oc1..xxxxxxEXAMPLExxxxxx"

- name: List transcription_tasks
  oci_ai_speech_transcription_task_facts:
    # required
    transcription_job_id: "ocid1.transcriptionjob.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: ACCEPTED
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
transcription_tasks:
    description:
        - List of TranscriptionTask resources
    returned: on success
    type: complex
    contains:
        ttl_in_days:
            description:
                - Time to live duration in days for tasks. Task will be available till max 90 days.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        model_details:
            description:
                - ""
                - Returned for get operation
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
                - Returned for get operation
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
        input_location:
            description:
                - ""
                - Returned for get operation
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
                - Returned for get operation
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
        percent_complete:
            description:
                - How much progress the operation has made, vs the total amount of work that must be performed.
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
    sample: [{
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "percent_complete": 56,
        "file_size_in_bytes": 56,
        "file_duration_in_seconds": 56,
        "processing_duration_in_seconds": 56,
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACCEPTED",
        "lifecycle_details": "lifecycle_details_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.ai_speech import AIServiceSpeechClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TranscriptionTaskFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "transcription_job_id",
            "transcription_task_id",
        ]

    def get_required_params_for_list(self):
        return [
            "transcription_job_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transcription_task,
            transcription_job_id=self.module.params.get("transcription_job_id"),
            transcription_task_id=self.module.params.get("transcription_task_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
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
            self.client.list_transcription_tasks,
            transcription_job_id=self.module.params.get("transcription_job_id"),
            **optional_kwargs
        )


TranscriptionTaskFactsHelperCustom = get_custom_class(
    "TranscriptionTaskFactsHelperCustom"
)


class ResourceFactsHelper(
    TranscriptionTaskFactsHelperCustom, TranscriptionTaskFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            transcription_task_id=dict(aliases=["id"], type="str"),
            transcription_job_id=dict(type="str", required=True),
            lifecycle_state=dict(
                type="str",
                choices=["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED"],
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
        resource_type="transcription_task",
        service_client_class=AIServiceSpeechClient,
        namespace="ai_speech",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(transcription_tasks=result)


if __name__ == "__main__":
    main()
