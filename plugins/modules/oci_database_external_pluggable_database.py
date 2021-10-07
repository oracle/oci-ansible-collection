#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_database_external_pluggable_database
short_description: Manage an ExternalPluggableDatabase resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an ExternalPluggableDatabase resource in Oracle Cloud Infrastructure
    - For I(state=present), registers a new L(ExternalPluggableDatabase,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/database/latest/datatypes/CreateExternalPluggableDatabaseDetails)
      resource.
    - "This resource has the following action operations in the M(oci_external_pluggable_database_actions) module: change_compartment,
      disable_external_pluggable_database_database_management, disable_external_pluggable_database_operations_insights,
      enable_external_pluggable_database_database_management, enable_external_pluggable_database_operations_insights."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the the non-container database that was converted
              to a pluggable database to create this resource.
        type: str
    external_container_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the
              L(external container database,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/latest/datatypes/CreateExternalContainerDatabaseDetails)
              that contains
              the specified L(external pluggable database,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/database/latest/datatypes/CreateExternalPluggableDatabaseDetails) resource.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - The user-friendly name for the external database. The name does not have to be unique.
            - Required for create using I(state=present), update using I(state=present) with external_pluggable_database_id present.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
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
    external_pluggable_database_id:
        description:
            - The ExternalPluggableDatabaseId L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ExternalPluggableDatabase.
            - Use I(state=present) to create or update an ExternalPluggableDatabase.
            - Use I(state=absent) to delete an ExternalPluggableDatabase.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create external_pluggable_database
  oci_database_external_pluggable_database:
    compartment_id: "ocid1.[tenancy|compartment].oc1.unique_ID"
    display_name: "myTestExternalCdb"
    external_container_database_id: "ocid1.externalcontainerdatabase.oc1.<example_unique_ID>"

- name: Update external_pluggable_database using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_external_pluggable_database:
    display_name: "myExternalPdb"

- name: Update external_pluggable_database
  oci_database_external_pluggable_database:
    display_name: myTestExternalCdb
    external_pluggable_database_id: "ocid1.externalpluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete external_pluggable_database
  oci_database_external_pluggable_database:
    external_pluggable_database_id: "ocid1.externalpluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete external_pluggable_database using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_external_pluggable_database:
    compartment_id: ocid1.[tenancy|compartment].oc1.unique_ID
    display_name: myTestExternalCdb
    state: absent

