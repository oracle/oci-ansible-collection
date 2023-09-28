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
module: oci_data_labeling_service_dataset_actions
short_description: Perform actions on a Dataset resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Dataset resource in Oracle Cloud Infrastructure
    - For I(action=add_dataset_labels), add Labels to the Dataset LabelSet until the maximum number of Labels has been reached.
    - For I(action=change_compartment), moves a Dataset resource from one compartment identifier to another. When provided, If-Match is checked against ETag
      values of the resource.
    - For I(action=generate_dataset_records), generates Record resources from the Dataset's data source
    - For I(action=import_pre_annotated_data), imports records and annotations from dataset files into existing Dataset.
    - For I(action=remove_dataset_labels), removes the labels from the Dataset Labelset.  Labels can only be removed if there are no Annotations associated with
      the Dataset that reference the Label names.
    - For I(action=rename_dataset_labels), renames the labels from the Dataset Labelset.  Labels that are renamed will be reflected in Annotations associated
      with the Dataset that reference the Label names.
    - For I(action=snapshot), writes the dataset records and annotations in a consolidated format out to an object storage reference for consumption.
      While the snapshot takes place, there may be a time while records and annotations cannot be created to ensure the snapshot is a point in time.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment where the resource should be moved.
            - Required for I(action=change_compartment).
        type: str
    limit:
        description:
            - the maximum number of records to generate.
            - Applicable only for I(action=generate_dataset_records).
        type: float
    import_format:
        description:
            - ""
            - Applicable only for I(action=import_pre_annotated_data).
        type: dict
        suboptions:
            name:
                description:
                    - Name of import format
                type: str
                choices:
                    - "JSONL_CONSOLIDATED"
                    - "JSONL_COMPACT_PLUS_CONTENT"
                    - "CONLL"
                    - "SPACY"
                    - "COCO"
                    - "YOLO"
                    - "PASCAL_VOC"
                required: true
            version:
                description:
                    - Version of import format
                type: str
                choices:
                    - "V2003"
                    - "V5"
    import_metadata_path:
        description:
            - ""
            - Applicable only for I(action=import_pre_annotated_data).
        type: dict
        suboptions:
            source_type:
                description:
                    - "The type of data source.
                      OBJECT_STORAGE - The source details for an object storage bucket."
                type: str
                choices:
                    - "OBJECT_STORAGE"
                required: true
            namespace:
                description:
                    - Bucket namespace name
                type: str
                required: true
            bucket:
                description:
                    - Bucket name
                type: str
                required: true
            path:
                description:
                    - Path for the metadata file.
                type: str
                required: true
    label_set:
        description:
            - ""
            - Applicable only for I(action=add_dataset_labels)I(action=remove_dataset_labels).
        type: dict
        suboptions:
            items:
                description:
                    - An ordered collection of labels that are unique by name.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - An unique name for a label within its dataset.
                        type: str
    source_label_set:
        description:
            - ""
            - Applicable only for I(action=rename_dataset_labels).
        type: dict
        suboptions:
            items:
                description:
                    - An ordered collection of labels that are unique by name.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - An unique name for a label within its dataset.
                        type: str
    target_label_set:
        description:
            - ""
            - Applicable only for I(action=rename_dataset_labels).
        type: dict
        suboptions:
            items:
                description:
                    - An ordered collection of labels that are unique by name.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - An unique name for a label within its dataset.
                        type: str
    dataset_id:
        description:
            - Unique Dataset OCID
        type: str
        aliases: ["id"]
        required: true
    are_annotations_included:
        description:
            - Whether annotations are to be included in the export dataset digest.
            - Required for I(action=snapshot).
        type: bool
    are_unannotated_records_included:
        description:
            - Whether to include records that have yet to be annotated in the export dataset digest.
            - Required for I(action=snapshot).
        type: bool
    export_details:
        description:
            - ""
            - Required for I(action=snapshot).
        type: dict
        suboptions:
            export_type:
                description:
                    - The target destination for the snapshot.  Using OBJECT_STORAGE means the snapshot will be written to Object Storage.
                type: str
                choices:
                    - "OBJECT_STORAGE"
                required: true
            namespace:
                description:
                    - Bucket namespace name
                type: str
                required: true
            bucket:
                description:
                    - Bucket name
                type: str
                required: true
            prefix:
                description:
                    - Object path prefix to put snapshot file(s)
                type: str
    export_format:
        description:
            - ""
            - Applicable only for I(action=snapshot).
        type: dict
        suboptions:
            name:
                description:
                    - Name of export format.
                type: str
                choices:
                    - "JSONL"
                    - "JSONL_CONSOLIDATED"
                    - "CONLL"
                    - "SPACY"
                    - "COCO"
                    - "YOLO"
                    - "PASCAL_VOC"
                    - "JSONL_COMPACT_PLUS_CONTENT"
            version:
                description:
                    - Version of export format.
                type: str
                choices:
                    - "V2003"
                    - "V5"
    action:
        description:
            - The action to perform on the Dataset.
        type: str
        required: true
        choices:
            - "add_dataset_labels"
            - "change_compartment"
            - "generate_dataset_records"
            - "import_pre_annotated_data"
            - "remove_dataset_labels"
            - "rename_dataset_labels"
            - "snapshot"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_dataset_labels on dataset
  oci_data_labeling_service_dataset_actions:
    # required
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
    action: add_dataset_labels

    # optional
    label_set:
      # optional
      items:
      - # optional
        name: name_example

