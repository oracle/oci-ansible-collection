# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_security_list
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import (
        CreateSecurityListDetails,
        SecurityList,
        UpdateSecurityListDetails,
        IngressSecurityRule,
        EgressSecurityRule,
        IcmpOptions,
        TcpOptions,
        UdpOptions,
        PortRange,
    )
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
except ImportError:
    raise SkipTest("test_oci_security_list.py requires `oci` module")


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
    mock_identity_client = mocker.patch("oci.core.VirtualNetworkClient")
    return mock_identity_client.return_value


@pytest.fixture()
def oci_wait_until_patch(mocker):
    return mocker.patch.object(oci, "wait_until")


@pytest.fixture()
def get_security_rules_patch(mocker):
    return mocker.patch.object(oci_security_list, "get_security_rules")


@pytest.fixture()
def create_security_list_patch(mocker):
    return mocker.patch.object(oci_security_list, "create_security_list")


@pytest.fixture()
def update_security_list_patch(mocker):
    return mocker.patch.object(oci_security_list, "update_security_list")


@pytest.fixture()
def check_and_create_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_create_resource")


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


def test_create_or_update_security_list_create(
    virtual_network_client, check_and_create_resource_patch
):
    security_list = get_security_list(None, None, "ansible_security_list")
    module = get_module(
        dict({"compartment_id": "ocid1.compartment.aa", "vcn_id": "ocid1.vcn.aa"})
    )
    check_and_create_resource_patch.return_value = dict(
        {"security_list": to_dict(security_list), "changed": True}
    )
    result = oci_security_list.create_or_update_security_list(
        virtual_network_client, module
    )
    assert result["changed"] is True
    result["security_list"]["display_name"] is security_list.display_name


def test_create_or_update_security_list_update(
    virtual_network_client, update_security_list_patch, get_existing_resource_patch
):
    security_list = get_security_list(None, None, "ansible_security_list")
    module = get_module(dict({"security_list_id": "ocid1.securitylist.aa"}))
    get_existing_resource_patch.return_value = security_list
    update_security_list_patch.return_value = dict(
        {"security_list": to_dict(security_list), "changed": True}
    )
    result = oci_security_list.create_or_update_security_list(
        virtual_network_client, module
    )
    assert result["changed"] is True
    assert result["security_list"]["display_name"] is security_list.display_name


