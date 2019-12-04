# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_cross_connect_group_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import CrossConnectGroup
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
except ImportError:
    raise SkipTest("test_oci_cross_connect_group_facts.py requires `oci` module")


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


def test_list_cross_connect_groups_all(
    virtual_network_client, list_all_resources_patch
):
    module = get_module()
    cross_connects = get_cross_connects()
    list_all_resources_patch.return_value = cross_connects
    result = oci_cross_connect_group_facts.list_cross_connect_groups(
        virtual_network_client, module
    )
    assert (
        result["cross_connect_groups"][0]["display_name"]
        == cross_connects[0].display_name
    )


def test_list_cross_connect_groups_specific(
    virtual_network_client, list_all_resources_patch
):
    module = get_module(dict(cross_connect_group_id="ocid1.crossconnectgroup..vgfc"))
    cross_connects = get_cross_connects()
    list_all_resources_patch.return_value = cross_connects
    result = oci_cross_connect_group_facts.list_cross_connect_groups(
        virtual_network_client, module
    )
    assert (
        result["cross_connect_groups"][0]["display_name"]
        == cross_connects[0].display_name
    )


def get_cross_connects():
    cross_connect_groups = []
    cross_connect_group = CrossConnectGroup()
    cross_connect_group.compartment_id = "ocid1.compartment..axsd"
    cross_connect_group.id = "ocid1.crossconectgroup..fxdv"
    cross_connect_group.display_name = "ansible_cross_connect_group"
    cross_connect_group.lifecycle_state = "AVAILABLE"
    cross_connect_group.time_created = "2018-08-25T21:10:29.600Z"
    cross_connect_groups.append(cross_connect_group)
    return cross_connect_groups


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {"compartment_id": "ocid1.compartment..axsd"}
    if additional_properties is not None:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
