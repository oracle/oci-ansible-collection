# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_bucket
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.object_storage.models import (
        Bucket,
        ListObjects,
        ObjectSummary,
        PreauthenticatedRequestSummary,
    )
    from oci.exceptions import ServiceError
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
def object_storage_client(mocker):
    mock_ob_store = mocker.patch(
        "oci.object_storage.object_storage_client.ObjectStorageClient"
    )
    return mock_ob_store.return_value


@pytest.fixture()
def get_existing_bucket_patch(mocker):
    return mocker.patch.object(oci_bucket, "get_existing_bucket")


@pytest.fixture()
def delete_all_objects_in_bucket_patch(mocker):
    return mocker.patch.object(oci_bucket, "delete_all_objects_in_bucket")


@pytest.fixture()
def delete_all_pars_of_bucket_patch(mocker):
    return mocker.patch.object(oci_bucket, "delete_all_pars_of_bucket")


@pytest.fixture()
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_bucket.set_logger(logging)


def test_bucket_details_factory_create_bucket():
    bucket_details = oci_bucket.bucket_details_factory("create", get_module())
    assert "Standard" in bucket_details.storage_tier
    assert "testbucket" in bucket_details.name


def test_bucket_details_factory_update_bucket():
    bucket_details = oci_bucket.bucket_details_factory("update", get_module())
    # Update operation has to storage_tier option
    assert "storage_tier" not in bucket_details.attribute_map
    assert "testbucket" in bucket_details.name


def test_create_or_update_bucket_create_success(
    object_storage_client, get_existing_bucket_patch
):
    get_existing_bucket_patch.return_value = None
    bucket = oci.object_storage.models.Bucket()
    bucket.name = "myBucket"
    object_storage_client.create_bucket.return_value = get_response(
        200, None, bucket, None
    )
    result = oci_bucket.create_or_update_bucket(object_storage_client, get_module())
    bucket = result["bucket"]
    assert "myBucket" in bucket["name"]


def test_create_or_update_bucket_update_success(
    object_storage_client, get_existing_bucket_patch
):
    existing_bucket = oci.object_storage.models.Bucket()
    existing_bucket.name = "myBucket"
    existing_bucket.metadata = {"project": "test_project"}
    get_existing_bucket_patch.return_value = existing_bucket
    updated_bucket = oci.object_storage.models.Bucket()
    updated_bucket.name = "myBucket"
    updated_bucket.metadata = {"project": "prod_project"}
    object_storage_client.update_bucket.return_value = get_response(
        200, None, updated_bucket, None
    )
    result = oci_bucket.create_or_update_bucket(object_storage_client, get_module())
    bucket = result["bucket"]
    assert "prod_project" in bucket["metadata"]["project"]


def test_create_or_update_bucket_no_update(
    object_storage_client, get_existing_bucket_patch
):
    existing_bucket = oci.object_storage.models.Bucket()
    existing_bucket.name = "testbucket"
    existing_bucket.metadata = {"org": "oracle"}
    existing_bucket.public_access_type = "NoPublicAccess"
    get_existing_bucket_patch.return_value = existing_bucket
    result = oci_bucket.create_or_update_bucket(object_storage_client, get_module())
    assert result["changed"] is False


