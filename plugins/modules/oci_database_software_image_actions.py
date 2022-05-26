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
module: oci_database_software_image_actions
short_description: Perform actions on a DatabaseSoftwareImage resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DatabaseSoftwareImage resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), move the Database Software Image and its dependent resources to the specified compartment.
      For more information about moving Databse Software Images, see
      L(Moving Database Resources to a Different Compartment,https://docs.cloud.oracle.com/Content/Database/Concepts/databaseoverview.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the resource to.
        type: str
        required: true
    database_software_image_id:
        description:
            - The DB system L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the DatabaseSoftwareImage.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on database_software_image
  oci_database_software_image_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import ChangeCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseSoftwareImageActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    def __init__(self, *args, **kwargs):
        super(DatabaseSoftwareImageActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "database_software_image_id"

    def get_module_resource_id(self):
        return self.module.params.get("database_software_image_id")

    def get_get_fn(self):
        return self.client.get_database_software_image

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_software_image,
            database_software_image_id=self.module.params.get(
                "database_software_image_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_database_software_image_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_compartment_details=action_details,
                database_software_image_id=self.module.params.get(
                    "database_software_image_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DatabaseSoftwareImageActionsHelperCustom = get_custom_class(
    "DatabaseSoftwareImageActionsHelperCustom"
)


class ResourceHelper(
    DatabaseSoftwareImageActionsHelperCustom, DatabaseSoftwareImageActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            database_software_image_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
