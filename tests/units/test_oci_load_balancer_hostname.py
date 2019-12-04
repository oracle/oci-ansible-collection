# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_hostname
from ansible.module_utils.oracle import oci_utils, oci_lb_utils

try:
    import oci
    from oci.util import to_dict
    from oci.load_balancer.models import Hostname, WorkRequest
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_load_balancer_hostname.py requires `oci` module")


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
def update_hostname_patch(mocker):
    return mocker.patch.object(oci_load_balancer_hostname, "update_hostname")


@pytest.fixture()
def verify_work_request_patch(mocker):
    return mocker.patch.object(oci_lb_utils, "verify_work_request")


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
    oci_load_balancer_hostname.set_logger(logging)


def test_create_or_update_backend_create(
    lb_client, check_and_create_resource_patch, get_existing_resource_patch
):
    module = get_module()
    hostname = get_hostname()
    get_existing_resource_patch.return_value = None
    check_and_create_resource_patch.return_value = {
        "hostname": to_dict(hostname),
        "changed": True,
    }
    result = oci_load_balancer_hostname.create_or_update_hostname(lb_client, module)
    assert result["hostname"]["name"] is hostname.name


def test_create_or_update_backend_update(
    lb_client, update_hostname_patch, get_existing_resource_patch
):
    module = get_module()
    hostname = get_hostname()
    get_existing_resource_patch.return_value = hostname
    update_hostname_patch.return_value = {
        "hostname": to_dict(hostname),
        "changed": True,
    }
    result = oci_load_balancer_hostname.create_or_update_hostname(lb_client, module)
    assert result["hostname"]["name"] is hostname.name


def test_create_backend(lb_client, create_or_update_lb_resources_and_wait_patch):
    module = get_module(dict(hostname="app.example.com"))
    hostname = get_hostname()
    create_or_update_lb_resources_and_wait_patch.return_value = {
        "hostname": to_dict(hostname),
        "changed": True,
    }
    result = oci_load_balancer_hostname.create_hostname(lb_client, module)
    assert result["hostname"]["name"] is hostname.name


def test_update_backend(lb_client, create_or_update_lb_resources_and_wait_patch):
    module = get_module(dict(hostname="app.production.com"))
    hostname = get_hostname()
    oci_load_balancer_hostname.update_hostname(
        lb_client, module, "ocid1.loadbalancer.oc1.iad.aaaaa", hostname, "hostname_001"
    )
    assert create_or_update_lb_resources_and_wait_patch.called


def test_update_backend_no_update(
    lb_client, create_or_update_lb_resources_and_wait_patch
):
    module = get_module()
    hostname = get_hostname()
    oci_load_balancer_hostname.update_hostname(
        lb_client, module, "ocid1.loadbalancer.oc1.iad.aaaaa", hostname, "hostname_001"
    )
    assert not create_or_update_lb_resources_and_wait_patch.called


def test_delete_hostname(lb_client, delete_lb_resources_and_wait_patch):
    module = get_module()
    hostname = get_hostname()
    delete_lb_resources_and_wait_patch.return_value = {
        "hostname": to_dict(hostname),
        "changed": True,
    }
    result = oci_load_balancer_hostname.delete_hostname(lb_client, module)
    assert result["changed"] is True


def get_hostname():
    hostname = Hostname()
    hostname.name = "hostname_001"
    hostname.hostname = "app.example.com"
    return hostname


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_info=None):
    params = {
        "load_balancer_id": "ocid1.loadbalancer.oc1.iad.aaaaa",
        "name": "hostname_001",
    }
    if additional_info:
        params.update(additional_info)
    module = FakeModule(**params)
    return module
