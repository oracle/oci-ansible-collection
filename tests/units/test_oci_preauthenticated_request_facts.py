# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_preauthenticated_request_facts
from ansible.module_utils.oracle import oci_utils


try:
    import oci
    from oci.object_storage.models import PreauthenticatedRequestSummary
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_preauthenticated_request_facts.py requires `oci` module")


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
def identity_client(mocker):
    mock_identity_client = mocker.patch("oci.identity.identity_client.IdentityClient")
    return mock_identity_client.return_value


@pytest.fixture()
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_preauthenticated_request_facts.set_logger(logging)


def test_list_suppressions_list_all(identity_client, list_all_resources_patch):
    module = get_module()
    list_all_resources_patch.return_value = get_preauthenticated_request_summaries()
    result = oci_preauthenticated_request_facts.list_preauthenticated_requests(
        identity_client, module
    )
    assert len(result["preauthenticated_requests"]) is 2


def test_list_suppressions_list_specific(identity_client):
    module = get_module(dict({"par_id": "xvdz:=test.html"}))
    preauthenticated_request_summary = get_preauthenticated_request_summary()
    identity_client.get_preauthenticated_request.return_value = get_response(
        200, None, preauthenticated_request_summary, None
    )
    result = oci_preauthenticated_request_facts.list_preauthenticated_requests(
        identity_client, module
    )
    assert (
        result["preauthenticated_requests"][0]["name"]
        is preauthenticated_request_summary.name
    )


def test_list_suppression_service_error(identity_client):
    error_message = "Internal Server Error"
    module = get_module(dict({"par_id": "xvdz:=test.html"}))
    identity_client.get_preauthenticated_request.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_preauthenticated_request_facts.list_preauthenticated_requests(
            identity_client, module
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def get_preauthenticated_request_summaries():
    preauthenticated_request_summaries = []
    preauthenticated_request_summary1 = PreauthenticatedRequestSummary()
    preauthenticated_request_summary1.name = "test_par1"
    preauthenticated_request_summary2 = PreauthenticatedRequestSummary()
    preauthenticated_request_summary2.name = "test_par2"
    preauthenticated_request_summaries.append(preauthenticated_request_summary1)
    preauthenticated_request_summaries.append(preauthenticated_request_summary2)
    return preauthenticated_request_summaries


def get_preauthenticated_request_summary():
    preauthenticated_request_summary = PreauthenticatedRequestSummary()
    preauthenticated_request_summary.name = "test_par"
    return preauthenticated_request_summary


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {"namespace_name": "example_namespace", "bucket_name": "test_bucket"}
    if additional_properties:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
