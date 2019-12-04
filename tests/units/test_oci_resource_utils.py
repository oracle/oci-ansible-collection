# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from nose.plugins.skip import SkipTest
from ansible.module_utils.oracle import oci_resource_utils

try:
    import oci
    from oci.util import to_dict
    from oci.object_storage.models import PreauthenticatedRequest
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_resource_utils.py requires `oci` module")

EXAMPLE_COMPARTMENT_ID = "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx"
EXAMPLE_AD = "IxGV:US-ASHBURN-AD-1"


def test_convert_input_data_to_model_class():
    data = {"availability_domain": EXAMPLE_AD, "compartment_id": EXAMPLE_COMPARTMENT_ID}

    model = oci_resource_utils.convert_input_data_to_model_class(
        data, oci.core.models.LaunchInstanceDetails
    )
    assert isinstance(model, oci.core.models.LaunchInstanceDetails)
    assert model.availability_domain == EXAMPLE_AD
    assert model.compartment_id == EXAMPLE_COMPARTMENT_ID


def test_convert_input_data_to_model_class_nested_input_type():
    vnic_display_name = "my_vnic"
    subnet_id = "ocid1.subnet.oc1..xxxxxEXAMPLExxxxx"

    data = {
        "availability_domain": EXAMPLE_AD,
        "compartment_id": EXAMPLE_COMPARTMENT_ID,
        "create_vnic_details": {
            "display_name": vnic_display_name,
            "subnet_id": subnet_id,
        },
    }

    model = oci_resource_utils.convert_input_data_to_model_class(
        data, oci.core.models.LaunchInstanceDetails
    )
    assert isinstance(model, oci.core.models.LaunchInstanceDetails)
    assert model.availability_domain == EXAMPLE_AD
    assert model.compartment_id == EXAMPLE_COMPARTMENT_ID
    assert model.create_vnic_details.display_name == vnic_display_name
    assert model.create_vnic_details.subnet_id == subnet_id


def test_convert_input_data_to_model_class_preserve_casing_of_user_supplied_dictionary():
    metadata_key1 = "my_MetdataKey1"
    metadata_key2 = "my_metadata_key_2"
    metadata_value1 = "value_1"
    metadata_value2 = "value_2"

    data = {
        "availability_domain": EXAMPLE_AD,
        "compartment_id": EXAMPLE_COMPARTMENT_ID,
        "metadata": {metadata_key1: metadata_value1, metadata_key2: metadata_value2},
    }

    model = oci_resource_utils.convert_input_data_to_model_class(
        data, oci.core.models.LaunchInstanceDetails
    )
    assert isinstance(model, oci.core.models.LaunchInstanceDetails)
    assert model.availability_domain == EXAMPLE_AD
    assert model.compartment_id == EXAMPLE_COMPARTMENT_ID
    assert len(model.metadata) == 2
    assert model.metadata[metadata_key1] == metadata_value1
    assert model.metadata[metadata_key2] == metadata_value2


def test_convert_input_data_to_model_class_nested_list_type():
    vcn_id = "ocid1.vcn.oc1..xxxxxEXAMPLExxxxx"
    cidr_block1 = "10.0.0.1/16"
    destination_type1 = "CIDR_BLOCK"
    cidr_block2 = "10.0.0.1/24"
    destination_type2 = "SERVICE_CIDR_BLOCK"

    data = {
        "vcn_id": vcn_id,
        "compartment_id": EXAMPLE_COMPARTMENT_ID,
        "route_rules": [
            {"cidr_block": cidr_block1, "destination_type": destination_type1},
            {"cidr_block": cidr_block2, "destination_type": destination_type2},
        ],
    }

    model = oci_resource_utils.convert_input_data_to_model_class(
        data, oci.core.models.CreateRouteTableDetails
    )
    assert isinstance(model, oci.core.models.CreateRouteTableDetails)
    assert model.vcn_id == vcn_id
    assert model.compartment_id == EXAMPLE_COMPARTMENT_ID
    assert len(model.route_rules) == 2
    assert model.route_rules[0].cidr_block == cidr_block1
    assert model.route_rules[0].destination_type == destination_type1
    assert model.route_rules[1].cidr_block == cidr_block2
    assert model.route_rules[1].destination_type == destination_type2


def test_convert_input_data_to_model_class_nested_dict_type():
    display_name = "my_load_balancer"
    private_key1 = "private_key1"
    public_certificate1 = "public_certificate1"
    private_key2 = "private_key2"
    public_certificate2 = "public_certificate2"

    data = {
        "display_name": display_name,
        "compartment_id": EXAMPLE_COMPARTMENT_ID,
        "certificates": {
            "certificate_1": {
                "private_key": private_key1,
                "public_certificate": public_certificate1,
            },
            "certificate_2": {
                "private_key": private_key2,
                "public_certificate": public_certificate2,
            },
        },
    }

    model = oci_resource_utils.convert_input_data_to_model_class(
        data, oci.load_balancer.models.CreateLoadBalancerDetails
    )
    assert isinstance(model, oci.load_balancer.models.CreateLoadBalancerDetails)
    assert model.display_name == display_name
    assert model.compartment_id == EXAMPLE_COMPARTMENT_ID
    assert len(model.certificates) == 2
    assert model.certificates["certificate_1"].private_key == private_key1
    assert model.certificates["certificate_1"].public_certificate == public_certificate1
    assert model.certificates["certificate_2"].private_key == private_key2
    assert model.certificates["certificate_2"].public_certificate == public_certificate2


def test_convert_input_data_to_model_class_polymorphic_input_type():
    source_type = "image"
    image_id = "ocid1.image.oc1..xxxxxEXAMPLExxxxx"
    data = {"source_type": source_type, "image_id": image_id}

    model = oci_resource_utils.convert_input_data_to_model_class(
        data, oci.core.models.InstanceSourceDetails
    )
    assert isinstance(model, oci.core.models.InstanceSourceViaImageDetails)
    assert model.image_id == image_id
    assert model.source_type == source_type


def test_convert_input_data_to_model_class_polymorphic_input_type_ignore_fields_that_dont_match_discriminator_value():
    source_type = "image"
    image_id = "ocid1.image.oc1..xxxxxEXAMPLExxxxx"
    boot_volume_id = "ocid1.bootvolume.oc1..xxxxxEXAMPLExxxxx"
    data = {
        "source_type": source_type,
        "image_id": image_id,
        "boot_volume_id": boot_volume_id,
    }

    # expect boot_volume_id is ignored because it does not exist on InstanceSourceViaImageDetails which is
    # the type that corresponds to sourceType = image
    model = oci_resource_utils.convert_input_data_to_model_class(
        data, oci.core.models.InstanceSourceDetails
    )
    assert isinstance(model, oci.core.models.InstanceSourceViaImageDetails)
    assert model.image_id == image_id
    assert model.source_type == source_type
