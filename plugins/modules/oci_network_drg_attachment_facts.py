#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_network_drg_attachment_facts
short_description: Fetches details about one or multiple DrgAttachment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DrgAttachment resources in Oracle Cloud Infrastructure
    - Lists the `DrgAttachment` resource for the specified compartment. You can filter the
      results by DRG, attached network, attachment type, DRG route table or
      VCN route table.
    - The LIST API lists DRG attachments by attachment type. It will default to list VCN attachments,
      but you may request to list ALL attachments of ALL types.
    - If I(drg_attachment_id) is specified, the details of a single DrgAttachment will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    drg_attachment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG attachment.
            - Required to get a specific drg_attachment.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple drg_attachments.
        type: str
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
        type: str
    drg_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG.
        type: str
    network_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource (virtual circuit, VCN, IPSec tunnel, or
              remote peering connection) attached to the DRG.
        type: str
    attachment_type:
        description:
            - The type for the network resource attached to the DRG.
        type: str
        choices:
            - "VCN"
            - "VIRTUAL_CIRCUIT"
            - "REMOTE_PEERING_CONNECTION"
            - "IPSEC_TUNNEL"
            - "ALL"
    drg_route_table_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table assigned to the DRG attachment.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
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
    lifecycle_state:
        description:
            - A filter to return only resources that match the specified lifecycle
              state. The value is case insensitive.
        type: str
        choices:
            - "ATTACHING"
            - "ATTACHED"
            - "DETACHING"
            - "DETACHED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific drg_attachment
  oci_network_drg_attachment_facts:
    # required
    drg_attachment_id: "ocid1.drgattachment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List drg_attachments
  oci_network_drg_attachment_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    drg_id: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
    network_id: "ocid1.network.oc1..xxxxxxEXAMPLExxxxxx"
    attachment_type: VCN
    drg_route_table_id: "ocid1.drgroutetable.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: ATTACHING

"""

RETURN = """
drg_attachments:
    description:
        - List of DrgAttachment resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the DRG attachment.
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
        drg_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DRG.
            returned: on success
            type: str
            sample: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The DRG attachment's Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The DRG attachment's current state.
            returned: on success
            type: str
            sample: ATTACHING
        time_created:
            description:
                - The date and time the DRG attachment was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        drg_route_table_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table that is assigned to this
                  attachment.
                - The DRG route table manages traffic inside the DRG.
            returned: on success
            type: str
            sample: "ocid1.drgroutetable.oc1..xxxxxxEXAMPLExxxxxx"
        network_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: VCN
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network attached to the DRG.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                ipsec_connection_id:
                    description:
                        - The IPSec connection that contains the attached IPSec tunnel.
                    returned: on success
                    type: str
                    sample: "ocid1.ipsecconnection.oc1..xxxxxxEXAMPLExxxxxx"
                route_table_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the route table the DRG attachment is using.
                        - "For information about why you would associate a route table with a DRG attachment, see:"
                        - " * L(Transit Routing: Access to Multiple VCNs in Same
                          Region,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)
                            * L(Transit Routing: Private Access to Oracle
                            Services,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)"
                    returned: on success
                    type: str
                    sample: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        route_table_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table the DRG attachment is using.
                - "For information about why you would associate a route table with a DRG attachment, see:"
                - " * L(Transit Routing: Access to Multiple VCNs in Same Region,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)
                    * L(Transit Routing: Private Access to Oracle
                    Services,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)"
                - This field is deprecated. Instead, use the `networkDetails` field to view the
                  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the attached resource.
            returned: on success
            type: str
            sample: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
                  This field is deprecated. Instead, use the `networkDetails` field to view the
                  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the attached resource.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        export_drg_route_distribution_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the export route distribution used to specify how routes
                  in the assigned DRG route table
                  are advertised to the attachment.
                  If this value is null, no routes are advertised through this attachment.
            returned: on success
            type: str
            sample: "ocid1.exportdrgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx"
        is_cross_tenancy:
            description:
                - Indicates whether the DRG attachment and attached network live in a different tenancy than the DRG.
                - "Example: `false`"
            returned: on success
            type: bool
            sample: true
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "drg_id": "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ATTACHING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "drg_route_table_id": "ocid1.drgroutetable.oc1..xxxxxxEXAMPLExxxxxx",
        "network_details": {
            "type": "VCN",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "ipsec_connection_id": "ocid1.ipsecconnection.oc1..xxxxxxEXAMPLExxxxxx",
            "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "export_drg_route_distribution_id": "ocid1.exportdrgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cross_tenancy": true
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


class DrgAttachmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "drg_attachment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_drg_attachment,
            drg_attachment_id=self.module.params.get("drg_attachment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "vcn_id",
            "drg_id",
            "network_id",
            "attachment_type",
            "drg_route_table_id",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_drg_attachments,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DrgAttachmentFactsHelperCustom = get_custom_class("DrgAttachmentFactsHelperCustom")


class ResourceFactsHelper(DrgAttachmentFactsHelperCustom, DrgAttachmentFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            drg_attachment_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            vcn_id=dict(type="str"),
            drg_id=dict(type="str"),
            network_id=dict(type="str"),
            attachment_type=dict(
                type="str",
                choices=[
                    "VCN",
                    "VIRTUAL_CIRCUIT",
                    "REMOTE_PEERING_CONNECTION",
                    "IPSEC_TUNNEL",
                    "ALL",
                ],
            ),
            drg_route_table_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str", choices=["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="drg_attachment",
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

    module.exit_json(drg_attachments=result)


if __name__ == "__main__":
    main()
