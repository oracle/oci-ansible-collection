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
module: oci_autonomous_database
short_description: Create,update and terminate an Autonomous Database in OCI Database Cloud Service.
description:
    - Create an OCI Autonomous Database
    - Update an OCI Autonomous Database, if present, with a new display name
    - Terminate an OCI Autonomous Database, if present.
    - Restore a specific state of an OCI Autonomous Database
    - Start and Stop an OCI Autonomous Database
    - Since all operations of this module takes a long time, it is recommended to set the C(wait) to False. Use
      M(oci_autonomous_database_facts) to check the status of the operation as a separate task.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which this Autonomous Database would be created. Mandatory for
                     create operation.
        required: false
    admin_password:
        description: A strong password for Admin. The password must be between 12 and 60 characters long, and must
                     contain at least 1 uppercase, 1 lowercase and 2 numeric characters. It cannot contain the double
                     quote symbol ("). It must be different than the last 4 passwords.
        required: false
    autonomous_database_id:
        description: Identifier of the existing Autonomous Database which required to be updated, terminated, restored,
                     started or stopped. Mandatory for terminate, update, restore, start and stop.
        required: false
        aliases: ['id']
    cpu_core_count:
        description: The number of CPU cores to be made available to the Autonomous Database.
        required: false
    display_name:
        description: The user-friendly name for the Autonomous Database. It does not have to be unique.
        required: false
    data_storage_size_in_tbs:
        description: The size, in terabytes, of the data volume that will be created and attached to the database.
                     This storage can later be scaled up if needed.
        required: false
    license_model:
        description: The Oracle license model that applies to all the databases on the Autonomous Database. The default
                     is LICENSE_INCLUDED.
        required: false
        choices: ['LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE']
    db_name:
        description: The database name. The name must begin with an alphabetic character and can contain a maximum of 14
                     alphanumeric characters. Special characters are not permitted. The database name must be unique in
                     the tenancy.
        required: false
    timestamp:
        description: The time to restore the database to.
        required: false
    password:
        description: The password to encrypt the keys inside the wallet. The password must be at least 8 characters long and
                     must include at least 1 letter and either 1 numeric character or 1 special character. I(password) is
                     required if I(state='generate_wallet').
        required: false
    wallet_file:
        description: The destination file path with file name when downloading wallet. The file must have 'zip' extension.
                     I(wallet_file) is required if I(state='generate_wallet').
        required: false
    force:
        description: Force overwriting existing wallet file when downloading wallet.
        required: false
        default: true
        type: bool
        aliases: [ 'overwrite' ]
    state:
        description: Create, update, terminate, restore, start, stop and generate wallet for Autonomous Database. For I(state=present), if it
                     does not exist, it gets created. If it exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent', 'restore', 'start', 'stop', 'generate_wallet']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create Autonomous Database
- name: Create Autonomous Database
  oci_autonomous_database:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx..qndq'
    admin_password: 'BEstr0ng_#1'
    data_storage_size_in_tbs: 1
    cpu_core_count: 2
    db_name: 'autonomousdb'
    display_name: 'autonomousdb'
    initial_data_storage_size_in_tbs: 2
    license_model: 'LICENSE_INCLUDED'
    node_count: 1
    freeform_tags:
        deployment: 'production'
    defined_tags:
        target_users:
            division: 'documentation'
    wait: False
    state: 'present'

# Update Autonomous Database's CPU core count
- name: Update Autonomous Database
  oci_autonomous_database:
    autonomous_database_id: 'ocid1.autonomousdatabase.oc1..xxxxxEXAMPLExxxxx..qndq'
    cpu_core_count: 4
    state: 'present'

# Restore Autonomous Database
- name: Restore Autonomous Database with the time to restore the database to.
  oci_autonomous_database:
    autonomous_database_id: 'ocid1.autonomousdatabase.oc1..xxxxxEXAMPLExxxxx..qndq'
    timestamp: '2018-03-23T00:59:07.032Z'
    state: 'restore'

# Start Autonomous Database
- name: Start Autonomous Database
  autonomous_database:
    autonomous_database_id: 'ocid1.autonomousdatabase.oc1..xxxxxEXAMPLExxxxx..qndq'
    state: 'start'

# Stop Autonomous Database
- name: Stop Autonomous Database
  oci_autonomous_database:
    autonomous_database_id: 'ocid1.autonomousdatabase.oc1..xxxxxEXAMPLExxxxx..qndq'
    state: 'stop'

# Download wallet for Autonomous Database
- name: Download wallet for Autonomous Database
  oci_autonomous_database:
    autonomous_database_id: 'ocid1.autonomousdatabase.oc1..xxxxxEXAMPLExxxxx'
    password: 'BEstr0ng_#1'
    wallet_file: '/tmp/atp_wallet.zip'
    state: 'generate_wallet'

# Delete Autonomous Database
- name: Delete Autonomous Database
  oci_autonomous_database:
    autonomous_database_id: 'ocid1.autonomousdatabase.oc1..xxxxxEXAMPLExxxxx..qndq'
    state: 'absent'
"""

RETURN = """
    autonomous_database:
        description: Attributes of the launched/updated Autonomous Database. For delete, deleted Autonomous Database
                     description will be returned.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the Autonomous Database
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf.xxxxxEXAMPLExxxxx
            connection_strings:
                description: The connection string used to connect to the Autonomous Database.
                             The username for the Service Console is ADMIN. Use the password you entered
                             when creating the Autonomous Database for the password value.
                returned: always
                type: dict
                sample: {"high": "adwc.EXAMPLE1.oraclecloud.com:1522/EXAMPLE1_autodb_high.atp.oraclecloud.com",
                         "low": "adwc.EXAMPLE2.oraclecloud.com:1522/EXAMPLE2_autodb_low.atp.oraclecloud.com",
                         "medium": "adwc.EXAMPLE3.oraclecloud.com:1522/EXAMPLE3_autodb_medium.atp.oraclecloud.com"}
            cpu_core_count:
                description: The number of CPU cores to enable.
                returned: always
                type: string
                sample: 2
            time_created:
                description: Date and time when the Autonomous Database was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            data_storage_size_in_tbs:
                description: Data storage size, in terrabytes, that is currently available to the Autonomous Database.
                returned: always
                type: string
                sample: 2048
            id:
                description: The identifier of the Autonomous Database
                returned: always
                type: string
                sample: ocid1.autonomousdatabase.oc1.xzvf.xxxxxEXAMPLExxxxx
            display_name:
                description: The user-friendly name for the Autonomous Database.
                returned: always
                type: string
                sample: ansibleautodb
            db_name:
                description: The database name.
                returned: always
                type: string
                sample: ansibleautodb
            license_model:
                description: The Oracle license model that applies to all the databases
                             on the Autonomous Database
                returned: always
                type: string
                sample: LICENSE_INCLUDED
            service_console_url:
                description: The URL of the Service Console for the Autonomous Database.
                returned: always
                type: string
                sample: https://example1.oraclecloud.com/console/index.html?
                        tenant_name=OCID1.TENANCY.OC1..xxxxxEXAMPLExxxxx
                        &database_name=ANSIBLEAUTODB&service_type=ATP
            lifecycle_details:
                description: Additional information about the current lifecycle state.
                returned: always
                type: string
                sample: details
            lifecycle_state:
                description: The current state of the Autonomous Database.
                returned: always
                type: string
                sample: AVAILABLE

        sample: {
                  "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                  "connection_strings":{
                                         "high": "adwc.EXAMPLE1.oraclecloud.com:1522/EXAMPLE1_autodb_high.atp.oraclecloud.com",
                                         "low": "adwc.EXAMPLE2.oraclecloud.com:1522/EXAMPLE2_autodb_low.atp.oraclecloud.com",
                                         "medium": "adwc.EXAMPLE3.oraclecloud.com:1522/EXAMPLE3_autodb_medium.atp.oraclecloud.com"
                                       },
                  "cpu_core_count":1,
                  "data_storage_size_in_tbs":1,
                  "db_name":"autodbbackup",
                  "defined_tags":{
                       "ansible_tag_namespace_integration_test_1":{
                       "ansible_tag_1":"initial"
                   }
                  },
                  "display_name":"ansible-autonomous-database-955",
                  "freeform_tags":{
                       "system_license":"trial"
                   },
                  "id":"ocid1.autonomousdatabase.oc1.iad.xxxxxEXAMPLExxxxx",
                  "license_model":"LICENSE_INCLUDED",
                  "lifecycle_details":null,
                  "lifecycle_state":"AVAILABLE",
                  "service_console_url":"https://example1.oraclecloud.com/console/index.html?
                        tenant_name=OCID1.TENANCY.OC1..xxxxxEXAMPLExxxxx
                        &database_name=ANSIBLEAUTODB&service_type=ATP",
                  "time_created":"2018-09-22T15:06:55.426000+00:00"
              }
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils
from ansible.module_utils.oracle import oci_db_utils
from ansible.module_utils._text import to_bytes
import os

