# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
from ansible.module_utils._text import to_bytes
from ansible.module_utils import six
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)


try:
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


logger = oci_common_utils.get_logger("oci_database_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


class AutonomousDatabaseHelperCustom:
    # get model doesn't return admin_password of existing database resources. Thus, excluding
    # admin_password for idempotency.
    def get_exclude_attributes(self):
        return super(AutonomousDatabaseHelperCustom, self).get_exclude_attributes() + [
            "admin_password",
            "source",
            "is_preview_version_with_service_terms_accepted",
        ]


class AutonomousDatabaseRegionalWalletHelperCustom:
    def is_update(self):
        return True

    def get_default_module_wait_timeout(self):
        return int(1 * 2400)


class AutonomousDatabaseActionsHelperCustom:
    REGISTER_AUTONOMOUS_DATABASE_DATA_SAFE = "register_autonomous_database_data_safe"
    DEREGISTER_AUTONOMOUS_DATABASE_DATA_SAFE = (
        "deregister_autonomous_database_data_safe"
    )
    ENABLE_AUTONOMOUS_DATABASE_OPERATIONS_INSIGHTS = (
        "enable_autonomous_database_operations_insights"
    )
    DISABLE_AUTONOMOUS_DATABASE_OPERATIONS_INSIGHTS = (
        "disable_autonomous_database_operations_insights"
    )

    def generate_autonomous_database_wallet(self):
        wallet_file = self.module.params.get("wallet_file")
        try:
            if wallet_file is None or len(wallet_file.strip()) == 0:
                self.module.fail_json(msg="Wallet file must be declared")

            if self.module.params.get("force") or not os.path.isfile(
                to_bytes(wallet_file)
            ):
                response_data = super(
                    AutonomousDatabaseActionsHelperCustom, self
                ).generate_autonomous_database_wallet()

                if not self.write_stream_to_file(
                    response_data, self.module.params.get("wallet_file")
                ):
                    self.module.fail_json(
                        msg="Error occurred while writing to wallet file"
                    )

            else:
                self.module.fail_json(
                    msg="Wallet file  %s already exists. Use force option to overwrite."
                    % wallet_file
                )
        except ServiceError as ex:
            self.module.fail_json(msg=ex.message)

    def write_stream_to_file(self, data, file):
        try:
            with open(to_bytes(file), "wb") as f:
                for d in data:
                    f.write(d)
        except IOError:
            return False
        return True

    def is_action_necessary(self, action, resource=None):
        if (
            action == self.REGISTER_AUTONOMOUS_DATABASE_DATA_SAFE
            and resource.data_safe_status == "REGISTERED"
        ):
            return False
        elif (
            action == self.DEREGISTER_AUTONOMOUS_DATABASE_DATA_SAFE
            and resource.data_safe_status == "NOT_REGISTERED"
        ):
            return False
        elif action == self.ENABLE_AUTONOMOUS_DATABASE_OPERATIONS_INSIGHTS:
            return resource.operations_insights_status != "ENABLED"
        elif action == self.DISABLE_AUTONOMOUS_DATABASE_OPERATIONS_INSIGHTS:
            return resource.operations_insights_status != "NOT_ENABLED"
        else:
            return super(
                AutonomousDatabaseActionsHelperCustom, self
            ).is_action_necessary(action, resource)


class AutonomousDatabaseBackupHelperCustom:
    def is_create(self):
        return True


class DbSystemHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        module.params["initial_data_storage_size_in_gb"] = module.params[
            "data_storage_size_in_gbs"
        ]

        super(DbSystemHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )

    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            DbSystemHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)

        # LaunchDbSystem takes the argument initial_data_storage_size_in_gb so data_storage_size_in_gbs
        # does not exist on LaunchDbSystemDetails
        # Thus data_storage_size_in_gbs will not be present by default in the create_model_dict
        # In the custom change above we the data_storage_size_in_gbs value into module.params["initial_data_storage_size_in_gb"]
        # so here we explicitly add that back to the create_model dict so it gets matched during the idemptency check
        if create_model_dict.get("initial_data_storage_size_in_gb") is not None:
            create_model_dict["data_storage_size_in_gbs"] = create_model_dict.pop(
                "initial_data_storage_size_in_gb"
            )
        return create_model_dict

    def get_update_model_dict_for_idempotence_check(self, update_model):
        update_model_dict = super(
            DbSystemHelperCustom, self
        ).get_update_model_dict_for_idempotence_check(update_model)

        # version only applies to patching and has custom idempotence logic which is handled in
        # is_update_necessary
        update_model_dict.pop("version", None)

        return update_model_dict

    def get_exclude_attributes(self):
        exclude_attributes = super(DbSystemHelperCustom, self).get_exclude_attributes()
        return exclude_attributes + [
            # source is the discriminator and is not returned by the GET model because post-creation
            # it doesn't matter what the DB was created from
            "source",
            # the db_home resource is not returned on GetDbSystem and cannot be updated through UpdateDbSystem
            # so we do not consider it
            # This means that if the user updates db_home in their playbook after the initial create, the resource
            # will continue to match and will not be updated
            "db_home",
            # attribute source_db_system_id is not returned on GetDbSystem
            "source_db_system_id",
            # attribute kms_key_version_id is not returned in Get model
            "kms_key_version_id",
        ]

    def is_update_necessary(self, existing_resource_dict):
        needs_update = super(DbSystemHelperCustom, self).is_update_necessary(
            existing_resource_dict
        )
        if not needs_update:
            update_model = self.get_update_model()
            needs_update = is_patch_necessary(
                patch_getter_method=self.client.get_db_system_patch,
                current_version=existing_resource_dict.get("version"),
                requested_patch_details=update_model.version,
                db_system_id=existing_resource_dict.get("id"),
            )

        return needs_update

    # summary model returns None value for attribute `kms_key_id`. This override makes a Get call for each and every resource
    # returned in list.
    def list_resources(self):
        result = [
            oci_common_utils.call_with_backoff(
                self.client.get_db_system, db_system_id=db_system.id,
            ).data
            for db_system in super(DbSystemHelperCustom, self).list_resources()
        ]
        return result


class DbHomeHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        if module.params.get("patch_details"):
            if module.params.get("db_version"):
                module.fail_json(
                    msg="db_version and patch_details parameters are mutually exclusive"
                )

            module.params["db_version"] = module.params.get("patch_details")

        # this is a param rename in the codegen so this name will be meaningless to
        # all subsequent generated code
        del module.params["patch_details"]

        super(DbHomeHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )

    def get_exclude_attributes(self):
        exclude_attributes = super(DbHomeHelperCustom, self).get_exclude_attributes()

        return exclude_attributes + [
            # source is the discriminator and is not returned by the GET model because post-creation
            # it doesn't matter what the DB was created from
            "source",
            # the database resource is not returned on GetDbHome and cannot be updated through UpdateDbHome
            # so we do not consider it
            # This means that if the user updates database in their playbook after the initial create, the resource
            # will continue to match and will not be updated
            "database",
            "kms_key_version_id",
        ]

    def get_update_model_dict_for_idempotence_check(self, update_model):
        update_model_dict = super(
            DbHomeHelperCustom, self
        ).get_update_model_dict_for_idempotence_check(update_model)

        # db_version only applies to patching and has custom idempotence logic which is handled in
        # is_update_necessary
        if "db_version" in update_model_dict:
            del update_model_dict["db_version"]

        return update_model_dict

    def is_update_necessary(self, resource=None):
        # dbVersion is the only updatable field so it is the only thing we need to check to determine
        # if an update is necessary
        update_model = self.get_update_model()
        needs_update = is_patch_necessary(
            patch_getter_method=self.client.get_db_home_patch,
            current_version=resource["db_version"],
            requested_patch_details=update_model.db_version,
            db_home_id=resource["id"],
        )
        return needs_update


class DataGuardAssociationHelperCustom:
    def get_module_resource_id(self):
        return None

    def get_module_resource_id_param(self):
        return None

    def get_get_model_from_summary_model(self, summary_model):
        return self.client.get_data_guard_association(
            database_id=self.module.params["database_id"],
            data_guard_association_id=summary_model.id,
        ).data

    def get_get_fn(self):
        def get_fn(data_guard_association_id):
            return self.client.get_data_guard_association(
                data_guard_association_id=data_guard_association_id,
                database_id=self.module.params["database_id"],
            )

        return get_fn
        # return self.client.get_data_guard_association

    def get_exclude_attributes(self):
        exclude_attributes = super(
            DataGuardAssociationHelperCustom, self
        ).get_exclude_attributes()
        return exclude_attributes + [
            # not returned by GET model
            "database_admin_password",
            # discriminator, not returned by GET (existing vs new db system)
            "creation_type",
        ]


class DataGuardAssociationActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        data_guard_association = resource or self.get_resource().data

        # This mirrors the old behavior
        if action == "switchover" and data_guard_association.role == "PRIMARY":
            return True
        if action == "failover" and data_guard_association.role == "STANDBY":
            return True
        if (
            action == "reinstate"
            and data_guard_association.peer_role == "DISABLED_STANDBY"
        ):
            return True

        return False


def is_patch_necessary(
    patch_getter_method, current_version, requested_patch_details, **kwargs
):
    is_patch_necessary = False
    if requested_patch_details:
        # the following logic is consistent with the way the legacy modules check if a patch has been applied
        get_patch_kwargs = kwargs.copy()
        get_patch_kwargs.update(patch_id=requested_patch_details.patch_id)

        existing_patch = oci_common_utils.call_with_backoff(
            patch_getter_method, **get_patch_kwargs
        ).data
        if existing_patch.version != current_version:
            _debug(
                "DB system version {current_version} does not match patch version: {patch_version}. Applying patch.".format(
                    current_version=current_version,
                    patch_version=existing_patch.version,
                )
            )
            is_patch_necessary = True

    return is_patch_necessary


class ExadataInfrastructureHelperCustom:
    def delete_resource(self):
        try:
            delete_operation_response = oci_wait_utils.call_and_wait(
                call_fn=self.client.delete_exadata_infrastructure,
                call_fn_args=(),
                call_fn_kwargs=dict(
                    exadata_infrastructure_id=self.module.params.get(
                        "exadata_infrastructure_id"
                    ),
                ),
                waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
                operation=oci_common_utils.DELETE_OPERATION_KEY,
                waiter_client=self.work_request_client,
                resource_helper=self,
                wait_for_states=oci_common_utils.get_work_request_completed_states(),
            )
        except ServiceError as delete_service_error:
            # delete_exadata_infrastructure can return a 404 if you are not allowed to delete it
            if delete_service_error.status == 404:
                # so attempt a GET to determine if the resource is really still there
                try:
                    oci_common_utils.call_with_backoff(
                        self.client.get_exadata_infrastructure,
                        exadata_infrastructure_id=self.module.params.get(
                            "exadata_infrastructure_id"
                        ),
                    )
                except ServiceError as get_service_error:
                    # if the resource truly doesn't exist, then just re-throw the existing delete 404
                    # and the resource_utils function will handle it appropriately
                    if get_service_error.status == 404:
                        raise delete_service_error

                # if we reach here it means that the DELETE call returned a 404 but the GET operation was successful
                # this means the resource is still present so the DELETE call must have recieved a 404 for some other
                # reason, so report that back to the user
                self.module.fail_json(
                    msg="Deleting resource failed with exception: {0}".format(
                        delete_service_error.message
                    )
                )

            raise delete_service_error

        return delete_operation_response


class ExadataInfrastructureActionsHelperCustom:
    def download_exadata_infrastructure_config_file(self):
        operation_response = oci_common_utils.call_with_backoff(
            self.client.download_exadata_infrastructure_config_file,
            exadata_infrastructure_id=self.module.params.get(
                "exadata_infrastructure_id"
            ),
        )

        dest = self.module.params.get("config_file_dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in operation_response.data.raw.stream(
                chunk_size, decode_content=True
            ):
                dest_file.write(chunk)

        return None


