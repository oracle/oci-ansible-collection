# Copyright (c) 2017, 2018, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_route_table
from ansible.module_utils.oracle import oci_utils
import json

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import RouteTable, RouteRule
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
except ImportError:
    raise SkipTest("test_oci_route_table.py requires `oci` module")


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
    virtual_network_client = mocker.patch("oci.core.VirtualNetworkClient")
    return virtual_network_client.return_value


@pytest.fixture()
def update_route_table_patch(mocker):
    return mocker.patch.object(oci_route_table, "update_route_table")


@pytest.fixture()
def get_existing_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "get_existing_resource")


@pytest.fixture()
def create_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "create_and_wait")


@pytest.fixture()
def update_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "update_and_wait")


@pytest.fixture()
def delete_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "delete_and_wait")


@pytest.fixture()
def check_and_create_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_create_resource")


def test_create_or_update_route_table_create(
    virtual_network_client, check_and_create_resource_patch
):
    route_table = get_route_table()
    module = get_module(None)
    check_and_create_resource_patch.return_value = dict(
        changed=True, route_table=route_table
    )
    result = oci_route_table.create_or_update_route_table(
        virtual_network_client, module
    )
    assert result["changed"] is True


def test_create_or_update_route_table_update(
    virtual_network_client, update_route_table_patch, get_existing_resource_patch
):
    route_table = get_route_table()
    module = get_module(dict({"rt_id": "ocid1.routetable..xvfd"}))
    update_route_table_patch.return_value = dict(changed=True, route_table=route_table)
    result = oci_route_table.create_or_update_route_table(
        virtual_network_client, module
    )
    assert result["changed"] is True


