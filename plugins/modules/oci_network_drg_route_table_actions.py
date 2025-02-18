#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_network_drg_route_table_actions
short_description: Perform actions on a DrgRouteTable resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DrgRouteTable resource in Oracle Cloud Infrastructure
    - For I(action=remove_import_drg_route_distribution), removes the import route distribution from the DRG route table so no routes are imported
      into it.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    drg_route_table_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the DrgRouteTable.
        type: str
        required: true
        choices:
            - "remove_import_drg_route_distribution"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action remove_import_drg_route_distribution on drg_route_table
  oci_network_drg_route_table_actions:
    # required
    drg_route_table_id: "ocid1.drgroutetable.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_import_drg_route_distribution

"""

RETURN = """
drg_route_table:
    description:
        - Details of the DrgRouteTable resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the
                  DRG route table.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment the DRG is in. The DRG route table
                  is always in the same compartment as the DRG.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        drg_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG the DRG that contains this route table.
            returned: on success
            type: str
            sample: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
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
        time_created:
            description:
                - The date and time the DRG route table was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The DRG route table's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        import_drg_route_distribution_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the import route distribution used to specify how
                  incoming route advertisements from
                  referenced attachments are inserted into the DRG route table.
            returned: on success
            type: str
            sample: "ocid1.importdrgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx"
        is_ecmp_enabled:
            description:
                - If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to
                  your on-premises network, enable ECMP on the DRG route table to which these attachments
                  import routes.
            returned: on success
            type: bool
            sample: true
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "drg_id": "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "PROVISIONING",
        "import_drg_route_distribution_id": "ocid1.importdrgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx",
        "is_ecmp_enabled": true
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
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrgRouteTableActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        remove_import_drg_route_distribution
    """

    @staticmethod
    def get_module_resource_id_param():
        return "drg_route_table_id"

    def get_module_resource_id(self):
        return self.module.params.get("drg_route_table_id")

    def get_get_fn(self):
        return self.client.get_drg_route_table

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_drg_route_table,
            drg_route_table_id=self.module.params.get("drg_route_table_id"),
        )

    def remove_import_drg_route_distribution(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_import_drg_route_distribution,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_route_table_id=self.module.params.get("drg_route_table_id"),
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


DrgRouteTableActionsHelperCustom = get_custom_class("DrgRouteTableActionsHelperCustom")


class ResourceHelper(DrgRouteTableActionsHelperCustom, DrgRouteTableActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            drg_route_table_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["remove_import_drg_route_distribution"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="drg_route_table",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
