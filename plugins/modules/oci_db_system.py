#!/usr/bin/python
# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_db_system
short_description: Launch,update and terminate a DB System in OCI Database Cloud Service.
description:
    - Launch an OCI DB System
    - Update an OCI DB System, if present, with a new display name
    - Terminate an OCI DB System, if present.
    - Since all operations of this module takes a long time, it is recommended to set the C(wait) to False. Use
      M(oci_db_system_facts) to check the status of the operation as a separate task.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which this
                     DB System would be created. Mandatory for create
                     operation.
        required: false
    db_system_id:
        description: Identifier of the existing DB System which required to be
                     updated or terminated. Mandatory for terminate and update.
        required: false
        aliases: ['id']
    availability_domain:
        description: The Availability Domain where the DB System is located.
        required: false
    backup_subnet_id:
        description: The OCID of the backup network subnet the DB System is
                     associated with. Applicable only to Exadata.
        required: false
    cluster_name:
        description: Cluster name for Exadata and 2-node RAC DB Systems. The cluster
                     name must begin with an an alphabetic character, and may contain
                     hyphens (-). Underscores are not permitted. The cluster name
                     can be no longer than 11 characters and is not case sensitive.
        required: false
    cpu_core_count:
        description: The number of CPU cores to enable. For VM DB systems, the core count
                     is inferred from the specific VM shape chosen, so this parameter is
                     not used. Do not provide this attribute if the I(shape) of the DB System
                     is a Virtual Machine shape.
        required: false
    data_storage_percentage:
        description: The percentage assigned to DATA storage (user data and database files).
                     The remaining percentage is assigned to RECO storage (database redo logs,
                     archive logs, and recovery manager backups). Specify 80 or 40. The default
                     is 80 percent assigned to DATA storage. This is not applicable for VM based
                     DB systems.
        required: false
    database_edition:
        description: The Oracle Database Edition that applies to all the databases on the DB System.
                     Exadata DB Systems and 2-node RAC DB Systems require
                     ENTERPRISE_EDITION_EXTREME_PERFORMANCE.
        required: false
        choices: ['STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE',
                  'ENTERPRISE_EDITION_HIGH_PERFORMANCE']
    db_home:
        description: Details of the DB home to use for this database. DB home is a directory where Oracle
                     database software is installed.
        suboptions:
            database:
               description: The details of the database to be created under the db home.
                            Consists of the following options, ['admin_password' describes
                            A strong password for SYS, SYSTEM, and PDB Admin. The password
                            must be at least nine characters and contain at least two uppercase,
                            two lowercase, two numbers, and two special characters. This parameter
                            valid for I(source=NONE) and I(source=DB_BACKUP). required - true],
                            ['character_set' describes the character set for the database. The default
                            is AL32UTF8. This parameter only valid for I(source=NONE). required - false],
                            ['freeform_tags' describes Free-form tags for this database. Each tag is a simple
                            key-value pair with no predefined name, type, or namespace. This parameter only
                            valid for I(source=NONE).required - false], ['defined_tags' describes Defined tags
                            for this database. Each key is predefined and scoped to a namespace. This parameter
                            only valid for I(source=NONE). required - false], ['db_backup_config' consists of the
                            option 'auto_backup_enabled' to determine whether to configures automatic backups of
                            the database. This parameter only valid for I(source=NONE). required - false], ['db_name'
                            describes the name of the database name. It must begin with an alphabetic character and can
                            contain a maximum of eight alphanumeric characters. Special characters
                            are not permitted. This parameter only valid for I(source=NONE). required - true],
                            ['db_workload' describes database workload type with allowed values OLTP and DSS.
                            This parameter only valid for I(source=NONE). required - false],['ncharacter_set' describes
                            National character set for the database.The default is AL16UTF16. Allowed values are AL16UTF16
                            or UTF8. This parameter only valid for I(source=NONE). required - false], ['pdb_name' describes
                            pluggable database name. It must begin with an alphabetic character and can contain a maximum of
                            eight alphanumeric characters. Special characters are notpermitted. Pluggable database should not
                            be same as database name. This parameter only valid for I(source=NONE). required - false],
                            ['backup_id' describes the backup OCID. This parameter only valid for I(source=DB_BACKUP). required - true],
                            ['backup_tde_password' describes the password to open the TDE wallet. This parameter only
                            valid for I(source=DB_BACKUP). required - true]
               required: true
            db_version:
               description: A valid Oracle database version. This parameter only valid for I(source=NONE).
               required: true
            display_name:
               description: The user-provided name of the database home.
               required: false
        required: true
    disk_redundancy:
        description: The type of redundancy configured for the DB System. Normal is 2-way redundancy,
                     recommended for test and development systems. High is 3-way redundancy, recommended
                     for production systems.
        required: false
        choices: ['HIGH', 'NORMAL']
    display_name:
        description: The user-friendly name for the DB System. It does not have to be unique.
        required: false
    domain:
        description: A domain name used for the DB System. If the Oracle-provided Internet and
                     VCN Resolver is enabled for the specified subnet, the domain name for the
                     subnet is used. Hyphens (-) are not permitted.
        required: false
    hostname:
        description: The host name for the DB System. The host name must begin with an alphabetic
                     character and can contain a maximum of 30 alphanumeric characters, including
                     hyphens (-).The maximum length of the combined hostname and domain is 63
                     characters. The hostname must be unique within the subnet. If it is not unique,
                     the DB System will fail to provision.
        required: false
    initial_data_storage_size_in_gb:
        description: Size, in GBs, of the initial data volume that will be created and attached to
                     VM-shape based DB system. This storage can later be scaled up if needed. Note that
                     the total storage size attached will be more than what is requested, to account for
                     REDO/RECO space and software volume.
        required: false
    data_storage_size_in_gbs:
        description: Size, in GBs, to which the currently attached storage needs to be scaled up to for VM
                     based DB system. This must be greater than current storage size. Note that the total
                     storage size attached will be more than what is requested, to account for REDO/RECO space
                     and software volume. This option required only for update operation.
        required: false
    license_model:
        description: The Oracle license model that applies to all the databases on the DB System. The default is
                     LICENSE_INCLUDED.
        required: false
        choices: ['LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE']
    node_count:
        description: Number of nodes to launch for a VM-shape based RAC DB system.
        required: false
    shape:
        description: The shape of the DB System. The shape determines resources allocated to the DB System - CPU cores
                     and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes.
        required: false
    ssh_public_keys:
        description: The public key portion of the key pair to use for SSH access to the DB System. Multiple public keys
                     can be provided. The length of the combined keys cannot exceed 10,000 characters.
        required: true
    source:
        description: The source of the database, NONE for creating a new database. DB_BACKUP for creating a new database
                     by restoring from a backup. The default is NONE.
        required: false
        default: "NONE"
        choices: ['DB_BACKUP', 'NONE']
    subnet_id:
        description: The OCID of the subnet the DB System is associated with.
        required: false
    purge_ssh_public_keys:
        description: Purge ssh public keys  from DB System which are not present in the provided ssh public keys.
                     If I(purge_ssh_public_keys=no), provided ssh public keys would be appended to existing ssh
                     public keys. I(purge_ssh_public_keys) and I(delete_ssh_public_keys) are mutually exclusive.
        required: false
        default: True
        choices: [True, False]
    delete_ssh_public_keys:
        description: Delete ssh public keys from DB System which are present in the provided ssh public keys.
                     If I(delete_ssh_public_keys=yes), ssh public keys provided by I(ssh_public_keys) would
                     be deleted from existing ssh public keys, if they are part of existing ssh public keys.
                     If they are not part of existing ssh public keys, they will be ignored. I(delete_ssh_public_keys)
                     and I(purge_ssh_public_keys) are mutually exclusive.
        required: false
        default: False
        choices: [True, False]
    version:
        description: This attribute describes the patch version and what actions to perform with that on specified DB
                     system. This is required only for update use case.
        suboptions:
            action:
               description: The action to perform on the patch.
               required: true
               choices: ['APPLY', 'PRECHECK']
            patch_id:
               description: The OCID of the patch.
               required: true
        required: false
    state:
        description: Launch,update or terminate DB System. For I(state=present), if it
                     does not exist, it gets created. If it exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Launch DB System
