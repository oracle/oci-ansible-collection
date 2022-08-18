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
module: oci_resource_manager_reachable_ip_facts
short_description: Fetches details about a ReachableIp resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ReachableIp resource in Oracle Cloud Infrastructure
    - Gets the reachable, or alternative, IP address for a nonpublic IP address that is associated with the private endpoint.
      Resource Manager uses this IP address to connect to nonpublic resources through the associated private endpoint.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    private_ip:
        description:
            - The IP address of the resource in the private subnet.
        type: str
        required: true
    private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the private endpoint.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific reachable_ip
  oci_resource_manager_reachable_ip_facts:
    # required
    private_ip: private_ip_example
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
reachable_ip:
    description:
        - ReachableIp resource
    returned: on success
    type: complex
    contains:
        ip_address:
            description:
                - Reachable IP address associated with the private endpoint.
            returned: on success
            type: str
            sample: ip_address_example
    sample: {
        "ip_address": "ip_address_example"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.resource_manager import ResourceManagerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ReachableIpFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "private_ip",
            "private_endpoint_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_reachable_ip,
            private_ip=self.module.params.get("private_ip"),
            private_endpoint_id=self.module.params.get("private_endpoint_id"),
        )


ReachableIpFactsHelperCustom = get_custom_class("ReachableIpFactsHelperCustom")


class ResourceFactsHelper(ReachableIpFactsHelperCustom, ReachableIpFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            private_ip=dict(type="str", required=True),
            private_endpoint_id=dict(aliases=["id"], type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="reachable_ip",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(reachable_ip=result)


if __name__ == "__main__":
    main()
