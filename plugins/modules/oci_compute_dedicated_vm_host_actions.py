#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_compute_dedicated_vm_host_actions
short_description: Perform actions on a DedicatedVmHost resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DedicatedVmHost resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a dedicated virtual machine host from one compartment to another.
version_added: "2.9"
author: Oracle (@oracle)
options:
    dedicated_vm_host_id:
        description:
            - The OCID of the dedicated VM host.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment
              to move the dedicated virtual machine host to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the DedicatedVmHost.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on dedicated_vm_host
  oci_compute_dedicated_vm_host_actions:
    dedicated_vm_host_id: "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
dedicated_vm_host:
    description:
        - Details of the DedicatedVmHost resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain the dedicated virtual machine host is running in.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment that contains the dedicated virtual machine host.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        dedicated_vm_host_shape:
            description:
                - The dedicated virtual machine host shape. The shape determines the number of CPUs and
                  other resources available for VMs.
            returned: on success
            type: string
            sample: dedicated_vm_host_shape_example
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
                - "Example: `My Dedicated Vm Host`"
            returned: on success
            type: string
            sample: My Dedicated Vm Host
        fault_domain:
            description:
                - The fault domain for the dedicated virtual machine host's assigned instances.
                  For more information, see L(Fault Domains,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm#fault).
                - If you do not specify the fault domain, the system selects one for you. To change the fault domain for a dedicated virtual machine host,
                  delete it, and then create a new dedicated virtual machine host in the preferred fault domain.
                - To get a list of fault domains, use the `ListFaultDomains` operation in the L(Identity and Access Management Service
                  API,https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/).
                - "Example: `FAULT-DOMAIN-1`"
            returned: on success
            type: string
            sample: FAULT-DOMAIN-1
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the dedicated VM host.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the dedicated VM host.
            returned: on success
            type: string
            sample: CREATING
        time_created:
            description:
                - The date and time the dedicated VM host was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        total_ocpus:
            description:
                - The total OCPUs of the dedicated VM host.
            returned: on success
            type: float
            sample: 3.4
        remaining_ocpus:
            description:
                - The available OCPUs of the dedicated VM host.
            returned: on success
            type: float
            sample: 3.4
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "dedicated_vm_host_shape": "dedicated_vm_host_shape_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "My Dedicated Vm Host",
        "fault_domain": "FAULT-DOMAIN-1",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2016-08-25T21:10:29.600Z",
        "total_ocpus": 3.4,
        "remaining_ocpus": 3.4
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.core import ComputeClient
    from oci.core.models import ChangeDedicatedVmHostCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DedicatedVmHostActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    def __init__(self, *args, **kwargs):
        super(DedicatedVmHostActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "dedicated_vm_host_id"

    def get_module_resource_id(self):
        return self.module.params.get("dedicated_vm_host_id")

    def get_get_fn(self):
        return self.client.get_dedicated_vm_host

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dedicated_vm_host,
            dedicated_vm_host_id=self.module.params.get("dedicated_vm_host_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDedicatedVmHostCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_dedicated_vm_host_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dedicated_vm_host_id=self.module.params.get("dedicated_vm_host_id"),
                change_dedicated_vm_host_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DedicatedVmHostActionsHelperCustom = get_custom_class(
    "DedicatedVmHostActionsHelperCustom"
)


class ResourceHelper(
    DedicatedVmHostActionsHelperCustom, DedicatedVmHostActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            dedicated_vm_host_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="dedicated_vm_host",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
