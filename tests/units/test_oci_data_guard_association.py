# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_data_guard_association
from ansible.module_utils.oracle import oci_utils, oci_db_utils


try:
    import oci
    from oci.util import to_dict
    from oci.database.models import DataGuardAssociation
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
def get_existing_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "get_existing_resource")


@pytest.fixture()
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


@pytest.fixture()
def execute_function_and_wait_patch(mocker):
    return mocker.patch.object(oci_db_utils, "execute_function_and_wait")


@pytest.fixture()
def create_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "create_and_wait")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_data_guard_association.set_logger(logging)


def test_create_data_guard_association(db_client, create_and_wait_patch):
    module = get_module(dict())
    data_guard_association = get_data_guard_association("PRIMARY", "STANDBY")
    create_and_wait_patch.return_value = {
        "data_guard_association": to_dict(data_guard_association),
        "changed": True,
    }
    result = oci_data_guard_association.create_data_guard_association(db_client, module)
    assert result["data_guard_association"]["role"] is data_guard_association.role


def test_create_data_guard_association_service_error(db_client):
    error_message = "Internal Server Error"
    module = get_module(dict())
    db_client.create_data_guard_association.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_data_guard_association.create_data_guard_association(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_perform_data_guard_operations_switchover(
    db_client, get_existing_resource_patch, execute_function_and_wait_patch
):
    module = get_module(dict({"state": "switchover"}))
    data_guard_association = get_data_guard_association("PRIMARY", "STANDBY")
    get_existing_resource_patch.return_value = data_guard_association
    execute_function_and_wait_patch.return_value = {
        "data_guard_association": to_dict(data_guard_association),
        "changed": True,
    }
    result = oci_data_guard_association.perform_data_guard_operations(db_client, module)
    assert result["changed"] is True


def test_perform_data_guard_operations_switchover_on_standby_role(
    db_client, get_existing_resource_patch
):
    module = get_module(dict({"state": "switchover"}))
    data_guard_association = get_data_guard_association("STANDBY", "PRIMARY")
    get_existing_resource_patch.return_value = data_guard_association
    result = oci_data_guard_association.perform_data_guard_operations(db_client, module)
    assert result["changed"] is False


def test_perform_data_guard_operations_failover(
    db_client, get_existing_resource_patch, execute_function_and_wait_patch
):
    module = get_module(dict({"state": "failover"}))
    data_guard_association = get_data_guard_association("STANDBY", "PRIMARY")
    get_existing_resource_patch.return_value = data_guard_association
    execute_function_and_wait_patch.return_value = {
        "data_guard_association": to_dict(data_guard_association),
        "changed": True,
    }
    result = oci_data_guard_association.perform_data_guard_operations(db_client, module)
    assert result["changed"] is True


def test_perform_data_guard_operations_failover_on_primary_role(
    db_client, get_existing_resource_patch
):
    module = get_module(dict({"state": "failover"}))
    data_guard_association = get_data_guard_association("PRIMARY", "STANDBY")
    get_existing_resource_patch.return_value = data_guard_association
    result = oci_data_guard_association.perform_data_guard_operations(db_client, module)
    assert result["changed"] is False


def test_perform_data_guard_operations_reinstate(
    db_client, get_existing_resource_patch, execute_function_and_wait_patch
):
    module = get_module(dict({"state": "reinstate"}))
    data_guard_association = get_data_guard_association("DISABLED_STANDBY", "PRIMARY")
    get_existing_resource_patch.return_value = data_guard_association
    execute_function_and_wait_patch.return_value = {
        "data_guard_association": to_dict(data_guard_association),
        "changed": True,
    }
    result = oci_data_guard_association.perform_data_guard_operations(db_client, module)
    assert result["changed"] is True


def test_perform_data_guard_operations_reinstate_on_non_disable_standby_role(
    db_client, get_existing_resource_patch
):
    module = get_module(dict({"state": "reinstate"}))
    data_guard_association = get_data_guard_association("STANDBY", "PRIMARY")
    get_existing_resource_patch.return_value = data_guard_association
    result = oci_data_guard_association.perform_data_guard_operations(db_client, module)
    assert result["changed"] is False


def get_data_guard_association(role, peer_role):
    data_guard_association = DataGuardAssociation()
    data_guard_association.role = role
    data_guard_association.peer_role = peer_role
    return data_guard_association


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = {
        "database_id": "ocid1.database.oc1.iad.abuwc",
        "data_guard_association_id": "ocid1.dataguardassociation.oc1.iad.abuwc",
        "creation_type": "ExistingDbSystem",
        "database_admin_password": "BEstr0ng_#1",
        "protection_mode": "MAXIMUM_PERFORMANCE",
        "transport_type": "ASYNC",
        "peer_db_system_id": "ocid1.dbsystem.oc1.iad.abuwc",
    }
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
