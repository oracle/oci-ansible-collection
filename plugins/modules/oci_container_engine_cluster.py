#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
version_added: "2.9"
author: Oracle (@oracle)
options:
    name:
        description:
            - The name of the cluster. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment in which to create the cluster.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    vcn_id:
        description:
            - The OCID of the virtual cloud network (VCN) in which to create the cluster.
            - Required for create using I(state=present).
        type: str
    kubernetes_version:
        description:
            - The version of Kubernetes to install into the cluster masters.
            - Required for create using I(state=present).
        type: str
    kms_key_id:
        description:
            - The OCID of the KMS key to be used as the master encryption key for Kubernetes secret encryption.
              When used, `kubernetesVersion` must be at least `v1.13.0`.
        type: str
    options:
        description:
            - Optional attributes for the cluster.
        type: dict
        suboptions:
            service_lb_subnet_ids:
                description:
                    - The OCIDs of the subnets used for Kubernetes services load balancers.
                type: list
            kubernetes_network_config:
                description:
                    - Network configuration for Kubernetes.
                type: dict
                suboptions:
                    pods_cidr:
                        description:
                            - The CIDR block for Kubernetes pods.
                        type: str
                    services_cidr:
                        description:
                            - The CIDR block for Kubernetes services.
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
    name: My Cluster
    compartment_id: ocid1.compartment.oc1..aaaaaaaafqm2df7ckwmmbtdsl2bgxsw4fcpvkoojytxrqst24yww2tdmtqcq
    vcn_id: ocid1.vcn.oc1.iad.aaaaaaaa5e3hn7hk6y63awlhbvlhsumkn5p3ficbjcevbnoylvptcpkxtsaa
    kubernetes_version: v1.9.4

- name: Update cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_container_engine_cluster:
    name: My Cluster
    compartment_id: ocid1.compartment.oc1..aaaaaaaafqm2df7ckwmmbtdsl2bgxsw4fcpvkoojytxrqst24yww2tdmtqcq
    kubernetes_version: v1.9.4

- name: Update cluster
  oci_container_engine_cluster:
    name: My Cluster
    kubernetes_version: v1.9.4
    cluster_id: ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete cluster
  oci_container_engine_cluster:
    cluster_id: ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_container_engine_cluster:
    name: My Cluster
    compartment_id: ocid1.compartment.oc1..aaaaaaaafqm2df7ckwmmbtdsl2bgxsw4fcpvkoojytxrqst24yww2tdmtqcq
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
            type: string
            sample: ocid1.cluster.oc1.iad.aaaaaaaaga3tombrmq3wgyrvmi3gcn3bmfsdizjwgy4wgyldmy3dcmtcmmyw
        name:
            description:
                - The name of the cluster.
            returned: on success
            type: string
            sample: My Cluster
        compartment_id:
            description:
                - The OCID of the compartment in which the cluster exists.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..aaaaaaaafqm2df7ckwmmbtdsl2bgxsw4fcpvkoojytxrqst24yww2tdmtqcq
        vcn_id:
            description:
                - The OCID of the virtual cloud network (VCN) in which the cluster exists.
            returned: on success
            type: string
            sample: ocid1.vcn.oc1.iad.aaaaaaaa5e3hn7hk6y63awlhbvlhsumkn5p3ficbjcevbnoylvptcpkxtsaa
        kubernetes_version:
            description:
                - The version of Kubernetes running on the cluster masters.
            returned: on success
            type: string
            sample: v1.9.4
        kms_key_id:
            description:
                - The OCID of the KMS key to be used as the master encryption key for Kubernetes secret encryption.
            returned: on success
            type: string
            sample: ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx
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
                            type: string
                            sample: 10.244.0.0/16
                        services_cidr:
                            description:
                                - The CIDR block for Kubernetes services.
                            returned: on success
                            type: string
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
                    type: string
                    sample: 2017-07-21T16:11:29Z
                created_by_user_id:
                    description:
                        - The user who created the cluster.
                    returned: on success
                    type: string
                    sample: ocid1.user.oc1..aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq
                created_by_work_request_id:
                    description:
                        - The OCID of the work request which created the cluster.
                    returned: on success
                    type: string
                    sample: ocid1.clustersworkrequest.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq
                time_deleted:
                    description:
                        - The time the cluster was deleted.
                    returned: on success
                    type: string
                    sample: 2017-07-21T16:11:29Z
                deleted_by_user_id:
                    description:
                        - The user who deleted the cluster.
                    returned: on success
                    type: string
                    sample: ocid1.user.oc1..aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq
                deleted_by_work_request_id:
                    description:
                        - The OCID of the work request which deleted the cluster.
                    returned: on success
                    type: string
                    sample: ocid1.clustersworkrequest.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq
                time_updated:
                    description:
                        - The time the cluster was updated.
                    returned: on success
                    type: string
                    sample: 2017-07-21T16:11:29Z
                updated_by_user_id:
                    description:
                        - The user who updated the cluster.
                    returned: on success
                    type: string
                    sample: ocid1.user.oc1..aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq
                updated_by_work_request_id:
                    description:
                        - The OCID of the work request which updated the cluster.
                    returned: on success
                    type: string
                    sample: ocid1.clustersworkrequest.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq
        lifecycle_state:
            description:
                - The state of the cluster masters.
            returned: on success
            type: string
            sample: UPDATING
        lifecycle_details:
            description:
                - Details about the state of the cluster masters.
            returned: on success
            type: string
            sample: waiting for node pools
        endpoints:
            description:
                - Endpoints served up by the cluster masters.
            returned: on success
            type: complex
            contains:
                kubernetes:
                    description:
                        - The Kubernetes API server endpoint.
                    returned: on success
                    type: string
                    sample: https://yourkubernetes
        available_kubernetes_upgrades:
            description:
                - Available Kubernetes versions to which the clusters masters may be upgraded.
            returned: on success
            type: list
            sample: []
    sample: {
        "id": "ocid1.cluster.oc1.iad.aaaaaaaaga3tombrmq3wgyrvmi3gcn3bmfsdizjwgy4wgyldmy3dcmtcmmyw",
        "name": "My Cluster",
        "compartment_id": "ocid1.compartment.oc1..aaaaaaaafqm2df7ckwmmbtdsl2bgxsw4fcpvkoojytxrqst24yww2tdmtqcq",
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
            "kubernetes": "https://yourkubernetes"
        },
        "available_kubernetes_upgrades": []
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

    def get_module_resource_id_param(self):
        return "cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("cluster_id")

    def get_get_fn(self):
        return self.client.get_cluster

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
            name=dict(type="str"),
            compartment_id=dict(type="str"),
            vcn_id=dict(type="str"),
            kubernetes_version=dict(type="str"),
            kms_key_id=dict(type="str"),
            options=dict(
                type="dict",
                options=dict(
                    service_lb_subnet_ids=dict(type="list"),
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
