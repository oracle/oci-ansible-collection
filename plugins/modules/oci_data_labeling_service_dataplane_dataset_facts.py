#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_data_labeling_service_dataplane_dataset_facts
short_description: Fetches details about a Dataset resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Dataset resource in Oracle Cloud Infrastructure
    - Gets a dataset by identifier.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dataset_id:
        description:
            - A unique dataset OCID.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific dataset
  oci_data_labeling_service_dataplane_dataset_facts:
    # required
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
dataset:
    description:
        - Dataset resource
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the Dataset.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the resource.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment of the resource.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - A user provided description of the dataset
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The date and time the resource was created, in the timestamp format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the resource was last updated, in the timestamp format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - "The state of a dataset.
                  CREATING - The dataset is being created.  It will transition to ACTIVE when it is ready for labeling.
                  ACTIVE   - The dataset is ready for labeling.
                  UPDATING - The dataset is being updated.  It and its related resources may be unavailable for other updates until it returns to ACTIVE.
                  NEEDS_ATTENTION - A dataset updation operation has failed due to validation or other errors and needs attention.
                  DELETING - The dataset and its related resources are being deleted.
                  DELETED  - The dataset has been deleted and is no longer available.
                  FAILED   - The dataset has failed due to validation or other errors."
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in FAILED
                  or NEEDS_ATTENTION state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_substate:
            description:
                - "The sub-state of the dataset.
                  IMPORT_DATASET - The dataset is being imported."
            returned: on success
            type: str
            sample: IMPORT_DATASET
        annotation_format:
            description:
                - The annotation format name required for labeling records.
            returned: on success
            type: str
            sample: annotation_format_example
        dataset_source_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                source_type:
                    description:
                        - The source type. OBJECT_STORAGE allows the user to describe where in object storage the dataset is.
                    returned: on success
                    type: str
                    sample: OBJECT_STORAGE
                namespace:
                    description:
                        - The namespace of the bucket that contains the dataset data source.
                    returned: on success
                    type: str
                    sample: namespace_example
                bucket:
                    description:
                        - The object storage bucket that contains the dataset data source.
                    returned: on success
                    type: str
                    sample: bucket_example
                prefix:
                    description:
                        - A common path prefix shared by the objects that make up the dataset. Except for the CSV file type, records are not generated for the
                          objects whose names exactly match with the prefix.
                    returned: on success
                    type: str
                    sample: prefix_example
        dataset_format_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                format_type:
                    description:
                        - The format type. DOCUMENT format is for record contents that are PDFs or TIFFs. IMAGE format is for record contents that are JPEGs or
                          PNGs. TEXT format is for record contents that are TXT files.
                    returned: on success
                    type: str
                    sample: DOCUMENT
                text_file_type_metadata:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        format_type:
                            description:
                                - It defines the format type of text files.
                            returned: on success
                            type: str
                            sample: DELIMITED
                        column_name:
                            description:
                                - The name of a selected column.
                            returned: on success
                            type: str
                            sample: column_name_example
                        column_index:
                            description:
                                - The index of a selected column. This is a zero-based index.
                            returned: on success
                            type: int
                            sample: 56
                        column_delimiter:
                            description:
                                - A column delimiter
                            returned: on success
                            type: str
                            sample: column_delimiter_example
                        line_delimiter:
                            description:
                                - A line delimiter.
                            returned: on success
                            type: str
                            sample: line_delimiter_example
                        escape_character:
                            description:
                                - An escape character.
                            returned: on success
                            type: str
                            sample: escape_character_example
        label_set:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - An ordered collection of labels that are unique by name.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - An unique name for a label within its dataset.
                            returned: on success
                            type: str
                            sample: name_example
        initial_record_generation_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                limit:
                    description:
                        - The maximum number of records to generate.
                    returned: on success
                    type: float
                    sample: 10
        initial_import_dataset_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                import_format:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of import format
                            returned: on success
                            type: str
                            sample: JSONL_CONSOLIDATED
                        version:
                            description:
                                - Version of import format
                            returned: on success
                            type: str
                            sample: V2003
                import_metadata_path:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        source_type:
                            description:
                                - "The type of data source.
                                  OBJECT_STORAGE - The source details for an object storage bucket."
                            returned: on success
                            type: str
                            sample: OBJECT_STORAGE
                        namespace:
                            description:
                                - Bucket namespace name
                            returned: on success
                            type: str
                            sample: namespace_example
                        bucket:
                            description:
                                - Bucket name
                            returned: on success
                            type: str
                            sample: bucket_example
                        path:
                            description:
                                - Path for the metadata file.
                            returned: on success
                            type: str
                            sample: path_example
        labeling_instructions:
            description:
                - The labeling instructions for human labelers in rich text format
            returned: on success
            type: str
            sample: labeling_instructions_example
        freeform_tags:
            description:
                - "A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
                  For example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "The defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "The usage of system tag keys. These predefined keys are scoped to namespaces.
                  For example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        additional_properties:
            description:
                - "A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
                  For example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_substate": "IMPORT_DATASET",
        "annotation_format": "annotation_format_example",
        "dataset_source_details": {
            "source_type": "OBJECT_STORAGE",
            "namespace": "namespace_example",
            "bucket": "bucket_example",
            "prefix": "prefix_example"
        },
        "dataset_format_details": {
            "format_type": "DOCUMENT",
            "text_file_type_metadata": {
                "format_type": "DELIMITED",
                "column_name": "column_name_example",
                "column_index": 56,
                "column_delimiter": "column_delimiter_example",
                "line_delimiter": "line_delimiter_example",
                "escape_character": "escape_character_example"
            }
        },
        "label_set": {
            "items": [{
                "name": "name_example"
            }]
        },
        "initial_record_generation_configuration": {
            "limit": 10
        },
        "initial_import_dataset_configuration": {
            "import_format": {
                "name": "JSONL_CONSOLIDATED",
                "version": "V2003"
            },
            "import_metadata_path": {
                "source_type": "OBJECT_STORAGE",
                "namespace": "namespace_example",
                "bucket": "bucket_example",
                "path": "path_example"
            }
        },
        "labeling_instructions": "labeling_instructions_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "additional_properties": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_labeling_service_dataplane import DataLabelingClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatasetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "dataset_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dataset, dataset_id=self.module.params.get("dataset_id"),
        )


DatasetFactsHelperCustom = get_custom_class("DatasetFactsHelperCustom")


class ResourceFactsHelper(DatasetFactsHelperCustom, DatasetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dataset_id=dict(aliases=["id"], type="str", required=True),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="dataset",
        service_client_class=DataLabelingClient,
        namespace="data_labeling_service_dataplane",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(dataset=result)


if __name__ == "__main__":
    main()
