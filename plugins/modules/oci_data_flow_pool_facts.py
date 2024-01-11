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
module: oci_data_flow_pool_facts
short_description: Fetches details about one or multiple Pool resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Pool resources in Oracle Cloud Infrastructure
    - Lists all pools in the specified compartment. The query must include compartmentId. The query may also include one other parameter. If the query does not
      include compartmentId, or includes compartmentId, but with two or more other parameters, an error is returned.
    - If I(pool_id) is specified, the details of a single Pool will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    pool_id:
        description:
            - The unique ID for a pool.
            - Required to get a specific pool.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple pools.
        type: str
    lifecycle_state:
        description:
            - The LifecycleState of the pool.
        type: str
        choices:
            - "ACCEPTED"
            - "SCHEDULED"
            - "CREATING"
            - "ACTIVE"
            - "STOPPING"
            - "STOPPED"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_by:
        description:
            - The field used to sort the results. Multiple fields are not supported.
        type: str
        choices:
            - "timeCreated"
    sort_order:
        description:
            - The ordering of results in ascending or descending order.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - The query parameter for the Spark application name.
        type: str
        aliases: ["name"]
    owner_principal_id:
        description:
            - The OCID of the user who created the resource.
        type: str
    display_name_starts_with:
        description:
            - The displayName prefix.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific pool
  oci_data_flow_pool_facts:
    # required
    pool_id: "ocid1.pool.oc1..xxxxxxEXAMPLExxxxxx"

- name: List pools
  oci_data_flow_pool_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: ACCEPTED
    sort_by: timeCreated
    sort_order: ASC
    display_name: display_name_example
    owner_principal_id: "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx"
    display_name_starts_with: display_name_starts_with_example

"""

RETURN = """
pools:
    description:
        - List of Pool resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - A user-friendly description. Avoid entering confidential information.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        lifecycle_details:
            description:
                - The detailed messages about the lifecycle state.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecycle_details_example
        pool_metrics:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                time_last_started:
                    description:
                        - The last time this pool was started.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_last_stopped:
                    description:
                        - The last time this pool was stopped.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_last_used:
                    description:
                        - The last time a run used this pool.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_last_metrics_updated:
                    description:
                        - The last time the mertics were updated for this.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                active_runs_count:
                    description:
                        - The number of runs that are currently running that are using this pool.
                    returned: on success
                    type: int
                    sample: 56
                actively_used_node_count:
                    description:
                        - A count of the nodes that are currently being used for each shape in this pool.
                    returned: on success
                    type: complex
                    contains:
                        logical_shape:
                            description:
                                - The compute shape of the nodes that the count is for.
                            returned: on success
                            type: str
                            sample: logical_shape_example
                        count:
                            description:
                                - The node count of this compute shape.
                            returned: on success
                            type: int
                            sample: 56
        configurations:
            description:
                - List of PoolConfig items.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                shape:
                    description:
                        - The compute shape of the resources you would like to provision.
                    returned: on success
                    type: str
                    sample: shape_example
                shape_config:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        ocpus:
                            description:
                                - The total number of OCPUs used for the driver or executors.
                                  See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                            returned: on success
                            type: float
                            sample: 10
                        memory_in_gbs:
                            description:
                                - The amount of memory used for the driver or executors.
                            returned: on success
                            type: float
                            sample: 10
                min:
                    description:
                        - Minimum number of compute instances in the pool for a given compute shape.
                    returned: on success
                    type: int
                    sample: 56
                max:
                    description:
                        - Maximum number of compute instances in the pool for a given compute shape.
                    returned: on success
                    type: int
                    sample: 56
        schedules:
            description:
                - A list of schedules for pool to auto start and stop.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                day_of_week:
                    description:
                        - Day of the week SUN-SAT
                    returned: on success
                    type: str
                    sample: SUNDAY
                start_time:
                    description:
                        - Hour of the day to start or stop pool.
                    returned: on success
                    type: int
                    sample: 56
                stop_time:
                    description:
                        - Hour of the day to stop the pool.
                    returned: on success
                    type: int
                    sample: 56
        idle_timeout_in_minutes:
            description:
                - Optional timeout value in minutes used to auto stop Pools. A Pool will be auto stopped after inactivity for this amount of time period.
                  If value not set, pool will not be auto stopped auto.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. It does not have to be unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of a pool. Unique Id to indentify a dataflow pool resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of this pool.
            returned: on success
            type: str
            sample: ACCEPTED
        owner_principal_id:
            description:
                - The OCID of the user who created the resource.
            returned: on success
            type: str
            sample: "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx"
        owner_user_name:
            description:
                - The username of the user who created the resource.  If the username of the owner does not exist,
                  `null` will be returned and the caller should refer to the ownerPrincipalId value instead.
            returned: on success
            type: str
            sample: owner_user_name_example
        time_created:
            description:
                - "The date and time the resource was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The date and time the resource was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "description": "description_example",
        "lifecycle_details": "lifecycle_details_example",
        "pool_metrics": {
            "time_last_started": "2013-10-20T19:20:30+01:00",
            "time_last_stopped": "2013-10-20T19:20:30+01:00",
            "time_last_used": "2013-10-20T19:20:30+01:00",
            "time_last_metrics_updated": "2013-10-20T19:20:30+01:00",
            "active_runs_count": 56,
            "actively_used_node_count": [{
                "logical_shape": "logical_shape_example",
                "count": 56
            }]
        },
        "configurations": [{
            "shape": "shape_example",
            "shape_config": {
                "ocpus": 10,
                "memory_in_gbs": 10
            },
            "min": 56,
            "max": 56
        }],
        "schedules": [{
            "day_of_week": "SUNDAY",
            "start_time": 56,
            "stop_time": 56
        }],
        "idle_timeout_in_minutes": 56,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACCEPTED",
        "owner_principal_id": "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx",
        "owner_user_name": "owner_user_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_flow import DataFlowClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowPoolFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "pool_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_pool, pool_id=self.module.params.get("pool_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "sort_by",
            "sort_order",
            "display_name",
            "owner_principal_id",
            "display_name_starts_with",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_pools,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataFlowPoolFactsHelperCustom = get_custom_class("DataFlowPoolFactsHelperCustom")


class ResourceFactsHelper(DataFlowPoolFactsHelperCustom, DataFlowPoolFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            pool_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACCEPTED",
                    "SCHEDULED",
                    "CREATING",
                    "ACTIVE",
                    "STOPPING",
                    "STOPPED",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_by=dict(type="str", choices=["timeCreated"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
            owner_principal_id=dict(type="str"),
            display_name_starts_with=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="pool",
        service_client_class=DataFlowClient,
        namespace="data_flow",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(pools=result)


if __name__ == "__main__":
    main()
