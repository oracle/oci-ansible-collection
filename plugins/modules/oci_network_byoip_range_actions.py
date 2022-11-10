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
module: oci_network_byoip_range_actions
short_description: Perform actions on a ByoipRange resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ByoipRange resource in Oracle Cloud Infrastructure
    - For I(action=advertise), begins BGP route advertisements for the BYOIP CIDR block you imported to the Oracle Cloud.
      The `ByoipRange` resource must be in the PROVISIONED state before the BYOIP CIDR block routes can be advertised with BGP.
    - For I(action=change_compartment), moves a BYOIP CIDR block to a different compartment. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - For I(action=validate), submits the BYOIP CIDR block you are importing for validation. Do not submit to Oracle for validation if you have not already
      modified the information for the BYOIP CIDR block with your Regional Internet Registry. See L(To import a CIDR
      block,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/BYOIP.htm#import_cidr) for details.
    - For I(action=withdraw), withdraws BGP route advertisement for the BYOIP CIDR block.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the destination compartment for the BYOIP CIDR block
              move.
            - Required for I(action=change_compartment).
        type: str
    byoip_range_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource containing the BYOIP CIDR
              block.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the ByoipRange.
        type: str
        required: true
        choices:
            - "advertise"
            - "change_compartment"
            - "validate"
            - "withdraw"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action advertise on byoip_range
  oci_network_byoip_range_actions:
    # required
    byoip_range_id: "ocid1.byoiprange.oc1..xxxxxxEXAMPLExxxxxx"
    action: advertise

- name: Perform action change_compartment on byoip_range
  oci_network_byoip_range_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    byoip_range_id: "ocid1.byoiprange.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action validate on byoip_range
  oci_network_byoip_range_actions:
    # required
    byoip_range_id: "ocid1.byoiprange.oc1..xxxxxxEXAMPLExxxxxx"
    action: validate

- name: Perform action withdraw on byoip_range
  oci_network_byoip_range_actions:
    # required
    byoip_range_id: "ocid1.byoiprange.oc1..xxxxxxEXAMPLExxxxxx"
    action: withdraw

"""

RETURN = """
byoip_range:
    description:
        - Details of the ByoipRange resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        byoip_range_vcn_ipv6_allocations:
            description:
                - A list of `ByoipRangeVcnIpv6AllocationSummary` objects.
            returned: on success
            type: complex
            contains:
                byoip_range_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource to which the CIDR
                          block belongs.
                    returned: on success
                    type: str
                    sample: "ocid1.byoiprange.oc1..xxxxxxEXAMPLExxxxxx"
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the
                          `ByoipRange`.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                ipv6_cidr_block:
                    description:
                        - The BYOIPv6 CIDR block range or subrange allocated to a VCN. This could be all or part of a BYOIPv6 CIDR block.
                          Each VCN allocation must be /64 or larger.
                    returned: on success
                    type: str
                    sample: ipv6_cidr_block_example
                vcn_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the `Vcn` resource to which the ByoipRange
                          belongs.
                    returned: on success
                    type: str
                    sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        cidr_block:
            description:
                - The public IPv4 CIDR block being imported from on-premises to the Oracle cloud.
            returned: on success
            type: str
            sample: cidr_block_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the BYOIP CIDR block.
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
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        ipv6_cidr_block:
            description:
                - The IPv6 CIDR block being imported to the Oracle cloud. This CIDR block must be /48 or larger, and can be subdivided into sub-ranges used
                  across multiple VCNs. A BYOIPv6 prefix can be also assigned across multiple VCNs, and each VCN must be /64 or larger. You may specify
                  a ULA or private IPv6 prefix of /64 or larger to use in the VCN. IPv6-enabled subnets will remain a fixed /64 in size.
            returned: on success
            type: str
            sample: ipv6_cidr_block_example
        lifecycle_details:
            description:
                - The `ByoipRange` resource's current status.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_state:
            description:
                - The `ByoipRange` resource's current state.
            returned: on success
            type: str
            sample: INACTIVE
        time_created:
            description:
                - The date and time the `ByoipRange` resource was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_validated:
            description:
                - The date and time the `ByoipRange` resource was validated, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_advertised:
            description:
                - The date and time the `ByoipRange` resource was advertised to the internet by BGP, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_withdrawn:
            description:
                - The date and time the `ByoipRange` resource was withdrawn from advertisement by BGP to the internet, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        validation_token:
            description:
                - The validation token is an internally-generated ASCII string used in the validation process. See L(Importing a CIDR
                  block,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/BYOIP.htm#import_cidr) for details.
            returned: on success
            type: str
            sample: validation_token_example
    sample: {
        "byoip_range_vcn_ipv6_allocations": [{
            "byoip_range_id": "ocid1.byoiprange.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "ipv6_cidr_block": "ipv6_cidr_block_example",
            "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "cidr_block": "cidr_block_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "ipv6_cidr_block": "ipv6_cidr_block_example",
        "lifecycle_details": "CREATING",
        "lifecycle_state": "INACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_validated": "2013-10-20T19:20:30+01:00",
        "time_advertised": "2013-10-20T19:20:30+01:00",
        "time_withdrawn": "2013-10-20T19:20:30+01:00",
        "validation_token": "validation_token_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.core import VirtualNetworkClient
    from oci.core.models import ChangeByoipRangeCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ByoipRangeActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        advertise
        change_compartment
        validate
        withdraw
    """

    def __init__(self, *args, **kwargs):
        super(ByoipRangeActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "byoip_range_id"

    def get_module_resource_id(self):
        return self.module.params.get("byoip_range_id")

    def get_get_fn(self):
        return self.client.get_byoip_range

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_byoip_range,
            byoip_range_id=self.module.params.get("byoip_range_id"),
        )

    def advertise(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.advertise_byoip_range,
            call_fn_args=(),
            call_fn_kwargs=dict(
                byoip_range_id=self.module.params.get("byoip_range_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeByoipRangeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_byoip_range_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                byoip_range_id=self.module.params.get("byoip_range_id"),
                change_byoip_range_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def validate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.validate_byoip_range,
            call_fn_args=(),
            call_fn_kwargs=dict(
                byoip_range_id=self.module.params.get("byoip_range_id"),
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

    def withdraw(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.withdraw_byoip_range,
            call_fn_args=(),
            call_fn_kwargs=dict(
                byoip_range_id=self.module.params.get("byoip_range_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


ByoipRangeActionsHelperCustom = get_custom_class("ByoipRangeActionsHelperCustom")


class ResourceHelper(ByoipRangeActionsHelperCustom, ByoipRangeActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            byoip_range_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["advertise", "change_compartment", "validate", "withdraw"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="byoip_range",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
