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
module: oci_database_management_pdb_metrics_facts
short_description: Fetches details about a PdbMetrics resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a PdbMetrics resource in Oracle Cloud Infrastructure
    - Gets a summary of the resource usage metrics such as CPU, User I/O, and Storage for each
      PDB within a specific CDB. If comparmentId is specified, then the metrics for
      each PDB (within the CDB) in the specified compartment are retrieved.
      If compartmentId is not specified, then the metrics for all the PDBs within the CDB are retrieved.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        aliases: ["id"]
        required: true
    start_time:
        description:
            - "The start time of the time range to retrieve the health metrics of a Managed Database
              in UTC in ISO-8601 format, which is \\"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\\"."
        type: str
        required: true
    end_time:
        description:
            - "The end time of the time range to retrieve the health metrics of a Managed Database
              in UTC in ISO-8601 format, which is \\"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\\"."
        type: str
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
    compare_type:
        description:
            - The time window used for metrics comparison.
        type: str
        choices:
            - "HOUR"
            - "DAY"
    filter_by_metric_names:
        description:
            - The filter used to retrieve a specific set of metrics by passing the desired metric names with a comma separator. Note that, by default, the
              service returns all supported metrics.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific pdb_metrics
  oci_database_management_pdb_metrics_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    start_time: start_time_example
    end_time: end_time_example

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    compare_type: HOUR
    filter_by_metric_names: filter_by_metric_names_example

"""

RETURN = """
pdb_metrics:
    description:
        - PdbMetrics resource
    returned: on success
    type: complex
    contains:
        database_usage_metrics:
            description:
                - A summary of PDBs and their resource usage metrics such as CPU, User I/O, and Storage, within a specific CDB.
            returned: on success
            type: complex
            contains:
                db_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
                    returned: on success
                    type: str
                    sample: "ocid1.db.oc1..xxxxxxEXAMPLExxxxxx"
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment where the Managed Database
                          resides.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                database_type:
                    description:
                        - The type of Oracle Database installation.
                    returned: on success
                    type: str
                    sample: EXTERNAL_SIDB
                database_sub_type:
                    description:
                        - The subtype of the Oracle Database. Indicates whether the database is a Container Database,
                          Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.
                    returned: on success
                    type: str
                    sample: CDB
                deployment_type:
                    description:
                        - The infrastructure used to deploy the Oracle Database.
                    returned: on success
                    type: str
                    sample: ONPREMISE
                database_version:
                    description:
                        - The Oracle Database version.
                    returned: on success
                    type: str
                    sample: database_version_example
                workload_type:
                    description:
                        - The workload type of the Autonomous Database.
                    returned: on success
                    type: str
                    sample: OLTP
                database_name:
                    description:
                        - The display name of the Managed Database.
                    returned: on success
                    type: str
                    sample: database_name_example
                database_container_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the parent Container Database, in the case of a
                          Pluggable Database.
                    returned: on success
                    type: str
                    sample: "ocid1.databasecontainer.oc1..xxxxxxEXAMPLExxxxxx"
                metrics:
                    description:
                        - A list of the database health metrics like CPU, Storage, and Memory.
                    returned: on success
                    type: complex
                    contains:
                        metric_name:
                            description:
                                - The name of the metric.
                            returned: on success
                            type: str
                            sample: metric_name_example
                        baseline_value:
                            description:
                                - The baseline value of the metric.
                            returned: on success
                            type: float
                            sample: 1.2
                        target_value:
                            description:
                                - The target value of the metric.
                            returned: on success
                            type: float
                            sample: 1.2
                        unit:
                            description:
                                - The unit of the value.
                            returned: on success
                            type: str
                            sample: unit_example
                        timestamp:
                            description:
                                - "The data point date and time in UTC in ISO-8601 format, which is \\"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\\"."
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        percentage_change:
                            description:
                                - The percentage change in the metric aggregated value compared to the baseline value.
                            returned: on success
                            type: float
                            sample: 1.2
                        dimensions:
                            description:
                                - The dimensions of the metric.
                            returned: on success
                            type: complex
                            contains:
                                dimension_name:
                                    description:
                                        - The name of the dimension.
                                    returned: on success
                                    type: str
                                    sample: dimension_name_example
                                dimension_value:
                                    description:
                                        - The value of the dimension.
                                    returned: on success
                                    type: str
                                    sample: dimension_value_example
    sample: {
        "database_usage_metrics": [{
            "db_id": "ocid1.db.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "database_type": "EXTERNAL_SIDB",
            "database_sub_type": "CDB",
            "deployment_type": "ONPREMISE",
            "database_version": "database_version_example",
            "workload_type": "OLTP",
            "database_name": "database_name_example",
            "database_container_id": "ocid1.databasecontainer.oc1..xxxxxxEXAMPLExxxxxx",
            "metrics": [{
                "metric_name": "metric_name_example",
                "baseline_value": 1.2,
                "target_value": 1.2,
                "unit": "unit_example",
                "timestamp": "2013-10-20T19:20:30+01:00",
                "percentage_change": 1.2,
                "dimensions": [{
                    "dimension_name": "dimension_name_example",
                    "dimension_value": "dimension_value_example"
                }]
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
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PdbMetricsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "managed_database_id",
            "start_time",
            "end_time",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "compartment_id",
            "compare_type",
            "filter_by_metric_names",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_pdb_metrics,
            managed_database_id=self.module.params.get("managed_database_id"),
            start_time=self.module.params.get("start_time"),
            end_time=self.module.params.get("end_time"),
            **optional_kwargs
        )


PdbMetricsFactsHelperCustom = get_custom_class("PdbMetricsFactsHelperCustom")


class ResourceFactsHelper(PdbMetricsFactsHelperCustom, PdbMetricsFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(aliases=["id"], type="str", required=True),
            start_time=dict(type="str", required=True),
            end_time=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            compare_type=dict(type="str", choices=["HOUR", "DAY"]),
            filter_by_metric_names=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="pdb_metrics",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(pdb_metrics=result)


if __name__ == "__main__":
    main()
