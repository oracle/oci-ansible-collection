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
module: oci_database_db_system_shape_facts
short_description: Fetches details about one or multiple DbSystemShape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DbSystemShape resources in Oracle Cloud Infrastructure
    - "Gets a list of the shapes that can be used to launch a new DB system. The shape determines resources to allocate to the DB system - CPU cores and memory
      for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    availability_domain:
        description:
            - The name of the Availability Domain.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List db_system_shapes
  oci_database_db_system_shape_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    availability_domain: Uocm:PHX-AD-1

"""

RETURN = """
db_system_shapes:
    description:
        - List of DbSystemShape resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the shape used for the DB system.
            returned: on success
            type: str
            sample: name_example
        shape_family:
            description:
                - The family of the shape used for the DB system.
            returned: on success
            type: str
            sample: shape_family_example
        shape:
            description:
                - Deprecated. Use `name` instead of `shape`.
            returned: on success
            type: str
            sample: shape_example
        available_core_count:
            description:
                - The maximum number of CPU cores that can be enabled on the DB system for this shape.
            returned: on success
            type: int
            sample: 56
        minimum_core_count:
            description:
                - The minimum number of CPU cores that can be enabled on the DB system for this shape.
            returned: on success
            type: int
            sample: 56
        core_count_increment:
            description:
                - The discrete number by which the CPU core count for this shape can be increased or decreased.
            returned: on success
            type: int
            sample: 56
        min_storage_count:
            description:
                - The minimum number of Exadata storage servers available for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        max_storage_count:
            description:
                - The maximum number of Exadata storage servers available for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        available_data_storage_per_server_in_tbs:
            description:
                - The maximum data storage available per storage server for this shape. Only applicable to ExaCC Elastic shapes.
            returned: on success
            type: float
            sample: 1.2
        available_memory_per_node_in_gbs:
            description:
                - The maximum memory available per database node for this shape. Only applicable to ExaCC Elastic shapes.
            returned: on success
            type: int
            sample: 56
        available_db_node_per_node_in_gbs:
            description:
                - The maximum Db Node storage available per database node for this shape. Only applicable to ExaCC Elastic shapes.
            returned: on success
            type: int
            sample: 56
        min_core_count_per_node:
            description:
                - The minimum number of CPU cores that can be enabled per node for this shape.
            returned: on success
            type: int
            sample: 56
        available_memory_in_gbs:
            description:
                - The maximum memory that can be enabled for this shape.
            returned: on success
            type: int
            sample: 56
        min_memory_per_node_in_g_bs:
            description:
                - The minimum memory that need be allocated per node for this shape.
            returned: on success
            type: int
            sample: 56
        available_db_node_storage_in_g_bs:
            description:
                - The maximum Db Node storage that can be enabled for this shape.
            returned: on success
            type: int
            sample: 56
        min_db_node_storage_per_node_in_g_bs:
            description:
                - The minimum Db Node storage that need be allocated per node for this shape.
            returned: on success
            type: int
            sample: 56
        available_data_storage_in_t_bs:
            description:
                - The maximum DATA storage that can be enabled for this shape.
            returned: on success
            type: int
            sample: 56
        min_data_storage_in_t_bs:
            description:
                - The minimum data storage that need be allocated for this shape.
            returned: on success
            type: int
            sample: 56
        minimum_node_count:
            description:
                - The minimum number of database nodes available for this shape.
            returned: on success
            type: int
            sample: 56
        maximum_node_count:
            description:
                - The maximum number of database nodes available for this shape.
            returned: on success
            type: int
            sample: 56
        available_core_count_per_node:
            description:
                - The maximum number of CPU cores per database node that can be enabled for this shape. Only applicable to the flex Exadata shape and ExaCC
                  Elastic shapes.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "name": "name_example",
        "shape_family": "shape_family_example",
        "shape": "shape_example",
        "available_core_count": 56,
        "minimum_core_count": 56,
        "core_count_increment": 56,
        "min_storage_count": 56,
        "max_storage_count": 56,
        "available_data_storage_per_server_in_tbs": 1.2,
        "available_memory_per_node_in_gbs": 56,
        "available_db_node_per_node_in_gbs": 56,
        "min_core_count_per_node": 56,
        "available_memory_in_gbs": 56,
        "min_memory_per_node_in_g_bs": 56,
        "available_db_node_storage_in_g_bs": 56,
        "min_db_node_storage_per_node_in_g_bs": 56,
        "available_data_storage_in_t_bs": 56,
        "min_data_storage_in_t_bs": 56,
        "minimum_node_count": 56,
        "maximum_node_count": 56,
        "available_core_count_per_node": 56
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DbSystemShapeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "availability_domain",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_db_system_shapes,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DbSystemShapeFactsHelperCustom = get_custom_class("DbSystemShapeFactsHelperCustom")


class ResourceFactsHelper(DbSystemShapeFactsHelperCustom, DbSystemShapeFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            availability_domain=dict(type="str"),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="db_system_shape",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(db_system_shapes=result)


if __name__ == "__main__":
    main()
