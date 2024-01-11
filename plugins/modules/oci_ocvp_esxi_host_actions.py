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
module: oci_ocvp_esxi_host_actions
short_description: Perform actions on an EsxiHost resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an EsxiHost resource in Oracle Cloud Infrastructure
    - For I(action=swap_billing), swap billing between two Active ESXi hosts.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    esxi_host_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the ESXi host.
        type: str
        aliases: ["id"]
        required: true
    swap_billing_host_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the active ESXi Host to swap billing with current host.
        type: str
        required: true
    action:
        description:
            - The action to perform on the EsxiHost.
        type: str
        required: true
        choices:
            - "swap_billing"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action swap_billing on esxi_host
  oci_ocvp_esxi_host_actions:
    # required
    esxi_host_id: "ocid1.esxihost.oc1..xxxxxxEXAMPLExxxxxx"
    swap_billing_host_id: "ocid1.swapbillinghost.oc1..xxxxxxEXAMPLExxxxxx"
    action: swap_billing

"""

RETURN = """
esxi_host:
    description:
        - Details of the EsxiHost resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the ESXi host.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A descriptive name for the ESXi host. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        sddc_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the SDDC that the
                  ESXi host belongs to.
            returned: on success
            type: str
            sample: "ocid1.sddc.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that
                  contains the SDDC.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        compute_instance_id:
            description:
                - In terms of implementation, an ESXi host is a Compute instance that
                  is configured with the chosen bundle of VMware software. The `computeInstanceId`
                  is the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of that Compute instance.
            returned: on success
            type: str
            sample: "ocid1.computeinstance.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the ESXi host was created, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the ESXi host was updated, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the ESXi host.
            returned: on success
            type: str
            sample: CREATING
        billing_donor_host_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deleted ESXi Host with LeftOver billing cycle.
            returned: on success
            type: str
            sample: "ocid1.billingdonorhost.oc1..xxxxxxEXAMPLExxxxxx"
        swap_billing_host_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the active ESXi Host to swap billing with current host.
            returned: on success
            type: str
            sample: "ocid1.swapbillinghost.oc1..xxxxxxEXAMPLExxxxxx"
        is_billing_continuation_in_progress:
            description:
                - Indicates whether this host is in the progress of billing continuation.
            returned: on success
            type: bool
            sample: true
        is_billing_swapping_in_progress:
            description:
                - Indicates whether this host is in the progress of swapping billing.
            returned: on success
            type: bool
            sample: true
        current_sku:
            description:
                - The billing option currently used by the ESXi host.
                  L(ListSupportedSkus,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/SupportedSkuSummary/ListSupportedSkus).
            returned: on success
            type: str
            sample: HOUR
        next_sku:
            description:
                - The billing option to switch to after the current billing cycle ends.
                  If `nextSku` is null or empty, `currentSku` continues to the next billing cycle.
                  L(ListSupportedSkus,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/SupportedSkuSummary/ListSupportedSkus).
            returned: on success
            type: str
            sample: HOUR
        billing_contract_end_date:
            description:
                - "Current billing cycle end date. If the value in `currentSku` and `nextSku` are different, the value specified in `nextSku`
                  becomes the new `currentSKU` when the `contractEndDate` is reached.
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        failed_esxi_host_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the ESXi host that failed.
            returned: on success
            type: str
            sample: "ocid1.failedesxihost.oc1..xxxxxxEXAMPLExxxxxx"
        replacement_esxi_host_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the ESXi host that
                  is created to replace the failed host.
            returned: on success
            type: str
            sample: "ocid1.replacementesxihost.oc1..xxxxxxEXAMPLExxxxxx"
        grace_period_end_date:
            description:
                - "The date and time when the new esxi host should start billing cycle.
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2021-07-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vmware_software_version:
            description:
                - The version of VMware software that Oracle Cloud VMware Solution installed on the ESXi hosts.
            returned: on success
            type: str
            sample: vmware_software_version_example
        non_upgraded_esxi_host_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the ESXi host that
                  will be upgraded.
            returned: on success
            type: str
            sample: "ocid1.nonupgradedesxihost.oc1..xxxxxxEXAMPLExxxxxx"
        upgraded_replacement_esxi_host_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the ESXi host that
                  is newly created to upgrade the original host.
            returned: on success
            type: str
            sample: "ocid1.upgradedreplacementesxihost.oc1..xxxxxxEXAMPLExxxxxx"
        compute_availability_domain:
            description:
                - The availability domain of the ESXi host.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        host_shape_name:
            description:
                - The compute shape name of the ESXi host.
                  L(ListSupportedHostShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/SupportedHostShapes/ListSupportedHostShapes).
            returned: on success
            type: str
            sample: host_shape_name_example
        host_ocpu_count:
            description:
                - The OCPU count of the ESXi host.
            returned: on success
            type: float
            sample: 3.4
        capacity_reservation_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Capacity Reservation.
            returned: on success
            type: str
            sample: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "sddc_id": "ocid1.sddc.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "compute_instance_id": "ocid1.computeinstance.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "billing_donor_host_id": "ocid1.billingdonorhost.oc1..xxxxxxEXAMPLExxxxxx",
        "swap_billing_host_id": "ocid1.swapbillinghost.oc1..xxxxxxEXAMPLExxxxxx",
        "is_billing_continuation_in_progress": true,
        "is_billing_swapping_in_progress": true,
        "current_sku": "HOUR",
        "next_sku": "HOUR",
        "billing_contract_end_date": "2013-10-20T19:20:30+01:00",
        "failed_esxi_host_id": "ocid1.failedesxihost.oc1..xxxxxxEXAMPLExxxxxx",
        "replacement_esxi_host_id": "ocid1.replacementesxihost.oc1..xxxxxxEXAMPLExxxxxx",
        "grace_period_end_date": "2013-10-20T19:20:30+01:00",
        "vmware_software_version": "vmware_software_version_example",
        "non_upgraded_esxi_host_id": "ocid1.nonupgradedesxihost.oc1..xxxxxxEXAMPLExxxxxx",
        "upgraded_replacement_esxi_host_id": "ocid1.upgradedreplacementesxihost.oc1..xxxxxxEXAMPLExxxxxx",
        "compute_availability_domain": "Uocm:PHX-AD-1",
        "host_shape_name": "host_shape_name_example",
        "host_ocpu_count": 3.4,
        "capacity_reservation_id": "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.ocvp import WorkRequestClient
    from oci.ocvp import EsxiHostClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EsxiHostActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        swap_billing
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "esxi_host_id"

    def get_module_resource_id(self):
        return self.module.params.get("esxi_host_id")

    def get_get_fn(self):
        return self.client.get_esxi_host

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_esxi_host,
            esxi_host_id=self.module.params.get("esxi_host_id"),
        )

    def swap_billing(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.swap_billing,
            call_fn_args=(),
            call_fn_kwargs=dict(
                esxi_host_id=self.module.params.get("esxi_host_id"),
                swap_billing_host_id=self.module.params.get("swap_billing_host_id"),
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


EsxiHostActionsHelperCustom = get_custom_class("EsxiHostActionsHelperCustom")


class ResourceHelper(EsxiHostActionsHelperCustom, EsxiHostActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            esxi_host_id=dict(aliases=["id"], type="str", required=True),
            swap_billing_host_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["swap_billing"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="esxi_host",
        service_client_class=EsxiHostClient,
        namespace="ocvp",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
