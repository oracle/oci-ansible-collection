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
module: oci_dts_transfer_job
short_description: Manage a TransferJob resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a TransferJob resource in Oracle Cloud Infrastructure
    - For I(state=present), create a new Transfer Job that corresponds with customer's logical dataset e.g. a DB or a filesystem.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - ""
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    upload_bucket_name:
        description:
            - ""
        type: str
    lifecycle_state:
        description:
            - ""
            - This parameter is updatable.
        type: str
        choices:
            - "CLOSED"
    display_name:
        description:
            - ""
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    device_type:
        description:
            - ""
            - This parameter is updatable.
        type: str
        choices:
            - "DISK"
            - "APPLIANCE"
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    id:
        description:
            - ID of the Transfer Job
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
    state:
        description:
            - The state of the TransferJob.
            - Use I(state=present) to create or update a TransferJob.
            - Use I(state=absent) to delete a TransferJob.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create transfer_job
  oci_dts_transfer_job:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    upload_bucket_name: upload_bucket_name_example
    display_name: display_name_example
    device_type: DISK
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update transfer_job
  oci_dts_transfer_job:
    # required
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CLOSED
    display_name: display_name_example
    device_type: DISK
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update transfer_job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_dts_transfer_job:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    lifecycle_state: CLOSED
    device_type: DISK
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete transfer_job
  oci_dts_transfer_job:
    # required
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete transfer_job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_dts_transfer_job:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
transfer_job:
    description:
        - Details of the TransferJob resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - ""
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - ""
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        upload_bucket_name:
            description:
                - ""
            returned: on success
            type: str
            sample: upload_bucket_name_example
        display_name:
            description:
                - ""
            returned: on success
            type: str
            sample: display_name_example
        label:
            description:
                - ""
            returned: on success
            type: str
            sample: label_example
        creation_time:
            description:
                - ""
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        device_type:
            description:
                - ""
            returned: on success
            type: str
            sample: DISK
        lifecycle_state:
            description:
                - ""
            returned: on success
            type: str
            sample: INITIATED
        attached_transfer_appliance_labels:
            description:
                - Transfer Appliance labels associated with this transfer Job
            returned: on success
            type: list
            sample: []
        attached_transfer_package_labels:
            description:
                - Transfer Package labels associated with this transfer Job
            returned: on success
            type: list
            sample: []
        attached_transfer_device_labels:
            description:
                - Transfer Device labels associated with this transfer Job
            returned: on success
            type: list
            sample: []
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "upload_bucket_name": "upload_bucket_name_example",
        "display_name": "display_name_example",
        "label": "label_example",
        "creation_time": "2013-10-20T19:20:30+01:00",
        "device_type": "DISK",
        "lifecycle_state": "INITIATED",
        "attached_transfer_appliance_labels": [],
        "attached_transfer_package_labels": [],
        "attached_transfer_device_labels": [],
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
    from oci.dts import TransferJobClient
    from oci.dts.models import CreateTransferJobDetails
    from oci.dts.models import UpdateTransferJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TransferJobHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(TransferJobHelperGen, self).get_possible_entity_types() + [
            "transferjob",
            "transferjobs",
            "dtstransferjob",
            "dtstransferjobs",
            "transferjobresource",
            "transferjobsresource",
            "dts",
        ]

    def get_module_resource_id_param(self):
        return "id"

    def get_module_resource_id(self):
        return self.module.params.get("id")

    def get_get_fn(self):
        return self.client.get_transfer_job

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_transfer_job, id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transfer_job, id=self.module.params.get("id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name"]
            if self._use_name_as_identifier()
            else ["lifecycle_state", "display_name"]
        )

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
        return oci_common_utils.list_all_resources(
            self.client.list_transfer_jobs, **kwargs
        )

    def get_create_model_class(self):
        return CreateTransferJobDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_transfer_job,
            call_fn_args=(),
            call_fn_kwargs=dict(create_transfer_job_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateTransferJobDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_transfer_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                id=self.module.params.get("id"),
                update_transfer_job_details=update_details,
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
            call_fn=self.client.delete_transfer_job,
            call_fn_args=(),
            call_fn_kwargs=dict(id=self.module.params.get("id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


TransferJobHelperCustom = get_custom_class("TransferJobHelperCustom")


class ResourceHelper(TransferJobHelperCustom, TransferJobHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            upload_bucket_name=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["CLOSED"]),
            display_name=dict(aliases=["name"], type="str"),
            device_type=dict(type="str", choices=["DISK", "APPLIANCE"]),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="transfer_job",
        service_client_class=TransferJobClient,
        namespace="dts",
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
