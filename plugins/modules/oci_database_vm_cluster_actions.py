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
module: oci_database_vm_cluster_actions
short_description: Perform actions on a VmCluster resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a VmCluster resource in Oracle Cloud Infrastructure
    - For I(action=add_virtual_machine), add Virtual Machines to the VM cluster. Applies to Exadata Cloud@Customer instances only.
    - For I(action=change_compartment), moves a VM cluster and its dependent resources to another compartment. Applies to Exadata Cloud@Customer instances only.
      To move a cloud VM cluster in an Exadata Cloud Service instance to another compartment, use the L(ChangeCloudVmClusterCompartment
      ,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/latest/CloudVmCluster/ChangeCloudVmClusterCompartment) operation.
    - For I(action=remove_virtual_machine), remove Virtual Machines from the VM cluster. Applies to Exadata Cloud@Customer instances only.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the VM cluster to.
            - Required for I(action=change_compartment).
        type: str
    db_servers:
        description:
            - The list of Exacc DB servers for the cluster to be added.
            - Required for I(action=add_virtual_machine), I(action=remove_virtual_machine).
        type: list
        elements: dict
        suboptions:
            db_server_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of Exacc Db server.
                type: str
                required: true
    vm_cluster_id:
        description:
            - The VM cluster L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the VmCluster.
        type: str
        required: true
        choices:
            - "add_virtual_machine"
            - "change_compartment"
            - "remove_virtual_machine"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_virtual_machine on vm_cluster
  oci_database_vm_cluster_actions:
    # required
    db_servers:
    - # required
      db_server_id: "ocid1.dbserver.oc1..xxxxxxEXAMPLExxxxxx"
    vm_cluster_id: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"
    action: add_virtual_machine

- name: Perform action change_compartment on vm_cluster
  oci_database_vm_cluster_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    vm_cluster_id: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action remove_virtual_machine on vm_cluster
  oci_database_vm_cluster_actions:
    # required
    db_servers:
    - # required
      db_server_id: "ocid1.dbserver.oc1..xxxxxxEXAMPLExxxxxx"
    vm_cluster_id: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_virtual_machine

