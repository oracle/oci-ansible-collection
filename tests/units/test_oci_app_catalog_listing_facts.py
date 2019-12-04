# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.module_utils import six
from ansible.module_utils.oracle import oci_utils
from ansible.modules.cloud.oracle import oci_app_catalog_listing_facts

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import AppCatalogListing
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_app_catalog_listing_facts.py requires `oci` module")


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
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


@pytest.fixture()
def call_with_backoff_patch(mocker):
    return mocker.patch.object(oci_utils, "call_with_backoff")


def get_app_catalog_listing(**kwargs):
    app_catalog_listing = AppCatalogListing(
        listing_id="ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx"
    )
    for attr, val in six.iteritems(kwargs):
        setattr(app_catalog_listing, attr, val)
    return app_catalog_listing


def get_app_catalog_listings():
    return [
        get_app_catalog_listing(
            listing_id="ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx1",
            display_name="listing1",
        ),
        get_app_catalog_listing(
            listing_id="ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx2",
            display_name="listing2",
        ),
    ]


def get_module(**kwargs):
    params = {"listing_id": "ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx"}
    params.update(kwargs)
    module = FakeModule(**params)
    return module


def get_response(status=200, headers=None, data=None, request=None):
    if not headers:
        headers = dict()
    return oci.Response(status, headers, data, request)


def test_get_app_catalog_listing_raises_service_error(
    compute_client, call_with_backoff_patch
):
    call_with_backoff_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    with pytest.raises(ServiceError) as exc_info:
        oci_app_catalog_listing_facts.get_app_catalog_listing(
            compute_client, get_module()
        )
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"


def test_get_app_catalog_listing(compute_client, call_with_backoff_patch):
    app_catalog_listing = get_app_catalog_listing()
    call_with_backoff_patch.return_value = get_response(data=app_catalog_listing)
    result = oci_app_catalog_listing_facts.get_app_catalog_listing(
        compute_client, get_module()
    )
    assert len(result) == 1
    call_with_backoff_patch.assert_called_once()
    assert result[0]["listing_id"] == app_catalog_listing.listing_id


def test_list_app_catalog_listings_raises_service_error(
    compute_client, list_all_resources_patch
):
    list_all_resources_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    with pytest.raises(ServiceError) as exc_info:
        oci_app_catalog_listing_facts.list_app_catalog_listings(
            compute_client, get_module()
        )
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"


def test_list_app_catalog_listings_when_no_listings_exist(
    compute_client, list_all_resources_patch
):
    list_all_resources_patch.return_value = []
    result = oci_app_catalog_listing_facts.list_app_catalog_listings(
        compute_client, get_module()
    )
    assert len(result) == 0


def test_list_app_catalog_listings_when_listings_exist(
    compute_client, list_all_resources_patch, call_with_backoff_patch
):
    app_catalog_listings = get_app_catalog_listings()
    list_all_resources_patch.return_value = app_catalog_listings
    call_with_backoff_patch.side_effect = [
        get_response(data=app_catalog_listing)
        for app_catalog_listing in app_catalog_listings
    ]
    result = oci_app_catalog_listing_facts.list_app_catalog_listings(
        compute_client, get_module()
    )
    assert len(result) == 2
    assert list_all_resources_patch.call_count == 1
    assert call_with_backoff_patch.call_count == 2


def test_list_app_catalog_listings_filter_by_display_name(
    compute_client, list_all_resources_patch
):
    display_name = "testlisting"
    module = get_module(display_name=display_name)
    app_catalog_listing = get_app_catalog_listing(display_name=display_name)
    list_all_resources_patch.return_value = [app_catalog_listing]
    result = oci_app_catalog_listing_facts.list_app_catalog_listings(
        compute_client, module
    )
    assert len(result) == 1
    list_all_resources_patch.assert_called_with(
        compute_client.list_app_catalog_listings, display_name=display_name
    )
