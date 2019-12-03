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
module: oci_data_guard_association
short_description: Create a Data Guard Association and, perform various Database role transitions
                   of Databases associated with a Data Guard Association in OCI Database Cloud Service.
description:
    - Create an OCI Data Guard Association
    - Perform a switchover between Databases associated in a Data Guard Association
    - Perform a failover on standby Database associated in a Data Guard Association
    - Perform a reinstate on a disabled standby Database associated in a Data Guard Association
    - Since all operations of this module takes a long time, it is recommended to set the C(wait) to False. Use
      M(oci_data_guard_association_facts) to check the status of the operation as a separate task.
version_added: "2.5"
options:
    database_id:
        description: Identifier of the Database to which the Data Guard should be Associated.
        required: true
    data_guard_association_id:
        description: The identifier of the Data Guard Association. Mandatory for role transition
                     of the Databases associated with a specified Data Guard Association.
        required: false
        aliases: ['id']
    creation_type:
        description: Specifies where to create the associated database ExistingDbSystem is the
                     only supported  value.
        required: false
        choices: ['ExistingDbSystem']
        default: 'ExistingDbSystem'
    database_admin_password:
        description: A strong password for SYS, SYSTEM, and PDB Admin. The password
                     must be at least nine characters and contain at least two
                     uppercase,two lowercase, two numbers, and two special characters.
        required: false
    peer_db_system_id:
        description: The OCID of the DB System to create the standby database on.
        required: false
    protection_mode:
        description: The protection mode to set up between the primary and standby databases.
                     The only protection mode currently supported by the Database Service is
                     MAXIMUM_PERFORMANCE. Allowed values are MAXIMUM_AVAILABILITY, MAXIMUM_PERFORMANCE,
                     MAXIMUM_PROTECTION
        required: false
        choices: ['MAXIMUM_AVAILABILITY', 'MAXIMUM_PERFORMANCE', 'MAXIMUM_PROTECTION']
    transport_type:
        description: The redo transport type to use for this Data Guard association. The only transport type
                     currently supported by the Database Service is ASYNC. Allowed values are SYNC, ASYNC,
                     FASTSYNC.
        required: false
        choices: ['SYNC', 'ASYNC', 'FASTSYNC']
    state:
        description: Create a new dataguard association or perform role transitions within associated databases
                     of a dataguard association. For I(state=present), it gets created. For I(state=switchover),
                     I(state=failover), I(state=reinstate), switchover, failover and reinstate on databases gets
                     performed respectively.
        required: false
        default: 'present'
        choices: ['present', 'switchover', 'failover', 'reinstate']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_wait_options, oracle_creatable_resource ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create Data Guard Association
- name: Create Data Guard Association
  oci_data_guard_association:
      database_id: 'ocid1.database..abuw'
      creation_type: 'ExistingDbSystem'
      database_admin_password: 'pasword#_'
      protection_mode: 'MAXIMUM_PERFORMANCE'
      transport_type: 'ASYNC'
      peer_db_system_id: 'ocid1.dbsystem.xdvf'
      wait: False
      state: 'present'

# Perform switchover action on Data Guard Association
- name: Perform switchover operation to make the primary database to secondary
  oci_data_guard_association:
      database_id: 'ocid1.database.abuw'
      data_guard_association_id: 'ocid1.dgassociation.abuw'
      database_admin_password: 'pasword#_'
      state: 'switchover'

# Perform failover action on Data Guard Association
- name: Perform failover operation to make the standby database to primary
  oci_data_guard_association:
      database_id: 'ocid1.database.abuw'
      data_guard_association_id: 'ocid1.dgassociation.abuw'
      database_admin_password: 'pasword#_'
      state: 'failover'

# Perform reinstate action on Data Guard Association
- name: Perform reinstate operation to make the disable standby database to standby
  oci_data_guard_association:
      database_id: 'ocid1.database.abuw'
      data_guard_association_id: 'ocid1.dgassociation.abuw'
      database_admin_password: 'pasword#_'
      state: 'reinstate'
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
        sample: {
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
                }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_db_utils

try:
    from oci.database.database_client import DatabaseClient
    from oci.exceptions import ServiceError
    from oci.database.models import (
        CreateDataGuardAssociationToExistingDbSystemDetails,
        SwitchoverDataGuardAssociationDetails,
        FailoverDataGuardAssociationDetails,
        ReinstateDataGuardAssociationDetails,
    )
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def create_data_guard_association(db_client, module):
    result = dict(changed=False, data_guard_association="")
    database_id = module.params.get("database_id")

    try:
        create_data_guard_assoc_details = get_create_data_guard_association_from_creation_type(
            module
        )

        result = oci_utils.create_and_wait(
            resource_type="data_guard_association",
            create_fn=db_client.create_data_guard_association,
            kwargs_create={
                "database_id": database_id,
                "create_data_guard_association_details": create_data_guard_assoc_details,
            },
            client=db_client,
            get_fn=db_client.get_data_guard_association,
            get_param="database_id",
            module=module,
        )

    except ServiceError as ex:
        get_logger().error(
            "Unable to create Data Guard Association due to: %s", ex.message
        )
        module.fail_json(msg=ex.message)

    return result


