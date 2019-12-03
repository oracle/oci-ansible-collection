#!/usr/bin/python
# Copyright (c) 2017, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_network_security_group_facts
short_description: Fetches details about one or multiple NetworkSecurityGroup resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple NetworkSecurityGroup resources in Oracle Cloud Infrastructure
    - Lists the network security groups in the specified compartment.
    - If I(network_security_group_id) is specified, the details of a single NetworkSecurityGroup will be returned.
version_added: "2.5"
options:
    network_security_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security group.
            - Required to get a specific network_security_group.
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple network_security_groups.
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
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
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to return only resources that match the specified lifecycle state. The value is case insensitive.
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "TERMINATING"
            - "TERMINATED"
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: List network_security_groups
  oci_network_security_group_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific network_security_group
  oci_network_security_group_facts:
    network_security_group_id: ocid1.networksecuritygroup.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
network_security_groups:
    description:
        - List of NetworkSecurityGroup resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment the network security group is in.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security group.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The network security group's current state.
            returned: on success
            type: string
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the network security group was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security group's VCN.
            returned: on success
            type: string
            sample: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "time_created": "2016-08-25T21:10:29.600Z",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkSecurityGroupFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return ["network_security_group_id"]

    def get_required_params_for_list(self):
        return ["compartment_id"]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_network_security_group,
            network_security_group_id=self.module.params.get(
                "network_security_group_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "vcn_id",
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
            self.client.list_network_security_groups,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


NetworkSecurityGroupFactsHelperCustom = get_custom_class(
    "NetworkSecurityGroupFactsHelperCustom"
)


class ResourceFactsHelper(
    NetworkSecurityGroupFactsHelperCustom, NetworkSecurityGroupFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            network_security_group_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            vcn_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
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
        resource_type="network_security_group",
        service_client_class=VirtualNetworkClient,
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(network_security_groups=result)


if __name__ == "__main__":
    main()