def test_create_or_update_security_list_service_error(
    virtual_network_client, check_and_create_resource_patch
):
    error_message = "Internal Server Error"
    module = get_module(
        dict({"compartment_id": "ocid1.compartment.aa", "vcn_id": "ocid1.vcn.aa"})
    )
    check_and_create_resource_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_security_list.create_or_update_security_list(virtual_network_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_security_list_timeout_error(
    virtual_network_client, check_and_create_resource_patch
):
    error_message = "Time Out Error"
    module = get_module(
        dict({"compartment_id": "ocid1.compartment.aa", "vcn_id": "ocid1.vcn.aa"})
    )
    check_and_create_resource_patch.side_effect = MaximumWaitTimeExceeded(
        500, "TimeoutError", dict(), error_message
    )
    try:
        oci_security_list.create_or_update_security_list(virtual_network_client, module)
    except Exception as ex:
        assert error_message in ex.args[0].__repr__()


def test_create_security_list(virtual_network_client, create_and_wait_patch):
    ingress_security_rules = [
        {
            "icmp_options": None,
            "is_stateless": None,
            "protocol": "6",
            "source": "0.0.0.0/0",
            "source_type": "CIDR_BLOCK",
            "tcp_options": {
                "destination_port_range": {"max": 22, "min": 22},
                "source_port_range": None,
            },
            "udp_options": None,
        },
        {
            "icmp_options": {"code": 4, "type": 3},
            "is_stateless": None,
            "protocol": "1",
            "source": "0.0.0.0/0",
            "tcp_options": None,
            "udp_options": None,
        },
    ]
    egress_security_rules = [
        {
            "destination": "0.0.0.0/0",
            "protocol": "17",
            "udp_options": {
                "source_port_range": {"max": 22, "min": 22},
                "destination_port_range": None,
            },
        }
    ]
    module = get_module(
        dict(
            {
                "egress_security_rules": egress_security_rules,
                "ingress_security_rules": ingress_security_rules,
            }
        )
    )
    security_list = get_security_list(
        egress_security_rules, egress_security_rules, "ansible_security_list"
    )
    create_and_wait_patch.return_value = dict(
        {"security_list": to_dict(security_list), "changed": True}
    )
    result = oci_security_list.create_security_list(virtual_network_client, module)
    assert result["security_list"]["id"] == security_list.id


def test_update_security_list_no_security_list_for_update(virtual_network_client):
    error_message = "No Security List"
    module = get_module(dict(security_list_id="ocid1.securitylist..xvdf"))
    try:
        oci_security_list.update_security_list(virtual_network_client, None, module)
    except Exception as ex:
        assert error_message in str(ex.args)


def test_update_security_list_name_changed(
    virtual_network_client, update_and_wait_patch
):
    module = get_module(
        dict(
            {
                "egress_security_rules": None,
                "ingress_security_rules": None,
                "purge_security_rules": True,
            }
        )
    )
    security_list = get_security_list(None, None, "ansible_security_list_updated")
    update_and_wait_patch.return_value = dict(
        {"security_list": to_dict(security_list), "changed": True}
    )
    result = oci_security_list.update_security_list(
        virtual_network_client, security_list, module
    )

    assert result["changed"] is True


def test_update_security_list_freeform_tags_changed(
    virtual_network_client, update_and_wait_patch
):
    module = get_module(dict(freeform_tags=dict(security_level="strict")))
    security_list = get_security_list(None, None, "ansible_security_list")
    update_and_wait_patch.return_value = dict(
        {"security_list": to_dict(security_list), "changed": True}
    )
    result = oci_security_list.update_security_list(
        virtual_network_client, security_list, module
    )

    assert result["changed"] is True


def test_update_security_list_defined_tags_changed(
    virtual_network_client, update_and_wait_patch
):
    module = get_module(
        dict(defined_tags=dict(department=dict(department_type="commericial")))
    )
    security_list = get_security_list(None, None, "ansible_security_list")
    update_and_wait_patch.return_value = dict(
        {"security_list": to_dict(security_list), "changed": True}
    )
    result = oci_security_list.update_security_list(
        virtual_network_client, security_list, module
    )

    assert result["changed"] is True


def test_get_security_rules_difference_ingress_tcp_options_append():
    input_ingress_rules = get_security_rules(
        "ingress",
        "hashed",
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        False,
        None,
        None,
        None,
        "3",
        "4",
    )

    existing_ingress_rules = get_security_rules(
        "ingress",
        "hashed",
        "10.0.0.0/8",
        "0.0.0.0/0",
        "10.0.0.0/16",
        False,
        None,
        None,
        None,
        "3",
        "4",
    )

    result, changed = oci_utils.get_component_list_difference(
        input_ingress_rules, existing_ingress_rules, False
    )

    assert changed is True
    assert result[0].source == "10.0.0.0/0"


def test_get_security_rules_difference_ingress_udp_options_append():
    input_ingress_rules = get_security_rules(
        "ingress",
        "hashed",
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/12",
        False,
        None,
        None,
        None,
        "3",
        "4",
    )

    existing_ingress_rules = get_security_rules(
        "ingress",
        "hashed",
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        False,
        None,
        None,
        None,
        "3",
        "4",
    )

    result, changed = oci_utils.get_component_list_difference(
        input_ingress_rules, existing_ingress_rules, False
    )

    assert changed is True
    assert result[0].source == "10.0.0.0/12"


def test_get_security_rules_difference_ingress_icmp_options_append():
    input_ingress_rules = get_security_rules(
        "ingress",
        "hashed",
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        False,
        None,
        None,
        None,
        "3",
        "4",
    )

    existing_ingress_rules = get_security_rules(
        "ingress",
        "hashed",
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        False,
        None,
        None,
        None,
        "3",
        None,
    )

    result, changed = oci_utils.get_component_list_difference(
        existing_ingress_rules, input_ingress_rules, False
    )

    assert changed is True
    assert result[0].source == "0.0.0.0/0"


def test_get_security_rules_difference_ingress_tcp_options_purge():
    input_ingress_rules = get_security_rules(
        "ingress",
        "hashed",
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        False,
        None,
        None,
        None,
        "3",
        "4",
    )

    existing_ingress_rules = get_security_rules(
        "ingress",
        "hashed",
        "10.0.0.0/8",
        "0.0.0.0/0",
        "10.0.0.0/16",
        False,
        None,
        None,
        None,
        "3",
        "4",
    )

    result, changed = oci_utils.get_component_list_difference(
        input_ingress_rules, existing_ingress_rules, True
    )

    assert changed is True
    assert len(result) is 3


def test_get_security_rules_difference_ingress_udp_options_purge():
    input_ingress_rules = get_security_rules(
        "ingress",
        "hashed",
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/12",
        False,
        None,
        None,
        None,
        "3",
        "4",
    )

    existing_ingress_rules = get_security_rules(
        "ingress",
        "hashed",
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        False,
        None,
        None,
        None,
        "3",
        "4",
    )

    result, changed = oci_utils.get_component_list_difference(
        existing_ingress_rules, input_ingress_rules, True
    )

    assert changed is True
    assert len(result) is 3


def test_get_security_rules_difference_ingress_icmp_options_purge():
    input_ingress_rules = get_security_rules(
        "ingress",
        "hashed",
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        False,
        None,
        None,
        None,
        "3",
        "4",
    )

    existing_ingress_rules = get_security_rules(
        "ingress",
        "hashed",
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        False,
        None,
        None,
        None,
        "3",
        None,
    )

    result, changed = oci_utils.get_component_list_difference(
        existing_ingress_rules, input_ingress_rules, True
    )

    assert changed is True
    assert len(result) is 3


def test_get_security_rules_difference_egress_tcp_options_append():
    input_egress_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        False,
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        "3",
        "4",
    )

    existing_egress_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        False,
        "10.0.0.0/8",
        "0.0.0.0/0",
        "10.0.0.0/16",
        "3",
        "4",
    )

    result, changed = oci_utils.get_component_list_difference(
        input_egress_rules, existing_egress_rules, False
    )
    assert changed is True
    assert result[0].destination == "10.0.0.0/0"


