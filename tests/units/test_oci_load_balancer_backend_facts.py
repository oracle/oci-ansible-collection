# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_backend_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.load_balancer.models import Backend
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_load_balancer_backend_facts.py requires `oci` module")


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
    oci_load_balancer_backend_facts.set_logger(logging)


def test_list_load_balancer_backends_specific_backend(lb_client):
    module = get_module(
        dict(
            {
                "backend_set_name": "backend1",
                "load_balancer_id": "ocid1.lodbalancer.xcds",
                "ip_address": "10.12.15.121",
                "port": "8080",
            }
        )
    )
    lb_client.get_backend.return_value = get_response(200, None, get_backend(), None)
    result = oci_load_balancer_backend_facts.list_load_balancer_backends(
        lb_client, module
    )
    assert result["backends"][0]["ip_address"] is get_backend().ip_address


def test_list_load_balancer_backends_all_backends(lb_client, list_all_resources_patch):
    module = get_module(
        dict(
            {
                "backend_set_name": "backend1",
                "load_balancer_id": "ocid1.lodbalancer.xcds",
            }
        )
    )
    list_all_resources_patch.return_value = [get_backend()]
    result = oci_load_balancer_backend_facts.list_load_balancer_backends(
        lb_client, module
    )
    assert result["backends"][0]["ip_address"] is get_backend().ip_address


def test_list_load_balancer_backends_service_error(lb_client, list_all_resources_patch):
    error_message = "Internal Server Error"
    module = get_module(
        dict(
            {
                "backend_set_name": "backend1",
                "load_balancer_id": "ocid1.lodbalancer.xcds",
            }
        )
    )
    list_all_resources_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    try:
        oci_load_balancer_backend_facts.list_load_balancer_backends(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def get_backend():
    backend = Backend()
    backend.name = "10.159.34.21:8181"
    backend.backup = True
    backend.drain = True
    backend.offline = True
    backend.weight = 5
    backend.ip_address = "10.159.34.21"
    backend.port = "8181"
    return backend


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = dict()
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
