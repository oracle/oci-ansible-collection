#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_waf_network_address_list_actions
short_description: Perform actions on a NetworkAddressList resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a NetworkAddressList resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a NetworkAddressList resource from one compartment to another.
      When provided, If-Match is checked against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    network_address_list_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the NetworkAddressList.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the NetworkAddressList.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on network_address_list
  oci_waf_network_address_list_actions:
    # required
    network_address_list_id: "ocid1.networkaddresslist.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
network_address_list:
    description:
        - Details of the NetworkAddressList resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        addresses:
            description:
                - "A list of IP address prefixes in CIDR notation.
                  To specify all addresses, use \\"0.0.0.0/0\\" for IPv4 and \\"::/0\\" for IPv6."
            returned: on success
            type: list
            sample: []
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the NetworkAddressList.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - NetworkAddressList display name, can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the NetworkAddressList was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the NetworkAddressList was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the NetworkAddressList.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a resource in FAILED state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        type:
            description:
                - Type of NetworkAddressList.
            returned: on success
            type: str
            sample: ADDRESSES
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        vcn_addresses:
            description:
                - "A list of private address prefixes, each associated with a particular VCN.
                  To specify all addresses in a VCN, use \\"0.0.0.0/0\\" for IPv4 and \\"::/0\\" for IPv6."
            returned: on success
            type: complex
            contains:
                vcn_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
                    returned: on success
                    type: str
                    sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
                addresses:
                    description:
                        - A private IP address or CIDR IP address range.
                    returned: on success
                    type: str
                    sample: addresses_example
    sample: {
        "addresses": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "type": "ADDRESSES",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "vcn_addresses": [{
            "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
            "addresses": "addresses_example"
        }]
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
    from oci.waf import WafClient
    from oci.waf.models import ChangeNetworkAddressListCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkAddressListActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "network_address_list_id"

    def get_module_resource_id(self):
        return self.module.params.get("network_address_list_id")

    def get_get_fn(self):
        return self.client.get_network_address_list

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_network_address_list,
            network_address_list_id=self.module.params.get("network_address_list_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeNetworkAddressListCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_network_address_list_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_address_list_id=self.module.params.get(
                    "network_address_list_id"
                ),
                change_network_address_list_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NetworkAddressListActionsHelperCustom = get_custom_class(
    "NetworkAddressListActionsHelperCustom"
)


class ResourceHelper(
    NetworkAddressListActionsHelperCustom, NetworkAddressListActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            network_address_list_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="network_address_list",
        service_client_class=WafClient,
        namespace="waf",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
