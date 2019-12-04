# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_virtual_circuit
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import VirtualCircuit, CrossConnectMapping
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
except ImportError:
    raise SkipTest("test_oci_virtual_circuit.py requires `oci` module")


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
def create_virtual_circuit_patch(mocker):
    return mocker.patch.object(oci_virtual_circuit, "create_virtual_circuit")


@pytest.fixture()
def update_virtual_circuit_patch(mocker):
    return mocker.patch.object(oci_virtual_circuit, "update_virtual_circuit")


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
def update_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "update_and_wait")


@pytest.fixture()
def delete_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "delete_and_wait")


def test_create_or_update_cross_connect_create_success(
    virtual_network_client, check_and_create_resource_patch
):
    virtual_circuit = get_virtual_circuit()
    module = get_module(dict())
    check_and_create_resource_patch.return_value = dict(
        {"virtual_circuit": virtual_circuit, "changed": True}
    )
    result = oci_virtual_circuit.create_or_update_virtual_circuit(
        virtual_network_client, module
    )
    assert result["virtual_circuit"].display_name == virtual_circuit.display_name
    assert result["changed"] is True


def test_create_or_update_cross_connect_update_success(
    virtual_network_client, update_virtual_circuit_patch
):
    virtual_circuit = get_virtual_circuit()
    module = get_module(dict({"virtual_circuit_id": "ocid1.virtualcircuit..xvdf"}))
    get_existing_resource_patch.return_value = virtual_circuit
    update_virtual_circuit_patch.return_value = dict(
        changed=True, virtual_circuit=to_dict(virtual_circuit)
    )
    result = oci_virtual_circuit.create_or_update_virtual_circuit(
        virtual_network_client, module
    )
    assert result["virtual_circuit"]["display_name"] == virtual_circuit.display_name
    assert result["changed"] is True


