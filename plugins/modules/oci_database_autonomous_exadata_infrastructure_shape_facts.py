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
module: oci_database_autonomous_exadata_infrastructure_shape_facts
short_description: Fetches details about one or multiple AutonomousExadataInfrastructureShape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AutonomousExadataInfrastructureShape resources in Oracle Cloud Infrastructure
    - Gets a list of the shapes that can be used to launch a new Autonomous Exadata Infrastructure resource. The shape determines resources to allocate (CPU
      cores, memory and storage).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    availability_domain:
        description:
            - The name of the Availability Domain.
        type: str
        required: true
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List autonomous_exadata_infrastructure_shapes
  oci_database_autonomous_exadata_infrastructure_shape_facts:
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
autonomous_exadata_infrastructure_shapes:
    description:
        - List of AutonomousExadataInfrastructureShape resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the shape used for the Autonomous Exadata Infrastructure.
            returned: on success
            type: str
            sample: name_example
        available_core_count:
            description:
                - The maximum number of CPU cores that can be enabled on the Autonomous Exadata Infrastructure.
            returned: on success
            type: int
            sample: 56
        minimum_core_count:
            description:
                - The minimum number of CPU cores that can be enabled on the Autonomous Exadata Infrastructure.
            returned: on success
            type: int
            sample: 56
        core_count_increment:
            description:
                - The increment in which core count can be increased or decreased.
            returned: on success
            type: int
            sample: 56
        minimum_node_count:
            description:
                - The minimum number of nodes available for the shape.
            returned: on success
            type: int
            sample: 56
        maximum_node_count:
            description:
                - The maximum number of nodes available for the shape.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "name": "name_example",
        "available_core_count": 56,
        "minimum_core_count": 56,
        "core_count_increment": 56,
        "minimum_node_count": 56,
        "maximum_node_count": 56
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


class AutonomousExadataInfrastructureShapeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "availability_domain",
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_autonomous_exadata_infrastructure_shapes,
            availability_domain=self.module.params.get("availability_domain"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AutonomousExadataInfrastructureShapeFactsHelperCustom = get_custom_class(
    "AutonomousExadataInfrastructureShapeFactsHelperCustom"
)


class ResourceFactsHelper(
    AutonomousExadataInfrastructureShapeFactsHelperCustom,
    AutonomousExadataInfrastructureShapeFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            availability_domain=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="autonomous_exadata_infrastructure_shape",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(autonomous_exadata_infrastructure_shapes=result)


if __name__ == "__main__":
    main()