- name: Create DB System
  oci_db_system:
    compartment_id: "ocid1.compartment.aaaa"
    availability_domain: "AD-2"
    cluster_name: "db-cluster"
    cpu_core_count: 2
    data_storage_percentage: 80
    database_edition: "STANDARD_EDITION"
    db_home:
      database:
        admin_password: 'BEstr0ng_#1'
        character_set: 'AL32UTF8'
        db_backup_config:
         auto_backup_enabled: False
        db_name: 'db15'
        db_workload: 'OLTP'
        ncharacter_set: 'AL16UTF16'
        pdb_name: 'db15'
        freeform_tags:
            deployment: 'production'
        defined_tags:
            target_users:
                division: 'design'
      db_version: '12.2.0.1'
      display_name: ansible-db
    disk_redundancy: "NORMAL"
    display_name: "ansibledb"
    hostname: "ansibledbsystem"
    initial_data_storage_size_in_gb: 4096
    license_model: "LICENSE_INCLUDED"
    node_count: 1
    shape: "BM.DenseIO1.36"
    ssh_public_keys: ["/tmp/id_rsa.pub"]
    subnet_id: "ocid1.subnet.aaaa"
    freeform_tags:
        deployment: 'production'
    defined_tags:
        target_users:
            division: 'documentation'
    wait: False
    state: 'present'

