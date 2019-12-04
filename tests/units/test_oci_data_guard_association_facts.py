# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_data_guard_association_facts
from ansible.module_utils.oracle import oci_utils


try:
    import oci
    from oci.database.models import DataGuardAssociationSummary
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_data_guard_association_facts.py requires `oci` module")


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
def db_client(mocker):
    mock_db_client = mocker.patch("oci.database.database_client.DatabaseClient")
    return mock_db_client.return_value


@pytest.fixture()
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, "list_all_resources")


def setUpModule():
    logging.basicConfig(
        filename="/tmp/oci_ansible_module.log", filemode="a", level=logging.INFO
    )
    oci_data_guard_association_facts.set_logger(logging)


def test_list_data_guard_associations_all(db_client, list_all_resources_patch):
    module = get_module(dict({"database_id": "ocid1.database.aaaa"}))
    list_all_resources_patch.return_value = get_data_guard_associations()
    result = oci_data_guard_association_facts.list_data_guard_associations(
        db_client, module
    )
    assert len(result["data_guard_associations"]) is 2


def test_list_data_guard_associations_specific(db_client):
    module = get_module(
        dict(
            {
                "database_id": "ocid1.database.aaaa",
                "data_guard_association_id": "ocid1.dataguardassociation.aaaa",
            }
        )
    )
    db_client.get_data_guard_association.return_value = get_response(
        200, None, get_data_guard_association(), None
    )
    result = oci_data_guard_association_facts.list_data_guard_associations(
        db_client, module
    )
    assert result["data_guard_associations"][0]["role"] is "PRIMARY"


def test_list_data_guard_associations_service_error(
    db_client, list_all_resources_patch
):
    error_message = "Internal Server Error"
    module = get_module(dict({"database_id": "ocid1.database.aaaa"}))
    list_all_resources_patch.side_effect = ServiceError(
        499, "InternalServerError", dict(), error_message
    )
    try:
        oci_data_guard_association_facts.list_data_guard_associations(db_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def get_data_guard_associations():
    data_guard_associations = []
    data_guard_association1 = DataGuardAssociationSummary()
    data_guard_association1.role = "PRIMARY"
    data_guard_association2 = DataGuardAssociationSummary()
    data_guard_association2.role = "STANDBY"
    data_guard_associations.append(data_guard_association1)
    data_guard_associations.append(data_guard_association2)
    return data_guard_associations


def get_data_guard_association():
    data_guard_association = DataGuardAssociationSummary()
    data_guard_association.role = "PRIMARY"
    return data_guard_association


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = dict()
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
