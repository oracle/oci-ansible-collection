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
module: oci_db_node
short_description: Control the lifecycle of a DB Node in OCI's Database Cloud Service.
description:
    - Stop/start a DB Node
    - Reset a DB Node
    - Soft-reset a DB Node
    - All operations of this module returns after triggering the lifecycle operation. Use M(oci_db_node_facts)
      to check the status of the operation.
version_added: "2.5"
options:
    db_node_id:
        description: Identifier of the DB Node whose lifecycle state is to be controlled.
        required: true
        aliases: ['id']
    state:
        description: The state of the DB Node that must be asserted to. When I(state=stop), specified DB Node is
                     powered off. When I(state=start), the specified DB Node is powered on. When I(state=softreset), an
                     ACPI shutdown is initiated and specified DB Node is powered on. When I(state=reset), specified DB
                     Node is powered off and then powered on. Note that I(state=softreset) and I(state=reset) states are
                     not idempotent. Every time a play is executed with these C(state) options, a shutdown and a
                     power-on sequence is executed against the DB node.
        required: true
        default: "start"
        choices: ['stop', 'start', 'reset', 'softreset']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_wait_options ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Assert that the database node is stopped
- name: Stop a Database Node
  oci_db_node:
    db_node_id: "ocid1.dbnode.aaaa"
    state: 'stop'
"""

RETURN = """
    db_node:
        description: Attributes of the Db Node.
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
        sample: {
                    "backup_vnic_id":"ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx",
                    "db_system_id":"ocid1.dbsystem.oc1.ia",
                    "hostname":"db-system-one",
                    "id":"ocid1.dbnode.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_state":"AVAILABLE",
                    "software_storage_size_in_gb":"1024",
                    "time_created":"2018-02-17T07:59:04.715000+00:00",
                    "vnic_id":"ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx"
                }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_db_utils

try:
    from oci.database.database_client import DatabaseClient
    from oci.exceptions import ServiceError, ClientError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def perform_db_node_action(db_client, module):
    db_node = None
    result = dict(changed=False, db_node="")
    try:
        db_node = oci_utils.get_existing_resource(
            db_client.get_db_node, module, db_node_id=module.params.get("db_node_id")
        )
        if db_node:
            result = db_node_action(db_client, module, db_node)
    except ServiceError as ex:
        get_logger().error(
            "Unable to perform the action on Db Node due to: %s", ex.message
        )
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error(
            "Unable to perform the action on Db Node due to: %s", str(ex)
        )
        module.fail_json(msg=str(ex))

    return result


def db_node_action(db_client, module, existing_db_node):
    result = dict()
    input_action = module.params.get("state")
    action_map = {
        "stop": "STOP",
        "start": "START",
        "reset": "RESET",
        "softreset": "SOFTRESET",
    }
    desired_lifecycle_states = {
        "stop": "STOPPED",
        "start": "AVAILABLE",
        "reset": "AVAILABLE",
        "softreset": "AVAILABLE",
    }
    intermediate_states = {
        "stop": "STOPPING",
        "start": "STARTING",
        "reset": "STOPPING",
        "softreset": "STOPPING",
    }
    logger.debug(
        "Attempting to change the state of DB Node %s from %s to %s",
        existing_db_node.id,
        existing_db_node.lifecycle_state,
        desired_lifecycle_states[input_action],
    )
    logger.debug(
        "Current state of the DB Node %s is %s",
        existing_db_node.id,
        existing_db_node.lifecycle_state,
    )
    if (
        existing_db_node.lifecycle_state != desired_lifecycle_states[input_action]
        and existing_db_node.lifecycle_state != intermediate_states[input_action]
    ) or (input_action in ("reset", "softreset")):
        logger.info(
            "Changing state of DB Node %s from %s to %s",
            existing_db_node.id,
            existing_db_node.lifecycle_state,
            desired_lifecycle_states[input_action],
        )
        result = oci_db_utils.execute_function_and_wait(
            resource_type="db_node",
            function=db_client.db_node_action,
            kwargs_function={
                "db_node_id": existing_db_node.id,
                "action": action_map[input_action],
            },
            client=db_client,
            get_fn=db_client.get_db_node,
            get_param="db_node_id",
            module=module,
        )
    else:
        result["db_node"] = to_dict(existing_db_node)
        result["changed"] = False
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_db_node")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            db_node_id=dict(type="str", required=True, aliases=["id"]),
            state=dict(
                type="str",
                required=False,
                default="start",
                choices=["stop", "start", "reset", "softreset"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)
    result = perform_db_node_action(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
