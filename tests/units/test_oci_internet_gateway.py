# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_internet_gateway
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import InternetGateway
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
except ImportError:
    raise SkipTest("test_oci_internet_gateway.py requires `oci` module")


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
def oci_wait_until_patch(mocker):
    return mocker.patch.object(oci, "wait_until")


@pytest.fixture()
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


@pytest.fixture()
def get_existing_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "get_existing_resource")


@pytest.fixture()
def create_internet_gateway_patch(mocker):
    return mocker.patch.object(oci_internet_gateway, "create_internet_gateway")


@pytest.fixture()
def update_internet_gateway_patch(mocker):
    return mocker.patch.object(oci_internet_gateway, "update_internet_gateway")


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


def test_create_or_update_internet_gateway_create_success(
    virtual_network_client, check_and_create_resource_patch
):
    internet_gateway = get_internet_gateway()
    module = get_module(dict())
    check_and_create_resource_patch.return_value = dict(
        {"internet_gateway": internet_gateway, "changed": True}
    )
    result = oci_internet_gateway.create_or_update_internet_gateway(
        virtual_network_client, module
    )
    assert result["internet_gateway"].display_name == internet_gateway.display_name
    assert result["changed"] is True


def test_create_or_update_internet_gateway_update_success(
    virtual_network_client, update_internet_gateway_patch
):
    internet_gateway = get_internet_gateway()
    module = get_module(dict({"ig_id": "test_ig_id"}))
    get_existing_resource_patch.return_value = internet_gateway
    update_internet_gateway_patch.return_value = dict(
        changed=True, internet_gateway=to_dict(internet_gateway)
    )
    result = oci_internet_gateway.create_or_update_internet_gateway(
        virtual_network_client, module
    )
    assert result["internet_gateway"]["display_name"] == internet_gateway.display_name
    assert result["changed"] is True


def test_create_or_update_internet_gateway_service_error(
    virtual_network_client, update_internet_gateway_patch
):
    error_message = "Internal Server Error"
    module = get_module(dict({"ig_id": "test_ig_id"}))
    update_internet_gateway_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    try:
        oci_internet_gateway.create_or_update_internet_gateway(
            virtual_network_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_internet_gateway_timeout_error(
    virtual_network_client, update_internet_gateway_patch
):
    error_message = "Maximum Timeout Reached"
    module = get_module(dict({"ig_id": "test_ig_id"}))
    update_internet_gateway_patch.side_effect = MaximumWaitTimeExceeded(
        500, "TimeOutError", dict(), error_message
    )
    try:
        oci_internet_gateway.create_or_update_internet_gateway(
            virtual_network_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0].__repr__()


def test_create_internet_gateway(virtual_network_client, create_and_wait_patch):
    module = get_module(dict({"display_name": "ansible_ig", "is_enabled": True}))
    internet_gateway = get_internet_gateway()
    create_and_wait_patch.return_value = dict(
        {"internet_gateway": to_dict(internet_gateway), "changed": True}
    )
    result = oci_internet_gateway.create_internet_gateway(
        virtual_network_client, module
    )
    assert result["internet_gateway"]["display_name"] == internet_gateway.display_name


def test_update_internet_gateway_success(
    virtual_network_client, check_and_update_resource_patch
):
    module = get_module(
        dict(display_name="ansible_ig_updated", ig_id="ocid1.internetgateway..xvzf")
    )
    internet_gateway = get_internet_gateway()
    check_and_update_resource_patch.return_value = dict(
        {"internet_gateway": internet_gateway, "changed": True}
    )
    result = oci_internet_gateway.update_internet_gateway(
        virtual_network_client, module
    )
    assert check_and_update_resource_patch.called


def test_delete_internet_gateway(virtual_network_client, delete_and_wait_patch):
    internet_gateway = get_internet_gateway()
    module = get_module(dict({"ig_id": "ocid1.internetgateway..xvzf"}))
    get_existing_resource_patch.return_value = internet_gateway
    result = oci_internet_gateway.delete_internet_gateway(
        virtual_network_client, module
    )
    assert delete_and_wait_patch.called


def get_internet_gateway():
    internet_gateway = InternetGateway()
    internet_gateway.compartment_id = "ocid1.comp..axsd"
    internet_gateway.vcn_id = "ocid1.vcn..fxdv"
    internet_gateway.id = "ocid1.ig..vfgc"
    internet_gateway.display_name = "ansible_ig"
    internet_gateway.is_enabled = True
    internet_gateway.lifecycle_state = "AVAILABLE"
    internet_gateway.time_created = "2016-08-25T21:10:29.600Z"

    return internet_gateway


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = {"compartment_id": "ocid1.comp..axsd", "vcn_id": "ocid1.vcn..fxdv"}
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
