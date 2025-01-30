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
module: oci_cloud_bridge_asset_source_connection_facts
short_description: Fetches details about one or multiple AssetSourceConnection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AssetSourceConnection resources in Oracle Cloud Infrastructure
    - Gets known connections to the asset source by the asset source ID.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    asset_source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the asset source.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List asset_source_connections
  oci_cloud_bridge_asset_source_connection_facts:
    # required
    asset_source_id: "ocid1.assetsource.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
asset_source_connections:
    description:
        - List of AssetSourceConnection resources
    returned: on success
    type: complex
    contains:
        connection_type:
            description:
                - The type of connection for an asset source.
            returned: on success
            type: str
            sample: DISCOVERY
        connector_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cloud bridge connector used for migration
                  operations.
            returned: on success
            type: str
            sample: "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx"
        asset_source_key:
            description:
                - Type-specific identifier for an asset source.
            returned: on success
            type: str
            sample: asset_source_key_example
        lifecycle_state:
            description:
                - The current state of the connection.
            returned: on success
            type: str
            sample: ACTIVE
        lifecycle_details:
            description:
                - The detailed sub-state of the connection.
            returned: on success
            type: str
            sample: lifecycle_details_example
    sample: [{
        "connection_type": "DISCOVERY",
        "connector_id": "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx",
        "asset_source_key": "asset_source_key_example",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.cloud_bridge import DiscoveryClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AssetSourceConnectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "asset_source_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_asset_source_connections,
            asset_source_id=self.module.params.get("asset_source_id"),
            **optional_kwargs
        )


AssetSourceConnectionFactsHelperCustom = get_custom_class(
    "AssetSourceConnectionFactsHelperCustom"
)


class ResourceFactsHelper(
    AssetSourceConnectionFactsHelperCustom, AssetSourceConnectionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(asset_source_id=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="asset_source_connection",
        service_client_class=DiscoveryClient,
        namespace="cloud_bridge",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(asset_source_connections=result)


if __name__ == "__main__":
    main()
