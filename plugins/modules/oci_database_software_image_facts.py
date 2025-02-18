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
module: oci_database_software_image_facts
short_description: Fetches details about one or multiple DatabaseSoftwareImage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DatabaseSoftwareImage resources in Oracle Cloud Infrastructure
    - Gets a list of the database software images in the specified compartment.
    - If I(database_software_image_id) is specified, the details of a single DatabaseSoftwareImage will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    database_software_image_id:
        description:
            - The DB system L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific database_software_image.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple database_software_images.
        type: str
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME
              is ascending. The DISPLAYNAME sort order is case sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state exactly.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "TERMINATING"
            - "TERMINATED"
            - "UPDATING"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
    image_type:
        description:
            - A filter to return only resources that match the given image type exactly.
        type: str
        choices:
            - "GRID_IMAGE"
            - "DATABASE_IMAGE"
    image_shape_family:
        description:
            - A filter to return only resources that match the given image shape family exactly.
        type: str
        choices:
            - "VM_BM_SHAPE"
            - "EXADATA_SHAPE"
            - "EXACC_SHAPE"
    is_upgrade_supported:
        description:
            - If provided, filters the results to the set of database versions which are supported for Upgrade.
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific database_software_image
  oci_database_software_image_facts:
    # required
    database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"

- name: List database_software_images
  oci_database_software_image_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: PROVISIONING
    display_name: display_name_example
    image_type: GRID_IMAGE
    image_shape_family: VM_BM_SHAPE
    is_upgrade_supported: true

"""

RETURN = """
database_software_images:
    description:
        - List of DatabaseSoftwareImage resources
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
                - The patches included in the image and the version of the image.
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
    sample: [{
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
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseSoftwareImageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "database_software_image_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_software_image,
            database_software_image_id=self.module.params.get(
                "database_software_image_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "display_name",
            "image_type",
            "image_shape_family",
            "is_upgrade_supported",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_database_software_images,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DatabaseSoftwareImageFactsHelperCustom = get_custom_class(
    "DatabaseSoftwareImageFactsHelperCustom"
)


class ResourceFactsHelper(
    DatabaseSoftwareImageFactsHelperCustom, DatabaseSoftwareImageFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            database_software_image_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "AVAILABLE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "TERMINATING",
                    "TERMINATED",
                    "UPDATING",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            image_type=dict(type="str", choices=["GRID_IMAGE", "DATABASE_IMAGE"]),
            image_shape_family=dict(
                type="str", choices=["VM_BM_SHAPE", "EXADATA_SHAPE", "EXACC_SHAPE"]
            ),
            is_upgrade_supported=dict(type="bool"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="database_software_image",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(database_software_images=result)


if __name__ == "__main__":
    main()
