# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_user
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.identity.models import User, Group, UserGroupMembership, UIPassword
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded, ClientError
except ImportError:
    raise SkipTest("test_oci_user.py requires `oci` module")


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
def get_ids_from_group_names(mocker):
    return mocker.patch.object(oci_user, "get_group_ids_from_group_names")


@pytest.fixture()
def add_user_to_groups(mocker):
    return mocker.patch.object(oci_user, "add_user_to_groups")


@pytest.fixture()
def create_or_reset_password(mocker):
    return mocker.patch.object(oci_user, "create_or_reset_password")


@pytest.fixture()
def update_user_description_and_tags(mocker):
    return mocker.patch.object(oci_user, "update_user_description_and_tags")


@pytest.fixture()
def modify_group_memberships(mocker):
    return mocker.patch.object(oci_user, "modify_group_memberships")


@pytest.fixture()
def reset_ui_password(mocker):
    return mocker.patch.object(oci_user, "reset_ui_password")


@pytest.fixture()
def unblock_user(mocker):
    return mocker.patch.object(oci_user, "unblock_user")


@pytest.fixture()
def get_memberships(mocker):
    return mocker.patch.object(oci_user, "get_group_ids_from_existing_memberships")


@pytest.fixture()
def update_group_memberships(mocker):
    return mocker.patch.object(oci_user, "update_group_memberships")


@pytest.fixture()
def delete_memberships(mocker):
    return mocker.patch.object(oci_user, "delete_all_group_memberships")


@pytest.fixture()
def delete_user_patch(mocker):
    return mocker.patch.object(oci_user, "delete_user")


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
def delete_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "delete_and_wait")


@pytest.fixture()
def create_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "create_and_wait")