# Create a new DB System Using a Database Backup
- name: Create a new DB System Using a Database Backup
  oci_db_system:
    compartment_id: "ocid1.compartment.aaaa"
    availability_domain: "AD-2"
    cluster_name: "db-cluster"
    cpu_core_count: 2
    data_storage_percentage: 80
    database_edition: "STANDARD_EDITION"
    source: "DB_BACKUP"
    db_home:
      database:
        admin_password: 'BEstr0ng_#1'
        backup_id: 'ocid1.dbbackup.oc1.xxxxxEXAMPLExxxxx'
        backup_tde_password: 'BEstr0ng_#1'
      display_name: new-ansibledbhome-sourced-from-backup
    disk_redundancy: "NORMAL"
    display_name: "new-ansibledb-sourced-from-backup"
    hostname: "ansibledbsystem"
    initial_data_storage_size_in_gb: 4096
    license_model: "LICENSE_INCLUDED"
    node_count: 1
    shape: "BM.DenseIO1.36"
    ssh_public_keys: ["/tmp/id_rsa.pub"]
    subnet_id: "ocid1.subnet.xxxxxEXAMPLExxxxx"
    freeform_tags:
        deployment: 'production'
    defined_tags:
        target_users:
            division: 'documentation'
    wait: False
    state: 'present'

# Perform a patch PRECHECK on the specified database system
- name: PRECHECK a patch on the DB System
  oci_db_system:
    db_system_id: "ocid1.dbsystem.aaaa"
    version:
      patch_id: "ocid1.patch.aaaa"
      action: 'PRECHECK'
    state: 'present'

# APPLY a patch on the specified database system
- name: APPLY a patch on the DB System
  oci_db_system:
    db_system_id: "ocid1.dbsystem.aaaa"
    version:
      patch_id: "ocid1.patch.aaaa"
      action: 'APPLY'
    state: 'present'

# Update a DB System's CPU core count
- name: Update DB System CPU core count
  oci_db_system:
    db_system_id: "ocid1.dbsystem.aaaa"
    cpu_core_count: 4
    state: 'present'