- name: Perform action change_compartment on dataset
  oci_data_labeling_service_dataset_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action generate_dataset_records on dataset
  oci_data_labeling_service_dataset_actions:
    # required
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
    action: generate_dataset_records

    # optional
    limit: 3.4

- name: Perform action import_pre_annotated_data on dataset
  oci_data_labeling_service_dataset_actions:
    # required
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
    action: import_pre_annotated_data

    # optional
    import_format:
      # required
      name: JSONL_CONSOLIDATED

      # optional
      version: V2003
    import_metadata_path:
      # required
      source_type: OBJECT_STORAGE
      namespace: namespace_example
      bucket: bucket_example
      path: path_example

- name: Perform action remove_dataset_labels on dataset
  oci_data_labeling_service_dataset_actions:
    # required
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_dataset_labels

    # optional
    label_set:
      # optional
      items:
      - # optional
        name: name_example

- name: Perform action rename_dataset_labels on dataset
  oci_data_labeling_service_dataset_actions:
    # required
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
    action: rename_dataset_labels

    # optional
    source_label_set:
      # optional
      items:
      - # optional
        name: name_example
    target_label_set:
      # optional
      items:
      - # optional
        name: name_example

- name: Perform action snapshot on dataset
  oci_data_labeling_service_dataset_actions:
    # required
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
    are_annotations_included: true
    are_unannotated_records_included: true
    export_details:
      # required
      export_type: OBJECT_STORAGE
      namespace: namespace_example
      bucket: bucket_example

      # optional
      prefix: prefix_example
    action: snapshot

    # optional
    export_format:
      # optional
      name: JSONL
      version: V2003

