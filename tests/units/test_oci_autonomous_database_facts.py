# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.module_utils.oracle import oci_utils
from ansible.modules.cloud.oracle import oci_autonomous_database_facts


try:
    import oci
    from oci.database.models import AutonomousDatabase
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_autonomous_database_facts.py requires `oci` module")


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
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_autonomous_database_facts.set_logger(logging)


def test_list_autonomous_databases_list_all(db_client, list_all_resources_patch):
    module = get_module(
        dict({"compartment_id": "ocid1.compartment.aaaa", "display_name": None})
    )
    list_all_resources_patch.return_value = get_autonomous_databases()
    result = oci_autonomous_database_facts.list_autonomous_databases(db_client, module)
    assert len(result["autonomous_databases"]) is 2


def test_list_autonomous_databases_list_specific(db_client):
    module = get_module(
        dict({"autonomous_database_id": "ocid1.autonomousdatabase.aaaa"})
    )
    db_client.get_autonomous_database.return_value = get_response(
        200, None, get_autonomous_database(), None
    )
    result = oci_autonomous_database_facts.list_autonomous_databases(db_client, module)
    assert (
        result["autonomous_databases"][0]["display_name"]
        is "ansible_autonomous_database"
    )


def test_list_autonomous_databases_service_error(db_client):
    error_message = "Internal Server Error"
    module = get_module(
        dict({"autonomous_database_id": "ocid1.autonomousdatabase.aaaa"})
    )
    db_client.get_autonomous_database.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_autonomous_database_facts.list_autonomous_databases(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def get_autonomous_databases():
    autonomous_databases = []
    autonomous_database1 = AutonomousDatabase()
    autonomous_database1.display_name = "ansible_autonomous_database1"
    autonomous_database2 = AutonomousDatabase()
    autonomous_database2.display_name = "ansible_autonomous_database2"
    autonomous_databases.append(autonomous_database1)
    autonomous_databases.append(autonomous_database2)
    return autonomous_databases


def get_autonomous_database():
    autonomous_database = AutonomousDatabase()
    autonomous_database.display_name = "ansible_autonomous_database"
    return autonomous_database


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = dict()
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
