# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_bucket_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.object_storage.models import BucketSummary
except ImportError:
    raise SkipTest("test_oci_bucket_facts.py requires `oci` module")


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
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


def test_list_buckets_success(object_storage_client, list_all_resources_patch):
    bucket_summaries = []
    bucket_summary_1 = BucketSummary()
    bucket_summary_1.name = "Bucket1"
    bucket_summary_2 = BucketSummary()
    bucket_summary_2.name = "Bucket2"
    bucket_summaries.append(bucket_summary_1)
    bucket_summaries.append(bucket_summary_2)
    list_all_resources_patch.return_value = bucket_summaries
    result = oci_bucket_facts.list_buckets(object_storage_client, get_module(), {}, {})
    assert "Bucket1" in result.__repr__()


def test_list_buckets_failure(object_storage_client):
    error_message = "You do not have authorization to perform this request,\
        or the requested resource could not be found."
    object_storage_client.list_buckets.side_effect = ServiceError(
        404, "NamespaceNotFound", dict(), error_message
    )
    try:
        oci_bucket_facts.list_buckets(object_storage_client, get_module(), {}, {})
    except Exception as ex:
        assert error_message in ex.args[0]


def test_list_buckets_failure_timeout_error(object_storage_client):
    error_message = "Maximum wait time has been exceeded."
    object_storage_client.list_buckets.side_effect = MaximumWaitTimeExceeded(
        error_message
    )
    try:
        oci_bucket_facts.list_buckets(object_storage_client, get_module(), {}, {})
    except Exception as ex:
        assert error_message in ex.args[0]


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module():
    params = {"namespace_name": "orapaas", "compartment_id": "test_compartment_axxd"}
    module = FakeModule(**params)
    return module