"""

RETURN = """
dataset:
    description:
        - Details of the Dataset resource acted upon by the current operation
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
    from oci.data_labeling_service import DataLabelingManagementClient
    from oci.data_labeling_service.models import AddDatasetLabelsDetails
    from oci.data_labeling_service.models import ChangeDatasetCompartmentDetails
    from oci.data_labeling_service.models import GenerateDatasetRecordsDetails
    from oci.data_labeling_service.models import ImportPreAnnotatedDataDetails
    from oci.data_labeling_service.models import RemoveDatasetLabelsDetails
    from oci.data_labeling_service.models import RenameDatasetLabelsDetails
    from oci.data_labeling_service.models import SnapshotDatasetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatasetActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_dataset_labels
        change_compartment
        generate_dataset_records
        import_pre_annotated_data
        remove_dataset_labels
        rename_dataset_labels
        snapshot
    """

    @staticmethod
    def get_module_resource_id_param():
        return "dataset_id"

    def get_module_resource_id(self):
        return self.module.params.get("dataset_id")

    def get_get_fn(self):
        return self.client.get_dataset

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dataset, dataset_id=self.module.params.get("dataset_id"),
        )

    def add_dataset_labels(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddDatasetLabelsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_dataset_labels,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dataset_id=self.module.params.get("dataset_id"),
                add_dataset_labels_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDatasetCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_dataset_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dataset_id=self.module.params.get("dataset_id"),
                change_dataset_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def generate_dataset_records(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, GenerateDatasetRecordsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.generate_dataset_records,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dataset_id=self.module.params.get("dataset_id"),
                generate_dataset_records_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def import_pre_annotated_data(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ImportPreAnnotatedDataDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.import_pre_annotated_data,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dataset_id=self.module.params.get("dataset_id"),
                import_pre_annotated_data_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def remove_dataset_labels(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveDatasetLabelsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_dataset_labels,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dataset_id=self.module.params.get("dataset_id"),
                remove_dataset_labels_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def rename_dataset_labels(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RenameDatasetLabelsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.rename_dataset_labels,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dataset_id=self.module.params.get("dataset_id"),
                rename_dataset_labels_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def snapshot(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SnapshotDatasetDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.snapshot_dataset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dataset_id=self.module.params.get("dataset_id"),
                snapshot_dataset_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DatasetActionsHelperCustom = get_custom_class("DatasetActionsHelperCustom")


class ResourceHelper(DatasetActionsHelperCustom, DatasetActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            limit=dict(type="float"),
            import_format=dict(
                type="dict",
                options=dict(
                    name=dict(
                        type="str",
                        required=True,
                        choices=[
                            "JSONL_CONSOLIDATED",
                            "JSONL_COMPACT_PLUS_CONTENT",
                            "CONLL",
                            "SPACY",
                            "COCO",
                            "YOLO",
                            "PASCAL_VOC",
                        ],
                    ),
                    version=dict(type="str", choices=["V2003", "V5"]),
                ),
            ),
            import_metadata_path=dict(
                type="dict",
                options=dict(
                    source_type=dict(
                        type="str", required=True, choices=["OBJECT_STORAGE"]
                    ),
                    namespace=dict(type="str", required=True),
                    bucket=dict(type="str", required=True),
                    path=dict(type="str", required=True),
                ),
            ),
            label_set=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        options=dict(name=dict(type="str")),
                    )
                ),
            ),
            source_label_set=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        options=dict(name=dict(type="str")),
                    )
                ),
            ),
            target_label_set=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        options=dict(name=dict(type="str")),
                    )
                ),
            ),
            dataset_id=dict(aliases=["id"], type="str", required=True),
            are_annotations_included=dict(type="bool"),
            are_unannotated_records_included=dict(type="bool"),
            export_details=dict(
                type="dict",
                options=dict(
                    export_type=dict(
                        type="str", required=True, choices=["OBJECT_STORAGE"]
                    ),
                    namespace=dict(type="str", required=True),
                    bucket=dict(type="str", required=True),
                    prefix=dict(type="str"),
                ),
            ),
            export_format=dict(
                type="dict",
                options=dict(
                    name=dict(
                        type="str",
                        choices=[
                            "JSONL",
                            "JSONL_CONSOLIDATED",
                            "CONLL",
                            "SPACY",
                            "COCO",
                            "YOLO",
                            "PASCAL_VOC",
                            "JSONL_COMPACT_PLUS_CONTENT",
                        ],
                    ),
                    version=dict(type="str", choices=["V2003", "V5"]),
                ),
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_dataset_labels",
                    "change_compartment",
                    "generate_dataset_records",
                    "import_pre_annotated_data",
                    "remove_dataset_labels",
                    "rename_dataset_labels",
                    "snapshot",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="dataset",
        service_client_class=DataLabelingManagementClient,
        namespace="data_labeling_service",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
