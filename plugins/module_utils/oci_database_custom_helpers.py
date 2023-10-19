# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
    oci_config_utils,
    oci_wait_utils,
)


try:
    from oci.core import VirtualNetworkClient
    from oci.database.models import ModifyDatabaseManagementDetails
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False
import logging

logger = logging.getLogger(__name__)


def get_db_management_status(resource):
    if not resource:
        return None
    if not hasattr(resource, "database_management_config"):
        return None
    if not hasattr(resource.database_management_config, "database_management_status"):
        return None
    return resource.database_management_config.database_management_status


def get_opsi_status(resource):
    if not resource:
        return None
    if not hasattr(resource, "operations_insights_config"):
        return None
    if not hasattr(resource.operations_insights_config, "operations_insights_status"):
        return None
    return resource.operations_insights_config.operations_insights_status


class AutonomousDatabaseRegionalWalletHelperCustom:
    def is_update(self):
        return True


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
    CONFIGURE_AUTONOMOUS_DATABASE_VAULT_KEY = "configure_autonomous_database_vault_key"

    def generate_autonomous_database_wallet(self):
        wallet_file = self.module.params.get("wallet_file")
        try:
            if wallet_file is None or len(wallet_file.strip()) == 0:
                self.module.fail_json(msg="Wallet file must be declared")

            if self.module.params.get("force") or not os.path.isfile(
                to_bytes(wallet_file)
            ):
                super(
                    AutonomousDatabaseActionsHelperCustom, self
                ).generate_autonomous_database_wallet()

            else:
                self.module.fail_json(
                    msg="Wallet file  %s already exists. Use force option to overwrite."
                    % wallet_file
                )
        except ServiceError as ex:
            self.module.fail_json(msg=ex.message)

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
        elif action == self.CONFIGURE_AUTONOMOUS_DATABASE_VAULT_KEY:
            if hasattr(resource, "kms_key_id") and hasattr(resource, "vault_id"):
                if (
                    self.module.params.get("kms_key_id")
                    and self.module.params["kms_key_id"] != resource.kms_key_id
                ):
                    return True
                if (
                    self.module.params.get("vault_id")
                    and self.module.params["vault_id"] != resource.vault_id
                ):
                    return True
                return False
            return True
        else:
            return super(
                AutonomousDatabaseActionsHelperCustom, self
            ).is_action_necessary(action, resource)


class AutonomousDatabaseBackupHelperCustom:
    def is_create(self):
        return True


# Handling idempotency logic
class ExternalContainerDatabaseActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        db_mgt_status = get_db_management_status(resource)
        logger.debug("EC Resource details {0} {1}".format(db_mgt_status, action))
        if action == "enable_external_container_database_database_management":
            if db_mgt_status == "ENABLED":
                return False
            elif db_mgt_status == "NOT_ENABLED":
                return True
            else:
                return True
        elif action == "disable_external_container_database_database_management":
            if db_mgt_status == "NOT_ENABLED":
                return False
            elif db_mgt_status == "ENABLED":
                return True
            else:
                return False
        else:
            return super(
                ExternalContainerDatabaseActionsHelperCustom, self
            ).is_action_necessary(action, resource)


# Handling idempotency logic
class ExternalPluggableDatabaseActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        db_mgt_status = get_db_management_status(resource)
        logger.debug(
            "EPC Resource details for db_mgt flag {0} {1}".format(db_mgt_status, action)
        )
        opsi_status = get_opsi_status(resource)
        logger.debug(
            "EPC Resource details for opsi flag {0} {1}".format(opsi_status, action)
        )
        if action == "enable_external_pluggable_database_database_management":
            if db_mgt_status == "ENABLED":
                return False
            elif db_mgt_status == "NOT_ENABLED":
                return True
            else:
                return True
        elif action == "disable_external_pluggable_database_database_management":
            if db_mgt_status == "NOT_ENABLED":
                return False
            elif db_mgt_status == "ENABLED":
                return True
            else:
                return False
        elif action == "enable_external_pluggable_database_operations_insights":
            if opsi_status == "ENABLED":
                return False
            elif opsi_status == "NOT_ENABLED":
                return True
            else:
                return True
        elif action == "disable_external_pluggable_database_operations_insights":
            if opsi_status == "NOT_ENABLED":
                return False
            elif opsi_status == "ENABLED":
                return True
            else:
                return False
        else:
            return super(
                ExternalPluggableDatabaseActionsHelperCustom, self
            ).is_action_necessary(action, resource)


