#!/usr/bin/python
# Copyright (c) 2017, 2019 Oracle and/or its affiliates.
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
module: oci_network_security_group
short_description: Manage a NetworkSecurityGroup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a NetworkSecurityGroup resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new network security group for the specified VCN.
version_added: "2.5"
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to contain the
              network security group.
            - Required for create using I(state=present).
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    display_name:
        description:
            - A user-friendly name for the network security group. Does not have to be unique.
              Avoid entering confidential information.
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN to create the network
              security group in.
            - Required for create using I(state=present).
    network_security_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security group.
            - Required for update using I(state=present), I(state=absent).
        aliases: ["id"]
    state:
        description:
            - The state of the NetworkSecurityGroup.
            - Use I(state=present) to create or update a NetworkSecurityGroup.
            - Use I(state=absent) to delete a NetworkSecurityGroup.
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
- name: Create network_security_group
  oci_network_security_group:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    vcn_id: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx

- name: Update network_security_group
  oci_network_security_group:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    network_security_group_id: ocid1.networksecuritygroup.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete network_security_group
  oci_network_security_group:
    network_security_group_id: ocid1.networksecuritygroup.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
network_security_group:
    description:
        - Details of the NetworkSecurityGroup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment the network security group is in.
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
                - A user-friendly name. Does not have to be unique.
                  Avoid entering confidential information.
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
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security group.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The network security group's current state.
            returned: on success
            type: string
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the network security group was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security group's VCN.
            returned: on success
            type: string
            sample: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "time_created": "2016-08-25T21:10:29.600Z",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateNetworkSecurityGroupDetails
    from oci.core.models import UpdateNetworkSecurityGroupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkSecurityGroupHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    @staticmethod
    def get_module_resource_id_param():
        return "network_security_group_id"

    def get_module_resource_id(self):
        return self.module.params.get("network_security_group_id")

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_network_security_group,
            network_security_group_id=self.module.params.get(
                "network_security_group_id"
            ),
        )

    def list_resources(self):
        required_list_method_params = ["compartment_id"]

        optional_list_method_params = ["vcn_id", "display_name"]

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
            self.client.list_network_security_groups, **kwargs
        )

    def get_create_model_class(self):
        return CreateNetworkSecurityGroupDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_common_utils.call_with_backoff(
            self.client.create_network_security_group,
            create_network_security_group_details=create_details,
        )

    def get_update_model_class(self):
        return UpdateNetworkSecurityGroupDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_common_utils.call_with_backoff(
            self.client.update_network_security_group,
            network_security_group_id=self.module.params.get(
                "network_security_group_id"
            ),
            update_network_security_group_details=update_details,
        )

    def delete_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.delete_network_security_group,
            network_security_group_id=self.module.params.get(
                "network_security_group_id"
            ),
        )


NetworkSecurityGroupHelperCustom = get_custom_class("NetworkSecurityGroupHelperCustom")


class ResourceHelper(NetworkSecurityGroupHelperCustom, NetworkSecurityGroupHelperGen):
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
            vcn_id=dict(type="str"),
            network_security_group_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="network_security_group",
        service_client_class=VirtualNetworkClient,
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
