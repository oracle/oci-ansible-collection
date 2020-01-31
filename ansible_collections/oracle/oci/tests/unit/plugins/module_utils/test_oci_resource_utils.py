# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
import pytest
from ansible_collections.oracle.oci.plugins.module_utils import oci_resource_utils
from . import test_custom_helpers


@pytest.fixture
def custom_helper_mapping_fixture(mocker):
    mocker.patch.dict(
        oci_resource_utils.custom_helper_mapping,
        {"ResourceHelperCustom": test_custom_helpers.ResourceHelperCustom},
    )


def test_get_custom_class_mapping_returns_correct_custom_class_mapping():
    custom_helper_mapping = oci_resource_utils.get_custom_class_mapping(
        [test_custom_helpers]
    )
    assert "ResourceHelperCustom" in custom_helper_mapping
    assert (
        test_custom_helpers.ResourceHelperCustom
        == custom_helper_mapping["ResourceHelperCustom"]
    )


def test_get_custom_class_returns_correct_custom_class(custom_helper_mapping_fixture):
    custom_class = oci_resource_utils.get_custom_class("ResourceHelperCustom")
    assert custom_class == test_custom_helpers.ResourceHelperCustom


def test_get_custom_class_returns_default_custom_class_if_not_exists(
    custom_helper_mapping_fixture,
):
    custom_class = oci_resource_utils.get_custom_class(
        "NonExistentResourceHelperCustom"
    )
    assert custom_class == oci_resource_utils.DefaultHelperCustom
