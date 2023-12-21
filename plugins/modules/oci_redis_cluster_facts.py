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
module: oci_redis_cluster_facts
short_description: Fetches details about one or multiple RedisCluster resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RedisCluster resources in Oracle Cloud Infrastructure
    - Lists the Redis clusters in the specified compartment. A Redis cluster is a memory-based storage solution. For more information, see L(OCI Caching Service
      with Redis,https://docs.cloud.oracle.com/iaas/Content/redis/home.htm).
    - If I(redis_cluster_id) is specified, the details of a single RedisCluster will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    redis_cluster_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle) of the Redis cluster.
            - Required to get a specific redis_cluster.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
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
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific redis_cluster
  oci_redis_cluster_facts:
    # required
    redis_cluster_id: "ocid1.rediscluster.oc1..xxxxxxEXAMPLExxxxxx"

- name: List redis_clusters
  oci_redis_cluster_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
redis_clusters:
    description:
        - List of RedisCluster resources
    returned: on success
    type: complex
    contains:
        node_collection:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - Collection of node objects.
                    returned: on success
                    type: complex
                    contains:
                        private_endpoint_fqdn:
                            description:
                                - The fully qualified domain name (FQDN) of the API endpoint to access a specific node.
                            returned: on success
                            type: str
                            sample: private_endpoint_fqdn_example
                        private_endpoint_ip_address:
                            description:
                                - The private IP address of the API endpoint to access a specific node.
                            returned: on success
                            type: str
                            sample: private_endpoint_ip_address_example
                        display_name:
                            description:
                                - A user-friendly name of a Redis cluster node.
                            returned: on success
                            type: str
                            sample: display_name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle) of the Redis cluster.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle) of the compartment that contains the Redis
                  cluster.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the Redis cluster.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, the message might provide actionable information for a resource in
                  `FAILED` state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        node_count:
            description:
                - The number of nodes in the Redis cluster.
            returned: on success
            type: int
            sample: 56
        node_memory_in_gbs:
            description:
                - The amount of memory allocated to the Redis cluster's nodes, in gigabytes.
            returned: on success
            type: float
            sample: 3.4
        primary_fqdn:
            description:
                - The fully qualified domain name (FQDN) of the API endpoint for the Redis cluster's primary node.
            returned: on success
            type: str
            sample: primary_fqdn_example
        primary_endpoint_ip_address:
            description:
                - The private IP address of the API endpoint for the Redis cluster's primary node.
            returned: on success
            type: str
            sample: primary_endpoint_ip_address_example
        replicas_fqdn:
            description:
                - The fully qualified domain name (FQDN) of the API endpoint for the Redis cluster's replica nodes.
            returned: on success
            type: str
            sample: replicas_fqdn_example
        replicas_endpoint_ip_address:
            description:
                - The private IP address of the API endpoint for the Redis cluster's replica nodes.
            returned: on success
            type: str
            sample: replicas_endpoint_ip_address_example
        software_version:
            description:
                - The Redis version that the cluster is running.
            returned: on success
            type: str
            sample: V7_0_5
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle) of the Redis cluster's subnet.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the Redis cluster was created. An L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339) formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the Redis cluster was updated. An L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339) formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
    sample: [{
        "node_collection": {
            "items": [{
                "private_endpoint_fqdn": "private_endpoint_fqdn_example",
                "private_endpoint_ip_address": "private_endpoint_ip_address_example",
                "display_name": "display_name_example"
            }]
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "node_count": 56,
        "node_memory_in_gbs": 3.4,
        "primary_fqdn": "primary_fqdn_example",
        "primary_endpoint_ip_address": "primary_endpoint_ip_address_example",
        "replicas_fqdn": "replicas_fqdn_example",
        "replicas_endpoint_ip_address": "replicas_endpoint_ip_address_example",
        "software_version": "V7_0_5",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
    from oci.redis import RedisClusterClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RedisClusterFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "redis_cluster_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_redis_cluster,
            redis_cluster_id=self.module.params.get("redis_cluster_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
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
            self.client.list_redis_clusters, **optional_kwargs
        )


RedisClusterFactsHelperCustom = get_custom_class("RedisClusterFactsHelperCustom")


class ResourceFactsHelper(RedisClusterFactsHelperCustom, RedisClusterFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            redis_cluster_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
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
        resource_type="redis_cluster",
        service_client_class=RedisClusterClient,
        namespace="redis",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(redis_clusters=result)


if __name__ == "__main__":
    main()
