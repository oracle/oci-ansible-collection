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
module: oci_compute_dedicated_vm_host_facts
short_description: Fetches details about one or multiple DedicatedVmHost resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DedicatedVmHost resources in Oracle Cloud Infrastructure
    - Returns the list of dedicated virtual machine hosts that match the specified criteria in the specified compartment.
    - You can limit the list by specifying a dedicated virtual machine host display name. The list will include all the identically-named
      dedicated virtual machine hosts in the compartment.
    - If I(dedicated_vm_host_id) is specified, the details of a single DedicatedVmHost will be returned.
version_added: "2.5"
options:
    dedicated_vm_host_id:
        description:
            - The OCID of the dedicated VM host.
            - Required to get a specific dedicated_vm_host.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple dedicated_vm_hosts.
        type: str
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
        type: str
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    instance_shape_name:
        description:
            - The name for the instance's shape.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List dedicated_vm_hosts
  oci_compute_dedicated_vm_host_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific dedicated_vm_host
  oci_compute_dedicated_vm_host_facts:
    dedicated_vm_host_id: ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
dedicated_vm_hosts:
    description:
        - List of DedicatedVmHost resources
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
                - The date and time the dedicated VM host was created, in the format defined by RFC3339.
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
    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DedicatedVmHostFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "dedicated_vm_host_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dedicated_vm_host,
            dedicated_vm_host_id=self.module.params.get("dedicated_vm_host_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "availability_domain",
            "lifecycle_state",
            "display_name",
            "instance_shape_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_dedicated_vm_hosts,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DedicatedVmHostFactsHelperCustom = get_custom_class("DedicatedVmHostFactsHelperCustom")


class ResourceFactsHelper(
    DedicatedVmHostFactsHelperCustom, DedicatedVmHostFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dedicated_vm_host_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            availability_domain=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            instance_shape_name=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="dedicated_vm_host",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(dedicated_vm_hosts=result)


if __name__ == "__main__":
    main()
