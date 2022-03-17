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
module: oci_ai_speech_transcription_job_facts
short_description: Fetches details about one or multiple TranscriptionJob resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TranscriptionJob resources in Oracle Cloud Infrastructure
    - Returns a list of Transcription Jobs.
    - If I(transcription_job_id) is specified, the details of a single TranscriptionJob will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    transcription_job_id:
        description:
            - Unique Transcription Job identifier.
            - Required to get a specific transcription_job.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources whose lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "ACCEPTED"
            - "IN_PROGRESS"
            - "SUCCEEDED"
            - "FAILED"
            - "CANCELING"
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
- name: Get a specific transcription_job
  oci_ai_speech_transcription_job_facts:
    # required
    transcription_job_id: "ocid1.transcriptionjob.oc1..xxxxxxEXAMPLExxxxxx"

- name: List transcription_jobs
  oci_ai_speech_transcription_job_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: ACCEPTED
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
transcription_jobs:
    description:
        - List of TranscriptionJob resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - Job description.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
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
                        - Locale value as per given in [https://datatracker.ietf.org/doc/html/rfc5646].
                    returned: on success
                    type: str
                    sample: en-US
        normalization:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                filters:
                    description:
                        - List of filters.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - "The type of filters.
                                  Allowed values are:
                                  - `PROFANITY`"
                            returned: on success
                            type: str
                            sample: PROFANITY
                        mode:
                            description:
                                - "The mode of filters.
                                  Allowed values are:
                                  - `MASK`: Will mask detected profanity in transcription.
                                  - `REMOVE`: Will replace profane word with * in transcription.
                                  - `TAG`: Will tag profane word as profanity but will show actual word."
                            returned: on success
                            type: str
                            sample: MASK
        ttl_in_days:
            description:
                - Time to live duration in days for Job. Job will be available till max 90 days.
                - Returned for get operation
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
                        - "The type of input location.
                          Allowed values are:
                          - `OBJECT_LIST_INLINE_INPUT_LOCATION`: A list of object locations in Object Storage.
                          - `OBJECT_LIST_FILE_INPUT_LOCATION`: An object in Object Storage that contains a list of input files."
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
                - Returned for get operation
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
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Job name.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment that contains the transcriptionJob.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        created_by:
            description:
                - OCID of the user who created the transcriptionJob.
            returned: on success
            type: str
            sample: created_by_example
        percent_complete:
            description:
                - How much progress the operation has made, vs the total amount of work that must be performed.
            returned: on success
            type: int
            sample: 56
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
    sample: [{
        "description": "description_example",
        "model_details": {
            "domain": "GENERIC",
            "language_code": "en-US"
        },
        "normalization": {
            "filters": [{
                "type": "PROFANITY",
                "mode": "MASK"
            }]
        },
        "ttl_in_days": 56,
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "created_by": "created_by_example",
        "percent_complete": 56,
        "time_accepted": "2013-10-20T19:20:30+01:00",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "total_tasks": 56,
        "outstanding_tasks": 56,
        "successful_tasks": 56,
        "lifecycle_state": "ACCEPTED",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.ai_speech import AIServiceSpeechClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TranscriptionJobFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "transcription_job_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transcription_job,
            transcription_job_id=self.module.params.get("transcription_job_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
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
            self.client.list_transcription_jobs, **optional_kwargs
        )


TranscriptionJobFactsHelperCustom = get_custom_class(
    "TranscriptionJobFactsHelperCustom"
)


class ResourceFactsHelper(
    TranscriptionJobFactsHelperCustom, TranscriptionJobFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            transcription_job_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACCEPTED",
                    "IN_PROGRESS",
                    "SUCCEEDED",
                    "FAILED",
                    "CANCELING",
                    "CANCELED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="transcription_job",
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

    module.exit_json(transcription_jobs=result)


if __name__ == "__main__":
    main()
