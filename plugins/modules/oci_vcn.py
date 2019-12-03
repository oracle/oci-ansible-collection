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
module: oci_vcn
short_description: Manage a Vcn resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Vcn resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new virtual cloud network (VCN). For more information, see
      L(VCNs and Subnets,https://docs.cloud.oracle.com/Content/Network/Tasks/managingVCNs.htm).
    - "For the VCN you must specify a single, contiguous IPv4 CIDR block. Oracle recommends using one of the
      private IP address ranges specified in L(RFC 1918,https://tools.ietf.org/html/rfc1918) (10.0.0.0/8,
      172.16/12, and 192.168/16). Example: 172.16.0.0/16. The CIDR block can range from /16 to /30, and it
      must not overlap with your on-premises network. You can't change the size of the VCN after creation."
    - For the purposes of access control, you must provide the OCID of the compartment where you want the VCN to
      reside. Consult an Oracle Cloud Infrastructure administrator in your organization if you're not sure which
      compartment to use. Notice that the VCN doesn't have to be in the same compartment as the subnets or other
      Networking Service components. For more information about compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
      L(Resource Identifiers,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
    - "You may optionally specify a *display name* for the VCN, otherwise a default is provided. It does not have to
      be unique, and you can change it. Avoid entering confidential information."
    - You can also add a DNS label for the VCN, which is required if you want the instances to use the
      Interent and VCN Resolver option for DNS in the VCN. For more information, see
      L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
    - The VCN automatically comes with a default route table, default security list, and default set of DHCP options.
      The OCID for each is returned in the response. You can't delete these default objects, but you can change their
      contents (that is, change the route rules, security list rules, and so on).
    - The VCN and subnets you create are not accessible until you attach an internet gateway or set up an IPSec VPN
      or FastConnect. For more information, see
      L(Overview of the Networking Service,https://docs.cloud.oracle.com/Content/Network/Concepts/overview.htm).
version_added: "2.5"
options:
    cidr_block:
        description:
            - The CIDR IP address block of the VCN.
            - "Example: `172.16.0.0/16`"
            - Required for create using I(state=present).
    compartment_id:
        description:
            - The OCID of the compartment to contain the VCN.
            - Required for create using I(state=present).
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        aliases: ["name"]
    dns_label:
        description:
            - A DNS label for the VCN, used in conjunction with the VNIC's hostname and
              subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC
              within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`).
              Not required to be unique, but it's a best practice to set unique DNS labels
              for VCNs in your tenancy. Must be an alphanumeric string that begins with a letter.
              The value cannot be changed.
            - You must set this value if you want instances to be able to use hostnames to
              resolve other instances in the VCN. Otherwise the Internet and VCN Resolver
              will not work.
            - For more information, see
              L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
            - "Example: `vcn1`"
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
            - Required for update using I(state=present), I(state=absent).
        aliases: ["id"]
    state:
        description:
            - The state of the Vcn.
            - Use I(state=present) to create or update a Vcn.
            - Use I(state=absent) to delete a Vcn.
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
- name: Create vcn
  oci_vcn:
    cidr_block: 10.0.0.0/16
    compartment_id: ocid1.compartment.oc1..aaaaaaaayzfqeibduyox6iib3olcmdar3ugly4fmameq4h7lcdlihrvur7xq
    display_name: MyVcn

- name: Update vcn
  oci_vcn:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: MyVcn
    vcn_id: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete vcn
  oci_vcn:
    vcn_id: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
vcn:
    description:
        - Details of the Vcn resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        cidr_block:
            description:
                - The CIDR IP address block of the VCN.
                - "Example: `172.16.0.0/16`"
            returned: on success
            type: string
            sample: 172.16.0.0/16
        compartment_id:
            description:
                - The OCID of the compartment containing the VCN.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        default_dhcp_options_id:
            description:
                - The OCID for the VCN's default set of DHCP options.
            returned: on success
            type: string
            sample: ocid1.defaultdhcpoptions.oc1..xxxxxxEXAMPLExxxxxx
        default_route_table_id:
            description:
                - The OCID for the VCN's default route table.
            returned: on success
            type: string
            sample: ocid1.defaultroutetable.oc1..xxxxxxEXAMPLExxxxxx
        default_security_list_id:
            description:
                - The OCID for the VCN's default security list.
            returned: on success
            type: string
            sample: ocid1.defaultsecuritylist.oc1..xxxxxxEXAMPLExxxxxx
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
            returned: on success
            type: string
            sample: display_name_example
        dns_label:
            description:
                - A DNS label for the VCN, used in conjunction with the VNIC's hostname and
                  subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC
                  within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`).
                  Must be an alphanumeric string that begins with a letter.
                  The value cannot be changed.
                - The absence of this parameter means the Internet and VCN Resolver will
                  not work for this VCN.
                - For more information, see
                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
                - "Example: `vcn1`"
            returned: on success
            type: string
            sample: vcn1
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
                - The VCN's Oracle ID (OCID).
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The VCN's current state.
            returned: on success
            type: string
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the VCN was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vcn_domain_name:
            description:
                - The VCN's domain name, which consists of the VCN's DNS label, and the
                  `oraclevcn.com` domain.
                - For more information, see
                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
                - "Example: `vcn1.oraclevcn.com`"
            returned: on success
            type: string
            sample: vcn1.oraclevcn.com
    sample: {
        "cidr_block": "172.16.0.0/16",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "default_dhcp_options_id": "ocid1.defaultdhcpoptions.oc1..xxxxxxEXAMPLExxxxxx",
        "default_route_table_id": "ocid1.defaultroutetable.oc1..xxxxxxEXAMPLExxxxxx",
        "default_security_list_id": "ocid1.defaultsecuritylist.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "dns_label": "vcn1",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "time_created": "2016-08-25T21:10:29.600Z",
        "vcn_domain_name": "vcn1.oraclevcn.com"
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
    from oci.core.models import CreateVcnDetails
    from oci.core.models import UpdateVcnDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VcnHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    @staticmethod
    def get_module_resource_id_param():
        return "vcn_id"

    def get_module_resource_id(self):
        return self.module.params.get("vcn_id")

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vcn, vcn_id=self.module.params.get("vcn_id")
        )

    def list_resources(self):
        required_list_method_params = ["compartment_id"]

        optional_list_method_params = ["display_name"]

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

        return oci_common_utils.list_all_resources(self.client.list_vcns, **kwargs)

    def get_create_model_class(self):
        return CreateVcnDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_common_utils.call_with_backoff(
            self.client.create_vcn, create_vcn_details=create_details
        )

    def get_update_model_class(self):
        return UpdateVcnDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_common_utils.call_with_backoff(
            self.client.update_vcn,
            vcn_id=self.module.params.get("vcn_id"),
            update_vcn_details=update_details,
        )

    def delete_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.delete_vcn, vcn_id=self.module.params.get("vcn_id")
        )


VcnHelperCustom = get_custom_class("VcnHelperCustom")


class ResourceHelper(VcnHelperCustom, VcnHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            cidr_block=dict(type="str"),
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            dns_label=dict(type="str"),
            freeform_tags=dict(type="dict"),
            vcn_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module, resource_type="vcn", service_client_class=VirtualNetworkClient
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
