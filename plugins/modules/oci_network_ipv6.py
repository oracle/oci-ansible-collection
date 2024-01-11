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
module: oci_network_ipv6
short_description: Manage an Ipv6 resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an Ipv6 resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an IPv6 for the specified VNIC.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ip_address:
        description:
            - An IPv6 address of your choice. Must be an available IP address within
              the subnet's CIDR. If you don't specify a value, Oracle automatically
              assigns an IPv6 address from the subnet. The subnet is the one that
              contains the VNIC you specify in `vnicId`.
            - "Example: `2001:DB8::`"
        type: str
    ipv6_subnet_cidr:
        description:
            - The IPv6 prefix allocated to the subnet. This is required if more than one IPv6 prefix exists on the subnet.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    vnic_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VNIC to assign the IPv6 to. The
              IPv6 will be in the VNIC's subnet.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    ipv6_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the IPv6.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Ipv6.
            - Use I(state=present) to create or update an Ipv6.
            - Use I(state=absent) to delete an Ipv6.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create ipv6
  oci_network_ipv6:
    # required
    vnic_id: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    ip_address: ip_address_example
    ipv6_subnet_cidr: ipv6_subnet_cidr_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}

- name: Update ipv6
  oci_network_ipv6:
    # required
    ipv6_id: "ocid1.ipv6.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    vnic_id: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update ipv6 using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_ipv6:
    # required
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    vnic_id: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete ipv6
  oci_network_ipv6:
    # required
    ipv6_id: "ocid1.ipv6.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete ipv6 using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_ipv6:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
ipv6:
    description:
        - Details of the Ipv6 resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the IPv6.
                  This is the same as the VNIC's compartment.
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
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the IPv6.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        ip_address:
            description:
                - The IPv6 address of the `IPv6` object. The address is within the IPv6 prefix of the VNIC's subnet
                  (see the `ipv6CidrBlock` attribute for the L(Subnet,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Subnet/) object.
                - "Example: `2001:0db8:0123:1111:abcd:ef01:2345:6789`"
            returned: on success
            type: str
            sample: ip_address_example
        lifecycle_state:
            description:
                - The IPv6's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet the VNIC is in.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the IPv6 was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vnic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VNIC the IPv6 is assigned to.
                  The VNIC and IPv6 must be in the same subnet.
            returned: on success
            type: str
            sample: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "ip_address": "ip_address_example",
        "lifecycle_state": "PROVISIONING",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "vnic_id": "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateIpv6Details
    from oci.core.models import UpdateIpv6Details

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class Ipv6HelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(Ipv6HelperGen, self).get_possible_entity_types() + [
            "ipv6",
            "ipv6s",
            "coreipv6",
            "coreipv6s",
            "ipv6resource",
            "ipv6sresource",
            "core",
        ]

    def get_module_resource_id_param(self):
        return "ipv6_id"

    def get_module_resource_id(self):
        return self.module.params.get("ipv6_id")

    def get_get_fn(self):
        return self.client.get_ipv6

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ipv6, ipv6_id=self.module.params.get("ipv6_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["ip_address"]
            if self._use_name_as_identifier()
            else ["ip_address", "vnic_id"]
        )

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
        return oci_common_utils.list_all_resources(self.client.list_ipv6s, **kwargs)

    def get_create_model_class(self):
        return CreateIpv6Details

    def get_exclude_attributes(self):
        return ["ipv6_subnet_cidr"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_ipv6,
            call_fn_args=(),
            call_fn_kwargs=dict(create_ipv6_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateIpv6Details

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_ipv6,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ipv6_id=self.module.params.get("ipv6_id"),
                update_ipv6_details=update_details,
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
            call_fn=self.client.delete_ipv6,
            call_fn_args=(),
            call_fn_kwargs=dict(ipv6_id=self.module.params.get("ipv6_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


Ipv6HelperCustom = get_custom_class("Ipv6HelperCustom")


class ResourceHelper(Ipv6HelperCustom, Ipv6HelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            ip_address=dict(type="str"),
            ipv6_subnet_cidr=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            vnic_id=dict(type="str"),
            ipv6_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ipv6",
        service_client_class=VirtualNetworkClient,
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
