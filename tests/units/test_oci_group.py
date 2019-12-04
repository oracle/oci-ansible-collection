# Copyright (c) 2017, 2018, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_group
from ansible.module_utils.oracle import oci_utils


try:
    import oci
    from oci.identity.models import Group, UserGroupMembership, User
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
except ImportError:
    raise SkipTest("test_oci_group.py requires `oci` module")


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
def oci_wait_until_patch(mocker):
    return mocker.patch.object(oci, "wait_until")


@pytest.fixture()
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


@pytest.fixture()
def get_existing_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "get_existing_resource")


@pytest.fixture()
def check_and_create_resource_patch(mocker):
    return mocker.patch.object(oci_utils, "check_and_create_resource")


@pytest.fixture()
def update_group_description_and_tags_patch(mocker):
    return mocker.patch.object(oci_group, "update_group_description_and_tags")


@pytest.fixture()
def get_existing_group_members_patch(mocker):
    return mocker.patch.object(oci_group, "get_existing_group_members")


def test_create_or_update_group_create_success(
    mocker,
    identity_client,
    check_and_create_resource_patch,
    get_existing_resource_patch,
):
    group = create_group_object()
    get_existing_resource_patch.return_value = None
    check_and_create_resource_patch.return_value = create_group_object()
    result = oci_group.create_or_update_group(
        identity_client, get_module({"compartment_id": "test_compartment"})
    )
    assert result.id is group.id


