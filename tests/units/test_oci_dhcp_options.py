# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_dhcp_options
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import DhcpOptions, DhcpSearchDomainOption, DhcpDnsOption
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
except ImportError:
    raise SkipTest("test_oci_dhcp_options.py requires `oci` module")


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
def oci_wait_until_patch(mocker):
    return mocker.patch.object(oci, "wait_until")


@pytest.fixture()
def check_and_create_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_create_resource")


@pytest.fixture()
def update_dhcp_options_patch(mocker):
    return mocker.patch.object(oci_dhcp_options, "update_dhcp_options")


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


def test_create_or_update_dhcp_options_create(
    virtual_network_client, check_and_create_resource_patch
):
    module = get_module(dict())
    check_and_create_resource_patch.return_value = dict({"changed": True})
    result = oci_dhcp_options.create_or_update_dhcp_options(
        virtual_network_client, module
    )
    assert result["changed"] is True


def test_create_or_update_dhcp_options_update(
    virtual_network_client, update_dhcp_options_patch, get_existing_resource_patch
):
    module = get_module(dict(dhcp_id="ocid1.dhcpoptions..aa"))
    update_dhcp_options_patch.return_value = dict({"changed": True})
    result = oci_dhcp_options.create_or_update_dhcp_options(
        virtual_network_client, module
    )
    assert result["changed"] is True


