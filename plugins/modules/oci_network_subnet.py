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
module: oci_network_subnet
short_description: Manage a Subnet resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Subnet resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new subnet in the specified VCN. You can't change the size of the subnet after creation,
      so it's important to think about the size of subnets you need before creating them.
      For more information, see L(VCNs and Subnets,https://docs.cloud.oracle.com/Content/Network/Tasks/managingVCNs.htm).
      For information on the number of subnets you can have in a VCN, see
      L(Service Limits,https://docs.cloud.oracle.com/Content/General/Concepts/servicelimits.htm).
    - For the purposes of access control, you must provide the OCID of the compartment where you want the subnet
      to reside. Notice that the subnet doesn't have to be in the same compartment as the VCN, route tables, or
      other Networking Service components. If you're not sure which compartment to use, put the subnet in
      the same compartment as the VCN. For more information about compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm). For information about OCIDs,
      see L(Resource Identifiers,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
    - You may optionally associate a route table with the subnet. If you don't, the subnet will use the
      VCN's default route table. For more information about route tables, see
      L(Route Tables,https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm).
    - You may optionally associate a security list with the subnet. If you don't, the subnet will use the
      VCN's default security list. For more information about security lists, see
      L(Security Lists,https://docs.cloud.oracle.com/Content/Network/Concepts/securitylists.htm).
    - You may optionally associate a set of DHCP options with the subnet. If you don't, the subnet will use the
      VCN's default set. For more information about DHCP options, see
      L(DHCP Options,https://docs.cloud.oracle.com/Content/Network/Tasks/managingDHCP.htm).
    - "You may optionally specify a *display name* for the subnet, otherwise a default is provided.
      It does not have to be unique, and you can change it. Avoid entering confidential information."
    - You can also add a DNS label for the subnet, which is required if you want the Internet and
      VCN Resolver to resolve hostnames for instances in the subnet. For more information, see
      L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
version_added: "2.9"
author: Oracle (@oracle)
options:
    availability_domain:
        description:
            - Controls whether the subnet is regional or specific to an availability domain. Oracle
              recommends creating regional subnets because they're more flexible and make it easier to
              implement failover across availability domains. Originally, AD-specific subnets were the
              only kind available to use.
            - To create a regional subnet, omit this attribute. Then any resources later created in this
              subnet (such as a Compute instance) can be created in any availability domain in the region.
            - To instead create an AD-specific subnet, set this attribute to the availability domain you
              want this subnet to be in. Then any resources later created in this subnet can only be
              created in that availability domain.
            - "Example: `Uocm:PHX-AD-1`"
        type: str
    cidr_block:
        description:
            - The CIDR IP address range of the subnet. The CIDR must maintain the following rules -
            - a. The CIDR block is valid and correctly formatted.
              b. The new range is within one of the parent VCN ranges.
            - "Example: `10.0.1.0/24`"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment to contain the subnet.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    dhcp_options_id:
        description:
            - The OCID of the set of DHCP options the subnet will use. If you don't
              provide a value, the subnet uses the VCN's default set of DHCP options.
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    dns_label:
        description:
            - A DNS label for the subnet, used in conjunction with the VNIC's hostname and
              VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC
              within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`).
              Must be an alphanumeric string that begins with a letter and is unique within the VCN.
              The value cannot be changed.
            - This value must be set if you want to use the Internet and VCN Resolver to resolve the
              hostnames of instances in the subnet. It can only be set if the VCN itself
              was created with a DNS label.
            - For more information, see
              L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
            - "Example: `subnet123`"
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    prohibit_public_ip_on_vnic:
        description:
            - Whether VNICs within this subnet can have public IP addresses.
              Defaults to false, which means VNICs created in this subnet will
              automatically be assigned public IP addresses unless specified
              otherwise during instance launch or VNIC creation (with the
              `assignPublicIp` flag in L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/)).
              If `prohibitPublicIpOnVnic` is set to true, VNICs created in this
              subnet cannot have public IP addresses (that is, it's a private
              subnet).
            - "Example: `true`"
        type: bool
    route_table_id:
        description:
            - The OCID of the route table the subnet will use. If you don't provide a value,
              the subnet uses the VCN's default route table.
            - This parameter is updatable.
        type: str
    security_list_ids:
        description:
            - "The OCIDs of the security list or lists the subnet will use. If you don't
              provide a value, the subnet uses the VCN's default security list.
              Remember that security lists are associated *with the subnet*, but the
              rules are applied to the individual VNICs in the subnet."
            - This parameter is updatable.
        type: list
    vcn_id:
        description:
            - The OCID of the VCN to contain the subnet.
            - Required for create using I(state=present).
        type: str
    subnet_id:
        description:
            - The OCID of the subnet.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Subnet.
            - Use I(state=present) to create or update a Subnet.
            - Use I(state=absent) to delete a Subnet.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create subnet
  oci_network_subnet:
    display_name: MySubnet
    cidr_block: 10.0.2.0/24
    availability_domain: Uocm:PHX-AD-1
    route_table_id: ocid1.routetable.oc1.phx.unique_ID
    security_list_ids:
    - ocid1.securitylist.oc1.phx.unique_ID
    dhcp_options_id: ocid1.dhcpoptions.oc1.phx.unique_ID
    vcn_id: ocid1.vcn.oc1.phx.unique_ID
    compartment_id: ocid1.compartment.oc1..unique_ID

- name: Update subnet using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_subnet:
    cidr_block: 10.0.2.0/24
    compartment_id: ocid1.compartment.oc1..unique_ID
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    dhcp_options_id: ocid1.dhcpoptions.oc1.phx.unique_ID
    display_name: MySubnet
    freeform_tags: {'Department': 'Finance'}
    route_table_id: ocid1.routetable.oc1.phx.unique_ID
    security_list_ids: [ "ocid1.securitylist.oc1.phx.unique_ID" ]

- name: Update subnet
  oci_network_subnet:
    cidr_block: 10.0.2.0/24
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    subnet_id: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete subnet
  oci_network_subnet:
    subnet_id: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete subnet using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_subnet:
    compartment_id: ocid1.compartment.oc1..unique_ID
    display_name: MySubnet
    state: absent

"""

RETURN = """
subnet:
    description:
        - Details of the Subnet resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The subnet's availability domain. This attribute will be null if this is a regional subnet
                  instead of an AD-specific subnet. Oracle recommends creating regional subnets.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        cidr_block:
            description:
                - The subnet's CIDR block.
                - "Example: `10.0.1.0/24`"
            returned: on success
            type: string
            sample: 10.0.1.0/24
        compartment_id:
            description:
                - The OCID of the compartment containing the subnet.
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
        dhcp_options_id:
            description:
                - The OCID of the set of DHCP options that the subnet uses.
            returned: on success
            type: string
            sample: ocid1.dhcpoptions.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        dns_label:
            description:
                - A DNS label for the subnet, used in conjunction with the VNIC's hostname and
                  VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC
                  within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`).
                  Must be an alphanumeric string that begins with a letter and is unique within the VCN.
                  The value cannot be changed.
                - The absence of this parameter means the Internet and VCN Resolver
                  will not resolve hostnames of instances in this subnet.
                - For more information, see
                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
                - "Example: `subnet123`"
            returned: on success
            type: string
            sample: subnet123
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
                - The subnet's Oracle ID (OCID).
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The subnet's current state.
            returned: on success
            type: string
            sample: PROVISIONING
        prohibit_public_ip_on_vnic:
            description:
                - Whether VNICs within this subnet can have public IP addresses.
                  Defaults to false, which means VNICs created in this subnet will
                  automatically be assigned public IP addresses unless specified
                  otherwise during instance launch or VNIC creation (with the
                  `assignPublicIp` flag in
                  L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/)).
                  If `prohibitPublicIpOnVnic` is set to true, VNICs created in this
                  subnet cannot have public IP addresses (that is, it's a private
                  subnet).
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        route_table_id:
            description:
                - The OCID of the route table that the subnet uses.
            returned: on success
            type: string
            sample: ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx
        security_list_ids:
            description:
                - "The OCIDs of the security list or lists that the subnet uses. Remember
                  that security lists are associated *with the subnet*, but the
                  rules are applied to the individual VNICs in the subnet."
            returned: on success
            type: list
            sample: []
        subnet_domain_name:
            description:
                - The subnet's domain name, which consists of the subnet's DNS label,
                  the VCN's DNS label, and the `oraclevcn.com` domain.
                - For more information, see
                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
                - "Example: `subnet123.vcn1.oraclevcn.com`"
            returned: on success
            type: string
            sample: subnet123.vcn1.oraclevcn.com
        time_created:
            description:
                - The date and time the subnet was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vcn_id:
            description:
                - The OCID of the VCN the subnet is in.
            returned: on success
            type: string
            sample: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
        virtual_router_ip:
            description:
                - The IP address of the virtual router.
                - "Example: `10.0.14.1`"
            returned: on success
            type: string
            sample: 10.0.14.1
        virtual_router_mac:
            description:
                - The MAC address of the virtual router.
                - "Example: `00:00:00:00:00:01`"
            returned: on success
            type: string
            sample: 00:00:00:00:00:01
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "cidr_block": "10.0.1.0/24",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "dhcp_options_id": "ocid1.dhcpoptions.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "dns_label": "subnet123",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "prohibit_public_ip_on_vnic": true,
        "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx",
        "security_list_ids": [],
        "subnet_domain_name": "subnet123.vcn1.oraclevcn.com",
        "time_created": "2016-08-25T21:10:29.600Z",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "virtual_router_ip": "10.0.14.1",
        "virtual_router_mac": "00:00:00:00:00:01"
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateSubnetDetails
    from oci.core.models import UpdateSubnetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SubnetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "subnet_id"

    def get_module_resource_id(self):
        return self.module.params.get("subnet_id")

    def get_get_fn(self):
        return self.client.get_subnet

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_subnet, subnet_id=self.module.params.get("subnet_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["vcn_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_subnets, **kwargs)

    def get_create_model_class(self):
        return CreateSubnetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_subnet,
            call_fn_args=(),
            call_fn_kwargs=dict(create_subnet_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateSubnetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_subnet,
            call_fn_args=(),
            call_fn_kwargs=dict(
                subnet_id=self.module.params.get("subnet_id"),
                update_subnet_details=update_details,
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
            call_fn=self.client.delete_subnet,
            call_fn_args=(),
            call_fn_kwargs=dict(subnet_id=self.module.params.get("subnet_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


SubnetHelperCustom = get_custom_class("SubnetHelperCustom")


class ResourceHelper(SubnetHelperCustom, SubnetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            availability_domain=dict(type="str"),
            cidr_block=dict(type="str"),
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            dhcp_options_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            dns_label=dict(type="str"),
            freeform_tags=dict(type="dict"),
            prohibit_public_ip_on_vnic=dict(type="bool"),
            route_table_id=dict(type="str"),
            security_list_ids=dict(type="list"),
            vcn_id=dict(type="str"),
            subnet_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="subnet",
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