def test_create_or_update_user_failure_service_error(
    identity_client, check_and_create_resource_patch
):
    error_message = "Internal Server Error"
    check_and_create_resource_patch.side_effect = ServiceError(
        500, "InternalServerError", dict(), error_message
    )
    try:
        oci_user.create_or_update_user(
            identity_client, get_module(dict({"compartment_id": "test_compartment"}))
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_user_failure_timeout_error(
    identity_client, check_and_create_resource_patch
):
    error_message = "Timeout Error"
    check_and_create_resource_patch.side_effect = MaximumWaitTimeExceeded(
        400, "TimeoutError", dict(), error_message
    )
    try:
        oci_user.create_or_update_user(
            identity_client, get_module(dict({"compartment_id": "test_compartment"}))
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_user_success(identity_client, create_and_wait_patch):
    user = get_user()
    create_and_wait_patch.return_value = dict({"user": to_dict(user), "changed": True})
    result = oci_user.create_user(
        identity_client,
        get_module(
            dict(
                {
                    "create_or_reset_ui_password": False,
                    "user_groups": None,
                    "compartment_id": "test_compartment",
                }
            )
        ),
    )
    assert result["user"]["name"] is user.name


def test_create_user_with_group_success(
    identity_client, get_ids_from_group_names, add_user_to_groups, create_and_wait_patch
):
    user = get_user()
    create_and_wait_patch.return_value = dict({"user": to_dict(user), "changed": True})
    get_ids_from_group_names.return_value = [
        "ocid1.group.oc1.asx",
        "ocid1.group.oc1.vfc",
    ]
    add_user_to_groups.return_value = None
    result = oci_user.create_user(
        identity_client,
        get_module(
            dict(
                {
                    "create_or_reset_ui_password": False,
                    "user_groups": ["admin", "network"],
                    "compartment_id": "test_compartment",
                }
            )
        ),
    )
    assert result["user"]["name"] is user.name


def test_create_user_with_password_success(
    identity_client, create_or_reset_password, create_and_wait_patch
):
    user = get_user()
    create_and_wait_patch.return_value = dict({"user": to_dict(user), "changed": True})
    create_or_reset_password.return_value = "asd_09g"
    result = oci_user.create_user(
        identity_client,
        get_module(
            dict(
                {
                    "create_or_reset_ui_password": True,
                    "user_groups": None,
                    "compartment_id": "test_compartment",
                }
            )
        ),
    )
    assert result["user"]["password"] is "asd_09g"


def test_create_user_with_password_failure(
    identity_client, create_or_reset_password, create_and_wait_patch, delete_user_patch
):
    error_message = "Error during password generation"
    user = get_user()
    create_and_wait_patch = dict({"user": to_dict(user), "changed": True})
    create_or_reset_password.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_user.create_user(
            identity_client,
            get_module(
                dict(
                    {
                        "create_or_reset_ui_password": True,
                        "user_groups": None,
                        "compartment_id": "test_compartment",
                    }
                )
            ),
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_user_with_group_failure_no_group_exists(
    identity_client,
    get_ids_from_group_names,
    add_user_to_groups,
    create_and_wait_patch,
    delete_user_patch,
):
    error_message = "No group named error_group exists"
    user = get_user()
    create_and_wait_patch.return_value = dict({"user": to_dict(user), "changed": True})
    delete_user_patch.return_value = None
    get_ids_from_group_names.side_effect = ClientError(error_message)
    add_user_to_groups.return_value = None
    try:
        oci_user.create_user(
            identity_client,
            get_module(
                dict(
                    {
                        "create_or_reset_ui_password": False,
                        "user_groups": ["admin", "network"],
                        "compartment_id": "test_compartment",
                    }
                )
            ),
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def test_update_user_success(
    identity_client,
    update_user_description_and_tags,
    modify_group_memberships,
    reset_ui_password,
    unblock_user,
):
    user = get_user()
    update_user_description_and_tags.return_value = to_dict(user), True
    modify_group_memberships.return_value = True
    reset_ui_password.return_value = "asd_09g", True
    unblock_user.return_value = user, True
    module = get_module(
        dict(
            {
                "create_or_reset_ui_password": True,
                "user_groups": ["admin", "network"],
                "blocked": "no",
                "compartment_id": "test_compartment",
            }
        )
    )
    changed, result = oci_user.update_user(identity_client, user, module)
    assert result["name"] is "ansible_user"


def test_unblock_user_unblocked(identity_client):
    user = get_user()
    identity_client.update_user_state.return_value = get_response(200, None, user, None)
    dummy, result = oci_user.unblock_user(identity_client, "no", user)
    assert result is True


def test_unblock_user_not_unblocked(identity_client):
    user = get_user()
    identity_client.update_user_state.return_value = user
    dummy, result = oci_user.unblock_user(identity_client, None, user)
    assert result is False


def test_reset_ui_password_changed(identity_client, create_or_reset_password):
    create_or_reset_password.return_value = "axd_v09"
    result, changed = oci_user.reset_ui_password(identity_client, get_user(), "always")
    assert changed is True
    assert result is "axd_v09"


def test_reset_ui_password_not_changed(identity_client):
    result, changed = oci_user.reset_ui_password(identity_client, get_user(), False)
    assert changed is False


def test_modify_group_memberships_group_updated(
    get_memberships, update_group_memberships
):
    get_memberships.return_value = ["ocid1.user.oc1..xdf", "ocid1.user.oc1..vgd"]
    update_group_memberships.return_value = True
    result = oci_user.modify_group_memberships(
        identity_client,
        ["test_group_1", "test_group_2"],
        get_user(),
        get_module(dict({"compartment_id": "test_compartment"})),
    )
    assert result is True


def test_modify_group_memberships_group_removed(get_memberships, delete_memberships):
    delete_memberships.return_value = True
    result = oci_user.modify_group_memberships(
        identity_client,
        [],
        get_user(),
        get_module(dict({"compartment_id": "test_compartment"})),
    )
    assert result is True


def test_modify_group_memberships_no_changes():
    result = oci_user.modify_group_memberships(
        identity_client,
        None,
        get_user(),
        get_module(dict({"compartment_id": "test_compartment"})),
    )
    assert result is False


def test_update_group_memberships_changed(identity_client, get_ids_from_group_names):
    existing_memberships_group_ids = ["ocid1.group.oc1..aaa"]
    get_ids_from_group_names.return_value = [
        "ocid1.group.oc1..aaa",
        "ocid1.group.oc1..xdv",
    ]
    result = oci_user.update_group_memberships(
        identity_client,
        "test_compartment",
        ["test_group_1", "test_group_2"],
        existing_memberships_group_ids,
        get_user().id,
        get_module(dict({"purge_group_memberships": False})),
    )
    assert result is True


def test_update_group_memberships_not_changed(
    identity_client, get_ids_from_group_names
):
    existing_memberships_group_ids = ["ocid1.group.oc1..aaa", "ocid1.group.oc1..xdv"]
    get_ids_from_group_names.return_value = [
        "ocid1.group.oc1..aaa",
        "ocid1.group.oc1..xdv",
    ]
    result = oci_user.update_group_memberships(
        identity_client,
        "test_compartment",
        ["test_group_1", "test_group_2"],
        existing_memberships_group_ids,
        get_user().id,
        get_module(dict({"purge_group_memberships": False})),
    )
    assert result is False


def test_update_group_memberships_purge(
    identity_client, get_ids_from_group_names, delete_memberships
):
    existing_memberships_group_ids = ["ocid1.group.oc1..aaa"]
    get_ids_from_group_names.return_value = ["ocid1.group.oc1..xdv"]
    delete_memberships.return_value = None
    result = oci_user.update_group_memberships(
        identity_client,
        "test_compartment",
        ["test_group_1"],
        existing_memberships_group_ids,
        get_user().id,
        get_module(dict({"purge_group_memberships": True})),
    )
    assert result is True


def test_update_group_memberships_no_purge(identity_client, get_ids_from_group_names):
    existing_memberships_group_ids = ["ocid1.group.oc1..aaa"]
    get_ids_from_group_names.return_value = ["ocid1.group.oc1..aaa"]
    result = oci_user.update_group_memberships(
        identity_client,
        "test_compartment",
        ["test_group_1"],
        existing_memberships_group_ids,
        get_user().id,
        get_module(dict({"purge_group_memberships": True})),
    )
    assert result is False


def test_get_group_ids_from_group_names_matched_name(
    identity_client, list_all_resources_patch
):
    group_one = create_group_object(
        "test_group_one", "ocid.test_group.1234xt2u", "Test Group One"
    )
    list_all_resources_patch.return_value = [group_one]
    result = oci_user.get_group_ids_from_group_names(
        identity_client,
        ["test_group_one"],
        get_module(dict({"compartment_id": "test_compartment"})),
    )
    assert result[0] is "ocid.test_group.1234xt2u"


def test_get_group_ids_from_group_names_no_matching_group_failure(
    identity_client, list_all_resources_patch
):
    error_message = "Group test_group_three does not exist"
    group_one = create_group_object(
        "test_group_one", "ocid.test_group.1234xt2u", "Test Group One"
    )
    list_all_resources_patch.return_value = [group_one]
    try:
        oci_user.get_group_ids_from_group_names(
            identity_client,
            ["test_group_three"],
            get_module(dict({"compartment_id": "test_compartment"})),
        )
    except Exception as ex:
        assert error_message in ex.args[0]


def test_delete_all_group_memberships_existing_memberships(
    identity_client, list_all_resources_patch
):
    user_group_membership_one = UserGroupMembership()
    user_group_membership_one.id = "ocid1.grp_mem.oc1.xdfs"
    user_group_membership_two = UserGroupMembership()
    user_group_membership_two.id = "ocid1.grp_mem.oc1.iues"
    existing_grp_mem = [user_group_membership_one, user_group_membership_two]
    list_all_resources_patch.return_value = existing_grp_mem
    identity_client.remove_user_from_group.return_value = None
    result = oci_user.delete_all_group_memberships(
        identity_client, "test_compartment", get_user()
    )
    assert result is True


def test_delete_all_group_memberships_no_memberships(
    identity_client, list_all_resources_patch
):
    list_all_resources_patch.return_value = []
    identity_client.remove_user_from_group.return_value = None
    result = oci_user.delete_all_group_memberships(
        identity_client, "test_compartment", get_user()
    )
    assert result is False


def test_add_user_to_groups(identity_client):
    identity_client.add_user_to_group.return_value = None
    oci_user.add_user_to_groups(
        identity_client, "ocid1.user.oc1..aaa", ["ocid1.group.oc1..xdv"]
    )


def test_get_group_ids_from_existing_memberships(
    identity_client, list_all_resources_patch
):
    user_group_membership_one = UserGroupMembership()
    user_group_membership_one.group_id = "ocid1.group.oc1.xdfs"
    list_all_resources_patch.return_value = [user_group_membership_one]
    result = oci_user.get_group_ids_from_existing_memberships(
        identity_client, "test_compartment", get_user().id
    )
    assert result[0] is "ocid1.group.oc1.xdfs"


def test_update_user_no_user_for_update(identity_client):
    error_message = "No User"
    module = get_module(dict(user_id="ocid1.user..xvdf"))
    try:
        oci_user.update_user(identity_client, None, module)
    except Exception as ex:
        assert error_message in str(ex.args)


def test_update_user_description_and_tags_description_changed(identity_client):
    module = get_module({"description": "Updated User"})
    user = get_user()
    identity_client.update_user.return_value = get_response(200, None, user, None)
    dummy, result = oci_user.update_user_description_and_tags(
        identity_client, user, module
    )
    assert result is True


def test_update_user_description_and_tags_description_not_changed(identity_client):
    module = get_module(dict())
    user = get_user()
    identity_client.update_user.return_value = get_response(200, None, user, None)
    dummy, result = oci_user.update_user_description_and_tags(
        identity_client, user, module
    )
    assert result is False


def test_update_user_description_and_tags_defined_tags_changed(identity_client):
    module = get_module({"defined_tags": {"organisation": {"org_type": "test"}}})
    user = get_user()
    identity_client.update_user.return_value = get_response(200, None, user, None)
    dummy, result = oci_user.update_user_description_and_tags(
        identity_client, user, module
    )
    assert result is True


def test_update_user_description_and_tags_defined_tags_not_changed(identity_client):
    module = get_module({"defined_tags": {"organisation": {"org_type": "dev"}}})
    user = get_user()
    identity_client.update_user.return_value = get_response(200, None, user, None)
    dummy, result = oci_user.update_user_description_and_tags(
        identity_client, user, module
    )
    assert result is False


def test_update_user_description_and_tags_freeform_tags_changed(identity_client):
    module = get_module({"freeform_tags": {"user_type": "tester"}})
    user = get_user()
    identity_client.update_user.return_value = get_response(200, None, user, None)
    dummy, result = oci_user.update_user_description_and_tags(
        identity_client, user, module
    )
    assert result is True


def test_update_user_description_and_tags_freeform_tags_not_changed(identity_client):
    module = get_module({"freeform_tags": {"user_type": "developer"}})
    user = get_user()
    identity_client.update_user.return_value = get_response(200, None, user, None)
    dummy, result = oci_user.update_user_description_and_tags(
        identity_client, user, module
    )
    assert result is False


def test_create_or_reset_password(identity_client):
    ui_password = UIPassword()
    ui_password.password = "asd_v09"
    identity_client.create_or_reset_ui_password.return_value = get_response(
        200, None, ui_password, None
    )
    result = oci_user.create_or_reset_password(identity_client, get_user().id)
    assert result is "asd_v09"


def test_delete_user_no_memberships(
    identity_client, get_existing_resource_patch, delete_and_wait_patch
):
    user = get_user()
    get_existing_resource_patch.return_value = user
    delete_and_wait_patch.return_value = {"user": to_dict(user), "changed": True}
    module = get_module(
        dict(
            {
                "force": False,
                "compartment_id": "ocid1.compartment..abuw",
                "user_id": "ocid1.user..abuw",
            }
        )
    )
    result = oci_user.delete_user(identity_client, module)
    assert result["changed"] is True


def test_delete_user_with_memberships_force_yes(
    identity_client,
    get_existing_resource_patch,
    delete_memberships,
    delete_and_wait_patch,
):
    user = get_user()
    get_existing_resource_patch.return_value = user
    delete_and_wait_patch.return_value = {"user": to_dict(user), "changed": True}
    delete_memberships.return_value = None
    module = get_module(
        dict(
            {
                "force": True,
                "compartment_id": "ocid1.compartment..abuw",
                "user_id": "ocid1.user..abuw",
            }
        )
    )
    result = oci_user.delete_user(identity_client, module)
    assert result["changed"] is True


def test_delete_user_with_memberships_force_no_failure(
    identity_client, get_existing_resource_patch, delete_memberships
):
    error_message = "User has group association"
    user = get_user()
    get_existing_resource_patch.return_value = user
    identity_client.delete_user.side_effect = ServiceError(
        400, "UserHasAssociation", dict(), error_message
    )
    module = get_module(
        dict(
            {
                "force": False,
                "compartment_id": "ocid1.compartment..abuw",
                "user_id": "ocid1.user..abuw",
            }
        )
    )
    try:
        oci_user.delete_user(identity_client, module)
    except Exception as ex:
        assert error_message is ex.args[0]


def create_group_object(name, id, description):
    group = Group()
    group.name = name
    group.id = id
    group.description = description
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
    user.defined_tags = {"organisation": {"org_type": "dev"}}
    user.freeform_tags = {"user_type": "developer"}
    return user


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = {"name": "ansible_use", "description": "Ansible User"}
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
