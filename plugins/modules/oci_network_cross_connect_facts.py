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
module: oci_network_cross_connect_facts
short_description: Fetches details about one or multiple CrossConnect resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CrossConnect resources in Oracle Cloud Infrastructure
    - Lists the cross-connects in the specified compartment. You can filter the list
      by specifying the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a cross-connect group.
    - If I(cross_connect_id) is specified, the details of a single CrossConnect will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    cross_connect_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cross-connect.
            - Required to get a specific cross_connect.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple cross_connects.
        type: str
    cross_connect_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cross-connect group.
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
            - "PENDING_CUSTOMER"
            - "PROVISIONING"
            - "PROVISIONED"
            - "INACTIVE"
            - "TERMINATING"
            - "TERMINATED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List cross_connects
  oci_network_cross_connect_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific cross_connect
  oci_network_cross_connect_facts:
    cross_connect_id: "ocid1.crossconnect.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
cross_connects:
    description:
        - List of CrossConnect resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment containing the cross-connect group.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        cross_connect_group_id:
            description:
                - The OCID of the cross-connect group this cross-connect belongs to (if any).
            returned: on success
            type: string
            sample: "ocid1.crossconnectgroup.oc1..xxxxxxEXAMPLExxxxxx"
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
                - The cross-connect's Oracle ID (OCID).
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The cross-connect's current state.
            returned: on success
            type: string
            sample: PENDING_CUSTOMER
        location_name:
            description:
                - The name of the FastConnect location where this cross-connect is installed.
            returned: on success
            type: string
            sample: location_name_example
        port_name:
            description:
                - A string identifying the meet-me room port for this cross-connect.
            returned: on success
            type: string
            sample: port_name_example
        port_speed_shape_name:
            description:
                - The port speed for this cross-connect.
                - "Example: `10 Gbps`"
            returned: on success
            type: string
            sample: 10 Gbps
        customer_reference_name:
            description:
                - A reference name or identifier for the physical fiber connection that this cross-connect
                  uses.
            returned: on success
            type: string
            sample: customer_reference_name_example
        time_created:
            description:
                - The date and time the cross-connect was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "cross_connect_group_id": "ocid1.crossconnectgroup.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PENDING_CUSTOMER",
        "location_name": "location_name_example",
        "port_name": "port_name_example",
        "port_speed_shape_name": "10 Gbps",
        "customer_reference_name": "customer_reference_name_example",
        "time_created": "2016-08-25T21:10:29.600Z"
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


class CrossConnectFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "cross_connect_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cross_connect,
            cross_connect_id=self.module.params.get("cross_connect_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "cross_connect_group_id",
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
            self.client.list_cross_connects,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


CrossConnectFactsHelperCustom = get_custom_class("CrossConnectFactsHelperCustom")


class ResourceFactsHelper(CrossConnectFactsHelperCustom, CrossConnectFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            cross_connect_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            cross_connect_group_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PENDING_CUSTOMER",
                    "PROVISIONING",
                    "PROVISIONED",
                    "INACTIVE",
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
        resource_type="cross_connect",
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

    module.exit_json(cross_connects=result)


if __name__ == "__main__":
    main()
