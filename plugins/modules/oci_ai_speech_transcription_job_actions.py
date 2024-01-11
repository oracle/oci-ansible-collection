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
module: oci_ai_speech_transcription_job_actions
short_description: Perform actions on a TranscriptionJob resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a TranscriptionJob resource in Oracle Cloud Infrastructure
    - For I(action=cancel), canceling the job cancels all the tasks under it.
    - For I(action=change_compartment), moves a transcription Job resource into a different compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    transcription_job_id:
        description:
            - Unique Transcription Job identifier.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              where the resource should be moved.
            - Required for I(action=change_compartment).
        type: str
    action:
        description:
            - The action to perform on the TranscriptionJob.
        type: str
        required: true
        choices:
            - "cancel"
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action cancel on transcription_job
  oci_ai_speech_transcription_job_actions:
    # required
    transcription_job_id: "ocid1.transcriptionjob.oc1..xxxxxxEXAMPLExxxxxx"
    action: cancel

- name: Perform action change_compartment on transcription_job
  oci_ai_speech_transcription_job_actions:
    # required
    transcription_job_id: "ocid1.transcriptionjob.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
transcription_job:
    description:
        - Details of the TranscriptionJob resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the job.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want to create the job.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - A short description of the job.
            returned: on success
            type: str
            sample: description_example
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
        normalization:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_punctuation_enabled:
                    description:
                        - Whether to add punctuation in the generated transcription. Enabled by default.
                    returned: on success
                    type: bool
                    sample: true
                filters:
                    description:
                        - List of filters.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - The type of filters.
                            returned: on success
                            type: str
                            sample: PROFANITY
                        mode:
                            description:
                                - "- `MASK`: Will mask detected profanity in transcription.
                                  - `REMOVE`: Will replace profane word with * in transcription.
                                  - `TAG`: Will tag profane word as profanity but will show actual word."
                            returned: on success
                            type: str
                            sample: MASK
        time_accepted:
            description:
                - Job accepted time.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_started:
            description:
                - Job started time.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_finished:
            description:
                - Job finished time.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        total_tasks:
            description:
                - Total tasks in a job.
            returned: on success
            type: int
            sample: 56
        outstanding_tasks:
            description:
                - Total outstanding tasks in a job.
            returned: on success
            type: int
            sample: 56
        successful_tasks:
            description:
                - Total successful tasks in a job.
            returned: on success
            type: int
            sample: 56
        ttl_in_days:
            description:
                - Time to live duration in days for Job. Job will be available till max 90 days.
            returned: on success
            type: int
            sample: 56
        percent_complete:
            description:
                - How much progress the operation has made, vs the total amount of work that must be performed.
            returned: on success
            type: int
            sample: 56
        input_location:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                object_location:
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
                location_type:
                    description:
                        - The type of input location.
                    returned: on success
                    type: str
                    sample: OBJECT_LIST_INLINE_INPUT_LOCATION
                object_locations:
                    description:
                        - A list of ObjectLocations.
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
        created_by:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the job.
            returned: on success
            type: str
            sample: created_by_example
        additional_transcription_formats:
            description:
                - Transcription format. JSON format will always be provided in addition to any formats in this list.
            returned: on success
            type: list
            sample: []
        lifecycle_state:
            description:
                - The current state of the Job.
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
        "description": "description_example",
        "model_details": {
            "domain": "GENERIC",
            "language_code": "en-US"
        },
        "normalization": {
            "is_punctuation_enabled": true,
            "filters": [{
                "type": "PROFANITY",
                "mode": "MASK"
            }]
        },
        "time_accepted": "2013-10-20T19:20:30+01:00",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "total_tasks": 56,
        "outstanding_tasks": 56,
        "successful_tasks": 56,
        "ttl_in_days": 56,
        "percent_complete": 56,
        "input_location": {
            "object_location": {
                "namespace_name": "namespace_name_example",
                "bucket_name": "bucket_name_example",
                "object_names": []
            },
            "location_type": "OBJECT_LIST_INLINE_INPUT_LOCATION",
            "object_locations": [{
                "namespace_name": "namespace_name_example",
                "bucket_name": "bucket_name_example",
                "object_names": []
            }]
        },
        "output_location": {
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example",
            "prefix": "prefix_example"
        },
        "created_by": "created_by_example",
        "additional_transcription_formats": [],
        "lifecycle_state": "ACCEPTED",
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
    from oci.ai_speech import AIServiceSpeechClient
    from oci.ai_speech.models import ChangeTranscriptionJobCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TranscriptionJobActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "transcription_job_id"

    def get_module_resource_id(self):
        return self.module.params.get("transcription_job_id")

    def get_get_fn(self):
        return self.client.get_transcription_job

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transcription_job,
            transcription_job_id=self.module.params.get("transcription_job_id"),
        )

    def cancel(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_transcription_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                transcription_job_id=self.module.params.get("transcription_job_id"),
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeTranscriptionJobCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_transcription_job_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                transcription_job_id=self.module.params.get("transcription_job_id"),
                change_transcription_job_compartment_details=action_details,
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


TranscriptionJobActionsHelperCustom = get_custom_class(
    "TranscriptionJobActionsHelperCustom"
)


class ResourceHelper(
    TranscriptionJobActionsHelperCustom, TranscriptionJobActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            transcription_job_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            action=dict(
                type="str", required=True, choices=["cancel", "change_compartment"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="transcription_job",
        service_client_class=AIServiceSpeechClient,
        namespace="ai_speech",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
