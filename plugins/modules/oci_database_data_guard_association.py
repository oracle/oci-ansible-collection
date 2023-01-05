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
module: oci_database_data_guard_association
short_description: Manage a DataGuardAssociation resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and update a DataGuardAssociation resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Data Guard association.  A Data Guard association represents the replication relationship between the
      specified database and a peer database. For more information, see L(Using Oracle Data
      Guard,https://docs.cloud.oracle.com/Content/Database/Tasks/usingdataguard.htm).
    - All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID
      called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response.
      You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the
      resource in the Console. For more information, see
      L(Resource Identifiers,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
    - "This resource has the following action operations in the M(oracle.oci.oci_database_data_guard_association_actions) module: failover, reinstate,
      switchover."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - The user-friendly name of the DB system that will contain the the standby database. The display name does not have to be unique.
            - Required for create, update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Applicable when creation_type is 'NewDbSystem'
        type: str
        aliases: ["name"]
    availability_domain:
        description:
            - "The name of the availability domain that the standby database DB system will be located in. For example- \\"Uocm:PHX-AD-1\\"."
            - Applicable when creation_type is 'NewDbSystem'
        type: str
    shape:
        description:
            - The virtual machine DB system shape to launch for the standby database in the Data Guard association. The shape determines the number of CPU cores
              and the amount of memory available for the DB system.
              Only virtual machine shapes are valid options. If you do not supply this parameter, the default shape is the shape of the primary DB system.
            - To get a list of all shapes, use the L(ListDbSystemShapes,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/database/latest/DbSystemShapeSummary/ListDbSystemShapes) operation.
            - Applicable when creation_type is 'NewDbSystem'
        type: str
    cpu_core_count:
        description:
            - The number of OCPU cores available for AMD-based virtual machine DB systems.
            - Applicable when creation_type is 'NewDbSystem'
        type: int
    storage_volume_performance_mode:
        description:
            - The block storage volume performance level. Valid values are `BALANCED` and `HIGH_PERFORMANCE`. See L(Block Volume
              Performance,https://docs.cloud.oracle.com/Content/Block/Concepts/blockvolumeperformance.htm) for more information.
            - Applicable when creation_type is 'NewDbSystem'
        type: str
        choices:
            - "BALANCED"
            - "HIGH_PERFORMANCE"
    node_count:
        description:
            - The number of nodes to launch for the DB system of the standby in the Data Guard association. For a 2-node RAC virtual machine DB system, specify
              either 1 or 2. If you do not supply this parameter, the default is the node count of the primary DB system.
            - Applicable when creation_type is 'NewDbSystem'
        type: int
    subnet_id:
        description:
            - "The OCID of the subnet the DB system is associated with.
              **Subnet Restrictions:**
              - For 1- and 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.16.16/28"
            - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
              Specifying an overlapping subnet will cause the private interconnect to malfunction.
              This restriction applies to both the client subnet and backup subnet.
            - Applicable when creation_type is 'NewDbSystem'
        type: str
    nsg_ids:
        description:
            - "The list of L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) for the network security groups (NSGs) to which this
              resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see L(Security
              Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm).
              **NsgIds restrictions:**
              - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty."
            - Applicable when creation_type is 'NewDbSystem'
        type: list
        elements: str
    backup_network_nsg_ids:
        description:
            - A list of the L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that the
              backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more
              information about NSGs, see L(Security Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm). Applicable only to Exadata
              systems.
            - Applicable when creation_type is 'NewDbSystem'
        type: list
        elements: str
    hostname:
        description:
            - The hostname for the DB node.
            - Applicable when creation_type is 'NewDbSystem'
        type: str
    time_zone:
        description:
            - The time zone of the dataguard standby DB system. For details, see L(DB System Time
              Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
            - Applicable when creation_type is 'NewDbSystem'
        type: str
    fault_domains:
        description:
            - A Fault Domain is a grouping of hardware and infrastructure within an availability domain.
              Fault Domains let you distribute your instances so that they are not on the same physical
              hardware within a single availability domain. A hardware failure or maintenance
              that affects one Fault Domain does not affect DB systems in other Fault Domains.
            - If you do not specify the Fault Domain, the system selects one for you. To change the Fault
              Domain for a DB system, terminate it and launch a new DB system in the preferred Fault Domain.
            - If the node count is greater than 1, you can specify which Fault Domains these nodes will be distributed into.
              The system assigns your nodes automatically to the Fault Domains you specify so that
              no Fault Domain contains more than one node.
            - To get a list of Fault Domains, use the
              L(ListFaultDomains,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/latest/FaultDomain/ListFaultDomains) operation in the
              Identity and Access Management Service API.
            - "Example: `FAULT-DOMAIN-1`"
            - Applicable when creation_type is 'NewDbSystem'
        type: list
        elements: str
    private_ip:
        description:
            - The IPv4 address from the provided OCI subnet which needs to be assigned to the VNIC. If not provided, it will
              be auto-assigned with an available IPv4 address from the subnet.
            - Applicable when creation_type is 'NewDbSystem'
        type: str
    license_model:
        description:
            - The Oracle license model that applies to all the databases on the dataguard standby DB system. The default is LICENSE_INCLUDED.
            - Applicable when creation_type is 'NewDbSystem'
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    db_system_freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - Applicable when creation_type is 'NewDbSystem'
        type: dict
    db_system_defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - Applicable when creation_type is 'NewDbSystem'
        type: dict
    database_freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - Applicable when creation_type is 'NewDbSystem'
        type: dict
    database_defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - Applicable when creation_type is 'NewDbSystem'
        type: dict
    data_collection_options:
        description:
            - ""
            - Applicable when creation_type is 'NewDbSystem'
        type: dict
        suboptions:
            is_diagnostics_events_enabled:
                description:
                    - Indicates whether diagnostic collection is enabled for the VM cluster/Cloud VM cluster/VMBM DBCS. Enabling diagnostic collection allows
                      you to receive Events service notifications for guest VM issues. Diagnostic collection also allows Oracle to provide enhanced service and
                      proactive support for your Exadata system. You can enable diagnostic collection during VM cluster/Cloud VM cluster provisioning. You can
                      also disable or enable it at any time using the `UpdateVmCluster` or `updateCloudVmCluster` API.
                    - Applicable when creation_type is 'NewDbSystem'
                type: bool
            is_health_monitoring_enabled:
                description:
                    - Indicates whether health monitoring is enabled for the VM cluster / Cloud VM cluster / VMBM DBCS. Enabling health monitoring allows Oracle
                      to collect diagnostic data and share it with its operations and support personnel. You may also receive notifications for some events.
                      Collecting health diagnostics enables Oracle to provide proactive support and enhanced service for your system.
                      Optionally enable health monitoring while provisioning a system. You can also disable or enable health monitoring anytime using the
                      `UpdateVmCluster`, `UpdateCloudVmCluster` or `updateDbsystem` API.
                    - Applicable when creation_type is 'NewDbSystem'
                type: bool
            is_incident_logs_enabled:
                description:
                    - Indicates whether incident logs and trace collection are enabled for the VM cluster / Cloud VM cluster / VMBM DBCS. Enabling incident logs
                      collection allows Oracle to receive Events service notifications for guest VM issues, collect incident logs and traces, and use them to
                      diagnose issues and resolve them.
                      Optionally enable incident logs collection while provisioning a system. You can also disable or enable incident logs collection anytime
                      using the `UpdateVmCluster`, `updateCloudVmCluster` or `updateDbsystem` API.
                    - Applicable when creation_type is 'NewDbSystem'
                type: bool
    peer_vm_cluster_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM Cluster in which to create the standby database.
              You must supply this value if creationType is `ExistingVmCluster`.
            - Applicable when creation_type is 'ExistingVmCluster'
        type: str
    database_software_image_id:
        description:
            - The database software image L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
        type: str
    creation_type:
        description:
            - Specifies whether to create the peer database in an existing DB system or in a new DB system.
            - Required for create using I(state=present).
        type: str
        choices:
            - "NewDbSystem"
            - "ExistingVmCluster"
            - "ExistingDbSystem"
    peer_db_unique_name:
        description:
            - Specifies the `DB_UNIQUE_NAME` of the peer database to be created.
        type: str
    peer_sid_prefix:
        description:
            - Specifies a prefix for the `Oracle SID` of the database to be created.
        type: str
    peer_db_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system in which to create the standby database.
              You must supply this value if creationType is `ExistingDbSystem`.
            - Applicable when creation_type is 'ExistingDbSystem'
        type: str
    peer_db_home_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB home in which to create the standby database.
              You must supply this value to create standby database with an existing DB home
            - Applicable when creation_type is one of ['ExistingDbSystem', 'ExistingVmCluster']
        type: str
    database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    data_guard_association_id:
        description:
            - The Data Guard association's L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    database_admin_password:
        description:
            - A strong password for the `SYS`, `SYSTEM`, and `PDB Admin` users to apply during standby creation.
            - "The password must contain no fewer than nine characters and include:"
            - "* At least two uppercase characters."
            - "* At least two lowercase characters."
            - "* At least two numeric characters."
            - "* At least two special characters. Valid special characters include \\"_\\", \\"#\\", and \\"-\\" only."
            - "**The password MUST be the same as the primary admin password.**"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    protection_mode:
        description:
            - The protection mode to set up between the primary and standby databases. For more information, see
              L(Oracle Data Guard Protection Modes,http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)
              in the Oracle Data Guard documentation.
            - "**IMPORTANT** - The only protection mode currently supported by the Database service is MAXIMUM_PERFORMANCE."
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "MAXIMUM_AVAILABILITY"
            - "MAXIMUM_PERFORMANCE"
            - "MAXIMUM_PROTECTION"
    transport_type:
        description:
            - "The redo transport type to use for this Data Guard association.  Valid values depend on the specified `protectionMode`:"
            - "* MAXIMUM_AVAILABILITY - SYNC or FASTSYNC
              * MAXIMUM_PERFORMANCE - ASYNC
              * MAXIMUM_PROTECTION - SYNC"
            - For more information, see
              L(Redo Transport Services,http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400)
              in the Oracle Data Guard documentation.
            - "**IMPORTANT** - The only transport type currently supported by the Database service is ASYNC."
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "SYNC"
            - "ASYNC"
            - "FASTSYNC"
    is_active_data_guard_enabled:
        description:
            - True if active Data Guard is enabled.
            - This parameter is updatable.
        type: bool
    state:
        description:
            - The state of the DataGuardAssociation.
            - Use I(state=present) to create or update a DataGuardAssociation.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create data_guard_association with creation_type = NewDbSystem
  oci_database_data_guard_association:
    # required
    creation_type: NewDbSystem
    database_admin_password: example-password
    protection_mode: MAXIMUM_AVAILABILITY
    transport_type: SYNC

    # optional
    display_name: display_name_example
    availability_domain: Uocm:PHX-AD-1
    shape: shape_example
    cpu_core_count: 56
    storage_volume_performance_mode: BALANCED
    node_count: 56
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    backup_network_nsg_ids: [ "backup_network_nsg_ids_example" ]
    hostname: hostname_example
    time_zone: time_zone_example
    fault_domains: [ "fault_domains_example" ]
    private_ip: private_ip_example
    license_model: LICENSE_INCLUDED
    db_system_freeform_tags: null
    db_system_defined_tags: null
    database_freeform_tags: null
    database_defined_tags: null
    data_collection_options:
      # optional
      is_diagnostics_events_enabled: true
      is_health_monitoring_enabled: true
      is_incident_logs_enabled: true
    database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
    peer_db_unique_name: peer_db_unique_name_example
    peer_sid_prefix: peer_sid_prefix_example
    is_active_data_guard_enabled: true

- name: Create data_guard_association with creation_type = ExistingVmCluster
  oci_database_data_guard_association:
    # required
    creation_type: ExistingVmCluster
    database_admin_password: example-password
    protection_mode: MAXIMUM_AVAILABILITY
    transport_type: SYNC

    # optional
    peer_vm_cluster_id: "ocid1.peervmcluster.oc1..xxxxxxEXAMPLExxxxxx"
    database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
    peer_db_unique_name: peer_db_unique_name_example
    peer_sid_prefix: peer_sid_prefix_example
    peer_db_home_id: "ocid1.peerdbhome.oc1..xxxxxxEXAMPLExxxxxx"
    is_active_data_guard_enabled: true

- name: Create data_guard_association with creation_type = ExistingDbSystem
  oci_database_data_guard_association:
    # required
    creation_type: ExistingDbSystem
    database_admin_password: example-password
    protection_mode: MAXIMUM_AVAILABILITY
    transport_type: SYNC

    # optional
    database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
    peer_db_unique_name: peer_db_unique_name_example
    peer_sid_prefix: peer_sid_prefix_example
    peer_db_system_id: "ocid1.peerdbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    peer_db_home_id: "ocid1.peerdbhome.oc1..xxxxxxEXAMPLExxxxxx"
    is_active_data_guard_enabled: true

- name: Update data_guard_association
  oci_database_data_guard_association:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    data_guard_association_id: "ocid1.dataguardassociation.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    database_admin_password: example-password
    protection_mode: MAXIMUM_AVAILABILITY
    transport_type: SYNC
    is_active_data_guard_enabled: true

- name: Update data_guard_association using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_data_guard_association:
    # required
    display_name: display_name_example
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    database_admin_password: example-password
    protection_mode: MAXIMUM_AVAILABILITY
    transport_type: SYNC
    is_active_data_guard_enabled: true

"""

RETURN = """
data_guard_association:
    description:
        - Details of the DataGuardAssociation resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Data Guard association.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the reporting database.
            returned: on success
            type: str
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        role:
            description:
                - The role of the reporting database in this Data Guard association.
            returned: on success
            type: str
            sample: PRIMARY
        lifecycle_state:
            description:
                - The current state of the Data Guard association.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState, if available.
            returned: on success
            type: str
            sample: lifecycle_details_example
        peer_db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system containing the associated
                  peer database.
            returned: on success
            type: str
            sample: "ocid1.peerdbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        peer_db_home_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Home containing the associated peer
                  database.
            returned: on success
            type: str
            sample: "ocid1.peerdbhome.oc1..xxxxxxEXAMPLExxxxxx"
        peer_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the associated peer database.
            returned: on success
            type: str
            sample: "ocid1.peerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
        peer_data_guard_association_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the peer database's Data Guard association.
            returned: on success
            type: str
            sample: "ocid1.peerdataguardassociation.oc1..xxxxxxEXAMPLExxxxxx"
        peer_role:
            description:
                - The role of the peer database in this Data Guard association.
            returned: on success
            type: str
            sample: PRIMARY
        apply_lag:
            description:
                - The lag time between updates to the primary database and application of the redo data on the standby database,
                  as computed by the reporting database.
                - "Example: `9 seconds`"
            returned: on success
            type: str
            sample: apply_lag_example
        apply_rate:
            description:
                - The rate at which redo logs are synced between the associated databases.
                - "Example: `180 Mb per second`"
            returned: on success
            type: str
            sample: apply_rate_example
        protection_mode:
            description:
                - The protection mode of this Data Guard association. For more information, see
                  L(Oracle Data Guard Protection Modes,http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)
                  in the Oracle Data Guard documentation.
            returned: on success
            type: str
            sample: MAXIMUM_AVAILABILITY
        transport_type:
            description:
                - The redo transport type used by this Data Guard association.  For more information, see
                  L(Redo Transport Services,http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400)
                  in the Oracle Data Guard documentation.
            returned: on success
            type: str
            sample: SYNC
        time_created:
            description:
                - The date and time the Data Guard association was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_active_data_guard_enabled:
            description:
                - True if active Data Guard is enabled.
            returned: on success
            type: bool
            sample: true
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "role": "PRIMARY",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "peer_db_system_id": "ocid1.peerdbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_db_home_id": "ocid1.peerdbhome.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_database_id": "ocid1.peerdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_data_guard_association_id": "ocid1.peerdataguardassociation.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_role": "PRIMARY",
        "apply_lag": "apply_lag_example",
        "apply_rate": "apply_rate_example",
        "protection_mode": "MAXIMUM_AVAILABILITY",
        "transport_type": "SYNC",
        "time_created": "2013-10-20T19:20:30+01:00",
        "is_active_data_guard_enabled": true
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
    from oci.database.models import CreateDataGuardAssociationDetails
    from oci.database.models import UpdateDataGuardAssociationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataGuardAssociationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def __init__(self, *args, **kwargs):
        super(DataGuardAssociationHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_possible_entity_types(self):
        return super(
            DataGuardAssociationHelperGen, self
        ).get_possible_entity_types() + [
            "dataguardassociation",
            "dataguardassociations",
            "databasedataguardassociation",
            "databasedataguardassociations",
            "dataguardassociationresource",
            "dataguardassociationsresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "data_guard_association_id"

    def get_module_resource_id(self):
        return self.module.params.get("data_guard_association_id")

    def get_get_fn(self):
        return self.client.get_data_guard_association

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_guard_association,
            data_guard_association_id=summary_model.id,
            database_id=self.module.params.get("database_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_guard_association,
            database_id=self.module.params.get("database_id"),
            data_guard_association_id=self.module.params.get(
                "data_guard_association_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "database_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_data_guard_associations, **kwargs
        )

    def get_create_model_class(self):
        return CreateDataGuardAssociationDetails

    def get_exclude_attributes(self):
        return [
            "database_software_image_id",
            "peer_vm_cluster_id",
            "fault_domains",
            "private_ip",
            "hostname",
            "data_collection_options",
            "database_admin_password",
            "peer_sid_prefix",
            "database_freeform_tags",
            "storage_volume_performance_mode",
            "node_count",
            "db_system_freeform_tags",
            "db_system_defined_tags",
            "shape",
            "availability_domain",
            "license_model",
            "display_name",
            "time_zone",
            "peer_db_unique_name",
            "creation_type",
            "nsg_ids",
            "subnet_id",
            "backup_network_nsg_ids",
            "database_defined_tags",
            "cpu_core_count",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_data_guard_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_id=self.module.params.get("database_id"),
                create_data_guard_association_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDataGuardAssociationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_data_guard_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_id=self.module.params.get("database_id"),
                data_guard_association_id=self.module.params.get(
                    "data_guard_association_id"
                ),
                update_data_guard_association_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataGuardAssociationHelperCustom = get_custom_class("DataGuardAssociationHelperCustom")


class ResourceHelper(DataGuardAssociationHelperCustom, DataGuardAssociationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            availability_domain=dict(type="str"),
            shape=dict(type="str"),
            cpu_core_count=dict(type="int"),
            storage_volume_performance_mode=dict(
                type="str", choices=["BALANCED", "HIGH_PERFORMANCE"]
            ),
            node_count=dict(type="int"),
            subnet_id=dict(type="str"),
            nsg_ids=dict(type="list", elements="str"),
            backup_network_nsg_ids=dict(type="list", elements="str"),
            hostname=dict(type="str"),
            time_zone=dict(type="str"),
            fault_domains=dict(type="list", elements="str"),
            private_ip=dict(type="str"),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            db_system_freeform_tags=dict(type="dict"),
            db_system_defined_tags=dict(type="dict"),
            database_freeform_tags=dict(type="dict"),
            database_defined_tags=dict(type="dict"),
            data_collection_options=dict(
                type="dict",
                options=dict(
                    is_diagnostics_events_enabled=dict(type="bool"),
                    is_health_monitoring_enabled=dict(type="bool"),
                    is_incident_logs_enabled=dict(type="bool"),
                ),
            ),
            peer_vm_cluster_id=dict(type="str"),
            database_software_image_id=dict(type="str"),
            creation_type=dict(
                type="str",
                choices=["NewDbSystem", "ExistingVmCluster", "ExistingDbSystem"],
            ),
            peer_db_unique_name=dict(type="str"),
            peer_sid_prefix=dict(type="str"),
            peer_db_system_id=dict(type="str"),
            peer_db_home_id=dict(type="str"),
            database_id=dict(type="str", required=True),
            data_guard_association_id=dict(aliases=["id"], type="str"),
            database_admin_password=dict(type="str", no_log=True),
            protection_mode=dict(
                type="str",
                choices=[
                    "MAXIMUM_AVAILABILITY",
                    "MAXIMUM_PERFORMANCE",
                    "MAXIMUM_PROTECTION",
                ],
            ),
            transport_type=dict(type="str", choices=["SYNC", "ASYNC", "FASTSYNC"]),
            is_active_data_guard_enabled=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="data_guard_association",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = dict(changed=False)

    if resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
