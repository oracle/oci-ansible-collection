#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_container_engine_cluster
short_description: Manage a Cluster resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Cluster resource in Oracle Cloud Infrastructure
    - For I(state=present), create a new cluster.
    - "This resource has the following action operations in the M(oracle.oci.oci_container_engine_cluster_actions) module: cluster_migrate_to_native_vcn,
      update_cluster_endpoint_config."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment in which to create the cluster.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    endpoint_config:
        description:
            - The network configuration for access to the Cluster control plane.
        type: dict
        suboptions:
            subnet_id:
                description:
                    - The OCID of the regional subnet in which to place the Cluster endpoint.
                type: str
            nsg_ids:
                description:
                    - A list of the OCIDs of the network security groups (NSGs) to apply to the cluster endpoint. For more information about NSGs, see
                      L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
                type: list
                elements: str
            is_public_ip_enabled:
                description:
                    - Whether the cluster should be assigned a public IP address. Defaults to false. If set to true on a private subnet, the cluster
                      provisioning will fail.
                type: bool
    vcn_id:
        description:
            - The OCID of the virtual cloud network (VCN) in which to create the cluster.
            - Required for create using I(state=present).
        type: str
    kms_key_id:
        description:
            - The OCID of the KMS key to be used as the master encryption key for Kubernetes secret encryption.
              When used, `kubernetesVersion` must be at least `v1.13.0`.
        type: str
    name:
        description:
            - The name of the cluster. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
    kubernetes_version:
        description:
            - The version of Kubernetes to install into the cluster masters.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    options:
        description:
            - Optional attributes for the cluster.
            - This parameter is updatable.
        type: dict
        suboptions:
            service_lb_subnet_ids:
                description:
                    - The OCIDs of the subnets used for Kubernetes services load balancers.
                type: list
                elements: str
            kubernetes_network_config:
                description:
                    - Network configuration for Kubernetes.
                type: dict
                suboptions:
                    pods_cidr:
                        description:
                            - The CIDR block for Kubernetes pods. Optional, defaults to 10.244.0.0/16.
                        type: str
                    services_cidr:
                        description:
                            - The CIDR block for Kubernetes services. Optional, defaults to 10.96.0.0/16.
                        type: str
            add_ons:
                description:
                    - Configurable cluster add-ons
                type: dict
                suboptions:
                    is_kubernetes_dashboard_enabled:
                        description:
                            - Whether or not to enable the Kubernetes Dashboard add-on.
                        type: bool
                    is_tiller_enabled:
                        description:
                            - Whether or not to enable the Tiller add-on.
                        type: bool
            admission_controller_options:
                description:
                    - Configurable cluster admission controllers
                type: dict
                suboptions:
                    is_pod_security_policy_enabled:
                        description:
                            - Whether or not to enable the Pod Security Policy admission controller.
                        type: bool
            persistent_volume_config:
                description:
                    - ""
                type: dict
                suboptions:
                    freeform_tags:
                        description:
                            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                              Example: `{\\"Department\\": \\"Finance\\"}`"
                        type: dict
                    defined_tags:
                        description:
                            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                        type: dict
            service_lb_config:
                description:
                    - ""
                type: dict
                suboptions:
                    freeform_tags:
                        description:
                            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                              Example: `{\\"Department\\": \\"Finance\\"}`"
                        type: dict
                    defined_tags:
                        description:
                            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                        type: dict
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    image_policy_config:
        description:
            - The image verification policy for signature validation. Once a policy is created and enabled with
              one or more kms keys, the policy will ensure all images deployed has been signed with the key(s)
              attached to the policy.
            - This parameter is updatable.
        type: dict
        suboptions:
            is_policy_enabled:
                description:
                    - Whether the image verification policy is enabled. Defaults to false. If set to true, the images will be verified against the policy at
                      runtime.
                    - This parameter is updatable.
                type: bool
            key_details:
                description:
                    - A list of KMS key details.
                type: list
                elements: dict
                suboptions:
                    kms_key_id:
                        description:
                            - The OCIDs of the KMS key that will be used to verify whether the images are signed by an approved source.
                        type: str
    cluster_id:
        description:
            - The OCID of the cluster.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Cluster.
            - Use I(state=present) to create or update a Cluster.
            - Use I(state=absent) to delete a Cluster.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create cluster
  oci_container_engine_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    kubernetes_version: kubernetes_version_example

    # optional
    endpoint_config:
      # optional
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
      nsg_ids: [ "nsg_ids_example" ]
      is_public_ip_enabled: true
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    options:
      # optional
      service_lb_subnet_ids: [ "service_lb_subnet_ids_example" ]
      kubernetes_network_config:
        # optional
        pods_cidr: pods_cidr_example
        services_cidr: services_cidr_example
      add_ons:
        # optional
        is_kubernetes_dashboard_enabled: true
        is_tiller_enabled: true
      admission_controller_options:
        # optional
        is_pod_security_policy_enabled: true
      persistent_volume_config:
        # optional
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
      service_lb_config:
        # optional
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    image_policy_config:
      # optional
      is_policy_enabled: true
      key_details:
      - # optional
        kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update cluster
  oci_container_engine_cluster:
    # required
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    kubernetes_version: kubernetes_version_example
    options:
      # optional
      service_lb_subnet_ids: [ "service_lb_subnet_ids_example" ]
      kubernetes_network_config:
        # optional
        pods_cidr: pods_cidr_example
        services_cidr: services_cidr_example
      add_ons:
        # optional
        is_kubernetes_dashboard_enabled: true
        is_tiller_enabled: true
      admission_controller_options:
        # optional
        is_pod_security_policy_enabled: true
      persistent_volume_config:
        # optional
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
      service_lb_config:
        # optional
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    image_policy_config:
      # optional
      is_policy_enabled: true
      key_details:
      - # optional
        kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_container_engine_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    kubernetes_version: kubernetes_version_example
    options:
      # optional
      service_lb_subnet_ids: [ "service_lb_subnet_ids_example" ]
      kubernetes_network_config:
        # optional
        pods_cidr: pods_cidr_example
        services_cidr: services_cidr_example
      add_ons:
        # optional
        is_kubernetes_dashboard_enabled: true
        is_tiller_enabled: true
      admission_controller_options:
        # optional
        is_pod_security_policy_enabled: true
      persistent_volume_config:
        # optional
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
      service_lb_config:
        # optional
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    image_policy_config:
      # optional
      is_policy_enabled: true
      key_details:
      - # optional
        kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete cluster
  oci_container_engine_cluster:
    # required
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_container_engine_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    state: absent

