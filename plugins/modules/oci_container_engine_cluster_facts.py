#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_container_engine_cluster_facts
short_description: Fetches details about one or multiple Cluster resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Cluster resources in Oracle Cloud Infrastructure
    - List all the cluster objects in a compartment.
    - If I(cluster_id) is specified, the details of a single Cluster will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    cluster_id:
        description:
            - The OCID of the cluster.
            - Required to get a specific cluster.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple clusters.
        type: str
    lifecycle_state:
        description:
            - A cluster lifecycle state to filter on. Can have multiple parameters of this name.
        type: list
        elements: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "FAILED"
            - "DELETING"
            - "DELETED"
            - "UPDATING"
    name:
        description:
            - The name to filter on.
        type: str
    sort_order:
        description:
            - The optional order in which to sort the results.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The optional field to sort the results by.
        type: str
        choices:
            - "ID"
            - "NAME"
            - "TIME_CREATED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List clusters
  oci_container_engine_cluster_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific cluster
  oci_container_engine_cluster_facts:
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
clusters:
    description:
        - List of Cluster resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the cluster.
            returned: on success
            type: str
            sample: ocid1.cluster.oc1.iad.aaaaaaaaga3tombrmq3wgyrvmi3gcn3bmfsdizjwgy4wgyldmy3dcmtcmmyw
        name:
            description:
                - The name of the cluster.
            returned: on success
            type: str
            sample: My Cluster
        compartment_id:
            description:
                - The OCID of the compartment in which the cluster exists.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..aaaaaaaafqm2df7ckwmmbtdsl2bgxsw4fcpvkoojytxrqst24yww2tdmtqcq"
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
            sample: ocid1.vcn.oc1.iad.aaaaaaaa5e3hn7hk6y63awlhbvlhsumkn5p3ficbjcevbnoylvptcpkxtsaa
        kubernetes_version:
            description:
                - The version of Kubernetes running on the cluster masters.
            returned: on success
            type: str
            sample: v1.9.4
        kms_key_id:
            description:
                - The OCID of the KMS key to be used as the master encryption key for Kubernetes secret encryption.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
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
                                - The CIDR block for Kubernetes pods.
                            returned: on success
                            type: str
                            sample: 10.244.0.0/16
                        services_cidr:
                            description:
                                - The CIDR block for Kubernetes services.
                            returned: on success
                            type: str
                            sample: 10.96.0.0/16
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
                            sample: false
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
                    sample: "2017-07-21T16:11:29Z"
                created_by_user_id:
                    description:
                        - The user who created the cluster.
                    returned: on success
                    type: str
                    sample: "ocid1.user.oc1..aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq"
                created_by_work_request_id:
                    description:
                        - The OCID of the work request which created the cluster.
                    returned: on success
                    type: str
                    sample: ocid1.clustersworkrequest.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq
                time_deleted:
                    description:
                        - The time the cluster was deleted.
                    returned: on success
                    type: str
                    sample: "2017-07-21T16:11:29Z"
                deleted_by_user_id:
                    description:
                        - The user who deleted the cluster.
                    returned: on success
                    type: str
                    sample: "ocid1.user.oc1..aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq"
                deleted_by_work_request_id:
                    description:
                        - The OCID of the work request which deleted the cluster.
                    returned: on success
                    type: str
                    sample: ocid1.clustersworkrequest.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq
                time_updated:
                    description:
                        - The time the cluster was updated.
                    returned: on success
                    type: str
                    sample: "2017-07-21T16:11:29Z"
                updated_by_user_id:
                    description:
                        - The user who updated the cluster.
                    returned: on success
                    type: str
                    sample: "ocid1.user.oc1..aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq"
                updated_by_work_request_id:
                    description:
                        - The OCID of the work request which updated the cluster.
                    returned: on success
                    type: str
                    sample: ocid1.clustersworkrequest.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq
        lifecycle_state:
            description:
                - The state of the cluster masters.
            returned: on success
            type: str
            sample: UPDATING
        lifecycle_details:
            description:
                - Details about the state of the cluster masters.
            returned: on success
            type: str
            sample: waiting for node pools
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
                    sample: https://yourkubernetes
                public_endpoint:
                    description:
                        - The public native networking Kubernetes API server endpoint, if one was requested.
                    returned: on success
                    type: str
                    sample: https://yourPublicEndpoint
                private_endpoint:
                    description:
                        - The private native networking Kubernetes API server endpoint.
                    returned: on success
                    type: str
                    sample: https://yourPrivateEndpoint
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
    sample: [{
        "id": "ocid1.cluster.oc1.iad.aaaaaaaaga3tombrmq3wgyrvmi3gcn3bmfsdizjwgy4wgyldmy3dcmtcmmyw",
        "name": "My Cluster",
        "compartment_id": "ocid1.compartment.oc1..aaaaaaaafqm2df7ckwmmbtdsl2bgxsw4fcpvkoojytxrqst24yww2tdmtqcq",
        "endpoint_config": {
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "nsg_ids": [],
            "is_public_ip_enabled": true
        },
        "vcn_id": "ocid1.vcn.oc1.iad.aaaaaaaa5e3hn7hk6y63awlhbvlhsumkn5p3ficbjcevbnoylvptcpkxtsaa",
        "kubernetes_version": "v1.9.4",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "options": {
            "service_lb_subnet_ids": [],
            "kubernetes_network_config": {
                "pods_cidr": "10.244.0.0/16",
                "services_cidr": "10.96.0.0/16"
            },
            "add_ons": {
                "is_kubernetes_dashboard_enabled": true,
                "is_tiller_enabled": true
            },
            "admission_controller_options": {
                "is_pod_security_policy_enabled": false
            }
        },
        "metadata": {
            "time_created": "2017-07-21T16:11:29Z",
            "created_by_user_id": "ocid1.user.oc1..aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq",
            "created_by_work_request_id": "ocid1.clustersworkrequest.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq",
            "time_deleted": "2017-07-21T16:11:29Z",
            "deleted_by_user_id": "ocid1.user.oc1..aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq",
            "deleted_by_work_request_id": "ocid1.clustersworkrequest.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq",
            "time_updated": "2017-07-21T16:11:29Z",
            "updated_by_user_id": "ocid1.user.oc1..aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq",
            "updated_by_work_request_id": "ocid1.clustersworkrequest.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq"
        },
        "lifecycle_state": "UPDATING",
        "lifecycle_details": "waiting for node pools",
        "endpoints": {
            "kubernetes": "https://yourkubernetes",
            "public_endpoint": "https://yourPublicEndpoint",
            "private_endpoint": "https://yourPrivateEndpoint"
        },
        "available_kubernetes_upgrades": [],
        "image_policy_config": {
            "is_policy_enabled": true,
            "key_details": [{
                "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        }
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.container_engine import ContainerEngineClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ClusterFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "cluster_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cluster, cluster_id=self.module.params.get("cluster_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_clusters,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ClusterFactsHelperCustom = get_custom_class("ClusterFactsHelperCustom")


class ResourceFactsHelper(ClusterFactsHelperCustom, ClusterFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            cluster_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="list",
                elements="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "FAILED",
                    "DELETING",
                    "DELETED",
                    "UPDATING",
                ],
            ),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["ID", "NAME", "TIME_CREATED"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="cluster",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(clusters=result)


if __name__ == "__main__":
    main()
