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
module: oci_ai_document_processor_job_facts
short_description: Fetches details about a ProcessorJob resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ProcessorJob resource in Oracle Cloud Infrastructure
    - Get the details of a processor job.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    processor_job_id:
        description:
            - Processor job id.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific processor_job
  oci_ai_document_processor_job_facts:
    # required
    processor_job_id: "ocid1.processorjob.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
processor_job:
    description:
        - ProcessorJob resource
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The id of the processor job.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The compartment identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the processor job.
            returned: on success
            type: str
            sample: display_name_example
        processor_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                processor_type:
                    description:
                        - The type of the processor.
                    returned: on success
                    type: str
                    sample: GENERAL
                document_type:
                    description:
                        - The document type.
                    returned: on success
                    type: str
                    sample: INVOICE
                features:
                    description:
                        - The types of document analysis requested.
                    returned: on success
                    type: complex
                    contains:
                        max_results:
                            description:
                                - The maximum number of results to return.
                            returned: on success
                            type: int
                            sample: 56
                        feature_type:
                            description:
                                - "The type of document analysis requested.
                                  The allowed values are:
                                  - `LANGUAGE_CLASSIFICATION`: Detect the language.
                                  - `TEXT_EXTRACTION`: Recognize text.
                                  - `TABLE_EXTRACTION`: Detect and extract data in tables.
                                  - `KEY_VALUE_EXTRACTION`: Extract form fields.
                                  - `DOCUMENT_CLASSIFICATION`: Identify the type of document."
                            returned: on success
                            type: str
                            sample: LANGUAGE_CLASSIFICATION
                        generate_searchable_pdf:
                            description:
                                - Whether or not to generate a searchable PDF file.
                            returned: on success
                            type: bool
                            sample: true
                is_zip_output_enabled:
                    description:
                        - Whether or not to generate a ZIP file containing the results.
                    returned: on success
                    type: bool
                    sample: true
                language:
                    description:
                        - The document language, abbreviated according to the BCP 47 Language-Tag syntax.
                    returned: on success
                    type: str
                    sample: language_example
        input_location:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                data:
                    description:
                        - Raw document data with Base64 encoding.
                    returned: on success
                    type: str
                    sample: "null"

                source_type:
                    description:
                        - "The type of input location.
                          The allowed values are:
                          - `OBJECT_STORAGE_LOCATIONS`: A list of object locations in Object Storage.
                          - `INLINE_DOCUMENT_CONTENT`: The content of an inline document."
                    returned: on success
                    type: str
                    sample: OBJECT_STORAGE_LOCATIONS
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
                - The current state of the processor job.
            returned: on success
            type: str
            sample: SUCCEEDED
        lifecycle_details:
            description:
                - The detailed status of FAILED state.
            returned: on success
            type: str
            sample: PARTIALLY_SUCCEEDED
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "processor_config": {
            "processor_type": "GENERAL",
            "document_type": "INVOICE",
            "features": [{
                "max_results": 56,
                "feature_type": "LANGUAGE_CLASSIFICATION",
                "generate_searchable_pdf": true
            }],
            "is_zip_output_enabled": true,
            "language": "language_example"
        },
        "input_location": {
            "data": null,
            "source_type": "OBJECT_STORAGE_LOCATIONS",
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
        "lifecycle_details": "PARTIALLY_SUCCEEDED"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.ai_document import AIServiceDocumentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProcessorJobFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "processor_job_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_processor_job,
            processor_job_id=self.module.params.get("processor_job_id"),
        )


ProcessorJobFactsHelperCustom = get_custom_class("ProcessorJobFactsHelperCustom")


class ResourceFactsHelper(ProcessorJobFactsHelperCustom, ProcessorJobFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            processor_job_id=dict(aliases=["id"], type="str", required=True),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="processor_job",
        service_client_class=AIServiceDocumentClient,
        namespace="ai_document",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(processor_job=result)


if __name__ == "__main__":
    main()
