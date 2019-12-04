# Copyright (c) 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from ansible.module_utils.oracle import oci_common_utils


@pytest.fixture
def is_dict_subset_patch(mocker):
    return mocker.patch.object(oci_common_utils, "is_dict_subset")


@pytest.fixture
def is_list_subset_patch(mocker):
    return mocker.patch.object(oci_common_utils, "is_list_subset")


def test_is_dict_subset_when_source_or_target_are_None():
    assert oci_common_utils.is_dict_subset(None, None) is False
    assert oci_common_utils.is_dict_subset({}, None) is False
    assert oci_common_utils.is_dict_subset(None, {}) is False


def test_is_dict_subset_when_source_or_target_are_not_dicts():
    assert oci_common_utils.is_dict_subset([], {}) is False
    assert oci_common_utils.is_dict_subset([], []) is False
    assert oci_common_utils.is_dict_subset("testsourcestr", {}) is False
    assert oci_common_utils.is_dict_subset(1, {}) is False
    assert oci_common_utils.is_dict_subset(True, {}) is False
    assert oci_common_utils.is_dict_subset({}, "testtargetstr") is False
    assert oci_common_utils.is_dict_subset({}, 1) is False
    assert oci_common_utils.is_dict_subset({}, True) is False


def test_is_dict_subset_when_source_and_target_are_empty():
    assert oci_common_utils.is_dict_subset({}, {}) is True


def test_is_dict_subset_when_source_has_more_keys():
    s = {"key1": "val1"}
    t = {}
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1", "key2": "val2"}
    t = {"key1": "val1"}
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    t = {"key1": "val1", "key2": {"subkey1": "subval1"}}
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey3": "subval3"}}
    t = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    assert oci_common_utils.is_dict_subset(s, t) is True


def test_is_dict_subset_when_source_has_less_keys():
    s = {"key1": "val1"}
    t = {"key1": "val1", "key2": "val2"}
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1"}
    t = {"key1": "val1", "key2": "val2", "key3": "val3"}
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {}
    t = {"key1": "val1", "key2": "val2"}
    assert oci_common_utils.is_dict_subset(s, t) is True


def test_is_dict_subset_when_dicts_have_list_values():
    s = {"key1": "val1", "key2": ["item1", "item2", "item3"]}
    t = {"key1": "val1", "key2": ["item2", "item3"]}
    assert oci_common_utils.is_dict_subset(s, t) is False

    s = {"key1": "val1", "key2": ["item1", "item2", "item3"]}
    t = {"key1": "val1", "key2": ["item2", "item3", "item1"]}
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1", "key2": ["item1", "item2", "item3"]}
    t = {"key1": "val1", "key2": ["item1", "item2", "item3", "item4"]}
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {
        "compartment_id": "ocid1.compartment.oc1..xxxxxExamplexxx",
        "defined_tags": None,
        "display_name": "db_system_rt_872",
        "freeform_tags": None,
        "route_rules": [
            {
                "cidr_block": "0.0.0.0/0",
                "destination": None,
                "destination_type": None,
                "network_entity_id": "ocid1.internetgateway.oc1.iad.xxxxxExamplexxx",
            }
        ],
        "vcn_id": "ocid1.vcn.oc1.iad.xxxxxExamplexxx",
    }

    t = {
        "compartment_id": "ocid1.compartment.oc1..xxxxxExamplexxx",
        "defined_tags": {},
        "display_name": "db_system_rt_872",
        "freeform_tags": {},
        "id": "ocid1.routetable.oc1.iad.xxxxxExamplexxx",
        "lifecycle_state": "AVAILABLE",
        "route_rules": [
            {
                "cidr_block": "0.0.0.0/0",
                "destination": "0.0.0.0/0",
                "destination_type": "CIDR_BLOCK",
                "network_entity_id": "ocid1.internetgateway.oc1.iad.xxxxxExamplexxx",
            }
        ],
        "time_created": "2019-07-18T18:41:09.752000+00:00",
        "vcn_id": "ocid1.vcn.oc1.iad.xxxxxExamplexxx",
    }
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {
        "compartment_id": "ocid1.compartment.oc1..xxxxxExamplexxx",
        "defined_tags": None,
        "display_name": "db_system_rt_872",
        "freeform_tags": None,
        "route_rules": [
            {
                "cidr_block": "0.0.0.0/0",
                "destination": None,
                "destination_type": None,
                "network_entity_id": "ocid1.internetgateway.oc1.iad.xxxxxExamplexxx",
            }
        ],
        "vcn_id": "ocid1.vcn.oc1.iad.xxxxxExamplexxx",
    }

    t = {
        "compartment_id": "ocid1.compartment.oc1..xxxxxExamplexxx",
        "defined_tags": {},
        "display_name": "db_system_rt_872",
        "freeform_tags": {},
        "id": "ocid1.routetable.oc1.iad.xxxxxExamplexxx",
        "lifecycle_state": "AVAILABLE",
        "route_rules": [
            {
                "cidr_block": "0.0.0.0/0",
                "destination": "0.0.0.0/0",
                "destination_type": "CIDR_BLOCK",
                "network_entity_id": "ocid1.internetgateway.oc1.iad.xxxxxExamplexxx",
            },
            {
                "cidr_block": "1.2.3.4/16",
                "destination": "1.2.3.4/16",
                "destination_type": "CIDR_BLOCK",
                "network_entity_id": "ocid1.localpeeringgateway.oc1.iad.xxxxxExamplexxx",
            },
        ],
        "time_created": "2019-07-18T18:41:09.752000+00:00",
        "vcn_id": "ocid1.vcn.oc1.iad.xxxxxExamplexxx",
    }
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {
        "compartment_id": "ocid1.compartment.oc1..xxxxxExamplexxx",
        "defined_tags": None,
        "display_name": "db_system_rt_872",
        "freeform_tags": None,
        "route_rules": [
            {
                "cidr_block": "0.0.0.0/0",
                "destination": None,
                "destination_type": None,
                "network_entity_id": "ocid1.internetgateway.oc1.iad.xxxxxExamplexxx",
            },
            {
                "cidr_block": "1.2.3.4/16",
                "destination": "1.2.3.4/16",
                "destination_type": "CIDR_BLOCK",
                "network_entity_id": "ocid1.localpeeringgateway.oc1.iad.xxxxxExamplexxx",
            },
        ],
        "vcn_id": "ocid1.vcn.oc1.iad.xxxxxExamplexxx",
    }

    t = {
        "compartment_id": "ocid1.compartment.oc1..xxxxxExamplexxx",
        "defined_tags": {},
        "display_name": "db_system_rt_872",
        "freeform_tags": {},
        "id": "ocid1.routetable.oc1.iad.xxxxxExamplexxx",
        "lifecycle_state": "AVAILABLE",
        "route_rules": [
            {
                "cidr_block": "0.0.0.0/0",
                "destination": "0.0.0.0/0",
                "destination_type": "CIDR_BLOCK",
                "network_entity_id": "ocid1.internetgateway.oc1.iad.xxxxxExamplexxx",
            }
        ],
        "time_created": "2019-07-18T18:41:09.752000+00:00",
        "vcn_id": "ocid1.vcn.oc1.iad.xxxxxExamplexxx",
    }
    assert oci_common_utils.is_dict_subset(s, t) is False


