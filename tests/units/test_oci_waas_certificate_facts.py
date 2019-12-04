# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.module_utils.oracle import oci_utils
from ansible.modules.cloud.oracle import oci_waas_certificate_facts

try:
    import oci
    from oci.util import to_dict
    from oci.response import Response
    from oci.exceptions import ServiceError
    from oci.waas.models import CertificateSummary
except ImportError:
    raise SkipTest("test_oci_waas_certificate_facts.py requires `oci` module")


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
def waas_client(mocker):
    mock_waas_client = mocker.patch("oci.waas.waas_client.WaasClient")
    return mock_waas_client.return_value


@pytest.fixture()
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


@pytest.fixture()
def call_with_backoff_patch(mocker):
    return mocker.patch.object(oci_utils, "call_with_backoff")


def get_module(**kwargs):
    params = {}
    params.update(kwargs)
    module = FakeModule(**params)
    return module


def get_certificates():
    return [
        CertificateSummary(
            id="ocid1.waascertificate.oc1..xxxxxEXAMPLExxxxx1", display_name="testname1"
        ),
        CertificateSummary(
            id="ocid1.waascertificate.oc1..xxxxxEXAMPLExxxxx2", display_name="testname2"
        ),
    ]


def get_response(status=200, headers=None, data=None, request=None):
    if not headers:
        headers = dict()
    return oci.Response(status, headers, data, request)


def test_list_certificates_raises_service_error(waas_client, list_all_resources_patch):
    list_all_resources_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    with pytest.raises(ServiceError) as exc_info:
        oci_waas_certificate_facts.list_certificates(
            waas_client,
            get_module(compartment_id="ocid1.compartment.oc1..xxxxxEXAMPLExxxxx"),
        )
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"


def test_list_certificates_calls_list_all_resources_with_correct_parameters(
    waas_client, list_all_resources_patch
):
    id = [
        "ocid1.waascertificate.oc1..xxxxxEXAMPLExxxxx1",
        "ocid1.waascertificate.oc1..xxxxxEXAMPLExxxxx2",
    ]
    display_name = "testname1"
    lifecycle_state = ["ACTIVE", "CREATING"]
    module = get_module(
        compartment_id="ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
        sort_by="timeCreated",
        sort_order="DESC",
        id=id,
        display_name=display_name,
        lifecycle_state=lifecycle_state,
        time_created_greater_than_or_equal_to="2019-04-02T17:12:42.454000+00:00",
        time_created_less_than="2019-04-02T17:12:42.454000+00:00",
    )
    list_all_resources_patch.return_value = []
    oci_waas_certificate_facts.list_certificates(waas_client, module)
    list_all_resources_patch.assert_called_once()
    list_all_resources_patch.assert_called_with(
        waas_client.list_certificates,
        compartment_id="ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
        sort_by="timeCreated",
        sort_order="DESC",
        id=id,
        display_name=display_name,
        lifecycle_state=lifecycle_state,
        time_created_greater_than_or_equal_to="2019-04-02T17:12:42.454000+00:00",
        time_created_less_than="2019-04-02T17:12:42.454000+00:00",
    )


def test_list_certificates_calls_get_certificate(
    waas_client, list_all_resources_patch, call_with_backoff_patch
):
    module = get_module(compartment_id="ocid1.compartment.oc1..xxxxxEXAMPLExxxxx")
    certificates = get_certificates()
    list_all_resources_patch.return_value = certificates
    oci_waas_certificate_facts.list_certificates(waas_client, module)
    list_all_resources_patch.assert_called_once()
    assert call_with_backoff_patch.call_count == 2
    call_with_backoff_patch.assert_any_call(
        waas_client.get_certificate, certificate_id=certificates[0].id
    )
    call_with_backoff_patch.assert_any_call(
        waas_client.get_certificate, certificate_id=certificates[1].id
    )


def test_get_certificate_raises_service_error(waas_client, call_with_backoff_patch):
    call_with_backoff_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    with pytest.raises(ServiceError) as exc_info:
        oci_waas_certificate_facts.get_certificate(
            waas_client,
            get_module(certificate_id="ocid1.waascertificate.oc1..xxxxxEXAMPLExxxxx"),
        )
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"


def test_get_certificate_calls_call_with_backoff_with_correct_parameters(
    waas_client, call_with_backoff_patch
):
    certificate_id = "ocid1.waascertificate.oc1..xxxxxEXAMPLExxxxx"
    module = get_module(certificate_id=certificate_id)
    call_with_backoff_patch.return_value = get_response(data=None)
    oci_waas_certificate_facts.get_certificate(waas_client, module)
    call_with_backoff_patch.assert_called_once()
    call_with_backoff_patch.assert_called_with(
        waas_client.get_certificate, certificate_id=certificate_id
    )
