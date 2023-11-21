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
module: oci_ai_document_processor_job
short_description: Manage a ProcessorJob resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a ProcessorJob resource in Oracle Cloud Infrastructure
    - For I(state=present), create a processor job for document analysis.
    - "This resource has the following action operations in the M(oracle.oci.oci_ai_document_processor_job_actions) module: cancel."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    input_location:
        description:
            - ""
        type: dict
        required: true
        suboptions:
            data:
                description:
                    - Raw document data with Base64 encoding.
                    - Required when source_type is 'INLINE_DOCUMENT_CONTENT'
                type: str
            source_type:
                description:
                    - "The type of input location.
                      The allowed values are:
                      - `OBJECT_STORAGE_LOCATIONS`: A list of object locations in Object Storage.
                      - `INLINE_DOCUMENT_CONTENT`: The content of an inline document."
                type: str
                choices:
                    - "INLINE_DOCUMENT_CONTENT"
                    - "OBJECT_STORAGE_LOCATIONS"
                required: true
            object_locations:
                description:
                    - The list of ObjectLocations.
                    - Required when source_type is 'OBJECT_STORAGE_LOCATIONS'
                type: list
                elements: dict
                suboptions:
                    namespace_name:
                        description:
                            - The Object Storage namespace name.
                            - Required when source_type is 'OBJECT_STORAGE_LOCATIONS'
                        type: str
                        required: true
                    bucket_name:
                        description:
                            - The Object Storage bucket name.
                            - Required when source_type is 'OBJECT_STORAGE_LOCATIONS'
                        type: str
                        required: true
                    object_name:
                        description:
                            - The Object Storage object name.
                            - Required when source_type is 'OBJECT_STORAGE_LOCATIONS'
                        type: str
                        required: true
    output_location:
        description:
            - ""
        type: dict
        required: true
        suboptions:
            namespace_name:
                description:
                    - The Object Storage namespace.
                type: str
                required: true
            bucket_name:
                description:
                    - The Object Storage bucket name.
                type: str
                required: true
            prefix:
                description:
                    - The Object Storage folder name.
                type: str
                required: true
    compartment_id:
        description:
            - The compartment identifier.
        type: str
        required: true
    display_name:
        description:
            - The display name of the processor job.
        type: str
        aliases: ["name"]
    processor_config:
        description:
            - ""
        type: dict
        required: true
        suboptions:
            processor_type:
                description:
                    - The type of the processor.
                type: str
                choices:
                    - "GENERAL"
                required: true
            document_type:
                description:
                    - The document type.
                type: str
                choices:
                    - "INVOICE"
                    - "RECEIPT"
                    - "RESUME"
                    - "TAX_FORM"
                    - "DRIVER_LICENSE"
                    - "PASSPORT"
                    - "BANK_STATEMENT"
                    - "CHECK"
                    - "PAYSLIP"
                    - "OTHERS"
            features:
                description:
                    - The types of document analysis requested.
                type: list
                elements: dict
                required: true
                suboptions:
                    model_id:
                        description:
                            - The custom model ID.
                            - Applicable when feature_type is one of ['KEY_VALUE_EXTRACTION', 'DOCUMENT_CLASSIFICATION']
                        type: str
                    tenancy_id:
                        description:
                            - The custom model tenancy ID when modelId represents aliasName.
                            - Applicable when feature_type is one of ['KEY_VALUE_EXTRACTION', 'DOCUMENT_CLASSIFICATION']
                        type: str
                    max_results:
                        description:
                            - The maximum number of results to return.
                            - Applicable when feature_type is one of ['DOCUMENT_CLASSIFICATION', 'LANGUAGE_CLASSIFICATION']
                        type: int
                    generate_searchable_pdf:
                        description:
                            - Whether or not to generate a searchable PDF file.
                            - Applicable when feature_type is 'TEXT_EXTRACTION'
                        type: bool
                    feature_type:
                        description:
                            - "The type of document analysis requested.
                              The allowed values are:
                              - `LANGUAGE_CLASSIFICATION`: Detect the language.
                              - `TEXT_EXTRACTION`: Recognize text.
                              - `TABLE_EXTRACTION`: Detect and extract data in tables.
                              - `KEY_VALUE_EXTRACTION`: Extract form fields.
                              - `DOCUMENT_CLASSIFICATION`: Identify the type of document."
                        type: str
                        choices:
                            - "DOCUMENT_CLASSIFICATION"
                            - "KEY_VALUE_EXTRACTION"
                            - "LANGUAGE_CLASSIFICATION"
                            - "TEXT_EXTRACTION"
                            - "TABLE_EXTRACTION"
                        required: true
            is_zip_output_enabled:
                description:
                    - Whether or not to generate a ZIP file containing the results.
                type: bool
            language:
                description:
                    - The document language, abbreviated according to the BCP 47 Language-Tag syntax.
                type: str
    state:
        description:
            - The state of the ProcessorJob.
            - Use I(state=present) to create a ProcessorJob.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create processor_job
  oci_ai_document_processor_job:
    # required
    input_location:
      # required
      data: data_example
      source_type: INLINE_DOCUMENT_CONTENT
    output_location:
      # required
      namespace_name: namespace_name_example
      bucket_name: bucket_name_example
      prefix: prefix_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    processor_config:
      # required
      processor_type: GENERAL
      features:
      - # required
        feature_type: DOCUMENT_CLASSIFICATION

        # optional
        model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
        tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        max_results: 56

        # optional
      document_type: INVOICE
      is_zip_output_enabled: true
      language: language_example

    # optional
    display_name: display_name_example