def test_is_dict_subset_when_dicts_have_dict_values():
    s = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    t = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": "subval2"}}}
    t = {
        "key1": "val1",
        "key2": {"subkey1": {"subkey2": "subval2"}, "subkey3": {"subkey4": "subval4"}},
    }
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": {"subkey3": "subval3"}}}}
    t = {
        "key1": "val1",
        "key2": {"subkey1": {"subkey2": {"subkey3": "subval3", "subkey4": "subval4"}}},
    }
    assert oci_common_utils.is_dict_subset(s, t) is True

    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": "subval2"}}, "key3": {}}
    t = {
        "key1": "val1",
        "key2": {"subkey1": {"subkey2": "subval2"}, "subkey3": {"subkey4": "subval4"}},
    }
    assert oci_common_utils.is_dict_subset(s, t) is True


def test_is_dict_subset_returns_False_when_dicts_are_different():

    s = {"key1": "val1", "key2": "val2"}
    t = {"key1": "val1", "key2": "differentval2"}
    assert oci_common_utils.is_dict_subset(s, t) is False

    s = {"key1": "val1", "key2": "val2", "key3": {"subkey1": "subval1"}}
    t = {"key1": "val1", "key2": "val2", "key3": {"subkey1": "differentval1"}}
    assert oci_common_utils.is_dict_subset(s, t) is False

    s = {"key1": "val1", "key2": "val2", "key3": {"subkey1": True}}
    t = {"key1": "val1", "key2": "val2", "key3": {"subkey1": False}}
    assert oci_common_utils.is_dict_subset(s, t) is False

    s = {"key1": "val1", "key2": "val2", "key3": {"subkey1": 1}}
    t = {"key1": "val1", "key2": "val2", "key3": {"subkey1": "subval1"}}
    assert oci_common_utils.is_dict_subset(s, t) is False


def test_are_dicts_equal_when_source_or_target_are_None():
    assert oci_common_utils.are_dicts_equal(None, None) is False
    assert oci_common_utils.are_dicts_equal({}, None) is False
    assert oci_common_utils.are_dicts_equal(None, {}) is False


