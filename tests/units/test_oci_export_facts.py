# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.module_utils.oracle import oci_utils
from ansible.modules.cloud.oracle import oci_export_facts


try:
    import oci
    from oci.file_storage.models import Export
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_export_facts.py requires `oci` module")


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
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_export_facts.set_logger(logging)


def test_list_exports_list_all_by_compartment_id(
    file_storage_client, list_all_resources_patch
):
    module = get_module(dict({"compartment_id": "ocid1.compartment.aaaa"}))
    list_all_resources_patch.return_value = get_exports()
    file_storage_client.get_export.side_effect = [
        get_response(200, None, get_export(), None),
        get_response(200, None, get_export(), None),
    ]
    result = oci_export_facts.list_exports(file_storage_client, module)
    assert len(result["exports"]) is 2


def test_list_exports_list_all_by_file_system_id(
    file_storage_client, list_all_resources_patch
):
    module = get_module(dict({"file_system_id": "ocid1.filesystem.aaaa"}))
    list_all_resources_patch.return_value = get_exports()
    file_storage_client.get_export.side_effect = [
        get_response(200, None, get_export(), None),
        get_response(200, None, get_export(), None),
    ]
    result = oci_export_facts.list_exports(file_storage_client, module)
    assert len(result["exports"]) is 2


def test_list_exports_list_all_by_export_set_id(
    file_storage_client, list_all_resources_patch
):
    module = get_module(dict({"export_set_id": "ocid1.exportset.aaaa"}))
    list_all_resources_patch.return_value = get_exports()
    file_storage_client.get_export.side_effect = [
        get_response(200, None, get_export(), None),
        get_response(200, None, get_export(), None),
    ]
    result = oci_export_facts.list_exports(file_storage_client, module)
    assert len(result["exports"]) is 2


def test_list_exports_list_specific(file_storage_client):
    module = get_module(dict({"export_id": "ocid1.export.aaaa"}))
    file_storage_client.get_export.return_value = get_response(
        200, None, get_export(), None
    )
    result = oci_export_facts.list_exports(file_storage_client, module)
    assert result["exports"][0]["lifecycle_state"] is "ACTIVE"


def test_list_exports_service_error(file_storage_client):
    error_message = "Internal Server Error"
    module = get_module(dict({"export_id": "ocid1.export.aaaa"}))
    file_storage_client.get_export.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_export_facts.list_exports(file_storage_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def get_exports():
    exports = []
    export1 = Export()
    export1.lifecycle_state = "ACTIVE"
    export2 = Export()
    export2.lifecycle_state = "CREATING"
    exports.append(export1)
    exports.append(export2)
    return exports


def get_export():
    export = Export()
    export.lifecycle_state = "ACTIVE"
    return export


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = dict()
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
