# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_database
from ansible.module_utils.oracle import oci_utils, oci_db_utils

try:
    import oci
    from oci.util import to_dict
    from oci.database.models import Database, DbBackupConfig
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_database.py requires `oci` module")


class FakeModule(object):
    def __init__(self, **kwargs):
        self.params = kwargs

    def fail_json(self, *args, **kwargs):
        self.exit_args = args
        self.exit_kwargs = kwargs
        raise Exception(kwargs["msg"])

    def exit_json(self, *args, **kwargs):
        self.exit_args = args
        self.exit_kwargs = kwargs


@pytest.fixture()
def db_client(mocker):
    mock_db_client = mocker.patch("oci.database.database_client.DatabaseClient")
    return mock_db_client.return_value


@pytest.fixture()
def get_existing_database_patch(mocker):
    return mocker.patch.object(oci_database, "get_existing_database")


@pytest.fixture()
def update_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "update_and_wait")


@pytest.fixture()
def execute_function_and_wait_patch(mocker):
    return mocker.patch.object(oci_db_utils, "execute_function_and_wait")


@pytest.fixture()
def get_existing_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "get_existing_resource")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_database.set_logger(logging)


def test_restore_database(db_client, execute_function_and_wait_patch):
    module = get_module(dict())
    database = get_database()
    execute_function_and_wait_patch.return_value = {
        "database": to_dict(database),
        "changed": True,
    }
    result = oci_database.restore_database(db_client, module)
    assert result["database"]["db_name"] is database.db_name


def test_restore_database_service_error(db_client, execute_function_and_wait_patch):
    error_message = "Internal Server Error"
    module = get_module(dict())
    execute_function_and_wait_patch.return_value = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        result = oci_database.restore_database(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_update_database_db_backup_config_changed(
    db_client, get_existing_resource_patch, update_and_wait_patch
):
    module = get_module(dict({"db_backup_config": {"auto_backup_enabled": True}}))
    database = get_database()
    get_existing_resource_patch.return_value = database
    update_and_wait_patch.return_value = {
        "database": to_dict(database),
        "changed": True,
    }
    result = oci_database.update_database(db_client, module)
    assert result["changed"] is True


def test_update_database_freeform_tags_changed(
    db_client, get_existing_resource_patch, update_and_wait_patch
):
    module = get_module(dict(freeform_tags=dict(database_type="payroll")))
    database = get_database()
    get_existing_resource_patch.return_value = database
    update_and_wait_patch.return_value = {
        "database": to_dict(database),
        "changed": True,
    }
    result = oci_database.update_database(db_client, module)
    assert result["changed"] is True


def test_update_database_defined_tags_changed(
    db_client, get_existing_resource_patch, update_and_wait_patch
):
    module = get_module(dict(defined_tags=dict(usert_type=dict(department="employee"))))
    database = get_database()
    get_existing_resource_patch.return_value = database
    update_and_wait_patch.return_value = {
        "database": to_dict(database),
        "changed": True,
    }
    result = oci_database.update_database(db_client, module)
    assert result["changed"] is True


def test_update_database_no_change(db_client, get_existing_resource_patch):
    module = get_module(dict())
    database = get_database()
    get_existing_resource_patch.return_value = database
    result = oci_database.update_database(db_client, module)
    assert result["changed"] is False


def test_update_database_no_database_for_update(db_client, get_existing_resource_patch):
    error_message = "No Database"
    module = get_module(dict({"db_backup_config": {"auto_backup_enabled": True}}))
    get_existing_resource_patch.return_value = None
    try:
        oci_database.update_database(db_client, module)
    except Exception as ex:
        assert error_message in str(ex.args)


def test_update_database_service_error(
    db_client, get_existing_resource_patch, update_and_wait_patch
):
    error_message = "Internal Server Error"
    database = get_database()
    module = get_module(dict({"db_backup_config": {"auto_backup_enabled": True}}))
    get_existing_resource_patch.return_value = database
    update_and_wait_patch.return_value = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_database.update_database(db_client, module)
    except Exception as ex:
        assert error_message in str(ex.args)


def get_database():
    database = Database()
    db_backup_config = DbBackupConfig()
    db_backup_config.auto_backup_enabled = False
    database.db_name = "ansibledb"
    database.db_backup_config = db_backup_config
    database.freeform_tags = {"database_type": "attendance"}
    database.defined_tags = {"user_type": {"department": "educational"}}
    return database


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = {
        "database_id": "ocid1.database.oc1",
        "db_backup_config": {"auto_backup_enabled": False},
        "latest": True,
    }
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
