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
module: oci_network_vcn_actions
short_description: Perform actions on a Vcn resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Vcn resource in Oracle Cloud Infrastructure
    - For I(action=add_vcn_cidr), add a CIDR to a VCN. The new CIDR must maintain the following rules -
      a. The CIDR provided is valid
      b. The new CIDR range should not overlap with any existing CIDRs
      c. The new CIDR should not exceed the max limit of CIDRs per VCNs
      d. The new CIDR range does not overlap with any peered VCNs
    - For I(action=modify_vcn_cidr), update a CIDR from a VCN. The new CIDR must maintain the following rules -
      a. The CIDR provided is valid
      b. The new CIDR range should not overlap with any existing CIDRs
      c. The new CIDR should not exceed the max limit of CIDRs per VCNs
      d. The new CIDR range does not overlap with any peered VCNs
      e. The new CIDR should overlap with any existing route rule within a VCN
      f. All existing subnet CIDRs are subsets of the updated CIDR ranges
    - For I(action=remove_vcn_cidr), remove a CIDR from a VCN. The CIDR being removed should not have
      any resources allocated from it.
version_added: "2.9"
author: Oracle (@oracle)
options:
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
        type: str
        aliases: ["id"]
        required: true
    cidr_block:
        description:
            - The CIDR IP address that needs to be added.
            - Required for I(action=add_vcn_cidr), I(action=remove_vcn_cidr).
        type: str
    original_cidr_block:
        description:
            - The CIDR IP address that needs to be updated.
            - Required for I(action=modify_vcn_cidr).
        type: str
    new_cidr_block:
        description:
            - The new CIDR IP address which will replace the orginal one.
            - Required for I(action=modify_vcn_cidr).
        type: str
    action:
        description:
            - The action to perform on the Vcn.
        type: str
        required: true
        choices:
            - "add_vcn_cidr"
            - "modify_vcn_cidr"
            - "remove_vcn_cidr"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_vcn_cidr on vcn
  oci_network_vcn_actions:
    vcn_id: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    cidr_block: cidr_block_example
    action: add_vcn_cidr

- name: Perform action modify_vcn_cidr on vcn
  oci_network_vcn_actions:
    vcn_id: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    original_cidr_block: original_cidr_block_example
    new_cidr_block: new_cidr_block_example
    action: modify_vcn_cidr

- name: Perform action remove_vcn_cidr on vcn
  oci_network_vcn_actions:
    vcn_id: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    cidr_block: cidr_block_example
    action: remove_vcn_cidr

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
                - Deprecated. The first CIDR IP address from cidrBlocks.
                - "Example: `172.16.0.0/16`"
            returned: on success
            type: string
            sample: 172.16.0.0/16
        cidr_blocks:
            description:
                - The list of IPv4 CIDR blocks the VCN will use.
            returned: on success
            type: list
            sample: []
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
                - The date and time the VCN was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
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
        "cidr_blocks": [],
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import AddVcnCidrDetails
    from oci.core.models import ModifyVcnCidrDetails
    from oci.core.models import RemoveVcnCidrDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VcnActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_vcn_cidr
        modify_vcn_cidr
        remove_vcn_cidr
    """

    def __init__(self, *args, **kwargs):
        super(VcnActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "vcn_id"

    def get_module_resource_id(self):
        return self.module.params.get("vcn_id")

    def get_get_fn(self):
        return self.client.get_vcn

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vcn, vcn_id=self.module.params.get("vcn_id"),
        )

    def add_vcn_cidr(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddVcnCidrDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_vcn_cidr,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vcn_id=self.module.params.get("vcn_id"),
                add_vcn_cidr_details=action_details,
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

    def modify_vcn_cidr(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ModifyVcnCidrDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.modify_vcn_cidr,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vcn_id=self.module.params.get("vcn_id"),
                modify_vcn_cidr_details=action_details,
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

    def remove_vcn_cidr(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveVcnCidrDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_vcn_cidr,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vcn_id=self.module.params.get("vcn_id"),
                remove_vcn_cidr_details=action_details,
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


VcnActionsHelperCustom = get_custom_class("VcnActionsHelperCustom")


class ResourceHelper(VcnActionsHelperCustom, VcnActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            vcn_id=dict(aliases=["id"], type="str", required=True),
            cidr_block=dict(type="str"),
            original_cidr_block=dict(type="str"),
            new_cidr_block=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=["add_vcn_cidr", "modify_vcn_cidr", "remove_vcn_cidr"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vcn",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
