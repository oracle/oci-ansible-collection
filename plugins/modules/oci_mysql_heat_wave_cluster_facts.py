#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_mysql_heat_wave_cluster_facts
short_description: Fetches details about a HeatWaveCluster resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a HeatWaveCluster resource in Oracle Cloud Infrastructure
    - Gets information about the HeatWave cluster.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_system_id:
        description:
            - The DB System L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific heat_wave_cluster
  oci_mysql_heat_wave_cluster_facts:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
heat_wave_cluster:
    description:
        - HeatWaveCluster resource
    returned: on success
    type: complex
    contains:
        db_system_id:
            description:
                - The OCID of the parent DB System this HeatWave cluster is attached to.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        shape_name:
            description:
                - "The shape determines resources to allocate to the HeatWave
                  nodes - CPU cores, memory."
            returned: on success
            type: str
            sample: shape_name_example
        cluster_size:
            description:
                - The number of analytics-processing compute instances, of the
                  specified shape, in the HeatWave cluster.
            returned: on success
            type: int
            sample: 56
        is_lakehouse_enabled:
            description:
                - Lakehouse enabled status for the HeatWave cluster.
            returned: on success
            type: bool
            sample: true
        cluster_nodes:
            description:
                - A HeatWave node is a compute host that is part of a HeatWave cluster.
            returned: on success
            type: complex
            contains:
                node_id:
                    description:
                        - The ID of the node within MySQL HeatWave cluster.
                    returned: on success
                    type: str
                    sample: "ocid1.node.oc1..xxxxxxEXAMPLExxxxxx"
                lifecycle_state:
                    description:
                        - The current state of the MySQL HeatWave node.
                    returned: on success
                    type: str
                    sample: CREATING
                time_created:
                    description:
                        - The date and time the MySQL HeatWave node was created,
                          as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The date and time the MySQL HeatWave node was updated,
                          as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the HeatWave cluster.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the HeatWave cluster was created,
                  as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the HeatWave cluster was last updated,
                  as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "shape_name": "shape_name_example",
        "cluster_size": 56,
        "is_lakehouse_enabled": true,
        "cluster_nodes": [{
            "node_id": "ocid1.node.oc1..xxxxxxEXAMPLExxxxxx",
            "lifecycle_state": "CREATING",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00"
        }],
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.mysql import DbSystemClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlHeatWaveClusterFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "db_system_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_heat_wave_cluster,
            db_system_id=self.module.params.get("db_system_id"),
        )


MysqlHeatWaveClusterFactsHelperCustom = get_custom_class(
    "MysqlHeatWaveClusterFactsHelperCustom"
)


class ResourceFactsHelper(
    MysqlHeatWaveClusterFactsHelperCustom, MysqlHeatWaveClusterFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(db_system_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="heat_wave_cluster",
        service_client_class=DbSystemClient,
        namespace="mysql",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(heat_wave_cluster=result)


if __name__ == "__main__":
    main()
