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
module: oci_compute_management_instance_pool_actions
short_description: Perform actions on an InstancePool resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an InstancePool resource in Oracle Cloud Infrastructure
    - For I(action=attach_load_balancer), attach a load balancer to the instance pool.
    - For I(action=change_compartment), moves an instance pool into a different compartment within the same tenancy. For
      information about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
      When you move an instance pool to a different compartment, associated resources such as the instances in
      the pool, boot volumes, VNICs, and autoscaling configurations are not moved.
    - For I(action=detach_load_balancer), detach a load balancer from the instance pool.
    - For I(action=reset), performs the reset (immediate power off and power on) action on the specified instance pool,
      which performs the action on all the instances in the pool.
    - For I(action=softreset), performs the softreset (ACPI shutdown and power on) action on the specified instance pool,
      which performs the action on all the instances in the pool.
      Softreset gracefully reboots the instances by sending a shutdown command to the operating systems.
      After waiting 15 minutes for the OS to shut down, the instances are powered off and then powered back on.
    - For I(action=start), performs the start (power on) action on the specified instance pool,
      which performs the action on all the instances in the pool.
    - For I(action=stop), performs the stop (immediate power off) action on the specified instance pool,
      which performs the action on all the instances in the pool.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    port:
        description:
            - The port value to use when creating the backend set.
            - Required for I(action=attach_load_balancer).
        type: int
    vnic_selection:
        description:
            - "Indicates which VNIC on each instance in the pool should be used to associate with the load balancer.
              Possible values are \\"PrimaryVnic\\" or the displayName of one of the secondary VNICs on the instance configuration
              that is associated with the instance pool."
            - Required for I(action=attach_load_balancer).
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to
              move the instance pool to.
            - Required for I(action=change_compartment).
        type: str
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer to attach to the instance pool.
            - Required for I(action=attach_load_balancer), I(action=detach_load_balancer).
        type: str
    backend_set_name:
        description:
            - The name of the backend set on the load balancer to add instances to.
            - Required for I(action=attach_load_balancer), I(action=detach_load_balancer).
        type: str
    instance_pool_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the InstancePool.
        type: str
        required: true
        choices:
            - "attach_load_balancer"
            - "change_compartment"
            - "detach_load_balancer"
            - "reset"
            - "softreset"
            - "start"
            - "stop"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action attach_load_balancer on instance_pool
  oci_compute_management_instance_pool_actions:
    # required
    port: 56
    vnic_selection: vnic_selection_example
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    backend_set_name: backend_set_name_example
    instance_pool_id: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
    action: attach_load_balancer

- name: Perform action change_compartment on instance_pool
  oci_compute_management_instance_pool_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    instance_pool_id: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action detach_load_balancer on instance_pool
  oci_compute_management_instance_pool_actions:
    # required
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    backend_set_name: backend_set_name_example
    instance_pool_id: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
    action: detach_load_balancer

- name: Perform action reset on instance_pool
  oci_compute_management_instance_pool_actions:
    # required
    instance_pool_id: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
    action: reset

- name: Perform action softreset on instance_pool
  oci_compute_management_instance_pool_actions:
    # required
    instance_pool_id: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
    action: softreset

- name: Perform action start on instance_pool
  oci_compute_management_instance_pool_actions:
    # required
    instance_pool_id: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
    action: start

- name: Perform action stop on instance_pool
  oci_compute_management_instance_pool_actions:
    # required
    instance_pool_id: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
    action: stop

