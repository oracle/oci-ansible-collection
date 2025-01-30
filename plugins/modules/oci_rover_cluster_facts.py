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
module: oci_rover_cluster_facts
short_description: Fetches details about one or multiple RoverCluster resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RoverCluster resources in Oracle Cloud Infrastructure
    - Returns a list of RoverClusters.
    - If I(rover_cluster_id) is specified, the details of a single RoverCluster will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    rover_cluster_id:
        description:
            - Unique RoverCluster identifier
            - Required to get a specific rover_cluster.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment in which to list resources.
            - Required to list multiple rover_clusters.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    cluster_type:
        description:
            - A filter to return only Clusters of type matched with the given cluster type.
        type: str
        choices:
            - "STANDALONE"
            - "STATION"
    lifecycle_state:
        description:
            - A filter to return only resources their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific rover_cluster
  oci_rover_cluster_facts:
    # required
    rover_cluster_id: "ocid1.rovercluster.oc1..xxxxxxEXAMPLExxxxxx"

- name: List rover_clusters
  oci_rover_cluster_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    cluster_type: STANDALONE
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
rover_clusters:
    description:
        - List of RoverCluster resources
    returned: on success
    type: complex
    contains:
        customer_shipping_address:
            description:
                - ""
                - Returned for get operation
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
        enclosure_type:
            description:
                - The type of enclosure rover nodes in this cluster are shipped in.
                - Returned for get operation
            returned: on success
            type: str
            sample: RUGGADIZED
        time_customer_received:
            description:
                - Time when customer received the cluster.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_customer_returned:
            description:
                - Time when customer returned the cluster.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        delivery_tracking_info:
            description:
                - Tracking information for device shipping.
                - Returned for get operation
            returned: on success
            type: str
            sample: delivery_tracking_info_example
        cluster_workloads:
            description:
                - List of existing workloads that should be provisioned on the nodes.
                - Returned for get operation
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
        subscription_id:
            description:
                - ID provided to customer after successful subscription to Rover Stations.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
        exterior_door_code:
            description:
                - Service generated code for the exterior trailer door of the trailer.
                - Returned for get operation
            returned: on success
            type: str
            sample: exterior_door_code_example
        interior_alarm_disarm_code:
            description:
                - Service generated code to disarm the interior alarm of the trailer.
                - Returned for get operation
            returned: on success
            type: str
            sample: interior_alarm_disarm_code_example
        super_user_password:
            description:
                - Root password for the rover cluster.
                - Returned for get operation
            returned: on success
            type: str
            sample: example-password
        unlock_passphrase:
            description:
                - Password to unlock the rover cluster.
                - Returned for get operation
            returned: on success
            type: str
            sample: unlock_passphrase_example
        point_of_contact:
            description:
                - Name of point of contact for this order if customer is picking up.
                - Returned for get operation
            returned: on success
            type: str
            sample: point_of_contact_example
        point_of_contact_phone_number:
            description:
                - Phone number of point of contact for this order if customer is picking up.
                - Returned for get operation
            returned: on success
            type: str
            sample: point_of_contact_phone_number_example
        shipping_preference:
            description:
                - Preference for device delivery.
                - Returned for get operation
            returned: on success
            type: str
            sample: ORACLE_SHIPPED
        oracle_shipping_tracking_url:
            description:
                - Tracking Url for the shipped Rover Cluster.
                - Returned for get operation
            returned: on success
            type: str
            sample: oracle_shipping_tracking_url_example
        shipping_vendor:
            description:
                - Shipping vendor of choice for orace to customer shipping.
                - Returned for get operation
            returned: on success
            type: str
            sample: shipping_vendor_example
        time_pickup_expected:
            description:
                - Expected date when customer wants to pickup the device if they chose customer pickup.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_return_window_starts:
            description:
                - Start time for the window to pickup the device from customer.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_return_window_ends:
            description:
                - End time for the window to pickup the device from customer.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        return_shipping_label_uri:
            description:
                - Uri to download return shipping label.
                - Returned for get operation
            returned: on success
            type: str
            sample: return_shipping_label_uri_example
        is_import_requested:
            description:
                - The flag indicating that customer requests data to be imported to OCI upon Rover cluster return.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        import_compartment_id:
            description:
                - An OCID of a compartment where data will be imported to upon Rover cluster return.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.importcompartment.oc1..xxxxxxEXAMPLExxxxxx"
        import_file_bucket:
            description:
                - Name of a bucket where files from NFS share will be imported to upon Rover cluster return.
                - Returned for get operation
            returned: on success
            type: str
            sample: import_file_bucket_example
        data_validation_code:
            description:
                - Validation code returned by data validation tool. Required for return shipping label generation if data import was requested.
                - Returned for get operation
            returned: on success
            type: str
            sample: data_validation_code_example
        image_export_par:
            description:
                - The link to pre-authenticated request for a bucket where image workloads are moved.
                - Returned for get operation
            returned: on success
            type: str
            sample: image_export_par_example
        master_key_id:
            description:
                - Customer provided master key ID to encrypt secret information. If not provided, Rover's master key will be used for encryption.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.masterkey.oc1..xxxxxxEXAMPLExxxxxx"
        tags:
            description:
                - The tags associated with tagSlug.
                - Returned for get operation
            returned: on success
            type: str
            sample: tags_example
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
        time_created:
            description:
                - The time the the RoverCluster was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        cluster_size:
            description:
                - Size of the cluster.
            returned: on success
            type: int
            sample: 56
        cluster_type:
            description:
                - Type of cluster.
            returned: on success
            type: str
            sample: STANDALONE
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
    sample: [{
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
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
        "cluster_size": 56,
        "cluster_type": "STANDALONE",
        "lifecycle_state": "CREATING",
        "lifecycle_state_details": "lifecycle_state_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.rover import RoverClusterClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RoverClusterFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "rover_cluster_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rover_cluster,
            rover_cluster_id=self.module.params.get("rover_cluster_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "cluster_type",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_rover_clusters,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


RoverClusterFactsHelperCustom = get_custom_class("RoverClusterFactsHelperCustom")


class ResourceFactsHelper(RoverClusterFactsHelperCustom, RoverClusterFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            rover_cluster_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            cluster_type=dict(type="str", choices=["STANDALONE", "STATION"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="rover_cluster",
        service_client_class=RoverClusterClient,
        namespace="rover",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(rover_clusters=result)


if __name__ == "__main__":
    main()
