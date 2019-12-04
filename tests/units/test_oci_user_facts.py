# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_user_facts, oci_user
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.identity.models import User, Group, UserGroupMembership
    from oci.exceptions import ServiceError
    from oci.util import to_dict
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
def get_associated_groups(mocker):
    return mocker.patch.object(oci_user_facts, "get_associated_groups")


@pytest.fixture()
def get_group_ids_from_existing_memberships(mocker):
    return mocker.patch.object(
        oci_user_facts, "get_group_ids_from_existing_memberships"
    )


@pytest.fixture()
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


def test_list_users_failure_service_error(identity_client, list_all_resources_patch):
    error_message = "Internal Server Error"
    list_all_resources_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_user_facts.list_users(identity_client, get_module(dict()))
    except Exception as ex:
        assert error_message in ex.args[0]


def test_get_all_users(
    identity_client, get_associated_groups, list_all_resources_patch
):
    list_all_resources_patch.return_value = get_user_list()
    member_group_dict = dict({"compartment_id": "test_compartment"})
    member_group_dict["member_of_groups"] = [to_dict(get_group())]
    get_associated_groups.return_value = member_group_dict
    result = oci_user_facts.get_all_users(identity_client, "test_compartment")
    assert len(result) is 2


def test_get_associated_groups_success(
    identity_client, get_group_ids_from_existing_memberships
):
    group = get_group()
    existing_memberships_group_ids = ["ocid1.group.oc1.phx.xccdx8e"]
    get_group_ids_from_existing_memberships.return_value = (
        existing_memberships_group_ids
    )
    identity_client.get_group.return_value = get_response(200, None, group, None)
    result = oci_user_facts.get_associated_groups(
        identity_client, "test_compartment", "ocid1.user.oc1..xdvf"
    )
    assert result["member_of_groups"][0]["name"] is group.name


def test_get_associated_groups_ignore_non_existing_groups(
    identity_client, get_group_ids_from_existing_memberships
):
    group_two = get_group()
    group_two.name = "Group Two"
    existing_memberships_group_ids = [
        "ocid1.group.oc1.phx.xccdx8e",
        "ocid1.group.oc1.phx.axdfg",
    ]
    get_group_ids_from_existing_memberships.return_value = (
        existing_memberships_group_ids
    )
    identity_client.get_group.side_effect = [
        ServiceError(404, "NotFound", dict(), "Group not present"),
        get_response(200, None, group_two, None),
    ]
    result = oci_user_facts.get_associated_groups(
        identity_client, "test_compartment", "ocid1.user.oc1..xdvf"
    )
    assert result["member_of_groups"][0]["name"] is group_two.name


def test_get_associated_groups_raise_other_error(
    identity_client, get_group_ids_from_existing_memberships
):
    existing_memberships_group_ids = [
        "ocid1.group.oc1.phx.xccdx8e",
        "ocid1.group.oc1.phx.axdfg",
    ]
    get_group_ids_from_existing_memberships.return_value = (
        existing_memberships_group_ids
    )
    identity_client.get_group.side_effect = ServiceError(
        499, "InternalServerError", dict(), "Internal Server Error"
    )
    try:
        oci_user_facts.get_associated_groups(
            identity_client, "test_compartment", "ocid1.user.oc1..xdvf"
        )
    except ServiceError as ex:
        assert ex.message == "Internal Server Error"


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_user_list():
    user_one = User()
    user_one.id = "ocid1.user.oc1..aaa"
    user_one.compartment_id = "ocidv1:tenancy:oc1:phx:1461"
    user_one.name = "ansible_user_one"
    user_one.description = "Ansible User One"
    user_one.time_created = "2017-11-02T16:15:24.604000+00:00"
    user_one.lifecycle_state = "ACTIVE"
    user_one.inactive_status = "null"

    user_two = User()
    user_two.id = "ocid1.user.oc1..xvd"
    user_two.compartment_id = "ocidv1:tenancy:oc1:phx:1566"
    user_two.name = "ansible_user_two"
    user_one.description = "Ansible User Two"
    user_one.time_created = "2017-11-02T17:15:24.604000+00:00"
    user_one.lifecycle_state = "ACTIVE"
    user_one.inactive_status = "null"

    return [user_one, user_two]


def get_group():
    group = Group()
    group.compartment_id = "ocid1.tenancy.phx.xdfgyz"
    group.id = "ocid1.group.oc1.phx.xccdx8e"
    group.name = "group_1"
    group.description = "Test Group 1"
    group.time_created = "2016-04-21T21:38:46.625000+00:00"
    group.lifecycle_state = "ACTIVE"
    group.inactive_status = "null"
    return group


def get_module(additional_info):
    params = additional_info
    module = FakeModule(**params)
    return module