def test_get_security_rules_difference_egress_udp_options_append():
    input_egress_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        False,
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        "3",
        "4",
    )

    existing_egress_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        False,
        "10.0.0.0/0",
        "10.0.0.0/0",
        "10.0.0.0/16",
        "3",
        "4",
    )

    result, changed = oci_utils.get_component_list_difference(
        input_egress_rules, existing_egress_rules, False
    )
    assert changed is True
    assert result[0].destination == "0.0.0.0/0"


def test_get_security_rules_difference_egress_icmp_options_append():
    input_egress_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        False,
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        "3",
        "4",
    )

    existing_egress_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        False,
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        "3",
        None,
    )

    result, changed = oci_utils.get_component_list_difference(
        input_egress_rules, existing_egress_rules, False
    )
    assert changed is True
    assert result[0].destination == "10.0.0.0/16"


def test_get_security_rules_difference_egress_state_changed():
    input_egress_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        True,
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        "3",
        "4",
    )

    existing_egress_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        False,
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        "3",
        "4",
    )

    result, changed = oci_utils.get_component_list_difference(
        input_egress_rules, existing_egress_rules, False
    )
    assert changed is True
    assert len(result) is 6


def test_get_security_rules_difference_egress_tcp_options_purge():
    input_egress_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        False,
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        "3",
        "4",
    )

    existing_egress_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        False,
        "10.0.0.0/8",
        "0.0.0.0/0",
        "10.0.0.0/16",
        "3",
        "4",
    )

    result, changed = oci_utils.get_component_list_difference(
        input_egress_rules, existing_egress_rules, True
    )
    assert changed is True
    assert len(result) is 3


def test_get_security_rules_difference_egress_udp_options_purge():
    input_egress_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        False,
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        "3",
        "4",
    )

    existing_egress_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        False,
        "10.0.0.0/0",
        "10.0.0.0/0",
        "10.0.0.0/16",
        "3",
        "4",
    )

    result, changed = oci_utils.get_component_list_difference(
        input_egress_rules, existing_egress_rules, True
    )
    assert changed is True
    assert len(result) is 3


def test_get_security_rules_difference_egress_icmp_options_purge():
    input_egress_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        False,
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        "3",
        "4",
    )

    existing_egress_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        False,
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        "3",
        None,
    )

    result, changed = oci_utils.get_component_list_difference(
        input_egress_rules, existing_egress_rules, True
    )
    assert changed is True
    assert len(result) is 3


def test_get_security_rules_difference_no_existing_rule():
    input_ingress_rules = get_security_rules(
        "ingress",
        "hashed",
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        False,
        None,
        None,
        None,
        "3",
        "4",
    )

    result, changed = oci_utils.get_component_list_difference(
        input_ingress_rules, None, True
    )

    assert changed is True
    assert len(result) is 3