"""

RETURN = """
instance_pool:
    description:
        - Details of the InstancePool resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the instance
                  pool.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        instance_configuration_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance configuration associated
                  with the instance pool.
            returned: on success
            type: str
            sample: "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the instance pool.
            returned: on success
            type: str
            sample: PROVISIONING
        placement_configurations:
            description:
                - The placement configurations for the instance pool.
            returned: on success
            type: complex
            contains:
                availability_domain:
                    description:
                        - The availability domain to place instances.
                        - "Example: `Uocm:PHX-AD-1`"
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                primary_subnet_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the primary subnet to place instances.
                    returned: on success
                    type: str
                    sample: "ocid1.primarysubnet.oc1..xxxxxxEXAMPLExxxxxx"
                fault_domains:
                    description:
                        - The fault domains to place instances.
                        - If you don't provide any values, the system makes a best effort to distribute
                          instances across all fault domains based on capacity.
                        - To distribute the instances evenly across selected fault domains, provide a
                          set of fault domains. For example, you might want instances to be evenly
                          distributed if your applications require high availability.
                        - To get a list of fault domains, use the
                          L(ListFaultDomains,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/FaultDomain/ListFaultDomains) operation
                          in the Identity and Access Management Service API.
                        - "Example: `[FAULT-DOMAIN-1, FAULT-DOMAIN-2, FAULT-DOMAIN-3]`"
                    returned: on success
                    type: list
                    sample: []
                secondary_vnic_subnets:
                    description:
                        - The set of secondary VNIC data for instances in the pool.
                    returned: on success
                    type: complex
                    contains:
                        display_name:
                            description:
                                - The display name of the VNIC. This is also used to match against the instance configuration defined
                                  secondary VNIC.
                            returned: on success
                            type: str
                            sample: display_name_example
                        subnet_id:
                            description:
                                - The subnet L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the secondary VNIC.
                            returned: on success
                            type: str
                            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        size:
            description:
                - The number of instances that should be in the instance pool.
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - "The date and time the instance pool was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        load_balancers:
            description:
                - The load balancers attached to the instance pool.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer attachment.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                instance_pool_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance pool of the load balancer
                          attachment.
                    returned: on success
                    type: str
                    sample: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
                load_balancer_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer attached to the instance
                          pool.
                    returned: on success
                    type: str
                    sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                backend_set_name:
                    description:
                        - The name of the backend set on the load balancer.
                    returned: on success
                    type: str
                    sample: backend_set_name_example
                port:
                    description:
                        - The port value used for the backends.
                    returned: on success
                    type: int
                    sample: 56
                vnic_selection:
                    description:
                        - "Indicates which VNIC on each instance in the instance pool should be used to associate with the load balancer.
                          Possible values are \\"PrimaryVnic\\" or the displayName of one of the secondary VNICs on the instance configuration
                          that is associated with the instance pool."
                    returned: on success
                    type: str
                    sample: vnic_selection_example
                lifecycle_state:
                    description:
                        - The status of the interaction between the instance pool and the load balancer.
                    returned: on success
                    type: str
                    sample: ATTACHING
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "instance_configuration_id": "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "placement_configurations": [{
            "availability_domain": "Uocm:PHX-AD-1",
            "primary_subnet_id": "ocid1.primarysubnet.oc1..xxxxxxEXAMPLExxxxxx",
            "fault_domains": [],
            "secondary_vnic_subnets": [{
                "display_name": "display_name_example",
                "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        }],
        "size": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "load_balancers": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "instance_pool_id": "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx",
            "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
            "backend_set_name": "backend_set_name_example",
            "port": 56,
            "vnic_selection": "vnic_selection_example",
            "lifecycle_state": "ATTACHING"
        }]
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
    from oci.core import ComputeManagementClient
    from oci.core.models import AttachLoadBalancerDetails
    from oci.core.models import ChangeInstancePoolCompartmentDetails
    from oci.core.models import DetachLoadBalancerDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstancePoolActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        attach_load_balancer
        change_compartment
        detach_load_balancer
        reset
        softreset
        start
        stop
    """

    @staticmethod
    def get_module_resource_id_param():
        return "instance_pool_id"

    def get_module_resource_id(self):
        return self.module.params.get("instance_pool_id")

    def get_get_fn(self):
        return self.client.get_instance_pool

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_pool,
            instance_pool_id=self.module.params.get("instance_pool_id"),
        )

    def attach_load_balancer(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AttachLoadBalancerDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_load_balancer,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_pool_id=self.module.params.get("instance_pool_id"),
                attach_load_balancer_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeInstancePoolCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_instance_pool_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_pool_id=self.module.params.get("instance_pool_id"),
                change_instance_pool_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def detach_load_balancer(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetachLoadBalancerDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_load_balancer,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_pool_id=self.module.params.get("instance_pool_id"),
                detach_load_balancer_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def reset(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.reset_instance_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_pool_id=self.module.params.get("instance_pool_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def softreset(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.softreset_instance_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_pool_id=self.module.params.get("instance_pool_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def start(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_instance_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_pool_id=self.module.params.get("instance_pool_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def stop(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_instance_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_pool_id=self.module.params.get("instance_pool_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


InstancePoolActionsHelperCustom = get_custom_class("InstancePoolActionsHelperCustom")


class ResourceHelper(InstancePoolActionsHelperCustom, InstancePoolActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            port=dict(type="int"),
            vnic_selection=dict(type="str"),
            compartment_id=dict(type="str"),
            load_balancer_id=dict(type="str"),
            backend_set_name=dict(type="str"),
            instance_pool_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "attach_load_balancer",
                    "change_compartment",
                    "detach_load_balancer",
                    "reset",
                    "softreset",
                    "start",
                    "stop",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="instance_pool",
        service_client_class=ComputeManagementClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