"""

RETURN = """
processor_job:
    description:
        - Details of the ProcessorJob resource acted upon by the current operation
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
                        model_id:
                            description:
                                - The custom model ID.
                            returned: on success
                            type: str
                            sample: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
                        tenancy_id:
                            description:
                                - The custom model tenancy ID when modelId represents aliasName.
                            returned: on success
                            type: str
                            sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
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
                "model_id": "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx",
                "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
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
    from oci.ai_document import AIServiceDocumentClient
    from oci.ai_document.models import CreateProcessorJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiDocumentProcessorJobHelperGen(OCIResourceHelperBase):
    """Supported operations: create and get"""

    def get_possible_entity_types(self):
        return super(
            AiDocumentProcessorJobHelperGen, self
        ).get_possible_entity_types() + [
            "processorjob",
            "processorjobs",
            "aiDocumentprocessorjob",
            "aiDocumentprocessorjobs",
            "processorjobresource",
            "processorjobsresource",
            "aidocument",
        ]

    def get_get_fn(self):
        return self.client.get_processor_job

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_processor_job,
            processor_job_id=self.module.params.get("processor_job_id"),
        )

    def get_create_model_class(self):
        return CreateProcessorJobDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_processor_job,
            call_fn_args=(),
            call_fn_kwargs=dict(create_processor_job_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


AiDocumentProcessorJobHelperCustom = get_custom_class(
    "AiDocumentProcessorJobHelperCustom"
)


class ResourceHelper(
    AiDocumentProcessorJobHelperCustom, AiDocumentProcessorJobHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            input_location=dict(
                type="dict",
                required=True,
                options=dict(
                    data=dict(type="str"),
                    source_type=dict(
                        type="str",
                        required=True,
                        choices=["INLINE_DOCUMENT_CONTENT", "OBJECT_STORAGE_LOCATIONS"],
                    ),
                    object_locations=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            namespace_name=dict(type="str", required=True),
                            bucket_name=dict(type="str", required=True),
                            object_name=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            output_location=dict(
                type="dict",
                required=True,
                options=dict(
                    namespace_name=dict(type="str", required=True),
                    bucket_name=dict(type="str", required=True),
                    prefix=dict(type="str", required=True),
                ),
            ),
            compartment_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            processor_config=dict(
                type="dict",
                required=True,
                options=dict(
                    processor_type=dict(type="str", required=True, choices=["GENERAL"]),
                    document_type=dict(
                        type="str",
                        choices=[
                            "INVOICE",
                            "RECEIPT",
                            "RESUME",
                            "TAX_FORM",
                            "DRIVER_LICENSE",
                            "PASSPORT",
                            "BANK_STATEMENT",
                            "CHECK",
                            "PAYSLIP",
                            "OTHERS",
                        ],
                    ),
                    features=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            model_id=dict(type="str"),
                            tenancy_id=dict(type="str"),
                            max_results=dict(type="int"),
                            generate_searchable_pdf=dict(type="bool"),
                            feature_type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "DOCUMENT_CLASSIFICATION",
                                    "KEY_VALUE_EXTRACTION",
                                    "LANGUAGE_CLASSIFICATION",
                                    "TEXT_EXTRACTION",
                                    "TABLE_EXTRACTION",
                                ],
                            ),
                        ),
                    ),
                    is_zip_output_enabled=dict(type="bool"),
                    language=dict(type="str"),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="processor_job",
        service_client_class=AIServiceDocumentClient,
        namespace="ai_document",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
