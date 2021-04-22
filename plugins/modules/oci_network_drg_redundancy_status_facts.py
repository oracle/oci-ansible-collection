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
module: oci_network_drg_redundancy_status_facts
short_description: Fetches details about a DrgRedundancyStatus resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a DrgRedundancyStatus resource in Oracle Cloud Infrastructure
    - Gets the redundancy status for the specified DRG. For more information, see
      L(Redundancy Remedies,https://docs.cloud.oracle.com/iaas/Content/Network/Troubleshoot/drgredundancy.htm).
version_added: "2.9"
author: Oracle (@oracle)
options:
    drg_id:
        description:
            - The L([OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific drg_redundancy_status
  oci_network_drg_redundancy_status_facts:
    drg_id: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
drg_redundancy_status:
    description:
        - DrgRedundancyStatus resource
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DRG.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - The redundancy status of the DRG.
            returned: on success
            type: string
            sample: NOT_AVAILABLE
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "NOT_AVAILABLE"
    }
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


class DrgRedundancyStatusFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "drg_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_drg_redundancy_status,
            drg_id=self.module.params.get("drg_id"),
        )


DrgRedundancyStatusFactsHelperCustom = get_custom_class(
    "DrgRedundancyStatusFactsHelperCustom"
)


class ResourceFactsHelper(
    DrgRedundancyStatusFactsHelperCustom, DrgRedundancyStatusFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(drg_id=dict(aliases=["id"], type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="drg_redundancy_status",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(drg_redundancy_status=result)


if __name__ == "__main__":
    main()
