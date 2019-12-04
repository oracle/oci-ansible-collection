# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_virtual_circuit_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import VirtualCircuit
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
except ImportError:
    raise SkipTest("test_oci_virtual_circuit_facts.py requires `oci` module")


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


def test_list_cross_virtual_circuits_all(
    virtual_network_client, list_all_resources_patch
):
    module = get_module()
    virtual_circuits = get_virtual_circuits()
    list_all_resources_patch.return_value = virtual_circuits
    result = oci_virtual_circuit_facts.list_virtual_circuits(
        virtual_network_client, module
    )
    assert (
        result["virtual_circuits"][0]["display_name"]
        == virtual_circuits[0].display_name
    )


def test_list_virtual_circuits_specific(
    virtual_network_client, list_all_resources_patch
):
    module = get_module(dict(virtual_circuit_id="ocid1.virtualcircuit..vgfc"))
    virtual_circuits = get_virtual_circuits()
    list_all_resources_patch.return_value = virtual_circuits
    result = oci_virtual_circuit_facts.list_virtual_circuits(
        virtual_network_client, module
    )
    assert (
        result["virtual_circuits"][0]["display_name"]
        == virtual_circuits[0].display_name
    )


def get_virtual_circuits():
    virtual_circuits = []
    virtual_circuit = VirtualCircuit()
    virtual_circuit.display_name = "ansible_virtual_circuit"
    virtual_circuits.append(virtual_circuit)
    return virtual_circuits


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {"compartment_id": "ocid1.compartment..axsd"}
    if additional_properties is not None:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
