# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_cross_connect
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import CrossConnect
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
except ImportError:
    raise SkipTest("test_oci_cross_connect.py requires `oci` module")


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
def virtual_network_client(mocker):
    mock_virtual_network_client = mocker.patch("oci.core.VirtualNetworkClient")
    return mock_virtual_network_client.return_value


@pytest.fixture()
def get_existing_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "get_existing_resource")


@pytest.fixture()
def create_cross_connect_patch(mocker):
    return mocker.patch.object(oci_cross_connect, "create_cross_connect")


@pytest.fixture()
def update_cross_connect_patch(mocker):
    return mocker.patch.object(oci_cross_connect, "update_cross_connect")


@pytest.fixture()
def check_and_create_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_create_resource")


@pytest.fixture()
def create_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "create_and_wait")


@pytest.fixture()
def check_and_update_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_update_resource")


@pytest.fixture()
def delete_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "delete_and_wait")


def test_create_or_update_cross_connect_create_success(
    virtual_network_client, check_and_create_resource_patch
):
    cross_connect = get_cross_connect()
    module = get_module(dict())
    check_and_create_resource_patch.return_value = dict(
        {"cross_connect": cross_connect, "changed": True}
    )
    result = oci_cross_connect.create_or_update_cross_connect(
        virtual_network_client, module
    )
    assert result["cross_connect"].display_name == cross_connect.display_name
    assert result["changed"] is True


def test_create_or_update_cross_connect_update_success(
    virtual_network_client, update_cross_connect_patch
):
    cross_connect = get_cross_connect()
    module = get_module(dict({"cross_connect_id": "test_cross_connect_id"}))
    get_existing_resource_patch.return_value = cross_connect
    update_cross_connect_patch.return_value = dict(
        changed=True, cross_connect=to_dict(cross_connect)
    )
    result = oci_cross_connect.create_or_update_cross_connect(
        virtual_network_client, module
    )
    assert result["cross_connect"]["display_name"] == cross_connect.display_name
    assert result["changed"] is True


def test_create_or_update_cross_connect_service_error(
    virtual_network_client, update_cross_connect_patch
):
    error_message = "Internal Server Error"
    module = get_module(dict({"cross_connect_id": "test_cross_connect_id"}))
    update_cross_connect_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    try:
        oci_cross_connect.create_or_update_cross_connect(virtual_network_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_cross_connect_timeout_error(
    virtual_network_client, update_cross_connect_patch
):
    error_message = "Maximum Timeout Reached"
    module = get_module(dict({"cross_connect_id": "test_cross_connect_id"}))
    update_cross_connect_patch.side_effect = MaximumWaitTimeExceeded(
        500, "TimeOutError", dict(), error_message
    )
    try:
        oci_cross_connect.create_or_update_cross_connect(virtual_network_client, module)
    except Exception as ex:
        assert error_message in ex.args[0].__repr__()


def test_create_cross_connect(virtual_network_client, create_and_wait_patch):
    module = get_module(dict({"display_name": "ansible_ig", "is_enabled": True}))
    cross_connect = get_cross_connect()
    create_and_wait_patch.return_value = dict(
        {"cross_connect": to_dict(cross_connect), "changed": True}
    )
    result = oci_cross_connect.create_cross_connect(virtual_network_client, module)
    assert result["cross_connect"]["display_name"] == cross_connect.display_name


def test_update_cross_connect_success(
    virtual_network_client, check_and_update_resource_patch
):
    module = get_module(
        dict(
            display_name="ansible_ig_updated",
            cross_connect_id="ocid1.crossconnect..xvzf",
        )
    )
    cross_connect = get_cross_connect()
    check_and_update_resource_patch.return_value = dict(
        {"cross_connect": cross_connect, "changed": True}
    )
    oci_cross_connect.update_cross_connect(
        virtual_network_client, cross_connect, module
    )
    assert check_and_update_resource_patch.called


def test_delete_cross_connect(virtual_network_client, delete_and_wait_patch):
    cross_connect = get_cross_connect()
    module = get_module(dict({"cross_connect_id": "ocid1.crossconnect..xvzf"}))
    get_existing_resource_patch.return_value = cross_connect
    oci_cross_connect.delete_cross_connect(virtual_network_client, module)
    assert delete_and_wait_patch.called


def get_cross_connect():
    cross_connect = CrossConnect()
    cross_connect.compartment_id = "ocid1.compartment..axsd"
    cross_connect.cross_connect_group_id = "ocid1.crossconectgroup..fxdv"
    cross_connect.id = "ocid1.crossconnect..vfgc"
    cross_connect.display_name = "ansible_cross_connect"
    cross_connect.location_name = "Equinix DC6, Ashburn, VA"
    cross_connect.port_name = "sample_port"
    cross_connect.port_speed_shape_name = "10 Gbps"
    cross_connect.lifecycle_state = "AVAILABLE"
    cross_connect.time_created = "2018-08-25T21:10:29.600Z"

    return cross_connect


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = {"compartment_id": "ocid1.comp..axsd"}
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
