# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_backend_set
from ansible.module_utils.oracle import oci_utils, oci_lb_utils

try:
    import oci
    from oci.util import to_dict
    from oci.load_balancer.models import (
        BackendSet,
        Backend,
        HealthChecker,
        SessionPersistenceConfigurationDetails,
        SSLConfiguration,
        WorkRequest,
    )
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_load_balancer_backend_set.py requires `oci` module")


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
def create_backend_set_patch(mocker):
    return mocker.patch.object(oci_load_balancer_backend_set, "create_backend_set")


@pytest.fixture()
def update_backend_set_patch(mocker):
    return mocker.patch.object(oci_load_balancer_backend_set, "update_backend_set")


@pytest.fixture()
def create_or_update_lb_resources_and_wait_patch(mocker):
    return mocker.patch.object(oci_lb_utils, "create_or_update_lb_resources_and_wait")


@pytest.fixture()
def delete_lb_resources_and_wait_patch(mocker):
    return mocker.patch.object(oci_lb_utils, "delete_lb_resources_and_wait")


@pytest.fixture()
def get_existing_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "get_existing_resource")


@pytest.fixture()
def check_and_create_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_create_resource")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_load_balancer_backend_set.set_logger(logging)


def test_create_or_update_backend_create(
    lb_client, check_and_create_resource_patch, get_existing_resource_patch
):
    module = get_module(dict())
    backend_set = create_default_backend_set()
    get_existing_resource_patch.return_value = None
    check_and_create_resource_patch.return_value = {
        "backend_set": to_dict(backend_set),
        "changed": True,
    }
    result = oci_load_balancer_backend_set.create_or_update_backend_set(
        lb_client, module
    )
    assert result["backend_set"]["policy"] is backend_set.policy


def test_create_or_update_backend_update(
    lb_client, update_backend_set_patch, get_existing_resource_patch
):
    module = get_module(dict())
    backend_set = create_default_backend_set()
    get_existing_resource_patch.return_value = backend_set
    update_backend_set_patch.return_value = {
        "backend_set": to_dict(backend_set),
        "changed": True,
    }
    result = oci_load_balancer_backend_set.create_or_update_backend_set(
        lb_client, module
    )
    assert result["backend_set"]["policy"] is backend_set.policy


def test_create_or_update_backend_set_service_error(
    lb_client, check_and_create_resource_patch, get_existing_resource_patch
):
    module = get_module(dict())
    error_message = "Internal Server Error"
    check_and_create_resource_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    get_existing_resource_patch.return_value = None
    try:
        oci_load_balancer_backend_set.create_or_update_backend_set(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_backend_set_client_error(
    lb_client, check_and_create_resource_patch, get_existing_resource_patch
):
    module = get_module(dict())
    error_message = "Work Request Failed"
    check_and_create_resource_patch.side_effect = ClientError(
        Exception("Work Request Failed")
    )
    get_existing_resource_patch.return_value = None
    try:
        oci_load_balancer_backend_set.create_or_update_backend_set(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_backend_set(
    lb_client, create_or_update_lb_resources_and_wait_patch, get_existing_resource_patch
):
    module = get_module(dict())
    backend_set = create_default_backend_set()
    create_or_update_lb_resources_and_wait_patch.return_value = {
        "backend_set": to_dict(backend_set),
        "changed": True,
    }
    result = oci_load_balancer_backend_set.create_backend_set(lb_client, module)
    assert result["backend_set"]["name"] == backend_set.name


def test_update_backend_set_backends_purge_new_backend(
    lb_client, create_or_update_lb_resources_and_wait_patch
):
    module = get_module(dict({"purge_backends": True}))
    assert_update_true(create_or_update_lb_resources_and_wait_patch, lb_client, module)


def test_update_backend_set_backends_purge_empty_backend(
    lb_client, create_or_update_lb_resources_and_wait_patch
):
    module = get_module(dict({"purge_backends": True}))
    module.params.update(dict({"backends": []}))
    assert_update_true(create_or_update_lb_resources_and_wait_patch, lb_client, module)


def test_update_backend_set_backends_append_new_backend(
    lb_client, create_or_update_lb_resources_and_wait_patch
):
    module = get_module(dict({"purge_backends": False}))
    assert_update_true(create_or_update_lb_resources_and_wait_patch, lb_client, module)


def test_update_backend_set_policy_change(
    lb_client, create_or_update_lb_resources_and_wait_patch
):
    module = get_module(dict({"purge_backends": True}))
    assert_update_true(create_or_update_lb_resources_and_wait_patch, lb_client, module)


def test_update_backend_set_health_checker_change(
    lb_client, create_or_update_lb_resources_and_wait_patch
):
    module = get_module(dict({"purge_backends": True}))
    assert_update_true(create_or_update_lb_resources_and_wait_patch, lb_client, module)


def test_update_backend_set_sp_config_change(
    lb_client, create_or_update_lb_resources_and_wait_patch
):
    module = get_module(dict({"purge_backends": True}))
    assert_update_true(create_or_update_lb_resources_and_wait_patch, lb_client, module)


def test_update_backend_set_ssl_config_change(
    lb_client, create_or_update_lb_resources_and_wait_patch
):
    module = get_module(dict({"purge_backends": True}))
    assert_update_true(create_or_update_lb_resources_and_wait_patch, lb_client, module)


def assert_update_true(create_or_update_lb_resources_and_wait_patch, lb_client, module):
    backend_set = create_default_backend_set()
    create_or_update_lb_resources_and_wait_patch.return_value = {
        "backend_set": to_dict(backend_set),
        "changed": True,
    }
    result = oci_load_balancer_backend_set.update_backend_set(
        lb_client, module, "ocid1.loadbalancer.aaa", backend_set, "backend_set1"
    )
    assert result["changed"] is True


def test_delete_backend_set(lb_client, delete_lb_resources_and_wait_patch):
    module = get_module(dict())
    backend_set = create_default_backend_set()
    delete_lb_resources_and_wait_patch.return_value = {
        "backend_set": to_dict(backend_set),
        "changed": True,
    }
    result = oci_load_balancer_backend_set.delete_backend_set(lb_client, module)
    assert result["changed"] is True


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
    params = {
        "backends": [
            {
                "ip_address": "10.159.34.21",
                "port": 8080,
                "backup": True,
                "offline": False,
                "drain": True,
                "weight": 1,
            }
        ],
        "health_checker": {
            "interval_in_millis": 30000,
            "port": 8080,
            "protocol": "HTTP",
            "response_body_regex": "^(500|40[1348])$",
            "retries": 3,
            "timeout_in_millis": 6000,
            "return_code": 200,
            "url_path": "/healthcheck",
        },
        "policy": "LEAST_CONNECTIONS",
        "name": "backend_set1",
        "session_persistence_configuration": {
            "cookie_name": "my_cookie",
            "disable_fallback": True,
        },
        "ssl_configuration": {
            "certificate_name": "cert1",
            "verify_depth": 1,
            "verify_peer_certificate": True,
        },
        "load_balancer_id": "ocid1.loadbalancer.aaaa",
    }
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