"""

RETURN = """
cluster:
    description:
        - Details of the Cluster resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the cluster.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the cluster.
            returned: on success
            type: str
            sample: name_example
        compartment_id:
            description:
                - The OCID of the compartment in which the cluster exists.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        endpoint_config:
            description:
                - The network configuration for access to the Cluster control plane.
            returned: on success
            type: complex
            contains:
                subnet_id:
                    description:
                        - The OCID of the regional subnet in which to place the Cluster endpoint.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                nsg_ids:
                    description:
                        - A list of the OCIDs of the network security groups (NSGs) to apply to the cluster endpoint. For more information about NSGs, see
                          L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
                    returned: on success
                    type: list
                    sample: []
                is_public_ip_enabled:
                    description:
                        - Whether the cluster should be assigned a public IP address. Defaults to false. If set to true on a private subnet, the cluster
                          provisioning will fail.
                    returned: on success
                    type: bool
                    sample: true
        vcn_id:
            description:
                - The OCID of the virtual cloud network (VCN) in which the cluster exists.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        kubernetes_version:
            description:
                - The version of Kubernetes running on the cluster masters.
            returned: on success
            type: str
            sample: kubernetes_version_example
        kms_key_id:
            description:
                - The OCID of the KMS key to be used as the master encryption key for Kubernetes secret encryption.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        options:
            description:
                - Optional attributes for the cluster.
            returned: on success
            type: complex
            contains:
                service_lb_subnet_ids:
                    description:
                        - The OCIDs of the subnets used for Kubernetes services load balancers.
                    returned: on success
                    type: list
                    sample: []
                kubernetes_network_config:
                    description:
                        - Network configuration for Kubernetes.
                    returned: on success
                    type: complex
                    contains:
                        pods_cidr:
                            description:
                                - The CIDR block for Kubernetes pods. Optional, defaults to 10.244.0.0/16.
                            returned: on success
                            type: str
                            sample: pods_cidr_example
                        services_cidr:
                            description:
                                - The CIDR block for Kubernetes services. Optional, defaults to 10.96.0.0/16.
                            returned: on success
                            type: str
                            sample: services_cidr_example
                add_ons:
                    description:
                        - Configurable cluster add-ons
                    returned: on success
                    type: complex
                    contains:
                        is_kubernetes_dashboard_enabled:
                            description:
                                - Whether or not to enable the Kubernetes Dashboard add-on.
                            returned: on success
                            type: bool
                            sample: true
                        is_tiller_enabled:
                            description:
                                - Whether or not to enable the Tiller add-on.
                            returned: on success
                            type: bool
                            sample: true
                admission_controller_options:
                    description:
                        - Configurable cluster admission controllers
                    returned: on success
                    type: complex
                    contains:
                        is_pod_security_policy_enabled:
                            description:
                                - Whether or not to enable the Pod Security Policy admission controller.
                            returned: on success
                            type: bool
                            sample: true
                persistent_volume_config:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        freeform_tags:
                            description:
                                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                                  Example: `{\\"Department\\": \\"Finance\\"}`"
                            returned: on success
                            type: dict
                            sample: {'Department': 'Finance'}
                        defined_tags:
                            description:
                                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                            returned: on success
                            type: dict
                            sample: {'Operations': {'CostCenter': 'US'}}
                service_lb_config:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        freeform_tags:
                            description:
                                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                                  Example: `{\\"Department\\": \\"Finance\\"}`"
                            returned: on success
                            type: dict
                            sample: {'Department': 'Finance'}
                        defined_tags:
                            description:
                                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                            returned: on success
                            type: dict
                            sample: {'Operations': {'CostCenter': 'US'}}
        metadata:
            description:
                - Metadata about the cluster.
            returned: on success
            type: complex
            contains:
                time_created:
                    description:
                        - The time the cluster was created.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                created_by_user_id:
                    description:
                        - The user who created the cluster.
                    returned: on success
                    type: str
                    sample: "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx"
                created_by_work_request_id:
                    description:
                        - The OCID of the work request which created the cluster.
                    returned: on success
                    type: str
                    sample: "ocid1.createdbyworkrequest.oc1..xxxxxxEXAMPLExxxxxx"
                time_deleted:
                    description:
                        - The time the cluster was deleted.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                deleted_by_user_id:
                    description:
                        - The user who deleted the cluster.
                    returned: on success
                    type: str
                    sample: "ocid1.deletedbyuser.oc1..xxxxxxEXAMPLExxxxxx"
                deleted_by_work_request_id:
                    description:
                        - The OCID of the work request which deleted the cluster.
                    returned: on success
                    type: str
                    sample: "ocid1.deletedbyworkrequest.oc1..xxxxxxEXAMPLExxxxxx"
                time_updated:
                    description:
                        - The time the cluster was updated.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                updated_by_user_id:
                    description:
                        - The user who updated the cluster.
                    returned: on success
                    type: str
                    sample: "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx"
                updated_by_work_request_id:
                    description:
                        - The OCID of the work request which updated the cluster.
                    returned: on success
                    type: str
                    sample: "ocid1.updatedbyworkrequest.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The state of the cluster masters.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details about the state of the cluster masters.
            returned: on success
            type: str
            sample: lifecycle_details_example
        endpoints:
            description:
                - Endpoints served up by the cluster masters.
            returned: on success
            type: complex
            contains:
                kubernetes:
                    description:
                        - The non-native networking Kubernetes API server endpoint.
                    returned: on success
                    type: str
                    sample: kubernetes_example
                public_endpoint:
                    description:
                        - The public native networking Kubernetes API server endpoint, if one was requested.
                    returned: on success
                    type: str
                    sample: public_endpoint_example
                private_endpoint:
                    description:
                        - The private native networking Kubernetes API server endpoint.
                    returned: on success
                    type: str
                    sample: private_endpoint_example
                vcn_hostname_endpoint:
                    description:
                        - "The FQDN assigned to the Kubernetes API private endpoint.
                          Example: 'https://yourVcnHostnameEndpoint'"
                    returned: on success
                    type: str
                    sample: vcn_hostname_endpoint_example
        available_kubernetes_upgrades:
            description:
                - Available Kubernetes versions to which the clusters masters may be upgraded.
            returned: on success
            type: list
            sample: []
        image_policy_config:
            description:
                - The image verification policy for signature validation.
            returned: on success
            type: complex
            contains:
                is_policy_enabled:
                    description:
                        - Whether the image verification policy is enabled. Defaults to false. If set to true, the images will be verified against the policy at
                          runtime.
                    returned: on success
                    type: bool
                    sample: true
                key_details:
                    description:
                        - A list of KMS key details.
                    returned: on success
                    type: complex
                    contains:
                        kms_key_id:
                            description:
                                - The OCIDs of the KMS key that will be used to verify whether the images are signed by an approved source.
                            returned: on success
                            type: str
                            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "endpoint_config": {
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "nsg_ids": [],
            "is_public_ip_enabled": true
        },
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "kubernetes_version": "kubernetes_version_example",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "options": {
            "service_lb_subnet_ids": [],
            "kubernetes_network_config": {
                "pods_cidr": "pods_cidr_example",
                "services_cidr": "services_cidr_example"
            },
            "add_ons": {
                "is_kubernetes_dashboard_enabled": true,
                "is_tiller_enabled": true
            },
            "admission_controller_options": {
                "is_pod_security_policy_enabled": true
            },
            "persistent_volume_config": {
                "freeform_tags": {'Department': 'Finance'},
                "defined_tags": {'Operations': {'CostCenter': 'US'}}
            },
            "service_lb_config": {
                "freeform_tags": {'Department': 'Finance'},
                "defined_tags": {'Operations': {'CostCenter': 'US'}}
            }
        },
        "metadata": {
            "time_created": "2013-10-20T19:20:30+01:00",
            "created_by_user_id": "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx",
            "created_by_work_request_id": "ocid1.createdbyworkrequest.oc1..xxxxxxEXAMPLExxxxxx",
            "time_deleted": "2013-10-20T19:20:30+01:00",
            "deleted_by_user_id": "ocid1.deletedbyuser.oc1..xxxxxxEXAMPLExxxxxx",
            "deleted_by_work_request_id": "ocid1.deletedbyworkrequest.oc1..xxxxxxEXAMPLExxxxxx",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "updated_by_user_id": "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx",
            "updated_by_work_request_id": "ocid1.updatedbyworkrequest.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "endpoints": {
            "kubernetes": "kubernetes_example",
            "public_endpoint": "public_endpoint_example",
            "private_endpoint": "private_endpoint_example",
            "vcn_hostname_endpoint": "vcn_hostname_endpoint_example"
        },
        "available_kubernetes_upgrades": [],
        "image_policy_config": {
            "is_policy_enabled": true,
            "key_details": [{
                "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        }
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.container_engine import ContainerEngineClient
    from oci.container_engine.models import CreateClusterDetails
    from oci.container_engine.models import UpdateClusterDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ClusterHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ClusterHelperGen, self).get_possible_entity_types() + [
            "cluster",
            "clusters",
            "containerEnginecluster",
            "containerEngineclusters",
            "clusterresource",
            "clustersresource",
            "containerengine",
        ]

    def get_module_resource_id_param(self):
        return "cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("cluster_id")

    def get_get_fn(self):
        return self.client.get_cluster

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_cluster, cluster_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cluster, cluster_id=self.module.params.get("cluster_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

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
        return oci_common_utils.list_all_resources(self.client.list_clusters, **kwargs)

    def get_create_model_class(self):
        return CreateClusterDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(create_cluster_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateClusterDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_id=self.module.params.get("cluster_id"),
                update_cluster_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(cluster_id=self.module.params.get("cluster_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ClusterHelperCustom = get_custom_class("ClusterHelperCustom")


class ResourceHelper(ClusterHelperCustom, ClusterHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            endpoint_config=dict(
                type="dict",
                options=dict(
                    subnet_id=dict(type="str"),
                    nsg_ids=dict(type="list", elements="str"),
                    is_public_ip_enabled=dict(type="bool"),
                ),
            ),
            vcn_id=dict(type="str"),
            kms_key_id=dict(type="str"),
            name=dict(type="str"),
            kubernetes_version=dict(type="str"),
            options=dict(
                type="dict",
                options=dict(
                    service_lb_subnet_ids=dict(type="list", elements="str"),
                    kubernetes_network_config=dict(
                        type="dict",
                        options=dict(
                            pods_cidr=dict(type="str"), services_cidr=dict(type="str")
                        ),
                    ),
                    add_ons=dict(
                        type="dict",
                        options=dict(
                            is_kubernetes_dashboard_enabled=dict(type="bool"),
                            is_tiller_enabled=dict(type="bool"),
                        ),
                    ),
                    admission_controller_options=dict(
                        type="dict",
                        options=dict(is_pod_security_policy_enabled=dict(type="bool")),
                    ),
                    persistent_volume_config=dict(
                        type="dict",
                        options=dict(
                            freeform_tags=dict(type="dict"),
                            defined_tags=dict(type="dict"),
                        ),
                    ),
                    service_lb_config=dict(
                        type="dict",
                        options=dict(
                            freeform_tags=dict(type="dict"),
                            defined_tags=dict(type="dict"),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            image_policy_config=dict(
                type="dict",
                options=dict(
                    is_policy_enabled=dict(type="bool"),
                    key_details=dict(
                        type="list",
                        elements="dict",
                        no_log=False,
                        options=dict(kms_key_id=dict(type="str")),
                    ),
                ),
            ),
            cluster_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="cluster",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
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
