# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_smtp_credential
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.identity.models import SmtpCredential
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_smtp_credential.py requires `oci` module")


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
def check_and_create_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_create_resource")


@pytest.fixture()
def update_smtp_credential_patch(mocker):
    return mocker.patch.object(oci_smtp_credential, "update_smtp_credential")


@pytest.fixture()
def check_and_update_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_update_resource")


@pytest.fixture()
def create_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "create_and_wait")


@pytest.fixture()
def get_existing_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "get_existing_resource")


@pytest.fixture()
def delete_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "delete_and_wait")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_smtp_credential.set_logger(logging)


def test_create_or_update_smtp_credential_create(
    identity_client, check_and_create_resource_patch
):
    module = get_module()
    smtp_credential = get_smtp_credential()
    check_and_create_resource_patch.return_value = {
        "smtp_credential": to_dict(smtp_credential),
        "changed": True,
    }
    result = oci_smtp_credential.create_or_update_smtp_credential(
        identity_client, module
    )
    assert result["smtp_credential"]["description"] is smtp_credential.description


def test_create_or_update_smtp_credential_update(
    identity_client, update_smtp_credential_patch
):
    module = get_module(dict({"smtp_credential_id": "ocid1.smtpcredential.aaa"}))
    smtp_credential = get_smtp_credential()
    update_smtp_credential_patch.return_value = {
        "smtp_credential": to_dict(smtp_credential),
        "changed": True,
    }
    result = oci_smtp_credential.create_or_update_smtp_credential(
        identity_client, module
    )
    assert result["smtp_credential"]["description"] is smtp_credential.description


def test_create_or_update_smtp_credentiale_client_error(
    identity_client, check_and_create_resource_patch
):
    error_message = "mount target attribute has no value"
    module = get_module()
    check_and_create_resource_patch.side_effect = ClientError(Exception(error_message))
    try:
        oci_smtp_credential.create_or_update_smtp_credential(identity_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_smtp_credentiale_service_error(
    identity_client, check_and_create_resource_patch
):
    error_message = "Internal Server Error"
    module = get_module()
    check_and_create_resource_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_smtp_credential.create_or_update_smtp_credential(identity_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_smtp_credential(identity_client, create_and_wait_patch):
    module = get_module()
    smtp_credential = get_smtp_credential()
    create_and_wait_patch.return_value = {
        "smtp_credential": to_dict(smtp_credential),
        "changed": True,
    }
    result = oci_smtp_credential.create_smtp_credential(identity_client, module)
    assert result["smtp_credential"]["description"] is smtp_credential.description


def test_update_smtp_credential_descriptiom(
    identity_client, check_and_update_resource_patch
):
    smtp_credential = get_smtp_credential()
    module = get_module(
        dict(
            description="updated description",
            smtp_credential_id="ocid1.mounttarget.aaa",
        )
    )
    check_and_update_resource_patch.return_value = {
        "smtp_credential": to_dict(smtp_credential),
        "changed": True,
    }
    result = oci_smtp_credential.update_smtp_credential(identity_client, module)
    assert result["changed"] is True


def test_delete_smtp_credential(identity_client, delete_and_wait_patch):
    module = get_module(dict(smtp_credential_id="ocid1.mounttarget.aaa"))
    smtp_credential = get_smtp_credential()
    delete_and_wait_patch.return_value = {
        "smtp_credential": to_dict(smtp_credential),
        "changed": True,
    }
    result = oci_smtp_credential.delete_smtp_credential(identity_client, module)
    assert result["smtp_credential"]["description"] is smtp_credential.description


def get_smtp_credential():
    smtp_credential = SmtpCredential()
    smtp_credential.description = "test smtp description"
    return smtp_credential


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {
        "user_id": "ocid1.user.oc1..abuw",
        "description": "sample smtp credential",
    }
    if additional_properties:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
