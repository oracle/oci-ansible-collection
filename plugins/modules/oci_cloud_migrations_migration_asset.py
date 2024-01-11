#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_cloud_migrations_migration_asset
short_description: Manage a MigrationAsset resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a MigrationAsset resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a migration asset.
    - "This resource has the following action operations in the M(oracle.oci.oci_cloud_migrations_migration_asset_actions) module: refresh,
      start_asset_replication."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    inventory_asset_id:
        description:
            - OCID of an asset for an inventory.
            - Required for create using I(state=present).
        type: str
    migration_id:
        description:
            - OCID of the associated migration.
            - Required for create using I(state=present).
        type: str
    availability_domain:
        description:
            - Availability domain
            - Required for create using I(state=present).
        type: str
    replication_compartment_id:
        description:
            - Replication compartment identifier
            - Required for create using I(state=present).
        type: str
    snap_shot_bucket_name:
        description:
            - Name of snapshot bucket
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - A user-friendly name. If empty, then source asset name will be used. Does not have to be unique, and it's changeable. Avoid entering confidential
              information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    replication_schedule_id:
        description:
            - Replication schedule identifier
            - This parameter is updatable.
        type: str
    depends_on:
        description:
            - List of migration assets that depends on this asset.
            - This parameter is updatable.
        type: list
        elements: str
    migration_asset_id:
        description:
            - Unique migration asset identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the MigrationAsset.
            - Use I(state=present) to create or update a MigrationAsset.
            - Use I(state=absent) to delete a MigrationAsset.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create migration_asset
  oci_cloud_migrations_migration_asset:
    # required
    inventory_asset_id: "ocid1.inventoryasset.oc1..xxxxxxEXAMPLExxxxxx"
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1
    replication_compartment_id: "ocid1.replicationcompartment.oc1..xxxxxxEXAMPLExxxxxx"
    snap_shot_bucket_name: snap_shot_bucket_name_example

    # optional
    display_name: display_name_example
    replication_schedule_id: "ocid1.replicationschedule.oc1..xxxxxxEXAMPLExxxxxx"
    depends_on: [ "depends_on_example" ]

- name: Update migration_asset
  oci_cloud_migrations_migration_asset:
    # required
    migration_asset_id: "ocid1.migrationasset.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    replication_schedule_id: "ocid1.replicationschedule.oc1..xxxxxxEXAMPLExxxxxx"
    depends_on: [ "depends_on_example" ]

- name: Update migration_asset using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_migrations_migration_asset:
    # required
    display_name: display_name_example

    # optional
    replication_schedule_id: "ocid1.replicationschedule.oc1..xxxxxxEXAMPLExxxxxx"
    depends_on: [ "depends_on_example" ]

- name: Delete migration_asset
  oci_cloud_migrations_migration_asset:
    # required
    migration_asset_id: "ocid1.migrationasset.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete migration_asset using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_migrations_migration_asset:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
