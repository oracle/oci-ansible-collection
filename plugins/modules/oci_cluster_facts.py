#!/usr/bin/python
# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
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
module: oci_cluster_facts
short_description: Retrieve facts of clusters in OCI Container Engine for Kubernetes Service
description:
    - This module retrieves information of a specific cluster or of all the clusters in OCI Container Engine for
      Kubernetes Service.
version_added: "2.5"
options:
    cluster_id:
        description: The OCID of the cluster. I(cluster_id) is required to get the details of a cluster.
        required: false
        aliases: [ 'id' ]
    compartment_id:
        description: The OCID of the compartment. I(compartment_id) is required to list all the cluster objects in a
                     compartment.
        required: false
    lifecycle_state:
        description: A cluster lifecycle state to filter on. Can have multiple parameters of this name. Allowed values
                     are "CREATING", "ACTIVE", "FAILED", "DELETING", "DELETED", "UPDATING".
        required: false
        type: list
        choices: ['CREATING', 'ACTIVE', 'FAILED', 'DELETING', 'DELETED', 'UPDATING']
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_name_option ]
"""

EXAMPLES = """
- name: Get all the clusters
  oci_cluster_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

- name: Get a specific cluster
  oci_cluster_facts:
    cluster_id: ocid1.cluster.oc1..xxxxxEXAMPLExxxxx

- name: Get clusters in a compartment having the specified name
  oci_cluster_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    name: test_cluster
"""

RETURN = """
clusters:
    description: List of cluster details
    returned: always
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
    sample: [{
            "available_kubernetes_upgrades": ["v1.10.3"],
            "compartment_id": ocid1.compartment.oc1..xxxxxEXAMPLExxxxx,
            "endpoints": {
                "kubernetes": "xxxxxEXAMPLExxxxx.clusters.oci.oraclecloud.com:xxxx"
            },
            "id": "ocid1.cluster.oc1..xxxxxEXAMPLExxxxx",
            "kubernetes_version": "v1.9.7",
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
        }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.container_engine.container_engine_client import ContainerEngineClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_name=True)
    module_args.update(
        dict(
            cluster_id=dict(type="str", required=False, aliases=["id"]),
            compartment_id=dict(type="str", required=False),
            lifecycle_state=dict(
                type="list",
                required=False,
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "FAILED",
                    "DELETING",
                    "DELETED",
                    "UPDATING",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    container_engine_client = oci_utils.create_service_client(
        module, ContainerEngineClient
    )

    cluster_id = module.params["cluster_id"]

    try:
        if cluster_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        container_engine_client.get_cluster, cluster_id=cluster_id
                    ).data
                )
            ]
        else:
            optional_list_method_params = ["name", "lifecycle_state"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            result = to_dict(
                oci_utils.list_all_resources(
                    container_engine_client.list_clusters,
                    compartment_id=module.params["compartment_id"],
                    **optional_kwargs
                )
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(clusters=result)


if __name__ == "__main__":
    main()
