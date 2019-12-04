# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.module_utils.oracle import oci_utils
from ansible.modules.cloud.oracle import oci_waas_work_request_facts

try:
    import oci
    from oci.util import to_dict
    from oci.response import Response
    from oci.exceptions import ServiceError
    from oci.waas.models import WorkRequestSummary
except ImportError:
    raise SkipTest("test_oci_waas_work_request_facts.py requires `oci` module")


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


def get_module(with_work_request=False, **kwargs):
    if with_work_request:
        params = dict(work_request_id="ocid1.waasworkrequest.oc1..xxxxxEXAMPLExxxxx")
    else:
        params = dict(
            compartment_id="ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            waas_policy_id="ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx",
        )
    params.update(kwargs)
    module = FakeModule(**params)
    return module


def get_work_requests():
    return [
        WorkRequestSummary(
            id="ocid1.waasworkrequest.oc1..xxxxxEXAMPLExxxxx1",
            compartment_id="ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
        ),
        WorkRequestSummary(
            id="ocid1.waasworkrequest.oc1..xxxxxEXAMPLExxxxx2",
            compartment_id="ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
        ),
    ]


def get_response(status=200, headers=None, data=None, request=None):
    if not headers:
        headers = dict()
    return oci.Response(status, headers, data, request)


def test_list_work_requests_raises_service_error(waas_client, list_all_resources_patch):
    list_all_resources_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    with pytest.raises(ServiceError) as exc_info:
        oci_waas_work_request_facts.list_work_requests(waas_client, get_module())
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"


def test_list_work_requests_fails_when_required_attrs_not_present_in_module(
    waas_client, list_all_resources_patch
):
    module = FakeModule()
    with pytest.raises(Exception) as exc_info:
        oci_waas_work_request_facts.list_work_requests(waas_client, module)
    ex = exc_info.value
    assert "required to list work requests" in str(ex)
    module = FakeModule(compartment_id="ocid1.compartment.oc1..xxxxxEXAMPLExxxxx")
    with pytest.raises(Exception) as exc_info:
        oci_waas_work_request_facts.list_work_requests(waas_client, module)
    ex = exc_info.value
    assert "required to list work requests" in str(ex)
    module = FakeModule(waas_policy_id="ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx")
    with pytest.raises(Exception) as exc_info:
        oci_waas_work_request_facts.list_work_requests(waas_client, module)
    ex = exc_info.value
    assert "required to list work requests" in str(ex)


def test_list_work_requests_calls_list_all_resources_with_correct_parameters(
    waas_client, list_all_resources_patch
):
    module = get_module(sort_by="timeStarted", sort_order="DESC")
    list_all_resources_patch.return_value = []
    oci_waas_work_request_facts.list_work_requests(waas_client, module)
    list_all_resources_patch.assert_called_once()
    list_all_resources_patch.assert_called_with(
        waas_client.list_work_requests,
        compartment_id=module.params["compartment_id"],
        waas_policy_id=module.params["waas_policy_id"],
        sort_by="timeStarted",
        sort_order="DESC",
    )


def test_list_work_requests_calls_get_work_request(
    waas_client, list_all_resources_patch, call_with_backoff_patch
):
    module = get_module()
    work_requests = get_work_requests()
    list_all_resources_patch.return_value = work_requests
    oci_waas_work_request_facts.list_work_requests(waas_client, module)
    list_all_resources_patch.assert_called_once()
    assert call_with_backoff_patch.call_count == 2
    call_with_backoff_patch.assert_any_call(
        waas_client.get_work_request, work_request_id=work_requests[0].id
    )
    call_with_backoff_patch.assert_any_call(
        waas_client.get_work_request, work_request_id=work_requests[1].id
    )


def test_get_work_request_raises_service_error(waas_client, call_with_backoff_patch):
    call_with_backoff_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    with pytest.raises(ServiceError) as exc_info:
        oci_waas_work_request_facts.get_work_request(
            waas_client, get_module(with_work_request=True)
        )
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"


def test_get_work_request_calls_call_with_backoff_with_correct_parameters(
    waas_client, call_with_backoff_patch
):
    module = get_module(with_work_request=True)
    call_with_backoff_patch.return_value = get_response(data=None)
    oci_waas_work_request_facts.get_work_request(waas_client, module)
    call_with_backoff_patch.assert_called_once()
    call_with_backoff_patch.assert_called_with(
        waas_client.get_work_request, work_request_id=module.params["work_request_id"]
    )