migration_asset:
    description:
        - Details of the MigrationAsset resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Asset ID generated by mirgration service. It is used in the mirgration service pipeline.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - The type of asset referenced for inventory.
            returned: on success
            type: str
            sample: type_example
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the migration asset.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The time when the migration asset was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the migration asset was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        migration_id:
            description:
                - OCID of the associated migration.
            returned: on success
            type: str
            sample: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
        snapshots:
            description:
                - "Key-value pair representing disks ID mapped to the OCIDs of replicated or hydration server volume snapshots.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: complex
            contains:
                uuid:
                    description:
                        - ID of the vCenter disk obtained from Inventory.
                    returned: on success
                    type: str
                    sample: uuid_example
                volume_id:
                    description:
                        - ID of the hydration server volume
                    returned: on success
                    type: str
                    sample: "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
                volume_type:
                    description:
                        - The hydration server volume type
                    returned: on success
                    type: str
                    sample: BOOT
                unmodified_volume_id:
                    description:
                        - ID of the unmodified volume
                    returned: on success
                    type: str
                    sample: "ocid1.unmodifiedvolume.oc1..xxxxxxEXAMPLExxxxxx"
        parent_snapshot:
            description:
                - The parent snapshot of the migration asset to be used by the replication task.
            returned: on success
            type: str
            sample: parent_snapshot_example
        source_asset_data:
            description:
                - "Key-value pair representing asset metadata keys and values scoped to a namespace.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {}
        notifications:
            description:
                - List of notifications
            returned: on success
            type: list
            sample: []
        source_asset_id:
            description:
                - OCID that is referenced to an asset for an inventory.
            returned: on success
            type: str
            sample: "ocid1.sourceasset.oc1..xxxxxxEXAMPLExxxxxx"
        replication_schedule_id:
            description:
                - Replication schedule identifier
            returned: on success
            type: str
            sample: "ocid1.replicationschedule.oc1..xxxxxxEXAMPLExxxxxx"
        availability_domain:
            description:
                - Availability domain
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        replication_compartment_id:
            description:
                - Replication compartment identifier
            returned: on success
            type: str
            sample: "ocid1.replicationcompartment.oc1..xxxxxxEXAMPLExxxxxx"
        tenancy_id:
            description:
                - Tenancy identifier
            returned: on success
            type: str
            sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        snap_shot_bucket_name:
            description:
                - Name of snapshot bucket
            returned: on success
            type: str
            sample: snap_shot_bucket_name_example
        depended_on_by:
            description:
                - List of migration assets that depend on the asset.
            returned: on success
            type: list
            sample: []
        depends_on:
            description:
                - List of migration assets that depends on the asset.
            returned: on success
            type: list
            sample: []
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "type_example",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "migration_id": "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx",
        "snapshots": {
            "uuid": "uuid_example",
            "volume_id": "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx",
            "volume_type": "BOOT",
            "unmodified_volume_id": "ocid1.unmodifiedvolume.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "parent_snapshot": "parent_snapshot_example",
        "source_asset_data": {},
        "notifications": [],
        "source_asset_id": "ocid1.sourceasset.oc1..xxxxxxEXAMPLExxxxxx",
        "replication_schedule_id": "ocid1.replicationschedule.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_domain": "Uocm:PHX-AD-1",
        "replication_compartment_id": "ocid1.replicationcompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "snap_shot_bucket_name": "snap_shot_bucket_name_example",
        "depended_on_by": [],
        "depends_on": []
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
    from oci.cloud_migrations import MigrationClient
    from oci.cloud_migrations.models import CreateMigrationAssetDetails
    from oci.cloud_migrations.models import UpdateMigrationAssetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MigrationAssetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(MigrationAssetHelperGen, self).get_possible_entity_types() + [
            "ocmmigrationasset",
            "ocmmigrationassets",
            "cloudMigrationsocmmigrationasset",
            "cloudMigrationsocmmigrationassets",
            "ocmmigrationassetresource",
            "ocmmigrationassetsresource",
            "migrationasset",
            "migrationassets",
            "cloudMigrationsmigrationasset",
            "cloudMigrationsmigrationassets",
            "migrationassetresource",
            "migrationassetsresource",
            "cloudmigrations",
        ]

    def get_module_resource_id_param(self):
        return "migration_asset_id"

    def get_module_resource_id(self):
        return self.module.params.get("migration_asset_id")

    def get_get_fn(self):
        return self.client.get_migration_asset

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_migration_asset, migration_asset_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_migration_asset,
            migration_asset_id=self.module.params.get("migration_asset_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "migration_id",
            "display_name",
            "migration_asset_id",
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
            self.client.list_migration_assets, **kwargs
        )

    def get_create_model_class(self):
        return CreateMigrationAssetDetails

    def get_exclude_attributes(self):
        return ["inventory_asset_id"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_migration_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(create_migration_asset_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateMigrationAssetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_migration_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                migration_asset_id=self.module.params.get("migration_asset_id"),
                update_migration_asset_details=update_details,
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
            call_fn=self.client.delete_migration_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                migration_asset_id=self.module.params.get("migration_asset_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MigrationAssetHelperCustom = get_custom_class("MigrationAssetHelperCustom")


class ResourceHelper(MigrationAssetHelperCustom, MigrationAssetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            inventory_asset_id=dict(type="str"),
            migration_id=dict(type="str"),
            availability_domain=dict(type="str"),
            replication_compartment_id=dict(type="str"),
            snap_shot_bucket_name=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            replication_schedule_id=dict(type="str"),
            depends_on=dict(type="list", elements="str"),
            migration_asset_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="migration_asset",
        service_client_class=MigrationClient,
        namespace="cloud_migrations",
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
