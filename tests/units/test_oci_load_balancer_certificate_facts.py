# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_certificate_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.load_balancer.models import Certificate
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_load_balancer_certificate_facts.py requires `oci` module")


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
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_load_balancer_certificate_facts.set_logger(logging)


def test_list_load_balancer_certificates_specific_certificate(lb_client):
    module = get_module(
        dict(
            {
                "name": "ansible_certificate_one",
                "load_balancer_id": "ocid1.lodbalancer.xcds",
            }
        )
    )
    lb_client.list_certificates.return_value = get_response(
        200, None, get_certificates(), None
    )
    result = oci_load_balancer_certificate_facts.list_load_balancer_certificates(
        lb_client, module
    )
    assert result["certificates"][0]["certificate_name"] is module.params.get("name")


def test_list_load_balancer_certificates_all_certificates(
    lb_client, list_all_resources_patch
):
    module = get_module(dict({"load_balancer_id": "ocid1.lodbalancer.xcds"}))
    list_all_resources_patch.return_value = get_certificates()
    result = oci_load_balancer_certificate_facts.list_load_balancer_certificates(
        lb_client, module
    )
    assert len(result["certificates"]) is 2


def test_list_load_balancer_certificates_service_error(
    lb_client, list_all_resources_patch
):
    error_message = "Internal Server Error"
    module = get_module(dict({"load_balancer_id": "ocid1.lodbalancer.xcds"}))
    list_all_resources_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    try:
        oci_load_balancer_certificate_facts.list_load_balancer_certificates(
            lb_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def get_certificates():
    certificate_one = Certificate()
    certificate_one.certificate_name = "ansible_certificate_one"
    certificate_two = Certificate()
    certificate_two.certificate_name = "ansible_certificate_two"
    return [certificate_one, certificate_two]


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = dict()
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