def test_are_dicts_equal_when_source_or_target_are_not_dicts():
    assert oci_common_utils.are_dicts_equal([], {}) is False
    assert oci_common_utils.are_dicts_equal([], []) is False
    assert oci_common_utils.are_dicts_equal("testsourcestr", {}) is False
    assert oci_common_utils.are_dicts_equal(1, {}) is False
    assert oci_common_utils.are_dicts_equal(True, {}) is False
    assert oci_common_utils.are_dicts_equal({}, "testtargetstr") is False
    assert oci_common_utils.are_dicts_equal({}, 1) is False
    assert oci_common_utils.are_dicts_equal({}, True) is False


def test_are_dicts_equal_when_source_and_target_are_empty():
    assert oci_common_utils.are_dicts_equal({}, {}) is True


def test_are_dicts_equal_when_source_has_more_keys():
    s = {"key1": "val1"}
    t = {}
    assert oci_common_utils.are_dicts_equal(s, t) is True

    s = {"key1": "val1", "key2": "val2"}
    t = {"key1": "val1"}
    assert oci_common_utils.are_dicts_equal(s, t) is True

    s = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    t = {"key1": "val1", "key2": {"subkey1": "subval1"}}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {
        "key1": "val1",
        "key2": {"subkey1": "subval1", "subkey3": "subval3"},
        "key3": "val3",
    }
    t = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    assert oci_common_utils.are_dicts_equal(s, t) is False


def test_are_dicts_equal_when_source_has_less_keys():
    s = {"key1": "val1"}
    t = {"key1": "val1", "key2": "val2"}
    assert oci_common_utils.are_dicts_equal(s, t) is True

    s = {"key1": "val1"}
    t = {"key1": "val1", "key2": "val2", "key3": "val3"}
    assert oci_common_utils.are_dicts_equal(s, t) is True

    s = {}
    t = {"key1": "val1", "key2": "val2"}
    assert oci_common_utils.are_dicts_equal(s, t) is False


def test_are_dicts_equal_when_source_subdicts_have_less_keys():
    s = {"key1": {"subkey1": "subval1"}}
    t = {"key1": {"subkey1": "subval1", "subkey2": "subval2"}}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": {"subkey1": {"subkey2": "subval2"}}}
    t = {"key1": {"subkey1": {"subkey2": "subval2", "subkey3": "subval3"}}}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": {"subkey1": {}}}
    t = {"key1": {"subkey1": {"subkey2": "subval2", "subkey3": "subval3"}}}
    assert oci_common_utils.are_dicts_equal(s, t) is False


def test_are_dicts_equal_when_source_subdicts_have_more_keys():
    s = {"key1": {"subkey1": "subval1", "subkey2": "subval2"}}
    t = {"key1": {"subkey1": "subval1"}}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": {"subkey1": {"subkey2": "subval2", "subkey3": "subval3"}}}
    t = {"key1": {"subkey1": {"subkey2": "subval2"}}}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": {"subkey1": {"subkey2": "subval2", "subkey3": "subval3"}}}
    t = {"key1": {"subkey1": {}}}
    assert oci_common_utils.are_dicts_equal(s, t) is False


def test_are_dicts_equal_when_dicts_have_list_values():
    s = {"key1": "val1", "key2": ["item1", "item2", "item3"]}
    t = {"key1": "val1", "key2": ["item2", "item3"]}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": "val1", "key2": ["item1", "item2", "item3"]}
    t = {"key1": "val1", "key2": ["item2", "item3", "item1"]}
    assert oci_common_utils.are_dicts_equal(s, t) is True

    s = {"key1": "val1", "key2": ["item1", "item2", "item3"]}
    t = {"key1": "val1", "key2": ["item1", "item2", "item3", "item4"]}
    assert oci_common_utils.are_dicts_equal(s, t) is False


def test_are_dicts_equal_when_dicts_have_dict_values():
    s = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    t = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    assert oci_common_utils.are_dicts_equal(s, t) is True

    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": "subval2"}}}
    t = {
        "key1": "val1",
        "key2": {"subkey1": {"subkey2": "subval2"}, "subkey3": {"subkey4": "subval4"}},
    }
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": "subval2"}}, "key3": {}}
    t = {
        "key1": "val1",
        "key2": {"subkey1": {"subkey2": "subval2"}, "subkey3": {"subkey4": "subval4"}},
    }
    assert oci_common_utils.are_dicts_equal(s, t) is False


def test_are_dicts_equal_when_dicts_have_different_values():
    s = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "subval2"}}
    t = {"key1": "val1", "key2": {"subkey1": "subval1", "subkey2": "differentsubval2"}}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": "subval2"}}}
    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": "differentsubval2"}}}
    assert oci_common_utils.are_dicts_equal(s, t) is False

    s = {"key1": "val1", "key2": {"subkey1": {"subkey2": "subval2"}}, "key3": {}}
    s = {
        "key1": "val1",
        "key2": {"subkey1": {"subkey2": "differentsubval2"}},
        "key3": {},
    }
    assert oci_common_utils.are_dicts_equal(s, t) is False


