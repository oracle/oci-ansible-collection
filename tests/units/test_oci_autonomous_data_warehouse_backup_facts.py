# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_autonomous_data_warehouse_backup_facts
from ansible.module_utils.oracle import oci_utils


try:
    import oci
    from oci.database.models import AutonomousDataWarehouseBackup
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest(
        "test_oci_autonomous_data_warehouse_backup_facts.py requires `oci` module"
    )


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
    oci_autonomous_data_warehouse_backup_facts.set_logger(logging)


def test_list_autonomous_data_warehouse_backups_list_all(
    db_client, list_all_resources_patch
):
    module = get_module(
        dict(
            compartment_id="ocid1.compartment.aaaa",
            autonomous_data_warehouse_backup_id="ocid1.autonomousdbwarehousebackup.aaaa",
        )
    )
    list_all_resources_patch.return_value = get_autonomous_data_warehouse_backups()
    result = oci_autonomous_data_warehouse_backup_facts.list_autonomous_data_warehouse_backups(
        db_client, module
    )
    assert len(result["autonomous_data_warehouse_backups"]) is 2


def test_list_autonomous_data_warehouse_backups_list_specific(db_client):
    module = get_module(
        dict(
            {
                "autonomous_data_warehouse_backup_id": "ocid1.autonomousdbwarehousebackup.aaaa"
            }
        )
    )
    autonomous_data_warehouse_backup = get_autonomous_data_warehouse_backup()
    db_client.get_autonomous_data_warehouse_backup.return_value = get_response(
        200, None, autonomous_data_warehouse_backup, None
    )
    result = oci_autonomous_data_warehouse_backup_facts.list_autonomous_data_warehouse_backups(
        db_client, module
    )
    assert (
        result["autonomous_data_warehouse_backups"][0]["display_name"]
        is autonomous_data_warehouse_backup.display_name
    )


def test_list_autonomous_data_warehouse_backup_service_error(db_client):
    error_message = "Internal Server Error"
    module = get_module(
        dict(
            {
                "autonomous_data_warehouse_backup_id": "ocid1.autonomousdatabasebackup.aaaa"
            }
        )
    )
    db_client.get_db_system.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_autonomous_data_warehouse_backup_facts.list_autonomous_data_warehouse_backups(
            db_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def get_autonomous_data_warehouse_backups():
    autonomous_data_warehouse_backups = []
    autonomous_data_warehouse_backup1 = AutonomousDataWarehouseBackup()
    autonomous_data_warehouse_backup1.display_name = (
        "ansible-autonomous_data_warehouse_backup1"
    )
    autonomous_data_warehouse_backup2 = AutonomousDataWarehouseBackup()
    autonomous_data_warehouse_backup2.display_name = (
        "ansible-autonomous_data_warehouse_backup2"
    )
    autonomous_data_warehouse_backups.append(autonomous_data_warehouse_backup1)
    autonomous_data_warehouse_backups.append(autonomous_data_warehouse_backup2)
    return autonomous_data_warehouse_backups


def get_autonomous_data_warehouse_backup():
    autonomous_data_warehouse_backup = AutonomousDataWarehouseBackup()
    autonomous_data_warehouse_backup.display_name = (
        "ansible-autonomous_data_warehouse_backup"
    )
    return autonomous_data_warehouse_backup


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = dict()
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
