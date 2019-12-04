# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_preauthenticated_request
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.object_storage.models import PreauthenticatedRequest
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_preauthenicated_request.py requires `oci` module")


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
def create_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "create_resource")


@pytest.fixture()
def delete_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "delete_and_wait")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_preauthenticated_request.set_logger(logging)


def test_create__preauthenicate_request(identity_client, create_resource_patch):
    module = get_module()
    preauthenticated_request = get_preauthenticated_request()
    create_resource_patch.return_value = {
        "preauthenticated_request": to_dict(preauthenticated_request),
        "changed": True,
    }
    result = oci_preauthenticated_request.create_preauthenticated_request(
        identity_client, module
    )
    assert result["preauthenticated_request"]["name"] is preauthenticated_request.name


def test_delete_suppression(identity_client, delete_and_wait_patch):
    module = get_module(dict({"par_id": "rE=:test.html"}))
    preauthenticated_request = get_preauthenticated_request()
    delete_and_wait_patch.return_value = dict(
        {"preauthenticated_request": to_dict(preauthenticated_request), "changed": True}
    )
    result = oci_preauthenticated_request.delete_preauthenticated_request(
        identity_client, module
    )
    assert result["changed"] is True


def get_preauthenticated_request():
    preauthenticated_request = PreauthenticatedRequest()
    preauthenticated_request.name = "test_preauthenticated_request"
    return preauthenticated_request


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {
        "namespace_name": "example_namespace",
        "bucket_name": "test_bucket",
        "time_expires": "2018-12-22T00:00:00+00:00",
    }
    if additional_properties:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
