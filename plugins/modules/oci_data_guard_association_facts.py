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
module: oci_data_guard_association_facts
short_description: Fetches details of an OCI Data Guard Association
description:
    - Fetches details of an OCI Data Guard Association
version_added: "2.5"
options:
    database_id:
        description: Identifier of the database whose Data Guard Association
                     details needs to be fetched
        required: false
    data_guard_association_id:
        description: Identifier of the Data Guard Association whose details needs to be fetched.
        required: false
        aliases: ['id']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# List all Data Guard Association related to a database
- name: List all Data Guard Association of a Database
  oci_data_guard_association_facts:
      database_id: 'ocid1.database..abuw'

# List a specific Data Guard Association related to a database
- name: List all Data Guard Association of a Database
  oci_data_guard_association_facts:
      database_id: 'ocid1.database..abuw'
      data_guard_association_id: 'ocid1.dgassociation.abuw'
"""

RETURN = """
    data_guard_association:
        description: Attributes of the Data Guard Association.
        returned: success
        type: complex
        contains:
            apply_lag:
                description: The lag time between updates to the primary database and application
                             of the redo data on the standby database, as computed by the reporting
                             database.
                returned: always
                type: string
                sample: 9 seconds
            apply_rate:
                description: The rate at which redo logs are synced between the associated databases.
                returned: always
                type: string
                sample: 17.00 KByte/s
            database_id:
                description: Identifier of the  reporting Database.
                returned: always
                type: string
                sample: ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx
            id:
                description: Identifier of the Data Guard Association.
                returned: always
                type: string
                sample: ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx
            time_created:
                description: Date and time when the Data Guard Association was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            lifecycle_details:
                description: Additional information about the current lifecycle_state, if available.
                returned: always
                type: string
                sample: Details of lifecycle state
            lifecycle_state:
                description: The current state of the Data Guard Association.
                returned: always
                type: string
                sample: AVAILABLE
            peer_data_guard_association_id:
                description: Identifier of the peer database's Data Guard association.
                returned: always
                type: string
                sample: ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx
            peer_database_id:
                description: Identifier of the associated peer database.
                returned: always
                type: string
                sample: ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx
            peer_db_system_id:
                description: Identifier of the  DB System containing the associated peer database.
                returned: always
                type: string
                sample: ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx
            peer_role:
                description: The role of the peer database in this Data Guard association.
                returned: always
                type: string
                sample: STANDBY
            protection_mode:
                description: The protection mode of this Data Guard association.
                returned: always
                type: string
                sample: MAXIMUM_PERFORMANCE
            role:
                description: The role of the reporting database in this Data Guard Association.
                returned: always
                type: string
                sample: PRIMARY
            transport_type:
                description: The redo transport type used by this Data Guard Association.
                returned: always
                type: string
                sample: ASYNC
        sample: [{
                    "apply_lag":"7 seconds",
                    "apply_rate":"15 KByte/s",
                    "database_id":"ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx",
                    "id":"ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_details":null,
                    "lifecycle_state":"PROVISIONING",
                    "peer_data_guard_association_id":"ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx",
                    "peer_database_id":"ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx",
                    "peer_db_home_id":"ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx",
                    "peer_db_system_id":"ocid1.dbsystem.oc1.iad.xxxxxEXAMPLExxxxx",
                    "peer_role":"STANDBY",
                    "protection_mode":"MAXIMUM_PERFORMANCE",
                    "role":"PRIMARY",
                    "time_created":"2018-03-03T06:55:49.463000+00:00",
                    "transport_type":"ASYNC"
              },
              {
                    "apply_lag":"7 seconds",
                    "apply_rate":"15 KByte/s",
                    "database_id":"ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx",
                    "id":"ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_details":null,
                    "lifecycle_state":"PROVISIONING",
                    "peer_data_guard_association_id":"ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx",
                    "peer_database_id":"ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx",
                    "peer_db_home_id":"ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx",
                    "peer_db_system_id":"ocid1.dbsystem.oc1.iad.xxxxxEXAMPLExxxxx",
                    "peer_role":"STANDBY",
                    "protection_mode":"MAXIMUM_PERFORMANCE",
                    "role":"PRIMARY",
                    "time_created":"2018-03-03T06:55:49.463000+00:00",
                    "transport_type":"ASYNC"
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


def list_data_guard_associations(db_client, module):
    result = dict(data_guard_associations="")
    database_id = module.params.get("database_id")
    data_guard_association_id = module.params.get("data_guard_association_id")
    try:
        if data_guard_association_id:
            get_logger().debug(
                "Listing Data Guard Association %s", data_guard_association_id
            )
            response = oci_utils.call_with_backoff(
                db_client.get_data_guard_association,
                database_id=database_id,
                data_guard_association_id=data_guard_association_id,
            )
            existing_data_guard_associations = [response.data]
        else:
            get_logger().debug(
                "Listing all Data Guard Association for Database %s", database_id
            )
            existing_data_guard_associations = oci_utils.list_all_resources(
                db_client.list_data_guard_associations, database_id=database_id
            )
    except ServiceError as ex:
        get_logger().error(
            "Unable to list Data Guard Associations due to %s", ex.message
        )
        module.fail_json(msg=ex.message)
    result["data_guard_associations"] = to_dict(existing_data_guard_associations)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_data_guard_association_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            database_id=dict(type="str", required=True),
            data_guard_association_id=dict(type="str", required=False, aliases=["id"]),
        )
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)
    result = list_data_guard_associations(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
