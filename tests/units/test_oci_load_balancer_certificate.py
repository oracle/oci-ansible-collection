# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_certificate
from ansible.module_utils.oracle import oci_lb_utils
import tempfile
import os
from ansible.module_utils import six

try:
    import oci
    from oci.util import to_dict
    from oci.load_balancer.models import (
        Certificate,
        WorkRequest,
        CreateCertificateDetails,
    )
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_load_balancer_certificate.py requires `oci` module")


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
def get_certificate_patch(mocker):
    return mocker.patch.object(oci_lb_utils, "get_certificate")


@pytest.fixture()
def is_same_certificate_patch(mocker):
    return mocker.patch.object(oci_lb_utils, "is_same_certificate")


@pytest.fixture()
def create_or_update_lb_resources_and_wait_patch(mocker):
    return mocker.patch.object(oci_lb_utils, "create_or_update_lb_resources_and_wait")


@pytest.fixture()
def delete_lb_resources_and_wait_patch(mocker):
    return mocker.patch.object(oci_lb_utils, "delete_lb_resources_and_wait")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_load_balancer_certificate.set_logger(logging)


def test_create_certificate(
    lb_client, get_certificate_patch, create_or_update_lb_resources_and_wait_patch
):
    certificate_bundle = get_certificate_bundle()
    module = get_module(certificate_bundle)
    certificate = get_certificate(certificate_bundle)
    get_certificate_patch.side_effect = [None, certificate]
    create_or_update_lb_resources_and_wait_patch.return_value = dict(
        certificate=to_dict(certificate), changed=True
    )
    result = oci_load_balancer_certificate.create_certificate(lb_client, module)
    delete_cert_bundle(certificate_bundle)
    assert result["changed"] is True


def test_create_certificate_certificate_exists_with_different_attribute_values(
    lb_client, get_certificate_patch, is_same_certificate_patch
):
    module = get_module(dict())
    error_message = (
        "Certificate "
        + module.params.get("name")
        + " with different attribute value already available in load balancer "
        + module.params.get("load_balancer_id")
    )
    certificate = get_certificate(dict())
    get_certificate_patch.return_value = certificate
    is_same_certificate_patch.return_value = False
    try:
        oci_load_balancer_certificate.create_certificate(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_certificate_certificate_exists_with_same_attribute_values(
    lb_client, get_certificate_patch, is_same_certificate_patch
):
    module = get_module(dict())
    certificate = get_certificate(dict())
    get_certificate_patch.return_value = certificate
    is_same_certificate_patch.return_value = True
    result = oci_load_balancer_certificate.create_certificate(lb_client, module)
    assert result["changed"] is False


def test_create_certificate_service_error(lb_client, get_certificate_patch):
    error_message = "Internal Server Error"
    module = get_module(dict())
    get_certificate_patch.return_value = None
    lb_client.create_certificate.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_load_balancer_certificate.create_certificate(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_certificate_client_error(lb_client, get_certificate_patch):
    error_message = "Work Request Failed"
    module = get_module(dict())
    get_certificate_patch.return_value = None
    create_or_update_lb_resources_and_wait_patch.side_effect = ClientError(
        Exception("Work Request Failed")
    )
    try:
        oci_load_balancer_certificate.create_certificate(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


"""
def test_get_existing_certificate(lb_client):
    certificate_bundle = get_certificate_bundle()
    module = get_module(certificate_bundle)
    certificate = get_certificate(certificate_bundle)
    lb_client.list_certificates.return_value = get_response(
        200, None, [certificate], None)
    result = oci_load_balancer_certificate.get_existing_certificate(
        lb_client, module, 'ocid1.loadbalancer.aaaa', module.params.get('name'))
    delete_cert_bundle(certificate_bundle)
    assert result.certificate_name is module.params.get('name')


def test_get_existing_certificate_not_found(lb_client):
    certificate_bundle = get_certificate_bundle()
    module = get_module(certificate_bundle)
    certificate = get_certificate(certificate_bundle)
    lb_client.list_certificates.return_value = get_response(
        200, None, [certificate], None)
    result = oci_load_balancer_certificate.get_existing_certificate(
        lb_client, module, 'ocid1.loadbalancer.aaaa', 'other_name')
    delete_cert_bundle(certificate_bundle)
    assert result is None


def test_get_existing_certificate_service_error(lb_client):
    error_message = "Internal Server Error"
    certificate_bundle = get_certificate_bundle()
    module = get_module(certificate_bundle)
    certificate = get_certificate(certificate_bundle)
    lb_client.list_certificates.side_effect = ServiceError(
        499, 'InternalServerError', dict(), error_message)
    delete_cert_bundle(certificate_bundle)
    try:
        result = oci_load_balancer_certificate.get_existing_certificate(
            lb_client, module, 'ocid1.loadbalancer.aaaa', 'other_name')
    except Exception as ex:
        assert error_message in ex.args[0]


def test_is_same_certificate_true():
    certificate_bundle = get_certificate_bundle()
    certificate = get_certificate(certificate_bundle)
    create_certificate_details = CreateCertificateDetails()
    create_certificate_details.ca_certificate = certificate.ca_certificate
    create_certificate_details.certificate_name = certificate.certificate_name
    create_certificate_details.public_certificate = certificate.public_certificate
    result = oci_load_balancer_certificate.is_same_certificate(create_certificate_details, certificate)
    delete_cert_bundle(certificate_bundle)
    assert result is True

def test_is_same_certificate_false():
    certificate_bundle = get_certificate_bundle()
    certificate = get_certificate(certificate_bundle)
    create_certificate_details = CreateCertificateDetails()
    create_certificate_details.ca_certificate = certificate.ca_certificate
    create_certificate_details.certificate_name = 'other_name'
    create_certificate_details.public_certificate = certificate.public_certificate
    result = oci_load_balancer_certificate.is_same_certificate(create_certificate_details, certificate)
    delete_cert_bundle(certificate_bundle)
    assert result is False
"""


def test_delete_certificate(lb_client, delete_lb_resources_and_wait_patch):
    module = get_module(dict())
    certificate = get_certificate(dict())
    delete_lb_resources_and_wait_patch.return_value = dict(
        certificate=to_dict(certificate), changed=True
    )
    result = oci_load_balancer_certificate.delete_certificate(lb_client, module)
    assert result["changed"] is True


def get_certificate(cert_bundle):
    certificate = Certificate()
    certificate.ca_certificate = cert_bundle.get("ca_certificate")
    certificate.public_certificate = cert_bundle.get("public_certificate")
    certificate.certificate_name = "test_certificate"
    return certificate


def get_certificate_bundle():
    cert_attributes = ["ca_certificate", "private_key", "public_certificate"]
    cert_bundle = dict()
    for cert_attribute in cert_attributes:
        new_file, filename = tempfile.mkstemp()
        os.write(new_file, b"Certificate content")
        cert_bundle.update({cert_attribute: filename})
    return cert_bundle


def delete_cert_bundle(certificate_bundle):
    cert_attributes = ["ca_certificate", "private_key", "public_certificate"]
    for dummy, value in six.iteritems(certificate_bundle):
        os.remove(value)


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = {
        "load_balancer_id": "ocid1.loadbalancer.oc1.iad.aaaaa",
        "name": "test_certificate",
        "passphrase": "secret",
    }
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
