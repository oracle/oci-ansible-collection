# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_backend_set_health_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.load_balancer.models import BackendSetHealth
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest(
        "test_oci_load_balancer_backend_set_health_facts.py requires `oci` module"
    )


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


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_load_balancer_backend_set_health_facts.set_logger(logging)


def test_get_load_balancer_backend_set_health(lb_client):
    module = get_module()
    backend_set_health = get_backend_set_health()
    lb_client.get_backend_set_health.return_value = get_response(
        200, None, backend_set_health, None
    )
    result = oci_load_balancer_backend_set_health_facts.get_load_balancer_backend_set_health(
        lb_client, module
    )
    assert result["backend_set_health"]["status"] == "CRITICAL"


def test_get_load_balancer_backend_set_health_service_error(lb_client):
    error_message = "Internal Server Error"
    module = get_module()
    lb_client.get_backend_health.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_load_balancer_backend_set_health_facts.get_load_balancer_backend_set_health(
            lb_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def get_backend_set_health():
    backend_set_health = BackendSetHealth()
    backend_set_health.critical_state_backend_names = ["10.1.2.3:8080"]
    backend_set_health.total_backend_count = 1
    backend_set_health.status = "CRITICAL"

    return backend_set_health


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module():
    params = {
        "backend_set_name": "backend1",
        "load_balancer_id": "ocid1.lodbalancer.xcds",
    }
    module = FakeModule(**params)
    return module
