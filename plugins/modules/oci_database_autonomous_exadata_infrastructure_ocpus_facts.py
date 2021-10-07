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
module: oci_database_autonomous_exadata_infrastructure_ocpus_facts
short_description: Fetches details about a AutonomousExadataInfrastructureOcpus resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AutonomousExadataInfrastructureOcpus resource in Oracle Cloud Infrastructure
    - Gets details of the available and consumed OCPUs for the specified Autonomous Exadata Infrastructure resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    autonomous_exadata_infrastructure_id:
        description:
            - The Autonomous Exadata Infrastructure  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific autonomous_exadata_infrastructure_ocpus
  oci_database_autonomous_exadata_infrastructure_ocpus_facts:
    autonomous_exadata_infrastructure_id: "ocid1.autonomousexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
autonomous_exadata_infrastructure_ocpus:
    description:
        - AutonomousExadataInfrastructureOcpus resource
    returned: on success
    type: complex
    contains:
        total_cpu:
            description:
                - The total number of OCPUs in the Autonomous Exadata Infrastructure instance.
            returned: on success
            type: float
            sample: 3.4
        consumed_cpu:
            description:
                - The total number of consumed OCPUs in the Autonomous Exadata Infrastructure instance.
            returned: on success
            type: float
            sample: 3.4
        by_workload_type:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                atp:
                    description:
                        - The total number of OCPU cores in use for Autonomous Transaction Processing databases in the infrastructure instance.
                    returned: on success
                    type: float
                    sample: 3.4
                adw:
                    description:
                        - The total number of OCPU cores in use for Autonomous Data Warehouse databases in the infrastructure instance.
                    returned: on success
                    type: float
                    sample: 3.4
    sample: {
        "total_cpu": 3.4,
        "consumed_cpu": 3.4,
        "by_workload_type": {
            "atp": 3.4,
            "adw": 3.4
        }
    }
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


class AutonomousExadataInfrastructureOcpusFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "autonomous_exadata_infrastructure_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_exadata_infrastructure_ocpus,
            autonomous_exadata_infrastructure_id=self.module.params.get(
                "autonomous_exadata_infrastructure_id"
            ),
        )


AutonomousExadataInfrastructureOcpusFactsHelperCustom = get_custom_class(
    "AutonomousExadataInfrastructureOcpusFactsHelperCustom"
)


class ResourceFactsHelper(
    AutonomousExadataInfrastructureOcpusFactsHelperCustom,
    AutonomousExadataInfrastructureOcpusFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            autonomous_exadata_infrastructure_id=dict(
                aliases=["id"], type="str", required=True
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="autonomous_exadata_infrastructure_ocpus",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(autonomous_exadata_infrastructure_ocpus=result)


if __name__ == "__main__":
    main()
