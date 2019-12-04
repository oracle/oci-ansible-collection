# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_autonomous_database
from ansible.module_utils.oracle import oci_utils, oci_db_utils
import tempfile
import os


try:
    import oci
    from oci.util import to_dict
    from oci.database.models import AutonomousDatabase
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_autonomous_database.py requires `oci` module")


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
def check_and_create_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_create_resource")


@pytest.fixture()
def update_autonomous_database_patch(mocker):
    return mocker.patch.object(oci_autonomous_database, "update_autonomous_database")


@pytest.fixture()
def check_and_update_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_update_resource")


@pytest.fixture()
def create_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "create_and_wait")


@pytest.fixture()
def get_existing_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "get_existing_resource")


@pytest.fixture()
def delete_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "delete_and_wait")


@pytest.fixture()
def execute_function_and_wait_patch(mocker):
    return mocker.patch.object(oci_db_utils, "execute_function_and_wait")


@pytest.fixture()
def call_with_backoff_patch(mocker):
    return mocker.patch.object(oci_utils, "call_with_backoff")


@pytest.fixture()
def write_stream_to_file_patch(mocker):
    return mocker.patch.object(oci_db_utils, "write_stream_to_file")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_autonomous_database.set_logger(logging)


def test_create_or_update_autonomous_database_create(
    db_client, check_and_create_resource_patch
):
    module = get_module()
    autonomous_database = get_autonomous_database()
    check_and_create_resource_patch.return_value = {
        "autonomous_database": to_dict(autonomous_database),
        "changed": True,
    }
    result = oci_autonomous_database.create_or_update_autonomous_database(
        db_client, module
    )
    assert (
        result["autonomous_database"]["display_name"]
        is autonomous_database.display_name
    )


def test_create_or_update_autonomous_database_update(
    db_client, update_autonomous_database_patch
):
    module = get_module(
        dict({"autonomous_database_id": "ocid1.autonomous_database.aaa"})
    )
    autonomous_database = get_autonomous_database()
    update_autonomous_database_patch.return_value = {
        "autonomous_database": to_dict(autonomous_database),
        "changed": True,
    }
    result = oci_autonomous_database.create_or_update_autonomous_database(
        db_client, module
    )
    assert (
        result["autonomous_database"]["display_name"]
        is autonomous_database.display_name
    )


