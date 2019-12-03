# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from ansible.module_utils.oracle import oci_utils
from ansible.module_utils._text import to_bytes

try:
    from oci.database.models import (
        PatchDetails,
        CreateDatabaseDetails,
        DbBackupConfig,
        CreateDatabaseFromBackupDetails,
    )
    from oci.exceptions import ClientError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def is_version_changed(
    patch_history_entry_getter_method,
    patch_getter_method,
    current_version,
    input_version_dict,
    last_patch_history_entry_id,
    **kwargs
):
    version_changed = False
    patch_details = None
    if is_patch_already_applied(
        patch_getter_method, current_version, input_version_dict, **kwargs
    ):
        return version_changed, patch_details

    if last_patch_history_entry_id is None:
        patch_details = get_patch_details_from_version(input_version_dict)
        return True, patch_details

    kwargs.update(patch_history_entry_id=last_patch_history_entry_id)
    last_patch_history = oci_utils.call_with_backoff(
        patch_history_entry_getter_method, **kwargs
    ).data
    if input_version_dict.get("patch_id") != last_patch_history.patch_id:
        patch_details = get_patch_details_from_version(input_version_dict)
        return True, patch_details
    else:
        input_action = input_version_dict.get("action")
        if (
            not (
                last_patch_history.action == "APPLY"
                and last_patch_history.lifecycle_state == "SUCCEEDED"
            )
            and last_patch_history.action != input_action
            or last_patch_history.lifecycle_state != "SUCCEEDED"
        ):
            patch_details = get_patch_details_from_version(input_version_dict)
            return True, patch_details

    return version_changed, patch_details


def is_patch_already_applied(
    patch_getter_method, current_version, input_version_dict, **kwargs
):
    if input_version_dict is None:
        return True
    patch_id = input_version_dict.get("patch_id")
    kwargs.update(patch_id=patch_id)
    existing_patch = oci_utils.call_with_backoff(patch_getter_method, **kwargs).data
    if existing_patch is None:
        raise ClientError(Exception("No Patch with id " + patch_id + " is available"))
    if existing_patch.version != current_version:
        return False
    return True


def get_patch_details_from_version(input_version_dict):
    patch_details = PatchDetails()
    for attribute in patch_details.attribute_map.keys():
        patch_details.__setattr__(attribute, input_version_dict.get(attribute, None))
    return patch_details


def create_database_details(database_dict):
    if database_dict is None:
        raise ClientError(
            Exception(
                "Proper value for attribute database is mandatory for creating this component"
            )
        )
    create_database_details = CreateDatabaseDetails()
    for attribute in create_database_details.attribute_map.keys():
        if attribute != "db_backup_config":
            create_database_details.__setattr__(
                attribute, database_dict.get(attribute, None)
            )
    input_db_backup_config = database_dict.get("db_backup_config")
    if input_db_backup_config is not None:
        db_backup_config = DbBackupConfig()
        db_backup_config.auto_backup_enabled = input_db_backup_config.get(
            "auto_backup_enabled"
        )
        create_database_details.db_backup_config = db_backup_config

    return create_database_details


def create_database_from_backup_details(database_dict):
    if database_dict is None:
        raise ClientError(
            Exception(
                "Proper value for attribute database is mandatory for creating this component"
            )
        )
    create_database_from_backup_details = CreateDatabaseFromBackupDetails()
    for attribute in create_database_from_backup_details.attribute_map.keys():
        create_database_from_backup_details.__setattr__(
            attribute, database_dict.get(attribute, None)
        )

    return create_database_from_backup_details


def execute_function_and_wait(
    resource_type,
    client,
    function,
    kwargs_function,
    get_fn,
    get_param,
    module,
    states=None,
    kwargs_get=None,
):
    return oci_utils.create_and_wait(
        resource_type=resource_type,
        create_fn=function,
        kwargs_create=kwargs_function,
        client=client,
        get_fn=get_fn,
        get_param=get_param,
        module=module,
        kwargs_get=kwargs_get,
        states=states,
    )


def write_stream_to_file(data, file):
    with open(to_bytes(file), "wb") as f:
        for d in data:
            f.write(d)
    return True
