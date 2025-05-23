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
module: oci_database_oneoff_patch
short_description: Manage an OneoffPatch resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an OneoffPatch resource in Oracle Cloud Infrastructure
    - For I(state=present), creates one-off patch for specified database version to download.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_oneoff_patch_actions) module: change_compartment, download."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - One-off patch name.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    db_version:
        description:
            - A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation.
            - "This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword,
              whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable, dbName,
              scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier."
            - Required for create using I(state=present).
        type: str
    release_update:
        description:
            - The PSU or PBP or Release Updates. To get a list of supported versions, use the L(ListDbVersions,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/database/latest/DbVersionSummary/ListDbVersions) operation.
            - Required for create using I(state=present).
        type: str
    one_off_patches:
        description:
            - List of one-off patches for Database Homes.
        type: list
        elements: str
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
    oneoff_patch_id:
        description:
            - The one-off patch L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the OneoffPatch.
            - Use I(state=present) to create or update an OneoffPatch.
            - Use I(state=absent) to delete an OneoffPatch.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create oneoff_patch
  oci_database_oneoff_patch:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    db_version: db_version_example
    release_update: release_update_example

    # optional
    one_off_patches: [ "one_off_patches_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update oneoff_patch
  oci_database_oneoff_patch:
    # required
    oneoff_patch_id: "ocid1.oneoffpatch.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update oneoff_patch using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_oneoff_patch:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete oneoff_patch
  oci_database_oneoff_patch:
    # required
    oneoff_patch_id: "ocid1.oneoffpatch.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete oneoff_patch using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_oneoff_patch:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
oneoff_patch:
    description:
        - Details of the OneoffPatch resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the one-off patch.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - One-off patch name.
            returned: on success
            type: str
            sample: display_name_example
        db_version:
            description:
                - A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation.
                - "This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel,
                  adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable,
                  dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier."
            returned: on success
            type: str
            sample: db_version_example
        release_update:
            description:
                - The PSU or PBP or Release Updates. To get a list of supported versions, use the L(ListDbVersions,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/database/latest/DbVersionSummary/ListDbVersions) operation.
            returned: on success
            type: str
            sample: release_update_example
        one_off_patches:
            description:
                - List of one-off patches for Database Homes.
            returned: on success
            type: list
            sample: []
        size_in_kbs:
            description:
                - The size of one-off patch in kilobytes.
            returned: on success
            type: float
            sample: 3.4
        lifecycle_state:
            description:
                - The current state of the one-off patch.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Detailed message for the lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        sha256_sum:
            description:
                - SHA-256 checksum of the one-off patch.
            returned: on success
            type: str
            sample: sha256_sum_example
        time_updated:
            description:
                - The date and time one-off patch was updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - The date and time one-off patch was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_expiration:
            description:
                - The date and time until which the one-off patch will be available for download.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "db_version": "db_version_example",
        "release_update": "release_update_example",
        "one_off_patches": [],
        "size_in_kbs": 3.4,
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "sha256_sum": "sha256_sum_example",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_of_expiration": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreateOneoffPatchDetails
    from oci.database.models import UpdateOneoffPatchDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OneoffPatchHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(OneoffPatchHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = oci_config_utils.create_service_client(
            self.module, WorkRequestClient
        )

    def get_possible_entity_types(self):
        return super(OneoffPatchHelperGen, self).get_possible_entity_types() + [
            "oneoffpatch",
            "oneoffpatches",
            "databaseoneoffpatch",
            "databaseoneoffpatches",
            "oneoffpatchresource",
            "oneoffpatchesresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "oneoff_patch_id"

    def get_module_resource_id(self):
        return self.module.params.get("oneoff_patch_id")

    def get_get_fn(self):
        return self.client.get_oneoff_patch

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_oneoff_patch, oneoff_patch_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_oneoff_patch,
            oneoff_patch_id=self.module.params.get("oneoff_patch_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_oneoff_patches, **kwargs
        )

    def get_create_model_class(self):
        return CreateOneoffPatchDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_oneoff_patch,
            call_fn_args=(),
            call_fn_kwargs=dict(create_oneoff_patch_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateOneoffPatchDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_oneoff_patch,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oneoff_patch_id=self.module.params.get("oneoff_patch_id"),
                update_oneoff_patch_details=update_details,
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
            call_fn=self.client.delete_oneoff_patch,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oneoff_patch_id=self.module.params.get("oneoff_patch_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OneoffPatchHelperCustom = get_custom_class("OneoffPatchHelperCustom")


class ResourceHelper(OneoffPatchHelperCustom, OneoffPatchHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            db_version=dict(type="str"),
            release_update=dict(type="str"),
            one_off_patches=dict(type="list", elements="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            oneoff_patch_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="oneoff_patch",
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
