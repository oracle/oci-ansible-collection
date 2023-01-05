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
module: oci_database_vm_cluster
short_description: Manage a VmCluster resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a VmCluster resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an Exadata Cloud@Customer VM cluster.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_vm_cluster_actions) module: add_virtual_machine, change_compartment,
      remove_virtual_machine."
version_added: "2.9.0"
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
    vm_cluster_network_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM cluster network.
            - Required for create using I(state=present).
        type: str
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
    db_servers:
        description:
            - The list of Db server.
        type: list
        elements: str
    cpu_core_count:
        description:
            - The number of CPU cores to enable for the VM cluster.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    ocpu_count:
        description:
            - The number of OCPU cores to enable for the VM cluster. Only one decimal place is allowed for the fractional part.
            - This parameter is updatable.
        type: float
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
    data_storage_size_in_gbs:
        description:
            - The data disk group size to be allocated in GBs.
            - This parameter is updatable.
        type: float
    license_model:
        description:
            - The Oracle license model that applies to the VM cluster. The default is BRING_YOUR_OWN_LICENSE.
            - This parameter is updatable.
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    ssh_public_keys:
        description:
            - The public key portion of one or more key pairs used for SSH access to the VM cluster.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: str
    version:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            patch_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the patch.
                    - This parameter is updatable.
                type: str
            database_software_image_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database software image.
                    - This parameter is updatable.
                type: str
            action:
                description:
                    - The action to perform on the patch.
                    - This parameter is updatable.
                type: str
                choices:
                    - "APPLY"
                    - "PRECHECK"
    update_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            update_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the maintenance update.
                    - This parameter is updatable.
                type: str
            update_action:
                description:
                    - The update action to perform.
                    - This parameter is updatable.
                type: str
                choices:
                    - "ROLLING_APPLY"
                    - "PRECHECK"
                    - "ROLLBACK"
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
    data_collection_options:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            is_diagnostics_events_enabled:
                description:
                    - Indicates whether diagnostic collection is enabled for the VM cluster/Cloud VM cluster/VMBM DBCS. Enabling diagnostic collection allows
                      you to receive Events service notifications for guest VM issues. Diagnostic collection also allows Oracle to provide enhanced service and
                      proactive support for your Exadata system. You can enable diagnostic collection during VM cluster/Cloud VM cluster provisioning. You can
                      also disable or enable it at any time using the `UpdateVmCluster` or `updateCloudVmCluster` API.
                type: bool
            is_health_monitoring_enabled:
                description:
                    - Indicates whether health monitoring is enabled for the VM cluster / Cloud VM cluster / VMBM DBCS. Enabling health monitoring allows Oracle
                      to collect diagnostic data and share it with its operations and support personnel. You may also receive notifications for some events.
                      Collecting health diagnostics enables Oracle to provide proactive support and enhanced service for your system.
                      Optionally enable health monitoring while provisioning a system. You can also disable or enable health monitoring anytime using the
                      `UpdateVmCluster`, `UpdateCloudVmCluster` or `updateDbsystem` API.
                type: bool
            is_incident_logs_enabled:
                description:
                    - Indicates whether incident logs and trace collection are enabled for the VM cluster / Cloud VM cluster / VMBM DBCS. Enabling incident logs
                      collection allows Oracle to receive Events service notifications for guest VM issues, collect incident logs and traces, and use them to
                      diagnose issues and resolve them.
                      Optionally enable incident logs collection while provisioning a system. You can also disable or enable incident logs collection anytime
                      using the `UpdateVmCluster`, `updateCloudVmCluster` or `updateDbsystem` API.
                type: bool
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
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    vm_cluster_network_id: "ocid1.vmclusternetwork.oc1..xxxxxxEXAMPLExxxxxx"
    gi_version: gi_version_example
    cpu_core_count: 56
    ssh_public_keys: [ "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..." ]

    # optional
    is_sparse_diskgroup_enabled: true
    is_local_backup_enabled: true
    time_zone: time_zone_example
    db_servers: [ "db_servers_example" ]
    ocpu_count: 3.4
    memory_size_in_gbs: 56
    db_node_storage_size_in_gbs: 56
    data_storage_size_in_tbs: 3.4
    data_storage_size_in_gbs: 3.4
    license_model: LICENSE_INCLUDED
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    data_collection_options:
      # optional
      is_diagnostics_events_enabled: true
      is_health_monitoring_enabled: true
      is_incident_logs_enabled: true

