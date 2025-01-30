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
module: oci_cloud_migrations_available_shapes_facts
short_description: Fetches details about one or multiple AvailableShapes resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AvailableShapes resources in Oracle Cloud Infrastructure
    - List of shapes by parameters.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    migration_plan_id:
        description:
            - Unique migration plan identifier
        type: str
        required: true
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    dvh_host_id:
        description:
            - The ID of the Dvh in which to list resources.
        type: str
    availability_domain:
        description:
            - The availability domain in which to list resources.
        type: str
    reserved_capacity_id:
        description:
            - The reserved capacity ID for which to list resources.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order can be provided. The default order for 'timeCreated' is descending. The default order for 'displayName'
              is ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List available_shapes
  oci_cloud_migrations_available_shapes_facts:
    # required
    migration_plan_id: "ocid1.migrationplan.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    dvh_host_id: "ocid1.dvhhost.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1
    reserved_capacity_id: "ocid1.reservedcapacity.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
available_shapes:
    description:
        - List of AvailableShapes resources
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - Availability domain of the shape.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        pagination_token:
            description:
                - Shape name and availability domain.  Used for pagination.
            returned: on success
            type: str
            sample: pagination_token_example
        min_total_baseline_ocpus_required:
            description:
                - Minimum CPUs required.
            returned: on success
            type: float
            sample: 10
        shape:
            description:
                - Name of the shape.
            returned: on success
            type: str
            sample: shape_example
        processor_description:
            description:
                - Description of the processor.
            returned: on success
            type: str
            sample: processor_description_example
        ocpus:
            description:
                - Number of CPUs.
            returned: on success
            type: float
            sample: 3.4
        memory_in_gbs:
            description:
                - Amount of memory for the shape.
            returned: on success
            type: float
            sample: 3.4
        networking_bandwidth_in_gbps:
            description:
                - Shape bandwidth.
            returned: on success
            type: float
            sample: 3.4
        max_vnic_attachments:
            description:
                - Maximum number of virtual network interfaces that can be attached.
            returned: on success
            type: int
            sample: 56
        gpus:
            description:
                - Number of GPUs.
            returned: on success
            type: int
            sample: 56
        gpu_description:
            description:
                - Description of the GPUs.
            returned: on success
            type: str
            sample: gpu_description_example
        local_disks:
            description:
                - Number of local disks.
            returned: on success
            type: int
            sample: 56
        local_disks_total_size_in_gbs:
            description:
                - Total size of local disks for shape.
            returned: on success
            type: float
            sample: 3.4
        local_disk_description:
            description:
                - Description of local disks.
            returned: on success
            type: str
            sample: local_disk_description_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "availability_domain": "Uocm:PHX-AD-1",
        "pagination_token": "pagination_token_example",
        "min_total_baseline_ocpus_required": 10,
        "shape": "shape_example",
        "processor_description": "processor_description_example",
        "ocpus": 3.4,
        "memory_in_gbs": 3.4,
        "networking_bandwidth_in_gbps": 3.4,
        "max_vnic_attachments": 56,
        "gpus": 56,
        "gpu_description": "gpu_description_example",
        "local_disks": 56,
        "local_disks_total_size_in_gbs": 3.4,
        "local_disk_description": "local_disk_description_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.cloud_migrations import MigrationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AvailableShapesFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "migration_plan_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "dvh_host_id",
            "availability_domain",
            "reserved_capacity_id",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_available_shapes,
            migration_plan_id=self.module.params.get("migration_plan_id"),
            **optional_kwargs
        )


AvailableShapesFactsHelperCustom = get_custom_class("AvailableShapesFactsHelperCustom")


class ResourceFactsHelper(
    AvailableShapesFactsHelperCustom, AvailableShapesFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            migration_plan_id=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            dvh_host_id=dict(type="str"),
            availability_domain=dict(type="str"),
            reserved_capacity_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="available_shapes",
        service_client_class=MigrationClient,
        namespace="cloud_migrations",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(available_shapes=result)


if __name__ == "__main__":
    main()
