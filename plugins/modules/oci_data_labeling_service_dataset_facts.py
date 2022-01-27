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
module: oci_data_labeling_service_dataset_facts
short_description: Fetches details about one or multiple Dataset resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Dataset resources in Oracle Cloud Infrastructure
    - Returns a list of Datasets.
    - If I(dataset_id) is specified, the details of a single Dataset will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dataset_id:
        description:
            - Unique Dataset OCID
            - Required to get a specific dataset.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple datasets.
        type: str
    annotation_format:
        description:
            - A filter to return only resources that match the entire annotation format given.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources whose lifecycleState matches this query param.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "NEEDS_ATTENTION"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific dataset
  oci_data_labeling_service_dataset_facts:
    # required
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"

- name: List datasets
  oci_data_labeling_service_dataset_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    annotation_format: annotation_format_example
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
datasets:
    description:
        - List of Dataset resources
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
                - Returned for get operation
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
        annotation_format:
            description:
                - The annotation format name required for labeling records.
            returned: on success
            type: str
            sample: annotation_format_example
        dataset_source_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                source_type:
                    description:
                        - Source type.  OBJECT_STORAGE allows the customer to describe where the dataset is in object storage.
                    returned: on success
                    type: str
                    sample: OBJECT_STORAGE
                namespace:
                    description:
                        - Namespace of the bucket that contains the dataset data source
                    returned: on success
                    type: str
                    sample: namespace_example
                bucket:
                    description:
                        - The object storage bucket that contains the dataset data source
                    returned: on success
                    type: str
                    sample: bucket_example
                prefix:
                    description:
                        - A common path prefix shared by the objects that make up the dataset. Records will not be generated for objects whose name match
                          exactly with prefix.
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
                        - Format type. DOCUMENT format is for record contents that are PDFs or TIFFs. IMAGE format is for record contents that are JPEGs or
                          PNGs. TEXT format is for record contents that are txt files.
                    returned: on success
                    type: str
                    sample: DOCUMENT
        label_set:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - An ordered collection of Labels that are unique by name.
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
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                limit:
                    description:
                        - the maximum number of records to generate.
                    returned: on success
                    type: float
                    sample: 10
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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "annotation_format": "annotation_format_example",
        "dataset_source_details": {
            "source_type": "OBJECT_STORAGE",
            "namespace": "namespace_example",
            "bucket": "bucket_example",
            "prefix": "prefix_example"
        },
        "dataset_format_details": {
            "format_type": "DOCUMENT"
        },
        "label_set": {
            "items": [{
                "name": "name_example"
            }]
        },
        "initial_record_generation_configuration": {
            "limit": 10
        },
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
    from oci.data_labeling_service import DataLabelingManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatasetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "dataset_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dataset, dataset_id=self.module.params.get("dataset_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "annotation_format",
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
            self.client.list_datasets,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DatasetFactsHelperCustom = get_custom_class("DatasetFactsHelperCustom")


class ResourceFactsHelper(DatasetFactsHelperCustom, DatasetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dataset_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            annotation_format=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "NEEDS_ATTENTION",
                    "DELETING",
                    "DELETED",
                    "FAILED",
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
        resource_type="dataset",
        service_client_class=DataLabelingManagementClient,
        namespace="data_labeling_service",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(datasets=result)


if __name__ == "__main__":
    main()
