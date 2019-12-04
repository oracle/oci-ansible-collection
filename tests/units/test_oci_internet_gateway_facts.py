# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_internet_gateway_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import InternetGateway
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
except ImportError:
    raise SkipTest("test_oci_bucket.py requires `oci` module")


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
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


def test_list_internet_gateways(virtual_network_client, list_all_resources_patch):
    module = get_module()
    internet_gateway = get_internet_gateway()
    list_all_resources_patch.return_value = [internet_gateway]
    result = oci_internet_gateway_facts.list_internet_gateways(
        virtual_network_client, module
    )
    assert (
        result["internet_gateways"][0]["display_name"] == internet_gateway.display_name
    )


def test_list_internet_gateways_with_ig_id(
    virtual_network_client, list_all_resources_patch
):
    module = get_module_with_ig_id()
    internet_gateway = get_internet_gateway()
    virtual_network_client.get_internet_gateway.return_value = get_response(
        200, None, internet_gateway, None
    )
    result = oci_internet_gateway_facts.list_internet_gateways(
        virtual_network_client, module
    )
    assert (
        result["internet_gateways"][0]["display_name"] == internet_gateway.display_name
    )


def test_list_internet_gateways_service_error(
    virtual_network_client, list_all_resources_patch
):
    error_message = "Internal Server Error"
    module = get_module()
    list_all_resources_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    try:
        result = oci_internet_gateway_facts.list_internet_gateways(
            virtual_network_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0]


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


def get_module():
    params = {
        "compartment_id": "ocid1.comp..axsd",
        "vcn_id": "ocid1.vcn..fxdv",
        "ig_id": "",
        "display_name": None,
    }
    module = FakeModule(**params)
    return module


def get_module_with_ig_id():
    params = {
        "compartment_id": "",
        "vcn_id": "",
        "ig_id": "ocid1.internetgateway..fxdv",
        "display_name": None,
    }
    module = FakeModule(**params)
    return module
