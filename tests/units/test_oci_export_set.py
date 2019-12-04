# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_export_set
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.file_storage.models import ExportSet
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_export_set.py requires `oci` module")


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
def update_export_set_patch(mocker):
    return mocker.patch.object(oci_export_set, "update_export_set")


@pytest.fixture()
def check_and_update_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_update_resource")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_export_set.set_logger(logging)


def test_update_export_sete_client_error(
    file_storage_client, check_and_update_resource_patch
):
    error_message = "export set attribute has no value"
    module = get_module(dict({"export_set_id": "ocid1.exportset.aaa"}))
    check_and_update_resource_patch.side_effect = ClientError(Exception(error_message))
    try:
        oci_export_set.update_export_set(file_storage_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_update_export_set_service_error(
    file_storage_client, check_and_update_resource_patch
):
    error_message = "Internal Server Error"
    module = get_module(dict({"export_set_id": "ocid1.exportset.aaa"}))
    check_and_update_resource_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_export_set.update_export_set(file_storage_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_update_export_set_display_name(
    file_storage_client, check_and_update_resource_patch
):
    export_set = get_export_set()
    export_set.display_name = "ansible_updated_export_set"
    module = get_module(dict({"export_set_id": "ocid1.exportset.aaa"}))
    check_and_update_resource_patch.return_value = {
        "export_set": to_dict(export_set),
        "changed": True,
    }
    result = oci_export_set.update_export_set(file_storage_client, module)
    assert result["changed"] is True


def test_update_export_set_max_fs_stat_bytes(
    file_storage_client, check_and_update_resource_patch
):
    export_set = get_export_set()
    module = get_module(
        dict(max_fs_stat_bytes=500, export_set_id="ocid1.exportset.aaa")
    )
    check_and_update_resource_patch.return_value = {
        "export_set": to_dict(export_set),
        "changed": True,
    }
    result = oci_export_set.update_export_set(file_storage_client, module)
    assert result["changed"] is True


def test_update_export_set_max_fs_stat_files(
    file_storage_client, check_and_update_resource_patch
):
    export_set = get_export_set()
    module = get_module(
        dict(max_fs_stat_files=500, export_set_id="ocid1.exportset.aaa")
    )
    check_and_update_resource_patch.return_value = {
        "export_set": to_dict(export_set),
        "changed": True,
    }
    result = oci_export_set.update_export_set(file_storage_client, module)
    assert result["changed"] is True


def get_export_set():
    export_set = ExportSet()
    export_set.max_fs_stat_bytes = 100
    export_set.max_fs_stat_files = 100
    export_set.display_name = "ansible_export_set"
    return export_set


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {
        "max_fs_stat_bytes": 100,
        "max_fs_stat_files": 100,
        "display_name": "ansible_export_set",
    }
    if additional_properties:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
