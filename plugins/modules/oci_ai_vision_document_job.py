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
module: oci_ai_vision_document_job
short_description: Manage a DocumentJob resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a DocumentJob resource in Oracle Cloud Infrastructure
    - For I(state=present), create a batch document analysis job
    - "This resource has the following action operations in the M(oracle.oci.oci_ai_vision_document_job_actions) module: cancel."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    input_location:
        description:
            - ""
        type: dict
        required: true
        suboptions:
            source_type:
                description:
                    - "The type of input location
                      Allowed values are:
                      - `OBJECT_LIST_INLINE_INPUT_LOCATION`: A list of object locations in Object Storage."
                type: str
                choices:
                    - "OBJECT_LIST_INLINE_INPUT_LOCATION"
                required: true
            object_locations:
                description:
                    - List of ObjectLocations.
                type: list
                elements: dict
                required: true
                suboptions:
                    namespace_name:
                        description:
                            - Object Storage namespace name.
                        type: str
                        required: true
                    bucket_name:
                        description:
                            - Object Storage bucket name.
                        type: str
                        required: true
                    object_name:
                        description:
                            - Object Storage object name.
                        type: str
                        required: true
    features:
        description:
            - List of document analysis types requested.
        type: list
        elements: dict
        required: true
        suboptions:
            feature_type:
                description:
                    - "Type of document analysis requested
                      Allowed values are:
                      - `LANGUAGE_CLASSIFICATION`: Detect the language.
                      - `TEXT_DETECTION`: Recognize text.
                      - `TABLE_DETECTION`: Detect and extract data in tables.
                      - `KEY_VALUE_DETECTION`: Extract form fields.
                      - `DOCUMENT_CLASSIFICATION`: Identify the type of document."
                type: str
                choices:
                    - "TABLE_DETECTION"
                    - "KEY_VALUE_DETECTION"
                    - "DOCUMENT_CLASSIFICATION"
                    - "TEXT_DETECTION"
                    - "LANGUAGE_CLASSIFICATION"
                required: true
            max_results:
                description:
                    - The maximum number of results to return.
                    - Applicable when feature_type is one of ['DOCUMENT_CLASSIFICATION', 'LANGUAGE_CLASSIFICATION']
                type: int
            model_id:
                description:
                    - Custom model id.
                    - Applicable when feature_type is 'DOCUMENT_CLASSIFICATION'
                type: str
            generate_searchable_pdf:
                description:
                    - Whether to generate a searchable PDF file.
                    - Applicable when feature_type is 'TEXT_DETECTION'
                type: bool
    output_location:
        description:
            - ""
        type: dict
        required: true
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
    compartment_id:
        description:
            - Compartment identifier from the requester.
        type: str
    display_name:
        description:
            - Document job display name.
        type: str
        aliases: ["name"]
    language:
        description:
            - Language of the document, abbreviated according to ISO 639-2.
        type: str
        choices:
            - "ENG"
            - "CES"
            - "DAN"
            - "NLD"
            - "FIN"
            - "FRA"
            - "DEU"
            - "ELL"
            - "HUN"
            - "ITA"
            - "NOR"
            - "POL"
            - "POR"
            - "RON"
            - "RUS"
            - "SLK"
            - "SPA"
            - "SWE"
            - "TUR"
            - "ARA"
            - "CHI_SIM"
            - "HIN"
            - "JPN"
            - "KOR"
            - "OTHERS"
    document_type:
        description:
            - The type of documents.
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
    is_zip_output_enabled:
        description:
            - Whether to generate a Zip file containing the results.
        type: bool
    state:
        description:
            - The state of the DocumentJob.
            - Use I(state=present) to create a DocumentJob.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create document_job
  oci_ai_vision_document_job:
    # required
    input_location:
      # required
      source_type: OBJECT_LIST_INLINE_INPUT_LOCATION
      object_locations:
      - # required
        namespace_name: namespace_name_example
        bucket_name: bucket_name_example
        object_name: object_name_example
    features:
    - # required
      feature_type: TABLE_DETECTION
    output_location:
      # required
      namespace_name: namespace_name_example
      bucket_name: bucket_name_example
      prefix: prefix_example

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    language: ENG
    document_type: INVOICE
    is_zip_output_enabled: true

