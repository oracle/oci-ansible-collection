# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_group
from ansible.modules.cloud.oracle import oci_group_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.identity.models import Group, User
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
except ImportError:
    raise SkipTest("test_oci_bucket.py requires `oci` module")


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
def get_associated_users(mocker):
    return mocker.patch.object(oci_group_facts, "get_associated_users")


@pytest.fixture()
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


@pytest.fixture()
def get_existing_group_members(mocker):
    return mocker.patch.object(oci_group_facts, "get_existing_group_members")


def test_list_user_groups_failure_service_error(
    identity_client, list_all_resources_patch
):
    error_message = "Operation failed due to Internal Error"
    list_all_resources_patch.side_effect = ServiceError(
        499, "InternalError", dict(), error_message
    )
    try:
        oci_group_facts.list_user_groups(
            identity_client, get_module(dict({"name": None}))
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def test_list_user_groups_failure_timeout_error(
    identity_client, list_all_resources_patch
):
    error_message = "Failed to create group due to timeout"
    list_all_resources_patch.side_effect = MaximumWaitTimeExceeded(
        400, "TimeOutError", dict(), error_message
    )
    try:
        oci_group_facts.list_user_groups(
            identity_client, get_module(dict({"name": None}))
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def test_get_all_groups(
    identity_client, list_all_resources_patch, get_associated_users
):
    list_all_resources_patch.return_value = get_group_list()
    get_associated_users.return_value = to_dict(get_user())
    result = oci_group_facts.get_all_groups(identity_client, "ocid1.tenancy.phx.xdfgyz")
    assert len(result) is 2


def test_get_associated_users(identity_client, get_existing_group_members):
    group_ids = ["ocid1.group.oc1.phx.xccdx8e", "ocid1.group.oc1.phx.xpssf5r"]
    get_existing_group_members.return_value = group_ids
    identity_client.get_user.return_value = get_response(200, None, get_user(), None)
    result = oci_group_facts.get_associated_users(
        identity_client, "ocid1.tenancy.phx.xdfgyz", "ocid1.group.oc1.phx.xccdx8e"
    )
    for member in result["members"]:
        assert member["name"] is "test_user"


def test_get_associated_users_pass_ignore_non_existing_user(
    identity_client, get_existing_group_members
):
    group_ids = ["ocid1.group.oc1.phx.xccdx8e", "ocid1.group.oc1.phx.xpssf5r"]
    get_existing_group_members.return_value = group_ids
    identity_client.get_user.side_effect = (
        ServiceError(404, "NotFound", dict(), "User not present"),
        get_response(200, None, get_user(), None),
    )
    result = oci_group_facts.get_associated_users(
        identity_client, "ocid1.tenancy.phx.xdfgyz", "ocid1.group.oc1.phx.xccdx8e"
    )
    for member in result["members"]:
        assert member["name"] is "test_user"


def test_get_associated_users_raise_service_error(
    identity_client, get_existing_group_members
):
    group_ids = ["ocid1.group.oc1.phx.xccdx8e", "ocid1.group.oc1.phx.xpssf5r"]
    get_existing_group_members.return_value = group_ids
    identity_client.get_user.side_effect = ServiceError(
        499, "InternalServerError", dict(), "Internal Server Error"
    )
    try:
        result = oci_group_facts.get_associated_users(
            identity_client, "ocid1.tenancy.phx.xdfgyz", "ocid1.group.oc1.phx.xccdx8e"
        )
    except ServiceError as ex:
        assert ex.status == 499


def get_group_list():
    group1 = Group()
    group1.compartment_id = "ocid1.tenancy.phx.xdfgyz"
    group1.id = "ocid1.group.oc1.phx.xccdx8e"
    group1.name = "group_1"
    group1.description = "Test Group 1"
    group1.time_created = "2016-04-21T21:38:46.625000+00:00"
    group1.lifecycle_state = "ACTIVE"
    group1.inactive_status = "null"

    group2 = Group()
    group2.compartment_id = "ocid1.tenancy.phx.xdfgyz"
    group2.id = "ocid1.group.oc1.phx.xpssf5r"
    group2.name = "group_2"
    group2.description = "Test Group 2"
    group2.time_created = "2016-04-19T21:38:46.625000+00:00"
    group2.lifecycle_state = "ACTIVE"
    group2.inactive_status = "null"

    group_list = []
    group_list.append(group1)
    group_list.append(group2)

    return group_list


def get_user():
    user = User()
    user.id = "ocid1.user.oc1..aaaaaaaa45ko"
    user.compartment_id = "ocidv1:tenancy:oc1:phx:1461274"
    user.name = "test_user"
    user.description = "Test User"
    user.time_created = "2017-03-22T04:26:34.830000+00:00"
    user.lifecycle_state = "ACTIVE"
    user.inactive_status = "null"
    return user


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = additional_properties
    module = FakeModule(**params)
    return module
