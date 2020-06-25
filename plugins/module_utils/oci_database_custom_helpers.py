# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
from ansible.module_utils._text import to_bytes
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.exceptions import ServiceError

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


class AutonomousDatabaseActionsHelperCustom:
    REGISTER_AUTONOMOUS_DATABASE_DATA_SAFE = "register_autonomous_database_data_safe"
    DEREGISTER_AUTONOMOUS_DATABASE_DATA_SAFE = (
        "deregister_autonomous_database_data_safe"
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