def test_get_final_security_rules_empty_input_security_rule():
    existing_egress_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        False,
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        "3",
        None,
    )

    result, changed = oci_utils.check_and_return_component_list_difference(
        None, existing_egress_rules, False
    )
    assert changed is True
    assert not result


def test_get_final_security_rules_rule_changed(get_security_rules_patch):
    final_security_rules = get_security_rules(
        "egress",
        "hashed",
        None,
        None,
        None,
        False,
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        "3",
        None,
    )

    result, changed = oci_utils.check_and_return_component_list_difference(
        final_security_rules, None, False
    )
    assert changed is True
    assert len(result) is 3


def test_delete_security_list(virtual_network_client, delete_and_wait_patch):
    module = get_module(dict({"security_list_id": "ocid1.securitylist..aaaa"}))
    security_list = get_security_list(None, None, "ansible_security_list")
    delete_and_wait_patch.return_value = dict(
        {"security_list": to_dict(security_list), "changed": True}
    )
    result = oci_security_list.delete_security_list(virtual_network_client, module)
    assert result["changed"] is True


def test_get_security_rules_difference_ingress_same_rules_state_unchanged():
    input_ingress_rules = get_security_rules(
        "ingress",
        "hashed",
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        False,
        None,
        None,
        None,
        "3",
        "4",
    )

    existing_ingress_rules = get_security_rules(
        "ingress",
        "hashed",
        "10.0.0.0/0",
        "0.0.0.0/0",
        "10.0.0.0/16",
        False,
        None,
        None,
        None,
        "3",
        "4",
    )

    result, changed = oci_utils.get_component_list_difference(
        existing_ingress_rules, input_ingress_rules, False
    )

    assert changed is False


def test_create_or_update_security_list_fails_when_egress_security_rules_are_not_passed(
    get_existing_resource_patch, check_and_create_resource_patch, virtual_network_client
):
    module = get_module(dict(egress_security_rules=None))
    with pytest.raises(Exception) as exc_info:
        oci_security_list.create_or_update_security_list(virtual_network_client, module)
    ex = exc_info.value
    assert (
        "ingress_security_rules and egress_security_rules are required for creating security list"
        in str(ex)
    )
    assert check_and_create_resource_patch.call_count == 0


def test_create_or_update_security_list_fails_when_ingress_security_rules_are_not_passed(
    get_existing_resource_patch, check_and_create_resource_patch, virtual_network_client
):
    module = get_module(dict(ingress_security_rules=None))
    with pytest.raises(Exception) as exc_info:
        oci_security_list.create_or_update_security_list(virtual_network_client, module)
    ex = exc_info.value
    assert (
        "ingress_security_rules and egress_security_rules are required for creating security list"
        in str(ex)
    )
    assert check_and_create_resource_patch.call_count == 0


