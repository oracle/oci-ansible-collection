# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_db_system
from ansible.module_utils.oracle import oci_utils
import tempfile
import os


try:
    import oci
    from oci.util import to_dict
    from oci.database.models import DbSystem, PatchHistoryEntry, UpdateDbSystemDetails
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_db_system.py requires `oci` module")


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
def get_existing_db_system_patch(mocker):
    return mocker.patch.object(oci_db_system, "get_existing_db_system")


@pytest.fixture()
def update_db_system_patch(mocker):
    return mocker.patch.object(oci_db_system, "update_db_system")


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
    oci_db_system.set_logger(logging)


def test_launch_or_update_db_system_launch(db_client, check_and_create_resource_patch):
    module = get_module(dict())
    db_system = get_db_system()
    check_and_create_resource_patch.return_value = {
        "db_system": to_dict(db_system),
        "changed": True,
    }
    result = oci_db_system.launch_or_update_db_system(db_client, module)
    assert result["db_system"]["display_name"] is db_system.display_name


def test_launch_or_update_db_system_update(db_client, update_db_system_patch):
    module = get_module(dict({"db_system_id": "ocid1.dbsystem.aaa"}))
    db_system = get_db_system()
    update_db_system_patch.return_value = {
        "db_system": to_dict(db_system),
        "changed": True,
    }
    result = oci_db_system.launch_or_update_db_system(db_client, module)
    assert result["db_system"]["display_name"] is db_system.display_name


