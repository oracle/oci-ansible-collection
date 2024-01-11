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
module: oci_network_drg_attachment
short_description: Manage a DrgAttachment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DrgAttachment resource in Oracle Cloud Infrastructure
    - For I(state=present), attaches the specified DRG to the specified network resource. A VCN can be attached to only one DRG
      at a time, but a DRG can be attached to more than one VCN. The response includes a `DrgAttachment`
      object with its own L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). For more information about DRGs, see
      L(Dynamic Routing Gateways (DRGs),https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingDRGs.htm).
    - "You may optionally specify a *display name* for the attachment, otherwise a default is provided.
      It does not have to be unique, and you can change it. Avoid entering confidential information."
    - For the purposes of access control, the DRG attachment is automatically placed into the currently selected compartment.
      For more information about compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
    - "This resource has the following action operations in the M(oracle.oci.oci_network_drg_attachment_actions) module: remove_export_drg_route_distribution."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    drg_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG.
            - Required for create using I(state=present).
        type: str
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
              This field is deprecated. Instead, use the `networkDetails` field to specify the
              L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the attached resource.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    drg_route_table_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table that is assigned to this
              attachment.
            - The DRG route table manages traffic inside the DRG.
            - This parameter is updatable.
        type: str
    network_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network attached to the DRG.
                type: str
            type:
                description:
                    - ""
                    - This parameter is updatable.
                type: str
                choices:
                    - "VCN"
                required: true
            route_table_id:
                description:
                    - This is the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table that is used to route
                      the traffic as it enters a VCN through this attachment.
                    - "For information about why you would associate a route table with a DRG attachment, see
                      L(Advanced Scenario: Transit Routing,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm).
                      For information about why you would associate a route table with a DRG attachment, see:"
                    - " * L(Transit Routing: Access to Multiple VCNs in Same Region,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)
                        * L(Transit Routing: Private Access to Oracle
                        Services,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)"
                    - This parameter is updatable.
                type: str
            vcn_route_type:
                description:
                    - Indicates whether the VCN CIDRs or the individual subnet CIDRs are imported from the attachment.
                      Routes from the VCN ingress route table are always imported.
                    - This parameter is updatable.
                type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    export_drg_route_distribution_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the export route distribution used to specify how
              routes in the assigned DRG route table
              are advertised out through the attachment.
              If this value is null, no routes are advertised through this attachment.
            - This parameter is updatable.
        type: str
    route_table_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table used by the DRG attachment.
            - "If you don't specify a route table here, the DRG attachment is created without an associated route
              table. The Networking service does NOT automatically associate the attached VCN's default route table
              with the DRG attachment.
              For information about why you would associate a route table with a DRG attachment, see:"
            - " * L(Transit Routing: Access to Multiple VCNs in Same Region,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)
                * L(Transit Routing: Private Access to Oracle
                Services,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)
              This field is deprecated. Instead, use the networkDetails field to specify the VCN route table for this attachment."
            - This parameter is updatable.
        type: str
    drg_attachment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG attachment.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the DrgAttachment.
            - Use I(state=present) to create or update a DrgAttachment.
            - Use I(state=absent) to delete a DrgAttachment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create drg_attachment
  oci_network_drg_attachment:
    # required
    drg_id: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    drg_route_table_id: "ocid1.drgroutetable.oc1..xxxxxxEXAMPLExxxxxx"
    network_details:
      # required
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      type: VCN

      # optional
      route_table_id: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
      vcn_route_type: vcn_route_type_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    route_table_id: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update drg_attachment
  oci_network_drg_attachment:
    # required
    drg_attachment_id: "ocid1.drgattachment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    drg_route_table_id: "ocid1.drgroutetable.oc1..xxxxxxEXAMPLExxxxxx"
    network_details:
      # required
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      type: VCN

      # optional
      route_table_id: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
      vcn_route_type: vcn_route_type_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    export_drg_route_distribution_id: "ocid1.exportdrgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx"
    route_table_id: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update drg_attachment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_drg_attachment:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    drg_route_table_id: "ocid1.drgroutetable.oc1..xxxxxxEXAMPLExxxxxx"
    network_details:
      # required
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      type: VCN

      # optional
      route_table_id: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
      vcn_route_type: vcn_route_type_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    export_drg_route_distribution_id: "ocid1.exportdrgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx"
    route_table_id: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete drg_attachment
  oci_network_drg_attachment:
    # required
    drg_attachment_id: "ocid1.drgattachment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete drg_attachment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_drg_attachment:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateDrgAttachmentDetails
    from oci.core.models import UpdateDrgAttachmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrgAttachmentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DrgAttachmentHelperGen, self).get_possible_entity_types() + [
            "drgattachment",
            "drgattachments",
            "coredrgattachment",
            "coredrgattachments",
            "drgattachmentresource",
            "drgattachmentsresource",
            "core",
        ]

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["vcn_id", "drg_id", "display_name"]
            if self._use_name_as_identifier()
            else ["vcn_id", "drg_id", "drg_route_table_id", "display_name"]
        )

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_drg_attachments, **kwargs
        )

    def get_create_model_class(self):
        return CreateDrgAttachmentDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_drg_attachment,
            call_fn_args=(),
            call_fn_kwargs=dict(create_drg_attachment_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateDrgAttachmentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_drg_attachment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_attachment_id=self.module.params.get("drg_attachment_id"),
                update_drg_attachment_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_drg_attachment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_attachment_id=self.module.params.get("drg_attachment_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DrgAttachmentHelperCustom = get_custom_class("DrgAttachmentHelperCustom")


class ResourceHelper(DrgAttachmentHelperCustom, DrgAttachmentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            drg_id=dict(type="str"),
            vcn_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            drg_route_table_id=dict(type="str"),
            network_details=dict(
                type="dict",
                options=dict(
                    id=dict(type="str"),
                    type=dict(type="str", required=True, choices=["VCN"]),
                    route_table_id=dict(type="str"),
                    vcn_route_type=dict(type="str"),
                ),
            ),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            export_drg_route_distribution_id=dict(type="str"),
            route_table_id=dict(type="str"),
            drg_attachment_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="drg_attachment",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
