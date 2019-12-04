# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_suppression
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.email.models import Suppression
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_suppression.py requires `oci` module")


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
def email_client(mocker):
    mock_email_client = mocker.patch("oci.email.email_client.EmailClient")
    return mock_email_client.return_value


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
    oci_suppression.set_logger(logging)


def test_create_suppression(email_client, create_resource_patch):
    module = get_module(dict(email_address="ansible@test.com"))
    suppression = get_suppression()
    create_resource_patch.return_value = {
        "suppression": to_dict(suppression),
        "changed": True,
    }
    result = oci_suppression.create_suppression(email_client, module)
    assert result["suppression"]["email_address"] is suppression.email_address


def test_delete_suppression(email_client, delete_and_wait_patch):
    module = get_module(dict({"suppression_id": "{ocid1.suppression..aa}"}))
    suppression = get_suppression()
    delete_and_wait_patch.return_value = dict(
        {"suppression": to_dict(suppression), "changed": True}
    )
    result = oci_suppression.delete_suppression(email_client, module)
    assert result["changed"] is True


def get_suppression():
    suppression = Suppression()
    suppression.email_address = "ansible@test.com"
    return suppression


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = {"compartment_id": "ocid1.compartment.oc1"}
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
