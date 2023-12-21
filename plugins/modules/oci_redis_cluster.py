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
module: oci_redis_cluster
short_description: Manage a RedisCluster resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a RedisCluster resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Redis cluster. A Redis cluster is a memory-based storage solution. For more information, see L(OCI Caching Service
      with Redis,https://docs.cloud.oracle.com/iaas/Content/redis/home.htm).
    - "This resource has the following action operations in the M(oracle.oci.oci_redis_cluster_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle) of the compartment that contains the Redis cluster.
            - Required for create using I(state=present).
        type: str
    software_version:
        description:
            - The Redis version that the cluster is running.
            - Required for create using I(state=present).
        type: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle) of the Redis cluster's subnet.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    node_count:
        description:
            - The number of nodes in the Redis cluster.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    node_memory_in_gbs:
        description:
            - The amount of memory allocated to the Redis cluster's nodes, in gigabytes.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: float
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    redis_cluster_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle) of the Redis cluster.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the RedisCluster.
            - Use I(state=present) to create or update a RedisCluster.
            - Use I(state=absent) to delete a RedisCluster.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create redis_cluster
  oci_redis_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    software_version: software_version_example
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    node_count: 56
    node_memory_in_gbs: 3.4

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update redis_cluster
  oci_redis_cluster:
    # required
    redis_cluster_id: "ocid1.rediscluster.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    node_count: 56
    node_memory_in_gbs: 3.4
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update redis_cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_redis_cluster:
    # required
    display_name: display_name_example

    # optional
    node_count: 56
    node_memory_in_gbs: 3.4
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete redis_cluster
  oci_redis_cluster:
    # required
    redis_cluster_id: "ocid1.rediscluster.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete redis_cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_redis_cluster:
    # required
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.redis import RedisClusterClient
    from oci.redis.models import CreateRedisClusterDetails
    from oci.redis.models import UpdateRedisClusterDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RedisClusterHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(RedisClusterHelperGen, self).get_possible_entity_types() + [
            "rediscluster",
            "redisclusters",
            "redisrediscluster",
            "redisredisclusters",
            "redisclusterresource",
            "redisclustersresource",
            "redis",
        ]

    def get_module_resource_id_param(self):
        return "redis_cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("redis_cluster_id")

    def get_get_fn(self):
        return self.client.get_redis_cluster

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_redis_cluster, redis_cluster_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_redis_cluster,
            redis_cluster_id=self.module.params.get("redis_cluster_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "display_name"]

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
            self.client.list_redis_clusters, **kwargs
        )

    def get_create_model_class(self):
        return CreateRedisClusterDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_redis_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(create_redis_cluster_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateRedisClusterDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_redis_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                redis_cluster_id=self.module.params.get("redis_cluster_id"),
                update_redis_cluster_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_redis_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                redis_cluster_id=self.module.params.get("redis_cluster_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


RedisClusterHelperCustom = get_custom_class("RedisClusterHelperCustom")


class ResourceHelper(RedisClusterHelperCustom, RedisClusterHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            software_version=dict(type="str"),
            subnet_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            node_count=dict(type="int"),
            node_memory_in_gbs=dict(type="float"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            redis_cluster_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
