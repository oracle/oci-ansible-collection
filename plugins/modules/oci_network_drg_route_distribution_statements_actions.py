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
module: oci_network_drg_route_distribution_statements_actions
short_description: Perform actions on a DrgRouteDistributionStatements resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DrgRouteDistributionStatements resource in Oracle Cloud Infrastructure
    - For I(action=add), adds one or more route distribution statements to the specified route distribution.
    - For I(action=remove), removes one or more route distribution statements from the specified route distribution's map.
    - For I(action=update), updates one or more route distribution statements in the specified route distribution.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    drg_route_distribution_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route distribution.
        type: str
        aliases: ["id"]
        required: true
    statements:
        description:
            - The collection of route distribution statements to insert into the route distribution.
            - Required for I(action=add), I(action=update).
        type: list
        elements: dict
        suboptions:
            match_criteria:
                description:
                    - The action is applied only if all of the match criteria is met.
                type: list
                elements: dict
                suboptions:
                    match_type:
                        description:
                            - The type of the match criteria for a route distribution statement.
                        type: str
                        choices:
                            - "DRG_ATTACHMENT_ID"
                            - "DRG_ATTACHMENT_TYPE"
                            - "MATCH_ALL"
                        required: true
                    drg_attachment_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG attachment.
                            - Required when match_type is 'DRG_ATTACHMENT_ID'
                        type: str
                    attachment_type:
                        description:
                            - The type of the network resource to be included in this match. A match for a network type implies that all
                              DRG attachments of that type insert routes into the table.
                            - Required when match_type is 'DRG_ATTACHMENT_TYPE'
                        type: str
                        choices:
                            - "VCN"
                            - "VIRTUAL_CIRCUIT"
                            - "REMOTE_PEERING_CONNECTION"
                            - "IPSEC_TUNNEL"
            action:
                description:
                    - "Accept: import/export the route \\"as is\\""
                type: str
                choices:
                    - "ACCEPT"
            priority:
                description:
                    - This field is used to specify the priority of each statement in a route distribution.
                      The priority will be represented as a number between 0 and 65535 where a lower number
                      indicates a higher priority. When a route is processed, statements are applied in the order
                      defined by their priority. The first matching rule dictates the action that will be taken
                      on the route.
                type: int
            id:
                description:
                    - The Oracle-assigned ID of each route distribution statement to be updated.
                type: str
    statement_ids:
        description:
            - The Oracle-assigned ID of each route distribution to remove.
            - Applicable only for I(action=remove).
        type: list
        elements: str
    action:
        description:
            - The action to perform on the DrgRouteDistributionStatements.
        type: str
        required: true
        choices:
            - "add"
            - "remove"
            - "update"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action add on drg_route_distribution_statements
  oci_network_drg_route_distribution_statements_actions:
    # required
    drg_route_distribution_id: "ocid1.drgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx"
    statements:
    - # optional
      match_criteria:
      - # required
        match_type: DRG_ATTACHMENT_ID
        drg_attachment_id: "ocid1.drgattachment.oc1..xxxxxxEXAMPLExxxxxx"
      action: ACCEPT
      priority: 56
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    action: add

- name: Perform action remove on drg_route_distribution_statements
  oci_network_drg_route_distribution_statements_actions:
    # required
    drg_route_distribution_id: "ocid1.drgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove

    # optional
    statement_ids: [ "statement_ids_example" ]

- name: Perform action update on drg_route_distribution_statements
  oci_network_drg_route_distribution_statements_actions:
    # required
    drg_route_distribution_id: "ocid1.drgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx"
    statements:
    - # optional
      match_criteria:
      - # required
        match_type: DRG_ATTACHMENT_ID
        drg_attachment_id: "ocid1.drgattachment.oc1..xxxxxxEXAMPLExxxxxx"
      action: ACCEPT
      priority: 56
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    action: update

