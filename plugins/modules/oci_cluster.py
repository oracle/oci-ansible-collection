#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_cluster
short_description: Manage Kubernetes clusters in OCI Container Engine for Kubernetes Service
description:
    - This module allows the user to create, delete and update Kubernetes clusters in OCI Container Engine for
      Kubernetes Service.
version_added: "2.5"
options:
    cluster_id:
        description: The OCID of the cluster. Required to update/delete a cluster.
        required: false
        aliases: [ 'id' ]
    compartment_id:
        description: The OCID of the compartment in which to create the cluster. Required to create a cluster.
        required: false
    kubernetes_version:
        description: The version of Kubernetes to install into the cluster masters. Required to create a cluster.
        required: false
    name:
        description: The name of the cluster. Avoid entering confidential information. Required to create a cluster.
        required: false
    options:
        description: Optional attributes for the cluster.
        required: false
        suboptions:
            add_ons:
                description: Configurable cluster add-ons.
                required: false
                suboptions:
                    is_kubernetes_dashboard_enabled:
                       description: Whether or not to enable the Kubernetes Dashboard add-on.
                       required: false
                    is_tiller_enabled:
                       description: Whether or not to enable the Tiller add-on.
                       required: false
            kubernetes_network_config:
                description: Network configuration for Kubernetes.
                required: false
                suboptions:
                    pods_cidr:
                        description: The CIDR block for Kubernetes pods.
                        required: false
                    services_cidr:
                        description: The CIDR block for Kubernetes services.
                        required: false
            service_lb_subnet_ids:
                description: The OCIDs of the subnets used for Kubernetes services load balancers.
                required: false
    vcn_id:
        description: The OCID of the virtual cloud network (VCN) in which to create the cluster. Required to create a
                     cluster.
        required: false
    state:
        description: Create or update a cluster with I(state=present). Use I(state=absent) to delete a cluster.
        required: false
        default: present
        choices: ['present', 'absent']
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
- name: Create a cluster
  oci_cluster:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    name: test_cluster
    vcn_id: ocid1.vcn.oc1..xxxxxEXAMPLExxxxx
    kubernetes_version: "v1.9.7"
    options:
      service_lb_subnet_ids:
        - ocid1.subnet.oc1..xxxxxEXAMPLExxxxx
        - ocid1.subnet.oc1..xxxxxEXAMPLExxxxx

- name: Update name and version of Kubernetes master
  oci_cluster:
    id: ocid1.cluster.oc1..xxxxxEXAMPLExxxxx
    name: ansible_cluster
    kubernetes_version: "v1.10.3"

- name: Delete a cluster
  oci_cluster:
    id: ocid1.cluster.oc1..xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
cluster:
    description: Information about the cluster
    returned: On successful create, delete & update operations on cluster
    type: complex
    contains:
        available_kubernetes_upgrades:
            description: Available Kubernetes versions to which the clusters masters may be upgraded.
            returned: always
            type: list
            sample: ["v1.10.3"]
        compartment_id:
            description: The OCID of the compartment in which the cluster exists.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        endpoints:
            description: Endpoints served up by the cluster masters.
            returned: always
            type: dict
            sample: {"kubernetes": "xxxEXAMPLExxx.us-ashburn-1.clusters.oci.oraclecloud.com:6443"}
        id:
            description: The OCID of the cluster.
            returned: always
            type: string
            sample: ocid1.cluster.oc1..xxxxxEXAMPLExxxxx
        kubernetes_version:
            description: The version of Kubernetes running on the cluster masters.
            returned: always
            type: string
            sample: v1.9.7
        lifecycle_details:
            description: Details about the state of the cluster masters.
            returned: always
            type: string
        lifecycle_state:
            description: The state of the cluster masters.
            returned: always
            type: string
            sample: ACTIVE
        metadata:
            description: Metadata about the cluster.
            returned: always
            type: dict
        name:
            description: The name of the cluster.
            returned: always
            type: string
            sample: sample_cluster
        options:
            description: Optional attributes for the cluster.
            returned: always
            type: dict
        vcn_id:
            description: The OCID of the virtual cloud network (VCN) in which the cluster exists.
            returned: always
            type: string
    sample: {
            "available_kubernetes_upgrades": [],
            "compartment_id": ocid1.compartment.oc1..xxxxxEXAMPLExxxxx,
            "endpoints": {
                "kubernetes": "xxxxxEXAMPLExxxxx.clusters.oci.oraclecloud.com:xxxx"
            },
            "id": "ocid1.cluster.oc1..xxxxxEXAMPLExxxxx",
            "kubernetes_version": "v1.10.3",
            "lifecycle_details": "",
            "lifecycle_state": "ACTIVE",
            "metadata": {
                "created_by_user_id": "ocid1.user.oc1..xxxxxEXAMPLExxxxx",
                "created_by_work_request_id": "ocid1.clustersworkrequest.oc1..xxxxxEXAMPLExxxxx",
                "deleted_by_user_id": null,
                "deleted_by_work_request_id": null,
                "time_created": "2018-07-26T18:42:25+00:00",
                "time_deleted": null,
                "time_updated": null,
                "updated_by_user_id": null,
                "updated_by_work_request_id": null
            },
            "name": "test",
            "options": {
                "add_ons": {
                    "is_kubernetes_dashboard_enabled": true,
                    "is_tiller_enabled": true
                },
                "kubernetes_network_config": {
                    "pods_cidr": "10.244.0.0/16",
                    "services_cidr": "10.96.0.0/16"
                },
                "service_lb_subnet_ids": []
            },
            "vcn_id": "ocid1.vcn.oc1.iad.xxxxxEXAMPLExxxxx"
        }
