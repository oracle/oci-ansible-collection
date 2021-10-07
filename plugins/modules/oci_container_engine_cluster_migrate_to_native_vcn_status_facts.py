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
module: oci_container_engine_cluster_migrate_to_native_vcn_status_facts
short_description: Fetches details about a ClusterMigrateToNativeVcnStatus resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ClusterMigrateToNativeVcnStatus resource in Oracle Cloud Infrastructure
    - Get details on a cluster's migration to native VCN.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    cluster_id:
        description:
            - The OCID of the cluster.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific cluster_migrate_to_native_vcn_status
  oci_container_engine_cluster_migrate_to_native_vcn_status_facts:
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
cluster_migrate_to_native_vcn_status:
    description:
        - ClusterMigrateToNativeVcnStatus resource
    returned: on success
    type: complex
    contains:
        time_decommission_scheduled:
            description:
                - The date and time the non-native VCN is due to be decommissioned.
            returned: on success
            type: str
            sample: "2017-07-21T16:11:29Z"
        state:
            description:
                - The current migration status of the cluster.
            returned: on success
            type: str
            sample: IN_PROGRESS
    sample: {
        "time_decommission_scheduled": "2017-07-21T16:11:29Z",
        "state": "IN_PROGRESS"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.container_engine import ContainerEngineClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ClusterMigrateToNativeVcnStatusFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "cluster_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cluster_migrate_to_native_vcn_status,
            cluster_id=self.module.params.get("cluster_id"),
        )


ClusterMigrateToNativeVcnStatusFactsHelperCustom = get_custom_class(
    "ClusterMigrateToNativeVcnStatusFactsHelperCustom"
)


class ResourceFactsHelper(
    ClusterMigrateToNativeVcnStatusFactsHelperCustom,
    ClusterMigrateToNativeVcnStatusFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(cluster_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="cluster_migrate_to_native_vcn_status",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(cluster_migrate_to_native_vcn_status=result)


if __name__ == "__main__":
    main()
