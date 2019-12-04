# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.module_utils import six
from ansible.module_utils.oracle import oci_utils
from ansible.modules.cloud.oracle import oci_app_catalog_subscription_facts

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import AppCatalogSubscription
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_app_catalog_subscription_facts.py requires `oci` module")


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


def get_app_catalog_subscription(**kwargs):
    app_catalog_subscription = AppCatalogSubscription(
        compartment_id="ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
        listing_id="ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx",
        listing_resource_version="1.0",
    )
    for attr, val in six.iteritems(kwargs):
        setattr(app_catalog_subscription, attr, val)
    return app_catalog_subscription


def get_app_catalog_subscriptions():
    return [
        get_app_catalog_subscription(
            compartment_id="ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            listing_id="ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx1",
            listing_resource_version="1.0",
        ),
        get_app_catalog_subscription(
            compartment_id="ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            listing_id="ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx2",
            listing_resource_version="1.0",
        ),
    ]


def get_module(**kwargs):
    params = {"compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx"}
    params.update(kwargs)
    module = FakeModule(**params)
    return module


def get_response(status=200, headers=None, data=None, request=None):
    if not headers:
        headers = dict()
    return oci.Response(status, headers, data, request)


def test_list_app_catalog_subscriptions_raises_service_error(
    compute_client, list_all_resources_patch
):
    list_all_resources_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), "Internal Server Error"
    )
    with pytest.raises(ServiceError) as exc_info:
        oci_app_catalog_subscription_facts.list_app_catalog_subscriptions(
            compute_client, get_module()
        )
    se = exc_info.value
    assert se.status == 500
    assert se.code == "InternalServerError"
    assert se.message == "Internal Server Error"


def test_list_app_catalog_subscriptions_when_no_subscriptions_exist(
    compute_client, list_all_resources_patch
):
    module = get_module()
    list_all_resources_patch.return_value = []
    result = oci_app_catalog_subscription_facts.list_app_catalog_subscriptions(
        compute_client, module
    )
    list_all_resources_patch.assert_called_once()
    list_all_resources_patch.assert_called_with(
        compute_client.list_app_catalog_subscriptions,
        compartment_id=module.params["compartment_id"],
    )
    assert len(result) == 0


def test_list_app_catalog_subscriptions_when_subscriptions_exist(
    compute_client, list_all_resources_patch
):
    module = get_module()
    app_catalog_subscriptions = get_app_catalog_subscriptions()
    list_all_resources_patch.return_value = app_catalog_subscriptions
    result = oci_app_catalog_subscription_facts.list_app_catalog_subscriptions(
        compute_client, module
    )
    list_all_resources_patch.assert_called_once()
    list_all_resources_patch.assert_called_with(
        compute_client.list_app_catalog_subscriptions,
        compartment_id=module.params["compartment_id"],
    )
    assert len(result) == 2


def test_list_app_catalog_subscriptions_filter_by_listing_id(
    compute_client, list_all_resources_patch
):
    listing_id = "ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx"
    module = get_module(listing_id=listing_id)
    app_catalog_subscription = get_app_catalog_subscription(listing_id=listing_id)
    list_all_resources_patch.return_value = [app_catalog_subscription]
    result = oci_app_catalog_subscription_facts.list_app_catalog_subscriptions(
        compute_client, module
    )
    assert len(result) == 1
    assert result[0]["compartment_id"] == app_catalog_subscription.compartment_id
    assert result[0]["listing_id"] == app_catalog_subscription.listing_id
    list_all_resources_patch.assert_called_with(
        compute_client.list_app_catalog_subscriptions,
        compartment_id=module.params["compartment_id"],
        listing_id=listing_id,
    )
