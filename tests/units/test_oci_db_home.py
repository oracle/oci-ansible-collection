# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_db_home
from ansible.module_utils.oracle import oci_db_utils, oci_utils


try:
    import oci
    from oci.util import to_dict
    from oci.database.models import DbHome, PatchDetails, DbSystem
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_db_home.py requires `oci` module")


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
def oci_wait_until_patch(mocker):
    return mocker.patch.object(oci, "wait_until")


@pytest.fixture()
def get_existing_db_home_patch(mocker):
    return mocker.patch.object(oci_db_home, "get_existing_db_home")


@pytest.fixture()
def create_db_home_patch(mocker):
    return mocker.patch.object(oci_db_home, "create_db_home")


@pytest.fixture()
def update_db_home_patch(mocker):
    return mocker.patch.object(oci_db_home, "update_db_home")


@pytest.fixture()
def oci_db_utils_is_version_changed_patch(mocker):
    return mocker.patch.object(oci_db_utils, "is_version_changed")


@pytest.fixture()
def check_and_create_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_create_resource")


@pytest.fixture()
def create_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "create_and_wait")


@pytest.fixture()
def update_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "update_and_wait")


@pytest.fixture()
def delete_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "delete_and_wait")


@pytest.fixture()
def get_existing_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "get_existing_resource")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_db_home.set_logger(logging)


def test_create_or_update_db_home_create(
    db_client, get_existing_resource_patch, check_and_create_resource_patch
):
    module = get_module(dict({"db_home_id": None}))
    db_system = DbSystem()
    db_system.compartment_id = "ocid1.compartment..xxx"
    db_home = get_db_home()
    get_existing_resource_patch.return_value = db_system
    check_and_create_resource_patch.return_value = {
        "db_home": to_dict(db_home),
        "changed": True,
    }
    result = oci_db_home.create_or_update_db_home(db_client, module)
    assert result["db_home"]["display_name"] is db_home.display_name


def test_create_or_update_db_home_update(db_client, update_db_home_patch):
    module = get_module(dict({"db_home_id": "ocid1.dbsystem.aaa"}))
    db_home = get_db_home()
    update_db_home_patch.return_value = {"db_home": to_dict(db_home), "changed": True}
    result = oci_db_home.create_or_update_db_home(db_client, module)
    assert result["db_home"]["display_name"] is db_home.display_name


def test_create_or_update_db_home_client_error(
    db_client, check_and_create_resource_patch
):
    error_message = "databse attribute has no value"
    module = get_module(dict())
    check_and_create_resource_patch.side_effect = ClientError(Exception(error_message))
    try:
        oci_db_home.create_or_update_db_home(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_db_home_service_error(
    db_client, check_and_create_resource_patch
):
    error_message = "Internal Server Error"
    module = get_module(dict())
    check_and_create_resource_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_db_home.create_or_update_db_home(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_db_home_source_none(db_client, create_and_wait_patch):
    module = get_module(dict())
    db_home = get_db_home()
    create_and_wait_patch.return_value = {"db_home": to_dict(db_home), "changed": True}
    result = oci_db_home.create_db_home(db_client, module)
    assert result["db_home"]["display_name"] is db_home.display_name


def test_create_db_home_source_db_backup(db_client, create_and_wait_patch):
    module = get_module(
        dict(
            {
                "database": {
                    "backup_id": "ocid1.backup.oc1.phx.abu",
                    "backup_tde_password ": "BEstr0ng_#1",
                    "admin_password": "BEstr0ng_#1",
                },
                "source": "DB_BACKUP",
            }
        )
    )
    db_home = get_db_home()
    create_and_wait_patch.return_value = {"db_home": to_dict(db_home), "changed": True}
    result = oci_db_home.create_db_home(db_client, module)
    assert result["db_home"]["display_name"] is db_home.display_name


def test_update_db_home_version_changed(
    db_client, update_db_home_patch, oci_db_utils_is_version_changed_patch
):
    module = get_module(dict())
    db_home = get_db_home()
    oci_db_utils_is_version_changed_patch.return_value = True, PatchDetails()
    update_db_home_patch.return_value = {"db_home": to_dict(db_home), "changed": True}
    result = oci_db_home.update_db_home(db_client, module, "ocid1.dbhome.aaaa")
    assert result["db_home"]["display_name"] is db_home.display_name


def test_update_db_home_client_error_no_db_home(db_client, get_existing_resource_patch):
    error_message = "No DB Home"
    module = get_module(dict())
    get_existing_resource_patch.return_value = None
    try:
        oci_db_home.update_db_home(db_client, module, "ocid1.dbhome.aaaa")
    except Exception as ex:
        assert error_message in str(ex.args)


def test_delete_db_home(db_client, delete_and_wait_patch):
    module = get_module(dict({"db_home_id": "ocid1.dbhome.aaa"}))
    db_home = get_db_home()
    delete_and_wait_patch.return_value = {"db_home": to_dict(db_home), "changed": True}
    result = oci_db_home.delete_db_home(db_client, module)
    assert result["db_home"]["display_name"] is db_home.display_name


def get_db_home():
    db_home = DbHome()
    db_home.display_name = "ansibledbhome"
    return db_home


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = {
        "db_system_id": "ocid1.dbsystem.oc1",
        "db_home_id": "ocid1.dbhome.aaaa",
        "database": {
            "admin_password": "BEstr0ng_#1",
            "character_set": "AL32UTF8",
            "db_backup_config": {"auto_backup_enabled": False},
            "db_name": "testdb",
            "db_workload": "OLTP",
            "ncharacter_set": "AL16UTF16",
        },
        "display_name": "ansibledbhome",
        "source": "NONE",
        "db_version": "12.0.0.1",
    }
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
