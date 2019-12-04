# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_export
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.file_storage.models import Export, ClientOptions
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_export.py requires `oci` module")


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
def update_export_patch(mocker):
    return mocker.patch.object(oci_export, "update_export")


@pytest.fixture()
def update_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "update_and_wait")


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
    oci_export.set_logger(logging)


def test_create_or_update_export_create(
    file_storage_client, check_and_create_resource_patch
):
    module = get_module()
    export = get_export()
    check_and_create_resource_patch.return_value = {
        "export": to_dict(export),
        "changed": True,
    }
    result = oci_export.create_or_update_export(file_storage_client, module)
    assert result["export"]["lifecycle_state"] is export.lifecycle_state


def test_create_or_update_export_update(file_storage_client, update_export_patch):
    module = get_module(dict({"export_id": "ocid1.export.aaa"}))
    export = get_export()
    update_export_patch.return_value = {"export": to_dict(export), "changed": True}
    result = oci_export.create_or_update_export(file_storage_client, module)
    assert result["export"]["lifecycle_state"] is export.lifecycle_state


def test_create_or_update_exporte_client_error(
    file_storage_client, check_and_create_resource_patch
):
    error_message = "export attribute has no value"
    module = get_module()
    check_and_create_resource_patch.side_effect = ClientError(Exception(error_message))
    try:
        oci_export.create_or_update_export(file_storage_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_exporte_service_error(
    file_storage_client, check_and_create_resource_patch
):
    error_message = "Internal Server Error"
    module = get_module()
    check_and_create_resource_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_export.create_or_update_export(file_storage_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_export(file_storage_client, create_and_wait_patch):
    module = get_module()
    export = get_export()
    create_and_wait_patch.return_value = {"export": to_dict(export), "changed": True}
    result = oci_export.create_export(file_storage_client, module)
    assert result["export"]["lifecycle_state"] is export.lifecycle_state


def test_update_export_different_export_options(
    file_storage_client, update_and_wait_patch
):
    export = get_export()
    export_options = [
        {
            "source": "0.0.0.0/0",
            "require_privileged_source_port": True,
            "access": "READ_WRITE",
            "identity_squash": "NONE",
        }
    ]
    module = get_module(
        dict({"export_id": "ocid1.export.aaa", "export_options": export_options})
    )
    update_and_wait_patch.return_value = {"export": to_dict(export), "changed": True}
    result = oci_export.update_export(file_storage_client, module, export)
    assert result["changed"] is True


def test_update_export_empty_input_export_options(
    file_storage_client, update_and_wait_patch
):
    export = get_export()
    export_options = []
    module = get_module(
        dict({"export_id": "ocid1.export.aaa", "export_options": export_options})
    )
    update_and_wait_patch.return_value = {"export": to_dict(export), "changed": True}
    result = oci_export.update_export(file_storage_client, module, export)
    assert result["changed"] is True


def test_update_export_no_export_options_difference(
    file_storage_client, update_and_wait_patch
):
    export = get_export()
    export_options = [
        {
            "source": "0.0.0.0/0",
            "require_privileged_source_port": False,
            "access": "READ_ONLY",
            "identity_squash": "NONE",
        }
    ]
    module = get_module(
        dict({"export_id": "ocid1.export.aaa", "export_options": export_options})
    )
    result = oci_export.update_export(file_storage_client, module, export)
    assert result["changed"] is False


def test_delete_export(file_storage_client, delete_and_wait_patch):
    module = get_module(dict(export_id="ocid1.export.aaa"))
    export = get_export()
    delete_and_wait_patch.return_value = {"export": to_dict(export), "changed": True}
    result = oci_export.delete_export(file_storage_client, module)
    assert result["export"]["lifecycle_state"] is export.lifecycle_state


def get_export():
    export = Export()
    export.export_options = get_common_export_options()
    export.path = "/testpath"
    export.lifecycle_state = "ACTIVE"
    return export


def get_common_export_options():
    export_options = []
    client_options = ClientOptions()
    client_options.source = "0.0.0.0/0"
    client_options.access = ClientOptions.ACCESS_READ_ONLY
    client_options.identity_squash = "NONE"
    client_options.require_privileged_source_port = False
    client_options.anonymous_gid = 65534
    client_options.anonymous_uid = 65534
    export_options.append(client_options)
    return export_options


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {
        "file_system_id": "ocid1.filesystem.oc1..abuw",
        "export_set_id": "ocid1.exportset.oc1..abuw",
        "export_options": [
            {
                "source": "0.0.0.0/0",
                "require_privileged_source_port": False,
                "access": "READ_WRITE",
                "identity_squash": "NONE",
            }
        ],
        "path": "/inputpath",
        "purge_export_options": False,
    }
    if additional_properties:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