def test_launch_or_update_db_system_client_error(
    db_client, check_and_create_resource_patch
):
    error_message = "databse attribute has no value"
    module = get_module(dict())
    check_and_create_resource_patch.side_effect = ClientError(Exception(error_message))
    try:
        oci_db_system.launch_or_update_db_system(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_launch_or_update_db_system_service_error(
    db_client, check_and_create_resource_patch
):
    error_message = "Internal Server Error"
    module = get_module(dict())
    check_and_create_resource_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_db_system.launch_or_update_db_system(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_launch_db_system(db_client, create_and_wait_patch):
    ssh_public_keys = get_ssh_public_keys(1)
    additional_properties = dict({"ssh_public_keys": ssh_public_keys})
    module = get_module(additional_properties)
    db_system = get_db_system()
    create_and_wait_patch.return_value = {
        "db_system": to_dict(db_system),
        "changed": True,
    }
    result = oci_db_system.launch_db_system(db_client, module)
    delete_ssh_public_keys(ssh_public_keys)
    assert result["db_system"]["display_name"] is db_system.display_name


def test_launch_db_system_with_database_from_backup(db_client, create_and_wait_patch):
    ssh_public_keys = get_ssh_public_keys(1)
    additional_properties = dict(
        {"source": "DB_BACKUP", "ssh_public_keys": ssh_public_keys}
    )
    module = get_module(additional_properties)
    db_system = get_db_system()
    create_and_wait_patch.return_value = {
        "db_system": to_dict(db_system),
        "changed": True,
    }
    result = oci_db_system.launch_db_system(db_client, module)
    delete_ssh_public_keys(ssh_public_keys)
    assert result["db_system"]["display_name"] is db_system.display_name


def test_update_db_systems_with_cpu_core_count(
    db_client, get_existing_resource_patch, update_and_wait_patch
):
    db_system = get_db_system()
    db_system.cpu_core_count = 4
    get_existing_resource_patch.return_value = db_system
    module = get_module(dict())
    update_and_wait_patch.return_value = {
        "db_system": to_dict(db_system),
        "changed": True,
    }
    result = oci_db_system.update_db_system(db_client, module, "ocid.dbsystem.ocid1")
    assert result["changed"] is True


def test_update_db_systems_ssh_public_keys_changed_purged(db_client):
    db_system = get_db_system()
    existing_ssh_public_keys = get_ssh_public_keys(1)
    input_ssh_public_keys = get_ssh_public_keys(1)
    db_system.ssh_public_keys = existing_ssh_public_keys
    module = get_module(
        dict({"ssh_public_keys": input_ssh_public_keys, "purge_ssh_public_keys": True})
    )
    update_and_wait_patch.return_value = {
        "db_system": to_dict(db_system),
        "changed": True,
    }
    result = oci_db_system.update_db_system(db_client, module, "ocid.dbsystem.ocid1")
    delete_ssh_public_keys(input_ssh_public_keys)
    delete_ssh_public_keys(existing_ssh_public_keys)
    assert result["changed"] is True


def test_update_db_systems_ssh_public_keys_changed_no_purge(db_client):
    db_system = get_db_system()
    existing_ssh_public_keys = get_ssh_public_keys(1)
    input_ssh_public_keys = get_ssh_public_keys(1)
    db_system.ssh_public_keys = existing_ssh_public_keys
    module = get_module(
        dict({"ssh_public_keys": input_ssh_public_keys, "purge_ssh_public_keys": False})
    )
    update_and_wait_patch.return_value = {
        "db_system": to_dict(db_system),
        "changed": True,
    }
    result = oci_db_system.update_db_system(db_client, module, "ocid.dbsystem.ocid1")
    delete_ssh_public_keys(input_ssh_public_keys)
    delete_ssh_public_keys(existing_ssh_public_keys)
    assert result["changed"] is True


def test_update_db_systems_freeform_tags(
    db_client, get_existing_resource_patch, update_and_wait_patch
):
    db_system = get_db_system()
    get_existing_resource_patch.return_value = db_system
    module = get_module(dict(freeform_tags=dict(system_type="oracledb")))
    update_and_wait_patch.return_value = {
        "db_system": to_dict(db_system),
        "changed": True,
    }
    result = oci_db_system.update_db_system(db_client, module, "ocid.dbsystem.ocid1")
    assert result["changed"] is True


def test_update_db_systems_defined_tags(
    db_client, get_existing_resource_patch, update_and_wait_patch
):
    db_system = get_db_system()
    get_existing_resource_patch.return_value = db_system
    module = get_module(dict(defined_tags=dict(system_strength=dict(shape="medium"))))
    update_and_wait_patch.return_value = {
        "db_system": to_dict(db_system),
        "changed": True,
    }
    result = oci_db_system.update_db_system(db_client, module, "ocid.dbsystem.ocid1")
    assert result["changed"] is True


def test_update_db_systems_client_error_no_db_system(
    db_client, get_existing_resource_patch
):
    error_message = "No DB System"
    module = get_module(dict())
    get_existing_resource_patch.return_value = None
    try:
        oci_db_system.update_db_system(db_client, module, "ocid1.dbsystem.aaaa")
    except Exception as ex:
        assert error_message in str(ex.args)


def test_delete_db_system(db_client, delete_and_wait_patch):
    module = get_module(
        dict({"db_system_id": "ocid1.dbsystem.aaa", "wait_untill_completion": True})
    )
    db_system = get_db_system()
    get_existing_db_system_patch.return_value = db_system
    delete_and_wait_patch.return_value = {
        "db_system": to_dict(db_system),
        "changed": True,
    }
    result = oci_db_system.delete_db_system(db_client, module)
    assert result["db_system"]["display_name"] is db_system.display_name


def get_patch_history_entry(lifecycle_state, action):
    patch_history_entry = PatchHistoryEntry()
    patch_history_entry.patch_id = "ocid1.dbpatch.oc1.iad.abu"
    patch_history_entry.lifecycle_state = lifecycle_state
    patch_history_entry.action = action
    return patch_history_entry


def get_ssh_public_keys(number_of_files):
    ssh_public_keys = []
    for file_count in range(number_of_files):
        new_file, filename = tempfile.mkstemp()
        os.write(new_file, b"Certificate content")
        ssh_public_keys.append(filename)
    return ssh_public_keys


def get_db_system():
    db_system = DbSystem()
    db_system.display_name = "ansible_db_system"
    db_system.freeform_tags = {"system_type": "exadata"}
    db_system.defined_tags = {"system_strength": {"shape": "small"}}
    return db_system


def delete_ssh_public_keys(files):
    for file in files:
        os.remove(file)


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = {
        "compartment_id": "ocid1.compartment.oc1",
        "availability_domain": "IwGV:US-ASHBURN-AD-2",
        "cluster_name": "my-cluster",
        "cpu_core_count": 2,
        "data_storage_percentage": 80,
        "database_edition": "STANDARD_EDITION",
        "db_home": {
            "database": {
                "admin_password": "BEstr0ng_#1",
                "character_set": "AL32UTF8",
                "db_backup_config": {"auto_backup_enabled": False},
                "db_name": "testdb",
                "db_workload": "OLTP",
                "ncharacter_set": "AL16UTF16",
            },
            "db_version": "12.2.0.1",
            "display_name": "ansible_db",
        },
        "disk_redundancy": "NORMAL",
        "display_name": "ansibledbsystem",
        "hostname": "ansibledbsystem",
        "initial_data_storage_size_in_gb": 4096,
        "license_model": "LICENSE_INCLUDED",
        "node_count": 1,
        "shape": "BM.DenseIO1.36",
        "subnet_id": "ocid1.subnet.oc1.iad.aaaa",
    }
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
