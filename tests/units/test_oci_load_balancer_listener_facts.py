# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_listener_facts
from ansible.module_utils.oracle import oci_utils, oci_lb_utils

try:
    import oci
    from oci.load_balancer.models import (
        Listener,
        SSLConfigurationDetails,
        LoadBalancer,
        ConnectionConfiguration,
    )
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_load_balancer_listener_facts.py requires `oci` module")


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
    oci_load_balancer_listener_facts.set_logger(logging)


def test_list_load_balancer_listeners_specific_listener(lb_client):
    module = get_module(
        dict({"name": "ansible_listener", "load_balancer_id": "ocid1.lodbalancer.xcds"})
    )
    load_balancer = LoadBalancer()
    load_balancer.listeners = dict({"ansible_listener": get_listener()})
    lb_client.get_load_balancer.return_value = get_response(
        200, None, load_balancer, None
    )
    result = oci_load_balancer_listener_facts.list_load_balancer_listeners(
        lb_client, module
    )
    assert result["listeners"][0]["name"] == module.params.get("name")


def test_list_load_balancer_listeners_all_listeners(lb_client):
    module = get_module(dict({"load_balancer_id": "ocid1.lodbalancer.xcds"}))
    load_balancer = LoadBalancer()
    load_balancer.listeners = dict({"ansible_listener": get_listener()})
    lb_client.get_load_balancer.return_value = get_response(
        200, None, load_balancer, None
    )
    result = oci_load_balancer_listener_facts.list_load_balancer_listeners(
        lb_client, module
    )
    assert result["listeners"][0]["name"] == "ansible_listener"


def test_list_load_balancer_listeners_service_error(lb_client):
    error_message = "Internal Server Error"
    module = get_module(
        dict({"name": "ansible_listener", "load_balancer_id": "ocid1.lodbalancer.xcds"})
    )
    load_balancer = LoadBalancer()
    load_balancer.listeners = dict({"ansible_listener": get_listener()})
    lb_client.get_load_balancer.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_load_balancer_listener_facts.list_load_balancer_listeners(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


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
    return listener


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = dict()
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
