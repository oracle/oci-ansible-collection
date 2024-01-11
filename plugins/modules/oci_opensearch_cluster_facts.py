#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_opensearch_cluster_facts
short_description: Fetches details about one or multiple OpensearchCluster resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OpensearchCluster resources in Oracle Cloud Infrastructure
    - Returns a list of OpensearchClusters.
    - If I(opensearch_cluster_id) is specified, the details of a single OpensearchCluster will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    opensearch_cluster_id:
        description:
            - unique OpensearchCluster identifier
            - Required to get a specific opensearch_cluster.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple opensearch_clusters.
        type: str
    lifecycle_state:
        description:
            - A filter to return only OpensearchClusters their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "ACTIVE"
            - "CREATING"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
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
- name: Get a specific opensearch_cluster
  oci_opensearch_cluster_facts:
    # required
    opensearch_cluster_id: "ocid1.opensearchcluster.oc1..xxxxxxEXAMPLExxxxxx"

- name: List opensearch_clusters
  oci_opensearch_cluster_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: ACTIVE
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
opensearch_clusters:
    description:
        - List of OpensearchCluster resources
    returned: on success
    type: complex
    contains:
        time_deleted:
            description:
                - The amount of time in milliseconds since the cluster was updated.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        opensearch_fqdn:
            description:
                - The fully qualified domain name (FQDN) for the cluster's API endpoint.
                - Returned for get operation
            returned: on success
            type: str
            sample: opensearch_fqdn_example
        opensearch_private_ip:
            description:
                - The cluster's private IP address.
                - Returned for get operation
            returned: on success
            type: str
            sample: opensearch_private_ip_example
        opendashboard_fqdn:
            description:
                - The fully qualified domain name (FQDN) for the cluster's OpenSearch Dashboard API endpoint.
                - Returned for get operation
            returned: on success
            type: str
            sample: opendashboard_fqdn_example
        opendashboard_private_ip:
            description:
                - The private IP address for the cluster's OpenSearch Dashboard.
                - Returned for get operation
            returned: on success
            type: str
            sample: opendashboard_private_ip_example
        master_node_count:
            description:
                - The number of master nodes configured for the cluster.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        master_node_host_type:
            description:
                - The instance type for the cluster's master nodes.
                - Returned for get operation
            returned: on success
            type: str
            sample: FLEX
        master_node_host_bare_metal_shape:
            description:
                - The bare metal shape for the cluster's master nodes.
                - Returned for get operation
            returned: on success
            type: str
            sample: master_node_host_bare_metal_shape_example
        master_node_host_ocpu_count:
            description:
                - The number of OCPUs configured for cluster's master nodes.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        master_node_host_memory_gb:
            description:
                - The amount of memory in GB, for the cluster's master nodes.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        data_node_count:
            description:
                - The number of data nodes configured for the cluster.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        data_node_host_type:
            description:
                - The instance type for the cluster's data nodes.
                - Returned for get operation
            returned: on success
            type: str
            sample: FLEX
        data_node_host_bare_metal_shape:
            description:
                - The bare metal shape for the cluster's data nodes.
                - Returned for get operation
            returned: on success
            type: str
            sample: data_node_host_bare_metal_shape_example
        data_node_host_ocpu_count:
            description:
                - The number of OCPUs configured for the cluster's data nodes.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        data_node_host_memory_gb:
            description:
                - The amount of memory in GB, for the cluster's data nodes.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        data_node_storage_gb:
            description:
                - The amount of storage in GB, to configure per node for the cluster's data nodes.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        opendashboard_node_count:
            description:
                - The number of OpenSearch Dashboard nodes configured for the cluster.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        opendashboard_node_host_ocpu_count:
            description:
                - The amount of memory in GB, for the cluster's OpenSearch Dashboard nodes.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        opendashboard_node_host_memory_gb:
            description:
                - The amount of memory in GB, for the cluster's OpenSearch Dashboard nodes.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        vcn_id:
            description:
                - The OCID of the cluster's VCN.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The OCID of the cluster's subnet.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        vcn_compartment_id:
            description:
                - The OCID for the compartment where the cluster's VCN is located.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.vcncompartment.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_compartment_id:
            description:
                - The OCID for the compartment where the cluster's subnet is located.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.subnetcompartment.oc1..xxxxxxEXAMPLExxxxxx"
        fqdn:
            description:
                - The fully qualified domain name (FQDN) for the cluster's API endpoint.
                - Returned for get operation
            returned: on success
            type: str
            sample: fqdn_example
        security_master_user_name:
            description:
                - The name of the master user that are used to manage security config
                - Returned for get operation
            returned: on success
            type: str
            sample: security_master_user_name_example
        security_master_user_password_hash:
            description:
                - The password hash of the master user that are used to manage security config
                - Returned for get operation
            returned: on success
            type: str
            sample: security_master_user_password_hash_example
        id:
            description:
                - The OCID of the cluster.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the cluster. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment where the cluster is located.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The amount of time in milliseconds since the cluster was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The amount of time in milliseconds since the cluster was updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state of the cluster.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
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
        software_version:
            description:
                - The software version the cluster is running.
            returned: on success
            type: str
            sample: software_version_example
        total_storage_gb:
            description:
                - The size in GB of the cluster's total storage.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of the cluster.
            returned: on success
            type: str
            sample: ACTIVE
        availability_domains:
            description:
                - The availability domains to distribute the cluser nodes across.
            returned: on success
            type: list
            sample: []
        security_mode:
            description:
                - The security mode of the cluster.
            returned: on success
            type: str
            sample: DISABLED
    sample: [{
        "time_deleted": "2013-10-20T19:20:30+01:00",
        "opensearch_fqdn": "opensearch_fqdn_example",
        "opensearch_private_ip": "opensearch_private_ip_example",
        "opendashboard_fqdn": "opendashboard_fqdn_example",
        "opendashboard_private_ip": "opendashboard_private_ip_example",
        "master_node_count": 56,
        "master_node_host_type": "FLEX",
        "master_node_host_bare_metal_shape": "master_node_host_bare_metal_shape_example",
        "master_node_host_ocpu_count": 56,
        "master_node_host_memory_gb": 56,
        "data_node_count": 56,
        "data_node_host_type": "FLEX",
        "data_node_host_bare_metal_shape": "data_node_host_bare_metal_shape_example",
        "data_node_host_ocpu_count": 56,
        "data_node_host_memory_gb": 56,
        "data_node_storage_gb": 56,
        "opendashboard_node_count": 56,
        "opendashboard_node_host_ocpu_count": 56,
        "opendashboard_node_host_memory_gb": 56,
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "vcn_compartment_id": "ocid1.vcncompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_compartment_id": "ocid1.subnetcompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "fqdn": "fqdn_example",
        "security_master_user_name": "security_master_user_name_example",
        "security_master_user_password_hash": "security_master_user_password_hash_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "software_version": "software_version_example",
        "total_storage_gb": 56,
        "lifecycle_state": "ACTIVE",
        "availability_domains": [],
        "security_mode": "DISABLED"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.opensearch import OpensearchClusterClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpensearchClusterFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "opensearch_cluster_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_opensearch_cluster,
            opensearch_cluster_id=self.module.params.get("opensearch_cluster_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_opensearch_clusters,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OpensearchClusterFactsHelperCustom = get_custom_class(
    "OpensearchClusterFactsHelperCustom"
)


class ResourceFactsHelper(
    OpensearchClusterFactsHelperCustom, OpensearchClusterFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            opensearch_cluster_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACTIVE",
                    "CREATING",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="opensearch_cluster",
        service_client_class=OpensearchClusterClient,
        namespace="opensearch",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(opensearch_clusters=result)


if __name__ == "__main__":
    main()