"""

RETURN = """
vm_cluster:
    description:
        - Details of the VmCluster resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM cluster.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        last_patch_history_entry_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last patch history. This value is updated as soon as
                  a patch operation starts.
            returned: on success
            type: str
            sample: "ocid1.lastpatchhistoryentry.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the VM cluster.
            returned: on success
            type: str
            sample: PROVISIONING
        display_name:
            description:
                - The user-friendly name for the Exadata Cloud@Customer VM cluster. The name does not need to be unique.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The date and time that the VM cluster was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_zone:
            description:
                - The time zone of the Exadata infrastructure. For details, see L(Exadata Infrastructure Time
                  Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
            returned: on success
            type: str
            sample: time_zone_example
        is_local_backup_enabled:
            description:
                - If true, database backup on local Exadata storage is configured for the VM cluster. If false, database backup on local Exadata storage is not
                  available in the VM cluster.
            returned: on success
            type: bool
            sample: true
        exadata_infrastructure_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
            returned: on success
            type: str
            sample: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
        is_sparse_diskgroup_enabled:
            description:
                - If true, sparse disk group is configured for the VM cluster. If false, sparse disk group is not created.
            returned: on success
            type: bool
            sample: true
        vm_cluster_network_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM cluster network.
            returned: on success
            type: str
            sample: "ocid1.vmclusternetwork.oc1..xxxxxxEXAMPLExxxxxx"
        cpus_enabled:
            description:
                - The number of enabled CPU cores.
            returned: on success
            type: int
            sample: 56
        ocpus_enabled:
            description:
                - The number of enabled OCPU cores.
            returned: on success
            type: float
            sample: 3.4
        memory_size_in_gbs:
            description:
                - The memory allocated in GBs.
            returned: on success
            type: int
            sample: 56
        db_node_storage_size_in_gbs:
            description:
                - The local node storage allocated in GBs.
            returned: on success
            type: int
            sample: 56
        data_storage_size_in_tbs:
            description:
                - Size, in terabytes, of the DATA disk group.
            returned: on success
            type: float
            sample: 1.2
        data_storage_size_in_gbs:
            description:
                - Size of the DATA disk group in GBs.
            returned: on success
            type: float
            sample: 1.2
        shape:
            description:
                - The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.
            returned: on success
            type: str
            sample: shape_example
        gi_version:
            description:
                - The Oracle Grid Infrastructure software version for the VM cluster.
            returned: on success
            type: str
            sample: gi_version_example
        system_version:
            description:
                - Operating system version of the image.
            returned: on success
            type: str
            sample: system_version_example
        ssh_public_keys:
            description:
                - The public key portion of one or more key pairs used for SSH access to the VM cluster.
            returned: on success
            type: list
            sample: [ ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz... ]
        license_model:
            description:
                - The Oracle license model that applies to the VM cluster. The default is LICENSE_INCLUDED.
            returned: on success
            type: str
            sample: LICENSE_INCLUDED
        db_servers:
            description:
                - The list of Db server.
            returned: on success
            type: list
            sample: []
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
        data_collection_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_diagnostics_events_enabled:
                    description:
                        - Indicates whether diagnostic collection is enabled for the VM cluster/Cloud VM cluster/VMBM DBCS. Enabling diagnostic collection
                          allows you to receive Events service notifications for guest VM issues. Diagnostic collection also allows Oracle to provide enhanced
                          service and proactive support for your Exadata system. You can enable diagnostic collection during VM cluster/Cloud VM cluster
                          provisioning. You can also disable or enable it at any time using the `UpdateVmCluster` or `updateCloudVmCluster` API.
                    returned: on success
                    type: bool
                    sample: true
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "last_patch_history_entry_id": "ocid1.lastpatchhistoryentry.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "time_zone": "time_zone_example",
        "is_local_backup_enabled": true,
        "exadata_infrastructure_id": "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx",
        "is_sparse_diskgroup_enabled": true,
        "vm_cluster_network_id": "ocid1.vmclusternetwork.oc1..xxxxxxEXAMPLExxxxxx",
        "cpus_enabled": 56,
        "ocpus_enabled": 3.4,
        "memory_size_in_gbs": 56,
        "db_node_storage_size_in_gbs": 56,
        "data_storage_size_in_tbs": 1.2,
        "data_storage_size_in_gbs": 1.2,
        "shape": "shape_example",
        "gi_version": "gi_version_example",
        "system_version": "system_version_example",
        "ssh_public_keys": [ ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz... ],
        "license_model": "LICENSE_INCLUDED",
        "db_servers": [],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "data_collection_options": {
            "is_diagnostics_events_enabled": true
        }
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import AddVirtualMachineToVmClusterDetails
    from oci.database.models import ChangeVmClusterCompartmentDetails
    from oci.database.models import RemoveVirtualMachineFromVmClusterDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VmClusterActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_virtual_machine
        change_compartment
        remove_virtual_machine
    """

    def __init__(self, *args, **kwargs):
        super(VmClusterActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "vm_cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("vm_cluster_id")

    def get_get_fn(self):
        return self.client.get_vm_cluster

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vm_cluster,
            vm_cluster_id=self.module.params.get("vm_cluster_id"),
        )

    def add_virtual_machine(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddVirtualMachineToVmClusterDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_virtual_machine_to_vm_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                add_virtual_machine_to_vm_cluster_details=action_details,
                vm_cluster_id=self.module.params.get("vm_cluster_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeVmClusterCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_vm_cluster_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_vm_cluster_compartment_details=action_details,
                vm_cluster_id=self.module.params.get("vm_cluster_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def remove_virtual_machine(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveVirtualMachineFromVmClusterDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_virtual_machine_from_vm_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                remove_virtual_machine_from_vm_cluster_details=action_details,
                vm_cluster_id=self.module.params.get("vm_cluster_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


VmClusterActionsHelperCustom = get_custom_class("VmClusterActionsHelperCustom")


class ResourceHelper(VmClusterActionsHelperCustom, VmClusterActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            db_servers=dict(
                type="list",
                elements="dict",
                options=dict(db_server_id=dict(type="str", required=True)),
            ),
            vm_cluster_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_virtual_machine",
                    "change_compartment",
                    "remove_virtual_machine",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vm_cluster",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
