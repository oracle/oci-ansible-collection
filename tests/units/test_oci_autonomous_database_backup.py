# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_autonomous_database_backup
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.database.models import AutonomousDatabaseBackup
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_autonomous_database_backup.py requires `oci` module")


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
def create_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "create_and_wait")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_autonomous_database_backup.set_logger(logging)


def test_create_autonomous_database_backup(db_client, create_and_wait_patch):
    module = get_module(dict())
    autonomous_database_backup = get_autonomous_database_backup()
    create_and_wait_patch.return_value = {
        "autonomous_database_backup": to_dict(autonomous_database_backup),
        "changed": True,
    }
    result = oci_autonomous_database_backup.create_autonomous_database_backup(
        db_client, module
    )
    assert (
        result["autonomous_database_backup"]["display_name"]
        is autonomous_database_backup.display_name
    )


def get_autonomous_database_backup():
    autonomous_database_backup = AutonomousDatabaseBackup()
    autonomous_database_backup.display_name = "ansible-autonomous_database_backup"
    return autonomous_database_backup


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = {
        "autonoumous_database_backup_id": "ocid1.autonomousdatabase.oc1.iad.abuw",
        "display_name": "ansible-autonomous_database_backup",
    }
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
