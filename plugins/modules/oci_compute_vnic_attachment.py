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
module: oci_compute_vnic_attachment
short_description: Manage a VnicAttachment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a VnicAttachment resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a secondary VNIC and attaches it to the specified instance.
      For more information about secondary VNICs, see
      L(Virtual Network Interface Cards (VNICs),https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    create_vnic_details:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            assign_public_ip:
                description:
                    - Whether the VNIC should be assigned a public IP address. Defaults to whether
                      the subnet is public or private. If not set and the VNIC is being created
                      in a private subnet (that is, where `prohibitPublicIpOnVnic` = true in the
                      L(Subnet,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Subnet/)), then no public IP address is assigned.
                      If not set and the subnet is public (`prohibitPublicIpOnVnic` = false), then
                      a public IP address is assigned. If set to true and
                      `prohibitPublicIpOnVnic` = true, an error is returned.
                    - "**Note:** This public IP address is associated with the primary private IP
                      on the VNIC. For more information, see
                      L(IP Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm)."
                    - "**Note:** There's a limit to the number of L(public IPs,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PublicIp/)
                      a VNIC or instance can have. If you try to create a secondary VNIC
                      with an assigned public IP for an instance that has already
                      reached its public IP limit, an error is returned. For information
                      about the public IP limits, see
                      L(Public IP Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm)."
                    - "Example: `false`"
                    - If you specify a `vlanId`, then `assignPublicIp` must be set to false. See
                      L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                type: bool
            assign_private_dns_record:
                description:
                    - Whether the VNIC should be assigned a DNS record. If set to false, there will be no DNS record
                      registration for the VNIC. If set to true, the DNS record will be registered. The default
                      value is true.
                    - If you specify a `hostnameLabel`, then `assignPrivateDnsRecord` must be set to true.
                type: bool
            defined_tags:
                description:
                    - Defined tags for this resource. Each key is predefined and scoped to a
                      namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                    - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                type: dict
            display_name:
                description:
                    - A user-friendly name. Does not have to be unique, and it's changeable.
                      Avoid entering confidential information.
                type: str
                aliases: ["name"]
            freeform_tags:
                description:
                    - Free-form tags for this resource. Each tag is a simple key-value pair with no
                      predefined name, type, or namespace. For more information, see L(Resource
                      Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                    - "Example: `{\\"Department\\": \\"Finance\\"}`"
                type: dict
            hostname_label:
                description:
                    - The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
                      portion of the primary private IP's fully qualified domain name (FQDN)
                      (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
                      Must be unique across all VNICs in the subnet and comply with
                      L(RFC 952,https://tools.ietf.org/html/rfc952) and
                      L(RFC 1123,https://tools.ietf.org/html/rfc1123).
                      The value appears in the L(Vnic,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vnic/) object and also the
                      L(PrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/) object returned by
                      L(ListPrivateIps,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/ListPrivateIps) and
                      L(GetPrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/GetPrivateIp).
                    - For more information, see
                      L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm).
                    - When launching an instance, use this `hostnameLabel` instead
                      of the deprecated `hostnameLabel` in
                      L(LaunchInstanceDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/requests/LaunchInstanceDetails).
                      If you provide both, the values must match.
                    - "Example: `bminstance-1`"
                    - If you specify a `vlanId`, the `hostnameLabel` cannot be specified. VNICs on a VLAN
                      can not be assigned a hostname. See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                type: str
            nsg_ids:
                description:
                    - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more
                      information about NSGs, see
                      L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
                    - If a `vlanId` is specified, the `nsgIds` cannot be specified. The `vlanId`
                      indicates that the VNIC will belong to a VLAN instead of a subnet. With VLANs,
                      all VNICs in the VLAN belong to the NSGs that are associated with the VLAN.
                      See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                type: list
                elements: str
            private_ip:
                description:
                    - "A private IP address of your choice to assign to the VNIC. Must be an
                      available IP address within the subnet's CIDR. If you don't specify a
                      value, Oracle automatically assigns a private IP address from the subnet.
                      This is the VNIC's *primary* private IP address. The value appears in
                      the L(Vnic,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vnic/) object and also the
                      L(PrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/) object returned by
                      L(ListPrivateIps,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/ListPrivateIps) and
                      L(GetPrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/GetPrivateIp)."
                    - If you specify a `vlanId`, the `privateIp` cannot be specified.
                      See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                    - "Example: `10.0.3.3`"
                type: str
            skip_source_dest_check:
                description:
                    - Whether the source/destination check is disabled on the VNIC.
                      Defaults to `false`, which means the check is performed. For information
                      about why you would skip the source/destination check, see
                      L(Using a Private IP as a Route Target,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip).
                    - If you specify a `vlanId`, the `skipSourceDestCheck` cannot be specified because the
                      source/destination check is always disabled for VNICs in a VLAN. See
                      L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                    - "Example: `true`"
                type: bool
            subnet_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet to create the VNIC in. When
                      launching an instance,
                      use this `subnetId` instead of the deprecated `subnetId` in
                      L(LaunchInstanceDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/requests/LaunchInstanceDetails).
                      At least one of them is required; if you provide both, the values must match.
                    - If you are an Oracle Cloud VMware Solution customer and creating a secondary
                      VNIC in a VLAN instead of a subnet, provide a `vlanId` instead of a `subnetId`.
                      If you provide both a `vlanId` and `subnetId`, the request fails.
                type: str
            vlan_id:
                description:
                    - Provide this attribute only if you are an Oracle Cloud VMware Solution
                      customer and creating a secondary VNIC in a VLAN. The value is the
                      L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.
                      See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                    - Provide a `vlanId` instead of a `subnetId`. If you provide both a
                      `vlanId` and `subnetId`, the request fails.
                type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    instance_id:
        description:
            - The OCID of the instance.
            - Required for create using I(state=present).
        type: str
    nic_index:
        description:
            - Which physical network interface card (NIC) the VNIC will use. Defaults to 0.
              Certain bare metal instance shapes have two active physical NICs (0 and 1). If
              you add a secondary VNIC to one of these instances, you can specify which NIC
              the VNIC will use. For more information, see
              L(Virtual Network Interface Cards (VNICs),https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).
        type: int
    vnic_attachment_id:
        description:
            - The OCID of the VNIC attachment.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the VnicAttachment.
            - Use I(state=present) to create a VnicAttachment.
            - Use I(state=absent) to delete a VnicAttachment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create vnic_attachment
  oci_compute_vnic_attachment:
    # required
    create_vnic_details:
      # optional
      assign_public_ip: true
      assign_private_dns_record: true
      defined_tags: {'Operations': {'CostCenter': 'US'}}
      display_name: display_name_example
      freeform_tags: {'Department': 'Finance'}
      hostname_label: hostname_label_example
      nsg_ids: [ "nsg_ids_example" ]
      private_ip: private_ip_example
      skip_source_dest_check: true
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
      vlan_id: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    nic_index: 56

- name: Delete vnic_attachment
  oci_compute_vnic_attachment:
    # required
    vnic_attachment_id: "ocid1.vnicattachment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete vnic_attachment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_vnic_attachment:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
vnic_attachment:
    description:
        - Details of the VnicAttachment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain of the instance.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment the VNIC attachment is in, which is the same
                  compartment the instance is in.
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
        id:
            description:
                - The OCID of the VNIC attachment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        instance_id:
            description:
                - The OCID of the instance.
            returned: on success
            type: str
            sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the VNIC attachment.
            returned: on success
            type: str
            sample: ATTACHING
        nic_index:
            description:
                - Which physical network interface card (NIC) the VNIC uses.
                  Certain bare metal instance shapes have two active physical NICs (0 and 1). If
                  you add a secondary VNIC to one of these instances, you can specify which NIC
                  the VNIC will use. For more information, see
                  L(Virtual Network Interface Cards (VNICs),https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).
            returned: on success
            type: int
            sample: 56
        subnet_id:
            description:
                - The OCID of the subnet to create the VNIC in.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        vlan_id:
            description:
                - The OCID of the VLAN to create the VNIC in. Creating the VNIC in a VLAN (instead
                  of a subnet) is possible only if you are an Oracle Cloud VMware Solution customer.
                  See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                - An error is returned if the instance already has a VNIC attached to it from this VLAN.
            returned: on success
            type: str
            sample: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the VNIC attachment was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vlan_tag:
            description:
                - The Oracle-assigned VLAN tag of the attached VNIC. Available after the
                  attachment process is complete.
                - However, if the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution,
                  the `vlanTag` value is instead the value of the `vlanTag` attribute for the VLAN.
                  See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                - "Example: `0`"
            returned: on success
            type: int
            sample: 56
        vnic_id:
            description:
                - The OCID of the VNIC. Available after the attachment process is complete.
            returned: on success
            type: str
            sample: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ATTACHING",
        "nic_index": 56,
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "vlan_id": "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "vlan_tag": 56,
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
    from oci.core import ComputeClient
    from oci.core.models import AttachVnicDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VnicAttachmentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_possible_entity_types(self):
        return super(VnicAttachmentHelperGen, self).get_possible_entity_types() + [
            "vnicattachment",
            "vnicattachments",
            "corevnicattachment",
            "corevnicattachments",
            "vnicattachmentresource",
            "vnicattachmentsresource",
            "core",
        ]

    def get_module_resource_id_param(self):
        return "vnic_attachment_id"

    def get_module_resource_id(self):
        return self.module.params.get("vnic_attachment_id")

    def get_get_fn(self):
        return self.client.get_vnic_attachment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vnic_attachment,
            vnic_attachment_id=self.module.params.get("vnic_attachment_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["instance_id"]

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
            self.client.list_vnic_attachments, **kwargs
        )

    def get_create_model_class(self):
        return AttachVnicDetails

    def get_exclude_attributes(self):
        return ["create_vnic_details"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_vnic,
            call_fn_args=(),
            call_fn_kwargs=dict(attach_vnic_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_vnic,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vnic_attachment_id=self.module.params.get("vnic_attachment_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


VnicAttachmentHelperCustom = get_custom_class("VnicAttachmentHelperCustom")


class ResourceHelper(VnicAttachmentHelperCustom, VnicAttachmentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            create_vnic_details=dict(
                type="dict",
                options=dict(
                    assign_public_ip=dict(type="bool"),
                    assign_private_dns_record=dict(type="bool"),
                    defined_tags=dict(type="dict"),
                    display_name=dict(aliases=["name"], type="str"),
                    freeform_tags=dict(type="dict"),
                    hostname_label=dict(type="str"),
                    nsg_ids=dict(type="list", elements="str"),
                    private_ip=dict(type="str"),
                    skip_source_dest_check=dict(type="bool"),
                    subnet_id=dict(type="str"),
                    vlan_id=dict(type="str"),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            instance_id=dict(type="str"),
            nic_index=dict(type="int"),
            vnic_attachment_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vnic_attachment",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