# Update DB System by purging SSH Public keys
- name: Update DB System by purging SSH Public keys
  oci_db_system:
    db_system_id: "ocid1.dbsystem.aaaa"
    ssh_public_keys: ["/tmp/id_rsa_updated.pub"]
    purge_ssh_public_keys: True
    state: 'present'

# Appending SSH public keys to a database system
- name: Update DB System by appending SSH Public keys
  oci_db_system:
    db_system_id: "ocid1.dbsystem.aaaa"
    ssh_public_keys: ["/tmp/id_rsa_updated.pub"]
    purge_ssh_public_keys: False
    state: 'present'

# Deleting SSH public keys from a database system
- name: Update DB System by deleting SSH Public keys
  oci_db_system:
    db_system_id: "ocid1.dbsystem.aaaa"
    ssh_public_keys: ["/tmp/id_rsa_updated.pub"]
    delete_ssh_public_keys: True
    state: 'present'

# Terminate DB System
- name: Terminate DB System
  oci_db_system:
    db_system_id: "ocid1.dbsystem.aaaa"
    state: 'absent'
"""


RETURN = """
    db_system:
        description: Attributes of the launched/updated DB System.
                    For delete, deleted DB System description will
                    be returned.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the DB System
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            availability_domain:
                description: The Availability Domain where the DB System is located.
                returned: always
                type: string
                sample: IwGV:US-ASHBURN-AD-2
            cluster_name:
                description: Cluster name for Exadata and 2-node RAC DB Systems
                returned: always
                type: string
                sample: db-cluster
            cpu_core_count:
                description: The number of CPU cores to enable.
                returned: always
                type: string
                sample: 2
            time_created:
                description: Date and time when the DB System was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            data_storage_percentage:
                description: The percentage assigned to DATA storage
                returned: always
                type: string
                sample: 80
            data_storage_size_in_gbs:
                description: Data storage size, in GBs, that is currently available to the DB system.
                             This is applicable only for VM-based DBs.
                returned: always
                type: string
                sample: 2048
            id:
                description: The identifier of the DB System
                returned: always
                type: string
                sample: ocid1.dbsystem.oc1.xzvf..oifds
            database_edition:
                description: The Oracle Database Edition that applies to all the databases on the DB System.
                returned: always
                type: string
                sample: STANDARD_EDITION
            disk_redundancy:
                description: The type of redundancy configured for the DB System.
                returned: always
                type: string
                sample: NORMAL
            display_name:
                description: The user-friendly name for the DB System.
                returned: always
                type: string
                sample: ansible-db-system
            domain:
                description: The domain name for the DB System.
                returned: always
                type: string
                sample: ansiblevcn955.ansiblevcn955.oraclevcn.com
            hostname:
                description: The user-friendly name for the DB System.
                returned: always
                type: string
                sample: db-system
            last_patch_history_entry_id:
                description: The OCID of the last patch history. This is updated
                             as soon as a patch operation is started.
                returned: always
                type: string
                sample: ocid1.lastpatchhistory.aaaa
            license_model:
                description: The Oracle license model that applies to all the databases
                             on the DB System
                returned: always
                type: string
                sample: LICENSE_INCLUDED
            lifecycle_details:
                description: Additional information about the current lifecycle state.
                returned: always
                type: string
                sample: details
            lifecycle_state:
                description: The current state of the DB System.
                returned: always
                type: string
                sample: AVAILABLE
            listener_port:
                description: The port number configured for the listener on the DB System.
                returned: always
                type: string
                sample: 1521
            node_count:
                description: Number of nodes in this DB system. For RAC DBs, this will be greater than 1.
                returned: always
                type: string
                sample: 2
            reco_storage_size_in_gb:
                description: RECO/REDO storage size, in GBs, that is currently allocated to the DB system.
                             This is applicable only for VM-based DBs.
                returned: always
                type: string
                sample: 1024
            scan_dns_record_id:
                description: The OCID of the DNS record for the SCAN IP addresses that are associated with the
                             DB System.
                returned: always
                type: string
                sample: ocid.dnsrecord.aaaa
            scan_ip_ids:
                description: The OCID of the Single Client Access Name (SCAN) IP addresses associated with the DB System.
                             SCAN IP addresses are typically used for load balancing and are not assigned to any interface.
                             Clusterware directs the requests to the appropriate nodes in the cluster. For a single-node
                             DB System, this list is empty.
                returned: always
                type: string
                sample: ocid1.scanip.aaaa
            shape:
                description: The shape of the DB System
                returned: always
                type: string
                sample: BM.DenseIO1.36
            ssh_public_keys:
                description: The public key portion of one or more key pairs used for SSH access to the DB System.
                returned: always
                type: string
                sample: ['ssh-rsa 3NzaC1y']
            subnet_id:
                description: The OCID of the subnet the DB System is associated with.
                returned: always
                type: string
                sample: ocid1.subnet.aaaa
            version:
                description: The version of the DB System.
                returned: always
                type: string
                sample: 12.2.0.1
            vip_ids:
                description: The OCID of the virtual IP (VIP) addresses associated with the DB System.
                returned: always
                type: string
                sample: ['159.28.0.1']
        sample: {
                    "availability_domain":"IwGV:US-ASHBURN-AD-2",
                    "freeform_tags":{"deployment":"production"},
                    "defined_tags":{"target_users":{"division":"accounts"}},
                    "backup_subnet_id":null,
                    "cluster_name":"db-clus-955",
                    "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "cpu_core_count":2,
                    "data_storage_percentage":80,
                    "data_storage_size_in_gbs":null,
                    "database_edition":"STANDARD_EDITION",
                    "disk_redundancy":"NORMAL",
                    "display_name":"ansible-db-system-955",
                    "domain":"ansiblevcn955.ansiblevcn955.oraclevcn.com",
                    "hostname":"db-system-955",
                    "id":"ocid1.dbsystem.oc1.iad.xxxxxEXAMPLExxxxx",
                    "last_patch_history_entry_id":null,
                    "license_model":"LICENSE_INCLUDED",
                    "lifecycle_details":null,
                    "lifecycle_state":"PROVISIONING",
                    "listener_port":1521,
                    "node_count":null,
                    "reco_storage_size_in_gb":null,
                    "scan_dns_record_id":null,
                    "scan_ip_ids":null,
                    "shape":"BM.DenseIO1.36",
                    "ssh_public_keys":["ssh-rsa AAA"],
                    "subnet_id":"ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx",
                    "time_created":"2018-02-10T19:21:44.171000+00:00",
                    "version":null,
                    "vip_ids":null
              }
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.facts.utils import get_file_content
from ansible.module_utils.oracle import oci_utils, oci_db_utils
import os

