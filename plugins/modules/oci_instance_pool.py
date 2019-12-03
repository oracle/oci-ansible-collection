#!/usr/bin/python
# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
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
module: oci_instance_pool
short_description: Manage Instance Pools in OCI
description:
    - This module allows the user to create, update, terminate and perform other power actions (such as reset,
      soft-reset, start and stop) on an Instance Pool in OCI.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment containing the instance pool. Required to create an instance
                     pool.
        required: false
    name:
        description: The user-friendly name. Does not have to be unique.
        required: false
        aliases: ['display_name']
    instance_configuration_id:
        description: The OCID of the instance configuration associated to the instance pool. Required for creating an
                     Instance pool
        required: false
    placement_configurations:
        description: The placement configurations for the instance pool. There should be 1 placement configuration for
                     each desired AD. Required to create an instance pool.
        required: false
        suboptions:
            availability_domain:
                description: The availability domain to place instances.
                required: true
            primary_subnet_id:
                description: The OCID of the primary subnet to place instances.
                required: true
            secondary_vnics:
                description: A list of secondary VNIC configurations for instances in the pool.
                required: false
                suboptions:
                    display_name:
                        description: The displayName of the vnic. This is also use to match against the Instance
                                     Configuration defined secondary vnic.
                        required: false
                    subnet_id:
                        description: The subnet OCID for the secondary vnic
                        required: false
    size:
        description: The number of instances that should be in the instance pool. Required to create an instance pool.
        required: false
    instance_pool_id:
        description: The OCID of the instance pool. Required for updating and terminating the instance pool
        required: false
        aliases: ['id']
    state:
        description: Create or update an instance pool with I(state=present). Use I(state=absent) to delete an
                     instance pool. When I(state=stopped), stop (power off) action is performed on the specified
                     instance pool, which performs the action on all the instances in the pool. When I(state=softreset),
                     the softreset (ACPI shutdown and power on) action is performed on the specified instance pool,
                     which performs the action on all the instances in the pool. When I(state=reset), the reset (power
                     off and power on) action is performed on the specified instance pool, which performs the action on
                     all the instances in the pool. Note that I(state=softreset) and I(state=reset) states are not
                     idempotent. Every time a play is executed with these C(state) options, a shutdown and a power on
                     sequence is executed against the instance pool.
        required: false
        default: present
        choices: ['present', 'absent', 'running', 'reset', 'softreset', 'stopped']
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create an instance pool
  oci_instance_pool:
    name: "backend-servers-pool"
    compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
    instance_configuration_id: ocid1.instanceconfiguration.oc1.phx.xxxxxEXAMPLExxxxx...rz3fhq
    size: 5
    placement_configurations:
        - availability_domain: "Uocm PHX-AD-1"
          primary_subnet_id: "ocid1.subnet.oci1.phx.xxxxxEXAMPLExxxxx...abcd"
        - availability_domain: "Uocm PHX-AD-2"
          primary_subnet_id: "ocid1.subnet.oci1.phx.xxxxxEXAMPLExxxxx...efgh"

- name: Stop an instance pool
  oci_instance_pool:
    id: ocid1.instancepool.oc1.phx.xxxxxEXAMPLExxxxx...rz3fhq
    state: stopped

- name: Start an instance pool
  oci_instance_pool:
    id: ocid1.instancepool.oc1.phx.xxxxxEXAMPLExxxxx...rz3fhq
    state: running

- name: Reset an instance pool
  oci_instance_pool:
    id: ocid1.instancepool.oc1.phx.xxxxxEXAMPLExxxxx...rz3fhq
    state: reset

- name: Soft-reset an instance pool
  oci_instance_pool:
    id: ocid1.instancepool.oc1.phx.xxxxxEXAMPLExxxxx...rz3fhq
    state: softreset

- name: Update an instance pool's display name
  oci_instance_pool:
    id: ocid1.instancepool.oc1.phx.xxxxxEXAMPLExxxxx...rz3fhq
    name: "old-backend-servers-pool"

- name: Delete an instance pool
  oci_instance_pool:
    id: ocid1.instancepool.oc1.phx.xxxxxEXAMPLExxxxx...rz3fhq
    state: absent
