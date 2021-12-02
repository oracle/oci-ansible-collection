#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_compute_management_instance_pool_instance
short_description: Manage an InstancePoolInstance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create an InstancePoolInstance resource in Oracle Cloud Infrastructure
    - For I(state=present), attaches an instance to an instance pool. For information about the prerequisites
      that an instance must meet before you can attach it to a pool, see
      L(Attaching an Instance to an Instance Pool,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/updatinginstancepool.htm#attach-instance).
    - "This resource has the following action operations in the M(oracle.oci.oci_compute_management_instance_pool_instance_actions) module: detach."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    instance_pool_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.
        type: str
        required: true
    instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    state:
        description:
            - The state of the InstancePoolInstance.
            - Use I(state=present) to create an InstancePoolInstance.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create instance_pool_instance
  oci_compute_management_instance_pool_instance:
    # required
    instance_pool_id: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
instance_pool_instance:
    description:
        - Details of the InstancePoolInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        instance_pool_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.
            returned: on success
            type: str
            sample: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
        availability_domain:
            description:
                - The availability domain the instance is running in.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        lifecycle_state:
            description:
                - The attachment state of the instance in relation to the instance pool.
            returned: on success
            type: str
            sample: ATTACHING
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the
                  instance.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        fault_domain:
            description:
                - The fault domain the instance is running in.
            returned: on success
            type: str
            sample: fault_domain_example
        instance_configuration_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance configuration
                  used to create the instance.
            returned: on success
            type: str
            sample: "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
        region:
            description:
                - The region that contains the availability domain the instance is running in.
            returned: on success
            type: str
            sample: region_example
        shape:
            description:
                - The shape of the instance. The shape determines the number of CPUs, amount of memory,
                  and other resources allocated to the instance.
            returned: on success
            type: str
            sample: shape_example
        state:
            description:
                - The lifecycle state of the instance. Refer to `lifecycleState` in the L(Instance,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/iaas/latest/Instance) resource.
            returned: on success
            type: str
            sample: state_example
        time_created:
            description:
                - "The date and time the instance pool instance was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        load_balancer_backends:
            description:
                - The load balancer backends that are configured for the instance.
            returned: on success
            type: complex
            contains:
                load_balancer_id:
                    description:
                        - The OCID of the load balancer attached to the instance pool.
                    returned: on success
                    type: str
                    sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                backend_set_name:
                    description:
                        - The name of the backend set on the load balancer.
                    returned: on success
                    type: str
                    sample: backend_set_name_example
                backend_name:
                    description:
                        - The name of the backend in the backend set.
                    returned: on success
                    type: str
                    sample: backend_name_example
                backend_health_status:
                    description:
                        - The health of the backend as observed by the load balancer.
                    returned: on success
                    type: str
                    sample: OK
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_pool_id": "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_domain": "Uocm:PHX-AD-1",
        "lifecycle_state": "ATTACHING",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "fault_domain": "fault_domain_example",
        "instance_configuration_id": "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx",
        "region": "region_example",
        "shape": "shape_example",
        "state": "state_example",
        "time_created": "2016-08-25T21:10:29.600Z",
        "load_balancer_backends": [{
            "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
            "backend_set_name": "backend_set_name_example",
            "backend_name": "backend_name_example",
            "backend_health_status": "OK"
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
    from oci.work_requests import WorkRequestClient
    from oci.core import ComputeManagementClient
    from oci.core.models import AttachInstancePoolInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstancePoolInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get and list"""

    def __init__(self, *args, **kwargs):
        super(InstancePoolInstanceHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_get_fn(self):
        return self.client.get_instance_pool_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_pool_instance,
            instance_pool_id=self.module.params.get("instance_pool_id"),
            instance_id=self.module.params.get("instance_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "instance_pool_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_instance_pool_instances, **kwargs
        )

    def get_create_model_class(self):
        return AttachInstancePoolInstanceDetails

    def get_exclude_attributes(self):
        return ["instance_id"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_instance_pool_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_pool_id=self.module.params.get("instance_pool_id"),
                attach_instance_pool_instance_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


InstancePoolInstanceHelperCustom = get_custom_class("InstancePoolInstanceHelperCustom")


class ResourceHelper(InstancePoolInstanceHelperCustom, InstancePoolInstanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            instance_pool_id=dict(type="str", required=True),
            instance_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="instance_pool_instance",
        service_client_class=ComputeManagementClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