try:
    import copy
    from oci.database.database_client import DatabaseClient
    from oci.exceptions import ServiceError, ClientError
    from oci.util import to_dict
    from oci.database.models import (
        LaunchDbSystemDetails,
        LaunchDbSystemFromBackupDetails,
        CreateDbHomeDetails,
        CreateDbHomeFromBackupDetails,
        UpdateDbSystemDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


logger = None


def launch_or_update_db_system(db_client, module):
    result = dict(changed=False, db_system="")
    db_system_id = module.params.get("db_system_id")
    exclude_attributes = {"display_name": True, "domain": True, "node_count": True}
    try:
        if db_system_id is not None:
            result = update_db_system(db_client, module, db_system_id)
        else:
            module_copy = copy.deepcopy(module)
            module_copy.params.update(
                {
                    "ssh_public_keys": to_dict(
                        create_ssh_public_keys(
                            module_copy.params.get("ssh_public_keys")
                        )
                    )
                }
            )
            result = oci_utils.check_and_create_resource(
                resource_type="db_system",
                create_fn=launch_db_system,
                kwargs_create={"db_client": db_client, "module": module},
                list_fn=db_client.list_db_systems,
                kwargs_list={"compartment_id": module.params.get("compartment_id")},
                module=module_copy,
                exclude_attributes=exclude_attributes,
                model=LaunchDbSystemDetails(),
            )

    except ServiceError as ex:
        get_logger().error(
            "Unable to launch/update database system due to: %s", ex.message
        )
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error(
            "Unable to launch/update database system due to: %s", str(ex)
        )
        module.fail_json(msg=str(ex))

    return result


def launch_db_system(db_client, module):
    launch_db_system_details = None
    if module.params.get("source") == "DB_BACKUP":
        launch_db_system_details = LaunchDbSystemFromBackupDetails()
        launch_db_system_details.db_home = create_db_home_from_backup_details(
            module.params.get("db_home", None)
        )
    else:
        launch_db_system_details = LaunchDbSystemDetails()
        launch_db_system_details.db_home = create_db_home(
            module.params.get("db_home", None)
        )
    launch_db_system_details.ssh_public_keys = create_ssh_public_keys(
        module.params.get("ssh_public_keys", None)
    )
    for attribute in launch_db_system_details.attribute_map:
        if attribute not in ("db_home", "ssh_public_keys"):
            launch_db_system_details.__setattr__(
                attribute, module.params.get(attribute)
            )
    result = oci_utils.create_and_wait(
        resource_type="db_system",
        create_fn=db_client.launch_db_system,
        kwargs_create={"launch_db_system_details": launch_db_system_details},
        client=db_client,
        get_fn=db_client.get_db_system,
        get_param="db_system_id",
        module=module,
    )

    return result


def create_db_home(db_home_dict):
    if db_home_dict is None:
        raise ClientError(
            Exception(
                "Proper value for attribute db_home is mandatory for creating DB System"
            )
        )
    create_db_home_details = CreateDbHomeDetails()
    create_db_home_details.database = oci_db_utils.create_database_details(
        db_home_dict.get("database", None)
    )
    create_db_home_details.db_version = db_home_dict.get("db_version")
    create_db_home_details.display_name = db_home_dict.get("display_name")
    return create_db_home_details


def create_db_home_from_backup_details(db_home_dict):
    if db_home_dict is None:
        raise ClientError(
            Exception(
                "Proper value for attribute db_home is mandatory for creating DB System"
            )
        )
    create_db_home_for_backup_details = CreateDbHomeFromBackupDetails()
    create_db_home_for_backup_details.database = oci_db_utils.create_database_from_backup_details(
        db_home_dict.get("database", None)
    )
    create_db_home_for_backup_details.display_name = db_home_dict.get("display_name")
    return create_db_home_for_backup_details


def update_db_system(db_client, module, db_system_id):
    result = dict()
    changed = False
    db_system = oci_utils.get_existing_resource(
        db_client.get_db_system, module, db_system_id=module.params.get("db_system_id")
    )
    if db_system is None:
        raise ClientError(
            Exception("No DB System with id " + db_system_id + " is found for update")
        )
    primitive_attributes = [
        "cpu_core_count",
        "data_storage_size_in_gbs",
        "freeform_tags",
        "defined_tags",
    ]
    existing_ssh_public_keys = db_system.ssh_public_keys
    last_patch_history_entry_id = db_system.last_patch_history_entry_id
    purge_ssh_public_keys = module.params.get("purge_ssh_public_keys")
    delete_ssh_public_keys = module.params.get("delete_ssh_public_keys")
    update_db_system_details = UpdateDbSystemDetails()

    for attribute in primitive_attributes:
        changed = oci_utils.check_and_update_attributes(
            update_db_system_details,
            attribute,
            module.params.get(attribute, None),
            getattr(db_system, attribute),
            changed,
        )

    input_ssh_public_keys = create_ssh_public_keys(
        module.params.get("ssh_public_keys", None)
    )
    ssh_public_keys_changed = False
    if input_ssh_public_keys is not None:
        ssh_public_keys, ssh_public_keys_changed = oci_utils.get_component_list_difference(
            input_ssh_public_keys,
            existing_ssh_public_keys,
            purge_ssh_public_keys,
            delete_ssh_public_keys,
        )
    if ssh_public_keys_changed:
        update_db_system_details.ssh_public_keys = ssh_public_keys
    else:
        update_db_system_details.ssh_public_keys = existing_ssh_public_keys

    input_version_dict = module.params.get("version", None)
    version_changed, patch_details = oci_db_utils.is_version_changed(
        db_client.get_db_system_patch_history_entry,
        db_client.get_db_system_patch,
        db_system.version,
        input_version_dict,
        last_patch_history_entry_id,
        db_system_id=db_system_id,
    )
    if version_changed:
        update_db_system_details.version = patch_details
    changed = changed or ssh_public_keys_changed or version_changed
    if changed:
        result = oci_utils.update_and_wait(
            resource_type="db_system",
            update_fn=db_client.update_db_system,
            kwargs_update={
                "db_system_id": db_system_id,
                "update_db_system_details": update_db_system_details,
            },
            client=db_client,
            get_fn=db_client.get_db_system,
            get_param="db_system_id",
            module=module,
        )
    else:
        result["db_system"] = to_dict(db_system)
        result["changed"] = False
    return result


def create_ssh_public_keys(ssh_public_keys):
    if ssh_public_keys is None:
        return None
    result_ssh_public_keys = []
    for ssh_public_key in ssh_public_keys:
        result_ssh_public_keys.append(get_file_content(ssh_public_key))
    return result_ssh_public_keys


def delete_db_system(db_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="db_system",
        client=db_client,
        get_fn=db_client.get_db_system,
        kwargs_get={"db_system_id": module.params["db_system_id"]},
        delete_fn=db_client.terminate_db_system,
        kwargs_delete={"db_system_id": module.params["db_system_id"]},
        module=module,
    )

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_db_system")
    set_logger(logger)
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            db_system_id=dict(type="str", required=False, aliases=["id"]),
            availability_domain=dict(type="str", required=False),
            backup_subnet_id=dict(type="str", required=False),
            cluster_name=dict(type="str", required=False),
            cpu_core_count=dict(type=int, required=False),
            data_storage_percentage=dict(type=int, required=False),
            database_edition=dict(
                type="str",
                required=False,
                choices=[
                    "STANDARD_EDITION",
                    "ENTERPRISE_EDITION",
                    "ENTERPRISE_EDITION_EXTREME_PERFORMANCE",
                    "ENTERPRISE_EDITION_HIGH_PERFORMANCE",
                ],
            ),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
            db_home=dict(type=dict, required=False),
            disk_redundancy=dict(
                type="str", required=False, choices=["HIGH", "NORMAL"]
            ),
            display_name=dict(type="str", required=False),
            domain=dict(type="str", required=False),
            hostname=dict(type="str", required=False),
            initial_data_storage_size_in_gb=dict(type=int, required=False),
            data_storage_size_in_gbs=dict(type=int, required=False),
            license_model=dict(
                type="str",
                required=False,
                choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"],
            ),
            node_count=dict(type=int, required=False),
            shape=dict(type="str", required=False),
            ssh_public_keys=dict(type=list, required=False),
            subnet_id=dict(type="str", required=False),
            purge_ssh_public_keys=dict(
                type=bool, required=False, default=True, choices=[True, False]
            ),
            delete_ssh_public_keys=dict(
                type=bool, required=False, default=False, choices=[True, False]
            ),
            version=dict(type=dict, required=False),
            source=dict(
                type="str",
                required=False,
                default="NONE",
                choices=["DB_BACKUP", "NONE"],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["purge_ssh_public_keys", "delete_ssh_public_keys"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)
    if os.environ.get("OCI_DB_MOCK") is not None:
        db_client.base_client.session.headers.update(
            {"opc-host-serial": "FakeHostSerial"}
        )
    state = module.params["state"]

    if state == "present":
        result = launch_or_update_db_system(db_client, module)
    elif state == "absent":
        result = delete_db_system(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
