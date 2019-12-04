# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.module_utils import six
from ansible.module_utils.oracle import oci_utils, oci_date_utils
from ansible.modules.cloud.oracle import oci_app_catalog_subscription

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import AppCatalogSubscription
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_app_catalog_subscription.py requires `oci` module")


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


@pytest.fixture()
def get_app_catalog_subscription_patch(mocker):
    return mocker.patch.object(
        oci_app_catalog_subscription, "get_app_catalog_subscription"
    )


@pytest.fixture()
def parse_iso8601_str_as_datetime_patch(mocker):
    return mocker.patch.object(oci_date_utils, "parse_iso8601_str_as_datetime")


def get_app_catalog_subscription(**kwargs):
    app_catalog_subscription = AppCatalogSubscription(
        compartment_id="ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
        listing_id="ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx",
        listing_resource_version="1.0",
    )
    for attr, val in six.iteritems(kwargs):
        setattr(app_catalog_subscription, attr, val)
    return app_catalog_subscription


def get_module(**kwargs):
    params = {
        "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
        "listing_id": "ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx",
        "listing_resource_version": "1.0",
        "time_retrieved": "2019-02-15T19:11:33+00:00",
    }
    params.update(kwargs)
    module = FakeModule(**params)
    return module


def get_response(status=200, headers=None, data=None, request=None):
    if not headers:
        headers = dict()
    return oci.Response(status, headers, data, request)


def test_get_app_catalog_subscription_returns_existing_subscription(
    compute_client, list_all_resources_patch
):
    app_catalog_subscription = get_app_catalog_subscription()
    list_all_resources_patch.return_value = [app_catalog_subscription]
    existing_app_catalog_subscription = oci_app_catalog_subscription.get_app_catalog_subscription(
        compute_client, get_module()
    )
    list_all_resources_patch.assert_called_once()
    assert (
        existing_app_catalog_subscription["compartment_id"]
        == app_catalog_subscription.compartment_id
    )
    assert (
        existing_app_catalog_subscription["listing_id"]
        == app_catalog_subscription.listing_id
    )
    assert (
        existing_app_catalog_subscription["listing_resource_version"]
        == app_catalog_subscription.listing_resource_version
    )


def test_get_app_catalog_subscription_returns_None_if_subscription_does_not_exist(
    compute_client, list_all_resources_patch
):
    app_catalog_subscription = get_app_catalog_subscription()
    list_all_resources_patch.return_value = [app_catalog_subscription]
    get_app_catalog_subscription_return_value = oci_app_catalog_subscription.get_app_catalog_subscription(
        compute_client, get_module(listing_resource_version="2.0")
    )
    list_all_resources_patch.assert_called_once()
    assert get_app_catalog_subscription_return_value is None


def test_get_app_catalog_subscription_raises_service_error(
    compute_client, list_all_resources_patch
):
    list_all_resources_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    with pytest.raises(ServiceError) as exc_info:
        oci_app_catalog_subscription.get_app_catalog_subscription(
            compute_client, get_module()
        )
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"


def test_delete_app_catalog_subscription_raises_service_error(
    compute_client, list_all_resources_patch
):
    list_all_resources_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    with pytest.raises(ServiceError) as exc_info:
        oci_app_catalog_subscription.delete_app_catalog_subscription(
            compute_client, get_module()
        )
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"


def test_delete_app_catalog_subscription_when_resource_does_not_exist(
    compute_client, call_with_backoff_patch, get_app_catalog_subscription_patch
):
    # Ideally if a subscription does not exist, the get function returns None
    # and the call_with_backoff will not be called. Still test for completion.
    call_with_backoff_patch.side_effect = ServiceError(
        404, "NotAuthorizedOrNotFound", dict(), "Resource not found"
    )
    result = oci_app_catalog_subscription.delete_app_catalog_subscription(
        compute_client, get_module()
    )
    assert result["changed"] is False
    assert result["app_catalog_subscription"] == dict()
    # for the case when get_app_catalog_subscription returns None.
    get_app_catalog_subscription_patch.return_value = None
    # set this to make sure the exception is not from call_with_backoff
    call_with_backoff_patch.side_effect = None
    result = oci_app_catalog_subscription.delete_app_catalog_subscription(
        compute_client, get_module()
    )
    assert result["changed"] is False
    assert result["app_catalog_subscription"] == dict()