try:
    from oci.database.database_client import DatabaseClient
    from oci.exceptions import ServiceError, ClientError
    from oci.util import to_dict
    from oci.database.models import (
        CreateAutonomousDatabaseDetails,
        UpdateAutonomousDatabaseDetails,
        RestoreAutonomousDatabaseDetails,
        GenerateAutonomousDatabaseWalletDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_or_update_autonomous_database(db_client, module):
    result = dict(changed=False, autonomous_database="")
    autonomous_database_id = module.params.get("autonomous_database_id")
    try:
        if autonomous_database_id:
            result = update_autonomous_database(db_client, module)
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="autonomous_database",
                create_fn=create_autonomous_database,
                kwargs_create={"db_client": db_client, "module": module},
                list_fn=db_client.list_autonomous_databases,
                kwargs_list={"compartment_id": module.params.get("compartment_id")},
                module=module,
                model=CreateAutonomousDatabaseDetails(),
            )
    except ServiceError as ex:
        get_logger().error(
            "Unable to create/update autonomous database due to: %s", ex.message
        )
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error(
            "Unable to create/update autonomous database due to: %s", str(ex)
        )
        module.fail_json(msg=str(ex))

    return result


def create_autonomous_database(db_client, module):
    create_autonomous_database_details = CreateAutonomousDatabaseDetails()
    for attribute in create_autonomous_database_details.attribute_map:
        create_autonomous_database_details.__setattr__(
            attribute, module.params.get(attribute)
        )

    result = oci_utils.create_and_wait(
        resource_type="autonomous_database",
        create_fn=db_client.create_autonomous_database,
        kwargs_create={
            "create_autonomous_database_details": create_autonomous_database_details
        },
        client=db_client,
        get_fn=db_client.get_autonomous_database,
        get_param="autonomous_database_id",
        module=module,
    )
    return result


