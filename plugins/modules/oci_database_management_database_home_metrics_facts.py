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
module: oci_database_management_database_home_metrics_facts
short_description: Fetches details about a DatabaseHomeMetrics resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a DatabaseHomeMetrics resource in Oracle Cloud Infrastructure
    - Gets a summary of the activity and resource usage metrics like DB Time, CPU, User I/O, Wait, Storage, and Memory for a Managed Database.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific database_home_metrics
  oci_database_management_database_home_metrics_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    start_time: start_time_example
    end_time: end_time_example

"""

RETURN = """
database_home_metrics:
    description:
        - DatabaseHomeMetrics resource
    returned: on success
    type: complex
    contains:
        database_home_metrics:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                activity_time_series_metrics:
                    description:
                        - A list of the active session metrics for CPU and Wait time for a specific database.
                    returned: on success
                    type: complex
                    contains:
                        timestamp:
                            description:
                                - The date and time the activity metric was created.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        cpu_time:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        wait_time:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        user_io_time:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        cpu_count:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        cluster:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                db_time_aggregate_metrics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        cpu_count:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        cpu_time:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        wait_time:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        user_io_time:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        cluster:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                io_aggregate_metrics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        iops:
                            description:
                                - A list of the Input/Output Operations Per Second metrics grouped by IOType for a specific database.
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        io_throughput:
                            description:
                                - A list of the IOThroughput metrics grouped for a specific database.
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                memory_aggregate_metrics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        memory_usage:
                            description:
                                - A list of the memory usage metrics grouped by memorypool for a specific database.
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                db_storage_aggregate_metrics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        storage_allocated:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        storage_used:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        storage_used_by_table_space:
                            description:
                                - A list of the storage metrics grouped by TableSpace for a specific database.
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                cpu_utilization_aggregate_metrics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        cpu_utilization:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                statements_aggregate_metrics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        queued_statements:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        running_statements:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                failed_connections_aggregate_metrics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        failed_connections:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
        database_instance_home_metrics:
            description:
                - The metrics for the RAC database instances.
            returned: on success
            type: complex
            contains:
                instance_name:
                    description:
                        - The name of the Oracle Real Application Clusters (Oracle RAC)
                          database instance to which the corresponding metrics belong.
                    returned: on success
                    type: str
                    sample: instance_name_example
                instance_number:
                    description:
                        - The number of Oracle Real Application Clusters (Oracle RAC)
                          database instance to which the corresponding metrics belong.
                    returned: on success
                    type: int
                    sample: 56
                activity_time_series_metrics:
                    description:
                        - A list of the active session metrics for CPU and Wait time for
                          a specific Oracle Real Application Clusters (Oracle RAC)
                          database instance.
                    returned: on success
                    type: complex
                    contains:
                        timestamp:
                            description:
                                - The date and time the activity metric was created.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        cpu_time:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        wait_time:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        user_io_time:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        cpu_count:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        cluster:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                db_time_aggregate_metrics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        cpu_count:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        cpu_time:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        wait_time:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        user_io_time:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        cluster:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                io_aggregate_metrics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        iops:
                            description:
                                - A list of the Input/Output Operations Per Second metrics grouped by IOType for a specific database.
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                        io_throughput:
                            description:
                                - A list of the IOThroughput metrics grouped for a specific database.
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                memory_aggregate_metrics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        memory_usage:
                            description:
                                - A list of the memory usage metrics grouped by memorypool for a specific database.
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
                cpu_utilization_aggregate_metrics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        cpu_utilization:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                value:
                                    description:
                                        - The value of the metric.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                unit:
                                    description:
                                        - The unit of the metric value.
                                    returned: on success
                                    type: str
                                    sample: unit_example
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
        "database_home_metrics": {
            "activity_time_series_metrics": [{
                "timestamp": "2013-10-20T19:20:30+01:00",
                "cpu_time": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "wait_time": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "user_io_time": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "cpu_count": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "cluster": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                }
            }],
            "db_time_aggregate_metrics": {
                "cpu_count": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "cpu_time": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "wait_time": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "user_io_time": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "cluster": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                }
            },
            "io_aggregate_metrics": {
                "iops": [{
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                }],
                "io_throughput": [{
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                }]
            },
            "memory_aggregate_metrics": {
                "memory_usage": [{
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                }]
            },
            "db_storage_aggregate_metrics": {
                "storage_allocated": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "storage_used": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "storage_used_by_table_space": [{
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                }]
            },
            "cpu_utilization_aggregate_metrics": {
                "cpu_utilization": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                }
            },
            "statements_aggregate_metrics": {
                "queued_statements": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "running_statements": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                }
            },
            "failed_connections_aggregate_metrics": {
                "failed_connections": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                }
            }
        },
        "database_instance_home_metrics": [{
            "instance_name": "instance_name_example",
            "instance_number": 56,
            "activity_time_series_metrics": [{
                "timestamp": "2013-10-20T19:20:30+01:00",
                "cpu_time": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "wait_time": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "user_io_time": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "cpu_count": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "cluster": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                }
            }],
            "db_time_aggregate_metrics": {
                "cpu_count": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "cpu_time": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "wait_time": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "user_io_time": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                },
                "cluster": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                }
            },
            "io_aggregate_metrics": {
                "iops": [{
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                }],
                "io_throughput": [{
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                }]
            },
            "memory_aggregate_metrics": {
                "memory_usage": [{
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                }]
            },
            "cpu_utilization_aggregate_metrics": {
                "cpu_utilization": {
                    "value": 1.2,
                    "unit": "unit_example",
                    "dimensions": [{
                        "dimension_name": "dimension_name_example",
                        "dimension_value": "dimension_value_example"
                    }]
                }
            }
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


class DatabaseHomeMetricsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "managed_database_id",
            "start_time",
            "end_time",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_home_metrics,
            managed_database_id=self.module.params.get("managed_database_id"),
            start_time=self.module.params.get("start_time"),
            end_time=self.module.params.get("end_time"),
        )


DatabaseHomeMetricsFactsHelperCustom = get_custom_class(
    "DatabaseHomeMetricsFactsHelperCustom"
)


class ResourceFactsHelper(
    DatabaseHomeMetricsFactsHelperCustom, DatabaseHomeMetricsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            start_time=dict(type="str", required=True),
            end_time=dict(type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="database_home_metrics",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(database_home_metrics=result)


if __name__ == "__main__":
    main()
