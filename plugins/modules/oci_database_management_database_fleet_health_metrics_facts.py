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
module: oci_database_management_database_fleet_health_metrics_facts
short_description: Fetches details about a DatabaseFleetHealthMetrics resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a DatabaseFleetHealthMetrics resource in Oracle Cloud Infrastructure
    - Gets the health metrics for a fleet of databases in a compartment or in a Managed Database Group.
      Either the CompartmentId or the ManagedDatabaseGroupId query parameters must be provided to retrieve the health metrics.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compare_baseline_time:
        description:
            - The baseline time for metrics comparison.
        type: str
        required: true
    compare_target_time:
        description:
            - The target time for metrics comparison.
        type: str
        required: true
    managed_database_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database Group.
        type: str
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
    filter_by_database_type:
        description:
            - The filter used to filter the databases in the fleet by a specific Oracle Database type.
        type: str
    filter_by_database_sub_type:
        description:
            - The filter used to filter the databases in the fleet by a specific Oracle Database subtype.
        type: str
    filter_by_database_deployment_type:
        description:
            - The filter used to filter the databases in the fleet by a specific Oracle Database deployment type.
        type: str
    filter_by_database_version:
        description:
            - The filter used to filter the databases in the fleet by a specific Oracle Database version.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific database_fleet_health_metrics
  oci_database_management_database_fleet_health_metrics_facts:
    # required
    compare_baseline_time: compare_baseline_time_example
    compare_target_time: compare_target_time_example

    # optional
    managed_database_group_id: "ocid1.manageddatabasegroup.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    compare_type: HOUR
    filter_by_metric_names: filter_by_metric_names_example
    filter_by_database_type: filter_by_database_type_example
    filter_by_database_sub_type: filter_by_database_sub_type_example
    filter_by_database_deployment_type: filter_by_database_deployment_type_example
    filter_by_database_version: filter_by_database_version_example

"""

RETURN = """
database_fleet_health_metrics:
    description:
        - DatabaseFleetHealthMetrics resource
    returned: on success
    type: complex
    contains:
        compare_baseline_time:
            description:
                - "The baseline date and time in UTC in ISO-8601 format, which is \\"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\\".
                  This is the date and time against which percentage change is calculated."
            returned: on success
            type: str
            sample: compare_baseline_time_example
        compare_target_time:
            description:
                - "The target date and time in UTC in ISO-8601 format, which is \\"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\\".
                  All the metrics are returned for the target date and time and the percentage change
                  is calculated against the baseline date and time."
            returned: on success
            type: str
            sample: compare_target_time_example
        compare_type:
            description:
                - The time window used for metrics comparison.
            returned: on success
            type: str
            sample: HOUR
        fleet_summary:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                aggregated_metrics:
                    description:
                        - A list of databases present in the fleet and their usage metrics.
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
                                - The metric aggregated value at the baseline date and time.
                            returned: on success
                            type: float
                            sample: 1.2
                        target_value:
                            description:
                                - The metric aggregated value at the target date and time.
                            returned: on success
                            type: float
                            sample: 1.2
                        unit:
                            description:
                                - The unit of the value.
                            returned: on success
                            type: str
                            sample: unit_example
                        percentage_change:
                            description:
                                - The percentage change in the metric aggregated value compared to the baseline value.
                            returned: on success
                            type: float
                            sample: 1.2
                        dimensions:
                            description:
                                - The unique dimension key and values of the baseline metric.
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
                inventory:
                    description:
                        - A list of the databases in the fleet, grouped by database type and subtype.
                    returned: on success
                    type: complex
                    contains:
                        database_type:
                            description:
                                - The type of Oracle Database installation.
                            returned: on success
                            type: str
                            sample: EXTERNAL_SIDB
                        database_sub_type:
                            description:
                                - The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-
                                  container Database.
                            returned: on success
                            type: str
                            sample: CDB
                        inventory_count:
                            description:
                                - The number of databases in the fleet.
                            returned: on success
                            type: int
                            sample: 56
        fleet_databases:
            description:
                - A list of the databases present in the fleet and their usage metrics.
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
                        - The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container
                          Database.
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
        "compare_baseline_time": "compare_baseline_time_example",
        "compare_target_time": "compare_target_time_example",
        "compare_type": "HOUR",
        "fleet_summary": {
            "aggregated_metrics": [{
                "metric_name": "metric_name_example",
                "baseline_value": 1.2,
                "target_value": 1.2,
                "unit": "unit_example",
                "percentage_change": 1.2,
                "dimensions": [{
                    "dimension_name": "dimension_name_example",
                    "dimension_value": "dimension_value_example"
                }]
            }],
            "inventory": [{
                "database_type": "EXTERNAL_SIDB",
                "database_sub_type": "CDB",
                "inventory_count": 56
            }]
        },
        "fleet_databases": [{
            "db_id": "ocid1.db.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "database_type": "EXTERNAL_SIDB",
            "database_sub_type": "CDB",
            "deployment_type": "ONPREMISE",
            "database_version": "database_version_example",
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


class DatabaseFleetHealthMetricsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "compare_baseline_time",
            "compare_target_time",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "managed_database_group_id",
            "compartment_id",
            "compare_type",
            "filter_by_metric_names",
            "filter_by_database_type",
            "filter_by_database_sub_type",
            "filter_by_database_deployment_type",
            "filter_by_database_version",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_database_fleet_health_metrics,
            compare_baseline_time=self.module.params.get("compare_baseline_time"),
            compare_target_time=self.module.params.get("compare_target_time"),
            **optional_kwargs
        )


DatabaseFleetHealthMetricsFactsHelperCustom = get_custom_class(
    "DatabaseFleetHealthMetricsFactsHelperCustom"
)


class ResourceFactsHelper(
    DatabaseFleetHealthMetricsFactsHelperCustom,
    DatabaseFleetHealthMetricsFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compare_baseline_time=dict(type="str", required=True),
            compare_target_time=dict(type="str", required=True),
            managed_database_group_id=dict(type="str"),
            compartment_id=dict(type="str"),
            compare_type=dict(type="str", choices=["HOUR", "DAY"]),
            filter_by_metric_names=dict(type="str"),
            filter_by_database_type=dict(type="str"),
            filter_by_database_sub_type=dict(type="str"),
            filter_by_database_deployment_type=dict(type="str"),
            filter_by_database_version=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="database_fleet_health_metrics",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(database_fleet_health_metrics=result)


if __name__ == "__main__":
    main()
