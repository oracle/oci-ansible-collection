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
module: oci_database_software_image
short_description: Manage a DatabaseSoftwareImage resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DatabaseSoftwareImage resource in Oracle Cloud Infrastructure
    - For I(state=present), create database software image in the specified compartment.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_software_image_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment the database software image  belongs in.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    database_version:
        description:
            - The database version with which the database software image is to be built.
        type: str
    image_shape_family:
        description:
            - To what shape the image is meant for.
        type: str
        choices:
            - "VM_BM_SHAPE"
            - "EXADATA_SHAPE"
            - "EXACC_SHAPE"
    image_type:
        description:
            - The type of software image. Can be grid or database.
        type: str
        choices:
            - "GRID_IMAGE"
            - "DATABASE_IMAGE"
    patch_set:
        description:
            - The PSU or PBP or Release Updates. To get a list of supported versions, use the L(ListDbVersions,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/database/latest/DbVersionSummary/ListDbVersions) operation.
        type: str
    database_software_image_one_off_patches:
        description:
            - List of one-off patches for Database Homes.
        type: list
        elements: str
    ls_inventory:
        description:
            - The output from the OPatch lsInventory command, which is passed as a string.
        type: str
    source_db_home_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Home.
        type: str
    display_name:
        description:
            - The user-friendly name for the database software image. The name does not have to be unique.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - This parameter is updatable.
        type: dict
    database_software_image_id:
        description:
            - The DB system L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DatabaseSoftwareImage.
            - Use I(state=present) to create or update a DatabaseSoftwareImage.
            - Use I(state=absent) to delete a DatabaseSoftwareImage.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create database_software_image
  oci_database_software_image:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    database_version: database_version_example
    image_shape_family: VM_BM_SHAPE
    image_type: GRID_IMAGE
    patch_set: patch_set_example
    database_software_image_one_off_patches: [ "database_software_image_one_off_patches_example" ]
    ls_inventory: ls_inventory_example
    source_db_home_id: "ocid1.sourcedbhome.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update database_software_image
  oci_database_software_image:
    # required
    database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update database_software_image using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_software_image:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete database_software_image
  oci_database_software_image:
    # required
    database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete database_software_image using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_software_image:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
database_software_image:
    description:
        - Details of the DatabaseSoftwareImage resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database software image.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        database_version:
            description:
                - The database version with which the database software image is to be built.
            returned: on success
            type: str
            sample: database_version_example
        display_name:
            description:
                - The user-friendly name for the database software image. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        lifecycle_state:
            description:
                - The current state of the database software image.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Detailed message for the lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the database software image was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        image_type:
            description:
                - The type of software image. Can be grid or database.
            returned: on success
            type: str
            sample: GRID_IMAGE
        image_shape_family:
            description:
                - To what shape the image is meant for.
            returned: on success
            type: str
            sample: VM_BM_SHAPE
        patch_set:
            description:
                - The PSU or PBP or Release Updates. To get a list of supported versions, use the L(ListDbVersions,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/database/latest/DbVersionSummary/ListDbVersions) operation.
            returned: on success
            type: str
            sample: patch_set_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        database_software_image_included_patches:
            description:
                - List of one-off patches for Database Homes.
            returned: on success
            type: list
            sample: []
        included_patches_summary:
            description:
                - The patches included in the image and the version of the image
            returned: on success
            type: str
            sample: included_patches_summary_example
        database_software_image_one_off_patches:
            description:
                - List of one-off patches for Database Homes.
            returned: on success
            type: list
            sample: []
        ls_inventory:
            description:
                - The output from the OPatch lsInventory command, which is passed as a string.
            returned: on success
            type: str
            sample: ls_inventory_example
        is_upgrade_supported:
            description:
                - True if this Database software image is supported for Upgrade.
            returned: on success
            type: bool
            sample: true
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "database_version": "database_version_example",
        "display_name": "display_name_example",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "image_type": "GRID_IMAGE",
        "image_shape_family": "VM_BM_SHAPE",
        "patch_set": "patch_set_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "database_software_image_included_patches": [],
        "included_patches_summary": "included_patches_summary_example",
        "database_software_image_one_off_patches": [],
        "ls_inventory": "ls_inventory_example",
        "is_upgrade_supported": true
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
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreateDatabaseSoftwareImageDetails
    from oci.database.models import UpdateDatabaseSoftwareImageDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseSoftwareImageHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(DatabaseSoftwareImageHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_possible_entity_types(self):
        return super(
            DatabaseSoftwareImageHelperGen, self
        ).get_possible_entity_types() + [
            "databasesoftwareimage",
            "databasesoftwareimages",
            "databasedatabasesoftwareimage",
            "databasedatabasesoftwareimages",
            "databasesoftwareimageresource",
            "databasesoftwareimagesresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "database_software_image_id"

    def get_module_resource_id(self):
        return self.module.params.get("database_software_image_id")

    def get_get_fn(self):
        return self.client.get_database_software_image

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_software_image,
            database_software_image_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_software_image,
            database_software_image_id=self.module.params.get(
                "database_software_image_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "display_name",
            "image_type",
            "image_shape_family",
        ]

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
            self.client.list_database_software_images, **kwargs
        )

    def get_create_model_class(self):
        return CreateDatabaseSoftwareImageDetails

    def get_exclude_attributes(self):
        return ["source_db_home_id"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_database_software_image,
            call_fn_args=(),
            call_fn_kwargs=dict(create_database_software_image_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDatabaseSoftwareImageDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_database_software_image,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_software_image_id=self.module.params.get(
                    "database_software_image_id"
                ),
                update_database_software_image_details=update_details,
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
            call_fn=self.client.delete_database_software_image,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_software_image_id=self.module.params.get(
                    "database_software_image_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DatabaseSoftwareImageHelperCustom = get_custom_class(
    "DatabaseSoftwareImageHelperCustom"
)


class ResourceHelper(DatabaseSoftwareImageHelperCustom, DatabaseSoftwareImageHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            database_version=dict(type="str"),
            image_shape_family=dict(
                type="str", choices=["VM_BM_SHAPE", "EXADATA_SHAPE", "EXACC_SHAPE"]
            ),
            image_type=dict(type="str", choices=["GRID_IMAGE", "DATABASE_IMAGE"]),
            patch_set=dict(type="str"),
            database_software_image_one_off_patches=dict(type="list", elements="str"),
            ls_inventory=dict(type="str"),
            source_db_home_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            database_software_image_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="database_software_image",
        service_client_class=DatabaseClient,
        namespace="database",
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