def get_create_data_guard_association_from_creation_type(module):
    create_data_guard_association_details = get_creation_type_instance(module)
    if create_data_guard_association_details is None:
        module.fail_json("creation_type either not specified or not supported")
    for attribute in create_data_guard_association_details.attribute_map:
        create_data_guard_association_details.__setattr__(
            attribute, module.params.get(attribute)
        )
    return create_data_guard_association_details


def get_creation_type_instance(module):
    create_data_guard_association_details = None
    if module.params.get("creation_type") == "ExistingDbSystem":
        create_data_guard_association_details = (
            CreateDataGuardAssociationToExistingDbSystemDetails()
        )
    return create_data_guard_association_details


def perform_data_guard_operations(db_client, module):
    changed = False
    result = dict(changed=False, data_guard_association="")
    data_guard_association_id = module.params.get("data_guard_association_id")
    database_id = module.params.get("database_id")
    if data_guard_association_id is None or database_id is None:
        module.fail_json(
            msg="Data Guard Association related operation must contain valid database_id and data_guard_association_id"
        )
    data_guard_association = oci_utils.get_existing_resource(
        db_client.get_data_guard_association,
        module,
        database_id=database_id,
        data_guard_association_id=data_guard_association_id,
    )
    changed, target_fn, kwargs = get_operation_details(
        db_client, module, data_guard_association
    )
    if changed:
        kwargs.update(
            database_id=database_id, data_guard_association_id=data_guard_association_id
        )
        try:
            result = oci_db_utils.execute_function_and_wait(
                resource_type="data_guard_association",
                function=target_fn,
                kwargs_function=kwargs,
                client=db_client,
                get_fn=db_client.get_data_guard_association,
                get_param=None,
                kwargs_get={
                    "database_id": database_id,
                    "data_guard_association_id": data_guard_association_id,
                },
                module=module,
            )
        except ServiceError as ex:
            get_logger().error(
                "Unable to perform operation on  Data Guard Association due to: %s",
                ex.message,
            )
            module.fail_json(msg=ex.message)

    result["changed"] = changed
    result["data_guard_association"] = to_dict(data_guard_association)

    return result


def get_operation_details(db_client, module, existing_data_guard_association):
    changed = False
    target_fn = None
    kwargs = dict()
    state = module.params.get("state")
    if existing_data_guard_association is None:
        module.fail_json(msg="No Data Guard Association Found")
    data_guard_association_details = get_data_guard_association_object_details(
        module, state
    )
    if state == "failover":
        if existing_data_guard_association.role == "STANDBY":
            kwargs.update(
                failover_data_guard_association_details=data_guard_association_details
            )
            target_fn = db_client.failover_data_guard_association
            changed = True
    elif state == "switchover":
        if existing_data_guard_association.role == "PRIMARY":
            target_fn = db_client.switchover_data_guard_association
            kwargs.update(
                switchover_data_guard_association_details=data_guard_association_details
            )
            changed = True
    elif state == "reinstate":
        if existing_data_guard_association.role == "DISABLED_STANDBY":
            kwargs.update(
                reinstate_data_guard_association_details=data_guard_association_details
            )
            target_fn = db_client.reinstate_data_guard_association
            changed = True

    return changed, target_fn, kwargs


def get_data_guard_association_object_details(module, state):
    state_to_object_details_dict = dict(
        {
            "switchover": SwitchoverDataGuardAssociationDetails(),
            "failover": FailoverDataGuardAssociationDetails(),
            "reinstate": ReinstateDataGuardAssociationDetails(),
        }
    )
    data_guard_association_details = state_to_object_details_dict.get(state)
    data_guard_association_details.database_admin_password = module.params.get(
        "database_admin_password"
    )
    return data_guard_association_details


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_data_guard_association")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            database_id=dict(type="str", required=True),
            data_guard_association_id=dict(type="str", required=False, aliases=["id"]),
            creation_type=dict(
                type="str",
                required=False,
                default="ExistingDbSystem",
                choices=["ExistingDbSystem"],
            ),
            database_admin_password=dict(type="str", required=False, no_log=True),
            protection_mode=dict(
                type="str",
                required=False,
                choices=[
                    "MAXIMUM_AVAILABILITY",
                    "MAXIMUM_PERFORMANCE",
                    "MAXIMUM_PROTECTION",
                ],
            ),
            transport_type=dict(
                type="str", required=False, choices=["SYNC", "ASYNC", "FASTSYNC"]
            ),
            peer_db_system_id=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "switchover", "failover", "reinstate"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)
    state = module.params["state"]
    if state == "present":
        result = oci_utils.check_and_create_resource(
            resource_type="data_guard_association",
            create_fn=create_data_guard_association,
            kwargs_create={"db_client": db_client, "module": module},
            list_fn=db_client.list_data_guard_associations,
            kwargs_list={"database_id": module.params["database_id"]},
            module=module,
            model=get_creation_type_instance(module),
        )

    else:
        result = perform_data_guard_operations(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