def update_autonomous_database(db_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type="autonomous_database",
        get_fn=db_client.get_autonomous_database,
        kwargs_get={"autonomous_database_id": module.params["autonomous_database_id"]},
        update_fn=db_client.update_autonomous_database,
        client=db_client,
        primitive_params_update=["autonomous_database_id"],
        kwargs_non_primitive_update={
            UpdateAutonomousDatabaseDetails: "update_autonomous_database_details"
        },
        module=module,
        update_attributes=UpdateAutonomousDatabaseDetails().attribute_map,
    )
    return result


def delete_autonomous_database(db_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="autonomous_database",
        client=db_client,
        get_fn=db_client.get_autonomous_database,
        kwargs_get={"autonomous_database_id": module.params["autonomous_database_id"]},
        delete_fn=db_client.delete_autonomous_database,
        kwargs_delete={
            "autonomous_database_id": module.params["autonomous_database_id"]
        },
        module=module,
    )

    return result


def restore_autonomous_database(db_client, module):
    result = dict(changed=True, autonomous_database="")
    autonomous_database_id = module.params.get("autonomous_database_id")
    restore_autonomous_database_details = RestoreAutonomousDatabaseDetails()
    for attribute in restore_autonomous_database_details.attribute_map:
        restore_autonomous_database_details.__setattr__(
            attribute, module.params.get(attribute)
        )

    result = oci_db_utils.execute_function_and_wait(
        resource_type="autonomous_database",
        function=db_client.restore_autonomous_database,
        kwargs_function={
            "autonomous_database_id": autonomous_database_id,
            "restore_autonomous_database_details": restore_autonomous_database_details,
        },
        client=db_client,
        get_fn=db_client.get_autonomous_database,
        get_param="autonomous_database_id",
        module=module,
        states=["AVAILABLE", "FAILED"],
    )
    return result


