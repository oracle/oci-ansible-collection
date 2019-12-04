# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_fast_connect_provider_service_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import FastConnectProviderService
except ImportError:
    raise SkipTest(
        "test_oci_fast_connect_provider_service_facts.py requires `oci` module"
    )


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


def test_list_fast_connect_provider_services_all(
    virtual_network_client, list_all_resources_patch
):
    module = get_module()
    fast_connect_provider_services = get_fast_connect_provider_services()
    list_all_resources_patch.return_value = fast_connect_provider_services
    result = oci_fast_connect_provider_service_facts.list_fast_connect_provider_services(
        virtual_network_client, module
    )
    assert (
        result["fast_connect_provider_services"][0]["description"]
        == fast_connect_provider_services[0].description
    )


def test_list_fast_connect_provider_services_specific(
    virtual_network_client, list_all_resources_patch
):
    module = get_module(dict(provider_service_id="ocid1.providerservice..vgfc"))
    fast_connect_provider_services = get_fast_connect_provider_services()
    list_all_resources_patch.return_value = fast_connect_provider_services
    result = oci_fast_connect_provider_service_facts.list_fast_connect_provider_services(
        virtual_network_client, module
    )
    assert (
        result["fast_connect_provider_services"][0]["description"]
        == fast_connect_provider_services[0].description
    )


def get_fast_connect_provider_services():
    fast_connect_provider_services = []
    fast_connect_provider_service = FastConnectProviderService()
    fast_connect_provider_service.description = "https://testexample.com"
    fast_connect_provider_service.id = "ocid1.providerservice..fxdv"
    fast_connect_provider_service.private_peering_bgp_management = "CUSTOMER_MANAGED"
    fast_connect_provider_service.provider_name = "Example Provider"
    fast_connect_provider_service.provider_service_name = "Example Provider Service"
    fast_connect_provider_service.public_peering_bgp_management = "ORACLE_MANAGED"
    fast_connect_provider_service.supported_virtual_circuit_types = [
        "PRIVATE",
        "PUBLIC",
    ]
    fast_connect_provider_service.type = "LAYER2"
    fast_connect_provider_services.append(fast_connect_provider_service)
    return fast_connect_provider_services


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {"compartment_id": "ocid1.compartment..axsd"}
    if additional_properties is not None:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