"""

RETURN = """
external_pluggable_database:
    description:
        - Details of the ExternalPluggableDatabase resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the the non-container database that was converted
                  to a pluggable database to create this resource.
            returned: on success
            type: str
            sample: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
        external_container_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the
                  L(external container database,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/database/latest/datatypes/CreateExternalContainerDatabaseDetails) that contains
                  the specified L(external pluggable database,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/database/latest/datatypes/CreateExternalPluggableDatabaseDetails) resource.
            returned: on success
            type: str
            sample: "ocid1.externalcontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
        operations_insights_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                operations_insights_status:
                    description:
                        - The status of Operations Insights
                    returned: on success
                    type: str
                    sample: ENABLING
                operations_insights_connector_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
                          L(external database connector,https://docs.cloud.oracle.com/en-
                          us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
                    returned: on success
                    type: str
                    sample: "ocid1.operationsinsightsconnector.oc1..xxxxxxEXAMPLExxxxxx"
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
        display_name:
            description:
                - The user-friendly name for the external database. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure external database
                  resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of the Oracle Cloud Infrastructure external database resource.
            returned: on success
            type: str
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the database was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        db_unique_name:
            description:
                - The `DB_UNIQUE_NAME` of the external database.
            returned: on success
            type: str
            sample: db_unique_name_example
        db_id:
            description:
                - The Oracle Database ID, which identifies an Oracle Database located outside of Oracle Cloud.
            returned: on success
            type: str
            sample: "ocid1.db.oc1..xxxxxxEXAMPLExxxxxx"
        database_version:
            description:
                - The Oracle Database version.
            returned: on success
            type: str
            sample: database_version_example
        database_edition:
            description:
                - The Oracle Database edition.
            returned: on success
            type: str
            sample: STANDARD_EDITION
        time_zone:
            description:
                - The time zone of the external database.
                  It is a time zone offset (a character type in the format '[+|-]TZH:TZM') or a time zone region name,
                  depending on how the time zone value was specified when the database was created / last altered.
            returned: on success
            type: str
            sample: time_zone_example
        character_set:
            description:
                - The character set of the external database.
            returned: on success
            type: str
            sample: character_set_example
        ncharacter_set:
            description:
                - The national character of the external database.
            returned: on success
            type: str
            sample: ncharacter_set_example
        db_packs:
            description:
                - The database packs licensed for the external Oracle Database.
            returned: on success
            type: str
            sample: db_packs_example
        database_configuration:
            description:
                - The Oracle Database configuration
            returned: on success
            type: str
            sample: RAC
        database_management_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                database_management_status:
                    description:
                        - The status of the Database Management service.
                    returned: on success
                    type: str
                    sample: ENABLING
                database_management_connection_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
                          L(external database connector,https://docs.cloud.oracle.com/en-
                          us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
                    returned: on success
                    type: str
                    sample: "ocid1.databasemanagementconnection.oc1..xxxxxxEXAMPLExxxxxx"
                license_model:
                    description:
                        - The Oracle license model that applies to the external database.
                    returned: on success
                    type: str
                    sample: LICENSE_INCLUDED
    sample: {
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "external_container_database_id": "ocid1.externalcontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "operations_insights_config": {
            "operations_insights_status": "ENABLING",
            "operations_insights_connector_id": "ocid1.operationsinsightsconnector.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "PROVISIONING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "db_unique_name": "db_unique_name_example",
        "db_id": "ocid1.db.oc1..xxxxxxEXAMPLExxxxxx",
        "database_version": "database_version_example",
        "database_edition": "STANDARD_EDITION",
        "time_zone": "time_zone_example",
        "character_set": "character_set_example",
        "ncharacter_set": "ncharacter_set_example",
        "db_packs": "db_packs_example",
        "database_configuration": "RAC",
        "database_management_config": {
            "database_management_status": "ENABLING",
            "database_management_connection_id": "ocid1.databasemanagementconnection.oc1..xxxxxxEXAMPLExxxxxx",
            "license_model": "LICENSE_INCLUDED"
        }
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreateExternalPluggableDatabaseDetails
    from oci.database.models import UpdateExternalPluggableDatabaseDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalPluggableDatabaseHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(ExternalPluggableDatabaseHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_module_resource_id_param(self):
        return "external_pluggable_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_pluggable_database_id")

    def get_get_fn(self):
        return self.client.get_external_pluggable_database

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_pluggable_database,
            external_pluggable_database_id=self.module.params.get(
                "external_pluggable_database_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["external_container_database_id", "display_name"]

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
            self.client.list_external_pluggable_databases, **kwargs
        )

    def get_create_model_class(self):
        return CreateExternalPluggableDatabaseDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_external_pluggable_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_external_pluggable_database_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateExternalPluggableDatabaseDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_external_pluggable_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_pluggable_database_id=self.module.params.get(
                    "external_pluggable_database_id"
                ),
                update_external_pluggable_database_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_external_pluggable_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_pluggable_database_id=self.module.params.get(
                    "external_pluggable_database_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ExternalPluggableDatabaseHelperCustom = get_custom_class(
    "ExternalPluggableDatabaseHelperCustom"
)


class ResourceHelper(
    ExternalPluggableDatabaseHelperCustom, ExternalPluggableDatabaseHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            source_id=dict(type="str"),
            external_container_database_id=dict(type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            external_pluggable_database_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="external_pluggable_database",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
