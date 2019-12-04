# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.module_utils.oracle import oci_utils
from ansible.modules.cloud.oracle import oci_waas_edge_subnet_facts

try:
    import oci
    from oci.util import to_dict
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_waas_edge_subnet_facts.py requires `oci` module")


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
def waas_client(mocker):
    mock_waas_client = mocker.patch("oci.waas.waas_client.WaasClient")
    return mock_waas_client.return_value


@pytest.fixture()
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


def get_module(**kwargs):
    params = {}
    params.update(kwargs)
    module = FakeModule(**params)
    return module


def test_list_edge_subnets_raises_service_error(waas_client, list_all_resources_patch):
    list_all_resources_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    with pytest.raises(ServiceError) as exc_info:
        oci_waas_edge_subnet_facts.list_edge_subnets(waas_client, get_module())
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"


def test_list_edge_subnets_calls_list_all_resources_with_correct_parameters(
    waas_client, list_all_resources_patch
):
    module = get_module(sort_by="region", sort_order="DESC")
    list_all_resources_patch.return_value = []
    oci_waas_edge_subnet_facts.list_edge_subnets(waas_client, module)
    list_all_resources_patch.assert_called_once()
    list_all_resources_patch.assert_called_with(
        waas_client.list_edge_subnets, sort_by="region", sort_order="DESC"
    )
