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
module: oci_ai_vision_document_job_facts
short_description: Fetches details about a DocumentJob resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a DocumentJob resource in Oracle Cloud Infrastructure
    - Get details of a batch document job.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    document_job_id:
        description:
            - Document job id.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific document_job
  oci_ai_vision_document_job_facts:
    # required
    document_job_id: "ocid1.documentjob.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
document_job:
    description:
        - DocumentJob resource
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
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.ai_vision import AIServiceVisionClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiVisionDocumentJobFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "document_job_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_document_job,
            document_job_id=self.module.params.get("document_job_id"),
        )


AiVisionDocumentJobFactsHelperCustom = get_custom_class(
    "AiVisionDocumentJobFactsHelperCustom"
)


class ResourceFactsHelper(
    AiVisionDocumentJobFactsHelperCustom, AiVisionDocumentJobFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            document_job_id=dict(aliases=["id"], type="str", required=True),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="document_job",
        service_client_class=AIServiceVisionClient,
        namespace="ai_vision",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(document_job=result)


if __name__ == "__main__":
    main()
