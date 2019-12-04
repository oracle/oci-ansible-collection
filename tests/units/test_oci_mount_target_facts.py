# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.module_utils.oracle import oci_utils
from ansible.modules.cloud.oracle import oci_mount_target_facts


try:
    import oci
    from oci.file_storage.models import MountTarget
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_mount_target_facts.py requires `oci` module")


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
    oci_mount_target_facts.set_logger(logging)


def test_list_mount_targets_list_all(file_storage_client, list_all_resources_patch):
    module = get_module(
        dict(
            {
                "compartment_id": "ocid1.compartment.aaaa",
                "availability_domain": "EXAMPLE-AD",
            }
        )
    )
    list_all_resources_patch.return_value = get_mount_targets()
    file_storage_client.get_mount_target.side_effect = [
        get_response(200, None, get_mount_target(), None),
        get_response(200, None, get_mount_target(), None),
    ]
    result = oci_mount_target_facts.list_mount_targets(file_storage_client, module)
    assert len(result["mount_targets"]) is 2


def test_list_mount_targets_list_specific(file_storage_client):
    module = get_module(dict({"mount_target_id": "ocid1.mounttarget.aaaa"}))
    file_storage_client.get_mount_target.return_value = get_response(
        200, None, get_mount_target(), None
    )
    result = oci_mount_target_facts.list_mount_targets(file_storage_client, module)
    assert result["mount_targets"][0]["display_name"] is "ansible_mount_target"


def test_list_mount_targets_service_error(file_storage_client):
    error_message = "Internal Server Error"
    module = get_module(dict({"mount_target_id": "ocid1.mounttarget.aaaa"}))
    file_storage_client.get_mount_target.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_mount_target_facts.list_mount_targets(file_storage_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def get_mount_targets():
    mount_targets = []
    mount_target1 = MountTarget()
    mount_target1.display_name = "ansible_mount_target1"
    mount_target2 = MountTarget()
    mount_target2.display_name = "ansible_mount_target2"
    mount_targets.append(mount_target1)
    mount_targets.append(mount_target2)
    return mount_targets


def get_mount_target():
    mount_target = MountTarget()
    mount_target.display_name = "ansible_mount_target"
    return mount_target


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = dict()
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
