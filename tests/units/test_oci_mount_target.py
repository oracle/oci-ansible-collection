# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_mount_target
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.file_storage.models import MountTarget
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_mount_target.py requires `oci` module")


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
def update_mount_target_patch(mocker):
    return mocker.patch.object(oci_mount_target, "update_mount_target")


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
    oci_mount_target.set_logger(logging)


def test_create_or_update_mount_target_create(
    file_storage_client, check_and_create_resource_patch
):
    module = get_module()
    mount_target = get_mount_target()
    check_and_create_resource_patch.return_value = {
        "mount_target": to_dict(mount_target),
        "changed": True,
    }
    result = oci_mount_target.create_or_update_mount_target(file_storage_client, module)
    assert result["mount_target"]["display_name"] is mount_target.display_name


def test_create_or_update_mount_target_update(
    file_storage_client, update_mount_target_patch
):
    module = get_module(dict({"mount_target_id": "ocid1.mount_target.aaa"}))
    mount_target = get_mount_target()
    update_mount_target_patch.return_value = {
        "mount_target": to_dict(mount_target),
        "changed": True,
    }
    result = oci_mount_target.create_or_update_mount_target(file_storage_client, module)
    assert result["mount_target"]["display_name"] is mount_target.display_name


def test_create_or_update_mount_targete_client_error(
    file_storage_client, check_and_create_resource_patch
):
    error_message = "mount target attribute has no value"
    module = get_module()
    check_and_create_resource_patch.side_effect = ClientError(Exception(error_message))
    try:
        oci_mount_target.create_or_update_mount_target(file_storage_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_mount_targete_service_error(
    file_storage_client, check_and_create_resource_patch
):
    error_message = "Internal Server Error"
    module = get_module()
    check_and_create_resource_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_mount_target.create_or_update_mount_target(file_storage_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_mount_target(file_storage_client, create_and_wait_patch):
    module = get_module()
    mount_target = get_mount_target()
    create_and_wait_patch.return_value = {
        "mount_target": to_dict(mount_target),
        "changed": True,
    }
    result = oci_mount_target.create_mount_target(file_storage_client, module)
    assert result["mount_target"]["display_name"] is mount_target.display_name


def test_update_mount_target_display_name(
    file_storage_client, check_and_update_resource_patch
):
    mount_target = get_mount_target()
    mount_target.display_name = "ansible_updated_mount_target"
    module = get_module(dict({"mount_target_id": "ocid1.mounttarget.aaa"}))
    check_and_update_resource_patch.return_value = {
        "mount_target": to_dict(mount_target),
        "changed": True,
    }
    result = oci_mount_target.update_mount_target(file_storage_client, module)
    assert result["changed"] is True


def test_update_mount_target_freeform_tags(
    file_storage_client, check_and_update_resource_patch
):
    mount_target = get_mount_target()
    module = get_module(
        dict(
            freeform_tags=dict(deploy_type="dev"),
            mount_target_id="ocid1.mounttarget.aaa",
        )
    )
    check_and_update_resource_patch.return_value = {
        "mount_target": to_dict(mount_target),
        "changed": True,
    }
    result = oci_mount_target.update_mount_target(file_storage_client, module)
    assert result["changed"] is True


def test_update_mount_target_defined_tags(
    file_storage_client, check_and_update_resource_patch
):
    mount_target = get_mount_target()
    module = get_module(
        dict(
            defined_tags=dict(plan=dict(corporate="medium")),
            mount_target_id="ocid1.mounttarget.aaa",
        )
    )
    check_and_update_resource_patch.return_value = {
        "mount_target": to_dict(mount_target),
        "changed": True,
    }
    result = oci_mount_target.update_mount_target(file_storage_client, module)
    assert result["changed"] is True


def test_delete_mount_target(file_storage_client, delete_and_wait_patch):
    module = get_module(dict(mount_target_id="ocid1.mounttarget.aaa"))
    mount_target = get_mount_target()
    delete_and_wait_patch.return_value = {
        "mount_target": to_dict(mount_target),
        "changed": True,
    }
    result = oci_mount_target.delete_mount_target(file_storage_client, module)
    assert result["mount_target"]["display_name"] is mount_target.display_name


def get_mount_target():
    mount_target = MountTarget()
    mount_target.availability_domain = "EXAMPLE-AD"
    mount_target.display_name = "ansible_mount_targete"
    mount_target.freeform_tags = {"deploy_type": "test"}
    mount_target.defined_tags = {"plan": {"student": "unlimited"}}
    return mount_target


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {
        "compartment_id": "ocid1.compartment.oc1..abuw",
        "availability_domain": "EXAMPLE-AD",
        "hostname_label": "example_host",
        "ip_address": "10.0.0.0.1",
        "display_name": "ansible_mount_target",
        "subnet_id": "ocid1.subnet.oc1...abuw",
        "freeform_tags": {"deploy_type": "test"},
    }
    if additional_properties:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
