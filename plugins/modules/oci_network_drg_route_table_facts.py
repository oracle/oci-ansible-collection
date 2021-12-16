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
module: oci_network_drg_route_table_facts
short_description: Fetches details about one or multiple DrgRouteTable resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DrgRouteTable resources in Oracle Cloud Infrastructure
    - Lists the DRG route tables for the specified DRG.
    - Use the `ListDrgRouteRules` operation to retrieve the route rules in a table.
    - If I(drg_route_table_id) is specified, the details of a single DrgRouteTable will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    drg_route_table_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.
            - Required to get a specific drg_route_table.
        type: str
        aliases: ["id"]
    drg_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG.
            - Required to list multiple drg_route_tables.
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
    import_drg_route_distribution_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the import route distribution.
        type: str
    lifecycle_state:
        description:
            - A filter that only returns matches for the specified lifecycle
              state. The value is case insensitive.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "TERMINATING"
            - "TERMINATED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific drg_route_table
  oci_network_drg_route_table_facts:
    # required
    drg_route_table_id: "ocid1.drgroutetable.oc1..xxxxxxEXAMPLExxxxxx"

- name: List drg_route_tables
  oci_network_drg_route_table_facts:
    # required
    drg_id: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC
    import_drg_route_distribution_id: "ocid1.importdrgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: PROVISIONING

"""

RETURN = """
drg_route_tables:
    description:
        - List of DrgRouteTable resources
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
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment the DRG is in. The DRG route table
                  is always in the same compartment as the DRG.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        drg_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DRG the DRG that contains this route table.
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
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the import route distribution used to specify how
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
    sample: [{
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


class DrgRouteTableFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "drg_route_table_id",
        ]

    def get_required_params_for_list(self):
        return [
            "drg_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_drg_route_table,
            drg_route_table_id=self.module.params.get("drg_route_table_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_by",
            "sort_order",
            "import_drg_route_distribution_id",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_drg_route_tables,
            drg_id=self.module.params.get("drg_id"),
            **optional_kwargs
        )


DrgRouteTableFactsHelperCustom = get_custom_class("DrgRouteTableFactsHelperCustom")


class ResourceFactsHelper(DrgRouteTableFactsHelperCustom, DrgRouteTableFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            drg_route_table_id=dict(aliases=["id"], type="str"),
            drg_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            import_drg_route_distribution_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="drg_route_table",
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

    module.exit_json(drg_route_tables=result)


if __name__ == "__main__":
    main()
