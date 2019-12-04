# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_route_table_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import RouteTable, RouteRule
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_route_table_facts.py requires `oci` module")


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


def test_list_route_tables(virtual_network_client, list_all_resources_patch):
    module = get_module()
    route_table = get_route_table()
    list_all_resources_patch.return_value = [route_table]
    result = oci_route_table_facts.list_route_tables(virtual_network_client, module)
    assert result["route_tables"][0]["display_name"] == route_table.display_name


def test_list_route_tables_with_ig_id(virtual_network_client, list_all_resources_patch):
    module = get_module_with_ig_id()
    route_table = get_route_table()
    virtual_network_client.get_route_table.return_value = get_response(
        200, None, route_table, None
    )
    result = oci_route_table_facts.list_route_tables(virtual_network_client, module)
    assert result["route_tables"][0]["display_name"] == route_table.display_name


def test_list_route_tables_service_error(
    virtual_network_client, list_all_resources_patch
):
    error_message = "Internal Server Error"
    module = get_module()
    list_all_resources_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    try:
        result = oci_route_table_facts.list_route_tables(virtual_network_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def get_route_table():
    route_table = RouteTable()
    route_table.display_name = "ansible_route_table"
    route_table.compartment_id = "ocid1.compartment.oc1..aa"
    route_table.id = "ocid1.routetable.oc1.phx.aa"
    route_table.lifecycle_state = "AVAILABLE"
    route_table.route_rules = [get_common_route_rule()]
    route_table.time_created = "2017-11-15T16:48:06.784000+00:00"
    route_table.vcn_id = "ocid1.vcn.oc1.phx.aa"

    return route_table


def get_common_route_rule():
    route_rule = RouteRule()
    route_rule.cidr_block = "0.0.0.0/0"
    route_rule.network_entity_id = "oci1.internetgateway.abcd"
    return route_rule


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module():
    params = {
        "compartment_id": "ocid1.comp..axsd",
        "vcn_id": "ocid1.vcn..fxdv",
        "rt_id": "",
        "display_name": None,
    }
    module = FakeModule(**params)
    return module


def get_module_with_ig_id():
    params = {
        "compartment_id": "",
        "vcn_id": "",
        "rt_id": "ocid1.internetgateway..fxdv",
        "display_name": None,
    }
    module = FakeModule(**params)
    return module