def test_create_or_update_group_failure_service_error(
    mocker, identity_client, check_and_create_resource_patch
):
    error_message = "Failed to create group"
    check_and_create_resource_patch.side_effect = ServiceError(
        400, "GroupNotEmpty", dict(), error_message
    )
    try:
        oci_group.create_or_update_group(
            identity_client, get_module({"compartment_id": "test_compartment"})
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_group_failure_timeout_error(
    mocker, identity_client, check_and_create_resource_patch
):
    error_message = "Failed to create group due to timeout"
    check_and_create_resource_patch.side_effect = MaximumWaitTimeExceeded(
        400, "GroupNotEmpty", dict(), error_message
    )
    try:
        oci_group.create_or_update_group(
            identity_client, get_module({"compartment_id": "test_compartment"})
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_group_update_success(
    mocker, identity_client, get_existing_resource_patch
):
    group = create_group_object()
    get_existing_resource_patch.return_value = group
    mock_update_group = mocker.patch.object(oci_group, "update_group")
    mock_update_group.return_value = True, create_group_object()
    result = oci_group.create_or_update_group(
        identity_client,
        get_module({"compartment_id": "test_compartment", "group_id": "test_group_id"}),
    )
    assert result["group"].id is group.id


def test_create_group_without_user_success(identity_client, oci_wait_until_patch):
    additional_properties = dict(
        {"state": "present", "users": None, "compartment_id": "test_compartment"}
    )
    module = get_module(additional_properties)
    group = create_group_object()
    identity_client.create_group.return_value = get_response(200, None, group, None)
    identity_client.get_group.return_value = get_response(200, None, group, None)
    result = oci_group.create_group(identity_client, module)
    assert result["group"]["id"] is group.id


def test_create_group_with_user_success(mocker, identity_client, oci_wait_until_patch):
    additional_properties = dict(
        {
            "state": "present",
            "users": ["test_user1"],
            "compartment_id": "test_compartment",
        }
    )
    m1 = mocker.patch.object(oci_group, "get_user_ids_from_user_names")
    m2 = mocker.patch.object(oci_group, "add_users_to_group")
    module = get_module(additional_properties)
    group = create_group_object()
    identity_client.create_group.return_value = get_response(200, None, group, None)
    identity_client.get_group.return_value = get_response(200, None, group, None)
    result = oci_group.create_group(identity_client, module)
    assert m1.called
    assert m2.called
    assert result["group"]["id"] is group.id


def test_update_group_no_group_for_update(identity_client):
    error_message = "No Group"
    module = get_module(dict(group_id="ocid1.group..xvdf"))
    try:
        oci_group.update_group(identity_client, None, module)
    except Exception as ex:
        assert error_message in str(ex.args)


def test_update_for_group_description_changed_success(
    mocker, identity_client, update_group_description_and_tags_patch
):
    additional_properties = dict(
        {"state": "present", "users": None, "compartment_id": "test_compartment"}
    )
    module = get_module(additional_properties)
    group = create_group_object()
    update_group_description_and_tags_patch.return_value = group, True
    changed, dummy = oci_group.update_group(identity_client, group, module)
    assert update_group_description_and_tags_patch.called
    assert changed is True


def test_update_user_changed_success(
    mocker,
    identity_client,
    oci_wait_until_patch,
    update_group_description_and_tags_patch,
    get_existing_group_members_patch,
):
    additional_properties = dict({"state": "present", "users": ["test_user"]})
    mock_update_members = mocker.patch.object(oci_group, "update_group_users")
    module = get_module(additional_properties)
    group = create_group_object()
    update_group_description_and_tags_patch.return_value = group, False
    mock_update_members.return_value = True
    changed, dummy = oci_group.update_group(identity_client, group, module)
    assert mock_update_members.called
    assert changed is True


def test_add_users_to_group_success(identity_client):
    user_ids = ["ocid1.testuser1..xszc"]
    identity_client.add_user_to_group.return_value = None
    oci_group.add_users_to_group(identity_client, create_group_object().id, user_ids)
    assert identity_client.add_user_to_group.called


def test_update_user_changed_no_user_success(
    mocker,
    identity_client,
    oci_wait_until_patch,
    update_group_description_and_tags_patch,
    get_existing_group_members_patch,
):
    additional_properties = dict({"state": "present", "users": []})
    mock_delete_user = mocker.patch.object(oci_group, "delete_all_users_from_group")
    module = get_module(additional_properties)
    group = create_group_object()
    update_group_description_and_tags_patch.return_value = group, False
    mock_delete_user.return_value = True
    changed, dummy = oci_group.update_group(identity_client, group, module)
    assert mock_delete_user.called
    assert changed is True


def test_update_group_description_and_tags_description_changed(identity_client):
    group = create_group_object()
    identity_client.update_group.return_value = get_response(200, None, group, None)
    dummy, changed = oci_group.update_group_description_and_tags(
        identity_client, group, get_module(dict({"description": "Production Group"}))
    )
    assert changed is True


def test_update_group_description_and_tags_description_not_changed(identity_client):
    group = create_group_object()
    identity_client.update_group.return_value = get_response(200, None, group, None)
    dummy, changed = oci_group.update_group_description_and_tags(
        identity_client, group, get_module(dict({"description": "Test Group"}))
    )
    assert changed is False


def test_update_group_description_and_tags_defined_tags_changed(identity_client):
    group = create_group_object()
    identity_client.update_group.return_value = get_response(200, None, group, None)
    dummy, changed = oci_group.update_group_description_and_tags(
        identity_client,
        group,
        get_module(
            dict({"defined_tags": {"organisation": {"division": "engineering"}}})
        ),
    )
    assert changed is True


def test_update_group_description_and_tags_defined_tags_not_changed(identity_client):
    group = create_group_object()
    identity_client.update_group.return_value = get_response(200, None, group, None)
    dummy, changed = oci_group.update_group_description_and_tags(
        identity_client,
        group,
        get_module(dict({"defined_tags": {"organisation": {"division": "finance"}}})),
    )
    assert changed is False


def test_update_group_description_and_tags_freeform_tags_changed(identity_client):
    group = create_group_object()
    identity_client.update_group.return_value = get_response(200, None, group, None)
    dummy, changed = oci_group.update_group_description_and_tags(
        identity_client,
        group,
        get_module(dict({"freeform_tags": {"member_type": "developer"}})),
    )
    assert changed is True


def test_update_group_description_and_tags_freeform_tags_not_changed(identity_client):
    group = create_group_object()
    identity_client.update_group.return_value = get_response(200, None, group, None)
    dummy, changed = oci_group.update_group_description_and_tags(
        identity_client,
        group,
        get_module(dict({"freeform_tags": {"member_type": "CA"}})),
    )
    assert changed is False


def test_update_group_users_new_user_success(mocker, identity_client):
    dditional_properties = dict({"purge_user_memberships": False})
    user_ids = dict({"ocid1.testuser1": "test_user1", "ocid1.testuser2": "test_user2"})
    mock_get_user_ids_from_user_names = mocker.patch.object(
        oci_group, "get_user_ids_from_user_names"
    )
    mock_get_user_ids_from_user_names.return_value = user_ids
    mock_add_users_to_group = mocker.patch.object(oci_group, "add_users_to_group")
    existing_group_members = ["ocid1.testuser1"]
    changed = oci_group.update_group_users(
        identity_client,
        "test_compartment",
        None,
        existing_group_members,
        create_group_object(),
        get_module(dditional_properties),
    )

    assert mock_add_users_to_group.called
    assert changed is True


def test_update_group_users_no_update(mocker, identity_client):
    additional_properties = dict({"purge_user_memberships": False})
    user_ids = dict({"ocid1.testuser1": "test_user1", "ocid1.testuser2": "test_user2"})
    mock_get_user_ids_from_user_names = mocker.patch.object(
        oci_group, "get_user_ids_from_user_names"
    )
    mock_get_user_ids_from_user_names.return_value = user_ids
    existing_group_members = ["ocid1.testuser1", "ocid1.testuser2"]
    changed = oci_group.update_group_users(
        identity_client,
        "test_compartment",
        None,
        existing_group_members,
        create_group_object(),
        get_module(additional_properties),
    )

    assert changed is False


def test_update_group_users_purge_members(mocker, identity_client):
    additional_properties = dict({"purge_user_memberships": True})
    user_ids = dict({"ocid1.testuser1": "test_user1"})
    mock_get_user_ids_from_user_names = mocker.patch.object(
        oci_group, "get_user_ids_from_user_names"
    )
    mock_get_user_ids_from_user_names.return_value = user_ids
    mock_delete_all_users_from_the_group = mocker.patch.object(
        oci_group, "delete_all_users_from_group"
    )
    mock_add_users_to_group = mocker.patch.object(oci_group, "add_users_to_group")
    existing_group_members = ["ocid1.testuser1", "ocid1.testuser2"]
    changed = oci_group.update_group_users(
        identity_client,
        "test_compartment",
        None,
        existing_group_members,
        create_group_object(),
        get_module(additional_properties),
    )

    assert changed is True


def test_update_group_users_no_purge(mocker, identity_client):
    additional_properties = dict({"purge_user_memberships": True})
    user_ids = dict({"ocid1.testuser1": "test_user1"})
    mock_get_user_ids_from_user_names = mocker.patch.object(
        oci_group, "get_user_ids_from_user_names"
    )
    mock_get_user_ids_from_user_names.return_value = user_ids
    existing_group_members = ["ocid1.testuser1"]
    changed = oci_group.update_group_users(
        identity_client,
        None,
        "test_compartment",
        existing_group_members,
        create_group_object(),
        get_module(additional_properties),
    )

    assert changed is False


def test_get_user_ids_from_user_names_no_matching_user_failure(
    identity_client, list_all_resources_patch
):
    error_message = "User ansible_user_two does not exist"
    ansible_user = get_user()
    list_all_resources_patch.return_value = [ansible_user]
    try:
        oci_group.get_user_ids_from_user_names(
            identity_client, ["ansible_user", "ansible_user_two"], get_module(dict())
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def test_get_user_ids_from_user_names_matching_user(
    identity_client, list_all_resources_patch
):
    ansible_user = get_user()
    list_all_resources_patch.return_value = [ansible_user]
    result = oci_group.get_user_ids_from_user_names(
        identity_client,
        ["ansible_user"],
        get_module(dict({"compartment_id": "test_compartment"})),
    )
    assert result[0] is ansible_user.id


def test_delete_all_users_from_group_success(identity_client, list_all_resources_patch):
    user_group_membership = UserGroupMembership()
    user_group_membership.id = "usr_group_1"
    list_all_resources_patch.return_value = [user_group_membership]
    identity_client.remove_user_from_group.return_value = None
    changed = oci_group.delete_all_users_from_group(
        identity_client, "test_compartment", create_group_object()
    )
    assert identity_client.remove_user_from_group.called
    assert changed is True


def test_delete_all_users_from_group_no_change(
    identity_client, list_all_resources_patch
):
    list_all_resources_patch.return_value = []
    identity_client.remove_user_from_group.return_value = None
    changed = oci_group.delete_all_users_from_group(
        identity_client, "test_compartment", create_group_object()
    )
    assert changed is False


def test_get_existing_group_members_success(identity_client, list_all_resources_patch):
    user_group_membership = UserGroupMembership()
    user_group_membership.user_id = "test_user_1"
    existing_memberships = [user_group_membership]
    list_all_resources_patch.return_value = existing_memberships
    user_group_memberships = oci_group.get_existing_group_members(
        identity_client, "test_compartment", create_group_object().id
    )
    assert user_group_memberships[0] == "test_user_1"


def test_get_difference_from_existing_users_no_existing_users():
    existing_users = []
    given_users = ["test_user1"]
    result = oci_group.get_difference_from_existing_users(existing_users, given_users)
    assert "test_user1" in result


def test_get_difference_from_existing_users_one_common_user():
    existing_users = ["test_user1"]
    given_users = ["test_user1", "test_user2"]
    result = oci_group.get_difference_from_existing_users(existing_users, given_users)
    assert len(result) is 1
    assert "test_user2" in result


def test_get_difference_from_existing_users_no_difference():
    existing_users = ["test_user1"]
    given_users = ["test_user1"]
    result = oci_group.get_difference_from_existing_users(existing_users, given_users)
    assert not result


def test_delete_group_success_no_force(
    mocker, identity_client, get_existing_resource_patch
):
    additional_properties = dict(
        {"state": "absent", "force": "no", "compartment_id": "compartment_id"}
    )
    get_existing_resource_patch.return_value = create_group_object()
    identity_client.delete_group.return_value = None
    result = oci_group.delete_group(identity_client, get_module(additional_properties))
    assert result["changed"] is True


def test_delete_group_failure_no_force(
    mocker, identity_client, get_existing_resource_patch
):
    error_message = "The Group is not empty so can not be remoed"
    additional_properties = dict(
        {"state": "absent", "force": "no", "compartment_id": "compartment_id"}
    )
    get_existing_resource_patch.return_value = create_group_object()
    identity_client.delete_group.side_effect = ServiceError(
        400, "GroupNotEmpty", dict(), error_message
    )
    try:
        oci_group.delete_group(identity_client, get_module(additional_properties))
    except Exception as ex:
        assert error_message in ex.args[0]


def test_delete_group_success_force(
    mocker, identity_client, get_existing_resource_patch
):
    additional_properties = dict(
        {"state": "absent", "force": "no", "compartment_id": "compartment_id"}
    )
    mock_delete_all_users_from_group = mocker.patch.object(
        oci_group, "delete_all_users_from_group"
    )
    get_existing_resource_patch.return_value = create_group_object()
    mock_delete_all_users_from_group.return_value = None
    identity_client.delete_group.return_value = None
    result = oci_group.delete_group(identity_client, get_module(additional_properties))
    assert result["changed"] is True


def test_delete_group_failure_timeout_error(
    mocker, identity_client, get_existing_resource_patch
):
    error_message = "Group deletion failed due to timeout"
    additional_properties = dict(
        {"state": "absent", "force": "no", "compartment_id": "compartment_id"}
    )
    get_existing_resource_patch.return_value = create_group_object()
    identity_client.delete_group.side_effect = MaximumWaitTimeExceeded(
        400, "GroupNotEmpty", dict(), error_message
    )
    try:
        oci_group.delete_group(identity_client, get_module(additional_properties))
    except Exception as ex:
        assert error_message in ex.args[0]


def create_group_object():
    group = Group()
    group.name = "test_group"
    group.id = "ocid.test_group.1234xt2u"
    group.description = "Test Group"
    group.defined_tags = {"organisation": {"division": "finance"}}
    group.freeform_tags = {"member_type": "CA"}
    return group


def get_user():
    user = User()
    user.id = "ocid1.user.oc1..aaa"
    user.compartment_id = "ocidv1:tenancy:oc1:phx:1461"
    user.name = "ansible_user"
    user.description = "Ansible User"
    user.time_created = "2017-11-02T16:15:24.604000+00:00"
    user.lifecycle_state = "ACTIVE"
    user.inactive_status = "null"
    return user


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = {
        "name": "test_group",
        "description": "Test Group",
        "delete_user_memberships": False,
    }
    # if additional_properties:
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
