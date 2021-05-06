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
module: oci_network_drg_route_distribution_statements_facts
short_description: Fetches details about one or multiple DrgRouteDistributionStatements resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DrgRouteDistributionStatements resources in Oracle Cloud Infrastructure
    - Lists the statements for the specified route distribution.
version_added: "2.9"
author: Oracle (@oracle)
options:
    drg_route_distribution_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route distribution.
        type: str
        required: true
    sort_by:
        description:
            - The field to sort by.
        type: str
        choices:
            - "TIMECREATED"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List drg_route_distribution_statements
  oci_network_drg_route_distribution_statements_facts:
    drg_route_distribution_id: "ocid1.drgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
drg_route_distribution_statements:
    description:
        - List of DrgRouteDistributionStatements resources
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
                match_type:
                    description:
                        - The type of the match criteria for a route distribution statement.
                    returned: on success
                    type: string
                    sample: DRG_ATTACHMENT_TYPE
                drg_attachment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG attachment.
                    returned: on success
                    type: string
                    sample: "ocid1.drgattachment.oc1..xxxxxxEXAMPLExxxxxx"
                attachment_type:
                    description:
                        - The type of the network resource to be included in this match. A match for a network type implies that all
                          DRG attachments of that type insert routes into the table.
                    returned: on success
                    type: string
                    sample: VCN
        action:
            description:
                - "`ACCEPT` indicates the route should be imported or exported as-is."
            returned: on success
            type: string
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
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "match_criteria": [{
            "match_type": "DRG_ATTACHMENT_TYPE",
            "drg_attachment_id": "ocid1.drgattachment.oc1..xxxxxxEXAMPLExxxxxx",
            "attachment_type": "VCN"
        }],
        "action": "ACCEPT",
        "priority": 56,
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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


class DrgRouteDistributionStatementsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "drg_route_distribution_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_drg_route_distribution_statements,
            drg_route_distribution_id=self.module.params.get(
                "drg_route_distribution_id"
            ),
            **optional_kwargs
        )


DrgRouteDistributionStatementsFactsHelperCustom = get_custom_class(
    "DrgRouteDistributionStatementsFactsHelperCustom"
)


class ResourceFactsHelper(
    DrgRouteDistributionStatementsFactsHelperCustom,
    DrgRouteDistributionStatementsFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            drg_route_distribution_id=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["TIMECREATED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="drg_route_distribution_statements",
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

    module.exit_json(drg_route_distribution_statements=result)


if __name__ == "__main__":
    main()