def test_is_in_list_when_element_is_primitive():
    empty_list = []
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bool_list = [True, False, True, True, False]
    str_list = ["testel1", "testel2", "testel3", "testel4", "testel5", "testel6"]
    list_with_nones = int_list + [None, None]

    assert oci_common_utils.is_in_list(empty_list, 1) is False
    assert oci_common_utils.is_in_list(empty_list, True) is False
    assert oci_common_utils.is_in_list(empty_list, "a") is False
    assert oci_common_utils.is_in_list(empty_list, None) is False

    assert oci_common_utils.is_in_list(int_list, 1) is True
    assert oci_common_utils.is_in_list(int_list, 9) is True
    assert oci_common_utils.is_in_list(int_list, -1) is False
    assert oci_common_utils.is_in_list(int_list, 100) is False

    assert oci_common_utils.is_in_list(bool_list, True) is True
    assert oci_common_utils.is_in_list(bool_list, False) is True

    assert oci_common_utils.is_in_list(str_list, "testel1") is True
    assert oci_common_utils.is_in_list(str_list, "testel3") is True
    assert oci_common_utils.is_in_list(str_list, "testel6") is True
    assert oci_common_utils.is_in_list(str_list, "nonexistentel1") is False
    assert oci_common_utils.is_in_list(str_list, "nonexistentel2") is False
    assert oci_common_utils.is_in_list(str_list, "nonexistentel3") is False

    assert oci_common_utils.is_in_list(list_with_nones, None) is True


def test_is_in_list_when_element_is_dict(is_dict_subset_patch):
    l = [{"testkey1": "testval1"}, {"testkey1": "testval2"}, {"testkey1": "testval3"}]
    is_dict_subset_patch.side_effect = [False, True, False]
    assert oci_common_utils.is_in_list(l, {"testkey1": "testval2"}) is True
    assert is_dict_subset_patch.call_count == 3

    is_dict_subset_patch.reset_mock()

    l = [
        {"testkey1": "testval1"},
        {"testkey1": "testval2", "testkey2": "testval3"},
        {"testkey1": "testval3"},
    ]
    is_dict_subset_patch.side_effect = [False, False, False]
    assert oci_common_utils.is_in_list(l, {"testkey2": "testval4"}) is False
    assert is_dict_subset_patch.call_count == 3

    is_dict_subset_patch.reset_mock()

    l = []
    is_dict_subset_patch.side_effect = []
    assert oci_common_utils.is_in_list(l, {"testkey2": "testval4"}) is False
    assert is_dict_subset_patch.call_count == 0


def test_is_in_list_when_element_is_list(is_list_subset_patch):
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    is_list_subset_patch.side_effect = [False, True, False]
    assert oci_common_utils.is_in_list(l, [4, 5, 6]) is True
    assert is_list_subset_patch.call_count == 3

    is_list_subset_patch.reset_mock()

    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    is_list_subset_patch.side_effect = [False, True, False]
    assert oci_common_utils.is_in_list(l, [4, 5]) is True
    assert is_list_subset_patch.call_count == 3

    is_list_subset_patch.reset_mock()

    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    is_list_subset_patch.side_effect = [False, False, False]
    assert oci_common_utils.is_in_list(l, [4, 5, 6, 7]) is False
    assert is_list_subset_patch.call_count == 3

    is_list_subset_patch.reset_mock()

    l = []
    is_list_subset_patch.side_effect = []
    assert oci_common_utils.is_in_list(l, [4, 5, 6]) is False
    assert is_list_subset_patch.call_count == 0


def test_merge_dicts():
    d1 = {"key1": "val1"}
    d2 = {"key2": "val2"}
    merged_dict = oci_common_utils.merge_dicts(d1, d2)
    assert "key1" in merged_dict
    assert "key2" in merged_dict
    assert merged_dict["key1"] == "val1"
    assert merged_dict["key2"] == "val2"

    complex_dict1 = {"complexkey1": {"subkey1": "subval1"}}
    complex_dict2 = {"complexkey2": {"subkey2": "subval2"}}
    merged_dict = oci_common_utils.merge_dicts(complex_dict1, complex_dict2)
    assert "complexkey1" in merged_dict
    assert "complexkey2" in merged_dict
    assert merged_dict["complexkey1"] == {"subkey1": "subval1"}
    assert merged_dict["complexkey2"] == {"subkey2": "subval2"}

    empty_dict = {}
    merged_dict = oci_common_utils.merge_dicts(d1, empty_dict)
    assert "key1" in merged_dict
    assert len(merged_dict) == 1

    none_dict = None
    merged_dict = oci_common_utils.merge_dicts(d1, none_dict)
    assert "key1" in merged_dict
    assert len(merged_dict) == 1