def get_security_rules(
    security_rule_type,
    security_rule_flavour,
    tcp_source,
    icmp_source,
    udp_source,
    stateless,
    tcp_destination,
    udp_destination,
    icmp_destination,
    icmp_type,
    icmp_code,
):
    security_rules = []
    security_rule_tcp = None
    security_rule_icmp = None
    security_rule_udp = None
    tcp_options = None
    tcp_source_port_range = None
    tcp_destination_port_range = None
    udp_options = None
    udp_source_port_range = None
    udp_destination_port_range = None
    icmp_options = None
    if security_rule_type == "ingress":
        if security_rule_flavour == "hashed":
            security_rule_tcp = oci_utils.create_hashed_instance(IngressSecurityRule)
            security_rule_tcp.source = tcp_source
            tcp_options = oci_utils.create_hashed_instance(TcpOptions)
            tcp_source_port_range = oci_utils.create_hashed_instance(PortRange)
            tcp_destination_port_range = oci_utils.create_hashed_instance(PortRange)
            security_rule_udp = oci_utils.create_hashed_instance(IngressSecurityRule)
            security_rule_udp.source = udp_source
            udp_options = oci_utils.create_hashed_instance(UdpOptions)
            udp_source_port_range = oci_utils.create_hashed_instance(PortRange)
            udp_destination_port_range = oci_utils.create_hashed_instance(PortRange)
            security_rule_icmp = oci_utils.create_hashed_instance(IngressSecurityRule)
            security_rule_icmp.source = icmp_source
            icmp_options = oci_utils.create_hashed_instance(IcmpOptions)
        else:
            security_rule_tcp = IngressSecurityRule()
            security_rule_tcp.source = tcp_source
            tcp_options = TcpOptions()
            tcp_source_port_range = PortRange()
            tcp_destination_port_range = PortRange()
            security_rule_udp = IngressSecurityRule()
            security_rule_udp.source = udp_source
            udp_options = UdpOptions()
            udp_source_port_range = PortRange()
            udp_destination_port_range = PortRange()
            security_rule_icmp = IngressSecurityRule()
            security_rule_icmp.source = icmp_source
            icmp_options = IcmpOptions()
    else:
        if security_rule_flavour == "hashed":
            security_rule_tcp = oci_utils.create_hashed_instance(EgressSecurityRule)
            security_rule_tcp.destination = tcp_destination
            tcp_options = oci_utils.create_hashed_instance(TcpOptions)
            tcp_source_port_range = oci_utils.create_hashed_instance(PortRange)
            tcp_destination_port_range = oci_utils.create_hashed_instance(PortRange)
            security_rule_udp = oci_utils.create_hashed_instance(EgressSecurityRule)
            security_rule_udp.destination = udp_destination
            udp_options = oci_utils.create_hashed_instance(UdpOptions)
            udp_source_port_range = oci_utils.create_hashed_instance(PortRange)
            udp_destination_port_range = oci_utils.create_hashed_instance(PortRange)
            security_rule_icmp = oci_utils.create_hashed_instance(EgressSecurityRule)
            security_rule_icmp.destination = icmp_destination
            icmp_options = oci_utils.create_hashed_instance(IcmpOptions)
        else:
            security_rule_tcp = EgressSecurityRule()
            security_rule_tcp.destination = tcp_destination
            tcp_options = TcpOptions()
            tcp_source_port_range = PortRange()
            tcp_destination_port_range = PortRange()
            security_rule_udp = EgressSecurityRule()
            security_rule_udp.destination = udp_destination
            udp_options = UdpOptions()
            udp_source_port_range = PortRange()
            udp_destination_port_range = PortRange()
            security_rule_icmp = EgressSecurityRule()
            security_rule_icmp.destination = icmp_destination
            icmp_options = IcmpOptions()

    security_rule_tcp.protocol = "6"
    security_rule_tcp.is_stateless = stateless
    tcp_source_port_range.min = 22
    tcp_source_port_range.max = 30
    tcp_options.source_port_range = tcp_source_port_range
    tcp_destination_port_range.min = 45
    tcp_destination_port_range.max = 50
    tcp_options.destination_port_range = tcp_destination_port_range
    security_rule_tcp.tcp_options = tcp_options

    security_rule_icmp.protocol = "1"
    security_rule_icmp.is_stateless = stateless
    icmp_options.code = icmp_code
    icmp_options.type = icmp_type
    security_rule_icmp.icmp_options = icmp_options

    security_rule_udp.protocol = "17"
    security_rule_udp.is_stateless = stateless
    udp_source_port_range.min = 22
    udp_source_port_range.max = 30
    udp_options.source_port_range = udp_source_port_range
    udp_destination_port_range.min = 45
    udp_destination_port_range.max = 50
    udp_options.destination_port_range = tcp_destination_port_range
    security_rule_udp.udp_options = udp_options

    security_rules.append(security_rule_tcp)
    security_rules.append(security_rule_udp)
    security_rules.append(security_rule_icmp)
    return security_rules


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_security_list(egress_security_rules, ingress_security_rules, name):
    security_list = SecurityList()
    security_list.compartment_id = "ocid1.compartment.oc1..aaa"
    security_list.vcn_id = "ocid1.vcn.oc1..aaa"
    security_list.id = "ocid1.securitylist.oc1.aaa"
    security_list.egress_security_rules = egress_security_rules
    security_list.ingress_security_rules = ingress_security_rules
    security_list.display_name = name
    security_list.lifecycle_state = "AVAILABLE"
    security_list.time_created = "2017-11-20T17:31:31.806000+00:00"
    security_list.freeform_tags = {"security_level": "moderate"}
    security_list.defined_tags = {"department": {"department_type": "educational"}}
    return security_list


def get_module(additional_properties):
    params = {
        "display_name": "ansible_security_list",
        "ingress_security_rules": [],
        "egress_security_rules": [],
    }
    if additional_properties:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
