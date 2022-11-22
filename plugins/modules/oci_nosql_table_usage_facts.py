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
module: oci_nosql_table_usage_facts
short_description: Fetches details about one or multiple TableUsage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TableUsage resources in Oracle Cloud Infrastructure
    - Get table usage info.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    table_name_or_id:
        description:
            - A table name within the compartment, or a table OCID.
        type: str
        required: true
    compartment_id:
        description:
            - The ID of a table's compartment. When a table is identified
              by name, the compartmentId is often needed to provide
              context for interpreting the name.
        type: str
    time_start:
        description:
            - The start time to use for the request. If no time range
              is set for this request, the most recent complete usage
              record is returned.
        type: str
    time_end:
        description:
            - The end time to use for the request.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List table_usages
  oci_nosql_table_usage_facts:
    # required
    table_name_or_id: "ocid1.tablenameor.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    time_start: 2013-10-20T19:20:30+01:00
    time_end: 2013-10-20T19:20:30+01:00

"""

RETURN = """
table_usages:
    description:
        - List of TableUsage resources
    returned: on success
    type: complex
    contains:
        seconds_in_period:
            description:
                - The length of the sampling period.
            returned: on success
            type: int
            sample: 56
        read_units:
            description:
                - Read throughput during the sampling period.
            returned: on success
            type: int
            sample: 56
        write_units:
            description:
                - Write throughput during the sampling period.
            returned: on success
            type: int
            sample: 56
        storage_in_g_bs:
            description:
                - The size of the table, in GB.
            returned: on success
            type: int
            sample: 56
        read_throttle_count:
            description:
                - The number of times reads were throttled due to exceeding
                  the read throughput limit.
            returned: on success
            type: int
            sample: 56
        write_throttle_count:
            description:
                - The number of times writes were throttled due to exceeding
                  the write throughput limit.
            returned: on success
            type: int
            sample: 56
        storage_throttle_count:
            description:
                - The number of times writes were throttled because the table
                  exceeded its size limit.
            returned: on success
            type: int
            sample: 56
        max_shard_size_usage_in_percent:
            description:
                - The percentage of allowed per-shard usage for the table shard with the highest usage.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "seconds_in_period": 56,
        "read_units": 56,
        "write_units": 56,
        "storage_in_g_bs": 56,
        "read_throttle_count": 56,
        "write_throttle_count": 56,
        "storage_throttle_count": 56,
        "max_shard_size_usage_in_percent": 56
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.nosql import NosqlClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TableUsageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "table_name_or_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "time_start",
            "time_end",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_table_usage,
            table_name_or_id=self.module.params.get("table_name_or_id"),
            **optional_kwargs
        )


TableUsageFactsHelperCustom = get_custom_class("TableUsageFactsHelperCustom")


class ResourceFactsHelper(TableUsageFactsHelperCustom, TableUsageFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            table_name_or_id=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            time_start=dict(type="str"),
            time_end=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="table_usage",
        service_client_class=NosqlClient,
        namespace="nosql",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(table_usages=result)


if __name__ == "__main__":
    main()
