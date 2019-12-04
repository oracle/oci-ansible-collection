# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_health_checker
from ansible.module_utils.oracle import oci_utils, oci_lb_utils

try:
    import oci
    from oci.util import to_dict
    from oci.load_balancer.models import HealthChecker
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_load_balancer_health_checker.py requires `oci` module")


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
def get_existing_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "get_existing_resource")


@pytest.fixture()
def create_or_update_lb_resources_and_wait_patch(mocker):
    return mocker.patch.object(oci_lb_utils, "create_or_update_lb_resources_and_wait")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_load_balancer_health_checker.set_logger(logging)


def test_update_health_checker(
    lb_client, get_existing_resource_patch, create_or_update_lb_resources_and_wait_patch
):
    module = get_module()
    health_checker = get_health_checker()
    get_existing_resource_patch.return_value = health_checker
    create_or_update_lb_resources_and_wait_patch.return_value = dict(
        health_checker=to_dict(health_checker), changed=True
    )
    result = oci_load_balancer_health_checker.update_health_checker(lb_client, module)
    assert result["changed"] is True


def test_update_health_checker_no_change(lb_client, get_existing_resource_patch):
    additional_properties = dict({"port": 82})
    module = get_module(additional_properties)
    health_checker = get_health_checker()
    get_existing_resource_patch.return_value = health_checker
    result = oci_load_balancer_health_checker.update_health_checker(lb_client, module)
    assert result["changed"] is False


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
    params = {
        "load_balancer_id": "ocid1.loadbalancer.oc1.iad.aaaa",
        "backend_set_name": "test_backend",
        "interval_in_millis": 30000,
        "port": 8080,
        "protocol": "HTTP",
        "retries": 3,
        "timeout_in_millis": 6000,
        "return_code": 200,
        "url_path": "/healthcheck",
    }
    if additional_properties is not None:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
