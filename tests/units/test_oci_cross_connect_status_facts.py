# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
import logging
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_cross_connect_status_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import CrossConnectStatus
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
except ImportError:
    raise SkipTest("test_oci_cross_connect_status_facts.py requires `oci` module")


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


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_cross_connect_status_facts.set_logger(logging)


def test_list_cross_connect_statuses_all(
    virtual_network_client, list_all_resources_patch
):
    module = get_module()
    cross_connect_statuses = get_cross_connect_statuses()
    virtual_network_client.get_cross_connect_status.return_value = (
        cross_connect_statuses
    )
    result = oci_cross_connect_status_facts.list_cross_connect_statuses(
        virtual_network_client, module
    )
    assert (
        result["cross_connect_statuses"][0]["light_level_indicator"]
        == cross_connect_statuses[0].light_level_indicator
    )


def get_cross_connect_statuses():
    cross_connect_statuses = []
    cross_connect_status = CrossConnectStatus()
    cross_connect_status.cross_connect_id = "ocid1.crossconnect..axsd"
    cross_connect_status.interface_state = "UP"
    cross_connect_status.light_level_ind_bm = 14.0
    cross_connect_status.light_level_indicator = "GOOD"
    cross_connect_statuses.append(cross_connect_status)
    return cross_connect_statuses


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {"compartment_id": "ocid1.compartment..axsd"}
    if additional_properties is not None:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
