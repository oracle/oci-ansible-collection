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
module: oci_compute_dedicated_vm_host
short_description: Manage a DedicatedVmHost resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DedicatedVmHost resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new dedicated virtual machine host in the specified compartment and the specified availability domain.
      Dedicated virtual machine hosts enable you to run your Compute virtual machine (VM) instances on dedicated servers
      that are a single tenant and not shared with other customers.
      For more information, see L(Dedicated Virtual Machine Hosts,https://docs.cloud.oracle.com/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm).
version_added: "2.9"
author: Oracle (@oracle)
options:
    availability_domain:
        description:
            - The availability domain of the dedicated virtual machine host.
            - "Example: `Uocm:PHX-AD-1`"
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    dedicated_vm_host_shape:
        description:
            - The dedicated virtual machine host shape. The shape determines the number of CPUs and
              other resources available for VM instances launched on the dedicated virtual machine host.
            - Required for create using I(state=present).
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - "Example: `My dedicated VM host`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    fault_domain:
        description:
            - The fault domain for the dedicated virtual machine host's assigned instances.
              For more information, see L(Fault Domains,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm#fault).
              If you do not specify the fault domain, the system selects one for you. To change the fault domain for a dedicated virtual machine host,
              delete it and create a new dedicated virtual machine host in the preferred fault domain.
            - To get a list of fault domains, use the `ListFaultDomains` operation in
              the L(Identity and Access Management Service API,https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/).
            - "Example: `FAULT-DOMAIN-1`"
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    dedicated_vm_host_id:
        description:
            - The OCID of the dedicated VM host.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DedicatedVmHost.
            - Use I(state=present) to create or update a DedicatedVmHost.
            - Use I(state=absent) to delete a DedicatedVmHost.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create dedicated_vm_host
  oci_compute_dedicated_vm_host:
    availability_domain: Uocm:PHX-AD-1
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    dedicated_vm_host_shape: dedicated_vm_host_shape_example

- name: Update dedicated_vm_host using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_dedicated_vm_host:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: My dedicated VM host
    freeform_tags: {'Department': 'Finance'}

- name: Update dedicated_vm_host
  oci_compute_dedicated_vm_host:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: My dedicated VM host
    dedicated_vm_host_id: ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete dedicated_vm_host
  oci_compute_dedicated_vm_host:
    dedicated_vm_host_id: ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete dedicated_vm_host using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_dedicated_vm_host:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    display_name: My dedicated VM host
    state: absent

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
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
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
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
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
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of the dedicated VM host.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.core import ComputeClient
    from oci.core.models import CreateDedicatedVmHostDetails
    from oci.core.models import UpdateDedicatedVmHostDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DedicatedVmHostHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(DedicatedVmHostHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["availability_domain", "display_name"]

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
            self.client.list_dedicated_vm_hosts, **kwargs
        )

    def get_create_model_class(self):
        return CreateDedicatedVmHostDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_dedicated_vm_host,
            call_fn_args=(),
            call_fn_kwargs=dict(create_dedicated_vm_host_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDedicatedVmHostDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_dedicated_vm_host,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dedicated_vm_host_id=self.module.params.get("dedicated_vm_host_id"),
                update_dedicated_vm_host_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_dedicated_vm_host,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dedicated_vm_host_id=self.module.params.get("dedicated_vm_host_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DedicatedVmHostHelperCustom = get_custom_class("DedicatedVmHostHelperCustom")


class ResourceHelper(DedicatedVmHostHelperCustom, DedicatedVmHostHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            availability_domain=dict(type="str"),
            compartment_id=dict(type="str"),
            dedicated_vm_host_shape=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            fault_domain=dict(type="str"),
            freeform_tags=dict(type="dict"),
            dedicated_vm_host_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