# Handling idempotency logic
class ExternalNonContainerDatabaseActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        db_mgt_status = get_db_management_status(resource)
        logger.debug(
            "ENC Resource details for db_mgt {0} {1}".format(db_mgt_status, action)
        )
        opsi_status = get_opsi_status(resource)
        logger.debug(
            "ENC Resource details for opsi {0} {1}".format(opsi_status, action)
        )
        if action == "enable_external_non_container_database_database_management":
            if db_mgt_status == "ENABLED":
                return False
            elif db_mgt_status == "NOT_ENABLED":
                return True
            else:
                return True
        elif action == "disable_external_non_container_database_database_management":
            if db_mgt_status == "NOT_ENABLED":
                return False
            elif db_mgt_status == "ENABLED":
                return True
            else:
                return False
        elif action == "enable_external_non_container_database_operations_insights":
            if opsi_status == "ENABLED":
                return False
            elif opsi_status == "NOT_ENABLED":
                return True
            else:
                return True
        elif action == "disable_external_non_container_database_operations_insights":
            if opsi_status == "NOT_ENABLED":
                return False
            elif opsi_status == "ENABLED":
                return True
            else:
                return False
        else:
            return super(
                ExternalNonContainerDatabaseActionsHelperCustom, self
            ).is_action_necessary(action, resource)


class DbSystemHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        if "data_storage_size_in_gbs" in module.params.keys():
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

    def get_exclude_attributes(self):
        # data_storage_size_in_gbs is there in
        exclude_attributes = super(DbSystemHelperCustom, self).get_exclude_attributes()

        remove_exclude_attributes = ["data_storage_size_in_gbs"]
        exclude_attributes = [
            x for x in exclude_attributes if x not in remove_exclude_attributes
        ]

        return exclude_attributes

    def get_update_model_dict_for_idempotence_check(self, update_model):
        update_model_dict = super(
            DbSystemHelperCustom, self
        ).get_update_model_dict_for_idempotence_check(update_model)

        # version only applies to patching and has custom idempotence logic which is handled in
        # is_update_necessary
        update_model_dict.pop("version", None)

        return update_model_dict

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
        super_result = super(DbHomeHelperCustom, self).is_update_necessary(resource)
        if super_result:
            return True
        update_model = self.get_update_model()
        current_version = resource.get("db_version")
        if not getattr(update_model, "db_version", None):
            return False
        patch_details = update_model.db_version
        if getattr(patch_details, "database_software_image_id", None):
            database_software_image = oci_common_utils.call_with_backoff(
                self.client.get_database_software_image,
                database_software_image_id=patch_details.database_software_image_id,
            ).data
            if (
                getattr(database_software_image, "database_version", None)
                != current_version
            ):
                logger.debug(
                    "DB system version {current_version} does not match database software image version: {patch_version}. "
                    "Applying patch.".format(
                        current_version=current_version,
                        patch_version=getattr(
                            database_software_image, "database_version", None
                        ),
                    )
                )
                return True
            return False
        elif getattr(patch_details, "patch_id", None):
            patch = oci_common_utils.call_with_backoff(
                self.client.get_db_home_patch,
                db_home_id=resource.get("id"),
                patch_id=getattr(patch_details, "patch_id"),
            ).data
            if patch.version != current_version:
                logger.debug(
                    "DB system version {current_version} does not match patch version: {patch_version}. "
                    "Applying patch.".format(
                        current_version=current_version, patch_version=patch.version,
                    )
                )
                return True
            return False

        return True