def test_create_or_update_virtual_circuit_service_error(
    virtual_network_client, update_virtual_circuit_patch
):
    error_message = "Internal Server Error"
    module = get_module(dict({"virtual_circuit_id": "ocid1.virtualcircuit.xvdf"}))
    update_virtual_circuit_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    try:
        oci_virtual_circuit.create_or_update_virtual_circuit(
            virtual_network_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_virtual_circuit_timeout_error(
    virtual_network_client, update_virtual_circuit_patch
):
    error_message = "Maximum Timeout Reached"
    module = get_module(dict({"virtual_circuit_id": "ocid1.virtualcircuit.xvdf"}))
    update_virtual_circuit_patch.side_effect = MaximumWaitTimeExceeded(
        500, "TimeOutError", dict(), error_message
    )
    try:
        oci_virtual_circuit.create_or_update_virtual_circuit(
            virtual_network_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0].__repr__()


def test_create_virtual_circuit(virtual_network_client, create_and_wait_patch):
    module = get_module(dict({"type": "PUBLIC"}))
    virtual_circuit = get_virtual_circuit()
    create_and_wait_patch.return_value = dict(
        {"virtual_circuit": to_dict(virtual_circuit), "changed": True}
    )
    result = oci_virtual_circuit.create_virtual_circuit(virtual_network_client, module)
    assert result["virtual_circuit"]["display_name"] == virtual_circuit.display_name


def test_create_virtual_circuit_fail_no_bgp_peering_ip_for_public(
    virtual_network_client, create_and_wait_patch
):
    error_message = "oracle_bgp_peering_ip or customer_bgp_peering_ip is not allowed for public virual circuit"
    module = get_module(
        dict(
            {
                "type": "PUBLIC",
                "cross_connect_mappings": [
                    dict({"customer_bgp_peering_ip": "10.0.0.21/31"})
                ],
            }
        )
    )
    try:
        oci_virtual_circuit.create_virtual_circuit(virtual_network_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_virtual_circuit_fail_mandatory_bgp_peering_ips_for_private(
    virtual_network_client, create_and_wait_patch
):
    error_message = "oracle_bgp_peering_ip and customer_bgp_peering_ip are mandatory for private virual circuit"
    module = get_module(
        dict(
            {
                "type": "PRIVATE",
                "cross_connect_mappings": [
                    dict({"customer_bgp_peering_ip": "10.0.0.21/31"})
                ],
            }
        )
    )
    try:
        oci_virtual_circuit.create_virtual_circuit(virtual_network_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_update_virtual_circuit_success_display_name_changed(
    virtual_network_client, update_and_wait_patch
):
    module = get_module(
        dict(
            display_name="ansible_virtual_circuit_updated",
            cross_connect_id="ocid1.crossconnect..xvzf",
            cross_connect_mappings=[dict({"vlan": 101})],
        )
    )
    virtual_circuit = get_virtual_circuit()
    update_and_wait_patch.return_value = dict(
        {"virtual_circuit": virtual_circuit, "changed": True}
    )
    oci_virtual_circuit.update_virtual_circuit(
        virtual_network_client, virtual_circuit, module
    )
    assert update_and_wait_patch.called


def test_update_virtual_circuit_success_cross_connect_mappings_changed(
    virtual_network_client, update_and_wait_patch
):
    module = get_module(
        dict(
            virtual_circuit_id_id="ocid1.virtualcircuit..xvzf",
            cross_connect_mappings=[dict({"vlan": 105})],
        )
    )
    virtual_circuit = get_virtual_circuit()
    update_and_wait_patch.return_value = dict(
        {"virtual_circuit": virtual_circuit, "changed": True}
    )
    oci_virtual_circuit.update_virtual_circuit(
        virtual_network_client, virtual_circuit, module
    )
    assert update_and_wait_patch.called


def test_update_virtual_circuit_success_bulk_add_public_prefixes(
    virtual_network_client, update_and_wait_patch
):
    module = get_module(
        dict(
            virtual_circuit_id="ocid1.virtualcircuit..xvzf",
            public_prefixes=["0.0.0.18/31"],
        )
    )
    virtual_circuit = get_virtual_circuit()
    update_and_wait_patch.return_value = dict(
        {"virtual_circuit": virtual_circuit, "changed": True}
    )
    oci_virtual_circuit.update_virtual_circuit(
        virtual_network_client, virtual_circuit, module
    )
    assert update_and_wait_patch.called


def test_update_virtual_circuit_success_bulk_delete_public_prefixes(
    virtual_network_client, update_and_wait_patch
):
    module = get_module(
        dict(
            virtual_circuit_id="ocid1.virtualcircuit..xvzf",
            public_prefixes=["0.0.0.18/31"],
            delete_public_prefixes=True,
        )
    )
    virtual_circuit = get_virtual_circuit()
    update_and_wait_patch.return_value = dict(
        {"virtual_circuit": virtual_circuit, "changed": True}
    )
    oci_virtual_circuit.update_virtual_circuit(
        virtual_network_client, virtual_circuit, module
    )
    assert update_and_wait_patch.called


def test_delete_virtual_circuit(virtual_network_client, delete_and_wait_patch):
    virtual_circuit = get_virtual_circuit()
    module = get_module(dict({"virtual_circuit_id": "ocid1.virtualcircuit..xvzf"}))
    get_existing_resource_patch.return_value = virtual_circuit
    oci_virtual_circuit.delete_virtual_circuit(virtual_network_client, module)
    assert delete_and_wait_patch.called


def get_virtual_circuit():
    virtual_circuit = VirtualCircuit()
    virtual_circuit.compartment_id = "ocid1.compartment..axsd"
    virtual_circuit.display_name = "ansible_virtual_circuit"
    cross_connect_mapping = CrossConnectMapping()
    cross_connect_mapping.customer_bgp_peering_ip = "10.0.0.18/30"
    cross_connect_mapping.oracle_bgp_peering_ip = "10.0.0.19/30"
    cross_connect_mapping.vlan = 101
    cross_connect_mapping.cross_connect_or_cross_connect_group_id = (
        "ocid1.crossconnect..xvdf"
    )
    virtual_circuit.cross_connect_mappings = [cross_connect_mapping]
    virtual_circuit.customer_bgp_asn = 5
    virtual_circuit.display_name = "ansible_cross_connect"
    virtual_circuit.type = "PUBLIC"

    return virtual_circuit


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = {"compartment_id": "ocid1.comp..axsd"}
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
