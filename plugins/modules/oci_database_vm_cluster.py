#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_database_vm_cluster
short_description: Manage a VmCluster resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a VmCluster resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a VM cluster.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - The user-friendly name for the VM cluster. The name does not need to be unique.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    exadata_infrastructure_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
            - Required for create using I(state=present).
        type: str
    cpu_core_count:
        description:
            - The number of CPU cores to enable for the VM cluster.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    memory_size_in_gbs:
        description:
            - The memory to be allocated in GBs.
            - This parameter is updatable.
        type: int
    db_node_storage_size_in_gbs:
        description:
            - The local node storage to be allocated in GBs.
            - This parameter is updatable.
        type: int
    data_storage_size_in_tbs:
        description:
            - The data disk group size to be allocated in TBs.
            - This parameter is updatable.
        type: float
    ssh_public_keys:
        description:
            - The public key portion of one or more key pairs used for SSH access to the VM cluster.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
    vm_cluster_network_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM cluster network.
            - Required for create using I(state=present).
        type: str
    license_model:
        description:
            - The Oracle license model that applies to the VM cluster. The default is BRING_YOUR_OWN_LICENSE.
            - This parameter is updatable.
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    is_sparse_diskgroup_enabled:
        description:
            - If true, the sparse disk group is configured for the VM cluster. If false, the sparse disk group is not created.
        type: bool
    is_local_backup_enabled:
        description:
            - If true, database backup on local Exadata storage is configured for the VM cluster. If false, database backup on local Exadata storage is not
              available in the VM cluster.
        type: bool
    time_zone:
        description:
            - The time zone to use for the VM cluster. For details, see L(DB System Time
              Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
        type: str
    gi_version:
        description:
            - The Oracle Grid Infrastructure software version for the VM cluster.
            - Required for create using I(state=present).
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - This parameter is updatable.
        type: dict
    vm_cluster_id:
        description:
            - The VM cluster L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the VmCluster.
            - Use I(state=present) to create or update a VmCluster.
            - Use I(state=absent) to delete a VmCluster.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create vm_cluster
  oci_database_vm_cluster:
    display_name: vmCluster
    compartment_id: ocid1.tenancy.oc1.unique_ID
    exadata_infrastructure_id: ocid1.tenancy.oc1.oc1.unique_ID
    vm_cluster_network_id: ocid1.vmclusternetwork.oc1.unique_ID
    cpu_core_count: 4
    memory_size_in_gbs: 30
    db_node_storage_size_in_gbs: 60
    data_storage_size_in_tbs: 84
    ssh_public_keys: ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz...
    license_model: LICENSE_INCLUDED
    is_sparse_diskgroup_enabled: false
    is_local_backup_enabled: true
    time_zone: PST
    gi_version: 19.1.0.0

- name: Update vm_cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_vm_cluster:
    cpu_core_count: 10

- name: Update vm_cluster
  oci_database_vm_cluster:
    vm_cluster_id: ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete vm_cluster
  oci_database_vm_cluster:
    vm_cluster_id: ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete vm_cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_vm_cluster:
    compartment_id: ocid1.tenancy.oc1.unique_ID
    display_name: vmCluster
    state: absent

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
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of the VM cluster.
            returned: on success
            type: string
            sample: PROVISIONING
        display_name:
            description:
                - The user-friendly name for the VM cluster. The name does not need to be unique.
            returned: on success
            type: string
            sample: display_name_example
        time_created:
            description:
                - The date and time that the VM cluster was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        time_zone:
            description:
                - The time zone of the Exadata infrastructure. For details, see L(Exadata Infrastructure Time
                  Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
            returned: on success
            type: string
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
            type: string
            sample: ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx
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
            type: string
            sample: ocid1.vmclusternetwork.oc1..xxxxxxEXAMPLExxxxxx
        cpus_enabled:
            description:
                - The number of enabled CPU cores.
            returned: on success
            type: int
            sample: 56
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
        shape:
            description:
                - The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.
            returned: on success
            type: string
            sample: shape_example
        gi_version:
            description:
                - The Oracle Grid Infrastructure software version for the VM cluster.
            returned: on success
            type: string
            sample: gi_version_example
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
            type: string
            sample: LICENSE_INCLUDED
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
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
        "memory_size_in_gbs": 56,
        "db_node_storage_size_in_gbs": 56,
        "data_storage_size_in_tbs": 1.2,
        "shape": "shape_example",
        "gi_version": "gi_version_example",
        "ssh_public_keys": [ ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz... ],
        "license_model": "LICENSE_INCLUDED",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreateVmClusterDetails
    from oci.database.models import UpdateVmClusterDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VmClusterHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(VmClusterHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["exadata_infrastructure_id", "display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_vm_clusters, **kwargs
        )

    def get_create_model_class(self):
        return CreateVmClusterDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_vm_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(create_vm_cluster_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateVmClusterDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_vm_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vm_cluster_id=self.module.params.get("vm_cluster_id"),
                update_vm_cluster_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_vm_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(vm_cluster_id=self.module.params.get("vm_cluster_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


VmClusterHelperCustom = get_custom_class("VmClusterHelperCustom")


class ResourceHelper(VmClusterHelperCustom, VmClusterHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            exadata_infrastructure_id=dict(type="str"),
            cpu_core_count=dict(type="int"),
            memory_size_in_gbs=dict(type="int"),
            db_node_storage_size_in_gbs=dict(type="int"),
            data_storage_size_in_tbs=dict(type="float"),
            ssh_public_keys=dict(type="list"),
            vm_cluster_network_id=dict(type="str"),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            is_sparse_diskgroup_enabled=dict(type="bool"),
            is_local_backup_enabled=dict(type="bool"),
            time_zone=dict(type="str"),
            gi_version=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            vm_cluster_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
