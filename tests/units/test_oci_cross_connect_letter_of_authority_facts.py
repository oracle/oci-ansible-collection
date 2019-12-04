# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
from ansible.modules.cloud.oracle import oci_letter_of_authority_facts
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core.models import LetterOfAuthority
except ImportError:
    raise SkipTest("test_oci_letter_of_authority_facts.py requires `oci` module")


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
def virtual_network_client(mocker):
    mock_virtual_network_client = mocker.patch("oci.core.VirtualNetworkClient")
    return mock_virtual_network_client.return_value


def test_list_cross_connect_letter_of_authorities_all(virtual_network_client):
    module = get_module()
    letter_of_authority = get_letter_of_authority()
    virtual_network_client.get_cross_connect_letter_of_authority.return_value = get_response(
        200, None, letter_of_authority, None
    )
    result = oci_letter_of_authority_facts.list_letter_of_authorities(
        virtual_network_client, module
    )
    assert (
        result["letter_of_authorities"][0]["circuit_type"]
        == letter_of_authority.circuit_type
    )


def get_letter_of_authority():
    letter_of_authority = LetterOfAuthority()
    letter_of_authority.authorized_entity_name = "Example Authorized Entity Name"
    letter_of_authority.circuit_type = "Single_mode_LC"
    letter_of_authority.cross_connect_id = "ocid1.crossconnect..vfgc"
    letter_of_authority.facility_location = "Example Location"
    letter_of_authority.time_expires = "2018-03-03T06:55:49.463000+00:00"
    letter_of_authority.time_issued = "2018-02-03T06:55:49.463000+00:00"
    return letter_of_authority


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {"cross_connect_id": "ocid1.crossconnect..axsd"}
    if additional_properties is not None:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module