def test_delete_app_catalog_subscription_when_resource_exists(
    compute_client, call_with_backoff_patch, get_app_catalog_subscription_patch
):
    call_with_backoff_patch.return_value = get_response()
    app_catalog_subscription = get_app_catalog_subscription()
    get_app_catalog_subscription_patch.return_value = to_dict(app_catalog_subscription)
    result = oci_app_catalog_subscription.delete_app_catalog_subscription(
        compute_client, get_module()
    )
    assert result["changed"] is True
    assert (
        result["app_catalog_subscription"]["compartment_id"]
        == app_catalog_subscription.compartment_id
    )
    assert (
        result["app_catalog_subscription"]["listing_id"]
        == app_catalog_subscription.listing_id
    )
    assert (
        result["app_catalog_subscription"]["listing_resource_version"]
        == app_catalog_subscription.listing_resource_version
    )


def test_create_app_catalog_subscription_raises_service_error(
    compute_client, call_with_backoff_patch, get_app_catalog_subscription_patch
):
    # Places when a ServiceError can be raised are get_app_catalog_subscription or call_with_backoff. Test both.
    # Test when call_with_backoff raises ServiceError
    get_app_catalog_subscription_patch.return_value = None
    call_with_backoff_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    with pytest.raises(ServiceError) as exc_info:
        oci_app_catalog_subscription.create_app_catalog_subscription(
            compute_client, get_module()
        )
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"

    # Test when get_app_catalog_subscription raises ServiceError
    get_app_catalog_subscription_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    # set call_with_backoff_patch side effect to None to make sure that the exception is not raised from call_with_backoff
    call_with_backoff_patch.side_effect = None
    with pytest.raises(ServiceError) as exc_info:
        oci_app_catalog_subscription.create_app_catalog_subscription(
            compute_client, get_module()
        )
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"


def test_create_app_catalog_subscription_when_resource_does_not_exist_already(
    compute_client,
    call_with_backoff_patch,
    get_app_catalog_subscription_patch,
    parse_iso8601_str_as_datetime_patch,
):
    app_catalog_subscription = get_app_catalog_subscription()
    get_app_catalog_subscription_patch.side_effect = [
        None,
        to_dict(app_catalog_subscription),
    ]
    module = get_module()
    parse_iso8601_str_as_datetime_patch.return_value = module.params.get(
        "time_retrieved"
    )
    call_with_backoff_patch.return_value = get_response(data=app_catalog_subscription)
    result = oci_app_catalog_subscription.create_app_catalog_subscription(
        compute_client, module
    )
    assert get_app_catalog_subscription_patch.call_count == 2
    assert parse_iso8601_str_as_datetime_patch.call_count == 1
    parse_iso8601_str_as_datetime_patch.assert_called_with(
        module.params.get("time_retrieved")
    )
    assert result["changed"] is True
    assert (
        result["app_catalog_subscription"]["compartment_id"]
        == app_catalog_subscription.compartment_id
    )
    assert (
        result["app_catalog_subscription"]["listing_id"]
        == app_catalog_subscription.listing_id
    )
    assert (
        result["app_catalog_subscription"]["listing_resource_version"]
        == app_catalog_subscription.listing_resource_version
    )


def test_create_app_catalog_subscription_when_resource_exists_already(
    compute_client,
    call_with_backoff_patch,
    get_app_catalog_subscription_patch,
    parse_iso8601_str_as_datetime_patch,
):
    app_catalog_subscription = get_app_catalog_subscription()
    get_app_catalog_subscription_patch.return_value = to_dict(app_catalog_subscription)
    call_with_backoff_patch.return_value = get_response()
    result = oci_app_catalog_subscription.create_app_catalog_subscription(
        compute_client, get_module()
    )
    assert get_app_catalog_subscription_patch.call_count == 1
    assert parse_iso8601_str_as_datetime_patch.call_count == 0
    assert call_with_backoff_patch.call_count == 0
    assert result["changed"] is False
    assert (
        result["app_catalog_subscription"]["compartment_id"]
        == app_catalog_subscription.compartment_id
    )
    assert (
        result["app_catalog_subscription"]["listing_id"]
        == app_catalog_subscription.listing_id
    )
    assert (
        result["app_catalog_subscription"]["listing_resource_version"]
        == app_catalog_subscription.listing_resource_version
    )
