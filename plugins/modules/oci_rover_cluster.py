#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_rover_cluster
short_description: Manage a RoverCluster resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a RoverCluster resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new RoverCluster.
    - "This resource has the following action operations in the M(oracle.oci.oci_rover_cluster_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment containing the RoverCluster.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    cluster_type:
        description:
            - Type of cluster.
        type: str
        choices:
            - "STANDALONE"
            - "STATION"
    master_key_id:
        description:
            - Customer provided master key ID to encrypt secret information. If not provided, Rover's master key will be used for encryption.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    cluster_size:
        description:
            - Number of nodes desired in the cluster, in standalone clusters, between 5 and 15 inclusive. In station clusters, between 15 and 30 inclusive.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    customer_shipping_address:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            addressee:
                description:
                    - Addressee in shipping address.
                type: str
                required: true
            care_of:
                description:
                    - CareOf for shipping address.
                type: str
            address1:
                description:
                    - Address line 1.
                type: str
                required: true
            address2:
                description:
                    - Address line 2.
                type: str
            address3:
                description:
                    - Address line 3.
                type: str
            address4:
                description:
                    - Address line 4.
                type: str
            city_or_locality:
                description:
                    - city or locality for shipping address.
                type: str
                required: true
            state_or_region:
                description:
                    - state or region for shipping address.
                type: str
                required: true
            zipcode:
                description:
                    - zipcode for shipping address.
                type: str
                required: true
            country:
                description:
                    - country for shipping address.
                type: str
                required: true
            phone_number:
                description:
                    - recepient phone number.
                type: str
                required: true
            email:
                description:
                    - recepient email address.
                type: str
    cluster_workloads:
        description:
            - List of existing workloads that should be provisioned on the nodes.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - Name of the Rover Workload
                type: str
            compartment_id:
                description:
                    - The OCID of the compartment containing the workload.
                type: str
                required: true
            id:
                description:
                    - The Unique Oracle ID (OCID) that is immutable on creation.
                type: str
                required: true
            size:
                description:
                    - Size of the workload.
                type: str
            object_count:
                description:
                    - Number of objects in a workload.
                type: str
            prefix:
                description:
                    - Prefix to filter objects in case it is a bucket.
                type: str
            range_start:
                description:
                    - Start of the range in a bucket.
                type: str
            range_end:
                description:
                    - End of the range in a bucket.
                type: str
            workload_type:
                description:
                    - The type of workload
                type: str
                required: true
            work_request_id:
                description:
                    - The compute work request id to track progress of custom image exports.
                type: str
    super_user_password:
        description:
            - Root password for the rover cluster.
            - This parameter is updatable.
        type: str
    lifecycle_state:
        description:
            - The current state of the RoverCluster.
            - This parameter is updatable.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    lifecycle_state_details:
        description:
            - A property that can contain details on the lifecycle.
            - This parameter is updatable.
        type: str
    unlock_passphrase:
        description:
            - Password to unlock the rover cluster.
            - This parameter is updatable.
        type: str
    enclosure_type:
        description:
            - The type of enclosure rover nodes in this cluster are shipped in.
            - This parameter is updatable.
        type: str
        choices:
            - "RUGGADIZED"
            - "NON_RUGGADIZED"
    point_of_contact:
        description:
            - Name of point of contact for this order if customer is picking up.
            - This parameter is updatable.
        type: str
    point_of_contact_phone_number:
        description:
            - Phone number of point of contact for this order if customer is picking up.
            - This parameter is updatable.
        type: str
    shipping_preference:
        description:
            - Preference for device delivery.
            - This parameter is updatable.
        type: str
        choices:
            - "ORACLE_SHIPPED"
            - "CUSTOMER_PICKUP"
    oracle_shipping_tracking_url:
        description:
            - Tracking Url for the shipped Rover Cluster.
            - This parameter is updatable.
        type: str
    subscription_id:
        description:
            - ID provided to customer after successful subscription to Rover Stations.
            - This parameter is updatable.
        type: str
    shipping_vendor:
        description:
            - Shipping vendor of choice for orace to customer shipping.
            - This parameter is updatable.
        type: str
    time_pickup_expected:
        description:
            - Expected date when customer wants to pickup the cluster if they chose customer pickup.
            - This parameter is updatable.
        type: str
    is_import_requested:
        description:
            - The flag indicating that customer requests data to be imported to OCI upon Rover cluster return.
            - This parameter is updatable.
        type: bool
    import_compartment_id:
        description:
            - An OCID of a compartment where data will be imported to upon Rover cluster return.
            - This parameter is updatable.
        type: str
    import_file_bucket:
        description:
            - Name of a bucket where files from NFS share will be imported to upon Rover cluster return.
            - This parameter is updatable.
        type: str
    data_validation_code:
        description:
            - Validation code returned by data validation tool. Required for return shipping label generation if data import was requested.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    system_tags:
        description:
            - "The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined
              and scoped to namespaces.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{orcl-cloud: {free-tier-retain: true}}`"
            - This parameter is updatable.
        type: dict
    rover_cluster_id:
        description:
            - Unique RoverCluster identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the RoverCluster.
            - Use I(state=present) to create or update a RoverCluster.
            - Use I(state=absent) to delete a RoverCluster.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create rover_cluster
  oci_rover_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    cluster_size: 56

    # optional
    cluster_type: STANDALONE
    master_key_id: "ocid1.masterkey.oc1..xxxxxxEXAMPLExxxxxx"
    customer_shipping_address:
      # required
      addressee: addressee_example
      address1: address1_example
      city_or_locality: city_or_locality_example
      state_or_region: us-phoenix-1
      zipcode: zipcode_example
      country: country_example
      phone_number: phone_number_example

      # optional
      care_of: care_of_example
      address2: address2_example
      address3: address3_example
      address4: address4_example
      email: email_example
    cluster_workloads:
    - # required
      compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      workload_type: workload_type_example

      # optional
      name: name_example
      size: size_example
      object_count: object_count_example
      prefix: prefix_example
      range_start: range_start_example
      range_end: range_end_example
      work_request_id: "ocid1.workrequest.oc1..xxxxxxEXAMPLExxxxxx"
    super_user_password: example-password
    lifecycle_state: CREATING
    lifecycle_state_details: lifecycle_state_details_example
    unlock_passphrase: unlock_passphrase_example
    enclosure_type: RUGGADIZED
    point_of_contact: point_of_contact_example
    point_of_contact_phone_number: point_of_contact_phone_number_example
    shipping_preference: ORACLE_SHIPPED
    oracle_shipping_tracking_url: oracle_shipping_tracking_url_example
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
    shipping_vendor: shipping_vendor_example
    time_pickup_expected: time_pickup_expected_example
    is_import_requested: true
    import_compartment_id: "ocid1.importcompartment.oc1..xxxxxxEXAMPLExxxxxx"
    import_file_bucket: import_file_bucket_example
    data_validation_code: data_validation_code_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Update rover_cluster
  oci_rover_cluster:
    # required
    rover_cluster_id: "ocid1.rovercluster.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    cluster_size: 56
    customer_shipping_address:
      # required
      addressee: addressee_example
      address1: address1_example
      city_or_locality: city_or_locality_example
      state_or_region: us-phoenix-1
      zipcode: zipcode_example
      country: country_example
      phone_number: phone_number_example

      # optional
      care_of: care_of_example
      address2: address2_example
      address3: address3_example
      address4: address4_example
      email: email_example
    cluster_workloads:
    - # required
      compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      workload_type: workload_type_example

      # optional
      name: name_example
      size: size_example
      object_count: object_count_example
      prefix: prefix_example
      range_start: range_start_example
      range_end: range_end_example
      work_request_id: "ocid1.workrequest.oc1..xxxxxxEXAMPLExxxxxx"
    super_user_password: example-password
    lifecycle_state: CREATING
    lifecycle_state_details: lifecycle_state_details_example
    unlock_passphrase: unlock_passphrase_example
    enclosure_type: RUGGADIZED
    point_of_contact: point_of_contact_example
    point_of_contact_phone_number: point_of_contact_phone_number_example
    shipping_preference: ORACLE_SHIPPED
    oracle_shipping_tracking_url: oracle_shipping_tracking_url_example
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
    shipping_vendor: shipping_vendor_example
    time_pickup_expected: time_pickup_expected_example
    is_import_requested: true
    import_compartment_id: "ocid1.importcompartment.oc1..xxxxxxEXAMPLExxxxxx"
    import_file_bucket: import_file_bucket_example
    data_validation_code: data_validation_code_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Update rover_cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_rover_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    cluster_size: 56
    customer_shipping_address:
      # required
      addressee: addressee_example
      address1: address1_example
      city_or_locality: city_or_locality_example
      state_or_region: us-phoenix-1
      zipcode: zipcode_example
      country: country_example
      phone_number: phone_number_example

      # optional
      care_of: care_of_example
      address2: address2_example
      address3: address3_example
      address4: address4_example
      email: email_example
    cluster_workloads:
    - # required
      compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      workload_type: workload_type_example

      # optional
      name: name_example
      size: size_example
      object_count: object_count_example
      prefix: prefix_example
      range_start: range_start_example
      range_end: range_end_example
      work_request_id: "ocid1.workrequest.oc1..xxxxxxEXAMPLExxxxxx"
    super_user_password: example-password
    lifecycle_state: CREATING
    lifecycle_state_details: lifecycle_state_details_example
    unlock_passphrase: unlock_passphrase_example
    enclosure_type: RUGGADIZED
    point_of_contact: point_of_contact_example
    point_of_contact_phone_number: point_of_contact_phone_number_example
    shipping_preference: ORACLE_SHIPPED
    oracle_shipping_tracking_url: oracle_shipping_tracking_url_example
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
    shipping_vendor: shipping_vendor_example
    time_pickup_expected: time_pickup_expected_example
    is_import_requested: true
    import_compartment_id: "ocid1.importcompartment.oc1..xxxxxxEXAMPLExxxxxx"
    import_file_bucket: import_file_bucket_example
    data_validation_code: data_validation_code_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Delete rover_cluster
  oci_rover_cluster:
    # required
    rover_cluster_id: "ocid1.rovercluster.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete rover_cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_rover_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.rover import RoverClusterClient
    from oci.rover.models import CreateRoverClusterDetails
    from oci.rover.models import UpdateRoverClusterDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RoverClusterHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(RoverClusterHelperGen, self).get_possible_entity_types() + [
            "rovercluster",
            "roverclusters",
            "roverrovercluster",
            "roverroverclusters",
            "roverclusterresource",
            "roverclustersresource",
            "rover",
        ]

    def get_module_resource_id_param(self):
        return "rover_cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("rover_cluster_id")

    def get_get_fn(self):
        return self.client.get_rover_cluster

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_rover_cluster, rover_cluster_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rover_cluster,
            rover_cluster_id=self.module.params.get("rover_cluster_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name", "cluster_type"]
            if self._use_name_as_identifier()
            else ["display_name", "cluster_type", "lifecycle_state"]
        )

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_rover_clusters, **kwargs
        )

    def get_create_model_class(self):
        return CreateRoverClusterDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_rover_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(create_rover_cluster_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateRoverClusterDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_rover_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                rover_cluster_id=self.module.params.get("rover_cluster_id"),
                update_rover_cluster_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_rover_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                rover_cluster_id=self.module.params.get("rover_cluster_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


RoverClusterHelperCustom = get_custom_class("RoverClusterHelperCustom")


class ResourceHelper(RoverClusterHelperCustom, RoverClusterHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            cluster_type=dict(type="str", choices=["STANDALONE", "STATION"]),
            master_key_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            cluster_size=dict(type="int"),
            customer_shipping_address=dict(
                type="dict",
                options=dict(
                    addressee=dict(type="str", required=True),
                    care_of=dict(type="str"),
                    address1=dict(type="str", required=True),
                    address2=dict(type="str"),
                    address3=dict(type="str"),
                    address4=dict(type="str"),
                    city_or_locality=dict(type="str", required=True),
                    state_or_region=dict(type="str", required=True),
                    zipcode=dict(type="str", required=True),
                    country=dict(type="str", required=True),
                    phone_number=dict(type="str", required=True),
                    email=dict(type="str"),
                ),
            ),
            cluster_workloads=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str"),
                    compartment_id=dict(type="str", required=True),
                    id=dict(type="str", required=True),
                    size=dict(type="str"),
                    object_count=dict(type="str"),
                    prefix=dict(type="str"),
                    range_start=dict(type="str"),
                    range_end=dict(type="str"),
                    workload_type=dict(type="str", required=True),
                    work_request_id=dict(type="str"),
                ),
            ),
            super_user_password=dict(type="str", no_log=True),
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
            lifecycle_state_details=dict(type="str"),
            unlock_passphrase=dict(type="str", no_log=True),
            enclosure_type=dict(type="str", choices=["RUGGADIZED", "NON_RUGGADIZED"]),
            point_of_contact=dict(type="str"),
            point_of_contact_phone_number=dict(type="str"),
            shipping_preference=dict(
                type="str", choices=["ORACLE_SHIPPED", "CUSTOMER_PICKUP"]
            ),
            oracle_shipping_tracking_url=dict(type="str"),
            subscription_id=dict(type="str"),
            shipping_vendor=dict(type="str"),
            time_pickup_expected=dict(type="str"),
            is_import_requested=dict(type="bool"),
            import_compartment_id=dict(type="str"),
            import_file_bucket=dict(type="str"),
            data_validation_code=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            system_tags=dict(type="dict"),
            rover_cluster_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
