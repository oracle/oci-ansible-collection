# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_shape_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.load_balancer.models import LoadBalancerShape
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_load_balancer_shape_facts.py requires `oci` module")


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
def lb_client(mocker):
    mock_lb_client = mocker.patch(
        "oci.load_balancer.load_balancer_client.LoadBalancerClient"
    )
    return mock_lb_client.return_value


@pytest.fixture()
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_load_balancer_shape_facts.set_logger(logging)


def test_list_load_balancer_shapes(lb_client, list_all_resources_patch):
    module = get_module()
    load_balancer_shape = get_load_balancer_shape()
    list_all_resources_patch.return_value = [load_balancer_shape]
    result = oci_load_balancer_shape_facts.list_load_balancer_shapes(lb_client, module)
    assert result["load_balancer_shapes"][0]["name"] == "HTTP"


def test_list_load_balancer_shapes_service_error(lb_client, list_all_resources_patch):
    error_message = "Internal Server Error"
    module = get_module()
    list_all_resources_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_load_balancer_shape_facts.list_load_balancer_shapes(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def get_load_balancer_shape():
    load_balancer_shape = LoadBalancerShape()
    load_balancer_shape.name = "HTTP"
    return load_balancer_shape


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module():
    params = {"compartment_id": "ocid1.compartment.xcds"}
    module = FakeModule(**params)
    return module
