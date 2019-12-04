# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_snapshot
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.file_storage.models import Snapshot
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_snapshot.py requires `oci` module")


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
def file_storage_client(mocker):
    mock_file_storage_client = mocker.patch(
        "oci.file_storage.file_storage_client.FileStorageClient"
    )
    return mock_file_storage_client.return_value


@pytest.fixture()
def check_and_create_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_create_resource")


@pytest.fixture()
def update_snapshot_patch(mocker):
    return mocker.patch.object(oci_snapshot, "update_snapshot")


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


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_snapshot.set_logger(logging)


def test_create_or_update_snapshot_create(
    file_storage_client, check_and_create_resource_patch
):
    module = get_module()
    snapshot = get_snapshot()
    check_and_create_resource_patch.return_value = {
        "snapshot": to_dict(snapshot),
        "changed": True,
    }
    result = oci_snapshot.create_or_update_snapshot(file_storage_client, module)
    assert result["snapshot"]["name"] is snapshot.name


def test_create_or_update_snapshot_update(file_storage_client, update_snapshot_patch):
    module = get_module(dict({"snapshot_id": "ocid1.snapshot.aaa"}))
    snapshot = get_snapshot()
    update_snapshot_patch.return_value = {
        "snapshot": to_dict(snapshot),
        "changed": True,
    }
    result = oci_snapshot.create_or_update_snapshot(file_storage_client, module)
    assert result["snapshot"]["name"] is snapshot.name


def test_create_or_update_snapshote_client_error(
    file_storage_client, check_and_create_resource_patch
):
    error_message = "mount target attribute has no value"
    module = get_module()
    check_and_create_resource_patch.side_effect = ClientError(Exception(error_message))
    try:
        oci_snapshot.create_or_update_snapshot(file_storage_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_snapshote_service_error(
    file_storage_client, check_and_create_resource_patch
):
    error_message = "Internal Server Error"
    module = get_module()
    check_and_create_resource_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_snapshot.create_or_update_snapshot(file_storage_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_snapshot(file_storage_client, create_and_wait_patch):
    module = get_module()
    snapshot = get_snapshot()
    create_and_wait_patch.return_value = {
        "snapshot": to_dict(snapshot),
        "changed": True,
    }
    result = oci_snapshot.create_snapshot(file_storage_client, module)
    assert result["snapshot"]["name"] is snapshot.name


def test_update_snapshot_freeform_tags(
    file_storage_client, check_and_update_resource_patch
):
    snapshot = get_snapshot()
    module = get_module(
        dict(freeform_tags=dict(deploy_type="dev"), snapshot_id="ocid1.mounttarget.aaa")
    )
    check_and_update_resource_patch.return_value = {
        "snapshot": to_dict(snapshot),
        "changed": True,
    }
    result = oci_snapshot.update_snapshot(file_storage_client, module)
    assert result["changed"] is True


def test_update_snapshot_defined_tags(
    file_storage_client, check_and_update_resource_patch
):
    snapshot = get_snapshot()
    module = get_module(
        dict(
            defined_tags=dict(plan=dict(corporate="medium")),
            snapshot_id="ocid1.mounttarget.aaa",
        )
    )
    check_and_update_resource_patch.return_value = {
        "snapshot": to_dict(snapshot),
        "changed": True,
    }
    result = oci_snapshot.update_snapshot(file_storage_client, module)
    assert result["changed"] is True


def test_delete_snapshot(file_storage_client, delete_and_wait_patch):
    module = get_module(dict(snapshot_id="ocid1.mounttarget.aaa"))
    snapshot = get_snapshot()
    delete_and_wait_patch.return_value = {
        "snapshot": to_dict(snapshot),
        "changed": True,
    }
    result = oci_snapshot.delete_snapshot(file_storage_client, module)
    assert result["snapshot"]["name"] is snapshot.name


def get_snapshot():
    snapshot = Snapshot()
    snapshot.name = "ansible_snapshot"
    snapshot.freeform_tags = {"deploy_type": "test"}
    snapshot.defined_tags = {"plan": {"student": "unlimited"}}
    return snapshot


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {
        "file_system_id": "ocid1.filesystem.oc1..abuw",
        "name": "ansible_snapshot",
    }
    if additional_properties:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
