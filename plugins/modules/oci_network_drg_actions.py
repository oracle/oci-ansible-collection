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
module: oci_network_drg_actions
short_description: Perform actions on a Drg resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Drg resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a DRG into a different compartment within the same tenancy. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - For I(action=get_all_drg_attachments), returns a complete list of DRG attachments that belong to a particular DRG.
    - For I(action=upgrade), upgrades the DRG. After upgrade, you can control routing inside your DRG
      via DRG attachments, route distributions, and DRG route tables.
version_added: "2.9"
author: Oracle (@oracle)
options:
    drg_id:
        description:
            - The L([OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
              DRG to.
            - Required for I(action=change_compartment).
        type: str
    attachment_type:
        description:
            - The type for the network resource attached to the DRG.
            - Applicable only for I(action=get_all_drg_attachments).
        type: str
        choices:
            - "VCN"
            - "VIRTUAL_CIRCUIT"
            - "REMOTE_PEERING_CONNECTION"
            - "IPSEC_TUNNEL"
            - "ALL"
    is_cross_tenancy:
        description:
            - Whether the DRG attachment lives in a different tenancy than the DRG.
            - Applicable only for I(action=get_all_drg_attachments).
        type: bool
    action:
        description:
            - The action to perform on the Drg.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "get_all_drg_attachments"
            - "upgrade"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on drg
  oci_network_drg_actions:
    drg_id: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action get_all_drg_attachments on drg
  oci_network_drg_actions:
    drg_id: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
    action: get_all_drg_attachments

- name: Perform action upgrade on drg
  oci_network_drg_actions:
    drg_id: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
    action: upgrade

"""

RETURN = """
drg:
    description:
        - Details of the Drg resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the DRG.
            returned: on success
            type: string
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
            type: string
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
                - The DRG's Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The DRG's current state.
            returned: on success
            type: string
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the DRG was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        default_drg_route_tables:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                vcn:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the default DRG route table to be assigned to
                          DRG attachments
                          of type VCN on creation.
                    returned: on success
                    type: string
                    sample: vcn_example
                ipsec_tunnel:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the default DRG route table assigned to DRG
                          attachments
                          of type IPSEC_TUNNEL on creation.
                    returned: on success
                    type: string
                    sample: ipsec_tunnel_example
                virtual_circuit:
                    description:
                        - The OCID of the default DRG route table to be assigned to DRG attachments
                          of type VIRTUAL_CIRCUIT on creation.
                    returned: on success
                    type: string
                    sample: virtual_circuit_example
                remote_peering_connection:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the default DRG route table to be assigned
                          to DRG attachments
                          of type REMOTE_PEERING_CONNECTION on creation.
                    returned: on success
                    type: string
                    sample: remote_peering_connection_example
        default_export_drg_route_distribution_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of this DRG's default export route distribution for the DRG
                  attachments.
            returned: on success
            type: string
            sample: "ocid1.defaultexportdrgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "time_created": "2016-08-25T21:10:29.600Z",
        "default_drg_route_tables": {
            "vcn": "vcn_example",
            "ipsec_tunnel": "ipsec_tunnel_example",
            "virtual_circuit": "virtual_circuit_example",
            "remote_peering_connection": "remote_peering_connection_example"
        },
        "default_export_drg_route_distribution_id": "ocid1.defaultexportdrgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core.models import ChangeDrgCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrgActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        get_all_drg_attachments
        upgrade
    """

    def __init__(self, *args, **kwargs):
        super(DrgActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "drg_id"

    def get_module_resource_id(self):
        return self.module.params.get("drg_id")

    def get_get_fn(self):
        return self.client.get_drg

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_drg, drg_id=self.module.params.get("drg_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDrgCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_drg_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_id=self.module.params.get("drg_id"),
                change_drg_compartment_details=action_details,
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

    def get_all_drg_attachments(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.get_all_drg_attachments,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_id=self.module.params.get("drg_id"),
                attachment_type=self.module.params.get("attachment_type"),
                is_cross_tenancy=self.module.params.get("is_cross_tenancy"),
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

    def upgrade(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.upgrade_drg,
            call_fn_args=(),
            call_fn_kwargs=dict(drg_id=self.module.params.get("drg_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DrgActionsHelperCustom = get_custom_class("DrgActionsHelperCustom")


class ResourceHelper(DrgActionsHelperCustom, DrgActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            drg_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
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
            is_cross_tenancy=dict(type="bool"),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "get_all_drg_attachments", "upgrade"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="drg",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
