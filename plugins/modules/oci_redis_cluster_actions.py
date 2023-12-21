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
module: oci_redis_cluster_actions
short_description: Perform actions on a RedisCluster resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a RedisCluster resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a Redis cluster into a different compartment within the same tenancy. A Redis cluster is a memory-based storage
      solution. For more information, see L(OCI Caching Service with Redis,https://docs.cloud.oracle.com/iaas/Content/redis/home.htm).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    redis_cluster_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle) of the Redis cluster.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle) of the compartment
              into which the Redis cluster should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the RedisCluster.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on redis_cluster
  oci_redis_cluster_actions:
    # required
    redis_cluster_id: "ocid1.rediscluster.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
redis_cluster:
    description:
        - Details of the RedisCluster resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
        node_collection:
            description:
                - ""
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
    sample: {
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
        "node_collection": {
            "items": [{
                "private_endpoint_fqdn": "private_endpoint_fqdn_example",
                "private_endpoint_ip_address": "private_endpoint_ip_address_example",
                "display_name": "display_name_example"
            }]
        },
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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.redis import RedisClusterClient
    from oci.redis.models import ChangeRedisClusterCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RedisClusterActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "redis_cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("redis_cluster_id")

    def get_get_fn(self):
        return self.client.get_redis_cluster

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_redis_cluster,
            redis_cluster_id=self.module.params.get("redis_cluster_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeRedisClusterCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_redis_cluster_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                redis_cluster_id=self.module.params.get("redis_cluster_id"),
                change_redis_cluster_compartment_details=action_details,
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


RedisClusterActionsHelperCustom = get_custom_class("RedisClusterActionsHelperCustom")


class ResourceHelper(RedisClusterActionsHelperCustom, RedisClusterActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            redis_cluster_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="redis_cluster",
        service_client_class=RedisClusterClient,
        namespace="redis",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
