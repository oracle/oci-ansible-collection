# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer, oci_load_balancer_listener
from ansible.module_utils.oracle import oci_utils, oci_lb_utils

try:
    import oci
    from oci.util import to_dict
    from oci.load_balancer.models import (
        Listener,
        SSLConfigurationDetails,
        LoadBalancer,
        ConnectionConfiguration,
    )
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_load_balancer_listener.py requires `oci` module")


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
def create_listener_patch(mocker):
    return mocker.patch.object(oci_load_balancer_listener, "create_listener")


@pytest.fixture()
def update_listener_patch(mocker):
    return mocker.patch.object(oci_load_balancer_listener, "update_listener")


@pytest.fixture()
def create_or_update_lb_resources_and_wait_patch(mocker):
    return mocker.patch.object(oci_lb_utils, "create_or_update_lb_resources_and_wait")


@pytest.fixture()
def delete_lb_resources_and_wait_patch(mocker):
    return mocker.patch.object(oci_lb_utils, "delete_lb_resources_and_wait")


@pytest.fixture()
def check_and_create_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_create_resource")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_load_balancer_listener.set_logger(logging)
    oci_load_balancer.set_logger(logging)


def test_create_or_update_listener_create(lb_client, check_and_create_resource_patch):
    module = get_module()
    load_balancer = LoadBalancer()
    load_balancer.listeners = dict()
    lb_client.get_load_balancer.return_value = get_response(
        200, None, load_balancer, None
    )
    check_and_create_resource_patch.return_value = {
        "listener": to_dict(get_listener()),
        "changed": True,
    }
    result = oci_load_balancer_listener.create_or_update_listener(lb_client, module)
    assert result["listener"]["name"] == module.params.get("name")


def test_create_or_update_listener_update(lb_client, update_listener_patch):
    module = get_module()
    update_listener_patch.return_value = {
        "listener": to_dict(get_listener()),
        "changed": True,
    }
    result = oci_load_balancer_listener.create_or_update_listener(lb_client, module)
    assert result["listener"]["name"] == module.params.get("name")


