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
module: oci_data_labeling_service_dataplane_record
short_description: Manage a Record resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Record resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a record.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - The name is automatically assigned by the service. It is unique and immutable.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    dataset_id:
        description:
            - The OCID of the dataset to associate the record with.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment for the record. This is tied to the dataset. It is not changeable on the record itself.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    source_details:
        description:
            - ""
            - Required for create using I(state=present).
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
            relative_path:
                description:
                    - The path relative to the prefix specified in the dataset source details (file name).
                type: str
                required: true
            offset:
                description:
                    - The offset into the file containing the content.
                type: float
            length:
                description:
                    - The length from offset into the file containing the content.
                type: float
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
    record_metadata:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            height:
                description:
                    - Height of the image record.
                    - Applicable when record_type is 'IMAGE_METADATA'
                type: int
            width:
                description:
                    - Width of the image record.
                    - Applicable when record_type is 'IMAGE_METADATA'
                type: int
            depth:
                description:
                    - Depth of the image record.
                    - Applicable when record_type is 'IMAGE_METADATA'
                type: int
            record_type:
                description:
                    - "The record type based on dataset format details.
                      IMAGE_METADATA  - Collection of metadata related to image record.
                      TEXT_METADATA - Collection of metadata related to text record.
                      DOCUMENT_METADATA - Collection of metadata related to document record."
                type: str
                choices:
                    - "DOCUMENT_METADATA"
                    - "IMAGE_METADATA"
                    - "TEXT_METADATA"
                required: true
    record_id:
        description:
            - The OCID of the record annotated.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Record.
            - Use I(state=present) to create or update a Record.
            - Use I(state=absent) to delete a Record.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create record
  oci_data_labeling_service_dataplane_record:
    # required
    name: name_example
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    source_details:
      # required
      source_type: OBJECT_STORAGE
      relative_path: relative_path_example

      # optional
      offset: 3.4
      length: 3.4

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    record_metadata:
      # required
      record_type: DOCUMENT_METADATA

- name: Update record
  oci_data_labeling_service_dataplane_record:
    # required
    record_id: "ocid1.record.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    record_metadata:
      # required
      record_type: DOCUMENT_METADATA

- name: Update record using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_labeling_service_dataplane_record:
    # required
    name: name_example
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    record_metadata:
      # required
      record_type: DOCUMENT_METADATA

- name: Delete record
  oci_data_labeling_service_dataplane_record:
    # required
    record_id: "ocid1.record.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete record using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_labeling_service_dataplane_record:
    # required
    name: name_example
    dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
record:
    description:
        - Details of the Record resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
        source_details:
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
        record_metadata:
            description:
                - ""
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "source_details": {
            "source_type": "OBJECT_STORAGE",
            "relative_path": "relative_path_example",
            "path": "path_example",
            "offset": 10,
            "length": 10
        },
        "is_labeled": true,
        "lifecycle_state": "ACTIVE",
        "record_metadata": {
            "height": 56,
            "width": 56,
            "depth": 56,
            "record_type": "IMAGE_METADATA"
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.data_labeling_service_dataplane import DataLabelingClient
    from oci.data_labeling_service_dataplane.models import CreateRecordDetails
    from oci.data_labeling_service_dataplane.models import UpdateRecordDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RecordHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(RecordHelperGen, self).get_possible_entity_types() + [
            "datalabelingrecord",
            "datalabelingrecords",
            "dataLabelingServiceDataplanedatalabelingrecord",
            "dataLabelingServiceDataplanedatalabelingrecords",
            "datalabelingrecordresource",
            "datalabelingrecordsresource",
            "record",
            "records",
            "dataLabelingServiceDataplanerecord",
            "dataLabelingServiceDataplanerecords",
            "recordresource",
            "recordsresource",
            "datalabelingservicedataplane",
        ]

    def get_module_resource_id_param(self):
        return "record_id"

    def get_module_resource_id(self):
        return self.module.params.get("record_id")

    def get_get_fn(self):
        return self.client.get_record

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_record, record_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_record, record_id=self.module.params.get("record_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "dataset_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

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
        return oci_common_utils.list_all_resources(self.client.list_records, **kwargs)

    def get_create_model_class(self):
        return CreateRecordDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_record,
            call_fn_args=(),
            call_fn_kwargs=dict(create_record_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateRecordDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_record,
            call_fn_args=(),
            call_fn_kwargs=dict(
                record_id=self.module.params.get("record_id"),
                update_record_details=update_details,
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
            call_fn=self.client.delete_record,
            call_fn_args=(),
            call_fn_kwargs=dict(record_id=self.module.params.get("record_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


RecordHelperCustom = get_custom_class("RecordHelperCustom")


class ResourceHelper(RecordHelperCustom, RecordHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            dataset_id=dict(type="str"),
            compartment_id=dict(type="str"),
            source_details=dict(
                type="dict",
                options=dict(
                    source_type=dict(
                        type="str", required=True, choices=["OBJECT_STORAGE"]
                    ),
                    relative_path=dict(type="str", required=True),
                    offset=dict(type="float"),
                    length=dict(type="float"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            record_metadata=dict(
                type="dict",
                options=dict(
                    height=dict(type="int"),
                    width=dict(type="int"),
                    depth=dict(type="int"),
                    record_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "DOCUMENT_METADATA",
                            "IMAGE_METADATA",
                            "TEXT_METADATA",
                        ],
                    ),
                ),
            ),
            record_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="record",
        service_client_class=DataLabelingClient,
        namespace="data_labeling_service_dataplane",
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