"""

RETURN = """
instance_pool:
    description: Information about the Instance Pool
    returned: On successful create, delete operations on instance pools
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment containing the instance pool.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        defined_tags:
            description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: always
            type: string
            sample: {"Operations": {"CostCenter": "42"}}
        display_name:
            description: A user-friendly name for the instance pool.  Does not have to be unique.
            returned: always
            type: string
            sample: "backend-servers-pool"
        freeform_tags:
            description: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                         type, or namespace.
            returned: always
            type: string
            sample: {"Department": "Finance"}
        id:
            description: The OCID of the instance pool.
            returned: always
            type: string
            sample: ocid1.instancepool.oc1.phx.xxxxxEXAMPLExxxxx...rz3fhq
        instance_configuration_id:
            description: The OCID of the instance configuration associated to the intance pool.
            returned: always
            type: string
            sample: ocid1.instanceconfiguration.oc1.phx.xxxxxEXAMPLExxxxx...rzxkhq
        lifecycle_state:
            description: The current state of the instance pool.
            returned: always
            type: string
            sample: RUNNING
        placement_configurations:
            description: The placement configurations for the instance pool.
            returned: always
            type: complex
            suboptions:
                availability_domain:
                    description: The availability domain to place instances.
                    returned: always
                    type: string
                primary_subnet_id:
                    description: The OCID of the primary subnet to place instances.
                    returned: always
                    type: string
                secondary_vnics:
                    description: A list of secondary VNIC configurations for instances in the pool.
                    required: false
                    suboptions:
                        display_name:
                            description: The displayName of the vnic. This is also use to match against the Instance
                                         Configuration defined secondary vnic.
                            returned: always
                            type: string
                        subnet_id:
                            description: The subnet OCID for the secondary vnic
                            returned: always
                            type: string
        size:
            description: The number of instances in the instance pool.
            returned: always
            type: int
            sample: 5
        time_created:
            description: The date and time the instance configuration was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: "2018-11-07T04:16:20.454000+00:00"
    sample: {
                "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...glmkwq",
                "defined_tags": {},
                "display_name": "backend-servers-pool",
                "freeform_tags": {},
                "id": "ocid1.instancepool.oc1.iad.xxxxxEXAMPLExxxxx...tztpq",
                "instance_configuration_id": "ocid1.instanceconfiguration.oc1.iad.xxxxxEXAMPLExxxxx...iejka",
                "lifecycle_state": "PROVISIONING",
                "placement_configurations": [
                    {
                        "availability-domain": "IwGV:US-ASHBURN-AD-1",
                        "primary-subnet-id": "ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx...dq4a",
                        "secondary-vnic-subnets": null
                    }
                ],
                "size": 1,
                "time-created": "2018-11-09T16:58:35.270000+00:00"
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.compute_management_client import ComputeManagementClient
    from oci.core.models import (
        CreateInstancePoolDetails,
        CreateInstancePoolPlacementConfigurationDetails,
        UpdateInstancePoolDetails,
    )

    import oci
    from oci.util import to_dict
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False

RESOURCE_NAME = "instance_pool"


def delete_instance_pool(compute_management_client, module):
    result = oci_utils.delete_and_wait(
        resource_type=RESOURCE_NAME,
        client=compute_management_client,
        get_fn=compute_management_client.get_instance_pool,
        kwargs_get={"instance_pool_id": module.params["instance_pool_id"]},
        delete_fn=compute_management_client.terminate_instance_pool,
        kwargs_delete={"instance_pool_id": module.params["instance_pool_id"]},
        module=module,
    )
    return result


def create_instance_pool(compute_management_client, module):
    create_instance_pool_details = CreateInstancePoolDetails()
    _update_model_with_attrs(create_instance_pool_details, module.params)

    user_placement_configurations = module.params["placement_configurations"]
    placement_configurations = []
    for item in user_placement_configurations:
        placement_config = CreateInstancePoolPlacementConfigurationDetails()
        _update_model_with_attrs(placement_config, item)
        placement_configurations.append(placement_config)
    create_instance_pool_details.placement_configurations = placement_configurations

    result = oci_utils.create_and_wait(
        resource_type=RESOURCE_NAME,
        create_fn=compute_management_client.create_instance_pool,
        kwargs_create={"create_instance_pool_details": create_instance_pool_details},
        client=compute_management_client,
        get_fn=compute_management_client.get_instance_pool,
        get_param="instance_pool_id",
        module=module,
    )
    return result


def _update_model_with_attrs(model_instance, value_dict):
    for attribute in model_instance.attribute_map:
        if attribute in value_dict:
            setattr(model_instance, attribute, value_dict[attribute])


def update_instance_pool(compute_management_client, module):
    # XXX support update of placement configurations
    return oci_utils.check_and_update_resource(
        resource_type=RESOURCE_NAME,
        client=compute_management_client,
        get_fn=compute_management_client.get_instance_pool,
        kwargs_get={"instance_pool_id": module.params["instance_pool_id"]},
        update_fn=compute_management_client.update_instance_pool,
        primitive_params_update=["instance_pool_id"],
        kwargs_non_primitive_update={
            UpdateInstancePoolDetails: "update_instance_pool_details"
        },
        module=module,
        update_attributes=UpdateInstancePoolDetails().attribute_map.keys(),
    )


def set_logger(my_logger):
    global logger
    logger = my_logger


def get_logger():
    return logger


def debug(s):
    get_logger().debug(s)


def power_action_on_instance_pool(compute_management_client, module):
    result = {}
    changed = False
    # The power action to execute on a compute instance pool to reach the desired 'state'
    state_action_map = {
        "stopped": "STOP",
        "running": "START",
        "reset": "RESET",
        "softreset": "SOFTRESET",
    }
    # The desired lifecycle state for the compute instance pool to reach the user specified 'state'
    desired_lifecycle_states = {
        "stopped": "STOPPED",
        "running": "RUNNING",
        "reset": "RUNNING",
        "softreset": "RUNNING",
    }

    desired_state = module.params["state"]
    instance_pool_id = module.params["id"]
    try:
        response = oci_utils.call_with_backoff(
            compute_management_client.get_instance_pool,
            instance_pool_id=instance_pool_id,
        )
        curr_state = response.data.lifecycle_state

        change_required = False

        # We need to perform a power action if the current state doesn't match the desired state
        if curr_state != desired_lifecycle_states[desired_state]:
            change_required = True

        # Resets also require a change
        if desired_state in ["softreset", "reset"]:
            change_required = True

        if change_required:
            changed = True
            instance_action_method_name = (
                state_action_map[desired_state].lower() + "_instance_pool"
            )
            instance_action_method = getattr(
                compute_management_client, instance_action_method_name
            )
            oci_utils.call_with_backoff(
                instance_action_method, instance_pool_id=instance_pool_id
            )
            response = oci_utils.call_with_backoff(
                compute_management_client.get_instance_pool,
                instance_pool_id=instance_pool_id,
            )
            # for now the power actions on instances do not go through common utilities for wait.
            if module.params.get("wait", None):
                debug(
                    "waiting for lifecycle_state to reach {0}".format(
                        desired_lifecycle_states[desired_state]
                    )
                )
                oci.wait_until(
                    compute_management_client,
                    response,
                    "lifecycle_state",
                    desired_lifecycle_states[desired_state],
                    max_wait_seconds=module.params.get(
                        "wait_timeout", oci_utils.MAX_WAIT_TIMEOUT_IN_SECONDS
                    ),
                )
                response = oci_utils.call_with_backoff(
                    compute_management_client.get_instance_pool,
                    instance_pool_id=instance_pool_id,
                )
            else:
                debug(
                    "Not waiting for power action request {0} as 'wait' is false.".format(
                        desired_state
                    )
                )

        result["instance_pool"] = to_dict(response.data)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))

    result["changed"] = changed
    return result


