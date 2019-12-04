# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_db_node
from ansible.module_utils.oracle import oci_db_utils, oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.database.models import DbNode
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_db_node.py requires `oci` module")


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
def execute_function_and_wait_patch(mocker):
    return mocker.patch.object(oci_db_utils, "execute_function_and_wait")


@pytest.fixture()
def get_existing_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "get_existing_resource")


@pytest.fixture()
def db_node_action_patch(mocker):
    return mocker.patch.object(oci_db_node, "db_node_action")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_db_node.set_logger(logging)


def test_perform_db_node_action(
    db_client, get_existing_resource_patch, db_node_action_patch
):
    module = get_module(dict())
    db_node = get_db_node("AVAILABLE")
    get_existing_resource_patch.return_value = db_node
    db_node_action_patch.return_value = {"db_node": to_dict(db_node), "changed": True}
    result = oci_db_node.perform_db_node_action(db_client, module)
    assert result["db_node"]["hostname"] is db_node.hostname


def test_create_or_update_db_node_client_error(db_client, get_existing_resource_patch):
    error_message = "Db Node id is mandatory"
    module = get_module(dict())
    get_existing_resource_patch.side_effect = ClientError(Exception(error_message))
    try:
        oci_db_node.perform_db_node_action(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_db_node_service_error(
    db_client, get_existing_resource_patch, db_node_action_patch
):
    error_message = "Internal Server Error"
    module = get_module(dict())
    db_node = get_db_node("AVAILABLE")
    get_existing_resource_patch.return_value = db_node
    db_node_action_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_db_node.perform_db_node_action(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_db_node_action_change_in_desired_state(
    db_client, execute_function_and_wait_patch
):
    module = get_module(dict({"state": "stop"}))
    db_node = get_db_node("AVAILABLE")
    execute_function_and_wait_patch.return_value = {
        "db_node": to_dict(db_node),
        "changed": True,
    }
    result = oci_db_node.db_node_action(db_client, module, db_node)
    assert result["changed"] is True


def test_db_node_action_no_change_in_desired_state(db_client):
    module = get_module(dict({"state": "start"}))
    db_node = get_db_node("AVAILABLE")
    result = oci_db_node.db_node_action(db_client, module, db_node)
    assert result["changed"] is False


def test_db_node_action_reset(db_client, execute_function_and_wait_patch):
    module = get_module(dict({"state": "reset"}))
    db_node = get_db_node("AVAILABLE")
    execute_function_and_wait_patch.return_value = {
        "db_node": to_dict(db_node),
        "changed": True,
    }
    result = oci_db_node.db_node_action(db_client, module, db_node)
    assert result["changed"] is True


def get_db_node(lifecycle_state):
    db_node = DbNode()
    db_node.hostname = "ansibledbnode"
    db_node.lifecycle_state = lifecycle_state
    return db_node


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = {"db_node_id": "ocid1.dbnode.aaaa"}
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
