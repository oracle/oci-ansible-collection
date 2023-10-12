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
module: oci_container_engine_cluster_actions
short_description: Perform actions on a Cluster resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Cluster resource in Oracle Cloud Infrastructure
    - For I(action=cluster_migrate_to_native_vcn), initiates cluster migration to use native VCN.
    - For I(action=complete_credential_rotation), complete cluster credential rotation. Retire old credentials from kubernetes components.
    - For I(action=start_credential_rotation), start cluster credential rotation by adding new credentials, old credentials will still work after this
      operation.
    - For I(action=update_cluster_endpoint_config), update the details of the cluster endpoint configuration.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    endpoint_config:
        description:
            - The network configuration for access to the Cluster control plane.
            - Required for I(action=cluster_migrate_to_native_vcn).
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
    decommission_delay_duration:
        description:
            - The optional override of the non-native endpoint decommission time after migration is complete. Defaults to 30 days.
            - Applicable only for I(action=cluster_migrate_to_native_vcn).
        type: str
    auto_completion_delay_duration:
        description:
            - The duration in days(in ISO 8601 notation eg. P5D) after which the old credentials should be retired. Maximum delay duration is 14 days.
            - Required for I(action=start_credential_rotation).
        type: str
    cluster_id:
        description:
            - The OCID of the cluster.
        type: str
        aliases: ["id"]
        required: true
    nsg_ids:
        description:
            - A list of the OCIDs of the network security groups (NSGs) to apply to the cluster endpoint. For more information about NSGs, see
              L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
            - Applicable only for I(action=update_cluster_endpoint_config).
        type: list
        elements: str
    is_public_ip_enabled:
        description:
            - Whether the cluster should be assigned a public IP address. Defaults to false. If set to true on a private subnet, the cluster update will fail.
            - Applicable only for I(action=update_cluster_endpoint_config).
        type: bool
    action:
        description:
            - The action to perform on the Cluster.
        type: str
        required: true
        choices:
            - "cluster_migrate_to_native_vcn"
            - "complete_credential_rotation"
            - "start_credential_rotation"
            - "update_cluster_endpoint_config"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action cluster_migrate_to_native_vcn on cluster
  oci_container_engine_cluster_actions:
    # required
    endpoint_config:
      # optional
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
      nsg_ids: [ "nsg_ids_example" ]
      is_public_ip_enabled: true
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    action: cluster_migrate_to_native_vcn

    # optional
    decommission_delay_duration: decommission_delay_duration_example

- name: Perform action complete_credential_rotation on cluster
  oci_container_engine_cluster_actions:
    # required
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    action: complete_credential_rotation

- name: Perform action start_credential_rotation on cluster
  oci_container_engine_cluster_actions:
    # required
    auto_completion_delay_duration: auto_completion_delay_duration_example
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    action: start_credential_rotation

- name: Perform action update_cluster_endpoint_config on cluster
  oci_container_engine_cluster_actions:
    # required
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    action: update_cluster_endpoint_config

    # optional
    nsg_ids: [ "nsg_ids_example" ]
    is_public_ip_enabled: true

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
                time_credential_expiration:
                    description:
                        - The time until which the cluster credential is valid.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
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
        cluster_pod_network_options:
            description:
                - Available CNIs and network options for existing and new node pools of the cluster
            returned: on success
            type: complex
            contains:
                cni_type:
                    description:
                        - The CNI used by the node pools of this cluster
                    returned: on success
                    type: str
                    sample: OCI_VCN_IP_NATIVE
        type:
            description:
                - Type of cluster
            returned: on success
            type: str
            sample: BASIC_CLUSTER
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
            "updated_by_work_request_id": "ocid1.updatedbyworkrequest.oc1..xxxxxxEXAMPLExxxxxx",
            "time_credential_expiration": "2013-10-20T19:20:30+01:00"
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
        },
        "cluster_pod_network_options": [{
            "cni_type": "OCI_VCN_IP_NATIVE"
        }],
        "type": "BASIC_CLUSTER"
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
    from oci.container_engine import ContainerEngineClient
    from oci.container_engine.models import ClusterMigrateToNativeVcnDetails
    from oci.container_engine.models import StartCredentialRotationDetails
    from oci.container_engine.models import UpdateClusterEndpointConfigDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ClusterActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cluster_migrate_to_native_vcn
        complete_credential_rotation
        start_credential_rotation
        update_cluster_endpoint_config
    """

    @staticmethod
    def get_module_resource_id_param():
        return "cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("cluster_id")

    def get_get_fn(self):
        return self.client.get_cluster

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cluster, cluster_id=self.module.params.get("cluster_id"),
        )

    def cluster_migrate_to_native_vcn(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ClusterMigrateToNativeVcnDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cluster_migrate_to_native_vcn,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_id=self.module.params.get("cluster_id"),
                cluster_migrate_to_native_vcn_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def complete_credential_rotation(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.complete_credential_rotation,
            call_fn_args=(),
            call_fn_kwargs=dict(cluster_id=self.module.params.get("cluster_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def start_credential_rotation(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, StartCredentialRotationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_credential_rotation,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_id=self.module.params.get("cluster_id"),
                start_credential_rotation_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def update_cluster_endpoint_config(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpdateClusterEndpointConfigDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_cluster_endpoint_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_id=self.module.params.get("cluster_id"),
                update_cluster_endpoint_config_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ClusterActionsHelperCustom = get_custom_class("ClusterActionsHelperCustom")


class ResourceHelper(ClusterActionsHelperCustom, ClusterActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            endpoint_config=dict(
                type="dict",
                options=dict(
                    subnet_id=dict(type="str"),
                    nsg_ids=dict(type="list", elements="str"),
                    is_public_ip_enabled=dict(type="bool"),
                ),
            ),
            decommission_delay_duration=dict(type="str"),
            auto_completion_delay_duration=dict(type="str"),
            cluster_id=dict(aliases=["id"], type="str", required=True),
            nsg_ids=dict(type="list", elements="str"),
            is_public_ip_enabled=dict(type="bool"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "cluster_migrate_to_native_vcn",
                    "complete_credential_rotation",
                    "start_credential_rotation",
                    "update_cluster_endpoint_config",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="cluster",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
