# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_backend
from ansible.module_utils.oracle import oci_utils, oci_lb_utils

try:
    import oci
    from oci.util import to_dict
    from oci.load_balancer.models import Backend, WorkRequest
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_load_balancer_backend.py requires `oci` module")


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
def create_backend_patch(mocker):
    return mocker.patch.object(oci_load_balancer_backend, "create_backend")


@pytest.fixture()
def update_backend_patch(mocker):
    return mocker.patch.object(oci_load_balancer_backend, "update_backend")


@pytest.fixture()
def create_or_update_lb_resources_and_wait_patch(mocker):
    return mocker.patch.object(oci_lb_utils, "create_or_update_lb_resources_and_wait")


@pytest.fixture()
def delete_lb_resources_and_wait_patch(mocker):
    return mocker.patch.object(oci_lb_utils, "delete_lb_resources_and_wait")


@pytest.fixture()
def check_and_create_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_create_resource")


@pytest.fixture()
def get_existing_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "get_existing_resource")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_load_balancer_backend.set_logger(logging)


def test_create_or_update_backend_create(
    lb_client, check_and_create_resource_patch, get_existing_resource_patch
):
    module = get_module()
    backend = get_backend()
    get_existing_resource_patch.return_value = None
    check_and_create_resource_patch.return_value = {
        "backend": to_dict(backend),
        "changed": True,
    }
    result = oci_load_balancer_backend.create_or_update_backend(lb_client, module)
    assert result["backend"]["ip_address"] is backend.ip_address


def test_create_or_update_backend_update(
    lb_client, update_backend_patch, get_existing_resource_patch
):
    module = get_module()
    backend = get_backend()
    get_existing_resource_patch.return_value = backend
    update_backend_patch.return_value = {"backend": to_dict(backend), "changed": True}
    result = oci_load_balancer_backend.create_or_update_backend(lb_client, module)
    assert result["backend"]["ip_address"] is backend.ip_address


def test_create_or_update_backend_service_error(
    lb_client, check_and_create_resource_patch, get_existing_resource_patch
):
    module = get_module()
    error_message = "Internal Server Error"
    check_and_create_resource_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    get_existing_resource_patch.return_value = None
    try:
        oci_load_balancer_backend.create_or_update_backend(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_backend_client_error(
    lb_client, check_and_create_resource_patch, get_existing_resource_patch
):
    module = get_module()
    error_message = "Work Request Failed"
    check_and_create_resource_patch.side_effect = ClientError(
        Exception("Work Request Failed")
    )
    get_existing_resource_patch.return_value = None
    try:
        oci_load_balancer_backend.create_or_update_backend(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_backend(lb_client, create_or_update_lb_resources_and_wait_patch):
    module = get_module()
    backend = get_backend()
    create_or_update_lb_resources_and_wait_patch.return_value = {
        "backend": to_dict(backend),
        "changed": True,
    }
    result = oci_load_balancer_backend.create_backend(
        lb_client, module, "ocid1.loadbalancer.oc1.iad.aaaaa", "10.159.34.21:8181"
    )
    assert result["backend"]["name"] == backend.name


def test_update_backend(lb_client, create_or_update_lb_resources_and_wait_patch):
    module = get_module()
    backend = get_backend()
    create_or_update_lb_resources_and_wait_patch.return_value = {
        "backend": to_dict(backend),
        "changed": True,
    }
    result = oci_load_balancer_backend.update_backend(
        lb_client,
        module,
        backend,
        "ocid1.loadbalancer.oc1.iad.aaaaa",
        "10.159.34.21:8181",
    )
    assert result["changed"] is True


def test_update_backend_no_update(lb_client):
    module = get_module()
    backend = get_backend()
    backend.offline = False
    result = oci_load_balancer_backend.update_backend(
        lb_client,
        module,
        backend,
        "ocid1.loadbalancer.oc1.iad.aaaaa",
        "10.159.34.21:8181",
    )
    assert result["changed"] is False


def test_delete_backend(lb_client, delete_lb_resources_and_wait_patch):
    module = get_module()
    backend = get_backend()
    delete_lb_resources_and_wait_patch.return_value = get_response(
        204, None, backend, None
    )
    delete_lb_resources_and_wait_patch.return_value = {
        "backend": to_dict(backend),
        "changed": True,
    }
    result = oci_load_balancer_backend.delete_backend(lb_client, module)
    assert result["changed"] is True


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


def get_module():
    params = {
        "load_balancer_id": "ocid1.loadbalancer.oc1.iad.aaaaa",
        "backend_set_name": "backend1",
        "ip_address": "10.159.34.21",
        "port": "8181",
        "backup": True,
        "offline": False,
        "drain": True,
        "weight": 5,
    }
    module = FakeModule(**params)
    return module
