#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
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
module: oci_db_node_facts
short_description: Fetches details of one or more OCI DB Nodes
description:
    - Fetches details of the OCI DB Home.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment in which the
                     specified DB System exists
        required: false
    db_system_id:
        description: Identifier of the DB System under which the DB Node is available.
        required: false
    db_node_id:
        description: Identifier of the DB Node whose details needs to be fetched.
        required: false
        aliases: ['id']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""
EXAMPLES = """
#Fetch Db Nodes
- name: List all Db Nodes in a compartment and Db system
  oci_db_home_facts:
      compartment_id: 'ocid1.compartment..xcds'
      db_system_id: 'ocid1.dbsystem..xcds'
#Fetch a specific DB Node
- name: List a specific DB Node
  oci_db_node_facts:
      db_node_id: 'ocid1.dbnode..xcds'
"""

RETURN = """
    db_nodes:
        description: Attributes of the fetched DB Nodes.
        returned: success
        type: complex
        contains:
            db_system_id:
                description: Identifier of the  DB System under which the DB Node exists.
                returned: always
                type: string
                sample: ocid1.dbsystem.oc1.iad.xxxxxEXAMPLExxxxx
            hostname:
                description: The host name for the DB Node.
                returned: always
                type: string
                sample: ansible-db-node
            id:
                description: Identifier of the DB Node.
                returned: always
                type: string
                sample: ocid1.dbnode.oc1.iad.xxxxxEXAMPLExxxxx
            time_created:
                description: Date and time when the DB Node was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            software_storage_size_in_gb:
                description: Storage size, in GBs, of the software volume that
                             is allocated to the DB system. This is applicable
                             only for VM-based DBs.
                returned: always
                type: string
                sample: 1024
            vnic_id:
                description: The OCID of the VNIC of this DB Node
                returned: always
                type: string
                sample: ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx
            backup_vnic_id:
                description: The OCID of the backup VNIC of this DB Node
                returned: always
                type: string
                sample: ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx
            lifecycle_state:
                description: The current state of the DB Node.
                returned: always
                type: string
                sample: AVAILABLE
        sample: [{
                    "backup_vnic_id":"ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx",
                    "db_system_id":"ocid1.dbsystem.oc1.ia",
                    "hostname":"db-system-one",
                    "id":"ocid1.dbnode.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_state":"AVAILABLE",
                    "software_storage_size_in_gb":"1024",
                    "time_created":"2018-02-17T07:59:04.715000+00:00",
                    "vnic_id":"ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx"
                },
                {
                    "backup_vnic_id":"ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx",
                    "db_system_id":"ocid1.dbsystem.oc1.xvf",
                    "hostname":"db-system-two",
                    "id":"ocid1.dbnode.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_state":"AVAILABLE",
                    "software_storage_size_in_gb":"1024",
                    "time_created":"2018-02-17T07:59:04.715000+00:00",
                    "vnic_id":"ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx"
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


def list_db_nodes(db_client, module):
    result = dict(db_nodes="")
    compartment_id = module.params.get("compartment_id")
    db_node_id = module.params.get("db_node_id")
    db_system_id = module.params.get("db_system_id")
    try:
        if db_node_id:
            get_logger().debug("Listing Db Node %s", db_node_id)
            response = oci_utils.call_with_backoff(
                db_client.get_db_node, db_node_id=db_node_id
            )
            existing_db_nodes = [response.data]
        elif compartment_id and db_system_id:
            get_logger().debug(
                "Listing all Db Nodes under compartment %s", compartment_id
            )
            existing_db_nodes = oci_utils.list_all_resources(
                db_client.list_db_nodes,
                compartment_id=compartment_id,
                db_system_id=db_system_id,
            )
    except ServiceError as ex:
        get_logger().error("Unable to list Db Nodes due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["db_nodes"] = to_dict(existing_db_nodes)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_db_node_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            db_node_id=dict(type="str", required=False, aliases=["id"]),
            db_system_id=dict(type="str", required=False),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[
            ["compartment_id", "db_node_id"],
            ["db_system_id", "db_node_id"],
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)
    result = list_db_nodes(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
