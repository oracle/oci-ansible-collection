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
module: oci_network_vnic
short_description: Manage a Vnic resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a Vnic resource in Oracle Cloud Infrastructure
version_added: "2.9"
author: Oracle (@oracle)
options:
    vnic_id:
        description:
            - The OCID of the VNIC.
        type: str
        aliases: ["id"]
        required: true
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
            - This parameter is updatable.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    hostname_label:
        description:
            - The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
              portion of the primary private IP's fully qualified domain name (FQDN)
              (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
              Must be unique across all VNICs in the subnet and comply with
              L(RFC 952,https://tools.ietf.org/html/rfc952) and
              L(RFC 1123,https://tools.ietf.org/html/rfc1123).
              The value appears in the L(Vnic,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vnic/) object and also the
              L(PrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PrivateIp/) object returned by
              L(ListPrivateIps,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PrivateIp/ListPrivateIps) and
              L(GetPrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PrivateIp/GetPrivateIp).
            - For more information, see
              L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
            - This parameter is updatable.
        type: str
    nsg_ids:
        description:
            - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. Setting this as
              an empty array removes the VNIC from all network security groups.
            - If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
              belonging to a subnet), the value of the `nsgIds` attribute is ignored. Instead, the
              VNIC belongs to the NSGs that are associated with the VLAN itself. See L(Vlan,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/iaas/20160918/Vlan).
            - For more information about NSGs, see
              L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
            - This parameter is updatable.
        type: list
    skip_source_dest_check:
        description:
            - Whether the source/destination check is disabled on the VNIC.
              Defaults to `false`, which means the check is performed. For information about why you would
              skip the source/destination check, see
              L(Using a Private IP as a Route Target,https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm#privateip).
            - "If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
              belonging to a subnet), the value of the `skipSourceDestCheck` attribute is ignored.
              This is because the source/destination check is always disabled for VNICs in a VLAN.
              Example: `true`"
            - This parameter is updatable.
        type: bool
    state:
        description:
            - The state of the Vnic.
            - Use I(state=present) to update an existing a Vnic.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update vnic
  oci_network_vnic:
    vnic_id: ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx
    defined_tags: {'Operations': {'CostCenter': 'US'}}

"""

RETURN = """
vnic:
    description:
        - Details of the Vnic resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The VNIC's availability domain.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment containing the VNIC.
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
        hostname_label:
            description:
                - The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
                  portion of the primary private IP's fully qualified domain name (FQDN)
                  (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
                  Must be unique across all VNICs in the subnet and comply with
                  L(RFC 952,https://tools.ietf.org/html/rfc952) and
                  L(RFC 1123,https://tools.ietf.org/html/rfc1123).
                - For more information, see
                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
                - "Example: `bminstance-1`"
            returned: on success
            type: string
            sample: bminstance-1
        id:
            description:
                - The OCID of the VNIC.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        is_primary:
            description:
                - Whether the VNIC is the primary VNIC (the VNIC that is automatically created
                  and attached during instance launch).
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The current state of the VNIC.
            returned: on success
            type: string
            sample: PROVISIONING
        mac_address:
            description:
                - The MAC address of the VNIC.
                - If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution,
                  the MAC address is learned. If the VNIC belongs to a subnet, the
                  MAC address is a static, Oracle-provided value.
                - "Example: `00:00:00:00:00:01`"
            returned: on success
            type: string
            sample: 00:00:00:00:00:01
        nsg_ids:
            description:
                - A list of the OCIDs of the network security groups that the VNIC belongs to.
                - If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
                  belonging to a subnet), the value of the `nsgIds` attribute is ignored. Instead, the
                  VNIC belongs to the NSGs that are associated with the VLAN itself. See L(Vlan,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/iaas/20160918/Vlan).
                - For more information about NSGs, see
                  L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
            returned: on success
            type: list
            sample: []
        vlan_id:
            description:
                - If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
                  belonging to a subnet), the `vlanId` is the OCID of the VLAN the VNIC is in. See
                  L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vlan). If the VNIC is instead in a subnet, `subnetId` has a value.
            returned: on success
            type: string
            sample: ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx
        private_ip:
            description:
                - The private IP address of the primary `privateIp` object on the VNIC.
                  The address is within the CIDR of the VNIC's subnet.
                - "Example: `10.0.3.3`"
            returned: on success
            type: string
            sample: 10.0.3.3
        public_ip:
            description:
                - The public IP address of the VNIC, if one is assigned.
            returned: on success
            type: string
            sample: public_ip_example
        skip_source_dest_check:
            description:
                - Whether the source/destination check is disabled on the VNIC.
                  Defaults to `false`, which means the check is performed. For information
                  about why you would skip the source/destination check, see
                  L(Using a Private IP as a Route Target,https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm#privateip).
                - If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
                  belonging to a subnet), the `skipSourceDestCheck` attribute is `true`.
                  This is because the source/destination check is always disabled for VNICs in a VLAN.
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        subnet_id:
            description:
                - The OCID of the subnet the VNIC is in.
            returned: on success
            type: string
            sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The date and time the VNIC was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "hostname_label": "bminstance-1",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_primary": true,
        "lifecycle_state": "PROVISIONING",
        "mac_address": "00:00:00:00:00:01",
        "nsg_ids": [],
        "vlan_id": "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx",
        "private_ip": "10.0.3.3",
        "public_ip": "public_ip_example",
        "skip_source_dest_check": true,
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z"
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
    from oci.core.models import UpdateVnicDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VnicHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_module_resource_id_param(self):
        return "vnic_id"

    def get_module_resource_id(self):
        return self.module.params.get("vnic_id")

    def get_get_fn(self):
        return self.client.get_vnic

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vnic, vnic_id=self.module.params.get("vnic_id"),
        )

    def get_update_model_class(self):
        return UpdateVnicDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_vnic,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vnic_id=self.module.params.get("vnic_id"),
                update_vnic_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


VnicHelperCustom = get_custom_class("VnicHelperCustom")


class ResourceHelper(VnicHelperCustom, VnicHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            vnic_id=dict(aliases=["id"], type="str", required=True),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            hostname_label=dict(type="str"),
            nsg_ids=dict(type="list"),
            skip_source_dest_check=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vnic",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
