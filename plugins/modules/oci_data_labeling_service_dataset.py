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
module: oci_data_labeling_service_dataset
short_description: Manage a Dataset resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Dataset resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Dataset.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_labeling_service_dataset_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment of the resource.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    annotation_format:
        description:
            - The annotation format name required for labeling records.
            - Required for create using I(state=present).
        type: str
    dataset_source_details:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            source_type:
                description:
                    - Source type.  OBJECT_STORAGE allows the customer to describe where the dataset is in object storage.
                type: str
                choices:
                    - "OBJECT_STORAGE"
                required: true
            namespace:
                description:
                    - Namespace of the bucket that contains the dataset data source
                type: str
                required: true
            bucket:
                description:
                    - The object storage bucket that contains the dataset data source
                type: str
                required: true
            prefix:
                description:
                    - A common path prefix shared by the objects that make up the dataset. Records will not be generated for objects whose name match exactly
                      with prefix.
                type: str
    dataset_format_details:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            format_type:
                description:
                    - Format type. DOCUMENT format is for record contents that are PDFs or TIFFs. IMAGE format is for record contents that are JPEGs or PNGs.
                      TEXT format is for record contents that are txt files.
                type: str
                choices:
                    - "IMAGE"
                    - "DOCUMENT"
                    - "TEXT"
                required: true
    initial_record_generation_configuration:
        description:
            - ""
        type: dict
        suboptions:
            limit:
                description:
                    - the maximum number of records to generate.
                type: float
    label_set:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            items:
                description:
                    - An ordered collection of Labels that are unique by name.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - An unique name for a label within its dataset.
                        type: str
    display_name:
        description:
            - A user-friendly display name for the resource.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A user provided description of the dataset
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
              For example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "The defined tags for this resource. Each key is predefined and scoped to a namespace.
              For example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    dataset_id:
        description:
            - Unique Dataset OCID
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Dataset.
            - Use I(state=present) to create or update a Dataset.
            - Use I(state=absent) to delete a Dataset.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create dataset
  oci_data_labeling_service_dataset:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    annotation_format: annotation_format_example
    dataset_source_details:
      # required
      source_type: OBJECT_STORAGE
      namespace: namespace_example
      bucket: bucket_example

      # optional
      prefix: prefix_example
    dataset_format_details:
      # required
      format_type: IMAGE
    label_set:
      # optional
      items:
      - # optional
        name: name_example

    # optional
    initial_record_generation_configuration:
      # optional
      limit: 3.4
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update dataset
  oci_data_labeling_service_dataset:
    # required
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update dataset using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_labeling_service_dataset:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete dataset
  oci_data_labeling_service_dataset:
    # required
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete dataset using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_labeling_service_dataset:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    sample: {
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
    from oci.data_labeling_service import DataLabelingManagementClient
    from oci.data_labeling_service.models import CreateDatasetDetails
    from oci.data_labeling_service.models import UpdateDatasetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatasetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DatasetHelperGen, self).get_possible_entity_types() + [
            "datalabelingdataset",
            "datalabelingdatasets",
            "dataLabelingServicedatalabelingdataset",
            "dataLabelingServicedatalabelingdatasets",
            "datalabelingdatasetresource",
            "datalabelingdatasetsresource",
            "dataset",
            "datasets",
            "dataLabelingServicedataset",
            "dataLabelingServicedatasets",
            "datasetresource",
            "datasetsresource",
            "datalabelingservice",
        ]

    def get_module_resource_id_param(self):
        return "dataset_id"

    def get_module_resource_id(self):
        return self.module.params.get("dataset_id")

    def get_get_fn(self):
        return self.client.get_dataset

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_dataset, dataset_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dataset, dataset_id=self.module.params.get("dataset_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["annotation_format", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_datasets, **kwargs)

    def get_create_model_class(self):
        return CreateDatasetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_dataset,
            call_fn_args=(),
            call_fn_kwargs=dict(create_dataset_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDatasetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_dataset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dataset_id=self.module.params.get("dataset_id"),
                update_dataset_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_dataset,
            call_fn_args=(),
            call_fn_kwargs=dict(dataset_id=self.module.params.get("dataset_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DatasetHelperCustom = get_custom_class("DatasetHelperCustom")


class ResourceHelper(DatasetHelperCustom, DatasetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            annotation_format=dict(type="str"),
            dataset_source_details=dict(
                type="dict",
                options=dict(
                    source_type=dict(
                        type="str", required=True, choices=["OBJECT_STORAGE"]
                    ),
                    namespace=dict(type="str", required=True),
                    bucket=dict(type="str", required=True),
                    prefix=dict(type="str"),
                ),
            ),
            dataset_format_details=dict(
                type="dict",
                options=dict(
                    format_type=dict(
                        type="str", required=True, choices=["IMAGE", "DOCUMENT", "TEXT"]
                    )
                ),
            ),
            initial_record_generation_configuration=dict(
                type="dict", options=dict(limit=dict(type="float"))
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
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            dataset_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="dataset",
        service_client_class=DataLabelingManagementClient,
        namespace="data_labeling_service",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
