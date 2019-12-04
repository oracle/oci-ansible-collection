# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_virtual_circuit_public_prefix_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import VirtualCircuitPublicPrefix
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
except ImportError:
    raise SkipTest(
        "test_oci_virtual_circuit_public_prefix_facts.py requires `oci` module"
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


def test_list_cross_virtual_circuit_public_prefixes_all(
    virtual_network_client, list_all_resources_patch
):
    module = get_module()
    virtual_circuit_public_prefixes = get_virtual_circuit_public_prefixes()
    list_all_resources_patch.return_value = virtual_circuit_public_prefixes
    result = oci_virtual_circuit_public_prefix_facts.list_virtual_circuit_public_prefixes(
        virtual_network_client, module
    )
    assert (
        result["virtual_circuit_public_prefixes"][0]["cidr_block"]
        == virtual_circuit_public_prefixes[0].cidr_block
    )


def test_list_virtual_circuit_public_prefixes_specific(
    virtual_network_client, list_all_resources_patch
):
    module = get_module(
        dict(virtual_circuit_public_prefix_id="ocid1.virtualcircuitpublicprefix..vgfc")
    )
    virtual_circuit_public_prefixes = get_virtual_circuit_public_prefixes()
    list_all_resources_patch.return_value = virtual_circuit_public_prefixes
    result = oci_virtual_circuit_public_prefix_facts.list_virtual_circuit_public_prefixes(
        virtual_network_client, module
    )
    assert (
        result["virtual_circuit_public_prefixes"][0]["cidr_block"]
        == virtual_circuit_public_prefixes[0].cidr_block
    )


def get_virtual_circuit_public_prefixes():
    virtual_circuit_public_prefixes = []
    virtual_circuit_public_prefix = VirtualCircuitPublicPrefix()
    virtual_circuit_public_prefix.cidr_block = "10.0.0.18/31"
    virtual_circuit_public_prefixes.append(virtual_circuit_public_prefix)
    return virtual_circuit_public_prefixes


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {"compartment_id": "ocid1.compartment..axsd"}
    if additional_properties is not None:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
