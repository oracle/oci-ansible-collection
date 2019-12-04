# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.module_utils import six
from ansible.module_utils.oracle import oci_utils
from ansible.modules.cloud.oracle import oci_identity_provider_facts

try:
    import oci
    from oci.util import to_dict
    from oci.identity.models import Saml2IdentityProvider
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_identity_provider_facts.py requires `oci` module")


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


@pytest.fixture()
def call_with_backoff_patch(mocker):
    return mocker.patch.object(oci_utils, "call_with_backoff")


def get_identity_provider(**kwargs):
    identity_provider = Saml2IdentityProvider(
        id="ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxx"
    )
    for attr, val in six.iteritems(kwargs):
        setattr(identity_provider, attr, val)
    return identity_provider


def get_identity_providers():
    return [
        get_identity_provider(
            id="ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxx1", protocol="SAML2"
        ),
        get_identity_provider(
            id="ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxx2", protocol="SAML2"
        ),
    ]


def get_module(**kwargs):
    params = {}
    params.update(kwargs)
    module = FakeModule(**params)
    return module


def get_response(status=200, headers=None, data=None, request=None):
    if not headers:
        headers = dict()
    return oci.Response(status, headers, data, request)


def test_get_identity_provider_raises_service_error(
    identity_client, call_with_backoff_patch
):
    call_with_backoff_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    with pytest.raises(ServiceError) as exc_info:
        oci_identity_provider_facts.get_identity_provider(identity_client, get_module())
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"


def test_get_identity_provider(identity_client, call_with_backoff_patch):
    identity_provider = get_identity_provider()
    call_with_backoff_patch.return_value = get_response(data=identity_provider)
    result = oci_identity_provider_facts.get_identity_provider(
        identity_client, get_module()
    )
    assert len(result) == 1
    call_with_backoff_patch.assert_called_once()
    assert result[0]["id"] == identity_provider.id


def test_list_identity_providers_raises_service_error(
    identity_client, list_all_resources_patch
):
    list_all_resources_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    with pytest.raises(ServiceError) as exc_info:
        oci_identity_provider_facts.list_identity_providers(
            identity_client, get_module()
        )
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"


def test_list_identity_providers_when_no_identity_providers_exist(
    identity_client, list_all_resources_patch
):
    list_all_resources_patch.return_value = []
    result = oci_identity_provider_facts.list_identity_providers(
        identity_client, get_module()
    )
    assert len(result) == 0


def test_list_identity_providers_when_identity_providers_exist(
    identity_client, list_all_resources_patch
):
    identity_providers = get_identity_providers()
    list_all_resources_patch.return_value = identity_providers
    result = oci_identity_provider_facts.list_identity_providers(
        identity_client, get_module()
    )
    assert len(result) == 2
    assert list_all_resources_patch.call_count == 1


def test_list_identity_providers_filter_by_name(
    identity_client, list_all_resources_patch
):
    module = get_module(
        name="testidentityprovider",
        protocol="SAML2",
        compartment_id="ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx",
    )
    list_all_resources_patch.return_value = [
        get_identity_provider(name="testidentityprovider")
    ]
    result = oci_identity_provider_facts.list_identity_providers(
        identity_client, module
    )
    assert len(result) == 1
    list_all_resources_patch.assert_called_with(
        identity_client.list_identity_providers,
        protocol="SAML2",
        compartment_id="ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx",
        name="testidentityprovider",
    )
