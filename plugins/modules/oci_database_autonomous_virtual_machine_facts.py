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
module: oci_database_autonomous_virtual_machine_facts
short_description: Fetches details about one or multiple AutonomousVirtualMachine resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AutonomousVirtualMachine resources in Oracle Cloud Infrastructure
    - Lists the Autonomous Virtual Machines in the specified Autonomous VM Cluster and Compartment.
    - If I(autonomous_virtual_machine_id) is specified, the details of a single AutonomousVirtualMachine will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    autonomous_virtual_machine_id:
        description:
            - The Autonomous Virtual machine L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific autonomous_virtual_machine.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple autonomous_virtual_machines.
        type: str
    autonomous_vm_cluster_id:
        description:
            - The Autonomous Virtual machine L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple autonomous_virtual_machines.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state exactly.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "UPDATING"
            - "TERMINATING"
            - "TERMINATED"
            - "FAILED"
            - "MAINTENANCE_IN_PROGRESS"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific autonomous_virtual_machine
  oci_database_autonomous_virtual_machine_facts:
    # required
    autonomous_virtual_machine_id: "ocid1.autonomousvirtualmachine.oc1..xxxxxxEXAMPLExxxxxx"

- name: List autonomous_virtual_machines
  oci_database_autonomous_virtual_machine_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_vm_cluster_id: "ocid1.autonomousvmcluster.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: PROVISIONING

"""

RETURN = """
autonomous_virtual_machines:
    description:
        - List of AutonomousVirtualMachine resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous Virtual Machine.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        vm_name:
            description:
                - The name of the Autonomous Virtual Machine.
            returned: on success
            type: str
            sample: vm_name_example
        db_server_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Db server associated with the Autonomous Virtual
                  Machine.
            returned: on success
            type: str
            sample: "ocid1.dbserver.oc1..xxxxxxEXAMPLExxxxxx"
        db_server_display_name:
            description:
                - The display name of the dbServer associated with the Autonomous Virtual Machine.
            returned: on success
            type: str
            sample: db_server_display_name_example
        cpu_core_count:
            description:
                - The number of CPU cores enabled on the Autonomous Virtual Machine.
            returned: on success
            type: int
            sample: 56
        memory_size_in_gbs:
            description:
                - The allocated memory in GBs on the Autonomous Virtual Machine.
            returned: on success
            type: int
            sample: 56
        db_node_storage_size_in_gbs:
            description:
                - The allocated local node storage in GBs on the Autonomous Virtual Machine.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of the Autonomous Virtual Machine.
            returned: on success
            type: str
            sample: PROVISIONING
        client_ip_address:
            description:
                - Client IP Address.
            returned: on success
            type: str
            sample: client_ip_address_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        autonomous_vm_cluster_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous VM Cluster associated with the Autonomous
                  Virtual Machine.
            returned: on success
            type: str
            sample: "ocid1.autonomousvmcluster.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        cloud_autonomous_vm_cluster_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Cloud Autonomous VM Cluster associated with the
                  Autonomous Virtual Machine.
            returned: on success
            type: str
            sample: "ocid1.cloudautonomousvmcluster.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "vm_name": "vm_name_example",
        "db_server_id": "ocid1.dbserver.oc1..xxxxxxEXAMPLExxxxxx",
        "db_server_display_name": "db_server_display_name_example",
        "cpu_core_count": 56,
        "memory_size_in_gbs": 56,
        "db_node_storage_size_in_gbs": 56,
        "lifecycle_state": "PROVISIONING",
        "client_ip_address": "client_ip_address_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "autonomous_vm_cluster_id": "ocid1.autonomousvmcluster.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "cloud_autonomous_vm_cluster_id": "ocid1.cloudautonomousvmcluster.oc1..xxxxxxEXAMPLExxxxxx"
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


class AutonomousVirtualMachineFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "autonomous_virtual_machine_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "autonomous_vm_cluster_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_virtual_machine,
            autonomous_virtual_machine_id=self.module.params.get(
                "autonomous_virtual_machine_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_autonomous_virtual_machines,
            compartment_id=self.module.params.get("compartment_id"),
            autonomous_vm_cluster_id=self.module.params.get("autonomous_vm_cluster_id"),
            **optional_kwargs
        )


AutonomousVirtualMachineFactsHelperCustom = get_custom_class(
    "AutonomousVirtualMachineFactsHelperCustom"
)


class ResourceFactsHelper(
    AutonomousVirtualMachineFactsHelperCustom, AutonomousVirtualMachineFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            autonomous_virtual_machine_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            autonomous_vm_cluster_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "AVAILABLE",
                    "UPDATING",
                    "TERMINATING",
                    "TERMINATED",
                    "FAILED",
                    "MAINTENANCE_IN_PROGRESS",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="autonomous_virtual_machine",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(autonomous_virtual_machines=result)


if __name__ == "__main__":
    main()