def test_create_or_update_dhcp_options_failure_service_error(
    virtual_network_client, update_dhcp_options_patch, get_existing_resource_patch
):
    error_message = "Internal Server Error"
    module = get_module(dict(dhcp_id="ocid1.dhcpoptions..aa"))
    update_dhcp_options_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_dhcp_options.create_or_update_dhcp_options(virtual_network_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_dhcp_options_failure_timeout_error(
    virtual_network_client, update_dhcp_options_patch, get_existing_resource_patch
):
    error_message = "Timeout Error"
    module = get_module(dict(dhcp_id="ocid1.dhcpoptions..aa"))
    update_dhcp_options_patch.side_effect = MaximumWaitTimeExceeded(
        400, "TimeoutError", dict(), error_message
    )
    try:
        oci_dhcp_options.create_or_update_dhcp_options(virtual_network_client, module)
    except Exception as ex:
        assert error_message in ex.args[0].__repr__()


def test_create_dhcp_options(virtual_network_client, create_and_wait_patch):
    dhcp_dns_options = get_options("DomainNameServer", "VcnLocalPlusInternet", [], None)
    dhcp_search_domain = get_options(
        "SearchDomain", None, None, ["ansibletestvcn.oraclevcn.com"]
    )
    options = [
        {
            "custom_dns_servers": [],
            "server_type": "VcnLocalPlusInternet",
            "type": "DomainNameServer",
        },
        {
            "search_domain_names": ["ansibletestvcn.oraclevcn.com"],
            "type": "SearchDomain",
        },
    ]
    module = get_module(dict({"options": options}))
    dhcp_options = get_dhcp_options(
        "ansible_dhcp", [dhcp_dns_options, dhcp_search_domain]
    )
    create_and_wait_patch.return_value = dict(
        {"dhcp_options": to_dict(dhcp_options), "changed": True}
    )
    result = oci_dhcp_options.create_dhcp_options(virtual_network_client, module)
    assert result["dhcp_options"]["display_name"] == dhcp_options.display_name


def test_update_dhcp_options_no_dhcp_options_for_update(virtual_network_client):
    error_message = "No Dhcp Options"
    module = get_module(dict(dhcp_id="ocid1.dhcpoptions..xvdf"))
    try:
        oci_dhcp_options.update_dhcp_options(virtual_network_client, None, module)
    except Exception as ex:
        assert error_message in str(ex.args)


def test_update_dhcp_options_name_changed(
    virtual_network_client, update_and_wait_patch
):
    dhcp_options = get_dhcp_options("ansible_dhcp", None)
    module = get_module(dict())
    update_and_wait_patch.return_value = dict(
        {"dhcp_options": to_dict(dhcp_options), "changed": True}
    )
    oci_dhcp_options.update_dhcp_options(virtual_network_client, dhcp_options, module)
    assert update_and_wait_patch.called


def test_update_dhcp_options_freeform_tags_changed(
    virtual_network_client, update_and_wait_patch
):
    dhcp_options = get_dhcp_options("ansible_dhcp", None)
    module = get_module(dict(freeform_tags=dict(group="employee")))
    update_and_wait_patch.return_value = dict(
        {"dhcp_options": to_dict(dhcp_options), "changed": True}
    )
    oci_dhcp_options.update_dhcp_options(virtual_network_client, dhcp_options, module)
    assert update_and_wait_patch.called


def test_update_dhcp_options_defined_tags_changed(
    virtual_network_client, update_and_wait_patch
):
    dhcp_options = get_dhcp_options("ansible_dhcp", None)
    module = get_module(dict(defined_tags=dict(dhcp_type=dict(choice="custom"))))
    update_and_wait_patch.return_value = dict(
        {"dhcp_options": to_dict(dhcp_options), "changed": True}
    )
    oci_dhcp_options.update_dhcp_options(virtual_network_client, dhcp_options, module)
    assert update_and_wait_patch.called


def test_update_dhcp_options_options_changed(
    virtual_network_client, update_and_wait_patch
):
    dhcp_dns_options = get_options("DomainNameServer", "VcnLocalPlusInternet", [], None)
    dhcp_search_domain = get_options(
        "SearchDomain", None, None, ["ansibletestvcn.oraclevcn.com"]
    )
    options = [dhcp_dns_options, dhcp_search_domain]
    input_options = [
        {
            "custom_dns_servers": [],
            "server_type": "VcnLocalPlusInternet",
            "type": "DomainNameServer",
        },
        {"search_domain_names": ["ansibletestvcn.oracle.com"], "type": "SearchDomain"},
    ]
    module = get_module(dict(options=input_options, purge_dhcp_options=False))
    dhcp_options = get_dhcp_options("ansible_dhcp_options", options)
    update_and_wait_patch.return_value = dict(
        {"dhcp_options": dhcp_options, "changed": True}
    )
    oci_dhcp_options.update_dhcp_options(virtual_network_client, dhcp_options, module)
    assert update_and_wait_patch.called


def test_get_options_difference_no_existing_dns():
    dhcp_dns_options = get_options("DomainNameServer", "VcnLocalPlusInternet", [], None)
    dhcp_search_domain = get_options(
        "SearchDomain", None, None, ["ansibletestvcn.oraclevcn.com"]
    )
    result, changed = oci_utils.get_component_list_difference(
        [dhcp_dns_options, dhcp_search_domain], [], True
    )
    assert changed is True


def test_update_dhcp_options_dns_changed_append():
    dhcp_dns_options = get_options("DomainNameServer", "VcnLocalPlusInternet", [], None)
    dhcp_search_domain = get_options(
        "SearchDomain", None, None, ["ansibletestvcn.oraclevcn.com"]
    )
    existing_options = [dhcp_dns_options, dhcp_search_domain]
    input_dhcp_dns_options = get_options(
        "DomainNameServer", "CustomDnsServer", ["10.0.0.8"], None
    )
    input_dhcp_search_domain = get_options(
        "SearchDomain", None, None, ["ansibletestvcn.oraclevcn.com"]
    )
    input_options = [input_dhcp_dns_options, input_dhcp_search_domain]
    result, changed = oci_utils.get_component_list_difference(
        input_options, existing_options, False
    )
    assert changed is True
    assert len(result) is 3


def test_update_dhcp_options_searchdomain_changed_append():
    dhcp_dns_options = get_options("DomainNameServer", "VcnLocalPlusInternet", [], None)
    dhcp_search_domain = get_options(
        "SearchDomain", None, None, ["ansibletestvcn.oraclevcn.com"]
    )
    existing_options = [dhcp_dns_options, dhcp_search_domain]
    input_dhcp_dns_options = get_options(
        "DomainNameServer", "VcnLocalPlusInternet", [], None
    )
    input_dhcp_search_domain = get_options(
        "SearchDomain", None, None, ["ansiblevcn.oraclevcn.com"]
    )
    input_options = [input_dhcp_dns_options, input_dhcp_search_domain]
    result, changed = oci_utils.get_component_list_difference(
        input_options, existing_options, False
    )
    assert changed is True
    assert len(result) is 3


def test_update_dhcp_options_dns_changed_purged():
    dhcp_dns_options = get_options("DomainNameServer", "VcnLocalPlusInternet", [], None)
    dhcp_search_domain = get_options(
        "SearchDomain", None, None, ["ansibletestvcn.oraclevcn.com"]
    )
    existing_options = [dhcp_dns_options, dhcp_search_domain]
    input_dhcp_dns_options = get_options(
        "DomainNameServer", "CustomDnsServer", ["10.0.0.8"], None
    )
    input_dhcp_search_domain = get_options(
        "SearchDomain", None, None, ["ansibletestvcn.oraclevcn.com"]
    )
    input_options = [input_dhcp_dns_options, input_dhcp_search_domain]
    result, changed = oci_utils.get_component_list_difference(
        input_options, existing_options, False
    )
    assert changed is True
    for option in result:
        if option.type == "CustomDnsServer":
            assert option.custom_dns_servers[0] == "10.0.0.8"


def test_update_dhcp_options_searchdomain_changed_purged():
    dhcp_dns_options = get_options("DomainNameServer", "VcnLocalPlusInternet", [], None)
    dhcp_search_domain = get_options(
        "SearchDomain", None, None, ["ansibletestvcn.oraclevcn.com"]
    )
    existing_options = [dhcp_dns_options, dhcp_search_domain]
    input_dhcp_dns_options = get_options(
        "DomainNameServer", "VcnLocalPlusInternet", [], None
    )
    input_dhcp_search_domain = get_options(
        "SearchDomain", None, None, ["ansiblevcn.oraclevcn.com"]
    )
    input_options = [input_dhcp_dns_options, input_dhcp_search_domain]
    result, changed = oci_utils.get_component_list_difference(
        input_options, existing_options, True
    )
    assert changed is True
    for option in result:
        if option.type == "SearchDomain":
            assert option.search_domain_names[0] == "ansiblevcn.oraclevcn.com"


def test_delete_dhcp_options(virtual_network_client, delete_and_wait_patch):
    module = get_module(dict({"dhcp_id": "{ocid1.dhcpoptions..aa}"}))
    dhcp_options = get_dhcp_options("ansible_dhcp_options", None)
    delete_and_wait_patch.return_value = dict(
        {"dhcp_options": dhcp_options, "changed": True}
    )
    result = oci_dhcp_options.delete_dhcp_options(virtual_network_client, module)
    assert result["changed"] is True


def get_dhcp_options(name, options):
    dhcp_options = DhcpOptions()
    dhcp_options.compartment_id = "ocid1.compartment.oc1..aaaa"
    dhcp_options.display_name = name
    dhcp_options.id = "ocid1.dhcpoptions.oc1..aaaa"
    dhcp_options.lifecycle_state = "AVAILABLE"
    dhcp_options.vcn_id = "ocid1.vcn.oc1..aaaa"
    dhcp_options.options = options
    dhcp_options.freeform_tags = {"group": "student"}
    dhcp_options.defined_tags = {"dhcp_type": {"choice": "server"}}
    return dhcp_options


def get_options(type, server_type, custom_dns_servers, search_domain_names):
    dhcp_option = None
    if type == "DomainNameServer":
        dhcp_option = oci_utils.create_hashed_instance(DhcpDnsOption)
        dhcp_option.__setattr__("type", type)
        dhcp_option.__setattr__("server_type", server_type)
        dhcp_option.__setattr__("custom_dns_servers", custom_dns_servers)
    else:
        dhcp_option = oci_utils.create_hashed_instance(DhcpSearchDomainOption)
        dhcp_option.__setattr__("type", type)
        dhcp_option.__setattr__("search_domain_names", search_domain_names)
    return dhcp_option


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = {"display_name": "ansible_dhcp_options"}
    if additional_properties:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