- name: Update vm_cluster
  oci_database_vm_cluster:
    # required
    vm_cluster_id: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    cpu_core_count: 56
    ocpu_count: 3.4
    memory_size_in_gbs: 56
    db_node_storage_size_in_gbs: 56
    data_storage_size_in_tbs: 3.4
    data_storage_size_in_gbs: 3.4
    license_model: LICENSE_INCLUDED
    ssh_public_keys: [ "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..." ]
    version:
      # optional
      patch_id: "ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx"
      database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
      action: APPLY
    update_details:
      # optional
      update_id: "ocid1.update.oc1..xxxxxxEXAMPLExxxxxx"
      update_action: ROLLING_APPLY
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    data_collection_options:
      # optional
      is_diagnostics_events_enabled: true
      is_health_monitoring_enabled: true
      is_incident_logs_enabled: true

- name: Update vm_cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_vm_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    cpu_core_count: 56
    ocpu_count: 3.4
    memory_size_in_gbs: 56
    db_node_storage_size_in_gbs: 56
    data_storage_size_in_tbs: 3.4
    data_storage_size_in_gbs: 3.4
    license_model: LICENSE_INCLUDED
    ssh_public_keys: [ "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..." ]
    version:
      # optional
      patch_id: "ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx"
      database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
      action: APPLY
    update_details:
      # optional
      update_id: "ocid1.update.oc1..xxxxxxEXAMPLExxxxxx"
      update_action: ROLLING_APPLY
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    data_collection_options:
      # optional
      is_diagnostics_events_enabled: true
      is_health_monitoring_enabled: true
      is_incident_logs_enabled: true

- name: Delete vm_cluster
  oci_database_vm_cluster:
    # required
    vm_cluster_id: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete vm_cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_vm_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
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
                is_health_monitoring_enabled:
                    description:
                        - Indicates whether health monitoring is enabled for the VM cluster / Cloud VM cluster / VMBM DBCS. Enabling health monitoring allows
                          Oracle to collect diagnostic data and share it with its operations and support personnel. You may also receive notifications for some
                          events. Collecting health diagnostics enables Oracle to provide proactive support and enhanced service for your system.
                          Optionally enable health monitoring while provisioning a system. You can also disable or enable health monitoring anytime using the
                          `UpdateVmCluster`, `UpdateCloudVmCluster` or `updateDbsystem` API.
                    returned: on success
                    type: bool
                    sample: true
                is_incident_logs_enabled:
                    description:
                        - Indicates whether incident logs and trace collection are enabled for the VM cluster / Cloud VM cluster / VMBM DBCS. Enabling incident
                          logs collection allows Oracle to receive Events service notifications for guest VM issues, collect incident logs and traces, and use
                          them to diagnose issues and resolve them.
                          Optionally enable incident logs collection while provisioning a system. You can also disable or enable incident logs collection
                          anytime using the `UpdateVmCluster`, `updateCloudVmCluster` or `updateDbsystem` API.
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
            "is_diagnostics_events_enabled": true,
            "is_health_monitoring_enabled": true,
            "is_incident_logs_enabled": true
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
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

    def get_possible_entity_types(self):
        return super(VmClusterHelperGen, self).get_possible_entity_types() + [
            "vmcluster",
            "vmclusters",
            "databasevmcluster",
            "databasevmclusters",
            "vmclusterresource",
            "vmclustersresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "vm_cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("vm_cluster_id")

    def get_get_fn(self):
        return self.client.get_vm_cluster

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_vm_cluster, vm_cluster_id=summary_model.id,
        ).data

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

    def get_exclude_attributes(self):
        return ["ocpu_count", "cpu_core_count"]

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
            vm_cluster_network_id=dict(type="str"),
            is_sparse_diskgroup_enabled=dict(type="bool"),
            is_local_backup_enabled=dict(type="bool"),
            time_zone=dict(type="str"),
            gi_version=dict(type="str"),
            db_servers=dict(type="list", elements="str"),
            cpu_core_count=dict(type="int"),
            ocpu_count=dict(type="float"),
            memory_size_in_gbs=dict(type="int"),
            db_node_storage_size_in_gbs=dict(type="int"),
            data_storage_size_in_tbs=dict(type="float"),
            data_storage_size_in_gbs=dict(type="float"),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            ssh_public_keys=dict(type="list", elements="str", no_log=True),
            version=dict(
                type="dict",
                options=dict(
                    patch_id=dict(type="str"),
                    database_software_image_id=dict(type="str"),
                    action=dict(type="str", choices=["APPLY", "PRECHECK"]),
                ),
            ),
            update_details=dict(
                type="dict",
                options=dict(
                    update_id=dict(type="str"),
                    update_action=dict(
                        type="str", choices=["ROLLING_APPLY", "PRECHECK", "ROLLBACK"]
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            data_collection_options=dict(
                type="dict",
                options=dict(
                    is_diagnostics_events_enabled=dict(type="bool"),
                    is_health_monitoring_enabled=dict(type="bool"),
                    is_incident_logs_enabled=dict(type="bool"),
                ),
            ),
            vm_cluster_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

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