"""

RETURN = """
drg_route_distribution_statements:
    description:
        - Details of the DrgRouteDistributionStatements resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        match_criteria:
            description:
                - The action is applied only if all of the match criteria is met.
                  If there are no match criteria in a statement, any input is considered a match and the action is applied.
            returned: on success
            type: complex
            contains:
                drg_attachment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG attachment.
                    returned: on success
                    type: str
                    sample: "ocid1.drgattachment.oc1..xxxxxxEXAMPLExxxxxx"
                attachment_type:
                    description:
                        - The type of the network resource to be included in this match. A match for a network type implies that all
                          DRG attachments of that type insert routes into the table.
                    returned: on success
                    type: str
                    sample: VCN
                match_type:
                    description:
                        - The type of the match criteria for a route distribution statement.
                    returned: on success
                    type: str
                    sample: DRG_ATTACHMENT_TYPE
        action:
            description:
                - "`ACCEPT` indicates the route should be imported or exported as-is."
            returned: on success
            type: str
            sample: ACCEPT
        priority:
            description:
                - This field specifies the priority of each statement in a route distribution.
                  Priorities must be unique within a particular route distribution.
                  The priority will be represented as a number between 0 and 65535 where a lower number
                  indicates a higher priority. When a route is processed, statements are applied in the order
                  defined by their priority. The first matching rule dictates the action that will be taken
                  on the route.
            returned: on success
            type: int
            sample: 56
        id:
            description:
                - The Oracle-assigned ID of the route distribution statement.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "match_criteria": [{
            "drg_attachment_id": "ocid1.drgattachment.oc1..xxxxxxEXAMPLExxxxxx",
            "attachment_type": "VCN",
            "match_type": "DRG_ATTACHMENT_TYPE"
        }],
        "action": "ACCEPT",
        "priority": 56,
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core.models import AddDrgRouteDistributionStatementsDetails
    from oci.core.models import RemoveDrgRouteDistributionStatementsDetails
    from oci.core.models import UpdateDrgRouteDistributionStatementsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrgRouteDistributionStatementsActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add
        remove
        update
    """

    @staticmethod
    def get_module_resource_id_param():
        return "drg_route_distribution_id"

    def get_module_resource_id(self):
        return self.module.params.get("drg_route_distribution_id")

    def add(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddDrgRouteDistributionStatementsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_drg_route_distribution_statements,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_route_distribution_id=self.module.params.get(
                    "drg_route_distribution_id"
                ),
                add_drg_route_distribution_statements_details=action_details,
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

    def remove(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveDrgRouteDistributionStatementsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_drg_route_distribution_statements,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_route_distribution_id=self.module.params.get(
                    "drg_route_distribution_id"
                ),
                remove_drg_route_distribution_statements_details=action_details,
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

    def update(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpdateDrgRouteDistributionStatementsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_drg_route_distribution_statements,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_route_distribution_id=self.module.params.get(
                    "drg_route_distribution_id"
                ),
                update_drg_route_distribution_statements_details=action_details,
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


DrgRouteDistributionStatementsActionsHelperCustom = get_custom_class(
    "DrgRouteDistributionStatementsActionsHelperCustom"
)


class ResourceHelper(
    DrgRouteDistributionStatementsActionsHelperCustom,
    DrgRouteDistributionStatementsActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            drg_route_distribution_id=dict(aliases=["id"], type="str", required=True),
            statements=dict(
                type="list",
                elements="dict",
                options=dict(
                    match_criteria=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            match_type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "DRG_ATTACHMENT_ID",
                                    "DRG_ATTACHMENT_TYPE",
                                    "MATCH_ALL",
                                ],
                            ),
                            drg_attachment_id=dict(type="str"),
                            attachment_type=dict(
                                type="str",
                                choices=[
                                    "VCN",
                                    "VIRTUAL_CIRCUIT",
                                    "REMOTE_PEERING_CONNECTION",
                                    "IPSEC_TUNNEL",
                                ],
                            ),
                        ),
                    ),
                    action=dict(type="str", choices=["ACCEPT"]),
                    priority=dict(type="int"),
                    id=dict(type="str"),
                ),
            ),
            statement_ids=dict(type="list", elements="str"),
            action=dict(type="str", required=True, choices=["add", "remove", "update"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="drg_route_distribution_statements",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
