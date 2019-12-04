# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_security_list_facts
import json

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import SecurityList
    from oci.exceptions import ServiceError
    from ansible.module_utils.oracle import oci_utils
except ImportError:
    raise SkipTest("test_oci_security_list_facts.py requires `oci` module")


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


def test_list_security_lists(virtual_network_client, list_all_resources_patch):
    module = get_module(
        dict(
            {
                "compartment_id": "ocid1.compartment.aa",
                "vcn_id": "ocid1.vcn.aa",
                "security_list_id": "",
            }
        )
    )
    list_all_resources_patch.return_value = get_security_lists(
        "ansible_security_list_one", "ansible_security_list_two"
    )
    result = oci_security_list_facts.list_security_lists(virtual_network_client, module)

    assert len(result["security_lists"]) is 2


def test_list_security_lists_for_specific_security_list(
    virtual_network_client, list_all_resources_patch
):
    module = get_module(
        dict(
            {
                "compartment_id": "",
                "vcn_id": "",
                "security_list_id": "ocid1.securitylist.aaa",
            }
        )
    )
    result = oci_security_list_facts.list_security_lists(virtual_network_client, module)

    assert len(result["security_lists"]) is 1


def test_list_security_lists_service_error(
    virtual_network_client, list_all_resources_patch
):
    error_message = "Internal Server Error"
    module = get_module(
        dict(
            {
                "compartment_id": "ocid1.compartment.aa",
                "vcn_id": "ocid1.vcn.aa",
                "security_list_id": "",
            }
        )
    )

    list_all_resources_patch.side_effects = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    try:
        result = oci_security_list_facts.list_security_lists(
            virtual_network_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_security_lists(name_one, name_two):
    security_lists = []
    security_list_one = SecurityList()
    security_list_one.compartment_id = "ocid1.compartment.oc1..aaa"
    security_list_one.vcn_id = "ocid1.vcn.oc1..aaa"
    security_list_one.id = "ocid1.securitylist.oc1.aaa"
    security_list_one.egress_security_rules = ["egress_security_rules"]
    security_list_one.ingress_security_rules = ["ingress_security_rules"]
    security_list_one.display_name = name_one
    security_list_one.lifecycle_state = "AVAILABLE"
    security_list_one.time_created = "2017-11-20T17:31:31.806000+00:00"

    security_list_two = SecurityList()
    security_list_two.compartment_id = "ocid1.compartment.oc1..aaa"
    security_list_two.vcn_id = "ocid1.vcn.oc1..aaa"
    security_list_two.id = "ocid1.securitylist.oc1.bbb"
    security_list_two.egress_security_rules = ["egress_security_rules"]
    security_list_two.ingress_security_rules = ["ingress_security_rules"]
    security_list_two.display_name = name_two
    security_list_two.lifecycle_state = "AVAILABLE"
    security_list_two.time_created = "2017-11-20T17:31:31.806000+00:00"
    security_lists.append(security_list_one)
    security_lists.append(security_list_two)
    return security_lists


def get_security_list(name_one):
    security_lists = []
    security_list_one = SecurityList()
    security_list_one.compartment_id = "ocid1.compartment.oc1..aaa"
    security_list_one.vcn_id = "ocid1.vcn.oc1..aaa"
    security_list_one.id = "ocid1.securitylist.oc1.aaa"
    security_list_one.egress_security_rules = ["egress_security_rules"]
    security_list_one.ingress_security_rules = ["ingress_security_rules"]
    security_list_one.display_name = name_one
    security_list_one.lifecycle_state = "AVAILABLE"
    security_list_one.time_created = "2017-11-20T17:31:31.806000+00:00"
    security_lists.append(security_list_one)
    return security_lists


def get_module(additional_properties):
    params = {"display_name": "ansible_security_list"}
    if additional_properties:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