def test_create_or_update_autonomous_database_client_error(
    db_client, check_and_create_resource_patch
):
    error_message = "database attribute has no value"
    module = get_module()
    check_and_create_resource_patch.side_effect = ClientError(Exception(error_message))
    try:
        oci_autonomous_database.create_or_update_autonomous_database(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_autonomous_database_service_error(
    db_client, check_and_create_resource_patch
):
    error_message = "Internal Server Error"
    module = get_module()
    check_and_create_resource_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_autonomous_database.create_or_update_autonomous_database(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_autonomous_database(db_client, create_and_wait_patch):
    module = get_module()
    autonomous_database = get_autonomous_database()
    create_and_wait_patch.return_value = {
        "autonomous_database": to_dict(autonomous_database),
        "changed": True,
    }
    result = oci_autonomous_database.create_autonomous_database(db_client, module)
    assert (
        result["autonomous_database"]["display_name"]
        is autonomous_database.display_name
    )


def test_update_autonomous_database_cpu_core_count(
    db_client, check_and_update_resource_patch
):
    autonomous_database = get_autonomous_database()
    autonomous_database.cpu_core_count = 4
    module = get_module(
        dict({"autonomous_database_id": "ocid1.autonomousdatabase.aaa"})
    )
    check_and_update_resource_patch.return_value = {
        "autonomous_database": to_dict(autonomous_database),
        "changed": True,
    }
    result = oci_autonomous_database.update_autonomous_database(db_client, module)
    assert result["changed"] is True


def test_update_autonomous_database_freeform_tags(
    db_client, check_and_update_resource_patch
):
    autonomous_database = get_autonomous_database()
    module = get_module(
        dict(
            freeform_tags=dict(system_type="oracledb"),
            autonomous_database_id="ocid1.autonomousdatabase.aaa",
        )
    )
    check_and_update_resource_patch.return_value = {
        "autonomous_database": to_dict(autonomous_database),
        "changed": True,
    }
    result = oci_autonomous_database.update_autonomous_database(db_client, module)
    assert result["changed"] is True


def test_update_autonomous_database_defined_tags(
    db_client, check_and_update_resource_patch
):
    autonomous_database = get_autonomous_database()
    module = get_module(
        dict(
            defined_tags=dict(system_strength=dict(shape="medium")),
            autonomous_database_id="ocid1.autonomousdatabase.aaa",
        )
    )
    check_and_update_resource_patch.return_value = {
        "autonomous_database": to_dict(autonomous_database),
        "changed": True,
    }
    result = oci_autonomous_database.update_autonomous_database(db_client, module)
    assert result["changed"] is True


def test_delete_autonomous_database(db_client, delete_and_wait_patch):
    module = get_module(dict(autonomous_database_id="ocid1.autonomousdatabase.aaa"))
    autonomous_database = get_autonomous_database()
    delete_and_wait_patch.return_value = {
        "autonomous_database": to_dict(autonomous_database),
        "changed": True,
    }
    result = oci_autonomous_database.delete_autonomous_database(db_client, module)
    assert (
        result["autonomous_database"]["display_name"]
        is autonomous_database.display_name
    )


def test_restore_autonomous_database(db_client, execute_function_and_wait_patch):
    autonomous_database = get_autonomous_database()
    module = get_module()
    execute_function_and_wait_patch.return_value = {
        "autonomous_database": to_dict(autonomous_database),
        "changed": True,
    }
    result = oci_autonomous_database.restore_autonomous_database(db_client, module)
    assert result["changed"] is True


def test_start_or_stop_autonomous_database_start(
    db_client, get_existing_resource_patch, execute_function_and_wait_patch
):
    autonomous_database = get_autonomous_database()
    autonomous_database.lifecycle_state = "STOPPED"
    get_existing_resource_patch.return_value = autonomous_database
    module = get_module(dict(state="start"))
    execute_function_and_wait_patch.return_value = {
        "autonomous_database": to_dict(autonomous_database),
        "changed": True,
    }
    result = oci_autonomous_database.start_or_stop_autonomous_database(
        db_client, module
    )
    assert result["changed"] is True


def test_start_or_stop_autonomous_database_start_idempotent(
    db_client, get_existing_resource_patch
):
    autonomous_database = get_autonomous_database()
    autonomous_database.lifecycle_state = "AVAILABLE"
    get_existing_resource_patch.return_value = autonomous_database
    module = get_module(dict(state="start"))
    result = oci_autonomous_database.start_or_stop_autonomous_database(
        db_client, module
    )
    assert result["changed"] is False


def test_start_or_stop_autonomous_database_stop(
    db_client, get_existing_resource_patch, execute_function_and_wait_patch
):
    autonomous_database = get_autonomous_database()
    autonomous_database.lifecycle_state = "AVAILABLE"
    get_existing_resource_patch.return_value = autonomous_database
    module = get_module(dict(state="stop"))
    execute_function_and_wait_patch.return_value = {
        "autonomous_database": to_dict(autonomous_database),
        "changed": True,
    }
    result = oci_autonomous_database.start_or_stop_autonomous_database(
        db_client, module
    )
    assert result["changed"] is True


def test_start_or_stop_autonomous_database_stop_idempotent(
    db_client, get_existing_resource_patch
):
    autonomous_database = get_autonomous_database()
    autonomous_database.lifecycle_state = "STOPPED"
    get_existing_resource_patch.return_value = autonomous_database
    module = get_module(dict(state="stop"))
    result = oci_autonomous_database.start_or_stop_autonomous_database(
        db_client, module
    )
    assert result["changed"] is False


def test_generate_wallet(
    db_client, call_with_backoff_patch, write_stream_to_file_patch
):
    call_with_backoff_patch.return_value = get_response(200, None, "test", None)
    write_stream_to_file_patch.return_value = True
    module = get_module(dict(password="password123", wallet_file="test_wallet_file"))
    result = oci_autonomous_database.generate_wallet(db_client, module)
    assert result["changed"] is True


def test_generate_wallet_no_wallet_file_defined(db_client):
    error_message = "Wallet file must be declared"
    module = get_module(dict(password="password123"))
    try:
        oci_autonomous_database.generate_wallet(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_generate_wallet_empty_wallet_file_defined(db_client):
    error_message = "Wallet file must be declared"
    module = get_module(dict(password="password123", wallet_file=" "))
    try:
        oci_autonomous_database.generate_wallet(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_generate_wallet_service_error(db_client, call_with_backoff_patch):
    error_message = "Internal Server Error"
    module = get_module(dict(password="password123", wallet_file="test_wallet_file"))
    call_with_backoff_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_autonomous_database.generate_wallet(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_generate_wallet_client_error(db_client, call_with_backoff_patch):
    error_message = "Wallet file not valid"
    module = get_module(dict(password="password123", wallet_file="test_wallet_file"))
    call_with_backoff_patch.side_effect = ClientError(Exception(error_message))
    try:
        oci_autonomous_database.generate_wallet(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def get_autonomous_database():
    autonomous_database = AutonomousDatabase()
    autonomous_database.display_name = "ansible_autonomous_databasee"
    autonomous_database.freeform_tags = {"system_type": "exadata"}
    autonomous_database.defined_tags = {"system_strength": {"shape": "small"}}
    return autonomous_database


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {
        "compartment_id": "ocid1.compartment.oc1..aaaaaaaaztglfq7tna6sygij2aoqxwkjvc4xnqtefqt5d4m4p3wpv6glmkwq",
        "admin_password": "BEstr0ng_#11",
        "data_storage_size_in_tbs": 1,
        "cpu_core_count": 1,
        "db_name": "ansibledb",
        "display_name": "ansibleautodb",
        "license_model": "LICENSE_INCLUDED",
        "wait": False,
        "freeform_tags": {"db_type": "test"},
    }
    if additional_properties:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