class DataGuardAssociationHelperCustom:
    def get_module_resource_id(self):
        return None

    def get_module_resource_id_param(self):
        return None

    def get_fn(self, data_guard_association_id):
        return self.client.get_data_guard_association(
            data_guard_association_id=data_guard_association_id,
            database_id=self.module.params["database_id"],
        )

    def get_get_fn(self):
        return self.get_fn
        # return self.client.get_data_guard_association


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
            logger.debug(
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
    ACTIVATE_ACTION_KEY = "activate"

    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        if self.module.params.get("action") == self.ACTIVATE_ACTION_KEY:
            if getattr(resource, "lifecycle_state", None) == "ACTIVE":
                return False
            return True
        return super(
            ExadataInfrastructureActionsHelperCustom, self
        ).is_action_necessary(action, resource)


class AutonomousExadataInfrastructureHelperCustom:
    # resource `AutonomousExadataInfrastructure` has attribute `maintenance_window` which gives the scheduling details for
    # the quarterly maintenance window. However object `UpdateAutonomousExadataInfrastructure` represents it with different
    # name 'maintenance_window_details'.
    def is_update_necessary(self, existing_resource_dict):
        resource_dict = dict(existing_resource_dict)
        resource_dict["maintenance_window_details"] = resource_dict.pop(
            "maintenance_window", None
        )
        return super(
            AutonomousExadataInfrastructureHelperCustom, self
        ).is_update_necessary(resource_dict)


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

        # removing this because the name in response model is maintenance_window
        # which is handled in get_existing_resource_dict_for_idempotence_check
        # in order to compare this parameter for idempotency check
        remove_exclude_attributes = ["maintenance_window_details"]
        exclude_attributes = [
            x for x in exclude_attributes if x not in remove_exclude_attributes
        ]

        return exclude_attributes


class VmClusterNetworkHelperCustom:
    def get_fn(self, vm_cluster_network_id):
        return self.client.get_vm_cluster_network(
            vm_cluster_network_id=vm_cluster_network_id,
            exadata_infrastructure_id=self.module.params.get(
                "exadata_infrastructure_id"
            ),
        )

    def get_get_fn(self):
        return self.get_fn

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


class VmClusterHelperCustom:
    def get_create_model_dict_for_idempotence_check(self, create_model):
        model_dict = super(
            VmClusterHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)

        if model_dict.get("cpu_core_count"):
            model_dict["cpus_enabled"] = model_dict["cpu_core_count"]
            del model_dict["cpu_core_count"]

        return model_dict

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
    # Parent method returns the attribute_map of create model which has only database attribute in it.
    # Due to that, child params of database attibute are not considered for create idempotence. So overriding
    # this method to include child params of database attribute to be considered for idempotence.
    def get_attributes_to_consider_for_create_idempotency_check(self, create_model):
        attributes_to_consider = super(
            DatabaseHelperCustom, self
        ).get_attributes_to_consider_for_create_idempotency_check(create_model)
        attributes_to_consider.pop("database", None)

        database_attribute_map = create_model.database.attribute_map

        for attr in database_attribute_map:
            if attr not in ["backup_id", "backup_tde_password", "admin_password"]:
                attributes_to_consider[attr] = database_attribute_map[attr]
        return attributes_to_consider

    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            DatabaseHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        for k, v in six.iteritems(create_model_dict.pop("database", dict())):
            if k not in ["backup_id", "backup_tde_password", "admin_password"]:
                create_model_dict[k] = v
        return create_model_dict

    def get_exclude_attributes(self):
        exclude_attributes = super(DatabaseHelperCustom, self).get_exclude_attributes()

        # model returned by GetDatabase operation doesn't have attribute `kms_key_version_id` & `tde_wallet_password`
        # and we have populated it from the database param of the CreateDatabaseDetails
        # check get_create_model_dict_for_idempotence_check
        exclude_attributes = exclude_attributes + [
            "tde_wallet_password",
        ]

        # this is already removed in the get_create_model_dict_for_idempotence_check
        # populating additional information
        remove_exclude_attributes = ["database"]
        exclude_attributes = [
            x for x in exclude_attributes if x not in remove_exclude_attributes
        ]

        return exclude_attributes


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
    # The gi_version also does not match with what is used when creating. For ex: 19.0.0.0 is used for create but
    # stored in the resource as 19.9.0.0.0. Tried with the version that is in the resource and that did not work.
    def get_exclude_attributes(self):
        exclude_attributes = super(
            CloudVmClusterHelperCustom, self
        ).get_exclude_attributes()
        return exclude_attributes + [
            "hostname",
            "gi_version",
        ]


class VmClusterActionsHelperCustom:
    ADD_VIRTUAL_MACHINE_ACTION = "add_virtual_machine"
    REMOVE_VIRTUAL_MACHINE_ACTION = "remove_virtual_machine"

    def is_action_necessary(self, action, resource=None):
        resource_dict = to_dict(resource)
        if action.lower() == self.ADD_VIRTUAL_MACHINE_ACTION:
            db_servers_list = self.module.params.get("db_servers")
            source_list = [item.get("db_server_id") for item in db_servers_list]
            target_list = resource_dict.get("db_servers")
            if all(
                [
                    oci_common_utils.is_in_list(target_list, element)
                    for element in source_list
                ]
            ):
                return False
            return True
        elif action.lower() == self.REMOVE_VIRTUAL_MACHINE_ACTION:
            db_servers_list = self.module.params.get("db_servers")
            source_list = [item.get("db_server_id") for item in db_servers_list]
            target_list = resource_dict.get("db_servers")
            if any(
                [
                    oci_common_utils.is_in_list(target_list, element)
                    for element in source_list
                ]
            ):
                return True
            return False
        return super(VmClusterActionsHelperCustom, self).is_action_necessary(
            action, resource
        )


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


class DbSystemActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        db_system = resource or self.get_resource().data
        if action == "migrate_exadata_db_system_resource_model":
            if db_system.lifecycle_state == "MIGRATED":
                return False
        return super(DbSystemActionsHelperCustom, self).is_action_necessary(
            action, resource
        )


class DatabaseActionsHelperCustom:
    UPGRADE_ACTION_KEY = "upgrade"
    DISABLE_DATABASE_MANAGEMENT_ACTION_KEY = "disable_database_management"
    ENABLE_DATABASE_MANAGEMENT_ACTION_KEY = "enable_database_management"
    MODIFY_DATABASE_MANAGEMENT_ACTION_KEY = "modify_database_management"

    # to decide if database upgrade is necessary or not we need to compare database version from DB home or Database
    # software image.
    def is_action_necessary(self, action, resource=None):
        if action == self.UPGRADE_ACTION_KEY:
            database = to_dict(resource)
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
        elif action == self.ENABLE_DATABASE_MANAGEMENT_ACTION_KEY:
            database_management_config = getattr(
                resource, "database_management_config", None
            )
            if database_management_config is None:
                return True
            if getattr(database_management_config, "management_status", None) in [
                "ENABLED",
                "ENABLING",
            ]:
                return False
            return True
        elif action == self.DISABLE_DATABASE_MANAGEMENT_ACTION_KEY:
            database_management_config = getattr(
                resource, "database_management_config", None
            )
            if database_management_config is None:
                return False
            if getattr(database_management_config, "management_status", None) in [
                "DISABLED",
                "DISABLING",
            ]:
                return False
            return True
        elif action == self.MODIFY_DATABASE_MANAGEMENT_ACTION_KEY:
            database_management_config = getattr(
                resource, "database_management_config", None
            )
            if database_management_config is None:
                return True
            action_details = oci_common_utils.convert_input_data_to_model_class(
                self.module.params, ModifyDatabaseManagementDetails
            )
            return not oci_common_utils.compare_dicts(
                source_dict=to_dict(action_details),
                target_dict=to_dict(database_management_config),
            )
        return super(DatabaseActionsHelperCustom, self).is_action_necessary(
            action, resource
        )


class DbNodeFactsHelperCustom:
    def __init__(self, *args, **kwargs):
        super(DbNodeFactsHelperCustom, self).__init__(*args, **kwargs)
        self.network_client = oci_config_utils.create_service_client(
            self.module, VirtualNetworkClient
        )

    def get(self, *args, **kwargs):
        db_node = super(DbNodeFactsHelperCustom, self).get(*args, **kwargs)
        add_primary_ip_info_to_db_node(db_node, self.network_client)
        return db_node

    def list(self, *args, **kwargs):
        db_nodes = super(DbNodeFactsHelperCustom, self).list(*args, **kwargs)
        for db_node in db_nodes:
            add_primary_ip_info_to_db_node(db_node, self.network_client)
        return db_nodes


def add_primary_ip_info_to_db_node(db_node, network_client):
    # vnic_id can be None if the db node is still in PROVISIONING state.
    if db_node and db_node.get("vnic_id"):
        vnic = oci_common_utils.call_with_backoff(
            network_client.get_vnic, vnic_id=db_node.get("vnic_id")
        ).data
        db_node["primary_private_ip"] = vnic.private_ip if vnic.is_primary else None
        db_node["primary_public_ip"] = vnic.public_ip if vnic.is_primary else None
    else:
        db_node["primary_private_ip"] = None
        db_node["primary_public_ip"] = None


class PluggableDatabaseActionsHelperCustom:
    STOP_ACTION_KEY = "stop"
    START_ACTION_KEY = "start"
    LOCAL_CLONE_ACTION_KEY = "local_clone"
    REMOTE_CLONE_ACTION_KEY = "remote_clone"

    def get_existing_pluggable_databases(self, container_database_id):
        return [
            pluggable_db
            for pluggable_db in oci_common_utils.list_all_resources(
                self.client.list_pluggable_databases, database_id=container_database_id,
            )
            if getattr(pluggable_db, "lifecycle_state", None)
            not in oci_common_utils.DEAD_STATES
        ]

    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        if action == self.STOP_ACTION_KEY:
            # https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/PluggableDatabase/StopPluggableDatabase
            if getattr(resource, "open_mode", None) == "MOUNTED":
                return False
            return True
        if action == self.START_ACTION_KEY:
            # https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/PluggableDatabase/StartPluggableDatabase
            if getattr(resource, "open_mode", None) == "READ_WRITE":
                return False
            return True
        if action == self.LOCAL_CLONE_ACTION_KEY:
            existing_pluggable_databases = self.get_existing_pluggable_databases(
                getattr(resource, "container_database_id", None)
            )
            for existing_pluggable_database in existing_pluggable_databases:
                if getattr(
                    existing_pluggable_database, "pdb_name", None
                ) == self.module.params.get("cloned_pdb_name"):
                    return False
            return True
        if action == self.REMOTE_CLONE_ACTION_KEY:
            existing_pluggable_databases = self.get_existing_pluggable_databases(
                self.module.params.get("target_container_database_id")
            )
            for existing_pluggable_database in existing_pluggable_databases:
                if getattr(
                    existing_pluggable_database, "pdb_name", None
                ) == self.module.params.get("cloned_pdb_name"):
                    return False
            return True
        return super(PluggableDatabaseActionsHelperCustom, self).is_action_necessary(
            action, resource
        )


class AutonomousDatabaseHelperCustom:
    def get_create_model(self):
        source = self.module.params.get("source")
        if source == "BACKUP_FROM_TIMESTAMP":
            source_autonomous_database_id = self.module.params.get(
                "source_autonomous_database_id",
            )
            create_model = super(
                AutonomousDatabaseHelperCustom, self
            ).get_create_model()
            setattr(
                create_model, "autonomous_database_id", source_autonomous_database_id
            )
            return create_model

        return super(AutonomousDatabaseHelperCustom, self).get_create_model()