class AutonomousContainerDatabaseHelperCustom:
    # resource `AutonomousContainerDatabase` has attribute `maintenance_window` which gives the scheduling details for
    # the quarterly maintenance window. However object `UpdateAutonomousContainerDatabase` represents it with different
    # name 'maintenance_window_details'.
    def is_update_necessary(self, existing_resource_dict):
        resource_dict = dict(existing_resource_dict)
        resource_dict["maintenance_window_details"] = resource_dict.pop(
            "maintenance_window", None
        )
        return super(AutonomousContainerDatabaseHelperCustom, self).is_update_necessary(
            resource_dict
        )

    def get_existing_resource_dict_for_idempotence_check(self, existing_resource):
        existing_resource_dict = super(
            AutonomousContainerDatabaseHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(existing_resource)

        existing_resource_dict[
            "maintenance_window_details"
        ] = existing_resource_dict.pop("maintenance_window", None)
        return existing_resource_dict

    def list_resources(self):
        # Method `ListAutonomousContainerDatabases` has filer `infrastructureType` which returns resources that
        # match the given Infrastructure Type. If not passed API sets its value to `CLOUD`. In order to return ExaCC
        # resources it's necessary to pass `infrastructureType` = `CLOUD_AT_CUSTOMER` and `infrastructureType` = `CLOUD`
        # for non ExaCC resources.
        if not (
            self.module.params.get("autonomous_exadata_infrastructure_id")
            and self.module.params.get("autonomous_vm_cluster_id")
        ):
            optional_kwargs = super(
                AutonomousContainerDatabaseHelperCustom, self
            ).get_optional_kwargs_for_list()
            required_kwargs = super(
                AutonomousContainerDatabaseHelperCustom, self
            ).get_required_kwargs_for_list()
            kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

            autonomous_container_database_at_cloud = oci_common_utils.list_all_resources(
                self.client.list_autonomous_container_databases, **kwargs
            )

            kwargs["infrastructure_type"] = "CLOUD_AT_CUSTOMER"
            autonomous_container_database_cloud_at_customer = oci_common_utils.list_all_resources(
                self.client.list_autonomous_container_databases, **kwargs
            )
            return (
                autonomous_container_database_at_cloud
                + autonomous_container_database_cloud_at_customer
            )
        return super(AutonomousContainerDatabaseHelperCustom, self).list_resources()

    def get_exclude_attributes(self):
        exclude_attributes = super(
            AutonomousContainerDatabaseHelperCustom, self
        ).get_exclude_attributes()
        return exclude_attributes + [
            "kms_key_version_id",
        ]


class VmClusterNetworkHelperCustom:
    def get_get_fn(self):
        def get_fn(vm_cluster_network_id):
            return self.client.get_vm_cluster_network(
                vm_cluster_network_id=vm_cluster_network_id,
                exadata_infrastructure_id=self.module.params.get(
                    "exadata_infrastructure_id"
                ),
            )

        return get_fn

    def list_resources(self):
        result = [
            oci_common_utils.call_with_backoff(
                self.client.get_vm_cluster_network,
                exadata_infrastructure_id=vm_cluster_networks.exadata_infrastructure_id,
                vm_cluster_network_id=vm_cluster_networks.id,
            ).data
            for vm_cluster_networks in super(
                VmClusterNetworkHelperCustom, self
            ).list_resources()
        ]
        return result


class VmClusterNetworkActionsHelperCustom:
    def get_action_desired_states(self, action):
        action_desired_states = super(
            VmClusterNetworkActionsHelperCustom, self
        ).get_action_desired_states(action)

        if action.lower() == "validate":
            return action_desired_states + [
                "VALIDATED",
            ]
        return action_desired_states

    def get_action_idempotent_states(self, action):
        action_idempotent_states = super(
            VmClusterNetworkActionsHelperCustom, self
        ).get_action_idempotent_states(action)

        if action.lower() == "validate":
            return action_idempotent_states + [
                "VALIDATED",
            ]
        return action_idempotent_states

    def download_vm_cluster_network_config_file(self):
        operation_response = oci_common_utils.call_with_backoff(
            self.client.download_vm_cluster_network_config_file,
            exadata_infrastructure_id=self.module.params.get(
                "exadata_infrastructure_id"
            ),
            vm_cluster_network_id=self.module.params.get("vm_cluster_network_id"),
        )

        dest = self.module.params.get("config_file_dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in operation_response.data.raw.stream(
                chunk_size, decode_content=True
            ):
                dest_file.write(chunk)

        return None


class VmClusterHelperCustom:
    def get_create_model_dict_for_idempotence_check(self, create_model):
        model_dict = super(
            VmClusterHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)

        if model_dict["cpu_core_count"]:
            model_dict["cpus_enabled"] = model_dict["cpu_core_count"]
            del model_dict["cpu_core_count"]

        return model_dict

    def get_attributes_to_consider_for_create_idempotency_check(self, create_model):
        attributes_to_consider = super(
            VmClusterHelperCustom, self
        ).get_attributes_to_consider_for_create_idempotency_check(create_model)
        if "cpu_core_count" in attributes_to_consider:
            attributes_to_consider.remove("cpu_core_count")
            attributes_to_consider.append("cpus_enabled")

        return attributes_to_consider

    def get_update_model_dict_for_idempotence_check(self, update_model):
        # The cpu count param has different names in update model (cpu_core_count) and get model
        # (cpus_enabled). So update the name in the update model for idempotence logic to work.
        update_model_dict = to_dict(update_model)
        update_model_dict["cpus_enabled"] = update_model_dict.pop(
            "cpu_core_count", None
        )
        return update_model_dict

    def get_update_model(self):
        # if license model is passed and matches the existing value on the resource
        # UPDATE will fail
        # so if license model matches what is on the resource, skip sending the field
        update_model = super(VmClusterHelperCustom, self).get_update_model()
        if update_model.license_model:
            existing_resource_dict = to_dict(self.get_resource().data)
            if update_model.license_model == existing_resource_dict.get(
                "license_model"
            ):
                update_model.license_model = None

        return update_model


class DatabaseHelperCustom:
    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            DatabaseHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        create_model_dict = dict(
            (k, v)
            for k, v in six.iteritems(create_model_dict)
            if k not in ["source", "db_version"]
        )
        for k, v in six.iteritems(create_model_dict.pop("database", dict())):
            if k not in ["backup_id", "backup_tde_password", "admin_password"]:
                create_model_dict[k] = v
        return create_model_dict

    # model returned by GetDatabase operation doesn't have attribute `kms_key_version_id` & `tde_wallet_password`
    def get_exclude_attributes(self):
        exclude_attributes = super(DatabaseHelperCustom, self).get_exclude_attributes()
        return exclude_attributes + [
            "kms_key_version_id",
            "tde_wallet_password",
        ]

    # attributes `new_admin_password`, `old_tde_wallet_password`, "new_tde_wallet_password" are not returned in GET model
    # for security reasons.
    def get_update_model_dict_for_idempotence_check(self, update_model):
        update_model_dict = super(
            DatabaseHelperCustom, self
        ).get_update_model_dict_for_idempotence_check(update_model)
        update_model_dict.pop("new_admin_password", None)
        update_model_dict.pop("old_tde_wallet_password", None)
        update_model_dict.pop("new_tde_wallet_password", None)
        return update_model_dict


class AutonomousVmClusterHelperCustom:
    # work requests generated for `UpdateAutonomousVmCluster` operation never gets completed however attributes get
    # updated with values passed in request.
    def update_resource(self):
        operation_response = oci_common_utils.call_with_backoff(
            self.client.update_autonomous_vm_cluster,
            autonomous_vm_cluster_id=self.module.params.get("autonomous_vm_cluster_id"),
            update_autonomous_vm_cluster_details=self.get_update_model(),
        )

        # Delete `opc-work-request-id` from operation_response to allow falling back to lifecycle based waiting.
        if (
            operation_response
            and operation_response.headers
            and oci_wait_utils.WORK_REQUEST_HEADER in operation_response.headers
        ):
            del operation_response.headers[oci_wait_utils.WORK_REQUEST_HEADER]

        return oci_wait_utils.get_waiter(
            oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            oci_common_utils.UPDATE_OPERATION_KEY,
            self.work_request_client,
            self,
            operation_response=operation_response,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        ).wait()


class BackupDestinationHelperCustom:
    def __init__(self, *args, **kwargs):
        super(BackupDestinationHelperCustom, self).__init__(*args, **kwargs)
        self.delete_vpc_users_from_update_model_dict = False

    # resource returned from server doesn't have an attribute `mount_type_details` Thus we add this attribute in
    # existing resource dict by using values returned for parameters `nfs_mount_type` , `local_mount_point_path`,
    # `nfs_server` & `nfs_server_export`.
    def get_existing_resource_dict_for_idempotence_check(self, resource):
        resource_dict = super(
            BackupDestinationHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(resource)
        resource_dict["mount_type_details"] = {
            "mount_type": resource_dict.get("nfs_mount_type", None),
            "local_mount_point_path": resource_dict.get("local_mount_point_path", None),
            "nfs_server": resource_dict.get("nfs_server", None),
            "nfs_server_export": resource_dict.get("nfs_server_export", None),
        }
        return resource_dict

    def get_update_model_dict_for_idempotence_check(self, update_model):
        update_model_dict = super(
            BackupDestinationHelperCustom, self
        ).get_update_model_dict_for_idempotence_check(update_model)
        if "vpc_users" in update_model_dict:
            del update_model_dict["vpc_users"]
        return update_model_dict

    def is_update_necessary(self, existing_resource_dict):
        vpc_users_source_list = self.module.params.get("vpc_users")
        vpc_users_target_list = existing_resource_dict["vpc_users"]

        if vpc_users_source_list is not None and not all(
            [
                oci_common_utils.is_in_list(
                    vpc_users_target_list, element, ignore_attr_if_not_in_target=False,
                )
                for element in vpc_users_source_list
            ]
        ):
            return True

        return super(BackupDestinationHelperCustom, self).is_update_necessary(
            existing_resource_dict
        )


class CloudVmClusterHelperCustom:

    # We chose to exclude attribute `hostname` for sake of idempotency. API creates Cloud VM cluster resource by
    # appending some random string to the value passed for attribute - `hostname`.
    # e.g.If we pass value as `hostname-example` API launches VM Cluster with hostname value as `hostname-example-pixd`
    # API randomizes hostname to avoid duplication.
    def get_exclude_attributes(self):
        exclude_attributes = super(
            CloudVmClusterHelperCustom, self
        ).get_exclude_attributes()
        return exclude_attributes + [
            "hostname",
        ]


class CloudVmClusterIormConfigHelperCustom:
    def is_update_necessary(self, existing_resource_dict):
        existing_db_plans_list = existing_resource_dict["db_plans"]
        update_db_plans_list = self.module.params.get("db_plans", None)

        if update_db_plans_list is not None:

            for update_db_plan in update_db_plans_list:
                is_update_db_plan_available = False
                for existing_db_plan in existing_db_plans_list:
                    if update_db_plan["db_name"] == existing_db_plan["db_name"]:
                        if update_db_plan["share"] != existing_db_plan["share"]:
                            return True
                        is_update_db_plan_available = True
                if not is_update_db_plan_available:
                    return True

        return super(CloudVmClusterIormConfigHelperCustom, self).is_update_necessary(
            existing_resource_dict
        )

    def get_update_model_dict_for_idempotence_check(self, update_model):
        update_model_dict = super(
            CloudVmClusterIormConfigHelperCustom, self
        ).get_update_model_dict_for_idempotence_check(update_model)
        update_model_dict.pop("db_plans", None)
        return update_model_dict


class DbSystemActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        db_system = resource or self.get_resource().data
        if action == "migrate_exadata_db_system_resource_model":
            if db_system.lifecycle_state == "MIGRATED":
                return False
        return super(DbSystemActionsHelperCustom, self).is_action_necessary(
            action, resource
        )


class DatabaseSoftwareImageHelperCustom:
    def get_default_module_wait_timeout(self):
        return int(1 * 2400)


class DatabaseActionsHelperCustom:
    # mapping actions - precheck, upgrade, rollback to upgrade method.
    def get_action_fn(self, action):
        if action == "precheck" or action == "upgrade" or action == "rollback":
            self.module.params["action"] = action.upper()
            return getattr(self, "upgrade", None)
        return super(DatabaseActionsHelperCustom, self).get_action_fn(action)

    # to decide if database upgrade is necessary or not we need to compare database version from DB home or Database
    # software image.
    def is_action_necessary(self, action, resource=None):
        database_resource = resource or self.get_resource().data
        if action == "upgrade":
            database = to_dict(database_resource)
            db_home_id = database["db_home_id"]
            db_home_resource = oci_common_utils.call_with_backoff(
                self.client.get_db_home, db_home_id=db_home_id,
            )
            db_home = to_dict(db_home_resource.data)

            if self.module.params.get(
                "database_upgrade_source_details"
            ) and self.module.params.get("database_upgrade_source_details").get(
                "source"
            ):
                if self.module.params.get("database_upgrade_source_details").get(
                    "source"
                ) == "DB_VERSION" and self.module.params.get(
                    "database_upgrade_source_details"
                ).get(
                    "db_version"
                ):

                    db_version = self.module.params.get(
                        "database_upgrade_source_details"
                    ).get("db_version")
                    if db_version == db_home["db_version"]:
                        return False
                    return True

                if self.module.params.get("database_upgrade_source_details").get(
                    "source"
                ) == "DB_SOFTWARE_IMAGE" and self.module.params.get(
                    "database_upgrade_source_details"
                ).get(
                    "database_software_image_id"
                ):
                    database_software_image_id = self.module.params.get(
                        "database_upgrade_source_details"
                    ).get("database_software_image_id")

                    if (
                        database["database_software_image_id"]
                        and database["database_software_image_id"]
                        == database_software_image_id
                    ):
                        return False
                    return True

                if self.module.params.get("database_upgrade_source_details").get(
                    "source"
                ) == "DB_HOME" and self.module.params.get(
                    "database_upgrade_source_details"
                ).get(
                    "db_home_id"
                ):
                    if (
                        self.module.params.get("database_upgrade_source_details").get(
                            "db_home_id"
                        )
                        == db_home["id"]
                    ):
                        return False
                    return True
        return super(DatabaseActionsHelperCustom, self).is_action_necessary(
            action, resource
        )
