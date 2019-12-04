# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.load_balancer.models import LoadBalancer
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_bucket.py requires `oci` module")


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
    mock_identity_client = mocker.patch("oci.identity.identity_client.IdentityClient")
    return mock_identity_client.return_value


@pytest.fixture()
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_load_balancer_facts.set_logger(logging)


def test_list_load_balancers_compartment_id(lb_client, list_all_resources_patch):
    module = get_module(
        dict({"compartment_id": "ocid1.compartment.xscf", "load_balancer_id": None})
    )
    load_balancer = LoadBalancer()
    load_balancer.id = "ocid.loadbalancer.cvghs"
    load_balancer.display_name = "ansible_lb"
    list_all_resources_patch.return_value = [load_balancer]
    result = oci_load_balancer_facts.list_load_balancers(lb_client, module)
    assert result["load_balancers"][0]["id"] == load_balancer.id


def test_list_load_balancers_load_balancer_id(lb_client):
    module = get_module(
        dict({"compartment_id": None, "load_balancer_id": "ocid1.lodbalancer.xcds"})
    )
    load_balancer = LoadBalancer()
    load_balancer.id = "ocid.loadbalancer.cvghs"
    load_balancer.display_name = "ansible_lb"
    lb_client.get_load_balancer.return_value = get_response(
        200, None, load_balancer, None
    )
    result = oci_load_balancer_facts.list_load_balancers(lb_client, module)
    assert result["load_balancers"][0]["id"] == load_balancer.id


def test_list_load_balancers_service_error(lb_client):
    error_message = "Internal Server Error"
    module = get_module(
        dict({"compartment_id": None, "load_balancer_id": "ocid1.lodbalancer.xcds"})
    )
    lb_client.get_load_balancer.side_effect = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    try:
        oci_load_balancer_facts.list_load_balancers(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = dict()
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
