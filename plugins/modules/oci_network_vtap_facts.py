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
module: oci_network_vtap_facts
short_description: Fetches details about one or multiple Vtap resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Vtap resources in Oracle Cloud Infrastructure
    - Lists the virtual test access points (VTAPs) in the specified compartment.
    - If I(vtap_id) is specified, the details of a single Vtap will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    vtap_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VTAP.
            - Required to get a specific vtap.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple vtaps.
        type: str
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
        type: str
    source:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VTAP source.
        type: str
    target_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VTAP target.
        type: str
    target_ip:
        description:
            - The IP address of the VTAP target.
        type: str
    is_vtap_enabled:
        description:
            - Indicates whether to list all VTAPs or only running VTAPs.
            - "* When `FALSE`, lists ALL running and stopped VTAPs.
              * When `TRUE`, lists only running VTAPs (VTAPs where isVtapEnabled = `TRUE`)."
        type: bool
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
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only resources that match the given VTAP administrative lifecycle state.
              The state value is case-insensitive.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "UPDATING"
            - "TERMINATING"
            - "TERMINATED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific vtap
  oci_network_vtap_facts:
    # required
    vtap_id: "ocid1.vtap.oc1..xxxxxxEXAMPLExxxxxx"

- name: List vtaps
  oci_network_vtap_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    source: source_example
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    target_ip: target_ip_example
    is_vtap_enabled: true
    sort_by: TIMECREATED
    sort_order: ASC
    display_name: display_name_example
    lifecycle_state: PROVISIONING

"""

RETURN = """
vtaps:
    description:
        - List of Vtap resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the `Vtap` resource.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN containing the `Vtap` resource.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
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
                - The VTAP's Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The VTAP's administrative lifecycle state.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_state_details:
            description:
                - The VTAP's current running state.
            returned: on success
            type: str
            sample: RUNNING
        time_created:
            description:
                - The date and time the VTAP was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2020-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source point where packets are captured.
            returned: on success
            type: str
            sample: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
        target_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the destination resource where mirrored packets are
                  sent.
            returned: on success
            type: str
            sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
        target_ip:
            description:
                - The IP address of the destination resource where mirrored packets are sent.
            returned: on success
            type: str
            sample: target_ip_example
        capture_filter_id:
            description:
                - The capture filter's Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.capturefilter.oc1..xxxxxxEXAMPLExxxxxx"
        encapsulation_protocol:
            description:
                - Defines an encapsulation header type for the VTAP's mirrored traffic.
            returned: on success
            type: str
            sample: VXLAN
        vxlan_network_identifier:
            description:
                - The virtual extensible LAN (VXLAN) network identifier (or VXLAN segment ID) that uniquely identifies the VXLAN.
            returned: on success
            type: int
            sample: 56
        is_vtap_enabled:
            description:
                - Used to start or stop a `Vtap` resource.
                - "* `TRUE` directs the VTAP to start mirroring traffic.
                  * `FALSE` (Default) directs the VTAP to stop mirroring traffic."
            returned: on success
            type: bool
            sample: true
        source_type:
            description:
                - The source type for the VTAP.
            returned: on success
            type: str
            sample: VNIC
        traffic_mode:
            description:
                - Used to control the priority of traffic. It is an optional field. If it not passed, the value is DEFAULT
            returned: on success
            type: str
            sample: DEFAULT
        max_packet_size:
            description:
                - The maximum size of the packets to be included in the filter.
            returned: on success
            type: int
            sample: 56
        target_type:
            description:
                - The target type for the VTAP.
            returned: on success
            type: str
            sample: VNIC
        source_private_endpoint_ip:
            description:
                - The IP Address of the source private endpoint.
            returned: on success
            type: str
            sample: source_private_endpoint_ip_example
        source_private_endpoint_subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet that source private endpoint belongs to.
            returned: on success
            type: str
            sample: "ocid1.sourceprivateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_state_details": "RUNNING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
        "target_ip": "target_ip_example",
        "capture_filter_id": "ocid1.capturefilter.oc1..xxxxxxEXAMPLExxxxxx",
        "encapsulation_protocol": "VXLAN",
        "vxlan_network_identifier": 56,
        "is_vtap_enabled": true,
        "source_type": "VNIC",
        "traffic_mode": "DEFAULT",
        "max_packet_size": 56,
        "target_type": "VNIC",
        "source_private_endpoint_ip": "source_private_endpoint_ip_example",
        "source_private_endpoint_subnet_id": "ocid1.sourceprivateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VtapFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "vtap_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vtap, vtap_id=self.module.params.get("vtap_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "vcn_id",
            "source",
            "target_id",
            "target_ip",
            "is_vtap_enabled",
            "sort_by",
            "sort_order",
            "display_name",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_vtaps,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


VtapFactsHelperCustom = get_custom_class("VtapFactsHelperCustom")


class ResourceFactsHelper(VtapFactsHelperCustom, VtapFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            vtap_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            vcn_id=dict(type="str"),
            source=dict(type="str"),
            target_id=dict(type="str"),
            target_ip=dict(type="str"),
            is_vtap_enabled=dict(type="bool"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "AVAILABLE",
                    "UPDATING",
                    "TERMINATING",
                    "TERMINATED",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="vtap",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(vtaps=result)


if __name__ == "__main__":
    main()