def test_get_exisiting_bucket_failure_service_error(object_storage_client):
    error_message = "Namespace does not exist"
    object_storage_client.get_bucket.side_effect = ServiceError(
        500, "NoNameSpaceExists", dict(), error_message
    )
    try:
        oci_bucket.get_existing_bucket(object_storage_client, get_module())
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_bucket_create_bucket_service_error(
    object_storage_client, get_existing_bucket_patch
):
    get_existing_bucket_patch.return_value = None
    error_message = "Namespace does not exist."
    object_storage_client.create_bucket.side_effect = ServiceError(
        400, "NoNameSpaceExists", dict(), error_message
    )
    module = get_module()
    try:
        oci_bucket.create_or_update_bucket(object_storage_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_or_update_bucket_update_bucket_service_error(
    object_storage_client, get_existing_bucket_patch
):
    get_existing_bucket_patch.return_value = oci.object_storage.models.Bucket()
    error_message = "Namespace does not exist."
    object_storage_client.update_bucket.side_effect = ServiceError(
        400, "NoNameSpaceExists", dict(), error_message
    )
    object_storage_client.get_bucket.return_value = Bucket()
    module = get_module()
    try:
        oci_bucket.create_or_update_bucket(object_storage_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_bucket_success(object_storage_client):
    bucket = oci.object_storage.models.Bucket()
    bucket.name = "myBucket"
    object_storage_client.create_bucket.return_value = get_response(
        200, None, bucket, None
    )
    response = oci_bucket.create_bucket(object_storage_client, get_module())
    bucket = str(response.data)
    assert "myBucket" in bucket


def test_update_bucket_success(object_storage_client):
    bucket = oci.object_storage.models.Bucket()
    bucket.name = "updatedBucket"
    object_storage_client.update_bucket.return_value = get_response(
        200, None, bucket, None
    )
    response = oci_bucket.update_bucket(object_storage_client, get_module())
    bucket = str(response.data)
    assert "updatedBucket" in bucket


def test_delete_bucket_success(object_storage_client, get_existing_bucket_patch):
    existing_bucket = oci.object_storage.models.Bucket()
    existing_bucket.name = "existingBucket"
    get_existing_bucket_patch.return_value = existing_bucket
    object_storage_client.delete_bucket.return_value = get_response(
        200, None, None, None
    )
    result = oci_bucket.delete_bucket(object_storage_client, get_module())
    assert result["changed"] is True
    assert result["bucket"]["name"] is "existingBucket"


def test_delete_bucket_success_with_force(
    object_storage_client,
    get_existing_bucket_patch,
    delete_all_objects_in_bucket_patch,
    delete_all_pars_of_bucket_patch,
):
    module = get_module()
    module.params.update({"force": True})
    existing_bucket = oci.object_storage.models.Bucket()
    existing_bucket.name = "existingBucket"
    get_existing_bucket_patch.return_value = existing_bucket
    object_storage_client.delete_bucket.return_value = get_response(
        200, None, None, None
    )
    result = oci_bucket.delete_bucket(object_storage_client, module)
    assert result["changed"] is True
    assert result["bucket"]["name"] is "existingBucket"


def test_delete_bucket_no_state_changed(
    object_storage_client, get_existing_bucket_patch
):
    get_existing_bucket_patch.return_value = None
    result = oci_bucket.delete_bucket(object_storage_client, get_module())
    assert result["changed"] is False


def test_delete_bucket_service_error(object_storage_client):
    error_message = "Bucket Exists but not deleted due to other error"
    object_storage_client.delete_bucket.side_effect = ServiceError(
        400, "OtherError", dict(), error_message
    )
    try:
        oci_bucket.delete_bucket(object_storage_client, get_module())
    except Exception as e:
        assert error_message in e.args[0]


def test_delete_all_objects_in_bucket(object_storage_client, list_all_resources_patch):
    list_objects = ListObjects()
    object_summary = ObjectSummary()
    object_summary.name = "test_object"
    list_objects.objects = [object_summary]
    list_all_resources_patch.return_value = list_objects
    oci_bucket.delete_all_objects_in_bucket(
        object_storage_client, "test_namespace", "test_bucket"
    )
    assert object_storage_client.delete_object.called


def test_delete_all_pars_of_bucket(object_storage_client, list_all_resources_patch):
    preauthenticated_request_summary = PreauthenticatedRequestSummary()
    preauthenticated_request_summary.name = "test_par"
    list_all_resources_patch.return_value = [preauthenticated_request_summary]
    oci_bucket.delete_all_pars_of_bucket(
        object_storage_client, "test_namespace", "test_bucket"
    )
    assert object_storage_client.delete_preauthenticated_request.called


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module():
    params = {
        "name": "testbucket",
        "namespace_name": "orapaas",
        "compartment_id": "test_compartment_axxd",
        "public_access_type": "NoPublicAccess",
        "metadata": {"org": "oracle"},
        "storage_tier": "Standard",
        "kms_key_id": None,
        "force": False,
    }
    module = FakeModule(**params)
    return module
