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
module: oci_ai_speech_transcription_job
short_description: Manage a TranscriptionJob resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and update a TranscriptionJob resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Transcription Job.
    - "This resource has the following action operations in the M(oracle.oci.oci_ai_speech_transcription_job_actions) module: cancel, change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want to create the job.
            - Required for create using I(state=present).
        type: str
    additional_transcription_formats:
        description:
            - Transcription Format. By default, the JSON format is used.
        type: list
        elements: str
        choices:
            - "SRT"
    model_details:
        description:
            - ""
        type: dict
        suboptions:
            domain:
                description:
                    - Domain for input files.
                type: str
                choices:
                    - "GENERIC"
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
                type: str
                choices:
                    - "en-US"
                    - "es-ES"
                    - "pt-BR"
                    - "en-GB"
                    - "en-AU"
                    - "en-IN"
                    - "hi-IN"
                    - "fr-FR"
                    - "de-DE"
                    - "it-IT"
    normalization:
        description:
            - ""
        type: dict
        suboptions:
            is_punctuation_enabled:
                description:
                    - Whether to add punctuation in the generated transcription. Enabled by default.
                type: bool
            filters:
                description:
                    - List of filters.
                type: list
                elements: dict
                suboptions:
                    type:
                        description:
                            - The type of filters.
                        type: str
                        choices:
                            - "PROFANITY"
                        required: true
                    mode:
                        description:
                            - "- `MASK`: Will mask detected profanity in transcription.
                              - `REMOVE`: Will replace profane word with * in transcription.
                              - `TAG`: Will tag profane word as profanity but will show actual word."
                        type: str
                        choices:
                            - "MASK"
                            - "REMOVE"
                            - "TAG"
                        required: true
    input_location:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            object_location:
                description:
                    - ""
                    - Required when location_type is 'OBJECT_LIST_FILE_INPUT_LOCATION'
                type: dict
                suboptions:
                    namespace_name:
                        description:
                            - Object Storage namespace name.
                            - Required when location_type is 'OBJECT_LIST_FILE_INPUT_LOCATION'
                        type: str
                        required: true
                    bucket_name:
                        description:
                            - Object Storage bucket name.
                            - Required when location_type is 'OBJECT_LIST_FILE_INPUT_LOCATION'
                        type: str
                        required: true
                    object_names:
                        description:
                            - Object Storage object names.
                            - Required when location_type is 'OBJECT_LIST_FILE_INPUT_LOCATION'
                        type: list
                        elements: str
                        required: true
            location_type:
                description:
                    - The type of input location.
                type: str
                choices:
                    - "OBJECT_LIST_FILE_INPUT_LOCATION"
                    - "OBJECT_LIST_INLINE_INPUT_LOCATION"
                required: true
            object_locations:
                description:
                    - A list of ObjectLocations.
                    - Required when location_type is 'OBJECT_LIST_INLINE_INPUT_LOCATION'
                type: list
                elements: dict
                suboptions:
                    namespace_name:
                        description:
                            - Object Storage namespace name.
                            - Required when location_type is 'OBJECT_LIST_INLINE_INPUT_LOCATION'
                        type: str
                        required: true
                    bucket_name:
                        description:
                            - Object Storage bucket name.
                            - Required when location_type is 'OBJECT_LIST_INLINE_INPUT_LOCATION'
                        type: str
                        required: true
                    object_names:
                        description:
                            - Object Storage object names.
                            - Required when location_type is 'OBJECT_LIST_INLINE_INPUT_LOCATION'
                        type: list
                        elements: str
                        required: true
    output_location:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
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
                required: true
    transcription_job_id:
        description:
            - Unique Transcription Job identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    display_name:
        description:
            - A user-friendly display name for the job.
            - Required for create, update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A short description of the job.
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
    state:
        description:
            - The state of the TranscriptionJob.
            - Use I(state=present) to create or update a TranscriptionJob.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create transcription_job
  oci_ai_speech_transcription_job:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    input_location:
      # required
      object_location:
        # required
        namespace_name: namespace_name_example
        bucket_name: bucket_name_example
        object_names: [ "object_names_example" ]
      location_type: OBJECT_LIST_FILE_INPUT_LOCATION
    output_location:
      # required
      namespace_name: namespace_name_example
      bucket_name: bucket_name_example
      prefix: prefix_example

    # optional
    additional_transcription_formats: [ "SRT" ]
    model_details:
      # optional
      domain: GENERIC
      language_code: en-US
    normalization:
      # optional
      is_punctuation_enabled: true
      filters:
      - # required
        type: PROFANITY
        mode: MASK
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update transcription_job
  oci_ai_speech_transcription_job:
    # required
    transcription_job_id: "ocid1.transcriptionjob.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update transcription_job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_ai_speech_transcription_job:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.ai_speech import AIServiceSpeechClient
    from oci.ai_speech.models import CreateTranscriptionJobDetails
    from oci.ai_speech.models import UpdateTranscriptionJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TranscriptionJobHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_possible_entity_types(self):
        return super(TranscriptionJobHelperGen, self).get_possible_entity_types() + [
            "aispeechtranscriptionjob",
            "aispeechtranscriptionjobs",
            "aiSpeechaispeechtranscriptionjob",
            "aiSpeechaispeechtranscriptionjobs",
            "aispeechtranscriptionjobresource",
            "aispeechtranscriptionjobsresource",
            "transcriptionjob",
            "transcriptionjobs",
            "aiSpeechtranscriptionjob",
            "aiSpeechtranscriptionjobs",
            "transcriptionjobresource",
            "transcriptionjobsresource",
            "aispeech",
        ]

    def get_module_resource_id_param(self):
        return "transcription_job_id"

    def get_module_resource_id(self):
        return self.module.params.get("transcription_job_id")

    def get_get_fn(self):
        return self.client.get_transcription_job

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_transcription_job, transcription_job_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transcription_job,
            transcription_job_id=self.module.params.get("transcription_job_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "display_name"]

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
            self.client.list_transcription_jobs, **kwargs
        )

    def get_create_model_class(self):
        return CreateTranscriptionJobDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_transcription_job,
            call_fn_args=(),
            call_fn_kwargs=dict(create_transcription_job_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateTranscriptionJobDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_transcription_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                transcription_job_id=self.module.params.get("transcription_job_id"),
                update_transcription_job_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


TranscriptionJobHelperCustom = get_custom_class("TranscriptionJobHelperCustom")


class ResourceHelper(TranscriptionJobHelperCustom, TranscriptionJobHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            additional_transcription_formats=dict(
                type="list", elements="str", choices=["SRT"]
            ),
            model_details=dict(
                type="dict",
                options=dict(
                    domain=dict(type="str", choices=["GENERIC"]),
                    language_code=dict(
                        type="str",
                        choices=[
                            "en-US",
                            "es-ES",
                            "pt-BR",
                            "en-GB",
                            "en-AU",
                            "en-IN",
                            "hi-IN",
                            "fr-FR",
                            "de-DE",
                            "it-IT",
                        ],
                    ),
                ),
            ),
            normalization=dict(
                type="dict",
                options=dict(
                    is_punctuation_enabled=dict(type="bool"),
                    filters=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(type="str", required=True, choices=["PROFANITY"]),
                            mode=dict(
                                type="str",
                                required=True,
                                choices=["MASK", "REMOVE", "TAG"],
                            ),
                        ),
                    ),
                ),
            ),
            input_location=dict(
                type="dict",
                options=dict(
                    object_location=dict(
                        type="dict",
                        options=dict(
                            namespace_name=dict(type="str", required=True),
                            bucket_name=dict(type="str", required=True),
                            object_names=dict(
                                type="list", elements="str", required=True
                            ),
                        ),
                    ),
                    location_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "OBJECT_LIST_FILE_INPUT_LOCATION",
                            "OBJECT_LIST_INLINE_INPUT_LOCATION",
                        ],
                    ),
                    object_locations=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            namespace_name=dict(type="str", required=True),
                            bucket_name=dict(type="str", required=True),
                            object_names=dict(
                                type="list", elements="str", required=True
                            ),
                        ),
                    ),
                ),
            ),
            output_location=dict(
                type="dict",
                options=dict(
                    namespace_name=dict(type="str", required=True),
                    bucket_name=dict(type="str", required=True),
                    prefix=dict(type="str", required=True),
                ),
            ),
            transcription_job_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            state=dict(type="str", default="present", choices=["present"]),
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

    result = dict(changed=False)

    if resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
