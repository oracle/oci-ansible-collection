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
module: oci_compute_management_instance_pool
short_description: Manage an InstancePool resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an InstancePool resource in Oracle Cloud Infrastructure
    - For I(state=present), create an instance pool.
    - "This resource has the following action operations in the M(oci_instance_pool_actions) module: attach_load_balancer, detach_load_balancer, reset,
      softreset, start, stop."
version_added: "2.5"
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the instance pool.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    display_name:
        description:
            - A user-friendly name for the instance pool. Does not have to be unique, and it's
              changeable. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    instance_configuration_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the instance configuration associated
              with the instance pool.
            - Required for create using I(state=present).
        type: str
    placement_configurations:
        description:
            - The placement configurations for the instance pool. Provide one placement configuration for
              each availability domain.
            - To use the instance pool with a regional subnet, provide a placement configuration for
              each availability domain, and include the regional subnet in each placement
              configuration.
            - Required for create using I(state=present).
        type: list
        suboptions:
            availability_domain:
                description:
                    - The availability domain to place instances.
                    - "Example: `Uocm:PHX-AD-1`"
                type: str
                required: true
            primary_subnet_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the primary subnet to place instances.
                type: str
                required: true
            secondary_vnic_subnets:
                description:
                    - The set of secondary VNIC data for instances in the pool.
                type: list
                suboptions:
                    display_name:
                        description:
                            - The display name of the VNIC. This is also use to match against the instance configuration defined
                              secondary VNIC.
                        type: str
                        aliases: ["name"]
                    subnet_id:
                        description:
                            - The subnet L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) for the secondary VNIC.
                        type: str
                        required: true
    size:
        description:
            - The number of instances that should be in the instance pool.
            - Required for create using I(state=present).
        type: int
    load_balancers:
        description:
            - The load balancers to attach to the instance pool.
        type: list
        suboptions:
            load_balancer_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer to attach to the instance pool.
                type: str
                required: true
            backend_set_name:
                description:
                    - The name of the backend set on the load balancer to add instances to.
                type: str
                required: true
            port:
                description:
                    - The port value to use when creating the backend set.
                type: int
                required: true
            vnic_selection:
                description:
                    - "Indicates which VNIC on each instance in the pool should be used to associate with the load balancer. Possible values are
                      \\"PrimaryVnic\\" or the displayName of one of the secondary VNICs on the instance configuration that is associated with the instance
                      pool."
                type: str
                required: true
    instance_pool_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the instance pool.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the InstancePool.
            - Use I(state=present) to create or update an InstancePool.
            - Use I(state=absent) to delete an InstancePool.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create instance_pool
  oci_compute_management_instance_pool:
    display_name: autoscaling-instance-pool
    compartment_id: ocid1.compartment.oc1..&lt;unique_ID&gt;
    instance_configuration_id: ocid1.instanceconfiguration.oc1..&lt;unique_ID&gt;
    size: 15
    placement_configurations:
    - availability_domain: Uocm:PHX-AD-1
      primary_subnet_id: ocid1.subnet.oc1..&lt;regional_subnet_unique_ID&gt;
    - availability_domain: Uocm:PHX-AD-1
      primary_subnet_id: ocid1.subnet.oc1..&lt;regional_subnet_unique_ID&gt;
    - availability_domain: Uocm:PHX-AD-1
      primary_subnet_id: ocid1.subnet.oc1..&lt;regional_subnet_unique_ID&gt;
    load_balancers:
    - load_balancer_id: ocid1.loadbalancer.oc1.phx..&lt;unique_ID&gt;
      backend_set_name: lb-20190410-1147-backend-set
      port: 80
      vnic_selection: PrimaryVnic

- name: Create instance_pool
  oci_compute_management_instance_pool:
    display_name: backend-servers-pool
    compartment_id: ocid1.compartment.oc1..&lt;unique_ID&gt;
    instance_configuration_id: ocid1.instanceconfiguration.oc1..&lt;unique_ID&gt;
    size: 10
    placement_configurations:
    - availability_domain: Uocm:PHX-AD-1
      primary_subnet_id: ocid1.subnet.oc1..&lt;unique_ID_1&gt;
    - availability_domain: Uocm:PHX-AD-1
      primary_subnet_id: ocid1.subnet.oc1..&lt;unique_ID_2&gt;

- name: Update instance_pool using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_management_instance_pool:
    compartment_id: ocid1.compartment.oc1..&lt;unique_ID&gt;
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: autoscaling-instance-pool
    freeform_tags: {'Department': 'Finance'}
    instance_configuration_id: ocid1.instanceconfiguration.oc1..&lt;unique_ID&gt;
    placement_configurations:
    - availability_domain: Uocm:PHX-AD-1
      primary_subnet_id: ocid1.subnet.oc1..&lt;regional_subnet_unique_ID&gt;
    size: 15

