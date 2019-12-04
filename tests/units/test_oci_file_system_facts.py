# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.module_utils.oracle import oci_utils
from ansible.modules.cloud.oracle import oci_file_system_facts


try:
    import oci
    from oci.file_storage.models import FileSystem
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_file_system_facts.py requires `oci` module")


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
    oci_file_system_facts.set_logger(logging)


def test_list_file_systems_list_all(file_storage_client, list_all_resources_patch):
    module = get_module(
        dict(
            {
                "compartment_id": "ocid1.compartment.aaaa",
                "availability_domain": "EXAMPLE-AD",
            }
        )
    )
    list_all_resources_patch.return_value = get_file_systems()
    file_storage_client.get_file_system.side_effect = [
        get_response(200, None, get_file_system(), None),
        get_response(200, None, get_file_system(), None),
    ]
    result = oci_file_system_facts.list_file_systems(file_storage_client, module)
    assert len(result["file_systems"]) is 2


def test_list_file_systems_list_specific(file_storage_client):
    module = get_module(dict({"file_system_id": "ocid1.filesystem.aaaa"}))
    file_storage_client.get_file_system.return_value = get_response(
        200, None, get_file_system(), None
    )
    result = oci_file_system_facts.list_file_systems(file_storage_client, module)
    assert result["file_systems"][0]["display_name"] is "ansible_file_system"


def test_list_file_systems_service_error(file_storage_client):
    error_message = "Internal Server Error"
    module = get_module(dict({"file_system_id": "ocid1.filesystem.aaaa"}))
    file_storage_client.get_file_system.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_file_system_facts.list_file_systems(file_storage_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def get_file_systems():
    file_systems = []
    file_system1 = FileSystem()
    file_system1.display_name = "ansible_file_system1"
    file_system2 = FileSystem()
    file_system2.display_name = "ansible_file_system2"
    file_systems.append(file_system1)
    file_systems.append(file_system2)
    return file_systems


def get_file_system():
    file_system = FileSystem()
    file_system.display_name = "ansible_file_system"
    return file_system


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = dict()
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
