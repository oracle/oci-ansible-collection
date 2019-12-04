# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_health_checker_facts
from ansible.module_utils.oracle import oci_utils, oci_lb_utils

try:
    import oci
    from oci.load_balancer.models import LoadBalancer, HealthChecker, BackendSet
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest(
        "test_oci_load_balancer_health_checker_facts.py requires `oci` module"
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
    oci_load_balancer_health_checker_facts.set_logger(logging)


def test_list_load_balancer_health_checker_list_specific_health_checker(lb_client):
    module = get_module(
        dict(
            {
                "backend_set_name": "backend_set",
                "load_balancer_id": "ocid1.lodbalancer.xcds",
            }
        )
    )
    health_checker = get_health_checker()
    lb_client.get_health_checker.return_value = get_response(
        200, None, health_checker, None
    )
    result = oci_load_balancer_health_checker_facts.list_load_balancer_health_checker(
        lb_client, module
    )
    assert result["health_checkers"][0]["protocol"] == health_checker.protocol


def test_list_load_balancer_health_checker_list_all_health_checkers(lb_client):
    module = get_module(dict({"load_balancer_id": "ocid1.lodbalancer.xcds"}))
    health_checker = get_health_checker()
    load_balancer = LoadBalancer()
    backend_set = BackendSet()
    health_checker = get_health_checker()
    backend_set.health_checker = health_checker
    load_balancer.backend_sets = dict({"backend_set": backend_set})
    lb_client.get_load_balancer.return_value = get_response(
        200, None, load_balancer, None
    )
    result = oci_load_balancer_health_checker_facts.list_load_balancer_health_checker(
        lb_client, module
    )
    assert result["health_checkers"][0]["protocol"] == health_checker.protocol


def test_list_load_balancer_health_checker_service_error(lb_client):
    error_message = "Internal Server Error"
    module = get_module(
        dict(
            {
                "backend_set_name": "backend_set",
                "load_balancer_id": "ocid1.lodbalancer.xcds",
            }
        )
    )
    health_checker = get_health_checker()
    lb_client.get_health_checker.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_load_balancer_health_checker_facts.list_load_balancer_health_checker(
            lb_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def get_health_checker():
    health_checker = HealthChecker()
    health_checker.interval_in_millis = 30000
    health_checker.port = 82
    health_checker.protocol = "HTTP"
    health_checker.response_body_regex = "^(500|40[1348])$"
    health_checker.retries = 3
    health_checker.return_code = 200
    health_checker.timeout_in_millis = 6000
    health_checker.url_path = "/healthcheck"
    return health_checker


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = dict()
    if additional_properties is not None:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
