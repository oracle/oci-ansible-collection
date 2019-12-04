# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.module_utils import six
from ansible.module_utils.oracle import oci_utils
from ansible.modules.cloud.oracle import oci_app_catalog_listing_agreement

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import AppCatalogListingResourceVersionAgreements
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_app_catalog_listing_agreement.py requires `oci` module")


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
def compute_client(mocker):
    mock_compute_client = mocker.patch("oci.core.compute_client.ComputeClient")
    return mock_compute_client.return_value


@pytest.fixture()
def call_with_backoff_patch(mocker):
    return mocker.patch.object(oci_utils, "call_with_backoff")


def get_app_catalog_listing_agreement(**kwargs):
    app_catalog_listing_agreement = AppCatalogListingResourceVersionAgreements(
        eula_link="http://test.eula.com",
        listing_id="ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx",
        listing_resource_version="1.0",
        oracle_terms_of_use_link="http://test.oracletermsofuse.com",
        signature="testsignature",
        time_retrieved="2019-02-13T12:21:11.053941+00:00",
    )
    for attr, val in six.iteritems(kwargs):
        setattr(app_catalog_listing_agreement, attr, val)
    return app_catalog_listing_agreement


def get_module(**kwargs):
    params = {
        "listing_id": "ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx",
        "resource_version": "1.0",
    }
    params.update(kwargs)
    module = FakeModule(**params)
    return module


def get_response(status=200, headers=None, data=None, request=None):
    if not headers:
        headers = dict()
    return oci.Response(status, headers, data, request)


def test_create_app_catalog_listing_agreement_raises_service_error(
    compute_client, call_with_backoff_patch
):
    call_with_backoff_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    with pytest.raises(ServiceError) as exc_info:
        oci_app_catalog_listing_agreement.create_app_catalog_listing_agreement(
            compute_client, get_module()
        )
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"


def test_create_app_catalog_listing_agreement(compute_client, call_with_backoff_patch):
    app_catalog_listing_agreement = get_app_catalog_listing_agreement()
    call_with_backoff_patch.return_value = get_response(
        data=app_catalog_listing_agreement
    )
    result = oci_app_catalog_listing_agreement.create_app_catalog_listing_agreement(
        compute_client, get_module()
    )
    assert result["changed"] is True
    assert (
        result["app_catalog_listing_agreement"]["eula_link"]
        == app_catalog_listing_agreement.eula_link
    )
    assert (
        result["app_catalog_listing_agreement"]["listing_id"]
        == app_catalog_listing_agreement.listing_id
    )
    assert (
        result["app_catalog_listing_agreement"]["listing_resource_version"]
        == app_catalog_listing_agreement.listing_resource_version
    )
    assert (
        result["app_catalog_listing_agreement"]["oracle_terms_of_use_link"]
        == app_catalog_listing_agreement.oracle_terms_of_use_link
    )