work_request:
    description: Information of work request
    returned: When a new work request is created
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment in which the work request exists.
            returned: always
            type: string
        id:
            description: The OCID of the work request.
            returned: always
            type: string
        operation_type:
            description: The type of work the work request is doing.
            returned: always
            type: string
        resources:
            description: The resources this work request affects.
            returned: always
            type: list
        status:
            description: The current status of the work request.
            returned: always
            type: string
        time_accepted:
            description: The time the work request was accepted.
            returned: always
            type: datetime
        time_finished:
            description: The time the work request was finished.
            returned: always
            type: datetime
        time_started:
            description: The time the work request was started.
            returned: always
            type: datetime
    sample: {
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "id": "ocid1.clustersworkrequest.oc1..xxxxxEXAMPLExxxxx",
            "operation_type": "CLUSTER_CREATE",
            "resources": [
                {
                    "action_type": "IN_PROGRESS",
                    "entity_type": "cluster",
                    "entity_uri": "/clusters/ocid1.cluster.oc1..xxxxxEXAMPLExxxxx",
                    "identifier": "ocid1.cluster.oc1..xxxxxEXAMPLExxxxx"
                }
            ],
            "status": "ACCEPTED",
            "time_accepted": "2018-07-26T18:42:26+00:00",
            "time_finished": "2018-07-26T18:44:13+00:00",
            "time_started": "2018-07-26T18:43:26+00:00"

    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils
from ansible.module_utils.oracle import oci_ce_utils

try:
    from oci.container_engine.container_engine_client import ContainerEngineClient
    from oci.container_engine.models import CreateClusterDetails
    from oci.container_engine.models import UpdateClusterDetails
    from oci.container_engine.models import ClusterCreateOptions
    from oci.container_engine.models import KubernetesNetworkConfig
    from oci.container_engine.models import AddOnOptions

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def delete_cluster(container_engine_client, module):
    result = oci_ce_utils.delete_and_wait(
        resource_type="cluster",
        client=container_engine_client,
        get_fn=container_engine_client.get_cluster,
        kwargs_get={"cluster_id": module.params["cluster_id"]},
        delete_fn=container_engine_client.delete_cluster,
        kwargs_delete={"cluster_id": module.params["cluster_id"]},
        module=module,
    )
    return result


def update_cluster(container_engine_client, module):
    result = oci_ce_utils.update_and_wait(
        resource_type="cluster",
        client=container_engine_client,
        get_fn=container_engine_client.get_cluster,
        kwargs_get={"cluster_id": module.params["cluster_id"]},
        update_fn=container_engine_client.update_cluster,
        primitive_params_update=["cluster_id"],
        kwargs_non_primitive_update={UpdateClusterDetails: "update_cluster_details"},
        module=module,
        update_attributes=UpdateClusterDetails().attribute_map.keys(),
    )
    return result


def create_cluster(container_engine_client, module):
    create_cluster_details = CreateClusterDetails()
    for attribute in create_cluster_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_cluster_details, attribute, module.params[attribute])

    options = module.params["options"]
    if options:
        cluster_create_options = ClusterCreateOptions()
        cluster_create_options.service_lb_subnet_ids = options["service_lb_subnet_ids"]
        if options.get("add_ons", None):
            add_ons = AddOnOptions()
            add_ons.is_kubernetes_dashboard_enabled = options["add_ons"][
                "is_kubernetes_dashboard_enabled"
            ]
            add_ons.is_tiller_enabled = options["add_ons"]["is_tiller_enabled"]
            cluster_create_options.add_ons = add_ons
        if options.get("kubernetes_network_config", None):
            kubernetes_network_config = KubernetesNetworkConfig()
            kubernetes_network_config.pods_cidr = options["kubernetes_network_config"][
                "pods_cidr"
            ]
            kubernetes_network_config.services_cidr = options[
                "kubernetes_network_config"
            ]["services_cidr"]
            cluster_create_options.kubernetes_network_config = kubernetes_network_config
        create_cluster_details.options = cluster_create_options

    result = oci_ce_utils.create_and_wait(
        resource_type="cluster",
        create_fn=container_engine_client.create_cluster,
        kwargs_create={"create_cluster_details": create_cluster_details},
        client=container_engine_client,
        get_fn=container_engine_client.get_cluster,
        get_param="cluster_id",
        module=module,
    )
    return result


def main():
    module_args = oci_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            cluster_id=dict(type="str", required=False, aliases=["id"]),
            kubernetes_version=dict(type="str", required=False),
            name=dict(type="str", required=False),
            options=dict(type=dict, required=False),
            vcn_id=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[("state", "absent", ["cluster_id"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    container_engine_client = oci_utils.create_service_client(
        module, ContainerEngineClient
    )

    state = module.params["state"]
    cluster_id = module.params["cluster_id"]

    if state == "absent":
        result = delete_cluster(container_engine_client, module)

    else:
        if cluster_id is not None:
            result = update_cluster(container_engine_client, module)
        else:
            kwargs_list = {"compartment_id": module.params["compartment_id"]}
            exclude_attributes = {"name": True}
            result = oci_utils.check_and_create_resource(
                resource_type="cluster",
                create_fn=create_cluster,
                kwargs_create={
                    "container_engine_client": container_engine_client,
                    "module": module,
                },
                list_fn=container_engine_client.list_clusters,
                kwargs_list=kwargs_list,
                module=module,
                model=CreateClusterDetails(),
                exclude_attributes=exclude_attributes,
            )
    module.exit_json(**result)


if __name__ == "__main__":
    main()
