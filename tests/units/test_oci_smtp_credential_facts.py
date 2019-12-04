# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.module_utils.oracle import oci_utils
from ansible.modules.cloud.oracle import oci_smtp_credential_facts


try:
    import oci
    from oci.identity.models import SmtpCredential
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_smtp_credential_facts.py requires `oci` module")


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
    oci_smtp_credential_facts.set_logger(logging)


def test_list_smtp_credentials_list_all(identity_client, list_all_resources_patch):
    module = get_module(dict({"user_id": "ocid1.user.aaaa"}))
    list_all_resources_patch.return_value = get_smtp_credentials()
    result = oci_smtp_credential_facts.list_smtp_credentials(identity_client, module)
    assert len(result["smtp_credentials"]) is 2


def test_list_smtp_credentials_service_error(identity_client, list_all_resources_patch):
    error_message = "Internal Server Error"
    module = get_module(dict({"user_id": "ocid1.user.aaaa"}))
    identity_client.list_all_resources_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_smtp_credential_facts.list_smtp_credentials(identity_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def get_smtp_credentials():
    smtp_credentials = []
    smtp_credential1 = SmtpCredential()
    smtp_credential1.description = "test smtp credential one"
    smtp_credential2 = SmtpCredential()
    smtp_credential2.description = "test smtp credential one"
    smtp_credentials.append(smtp_credential1)
    smtp_credentials.append(smtp_credential2)
    return smtp_credentials


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = dict()
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
