#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_rover_cluster_actions
short_description: Perform actions on a RoverCluster resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a RoverCluster resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a cluster into a different compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    rover_cluster_id:
        description:
            - Unique RoverCluster identifier
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID],https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the resources should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the RoverCluster.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on rover_cluster
  oci_rover_cluster_actions:
    # required
    rover_cluster_id: "ocid1.rovercluster.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
rover_cluster:
    description:
        - Details of the RoverCluster resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of RoverCluster.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the RoverCluster.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        cluster_size:
            description:
                - Size of the cluster.
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - The time the the RoverCluster was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the RoverCluster.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_state_details:
            description:
                - A property that can contain details on the lifecycle.
            returned: on success
            type: str
            sample: lifecycle_state_details_example
        customer_shipping_address:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                addressee:
                    description:
                        - Addressee in shipping address.
                    returned: on success
                    type: str
                    sample: addressee_example
                care_of:
                    description:
                        - CareOf for shipping address.
                    returned: on success
                    type: str
                    sample: care_of_example
                address1:
                    description:
                        - Address line 1.
                    returned: on success
                    type: str
                    sample: address1_example
                address2:
                    description:
                        - Address line 2.
                    returned: on success
                    type: str
                    sample: address2_example
                address3:
                    description:
                        - Address line 3.
                    returned: on success
                    type: str
                    sample: address3_example
                address4:
                    description:
                        - Address line 4.
                    returned: on success
                    type: str
                    sample: address4_example
                city_or_locality:
                    description:
                        - city or locality for shipping address.
                    returned: on success
                    type: str
                    sample: city_or_locality_example
                state_or_region:
                    description:
                        - state or region for shipping address.
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                zipcode:
                    description:
                        - zipcode for shipping address.
                    returned: on success
                    type: str
                    sample: zipcode_example
                country:
                    description:
                        - country for shipping address.
                    returned: on success
                    type: str
                    sample: country_example
                phone_number:
                    description:
                        - recepient phone number.
                    returned: on success
                    type: str
                    sample: phone_number_example
                email:
                    description:
                        - recepient email address.
                    returned: on success
                    type: str
                    sample: email_example
        nodes:
            description:
                - The summary of nodes that are part of this cluster.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The OCID of the RoverNode.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                compartment_id:
                    description:
                        - The OCID of the compartment containing the RoverNode.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                cluster_id:
                    description:
                        - The cluster ID if the node is part of a cluster.
                    returned: on success
                    type: str
                    sample: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
                serial_number:
                    description:
                        - Serial number of the node.
                    returned: on success
                    type: str
                    sample: serial_number_example
                node_type:
                    description:
                        - The type of node indicating if it belongs to a cluster
                    returned: on success
                    type: str
                    sample: STANDALONE
                shape:
                    description:
                        - The shape of the node.
                    returned: on success
                    type: str
                    sample: shape_example
                display_name:
                    description:
                        - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: display_name_example
                time_created:
                    description:
                        - The time the the RoverNode was created. An RFC3339 formatted datetime string
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                lifecycle_state:
                    description:
                        - The current state of the RoverNode.
                    returned: on success
                    type: str
                    sample: CREATING
                lifecycle_state_details:
                    description:
                        - A property that can contain details on the lifecycle.
                    returned: on success
                    type: str
                    sample: lifecycle_state_details_example
                freeform_tags:
                    description:
                        - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                          predefined name, type, or namespace. For more information, see L(Resource
                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                          Example: `{\\"Department\\": \\"Finance\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                defined_tags:
                    description:
                        - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                          For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                          Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                    returned: on success
                    type: dict
                    sample: {'Operations': {'CostCenter': 'US'}}
                system_tags:
                    description:
                        - "The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is
                          predefined and scoped to namespaces.
                          For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                          Example: `{orcl-cloud: {free-tier-retain: true}}`"
                    returned: on success
                    type: dict
                    sample: {}
        enclosure_type:
            description:
                - The type of enclosure rover nodes in this cluster are shipped in.
            returned: on success
            type: str
            sample: RUGGADIZED
        time_customer_received:
            description:
                - Time when customer received the cluster.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_customer_returned:
            description:
                - Time when customer returned the cluster.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        delivery_tracking_info:
            description:
                - Tracking information for device shipping.
            returned: on success
            type: str
            sample: delivery_tracking_info_example
        cluster_workloads:
            description:
                - List of existing workloads that should be provisioned on the nodes.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Name of the Rover Workload
                    returned: on success
                    type: str
                    sample: name_example
                compartment_id:
                    description:
                        - The OCID of the compartment containing the workload.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                id:
                    description:
                        - The Unique Oracle ID (OCID) that is immutable on creation.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                size:
                    description:
                        - Size of the workload.
                    returned: on success
                    type: str
                    sample: size_example
                object_count:
                    description:
                        - Number of objects in a workload.
                    returned: on success
                    type: str
                    sample: object_count_example
                prefix:
                    description:
                        - Prefix to filter objects in case it is a bucket.
                    returned: on success
                    type: str
                    sample: prefix_example
                range_start:
                    description:
                        - Start of the range in a bucket.
                    returned: on success
                    type: str
                    sample: range_start_example
                range_end:
                    description:
                        - End of the range in a bucket.
                    returned: on success
                    type: str
                    sample: range_end_example
                workload_type:
                    description:
                        - The type of workload
                    returned: on success
                    type: str
                    sample: workload_type_example
                work_request_id:
                    description:
                        - The compute work request id to track progress of custom image exports.
                    returned: on success
                    type: str
                    sample: "ocid1.workrequest.oc1..xxxxxxEXAMPLExxxxxx"
        cluster_type:
            description:
                - Type of cluster.
            returned: on success
            type: str
            sample: STANDALONE
        subscription_id:
            description:
                - ID provided to customer after successful subscription to Rover Stations.
            returned: on success
            type: str
            sample: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
        exterior_door_code:
            description:
                - Service generated code for the exterior trailer door of the trailer.
            returned: on success
            type: str
            sample: exterior_door_code_example
        interior_alarm_disarm_code:
            description:
                - Service generated code to disarm the interior alarm of the trailer.
            returned: on success
            type: str
            sample: interior_alarm_disarm_code_example
        super_user_password:
            description:
                - Root password for the rover cluster.
            returned: on success
            type: str
            sample: example-password
        unlock_passphrase:
            description:
                - Password to unlock the rover cluster.
            returned: on success
            type: str
            sample: unlock_passphrase_example
        point_of_contact:
            description:
                - Name of point of contact for this order if customer is picking up.
            returned: on success
            type: str
            sample: point_of_contact_example
        point_of_contact_phone_number:
            description:
                - Phone number of point of contact for this order if customer is picking up.
            returned: on success
            type: str
            sample: point_of_contact_phone_number_example
        shipping_preference:
            description:
                - Preference for device delivery.
            returned: on success
            type: str
            sample: ORACLE_SHIPPED
        oracle_shipping_tracking_url:
            description:
                - Tracking Url for the shipped Rover Cluster.
            returned: on success
            type: str
            sample: oracle_shipping_tracking_url_example
        shipping_vendor:
            description:
                - Shipping vendor of choice for orace to customer shipping.
            returned: on success
            type: str
            sample: shipping_vendor_example
        time_pickup_expected:
            description:
                - Expected date when customer wants to pickup the device if they chose customer pickup.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_return_window_starts:
            description:
                - Start time for the window to pickup the device from customer.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_return_window_ends:
            description:
                - End time for the window to pickup the device from customer.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        return_shipping_label_uri:
            description:
                - Uri to download return shipping label.
            returned: on success
            type: str
            sample: return_shipping_label_uri_example
        is_import_requested:
            description:
                - The flag indicating that customer requests data to be imported to OCI upon Rover cluster return.
            returned: on success
            type: bool
            sample: true
        import_compartment_id:
            description:
                - An OCID of a compartment where data will be imported to upon Rover cluster return.
            returned: on success
            type: str
            sample: "ocid1.importcompartment.oc1..xxxxxxEXAMPLExxxxxx"
        import_file_bucket:
            description:
                - Name of a bucket where files from NFS share will be imported to upon Rover cluster return.
            returned: on success
            type: str
            sample: import_file_bucket_example
        data_validation_code:
            description:
                - Validation code returned by data validation tool. Required for return shipping label generation if data import was requested.
            returned: on success
            type: str
            sample: data_validation_code_example
        image_export_par:
            description:
                - The link to pre-authenticated request for a bucket where image workloads are moved.
            returned: on success
            type: str
            sample: image_export_par_example
        master_key_id:
            description:
                - Customer provided master key ID to encrypt secret information. If not provided, Rover's master key will be used for encryption.
            returned: on success
            type: str
            sample: "ocid1.masterkey.oc1..xxxxxxEXAMPLExxxxxx"
        tags:
            description:
                - The tags associated with tagSlug.
            returned: on success
            type: str
            sample: tags_example
        freeform_tags:
            description:
                - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is
                  predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "cluster_size": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_state_details": "lifecycle_state_details_example",
        "customer_shipping_address": {
            "addressee": "addressee_example",
            "care_of": "care_of_example",
            "address1": "address1_example",
            "address2": "address2_example",
            "address3": "address3_example",
            "address4": "address4_example",
            "city_or_locality": "city_or_locality_example",
            "state_or_region": "us-phoenix-1",
            "zipcode": "zipcode_example",
            "country": "country_example",
            "phone_number": "phone_number_example",
            "email": "email_example"
        },
        "nodes": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "cluster_id": "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx",
            "serial_number": "serial_number_example",
            "node_type": "STANDALONE",
            "shape": "shape_example",
            "display_name": "display_name_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "lifecycle_state": "CREATING",
            "lifecycle_state_details": "lifecycle_state_details_example",
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}},
            "system_tags": {}
        }],
        "enclosure_type": "RUGGADIZED",
        "time_customer_received": "2013-10-20T19:20:30+01:00",
        "time_customer_returned": "2013-10-20T19:20:30+01:00",
        "delivery_tracking_info": "delivery_tracking_info_example",
        "cluster_workloads": [{
            "name": "name_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "size": "size_example",
            "object_count": "object_count_example",
            "prefix": "prefix_example",
            "range_start": "range_start_example",
            "range_end": "range_end_example",
            "workload_type": "workload_type_example",
            "work_request_id": "ocid1.workrequest.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "cluster_type": "STANDALONE",
        "subscription_id": "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx",
        "exterior_door_code": "exterior_door_code_example",
        "interior_alarm_disarm_code": "interior_alarm_disarm_code_example",
        "super_user_password": "example-password",
        "unlock_passphrase": "unlock_passphrase_example",
        "point_of_contact": "point_of_contact_example",
        "point_of_contact_phone_number": "point_of_contact_phone_number_example",
        "shipping_preference": "ORACLE_SHIPPED",
        "oracle_shipping_tracking_url": "oracle_shipping_tracking_url_example",
        "shipping_vendor": "shipping_vendor_example",
        "time_pickup_expected": "2013-10-20T19:20:30+01:00",
        "time_return_window_starts": "2013-10-20T19:20:30+01:00",
        "time_return_window_ends": "2013-10-20T19:20:30+01:00",
        "return_shipping_label_uri": "return_shipping_label_uri_example",
        "is_import_requested": true,
        "import_compartment_id": "ocid1.importcompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "import_file_bucket": "import_file_bucket_example",
        "data_validation_code": "data_validation_code_example",
        "image_export_par": "image_export_par_example",
        "master_key_id": "ocid1.masterkey.oc1..xxxxxxEXAMPLExxxxxx",
        "tags": "tags_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.rover import RoverClusterClient
    from oci.rover.models import ChangeRoverClusterCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RoverClusterActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "rover_cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("rover_cluster_id")

    def get_get_fn(self):
        return self.client.get_rover_cluster

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rover_cluster,
            rover_cluster_id=self.module.params.get("rover_cluster_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeRoverClusterCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_rover_cluster_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                rover_cluster_id=self.module.params.get("rover_cluster_id"),
                change_rover_cluster_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


RoverClusterActionsHelperCustom = get_custom_class("RoverClusterActionsHelperCustom")


class ResourceHelper(RoverClusterActionsHelperCustom, RoverClusterActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            rover_cluster_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="rover_cluster",
        service_client_class=RoverClusterClient,
        namespace="rover",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
