#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_database_pluggable_database_actions
short_description: Perform actions on a PluggableDatabase resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a PluggableDatabase resource in Oracle Cloud Infrastructure
    - For I(action=convert_to_regular), converts a Refreshable clone to Regular pluggable database (PDB).
      Pluggable Database will be in `READ_WRITE` openmode after conversion.
    - For I(action=disable_pluggable_database_management), disables the Database Management service for the pluggable database.
    - For I(action=enable_pluggable_database_management), enables the Database Management service for an Oracle Pluggable Database located in Oracle Cloud
      Infrastructure. This service allows the pluggable database to access tools including Metrics and Performance hub. Database Management is enabled at the
      pluggable database (PDB) level.
    - "For I(action=local_clone), **Deprecated.** Use L(CreatePluggableDatabase,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/database/latest/PluggableDatabase/CreatePluggableDatabase) for Pluggable Database LocalClone Operation.
      Clones and starts a pluggable database (PDB) in the same database (CDB) as the source PDB. The source PDB must be in the `READ_WRITE` openMode to perform
      the clone operation."
    - For I(action=modify_pluggable_database_management), updates one or more attributes of the Database Management service for the pluggable database.
    - For I(action=refresh), refreshes a pluggable database (PDB) Refreshable clone.
    - "For I(action=remote_clone), **Deprecated.** Use L(CreatePluggableDatabase,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/database/latest/PluggableDatabase/CreatePluggableDatabase) for Pluggable Database RemoteClone Operation.
      Clones a pluggable database (PDB) to a different database from the source PDB. The cloned PDB will be started upon completion of the clone operation. The
      source PDB must be in the `READ_WRITE` openMode when performing the clone.
      For Exadata Cloud@Customer instances, the source pluggable database (PDB) must be on the same Exadata Infrastructure as the target container database
      (CDB) to create a remote clone."
    - For I(action=rotate_pluggable_database_encryption_key), create a new version of the existing encryption key.
    - For I(action=start), starts a stopped pluggable database. The `openMode` value of the pluggable database will be `READ_WRITE` upon completion.
    - For I(action=stop), stops a pluggable database. The `openMode` value of the pluggable database will be `MOUNTED` upon completion.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    should_create_pdb_backup:
        description:
            - Indicates whether to take Pluggable Database Backup after the operation.
            - Applicable only for I(action=convert_to_regular).
        type: bool
    container_database_admin_password:
        description:
            - The DB system administrator password of the Container Database.
            - Applicable only for I(action=convert_to_regular).
        type: str
    tde_wallet_password:
        description:
            - The existing TDE wallet password of the Container Database.
            - Applicable only for I(action=convert_to_regular).
        type: str
    credential_details:
        description:
            - ""
            - Required for I(action=enable_pluggable_database_management).
        type: dict
        suboptions:
            user_name:
                description:
                    - The name of the Oracle Database user that will be used to connect to the database.
                type: str
                required: true
            password_secret_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
                      L(secret,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
                type: str
                required: true
    private_end_point_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the private endpoint.
            - Required for I(action=enable_pluggable_database_management).
        type: str
    service_name:
        description:
            - The name of the Oracle Database service that will be used to connect to the database.
            - Required for I(action=enable_pluggable_database_management).
        type: str
    protocol:
        description:
            - Protocol used by the database connection.
            - Applicable only for I(action=enable_pluggable_database_management)I(action=modify_pluggable_database_management).
        type: str
        choices:
            - "TCP"
            - "TCPS"
    port:
        description:
            - The port used to connect to the pluggable database.
            - Applicable only for I(action=enable_pluggable_database_management)I(action=modify_pluggable_database_management).
        type: int
    ssl_secret_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
              L(secret,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
            - Applicable only for I(action=enable_pluggable_database_management)I(action=modify_pluggable_database_management).
        type: str
    role:
        description:
            - The role of the user that will be connecting to the pluggable database.
            - Applicable only for I(action=enable_pluggable_database_management)I(action=modify_pluggable_database_management).
        type: str
        choices:
            - "SYSDBA"
            - "NORMAL"
    target_container_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the target CDB
            - Required for I(action=remote_clone).
        type: str
    source_container_db_admin_password:
        description:
            - The DB system administrator password of the source CDB.
            - Required for I(action=remote_clone).
        type: str
    cloned_pdb_name:
        description:
            - The name for the pluggable database (PDB). The name is unique in the context of a L(container database,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/database/latest/Database/). The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric
              characters. Special characters are not permitted. The pluggable database name should not be same as the container database name.
            - Required for I(action=local_clone), I(action=remote_clone).
        type: str
    pdb_admin_password:
        description:
            - "A strong password for PDB Admin of the newly cloned PDB. The password must be at least nine characters and contain at least two uppercase, two
              lowercase, two numbers, and two special characters. The special characters must be _, #, or -."
            - Applicable only for I(action=local_clone)I(action=remote_clone).
        type: str
    target_tde_wallet_password:
        description:
            - The existing TDE wallet password of the target CDB.
            - Applicable only for I(action=local_clone)I(action=remote_clone).
        type: str
    should_pdb_admin_account_be_locked:
        description:
            - The locked mode of the pluggable database admin account. If false, the user needs to provide the PDB Admin Password to connect to it.
              If true, the pluggable database will be locked and user cannot login to it.
            - Applicable only for I(action=local_clone)I(action=remote_clone).
        type: bool
    pluggable_database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the PluggableDatabase.
        type: str
        required: true
        choices:
            - "convert_to_regular"
            - "disable_pluggable_database_management"
            - "enable_pluggable_database_management"
            - "local_clone"
            - "modify_pluggable_database_management"
            - "refresh"
            - "remote_clone"
            - "rotate_pluggable_database_encryption_key"
            - "start"
            - "stop"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action convert_to_regular on pluggable_database
  oci_database_pluggable_database_actions:
    # required
    pluggable_database_id: "ocid1.pluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: convert_to_regular

    # optional
    should_create_pdb_backup: true
    container_database_admin_password: example-password
    tde_wallet_password: example-password

- name: Perform action disable_pluggable_database_management on pluggable_database
  oci_database_pluggable_database_actions:
    # required
    pluggable_database_id: "ocid1.pluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: disable_pluggable_database_management

- name: Perform action enable_pluggable_database_management on pluggable_database
  oci_database_pluggable_database_actions:
    # required
    credential_details:
      # required
      user_name: user_name_example
      password_secret_id: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
    private_end_point_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    service_name: service_name_example
    pluggable_database_id: "ocid1.pluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: enable_pluggable_database_management

    # optional
    protocol: TCP
    port: 56
    ssl_secret_id: "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
    role: SYSDBA

- name: Perform action local_clone on pluggable_database
  oci_database_pluggable_database_actions:
    # required
    cloned_pdb_name: cloned_pdb_name_example
    pluggable_database_id: "ocid1.pluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: local_clone

    # optional
    pdb_admin_password: example-password
    target_tde_wallet_password: example-password
    should_pdb_admin_account_be_locked: true

- name: Perform action modify_pluggable_database_management on pluggable_database
  oci_database_pluggable_database_actions:
    # required
    pluggable_database_id: "ocid1.pluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: modify_pluggable_database_management

    # optional
    credential_details:
      # required
      user_name: user_name_example
      password_secret_id: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
    private_end_point_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    service_name: service_name_example
    protocol: TCP
    port: 56
    ssl_secret_id: "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
    role: SYSDBA

- name: Perform action refresh on pluggable_database
  oci_database_pluggable_database_actions:
    # required
    pluggable_database_id: "ocid1.pluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: refresh

- name: Perform action remote_clone on pluggable_database
  oci_database_pluggable_database_actions:
    # required
    target_container_database_id: "ocid1.targetcontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    source_container_db_admin_password: example-password
    cloned_pdb_name: cloned_pdb_name_example
    pluggable_database_id: "ocid1.pluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: remote_clone

    # optional
    pdb_admin_password: example-password
    target_tde_wallet_password: example-password
    should_pdb_admin_account_be_locked: true

- name: Perform action rotate_pluggable_database_encryption_key on pluggable_database
  oci_database_pluggable_database_actions:
    # required
    pluggable_database_id: "ocid1.pluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: rotate_pluggable_database_encryption_key

- name: Perform action start on pluggable_database
  oci_database_pluggable_database_actions:
    # required
    pluggable_database_id: "ocid1.pluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: start

- name: Perform action stop on pluggable_database
  oci_database_pluggable_database_actions:
    # required
    pluggable_database_id: "ocid1.pluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: stop

"""

RETURN = """
pluggable_database:
    description:
        - Details of the PluggableDatabase resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the pluggable database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        container_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the CDB.
            returned: on success
            type: str
            sample: "ocid1.containerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
        pdb_name:
            description:
                - The name for the pluggable database (PDB). The name is unique in the context of a L(container database,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/database/latest/Database/). The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric
                  characters. Special characters are not permitted. The pluggable database name should not be same as the container database name.
            returned: on success
            type: str
            sample: pdb_name_example
        lifecycle_state:
            description:
                - The current state of the pluggable database.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Detailed message for the lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the pluggable database was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        connection_strings:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                pdb_default:
                    description:
                        - A host name-based PDB connection string.
                    returned: on success
                    type: str
                    sample: pdb_default_example
                pdb_ip_default:
                    description:
                        - An IP-based PDB connection string.
                    returned: on success
                    type: str
                    sample: pdb_ip_default_example
                all_connection_strings:
                    description:
                        - All connection strings to use to connect to the pluggable database.
                    returned: on success
                    type: dict
                    sample: {}
        open_mode:
            description:
                - "**Deprecated.** Use L(PluggableDatabaseNodeLevelDetails,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/database/latest/datatypes/PluggableDatabaseNodeLevelDetails) for OpenMode details.
                  The mode that pluggable database is in. Open mode can only be changed to READ_ONLY or MIGRATE directly from the backend (within the Oracle
                  Database software)."
            returned: on success
            type: str
            sample: READ_ONLY
        is_restricted:
            description:
                - The restricted mode of the pluggable database. If a pluggable database is opened in restricted mode,
                  the user needs both create a session and have restricted session privileges to connect to it.
            returned: on success
            type: bool
            sample: true
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
        pluggable_database_management_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                management_status:
                    description:
                        - The status of the Pluggable Database Management service.
                    returned: on success
                    type: str
                    sample: ENABLING
        refreshable_clone_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_refreshable_clone:
                    description:
                        - Indicates whether the Pluggable Database is a refreshable clone.
                    returned: on success
                    type: bool
                    sample: true
        pdb_node_level_details:
            description:
                - "Pluggable Database Node Level Details.
                  Example: [{\\"nodeName\\" : \\"node1\\", \\"openMode\\" : \\"READ_WRITE\\"}, {\\"nodeName\\" : \\"node2\\", \\"openMode\\" :
                  \\"READ_ONLY\\"}]"
            returned: on success
            type: complex
            contains:
                node_name:
                    description:
                        - The Node name of the Database Instance.
                    returned: on success
                    type: str
                    sample: node_name_example
                open_mode:
                    description:
                        - The mode that pluggable database is in. Open mode can only be changed to READ_ONLY or MIGRATE directly from the backend (within the
                          Oracle Database software).
                    returned: on success
                    type: str
                    sample: READ_ONLY
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "container_database_id": "ocid1.containerdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "pdb_name": "pdb_name_example",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "connection_strings": {
            "pdb_default": "pdb_default_example",
            "pdb_ip_default": "pdb_ip_default_example",
            "all_connection_strings": {}
        },
        "open_mode": "READ_ONLY",
        "is_restricted": true,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "pluggable_database_management_config": {
            "management_status": "ENABLING"
        },
        "refreshable_clone_config": {
            "is_refreshable_clone": true
        },
        "pdb_node_level_details": [{
            "node_name": "node_name_example",
            "open_mode": "READ_ONLY"
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import ConvertToRegularPluggableDatabaseDetails
    from oci.database.models import EnablePluggableDatabaseManagementDetails
    from oci.database.models import LocalClonePluggableDatabaseDetails
    from oci.database.models import ModifyPluggableDatabaseManagementDetails
    from oci.database.models import RemoteClonePluggableDatabaseDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PluggableDatabaseActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        convert_to_regular
        disable_pluggable_database_management
        enable_pluggable_database_management
        local_clone
        modify_pluggable_database_management
        refresh
        remote_clone
        rotate_pluggable_database_encryption_key
        start
        stop
    """

    def __init__(self, *args, **kwargs):
        super(PluggableDatabaseActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = oci_config_utils.create_service_client(
            self.module, WorkRequestClient
        )

    @staticmethod
    def get_module_resource_id_param():
        return "pluggable_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("pluggable_database_id")

    def get_get_fn(self):
        return self.client.get_pluggable_database

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_pluggable_database,
            pluggable_database_id=self.module.params.get("pluggable_database_id"),
        )

    def convert_to_regular(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ConvertToRegularPluggableDatabaseDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.convert_to_regular_pluggable_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                convert_to_regular_pluggable_database_details=action_details,
                pluggable_database_id=self.module.params.get("pluggable_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def disable_pluggable_database_management(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_pluggable_database_management,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pluggable_database_id=self.module.params.get("pluggable_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def enable_pluggable_database_management(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, EnablePluggableDatabaseManagementDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_pluggable_database_management,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pluggable_database_id=self.module.params.get("pluggable_database_id"),
                enable_pluggable_database_management_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def local_clone(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, LocalClonePluggableDatabaseDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.local_clone_pluggable_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                local_clone_pluggable_database_details=action_details,
                pluggable_database_id=self.module.params.get("pluggable_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def modify_pluggable_database_management(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ModifyPluggableDatabaseManagementDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.modify_pluggable_database_management,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pluggable_database_id=self.module.params.get("pluggable_database_id"),
                modify_pluggable_database_management_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def refresh(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.refresh_pluggable_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pluggable_database_id=self.module.params.get("pluggable_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def remote_clone(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoteClonePluggableDatabaseDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remote_clone_pluggable_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                remote_clone_pluggable_database_details=action_details,
                pluggable_database_id=self.module.params.get("pluggable_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def rotate_pluggable_database_encryption_key(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.rotate_pluggable_database_encryption_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pluggable_database_id=self.module.params.get("pluggable_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def start(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_pluggable_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pluggable_database_id=self.module.params.get("pluggable_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def stop(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_pluggable_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pluggable_database_id=self.module.params.get("pluggable_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


PluggableDatabaseActionsHelperCustom = get_custom_class(
    "PluggableDatabaseActionsHelperCustom"
)


class ResourceHelper(
    PluggableDatabaseActionsHelperCustom, PluggableDatabaseActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            should_create_pdb_backup=dict(type="bool"),
            container_database_admin_password=dict(type="str", no_log=True),
            tde_wallet_password=dict(type="str", no_log=True),
            credential_details=dict(
                type="dict",
                options=dict(
                    user_name=dict(type="str", required=True),
                    password_secret_id=dict(type="str", required=True),
                ),
            ),
            private_end_point_id=dict(type="str"),
            service_name=dict(type="str"),
            protocol=dict(type="str", choices=["TCP", "TCPS"]),
            port=dict(type="int"),
            ssl_secret_id=dict(type="str"),
            role=dict(type="str", choices=["SYSDBA", "NORMAL"]),
            target_container_database_id=dict(type="str"),
            source_container_db_admin_password=dict(type="str", no_log=True),
            cloned_pdb_name=dict(type="str"),
            pdb_admin_password=dict(type="str", no_log=True),
            target_tde_wallet_password=dict(type="str", no_log=True),
            should_pdb_admin_account_be_locked=dict(type="bool"),
            pluggable_database_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "convert_to_regular",
                    "disable_pluggable_database_management",
                    "enable_pluggable_database_management",
                    "local_clone",
                    "modify_pluggable_database_management",
                    "refresh",
                    "remote_clone",
                    "rotate_pluggable_database_encryption_key",
                    "start",
                    "stop",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="pluggable_database",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
