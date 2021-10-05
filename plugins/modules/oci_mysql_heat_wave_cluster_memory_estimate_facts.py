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
module: oci_mysql_heat_wave_cluster_memory_estimate_facts
short_description: Fetches details about a HeatWaveClusterMemoryEstimate resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a HeatWaveClusterMemoryEstimate resource in Oracle Cloud Infrastructure
    - Gets the most recent HeatWave cluster memory estimate that can be used to determine a suitable
      HeatWave cluster size.
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
- name: Get a specific heat_wave_cluster_memory_estimate
  oci_mysql_heat_wave_cluster_memory_estimate_facts:
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
heat_wave_cluster_memory_estimate:
    description:
        - HeatWaveClusterMemoryEstimate resource
    returned: on success
    type: complex
    contains:
        db_system_id:
            description:
                - The OCID of the DB System the HeatWave cluster memory estimate is associated with.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - Current status of the Work Request generating the HeatWave cluster memory estimate.
            returned: on success
            type: str
            sample: ACCEPTED
        time_created:
            description:
                - The date and time that the Work Request to generate the HeatWave cluster memory estimate was issued, as described by L(RFC
                  3339,https://tools.ietf.org/rfc/rfc333).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time that the HeatWave cluster memory estimate was generated, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc333).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        table_schemas:
            description:
                - Collection of schemas with estimated memory footprints for MySQL user tables of each schema
                  when loaded to HeatWave cluster memory.
            returned: on success
            type: complex
            contains:
                schema_name:
                    description:
                        - The name of the schema.
                    returned: on success
                    type: str
                    sample: schema_name_example
                per_table_estimates:
                    description:
                        - Estimated memory footprints for MySQL user tables of the schema
                          when loaded to HeatWave cluster memory.
                    returned: on success
                    type: complex
                    contains:
                        table_name:
                            description:
                                - The table name.
                            returned: on success
                            type: str
                            sample: table_name_example
                        to_load_column_count:
                            description:
                                - The number of columns to be loaded to HeatWave cluster memory.
                                  These columns contribute to the analytical memory footprint.
                            returned: on success
                            type: int
                            sample: 56
                        varlen_column_count:
                            description:
                                - The number of variable-length columns to be loaded to HeatWave cluster memory.
                                  These columns contribute to the analytical memory footprint.
                            returned: on success
                            type: int
                            sample: 56
                        estimated_row_count:
                            description:
                                - The estimated number of rows in the table. This number was used to
                                  derive the analytical memory footprint.
                            returned: on success
                            type: int
                            sample: 56
                        analytical_footprint_in_mbs:
                            description:
                                - The estimated memory footprint of the table in MBs when loaded to
                                  HeatWave cluster memory (null if the table cannot be loaded to the
                                  HeatWave cluster).
                            returned: on success
                            type: int
                            sample: 56
                        error_comment:
                            description:
                                - Error comment (empty string if no errors occured).
                            returned: on success
                            type: str
                            sample: error_comment_example
    sample: {
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "ACCEPTED",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "table_schemas": [{
            "schema_name": "schema_name_example",
            "per_table_estimates": [{
                "table_name": "table_name_example",
                "to_load_column_count": 56,
                "varlen_column_count": 56,
                "estimated_row_count": 56,
                "analytical_footprint_in_mbs": 56,
                "error_comment": "error_comment_example"
            }]
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.mysql import DbSystemClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlHeatWaveClusterMemoryEstimateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "db_system_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_heat_wave_cluster_memory_estimate,
            db_system_id=self.module.params.get("db_system_id"),
        )


MysqlHeatWaveClusterMemoryEstimateFactsHelperCustom = get_custom_class(
    "MysqlHeatWaveClusterMemoryEstimateFactsHelperCustom"
)


class ResourceFactsHelper(
    MysqlHeatWaveClusterMemoryEstimateFactsHelperCustom,
    MysqlHeatWaveClusterMemoryEstimateFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(db_system_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="heat_wave_cluster_memory_estimate",
        service_client_class=DbSystemClient,
        namespace="mysql",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(heat_wave_cluster_memory_estimate=result)


if __name__ == "__main__":
    main()
