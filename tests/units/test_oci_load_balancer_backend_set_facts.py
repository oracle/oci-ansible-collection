# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_backend_set_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.load_balancer.models import (
        BackendSet,
        Backend,
        HealthChecker,
        SessionPersistenceConfigurationDetails,
        SSLConfiguration,
        WorkRequest,
    )
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_load_balancer_backend_set_facts.py requires `oci` module")


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
def oci_wait_until_patch(mocker):
    return mocker.patch.object(oci, "wait_until")


@pytest.fixture()
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


@pytest.fixture()
def oci_utils_call_with_backoff_patch(mocker):
    return mocker.patch.object(oci_utils, "call_with_backoff")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_load_balancer_backend_set_facts.set_logger(logging)

    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_load_balancer_backend_set_facts.set_logger(logging)


def test_list_load_balancer_backend_sets_specific_backend_set(
    lb_client, oci_utils_call_with_backoff_patch
):
    module = get_module(
        dict({"name": "backend_set1", "load_balancer_id": "ocid1.lodbalancer.xcds"})
    )
    backend_set = create_default_backend_set()
    lb_client.get_backend_set.return_value = get_response(200, None, backend_set, None)
    oci_utils_call_with_backoff_patch.return_value = get_response(
        200, None, backend_set, None
    )
    result = oci_load_balancer_backend_set_facts.list_load_balancer_backend_sets(
        lb_client, module
    )
    assert result["backend_sets"][0]["policy"] is backend_set.policy


def test_list_load_balancer_backends_all_backends(lb_client, list_all_resources_patch):
    module = get_module(dict({"load_balancer_id": "ocid1.lodbalancer.xcds"}))
    backend_set = create_default_backend_set()
    list_all_resources_patch.return_value = [backend_set]
    result = oci_load_balancer_backend_set_facts.list_load_balancer_backend_sets(
        lb_client, module
    )
    assert result["backend_sets"][0]["policy"] is backend_set.policy


def test_list_load_balancer_backend_sets_service_error(
    lb_client, list_all_resources_patch
):
    error_message = "Internal Server Error"
    module = get_module(
        dict({"name": "backend_set1", "load_balancer_id": "ocid1.lodbalancer.xcds"})
    )
    list_all_resources_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    try:
        oci_load_balancer_backend_set_facts.list_load_balancer_backend_sets(
            lb_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def create_default_backend_set():
    health_checker_dict = {
        "interval_in_millis": 30000,
        "port": 8080,
        "protocol": "HTTP",
        "response_body_regex": "^(500|40[1348])$",
        "retries": 3,
        "timeout_in_millis": 6000,
        "return_code": 200,
        "url_path": "/healthcheck",
    }
    backends = [
        {
            "ip_address": "10.159.34.21",
            "port": 8080,
            "backup": True,
            "offline": False,
            "drain": True,
            "weight": 1,
        }
    ]
    sp_config_dict = {"cookie_name": "my_cookie", "disable_fallback": True}
    ssl_config_dict = {
        "certificate_name": "cert1",
        "verify_depth": 3,
        "verify_peer_certificate": True,
    }
    backend_set = get_backend_set(
        "backend_set1",
        "LEAST_CONNECTIONS",
        backends,
        health_checker_dict,
        sp_config_dict,
        ssl_config_dict,
    )
    return backend_set


def get_backend_set(
    name, policy, backends, health_checker_dict, sp_config_dict, ssl_config_dict
):
    backend_set = BackendSet()
    backend_set.name = name
    backend_set.policy = policy
    backend_set.backends = create_backends(backends)
    backend_set.health_checker = create_attribute_instance(
        HealthChecker(), health_checker_dict
    )
    backend_set.session_persistence_configuration = create_attribute_instance(
        SessionPersistenceConfigurationDetails(), sp_config_dict
    )
    backend_set.ssl_configuration = create_attribute_instance(
        SSLConfiguration(), ssl_config_dict
    )
    return backend_set


def create_attribute_instance(attribute_instance, attribute_instance_dict):
    if attribute_instance_dict is None:
        return None
    for attribute in attribute_instance.attribute_map.keys():
        attribute_instance.__setattr__(
            attribute, attribute_instance_dict.get(attribute)
        )
    return attribute_instance


def create_backends(backends):
    result_backends = []
    for backend_dict in backends:
        backend = Backend()
        for attribute in backend.attribute_map.keys():
            backend.__setattr__(attribute, backend_dict.get(attribute))
        result_backends.append(backend)
    return result_backends


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = dict()
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