- name: Update instance_pool
  oci_compute_management_instance_pool:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: autoscaling-instance-pool
    instance_pool_id: ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete instance_pool
  oci_compute_management_instance_pool:
    instance_pool_id: ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete instance_pool using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_management_instance_pool:
    compartment_id: ocid1.compartment.oc1..&lt;unique_ID&gt;
    display_name: autoscaling-instance-pool
    state: absent

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
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the instance pool.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the instance
                  pool.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - The user-friendly name. Does not have to be unique.
            returned: on success
            type: string
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        instance_configuration_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the instance configuration associated
                  with the instance pool.
            returned: on success
            type: string
            sample: ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of the instance pool.
            returned: on success
            type: string
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
                    type: string
                    sample: Uocm:PHX-AD-1
                primary_subnet_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the primary subnet to place instances.
                    returned: on success
                    type: string
                    sample: ocid1.primarysubnet.oc1..xxxxxxEXAMPLExxxxxx
                secondary_vnic_subnets:
                    description:
                        - The set of secondary VNIC data for instances in the pool.
                    returned: on success
                    type: complex
                    contains:
                        display_name:
                            description:
                                - The display name of the VNIC. This is also use to match against the instance configuration defined
                                  secondary VNIC.
                            returned: on success
                            type: string
                            sample: display_name_example
                        subnet_id:
                            description:
                                - The subnet L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) for the secondary VNIC.
                            returned: on success
                            type: string
                            sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
        size:
            description:
                - The number of instances that should be in the instance pool.
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - "The date and time the instance pool was created, in the format defined by RFC3339.
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        load_balancers:
            description:
                - The load balancers attached to the instance pool.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer attachment.
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                instance_pool_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the instance pool of the load balancer
                          attachment.
                    returned: on success
                    type: string
                    sample: ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx
                load_balancer_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer attached to the instance pool.
                    returned: on success
                    type: string
                    sample: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx
                backend_set_name:
                    description:
                        - The name of the backend set on the load balancer.
                    returned: on success
                    type: string
                    sample: backend_set_name_example
                port:
                    description:
                        - The port value used for the backends.
                    returned: on success
                    type: int
                    sample: 56
                vnic_selection:
                    description:
                        - "Indicates which VNIC on each instance in the instance pool should be used to associate with the load balancer. Possible values are
                          \\"PrimaryVnic\\" or the displayName of one of the secondary VNICs on the instance configuration that is associated with the instance
                          pool."
                    returned: on success
                    type: string
                    sample: vnic_selection_example
                lifecycle_state:
                    description:
                        - The status of the interaction between the instance pool and the load balancer.
                    returned: on success
                    type: string
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
            "secondary_vnic_subnets": [{
                "display_name": "display_name_example",
                "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        }],
        "size": 56,
        "time_created": "2016-08-25T21:10:29.600Z",
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
    from oci.core import ComputeManagementClient
    from oci.core.models import CreateInstancePoolDetails
    from oci.core.models import UpdateInstancePoolDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstancePoolHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def list_resources(self):
        required_list_method_params = [
            "compartment_id",
        ]

        optional_list_method_params = [
            "display_name",
        ]

        required_kwargs = dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

        return oci_common_utils.list_all_resources(
            self.client.list_instance_pools, **kwargs
        )

    def get_create_model_class(self):
        return CreateInstancePoolDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_instance_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(create_instance_pool_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateInstancePoolDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_instance_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_pool_id=self.module.params.get("instance_pool_id"),
                update_instance_pool_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.terminate_instance_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_pool_id=self.module.params.get("instance_pool_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or self.get_resource_terminated_states(),
        )


InstancePoolHelperCustom = get_custom_class("InstancePoolHelperCustom")


class ResourceHelper(InstancePoolHelperCustom, InstancePoolHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            instance_configuration_id=dict(type="str"),
            placement_configurations=dict(
                type="list",
                elements="dict",
                options=dict(
                    availability_domain=dict(type="str", required=True),
                    primary_subnet_id=dict(type="str", required=True),
                    secondary_vnic_subnets=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            display_name=dict(aliases=["name"], type="str"),
                            subnet_id=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            size=dict(type="int"),
            load_balancers=dict(
                type="list",
                elements="dict",
                options=dict(
                    load_balancer_id=dict(type="str", required=True),
                    backend_set_name=dict(type="str", required=True),
                    port=dict(type="int", required=True),
                    vnic_selection=dict(type="str", required=True),
                ),
            ),
            instance_pool_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="instance_pool",
        service_client_class=ComputeManagementClient,
        namespace="core",
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
