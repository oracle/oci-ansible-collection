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
module: oci_ocvp_esxi_host_facts
short_description: Fetches details about one or multiple EsxiHost resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple EsxiHost resources in Oracle Cloud Infrastructure
    - Lists the ESXi hosts in the specified SDDC. The list can be filtered
      by Compute instance OCID or ESXi display name.
    - Remember that in terms of implementation, an ESXi host is a Compute instance that
      is configured with the chosen bundle of VMware software. Each `EsxiHost`
      object has its own OCID (`id`), and a separate attribute for the OCID of
      the Compute instance (`computeInstanceId`). When filtering the list of
      ESXi hosts, you can specify the OCID of the Compute instance, not the
      ESXi host OCID.
    - If I(esxi_host_id) is specified, the details of a single EsxiHost will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    esxi_host_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the ESXi host.
            - Required to get a specific esxi_host.
        type: str
        aliases: ["id"]
    sddc_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the SDDC.
        type: str
    compute_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Compute instance.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    lifecycle_state:
        description:
            - The lifecycle state of the resource.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific esxi_host
  oci_ocvp_esxi_host_facts:
    # required
    esxi_host_id: "ocid1.esxihost.oc1..xxxxxxEXAMPLExxxxxx"

- name: List esxi_hosts
  oci_ocvp_esxi_host_facts:

    # optional
    sddc_id: "ocid1.sddc.oc1..xxxxxxEXAMPLExxxxxx"
    compute_instance_id: "ocid1.computeinstance.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated
    lifecycle_state: CREATING

"""

RETURN = """
esxi_hosts:
    description:
        - List of EsxiHost resources
    returned: on success
    type: complex
    contains:
        capacity_reservation_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Capacity Reservation.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
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
    sample: [{
        "capacity_reservation_id": "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "sddc_id": "ocid1.sddc.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "compute_instance_id": "ocid1.computeinstance.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "current_sku": "HOUR",
        "next_sku": "HOUR",
        "billing_contract_end_date": "2013-10-20T19:20:30+01:00",
        "failed_esxi_host_id": "ocid1.failedesxihost.oc1..xxxxxxEXAMPLExxxxxx",
        "replacement_esxi_host_id": "ocid1.replacementesxihost.oc1..xxxxxxEXAMPLExxxxxx",
        "grace_period_end_date": "2013-10-20T19:20:30+01:00",
        "compute_availability_domain": "Uocm:PHX-AD-1",
        "host_shape_name": "host_shape_name_example",
        "host_ocpu_count": 3.4,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.ocvp import EsxiHostClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EsxiHostFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "esxi_host_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_esxi_host,
            esxi_host_id=self.module.params.get("esxi_host_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sddc_id",
            "compute_instance_id",
            "display_name",
            "sort_order",
            "sort_by",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_esxi_hosts, **optional_kwargs
        )


EsxiHostFactsHelperCustom = get_custom_class("EsxiHostFactsHelperCustom")


class ResourceFactsHelper(EsxiHostFactsHelperCustom, EsxiHostFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            esxi_host_id=dict(aliases=["id"], type="str"),
            sddc_id=dict(type="str"),
            compute_instance_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="esxi_host",
        service_client_class=EsxiHostClient,
        namespace="ocvp",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(esxi_hosts=result)


if __name__ == "__main__":
    main()
