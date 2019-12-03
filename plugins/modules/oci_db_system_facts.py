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
module: oci_db_system_facts
short_description: Fetches details of the OCI DB System
description:
    - Fetches details of the OCI DB System.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment in which this
                     DB System exists
        required: false
    db_system_id:
        description: Identifier of the DB System whose details needs to be fetched.
        required: false
        aliases: ['id']
    backup_id:
        description: The OCID of the backup. Specify a backupId to list only the DB Systems that support creating a
                     database using this backup in this compartment.
        required: false
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
#Fetch DB System
- name: List all DB System in a compartment
  oci_db_system_facts:
      compartment_id: 'ocid1.compartment..xcds'

#Fetch specific DB System
- name: List a specific DB System
  oci_db_system_facts:
      db_system_id: 'ocid1.dbsystem..xcds'
"""

RETURN = """
    db_system:
        description: Attributes of the Fetched DB System.
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
        sample: [{
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
              }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.database.database_client import DatabaseClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def list_db_systems(db_client, module):
    result = dict(db_systems="")
    compartment_id = module.params.get("compartment_id")
    db_system_id = module.params.get("db_system_id")
    try:
        if compartment_id:
            get_logger().debug(
                "Listing all DB Systems under compartment %s", compartment_id
            )
            optional_list_method_params = ["backup_id", "display_name"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            existing_db_systems = oci_utils.list_all_resources(
                db_client.list_db_systems,
                compartment_id=compartment_id,
                **optional_kwargs
            )
        elif db_system_id:
            get_logger().debug("Listing DB System %s", db_system_id)
            response = oci_utils.call_with_backoff(
                db_client.get_db_system, db_system_id=db_system_id
            )
            existing_db_systems = [response.data]
    except ServiceError as ex:
        get_logger().error("Unable to list DB Systems due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["db_systems"] = to_dict(existing_db_systems)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_db_system_facts")
    set_logger(logger)
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            db_system_id=dict(type="str", required=False, aliases=["id"]),
            backup_id=dict(type="str", required=False),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["compartment_id", "db_system_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)
    result = list_db_systems(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