"""

RETURN = """
document_job:
    description:
        - Details of the DocumentJob resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Job id.
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
                - Document job display name.
            returned: on success
            type: str
            sample: display_name_example
        features:
            description:
                - List of document analysis types requested.
            returned: on success
            type: complex
            contains:
                model_id:
                    description:
                        - Custom model id.
                    returned: on success
                    type: str
                    sample: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
                max_results:
                    description:
                        - The maximum number of results to return.
                    returned: on success
                    type: int
                    sample: 56
                feature_type:
                    description:
                        - "Type of document analysis requested
                          Allowed values are:
                          - `LANGUAGE_CLASSIFICATION`: Detect the language.
                          - `TEXT_DETECTION`: Recognize text.
                          - `TABLE_DETECTION`: Detect and extract data in tables.
                          - `KEY_VALUE_DETECTION`: Extract form fields.
                          - `DOCUMENT_CLASSIFICATION`: Identify the type of document."
                    returned: on success
                    type: str
                    sample: LANGUAGE_CLASSIFICATION
                generate_searchable_pdf:
                    description:
                        - Whether to generate a searchable PDF file.
                    returned: on success
                    type: bool
                    sample: true
        language:
            description:
                - Language of the document, abbreviated according to ISO 639-2.
            returned: on success
            type: str
            sample: ENG
        document_type:
            description:
                - The type of documents.
            returned: on success
            type: str
            sample: INVOICE
        input_location:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                source_type:
                    description:
                        - "The type of input location
                          Allowed values are:
                          - `OBJECT_LIST_INLINE_INPUT_LOCATION`: A list of object locations in Object Storage."
                    returned: on success
                    type: str
                    sample: OBJECT_LIST_INLINE_INPUT_LOCATION
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
        percent_complete:
            description:
                - How much progress the operation has made, vs the total amount of work that must be performed.
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
        lifecycle_state:
            description:
                - The current state of the batch document job.
            returned: on success
            type: str
            sample: SUCCEEDED
        is_zip_output_enabled:
            description:
                - Whether to generate a Zip file containing the results.
            returned: on success
            type: bool
            sample: true
        lifecycle_details:
            description:
                - Detailed status of FAILED state.
            returned: on success
            type: str
            sample: PARTIALLY_SUCCEEDED
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "features": [{
            "model_id": "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx",
            "max_results": 56,
            "feature_type": "LANGUAGE_CLASSIFICATION",
            "generate_searchable_pdf": true
        }],
        "language": "ENG",
        "document_type": "INVOICE",
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
        "is_zip_output_enabled": true,
        "lifecycle_details": "PARTIALLY_SUCCEEDED"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.ai_vision import AIServiceVisionClient
    from oci.ai_vision.models import CreateDocumentJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiVisionDocumentJobHelperGen(OCIResourceHelperBase):
    """Supported operations: create and get"""

    def get_possible_entity_types(self):
        return super(AiVisionDocumentJobHelperGen, self).get_possible_entity_types() + [
            "documentjob",
            "documentjobs",
            "aiVisiondocumentjob",
            "aiVisiondocumentjobs",
            "documentjobresource",
            "documentjobsresource",
            "aivision",
        ]

    def get_get_fn(self):
        return self.client.get_document_job

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_document_job,
            document_job_id=self.module.params.get("document_job_id"),
        )

    def get_create_model_class(self):
        return CreateDocumentJobDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_document_job,
            call_fn_args=(),
            call_fn_kwargs=dict(create_document_job_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


AiVisionDocumentJobHelperCustom = get_custom_class("AiVisionDocumentJobHelperCustom")


class ResourceHelper(AiVisionDocumentJobHelperCustom, AiVisionDocumentJobHelperGen):
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
                    source_type=dict(
                        type="str",
                        required=True,
                        choices=["OBJECT_LIST_INLINE_INPUT_LOCATION"],
                    ),
                    object_locations=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            namespace_name=dict(type="str", required=True),
                            bucket_name=dict(type="str", required=True),
                            object_name=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            features=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    feature_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "TABLE_DETECTION",
                            "KEY_VALUE_DETECTION",
                            "DOCUMENT_CLASSIFICATION",
                            "TEXT_DETECTION",
                            "LANGUAGE_CLASSIFICATION",
                        ],
                    ),
                    max_results=dict(type="int"),
                    model_id=dict(type="str"),
                    generate_searchable_pdf=dict(type="bool"),
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
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            language=dict(
                type="str",
                choices=[
                    "ENG",
                    "CES",
                    "DAN",
                    "NLD",
                    "FIN",
                    "FRA",
                    "DEU",
                    "ELL",
                    "HUN",
                    "ITA",
                    "NOR",
                    "POL",
                    "POR",
                    "RON",
                    "RUS",
                    "SLK",
                    "SPA",
                    "SWE",
                    "TUR",
                    "ARA",
                    "CHI_SIM",
                    "HIN",
                    "JPN",
                    "KOR",
                    "OTHERS",
                ],
            ),
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
            is_zip_output_enabled=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="document_job",
        service_client_class=AIServiceVisionClient,
        namespace="ai_vision",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
