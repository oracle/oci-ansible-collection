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
module: oci_network_drg_attachment_actions
short_description: Perform actions on a DrgAttachment resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DrgAttachment resource in Oracle Cloud Infrastructure
    - For I(action=remove_export_drg_route_distribution), removes the export route distribution from the DRG attachment so no routes are advertised to it.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    drg_attachment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG attachment.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the DrgAttachment.
        type: str
        required: true
        choices:
            - "remove_export_drg_route_distribution"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action remove_export_drg_route_distribution on drg_attachment
  oci_network_drg_attachment_actions:
    # required
    drg_attachment_id: "ocid1.drgattachment.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_export_drg_route_distribution

"""

RETURN = """
drg_attachment:
    description:
        - Details of the DrgAttachment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the DRG attachment.
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
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG.
            returned: on success
            type: str
            sample: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The DRG attachment's Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
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
                ipsec_connection_id:
                    description:
                        - The IPSec connection that contains the attached IPSec tunnel.
                    returned: on success
                    type: str
                    sample: "ocid1.ipsecconnection.oc1..xxxxxxEXAMPLExxxxxx"
                route_table_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table the DRG attachment is
                          using.
                        - "For information about why you would associate a route table with a DRG attachment, see:"
                        - " * L(Transit Routing: Access to Multiple VCNs in Same
                          Region,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)
                            * L(Transit Routing: Private Access to Oracle
                            Services,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)"
                    returned: on success
                    type: str
                    sample: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
                vcn_route_type:
                    description:
                        - Indicates whether the VCN CIDRs or the individual subnet CIDRs are imported from the attachment.
                          Routes from the VCN ingress route table are always imported.
                    returned: on success
                    type: str
                    sample: VCN_CIDRS
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
                  L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the attached resource.
            returned: on success
            type: str
            sample: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
                  This field is deprecated. Instead, use the `networkDetails` field to view the
                  L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the attached resource.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        export_drg_route_distribution_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the export route distribution used to specify how
                  routes in the assigned DRG route table
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
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "drg_id": "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ATTACHING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "drg_route_table_id": "ocid1.drgroutetable.oc1..xxxxxxEXAMPLExxxxxx",
        "network_details": {
            "ipsec_connection_id": "ocid1.ipsecconnection.oc1..xxxxxxEXAMPLExxxxxx",
            "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx",
            "vcn_route_type": "VCN_CIDRS",
            "type": "VCN",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "export_drg_route_distribution_id": "ocid1.exportdrgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cross_tenancy": true
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
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrgAttachmentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        remove_export_drg_route_distribution
    """

    @staticmethod
    def get_module_resource_id_param():
        return "drg_attachment_id"

    def get_module_resource_id(self):
        return self.module.params.get("drg_attachment_id")

    def get_get_fn(self):
        return self.client.get_drg_attachment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_drg_attachment,
            drg_attachment_id=self.module.params.get("drg_attachment_id"),
        )

    def remove_export_drg_route_distribution(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_export_drg_route_distribution,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_attachment_id=self.module.params.get("drg_attachment_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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


DrgAttachmentActionsHelperCustom = get_custom_class("DrgAttachmentActionsHelperCustom")


class ResourceHelper(DrgAttachmentActionsHelperCustom, DrgAttachmentActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            drg_attachment_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["remove_export_drg_route_distribution"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="drg_attachment",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
