#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_database_db_system_compute_performance_facts
short_description: Fetches details about one or multiple DbSystemComputePerformance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DbSystemComputePerformance resources in Oracle Cloud Infrastructure
    - Gets a list of expected compute performance parameters for a virtual machine DB system based on system configuration.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_system_shape:
        description:
            - If provided, filters the results to the set of database versions which are supported for the given shape.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List db_system_compute_performances
  oci_database_db_system_compute_performance_facts:

    # optional
    db_system_shape: db_system_shape_example

"""

RETURN = """
db_system_compute_performances:
    description:
        - List of DbSystemComputePerformance resources
    returned: on success
    type: complex
    contains:
        shape:
            description:
                - The shape of the DB system.
            returned: on success
            type: str
            sample: shape_example
        compute_performance_list:
            description:
                - List of Compute performance details for the specified DB system shape.
            returned: on success
            type: complex
            contains:
                cpu_core_count:
                    description:
                        - The number of OCPU cores available.
                    returned: on success
                    type: int
                    sample: 56
                memory_in_gbs:
                    description:
                        - The amount of memory allocated for the VMDB System.
                    returned: on success
                    type: float
                    sample: 1.2
                network_bandwidth_in_gbps:
                    description:
                        - The network bandwidth of the VMDB system in gbps.
                    returned: on success
                    type: float
                    sample: 3.4
                network_iops:
                    description:
                        - IOPS for the VMDB System.
                    returned: on success
                    type: float
                    sample: 3.4
                network_throughput_in_mbps:
                    description:
                        - Network throughput for the VMDB System.
                    returned: on success
                    type: float
                    sample: 3.4
    sample: [{
        "shape": "shape_example",
        "compute_performance_list": [{
            "cpu_core_count": 56,
            "memory_in_gbs": 1.2,
            "network_bandwidth_in_gbps": 3.4,
            "network_iops": 3.4,
            "network_throughput_in_mbps": 3.4
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DbSystemComputePerformanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "db_system_shape",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_db_system_compute_performances, **optional_kwargs
        )


DbSystemComputePerformanceFactsHelperCustom = get_custom_class(
    "DbSystemComputePerformanceFactsHelperCustom"
)


class ResourceFactsHelper(
    DbSystemComputePerformanceFactsHelperCustom,
    DbSystemComputePerformanceFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(db_system_shape=dict(type="str"),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="db_system_compute_performance",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(db_system_compute_performances=result)


if __name__ == "__main__":
    main()