def test_create_or_update_listener_service_error(
    lb_client, check_and_create_resource_patch
):
    error_message = "Internal Server Error"
    module = get_module()
    load_balancer = LoadBalancer()
    load_balancer.listeners = dict()
    lb_client.get_load_balancer.return_value = get_response(
        200, None, load_balancer, None
    )
    check_and_create_resource_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    try:
        oci_load_balancer_listener.create_or_update_listener(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_listener_client_error(
    lb_client, check_and_create_resource_patch
):
    error_message = "Work Request Failed"
    module = get_module()
    load_balancer = LoadBalancer()
    load_balancer.listeners = dict()
    lb_client.get_load_balancer.return_value = get_response(
        200, None, load_balancer, None
    )
    check_and_create_resource_patch.side_effect = ClientError(
        Exception("Work Request Failed")
    )
    try:
        oci_load_balancer_listener.create_or_update_listener(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_listener(lb_client, create_or_update_lb_resources_and_wait_patch):
    module = get_module()
    create_or_update_lb_resources_and_wait_patch.return_value = {
        "listener": to_dict(get_listener()),
        "changed": True,
    }
    result = oci_load_balancer_listener.create_listener(
        lb_client, module, "ocid1.loadbalancer.aaaa", "ansible_listener"
    )
    assert result["listener"]["name"] == module.params.get("name")


def test_update_listener(lb_client, create_or_update_lb_resources_and_wait_patch):
    updated_backend_set_name = dict({"default_backend_set_name": "backend2"})
    module = get_module(updated_backend_set_name)
    create_or_update_lb_resources_and_wait_patch.return_value = {
        "listener": to_dict(get_listener()),
        "changed": True,
    }
    oci_load_balancer_listener.update_listener(
        lb_client, module, get_listener(), "ocid1.loadbalancer.aaaa", "ansible_listener"
    )
    assert create_or_update_lb_resources_and_wait_patch.called


def test_update_listener_ssl_config_changed(
    lb_client, create_or_update_lb_resources_and_wait_patch
):
    updated_backend_set_name = dict(
        {
            "ssl_configuration": {
                "certificate_name": "test_cert1",
                "verify_depth": 2,
                "verify_peer_certificate": True,
            }
        }
    )
    module = get_module(updated_backend_set_name)
    create_or_update_lb_resources_and_wait_patch.return_value = {
        "listener": to_dict(get_listener()),
        "changed": True,
    }
    oci_load_balancer_listener.update_listener(
        lb_client, module, get_listener(), "ocid1.loadbalancer.aaaa", "ansible_listener"
    )
    assert create_or_update_lb_resources_and_wait_patch.called


def test_update_listener_connection_configuration_changed(
    lb_client, create_or_update_lb_resources_and_wait_patch
):
    updated_backend_set_name = dict({"connection_configuration": {"idle_timeout": 600}})
    module = get_module(updated_backend_set_name)
    create_or_update_lb_resources_and_wait_patch.return_value = {
        "listener": to_dict(get_listener()),
        "changed": True,
    }
    oci_load_balancer_listener.update_listener(
        lb_client, module, get_listener(), "ocid1.loadbalancer.aaaa", "ansible_listener"
    )
    assert create_or_update_lb_resources_and_wait_patch.called


def test_update_listener_hostname_names_changed(
    lb_client, create_or_update_lb_resources_and_wait_patch
):
    updated_hostname_names = dict({"hostname_names": ["host_name_002"]})
    module = get_module(updated_hostname_names)
    create_or_update_lb_resources_and_wait_patch.return_value = {
        "listener": to_dict(get_listener()),
        "changed": True,
    }
    oci_load_balancer_listener.update_listener(
        lb_client, module, get_listener(), "ocid1.loadbalancer.aaaa", "ansible_listener"
    )
    assert create_or_update_lb_resources_and_wait_patch.called


def test_update_listener_path_route_set_name_changed(
    lb_client, create_or_update_lb_resources_and_wait_patch
):
    updated_path_route_set_name = dict({"path_route_set_name": "path_route_002"})
    module = get_module(updated_path_route_set_name)
    create_or_update_lb_resources_and_wait_patch.return_value = {
        "listener": to_dict(get_listener()),
        "changed": True,
    }
    oci_load_balancer_listener.update_listener(
        lb_client, module, get_listener(), "ocid1.loadbalancer.aaaa", "ansible_listener"
    )
    assert create_or_update_lb_resources_and_wait_patch.called


def test_update_listener_no_update(lb_client):
    module = get_module()
    result = oci_load_balancer_listener.update_listener(
        lb_client, module, get_listener(), "ocid1.loadbalancer.aaaa", "ansible_listener"
    )
    assert result["changed"] is False


def test_delete_listener(lb_client, delete_lb_resources_and_wait_patch):
    module = get_module()
    delete_lb_resources_and_wait_patch.return_value = {
        "listener": to_dict(get_listener()),
        "changed": True,
    }
    result = oci_load_balancer_listener.delete_listener(lb_client, module)
    assert result["changed"] is True


def get_listener():
    listener = Listener()
    listener.default_backend_set_name = "ansible_backend_set"
    listener.name = "ansible_listener"
    listener.port = 80
    listener.protocol = "HTTP"
    ssl_configuration_details = SSLConfigurationDetails()
    ssl_configuration_details.certificate_name = "cert1"
    ssl_configuration_details.__setattr__("verify_depth", 1)
    ssl_configuration_details.__setattr__("verify_peer_certificate", True)
    listener.ssl_configuration = ssl_configuration_details
    connection_configuration = ConnectionConfiguration()
    connection_configuration.idle_timeout = 1200
    listener.connection_configuration = connection_configuration
    listener.hostname_names = ["host_name_001"]
    listener.path_route_set_name = "path_route_001"
    return listener


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {
        "load_balancer_id": "ocid1.loadbalancer.oc1.iad.aaaa",
        "name": "ansible_listener",
        "default_backend_set_name": "ansible_backend_set",
        "port": 80,
        "protocol": "HTTP",
        "ssl_configuration": {
            "certificate_name": "cert1",
            "verify_depth": 1,
            "verify_peer_certificate": True,
        },
        "connection_configuration": {"idle_timeout": 1200},
    }
    if additional_properties is not None:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
