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
module: oci_data_labeling_service_dataplane_record_facts
short_description: Fetches details about one or multiple Record resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Record resources in Oracle Cloud Infrastructure
    - The list of records in the specified compartment.
    - If I(record_id) is specified, the details of a single Record will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    record_id:
        description:
            - The OCID of the record annotated.
            - Required to get a specific record.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple records.
        type: str
    dataset_id:
        description:
            - Filter the results by the OCID of the dataset.
            - Required to list multiple records.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources whose lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "ACTIVE"
            - "INACTIVE"
            - "DELETED"
    name:
        description:
            - The name of the record.
        type: str
    is_labeled:
        description:
            - Whether the record has been labeled and has associated annotations.
        type: bool
    annotation_labels_contains:
        description:
            - Lets the user filter records based on the related annotations.
        type: list
        elements: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. The default order for timeCreated is descending. The default order for name is
              ascending. If no value is specified, timeCreated is used by default.
        type: str
        choices:
            - "timeCreated"
            - "name"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific record
  oci_data_labeling_service_dataplane_record_facts:
    # required
    record_id: "ocid1.record.oc1..xxxxxxEXAMPLExxxxxx"

- name: List records
  oci_data_labeling_service_dataplane_record_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: ACTIVE
    name: name_example
    is_labeled: true
    annotation_labels_contains: [ "annotation_labels_contains_example" ]
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
records:
    description:
        - List of Record resources
    returned: on success
    type: complex
    contains:
        source_details:
            description:
                - ""
                - Returned for get operation
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
                relative_path:
                    description:
                        - The path relative to the prefix specified in the dataset source details (file name).
                    returned: on success
                    type: str
                    sample: relative_path_example
                path:
                    description:
                        - The full path of the file this record belongs to.
                    returned: on success
                    type: str
                    sample: path_example
                offset:
                    description:
                        - The offset into the file containing the content.
                    returned: on success
                    type: float
                    sample: 10
                length:
                    description:
                        - The length from the offset into the file containing the content.
                    returned: on success
                    type: float
                    sample: 10
        record_metadata:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                height:
                    description:
                        - Height of the image record.
                    returned: on success
                    type: int
                    sample: 56
                width:
                    description:
                        - Width of the image record.
                    returned: on success
                    type: int
                    sample: 56
                depth:
                    description:
                        - Depth of the image record.
                    returned: on success
                    type: int
                    sample: 56
                record_type:
                    description:
                        - "The record type based on dataset format details.
                          IMAGE_METADATA  - Collection of metadata related to image record.
                          TEXT_METADATA - Collection of metadata related to text record.
                          DOCUMENT_METADATA - Collection of metadata related to document record."
                    returned: on success
                    type: str
                    sample: IMAGE_METADATA
        id:
            description:
                - The OCID of the record.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name is created by the user. It is unique and immutable.
            returned: on success
            type: str
            sample: name_example
        time_created:
            description:
                - The date and time the resource was created, in the timestamp format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the resource was updated, in the timestamp format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        dataset_id:
            description:
                - The OCID of the dataset to associate the record with.
            returned: on success
            type: str
            sample: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment for the task.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        is_labeled:
            description:
                - Whether or not the record has been labeled and has associated annotations.
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - "The lifecycle state of the record.
                  ACTIVE - The record is active and ready for labeling.
                  INACTIVE - The record has been marked as inactive and should not be used for labeling.
                  DELETED - The record has been deleted and is no longer available for labeling."
            returned: on success
            type: str
            sample: ACTIVE
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
    sample: [{
        "source_details": {
            "source_type": "OBJECT_STORAGE",
            "relative_path": "relative_path_example",
            "path": "path_example",
            "offset": 10,
            "length": 10
        },
        "record_metadata": {
            "height": 56,
            "width": 56,
            "depth": 56,
            "record_type": "IMAGE_METADATA"
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_labeled": true,
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
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


class RecordFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "record_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "dataset_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_record, record_id=self.module.params.get("record_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "name",
            "is_labeled",
            "annotation_labels_contains",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_records,
            compartment_id=self.module.params.get("compartment_id"),
            dataset_id=self.module.params.get("dataset_id"),
            **optional_kwargs
        )


RecordFactsHelperCustom = get_custom_class("RecordFactsHelperCustom")


class ResourceFactsHelper(RecordFactsHelperCustom, RecordFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            record_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            dataset_id=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "INACTIVE", "DELETED"]),
            name=dict(type="str"),
            is_labeled=dict(type="bool"),
            annotation_labels_contains=dict(type="list", elements="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "name"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="record",
        service_client_class=DataLabelingClient,
        namespace="data_labeling_service_dataplane",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(records=result)


if __name__ == "__main__":
    main()