def test_create_or_update_route_service_error(
    virtual_network_client, check_and_create_resource_patch
):
    error_message = "Internal Server Error"
    module = get_module(None)
    check_and_create_resource_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_route_table.create_or_update_route_table(virtual_network_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_route_timeout_error(
    virtual_network_client, check_and_create_resource_patch
):
    error_message = "Time Out Error"
    module = get_module(None)
    check_and_create_resource_patch.side_effect = MaximumWaitTimeExceeded(
        499, "TimeoutError", dict(), error_message
    )
    try:
        oci_route_table.create_or_update_route_table(virtual_network_client, module)
    except Exception as ex:
        assert error_message in ex.args[0].__repr__()


def test_create_route_table(virtual_network_client, create_and_wait_patch):
    route_table = get_route_table()
    route_rules = [
        {"cidr_block": "0.0.0.0/0", "network_entity_id": "10.0.10.5"},
        {"cidr_block": "10.0.0.4/16", "network_entity_id": "10.0.20.5"},
    ]
    module = get_module(dict({"route_rules": route_rules}))
    create_and_wait_patch.return_value = dict(
        changed=True, route_table=to_dict(route_table)
    )
    result = oci_route_table.create_route_table(virtual_network_client, module)
    assert result["route_table"]["display_name"] == route_table.display_name


def test_update_route_table_no_route_table_for_update(virtual_network_client):
    error_message = "No Route Table"
    module = get_module(dict(rt_id="ocid1.routetable..xvdf"))
    try:
        oci_route_table.update_route_table(virtual_network_client, None, module)
    except Exception as ex:
        assert error_message in str(ex.args)


def test_update_route_table_name_changed(virtual_network_client, update_and_wait_patch):
    route_table = get_route_table()
    module = get_module(dict(display_name="updated_ansible_route_table"))
    update_and_wait_patch.return_value = dict(changed=True, route_table=route_table)
    result = oci_route_table.update_route_table(
        virtual_network_client, route_table, module
    )
    assert result["changed"] is True


def test_update_route_table_freeform_tags_changed(
    virtual_network_client, update_and_wait_patch
):
    route_table = get_route_table()
    module = get_module(dict(freeform_tags=dict(route_type="intranet")))
    update_and_wait_patch.return_value = dict(changed=True, route_table=route_table)
    result = oci_route_table.update_route_table(
        virtual_network_client, route_table, module
    )
    assert result["changed"] is True


def test_update_route_table_defined_tags_changed(
    virtual_network_client, update_and_wait_patch
):
    route_table = get_route_table()
    module = get_module(
        dict(defined_tags=dict(admin_type=dict(admin_role="limited_user")))
    )
    update_and_wait_patch.return_value = dict(changed=True, route_table=route_table)
    result = oci_route_table.update_route_table(
        virtual_network_client, route_table, module
    )
    assert result["changed"] is True


def test_update_route_table_input_route_rules_different(
    virtual_network_client, update_and_wait_patch
):
    route_table = get_route_table()
    route_rules = [
        {"cidr_block": "0.0.0.0/0", "network_entity_id": "oci1.internetgateway.abcd"},
        {"cidr_block": "10.0.0.4/16", "network_entity_id": "oci1.internetgateway.efgh"},
    ]
    module = get_module(dict(route_rules=route_rules))
    update_and_wait_patch.return_value = dict(
        changed=True, route_table=to_dict(route_table)
    )
    result = oci_route_table.update_route_table(
        virtual_network_client, route_table, module
    )
    assert result["changed"] is True


def test_update_route_table_service_cidr_input_route_rules_different(
    virtual_network_client, update_and_wait_patch
):
    route_table = get_route_table()
    route_table.route_rules = [get_service_cidr_route_rule()]
    route_rules = [
        {
            "destination": "oci-ashburn-objectstorage",
            "destination_type": RouteRule.DESTINATION_TYPE_SERVICE_CIDR_BLOCK,
            "network_entity_id": "oci1.internetgateway.abcd",
        }
    ]
    module = get_module(dict(route_rules=route_rules))
    update_and_wait_patch.return_value = dict(
        changed=True, route_table=to_dict(route_table)
    )
    result = oci_route_table.update_route_table(
        virtual_network_client, route_table, module
    )
    assert result["changed"] is True


def test_update_route_table_empty_input_route_rules(
    virtual_network_client, update_and_wait_patch
):
    route_table = get_route_table()
    route_rules = []
    module = get_module(dict(route_rules=route_rules))
    update_and_wait_patch.return_value = dict(
        changed=True, route_table=to_dict(route_table)
    )
    result = oci_route_table.update_route_table(
        virtual_network_client, route_table, module
    )
    assert result["changed"] is True


def test_update_route_table_input_no_route_rules_different(
    virtual_network_client, update_and_wait_patch
):
    route_table = get_route_table()
    route_rules = [
        {"cidr_block": "10.0.0.0/12", "network_entity_id": "oci1.internetgateway.ijkl"},
        {"cidr_block": "10.0.0.0/16", "network_entity_id": "oci1.internetgateway.efgh"},
    ]
    module = get_module(dict(route_rules=route_rules))
    update_and_wait_patch.return_value = dict(
        changed=False, route_table=to_dict(route_table)
    )
    result = oci_route_table.update_route_table(
        virtual_network_client, route_table, module
    )
    assert result["changed"] is False


def test_delete_route_table(virtual_network_client, delete_and_wait_patch):
    route_table = get_route_table()
    module = get_module(dict(rt_id="ocid.routetable..xvdz"))
    delete_and_wait_patch.return_value = dict(
        changed=True, route_table=to_dict(route_table)
    )
    result = oci_route_table.delete_route_table(virtual_network_client, module)
    assert result["changed"] is True


def test_delete_route_table_rt_not_exists(
    virtual_network_client, delete_and_wait_patch
):
    module = get_module(dict(rt_id="ocid.routetable..xvdz"))
    delete_and_wait_patch.return_value = dict(changed=False, route_table="")
    result = oci_route_table.delete_route_table(virtual_network_client, module)
    assert result["changed"] is False


def test_get_route_rules_difference_no_existing_route_rule(virtual_network_client):
    route_table = get_route_table()
    route_table.route_rules = []
    route_rules = [
        {"cidr_block": "0.0.0.0/0", "network_entity_id": "oci1.internetgateway.abcd"},
        {"cidr_block": "10.0.0.4/16", "network_entity_id": "oci1.internetgateway.efgh"},
    ]

    result_rt, result = oci_utils.get_component_list_difference(route_rules, None, True)
    assert result is True
    assert len(result_rt) is 2


def test_get_route_rules_difference_no_purge_same_rule(virtual_network_client):
    route_table = get_route_table()
    dummy, result = oci_utils.get_component_list_difference(
        get_hashed_route_rules(route_table.route_rules),
        get_hashed_route_rules(route_table.route_rules),
        True,
    )
    assert result is False


def test_get_route_rules_difference_append_different_rule():
    route_table = get_route_table()
    result_rt, result = oci_utils.get_component_list_difference(
        get_hashed_route_rules(get_route_rules()),
        get_hashed_route_rules(route_table.route_rules),
        False,
    )
    assert result is True
    assert len(result_rt) is 3


def get_route_rules_difference_append_only_different_rules():
    route_table = get_route_table()
    result_rt, result = oci_utils.get_component_list_difference(
        get_route_rules(), route_table.route_rules, False
    )
    assert result is True
    assert len(result_rt) is 3


def test_get_route_rules_difference_no_different_rules():
    existing_route_rules = get_route_rules() + [(get_common_route_rule())]
    dummy, result = oci_utils.get_component_list_difference(
        get_hashed_route_rules([get_common_route_rule()]),
        get_hashed_route_rules(existing_route_rules),
        False,
    )
    assert result is False


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_route_table():
    route_table = RouteTable()
    route_table.display_name = "ansible_route_table"
    route_table.compartment_id = "ocid1.compartment.oc1..aa"
    route_table.id = "ocid1.routetable.oc1.phx.aa"
    route_table.lifecycle_state = "AVAILABLE"
    route_table.route_rules = [get_common_route_rule()]
    route_table.time_created = "2017-11-15T16:48:06.784000+00:00"
    route_table.vcn_id = "ocid1.vcn.oc1.phx.aa"
    route_table.freeform_tags = {"route_type": "internet"}
    route_table.defined_tags = {"admin_type": {"admin_role": "super_user"}}

    return route_table


def get_common_route_rule():
    route_rule = RouteRule()
    route_rule.cidr_block = "0.0.0.0/0"
    route_rule.destination = "0.0.0.0/0"
    route_rule.destination_type = RouteRule.DESTINATION_TYPE_CIDR_BLOCK
    route_rule.network_entity_id = "oci1.internetgateway.abcd"
    return route_rule


def get_service_cidr_route_rule():
    route_rule = RouteRule()
    route_rule.destination = "oci-phx-objectstorage"
    route_rule.destination_type = RouteRule.DESTINATION_TYPE_SERVICE_CIDR_BLOCK
    route_rule.network_entity_id = "oci1.servicegateway.abcd"
    return route_rule


def get_route_rules():
    route_rule1 = RouteRule()
    route_rule2 = RouteRule()
    route_rule1.cidr_block = "10.0.0.0/12"
    route_rule1.network_entity_id = "oci1.internetgateway.ijkl"
    route_rule2.cidr_block = "10.0.0.0/16"
    route_rule2.network_entity_id = "oci1.internetgateway.efgh"
    return [route_rule1, route_rule2]


def get_hashed_route_rules(route_rules):
    route_rules_reprs = []
    supported_route_rule_attributes = ["cidr_block", "network_entity_id"]
    for route_rule in route_rules:
        hashed_route_rule = oci_utils.get_hashed_object(
            RouteRule, route_rule, supported_attributes=supported_route_rule_attributes
        )
        route_rules_reprs.append(hashed_route_rule)
    return route_rules_reprs


def get_module(additional_properties):
    params = {
        "display_name": "ansible_route_table",
        "compartment_id": "ocid1.compartment.xvds",
        "vcn_id": "ocid1.vcn..kjsd",
        "route_rules": [
            {
                "cidr_block": "0.0.0.0/0",
                "network_entity_id": "oci1.internetgateway.abcd",
            }
        ],
        "purge_route_rules": False,
        "delete_route_rules": False,
    }
    if additional_properties:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