def start_or_stop_autonomous_database(db_client, module):
    autonomous_database_id = module.params.get("autonomous_database_id")
    autonomous_database = oci_utils.get_existing_resource(
        db_client.get_autonomous_database,
        module,
        autonomous_database_id=autonomous_database_id,
    )
    if autonomous_database is None:
        raise ClientError(
            Exception(
                "No Autonomous Database with id "
                + autonomous_database_id
                + " is found for update"
            )
        )

    return perform_start_or_stop(
        db_client, autonomous_database, autonomous_database_id, module
    )


def perform_start_or_stop(
    db_client, autonomous_database, autonomous_database_id, module
):
    result = dict()
    idempotent_lifecycle_state = []
    target_state = []

    lifecycle_func = None
    state = module.params.get("state")
    if state == "start":
        idempotent_lifecycle_state = ["AVAILABLE", "STARTING"]
        target_state = ["AVAILABLE"]
        lifecycle_func = db_client.start_autonomous_database
    elif state == "stop":
        idempotent_lifecycle_state = ["STOPPED", "STOPPING"]
        target_state = ["STOPPED"]
        lifecycle_func = db_client.stop_autonomous_database

    if autonomous_database.lifecycle_state not in idempotent_lifecycle_state:
        result = oci_db_utils.execute_function_and_wait(
            resource_type="autonomous_database",
            function=lifecycle_func,
            kwargs_function={"autonomous_database_id": autonomous_database_id},
            client=db_client,
            get_fn=db_client.get_autonomous_database,
            get_param="autonomous_database_id",
            module=module,
            states=target_state,
        )
    else:
        result["autonomous_database"] = to_dict(autonomous_database)
        result["changed"] = False
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def generate_wallet(db_client, module):
    result = dict(changed=False)
    autonomous_database_id = module.params.get("autonomous_database_id")
    generate_autonomous_database_wallet_details = (
        GenerateAutonomousDatabaseWalletDetails()
    )
    generate_autonomous_database_wallet_details.password = module.params.get("password")
    wallet_file = module.params.get("wallet_file")

    try:
        if wallet_file is None or len(wallet_file.strip()) == 0:
            raise ClientError(Exception("Wallet file must be declared"))
        if module.params.get("force") or not os.path.isfile(to_bytes(wallet_file)):
            response = oci_utils.call_with_backoff(
                db_client.generate_autonomous_database_wallet,
                autonomous_database_id=autonomous_database_id,
                generate_autonomous_database_wallet_details=generate_autonomous_database_wallet_details,
            )
            result["changed"] = oci_db_utils.write_stream_to_file(
                response.data, module.params.get("wallet_file")
            )
        else:
            result["msg"] = (
                "Wallet file  %s already exists. Use force option to overwrite."
                % wallet_file
            )
    except ServiceError as ex:
        get_logger().error(
            "Unable to get autonomous database wallet due to: %s", ex.message
        )
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error(
            "Unable to get autonomous database wallet due to: %s", str(ex)
        )
        module.fail_json(msg=str(ex))

    return result


def main():
    logger = oci_utils.get_logger("oci_autonomous_database")
    set_logger(logger)

    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            admin_password=dict(type="str", required=False, no_log=True),
            password=dict(type="str", required=False, no_log=True),
            autonomous_database_id=dict(type="str", required=False, aliases=["id"]),
            cpu_core_count=dict(type=int, required=False),
            data_storage_size_in_tbs=dict(type=int, required=False),
            db_name=dict(type="str", required=False),
            display_name=dict(type="str", required=False),
            license_model=dict(
                type="str",
                required=False,
                choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"],
            ),
            timestamp=dict(type="str", required=False),
            wallet_file=dict(type="str", required=False),
            force=dict(
                type="bool", required=False, default=True, aliases=["overwrite"]
            ),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=[
                    "present",
                    "absent",
                    "restore",
                    "start",
                    "stop",
                    "generate_wallet",
                ],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        required_if=[("state", "generate_wallet", ["password", "wallet_file"])],
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
        result = create_or_update_autonomous_database(db_client, module)
    elif state == "absent":
        result = delete_autonomous_database(db_client, module)
    elif state == "restore":
        result = restore_autonomous_database(db_client, module)
    elif state == "generate_wallet":
        result = generate_wallet(db_client, module)
    else:
        result = start_or_stop_autonomous_database(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
