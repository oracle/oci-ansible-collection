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
module: oci_database_db_system_storage_performance_facts
short_description: Fetches details about one or multiple DbSystemStoragePerformance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DbSystemStoragePerformance resources in Oracle Cloud Infrastructure
    - Gets a list of possible expected storage performance parameters of a VMDB System based on Configuration.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    storage_management:
        description:
            - "The DB system storage management option. Used to list database versions available for that storage manager. Valid values are `ASM` and `LVM`.
              * ASM specifies Oracle Automatic Storage Management
              * LVM specifies logical volume manager, sometimes called logical disk manager."
        type: str
        choices:
            - "ASM"
            - "LVM"
        required: true
    shape_type:
        description:
            - Optional. Filters the performance results by shape type.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List db_system_storage_performances
  oci_database_db_system_storage_performance_facts:
    # required
    storage_management: ASM

    # optional
    shape_type: shape_type_example

"""

RETURN = """
db_system_storage_performances:
    description:
        - List of DbSystemStoragePerformance resources
    returned: on success
    type: complex
    contains:
        shape_type:
            description:
                - ShapeType of the DbSystems,INTEL or AMD
            returned: on success
            type: str
            sample: AMD
        data_storage_performance_list:
            description:
                - List of storage performance for the DATA disks
            returned: on success
            type: complex
            contains:
                size_in_gbs:
                    description:
                        - Size in GBs.
                    returned: on success
                    type: int
                    sample: 56
                balanced_disk_performance:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        disk_iops:
                            description:
                                - Disk IOPS in thousands.
                            returned: on success
                            type: float
                            sample: 3.4
                        disk_throughput_in_mbps:
                            description:
                                - Disk Throughput in Mbps.
                            returned: on success
                            type: float
                            sample: 3.4
                high_disk_performance:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        disk_iops:
                            description:
                                - Disk IOPS in thousands.
                            returned: on success
                            type: float
                            sample: 3.4
                        disk_throughput_in_mbps:
                            description:
                                - Disk Throughput in Mbps.
                            returned: on success
                            type: float
                            sample: 3.4
        reco_storage_performance_list:
            description:
                - List of storage performance for the RECO disks
            returned: on success
            type: complex
            contains:
                size_in_gbs:
                    description:
                        - Size in GBs.
                    returned: on success
                    type: int
                    sample: 56
                balanced_disk_performance:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        disk_iops:
                            description:
                                - Disk IOPS in thousands.
                            returned: on success
                            type: float
                            sample: 3.4
                        disk_throughput_in_mbps:
                            description:
                                - Disk Throughput in Mbps.
                            returned: on success
                            type: float
                            sample: 3.4
                high_disk_performance:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        disk_iops:
                            description:
                                - Disk IOPS in thousands.
                            returned: on success
                            type: float
                            sample: 3.4
                        disk_throughput_in_mbps:
                            description:
                                - Disk Throughput in Mbps.
                            returned: on success
                            type: float
                            sample: 3.4
    sample: [{
        "shape_type": "AMD",
        "data_storage_performance_list": [{
            "size_in_gbs": 56,
            "balanced_disk_performance": {
                "disk_iops": 3.4,
                "disk_throughput_in_mbps": 3.4
            },
            "high_disk_performance": {
                "disk_iops": 3.4,
                "disk_throughput_in_mbps": 3.4
            }
        }],
        "reco_storage_performance_list": [{
            "size_in_gbs": 56,
            "balanced_disk_performance": {
                "disk_iops": 3.4,
                "disk_throughput_in_mbps": 3.4
            },
            "high_disk_performance": {
                "disk_iops": 3.4,
                "disk_throughput_in_mbps": 3.4
            }
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


class DbSystemStoragePerformanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "storage_management",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "shape_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_db_system_storage_performances,
            storage_management=self.module.params.get("storage_management"),
            **optional_kwargs
        )


DbSystemStoragePerformanceFactsHelperCustom = get_custom_class(
    "DbSystemStoragePerformanceFactsHelperCustom"
)


class ResourceFactsHelper(
    DbSystemStoragePerformanceFactsHelperCustom,
    DbSystemStoragePerformanceFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            storage_management=dict(type="str", required=True, choices=["ASM", "LVM"]),
            shape_type=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="db_system_storage_performance",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(db_system_storage_performances=result)


if __name__ == "__main__":
    main()