def main():
    my_logger = oci_utils.get_logger(RESOURCE_NAME)
    set_logger(my_logger)

    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            display_name=dict(type="str", required=False, aliases=["name"]),
            instance_configuration_id=dict(type="str", required=False),
            placement_configurations=dict(type="list", required=False),
            instance_pool_id=dict(type="str", required=False, aliases=["id"]),
            size=dict(type="int", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=[
                    "absent",
                    "present",
                    "running",
                    "reset",
                    "softreset",
                    "stopped",
                ],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[("instance_pool_id", "compartment_id")],
        required_if=[("state", "absent", ["instance_pool_id"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_management_client = oci_utils.create_service_client(
        module, ComputeManagementClient
    )

    state = module.params["state"]

    if state == "absent":
        result = delete_instance_pool(compute_management_client, module)

    elif state == "present":
        instance_pool_id = module.params["instance_pool_id"]

        if instance_pool_id is None:
            kwargs_list = {"compartment_id": module.params["compartment_id"]}
            result = oci_utils.check_and_create_resource(
                resource_type=RESOURCE_NAME,
                create_fn=create_instance_pool,
                kwargs_create={
                    "compute_management_client": compute_management_client,
                    "module": module,
                },
                list_fn=compute_management_client.list_instance_pools,
                kwargs_list=kwargs_list,
                module=module,
                model=CreateInstancePoolDetails(),
                exclude_attributes=None,
                supports_sort_by_time_created=False,
            )
        else:
            result = update_instance_pool(compute_management_client, module)
    else:
        # one of the power actions
        result = power_action_on_instance_pool(compute_management_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
