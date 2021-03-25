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
module: oci_network_security_group_vnic_facts
short_description: Fetches details about one or multiple NetworkSecurityGroupVnic resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple NetworkSecurityGroupVnic resources in Oracle Cloud Infrastructure
    - Lists the VNICs in the specified network security group.
version_added: "2.9"
author: Oracle (@oracle)
options:
    network_security_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network security group.
        type: str
        required: true
    sort_by:
        description:
            - The field to sort by.
        type: str
        choices:
            - "TIMEASSOCIATED"
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
- name: List network_security_group_vnics
  oci_network_security_group_vnic_facts:
    network_security_group_id: "ocid1.networksecuritygroup.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
network_security_group_vnics:
    description:
        - List of NetworkSecurityGroupVnic resources
    returned: on success
    type: complex
    contains:
        resource_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the parent resource that the VNIC
                  is attached to (for example, a Compute instance).
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_associated:
            description:
                - The date and time the VNIC was added to the network security group, in the format
                  defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vnic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VNIC.
            returned: on success
            type: string
            sample: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_associated": "2016-08-25T21:10:29.600Z",
        "vnic_id": "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
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


class NetworkSecurityGroupVnicFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "network_security_group_id",
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
            self.client.list_network_security_group_vnics,
            network_security_group_id=self.module.params.get(
                "network_security_group_id"
            ),
            **optional_kwargs
        )


NetworkSecurityGroupVnicFactsHelperCustom = get_custom_class(
    "NetworkSecurityGroupVnicFactsHelperCustom"
)


class ResourceFactsHelper(
    NetworkSecurityGroupVnicFactsHelperCustom, NetworkSecurityGroupVnicFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            network_security_group_id=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["TIMEASSOCIATED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="network_security_group_vnic",
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

    module.exit_json(network_security_group_vnics=result)


if __name__ == "__main__":
    main()
