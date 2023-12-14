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
module: oci_database_pluggable_database
short_description: Manage a PluggableDatabase resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a PluggableDatabase resource in Oracle Cloud Infrastructure
    - For I(state=present), creates and starts a pluggable database in the specified container database.
      Pluggable Database can be created using different operations (e.g. LocalClone, RemoteClone, Relocate ) with this API.
      Use the L(StartPluggableDatabase,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/latest/PluggableDatabase/StartPluggableDatabase) and
      L(StopPluggableDatabase,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/latest/PluggableDatabase/StopPluggableDatabase) APIs to start and stop
      the pluggable database.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_pluggable_database_actions) module: convert_to_regular,
      disable_pluggable_database_management, enable_pluggable_database_management, local_clone, modify_pluggable_database_management, refresh, remote_clone,
      rotate_pluggable_database_encryption_key, start, stop."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
    pdb_name:
        description:
            - The name for the pluggable database (PDB). The name is unique in the context of a L(container database,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/database/latest/Database/). The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric
              characters. Special characters are not permitted. The pluggable database name should not be same as the container database name.
            - Required for create using I(state=present).
        type: str
    container_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the CDB
            - Required for create using I(state=present).
        type: str
    pdb_admin_password:
        description:
            - "A strong password for PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers,
              and two special characters. The special characters must be _, #, or -."
        type: str
    tde_wallet_password:
        description:
            - The existing TDE wallet password of the CDB.
        type: str
    should_pdb_admin_account_be_locked:
        description:
            - The locked mode of the pluggable database admin account. If false, the user needs to provide the PDB Admin Password to connect to it.
              If true, the pluggable database will be locked and user cannot login to it.
        type: bool
    container_database_admin_password:
        description:
            - The DB system administrator password of the Container Database.
        type: str
    should_create_pdb_backup:
        description:
            - Indicates whether to take Pluggable Database Backup after the operation.
        type: bool
    pdb_creation_type_details:
        description:
            - ""
        type: dict
        suboptions:
            dblink_username:
                description:
                    - The name of the DB link user.
                    - Applicable when creation_type is one of ['REMOTE_CLONE_PDB', 'RELOCATE_PDB']
                type: str
            dblink_user_password:
                description:
                    - The DB link user password.
                    - Applicable when creation_type is one of ['REMOTE_CLONE_PDB', 'RELOCATE_PDB']
                type: str
            source_container_database_admin_password:
                description:
                    - The DB system administrator password of the source Container Database.
                    - Required when creation_type is one of ['REMOTE_CLONE_PDB', 'RELOCATE_PDB']
                type: str
            refreshable_clone_details:
                description:
                    - ""
                    - Applicable when creation_type is 'REMOTE_CLONE_PDB'
                type: dict
                suboptions:
                    is_refreshable_clone:
                        description:
                            - Indicates whether Pluggable Database is a refreshable clone.
                            - Applicable when creation_type is 'REMOTE_CLONE_PDB'
                        type: bool
            creation_type:
                description:
                    - The Pluggable Database creation type.
                type: str
                choices:
                    - "RELOCATE_PDB"
                    - "REMOTE_CLONE_PDB"
                    - "LOCAL_CLONE_PDB"
                required: true
            source_pluggable_database_id:
                description:
                    - The OCID of the Source Pluggable Database.
                type: str
                required: true
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
    pluggable_database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the PluggableDatabase.
            - Use I(state=present) to create or update a PluggableDatabase.
            - Use I(state=absent) to delete a PluggableDatabase.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create pluggable_database
  oci_database_pluggable_database:
    # required
    pdb_name: pdb_name_example
    container_database_id: "ocid1.containerdatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    pdb_admin_password: example-password
    tde_wallet_password: example-password
    should_pdb_admin_account_be_locked: true
    container_database_admin_password: example-password
    should_create_pdb_backup: true
    pdb_creation_type_details:
      # required
      source_container_database_admin_password: example-password
      creation_type: RELOCATE_PDB
      source_pluggable_database_id: "ocid1.sourcepluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      dblink_username: dblink_username_example
      dblink_user_password: example-password
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update pluggable_database
  oci_database_pluggable_database:
    # required
    pluggable_database_id: "ocid1.pluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete pluggable_database
  oci_database_pluggable_database:
    # required
    pluggable_database_id: "ocid1.pluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreatePluggableDatabaseDetails
    from oci.database.models import UpdatePluggableDatabaseDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PluggableDatabaseHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(PluggableDatabaseHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = oci_config_utils.create_service_client(
            self.module, WorkRequestClient
        )

    def get_possible_entity_types(self):
        return super(PluggableDatabaseHelperGen, self).get_possible_entity_types() + [
            "pluggabledatabase",
            "pluggabledatabases",
            "databasepluggabledatabase",
            "databasepluggabledatabases",
            "pluggabledatabaseresource",
            "pluggabledatabasesresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "pluggable_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("pluggable_database_id")

    def get_get_fn(self):
        return self.client.get_pluggable_database

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_pluggable_database, pluggable_database_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_pluggable_database,
            pluggable_database_id=self.module.params.get("pluggable_database_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "pdb_name"]

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
            self.client.list_pluggable_databases, **kwargs
        )

    def get_create_model_class(self):
        return CreatePluggableDatabaseDetails

    def get_exclude_attributes(self):
        return [
            "tde_wallet_password",
            "container_database_admin_password",
            "should_create_pdb_backup",
            "pdb_creation_type_details",
            "pdb_admin_password",
            "should_pdb_admin_account_be_locked",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_pluggable_database,
            call_fn_args=(),
            call_fn_kwargs=dict(create_pluggable_database_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdatePluggableDatabaseDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_pluggable_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pluggable_database_id=self.module.params.get("pluggable_database_id"),
                update_pluggable_database_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_pluggable_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pluggable_database_id=self.module.params.get("pluggable_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


PluggableDatabaseHelperCustom = get_custom_class("PluggableDatabaseHelperCustom")


class ResourceHelper(PluggableDatabaseHelperCustom, PluggableDatabaseHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            pdb_name=dict(type="str"),
            container_database_id=dict(type="str"),
            pdb_admin_password=dict(type="str", no_log=True),
            tde_wallet_password=dict(type="str", no_log=True),
            should_pdb_admin_account_be_locked=dict(type="bool"),
            container_database_admin_password=dict(type="str", no_log=True),
            should_create_pdb_backup=dict(type="bool"),
            pdb_creation_type_details=dict(
                type="dict",
                options=dict(
                    dblink_username=dict(type="str"),
                    dblink_user_password=dict(type="str", no_log=True),
                    source_container_database_admin_password=dict(
                        type="str", no_log=True
                    ),
                    refreshable_clone_details=dict(
                        type="dict",
                        options=dict(is_refreshable_clone=dict(type="bool")),
                    ),
                    creation_type=dict(
                        type="str",
                        required=True,
                        choices=["RELOCATE_PDB", "REMOTE_CLONE_PDB", "LOCAL_CLONE_PDB"],
                    ),
                    source_pluggable_database_id=dict(type="str", required=True),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            pluggable_database_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
