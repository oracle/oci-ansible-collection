# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.module_utils.oracle import oci_utils
from ansible.modules.cloud.oracle import oci_waas_work_request

try:
    import oci
    from oci.waas.models import WorkRequest
    from oci.util import to_dict
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_waas_work_request.py requires `oci` module")


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
def call_with_backoff_patch(mocker):
    return mocker.patch.object(oci_utils, "call_with_backoff")


@pytest.fixture()
def oci_wait_until_patch(mocker):
    return mocker.patch.object(oci, "wait_until")


def get_module(**kwargs):
    params = dict(work_request_id="ocid1.waasworkrequest.oc1..xxxxxEXAMPLExxxxx")
    params.update(kwargs)
    module = FakeModule(**params)
    return module


def get_response(status=200, headers=None, data=None, request=None):
    if not headers:
        headers = dict()
    return oci.Response(status, headers, data, request)


def get_work_request():
    return WorkRequest(
        id="ocid1.waasworkrequest.oc1..xxxxxEXAMPLExxxxx1",
        compartment_id="ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
    )


def test_cancel_work_request_raises_service_error(waas_client, call_with_backoff_patch):
    call_with_backoff_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    with pytest.raises(ServiceError) as exc_info:
        oci_waas_work_request.cancel_work_request(waas_client, get_module())
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"


def test_cancel_work_request_does_not_call_wait_until_when_wait_set_to_false(
    waas_client, call_with_backoff_patch, oci_wait_until_patch
):
    module = get_module(wait=False)
    work_request = get_work_request()
    call_with_backoff_patch.return_value = get_response(data=work_request)
    result = oci_waas_work_request.cancel_work_request(waas_client, module)
    assert call_with_backoff_patch.call_count == 2
    call_with_backoff_patch.assert_any_call(
        waas_client.cancel_work_request,
        work_request_id=module.params["work_request_id"],
    )
    call_with_backoff_patch.assert_any_call(
        waas_client.get_work_request, work_request_id=module.params["work_request_id"]
    )
    assert oci_wait_until_patch.call_count == 0
    assert result["changed"] is True
    assert result["waas_work_request"] == to_dict(work_request)


def test_cancel_work_request_calls_wait_until_when_wait_set_to_true(
    waas_client, call_with_backoff_patch, oci_wait_until_patch
):
    module = get_module(wait=True)
    work_request = get_work_request()
    call_with_backoff_patch.return_value = get_response(data=work_request)
    oci_wait_until_patch.return_value = get_response(data=work_request)
    result = oci_waas_work_request.cancel_work_request(waas_client, module)
    assert call_with_backoff_patch.call_count == 2
    call_with_backoff_patch.assert_any_call(
        waas_client.cancel_work_request,
        work_request_id=module.params["work_request_id"],
    )
    call_with_backoff_patch.assert_any_call(
        waas_client.get_work_request, work_request_id=module.params["work_request_id"]
    )
    assert oci_wait_until_patch.call_count == 1
    assert result["changed"] is True
    assert result["waas_work_request"] == to_dict(work_request)
