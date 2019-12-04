# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_dhcp_options_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import DhcpOptions
    from oci.exceptions import ServiceError
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


def test_list_dhcp_optionss(virtual_network_client, list_all_resources_patch):
    module = get_module()
    dhcp_options = get_dhcp_options()
    list_all_resources_patch.return_value = [dhcp_options]
    result = oci_dhcp_options_facts.list_dhcp_options(virtual_network_client, module)
    assert result["dhcp_options_list"][0]["display_name"] == dhcp_options.display_name


def test_list_dhcp_optionss_with_ig_id(
    virtual_network_client, list_all_resources_patch
):
    module = get_module_with_dhcp_id()
    dhcp_options = get_dhcp_options()
    virtual_network_client.get_dhcp_options.return_value = get_response(
        200, None, dhcp_options, None
    )
    result = oci_dhcp_options_facts.list_dhcp_options(virtual_network_client, module)
    assert result["dhcp_options_list"][0]["display_name"] == dhcp_options.display_name


def test_list_dhcp_optionss_service_error(
    virtual_network_client, list_all_resources_patch
):
    error_message = "Internal Server Error"
    module = get_module()
    list_all_resources_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        result = oci_dhcp_options_facts.list_dhcp_options(
            virtual_network_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def get_dhcp_options():
    dhcp_options = DhcpOptions()
    dhcp_options.compartment_id = "ocid1.compartment.oc1..aaaa"
    dhcp_options.display_name = "ansible_dhcp_options"
    dhcp_options.id = "ocid1.dhcpoptions.oc1..aaaa"
    dhcp_options.lifecycle_state = "AVAILABLE"
    dhcp_options.vcn_id = "ocid1.vcn.oc1..aaaa"
    dhcp_options.options = []
    return dhcp_options


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module():
    params = {
        "compartment_id": "ocid1.comp..axsd",
        "vcn_id": "ocid1.vcn..fxdv",
        "dhcp_id": None,
        "display_name": None,
    }
    module = FakeModule(**params)
    return module


def get_module_with_dhcp_id():
    params = {"compartment_id": None, "vcn_id": None, "dhcp_id": "ocid.dhcp..fxdv"}
    module = FakeModule(**params)
    return module
