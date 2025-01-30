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
module: oci_network_drg_upgrade_status_facts
short_description: Fetches details about a DrgUpgradeStatus resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a DrgUpgradeStatus resource in Oracle Cloud Infrastructure
    - Returns the DRG upgrade status. The status can be not updated, in progress, or updated. Also indicates how much of the upgrade is completed.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    drg_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific drg_upgrade_status
  oci_network_drg_upgrade_status_facts:
    # required
    drg_id: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
drg_upgrade_status:
    description:
        - DrgUpgradeStatus resource
    returned: on success
    type: complex
    contains:
        drg_id:
            description:
                - The `drgId` of the upgraded DRG.
            returned: on success
            type: str
            sample: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - The current upgrade status of the DRG attachment.
            returned: on success
            type: str
            sample: NOT_UPGRADED
        upgraded_connections:
            description:
                - The number of upgraded connections.
            returned: on success
            type: str
            sample: upgraded_connections_example
    sample: {
        "drg_id": "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "NOT_UPGRADED",
        "upgraded_connections": "upgraded_connections_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrgUpgradeStatusFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "drg_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_upgrade_status, drg_id=self.module.params.get("drg_id"),
        )


DrgUpgradeStatusFactsHelperCustom = get_custom_class(
    "DrgUpgradeStatusFactsHelperCustom"
)


class ResourceFactsHelper(
    DrgUpgradeStatusFactsHelperCustom, DrgUpgradeStatusFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(drg_id=dict(aliases=["id"], type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="drg_upgrade_status",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(drg_upgrade_status=result)


if __name__ == "__main__":
    main()
