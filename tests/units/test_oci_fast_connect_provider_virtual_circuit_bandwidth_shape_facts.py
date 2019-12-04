# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import (
    oci_fast_connect_provider_virtual_circuit_bandwidth_shape_facts,
)
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import VirtualCircuitBandwidthShape
except ImportError:
    raise SkipTest(
        "test_oci_fast_connect_provider_virtual_circuit_bandwidth_shape_facts.py requires `oci` module"
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


def test_list_fast_connect_provider_virtual_circuit_bandwidth_shapes_all(
    virtual_network_client, list_all_resources_patch
):
    module = get_module()
    fast_connect_provider_virtual_circuit_bandwidth_shapes = (
        get_fast_connect_provider_virtual_circuit_bandwidth_shapes()
    )
    list_all_resources_patch.return_value = (
        fast_connect_provider_virtual_circuit_bandwidth_shapes
    )
    result = oci_fast_connect_provider_virtual_circuit_bandwidth_shape_facts.list_fast_connect_provider_virtual_circuit_bandwidth_shapes(
        virtual_network_client, module
    )
    assert (
        result["fast_connect_provider_virtual_circuit_bandwidth_shapes"][0]["name"]
        == fast_connect_provider_virtual_circuit_bandwidth_shapes[0].name
    )


def get_fast_connect_provider_virtual_circuit_bandwidth_shapes():
    fast_connect_provider_virtual_circuit_bandwidth_shapes = []
    virtual_circuit_bandwidth_shape = VirtualCircuitBandwidthShape()
    virtual_circuit_bandwidth_shape.bandwidth_in_mbps = 1000
    virtual_circuit_bandwidth_shape.name = "1 Mbps"
    fast_connect_provider_virtual_circuit_bandwidth_shapes.append(
        virtual_circuit_bandwidth_shape
    )
    return fast_connect_provider_virtual_circuit_bandwidth_shapes


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {"provider_service_id": "ocid1.serviceprovider..axsd"}
    if additional_properties is not None:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
