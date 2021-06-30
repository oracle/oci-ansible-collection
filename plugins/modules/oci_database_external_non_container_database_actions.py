#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_database_external_non_container_database_actions
short_description: Perform actions on an ExternalNonContainerDatabase resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an ExternalNonContainerDatabase resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), move the external non-container database and its dependent resources to the specified compartment.
      For more information about moving external non-container databases, see
      L(Moving Database Resources to a Different Compartment,https://docs.cloud.oracle.com/Content/Database/Concepts/databaseoverview.htm#moveRes).
    - For I(action=disable_external_non_container_database_database_management), disable Database Management Service for the external non-container database.
      For more information about the Database Management Service, see
      L(Database Management Service,https://docs.cloud.oracle.com/Content/ExternalDatabase/Concepts/databasemanagementservice.htm).
    - For I(action=disable_external_non_container_database_operations_insights), disable Operations Insights for the external non-container database.
    - For I(action=enable_external_non_container_database_database_management), enable Database Management Service for the external non-container database.
      For more information about the Database Management Service, see
      L(Database Management Service,https://docs.cloud.oracle.com/Content/ExternalDatabase/Concepts/databasemanagementservice.htm).
    - For I(action=enable_external_non_container_database_operations_insights), enable Operations Insights for the external non-container database.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the resource to.
            - Required for I(action=change_compartment).
        type: str
    external_non_container_database_id:
        description:
            - The external non-container database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    license_model:
        description:
            - The Oracle license model that applies to the external database.
            - Required for I(action=enable_external_non_container_database_database_management).
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    external_database_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
              L(external database connector,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
            - Required for I(action=enable_external_non_container_database_database_management),
              I(action=enable_external_non_container_database_operations_insights).
        type: str
    action:
        description:
            - The action to perform on the ExternalNonContainerDatabase.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "disable_external_non_container_database_database_management"
            - "disable_external_non_container_database_operations_insights"
            - "enable_external_non_container_database_database_management"
            - "enable_external_non_container_database_operations_insights"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on external_non_container_database
  oci_database_external_non_container_database_actions:
    compartment_id: "ocid.compartment.oc1..unique_ID"
    external_non_container_database_id: "ocid1.externalnoncontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: "change_compartment"

- name: Perform action disable_external_non_container_database_database_management on external_non_container_database
  oci_database_external_non_container_database_actions:
    external_non_container_database_id: "ocid1.externalnoncontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: disable_external_non_container_database_database_management

- name: Perform action disable_external_non_container_database_operations_insights on external_non_container_database
  oci_database_external_non_container_database_actions:
    external_non_container_database_id: "ocid1.externalnoncontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: disable_external_non_container_database_operations_insights

- name: Perform action enable_external_non_container_database_database_management on external_non_container_database
  oci_database_external_non_container_database_actions:
    external_database_connector_id: "ocid1.externaldatabaseconnector..unique_ID"
    license_model: "BRING_YOUR_OWN_LICENSE"
    external_non_container_database_id: "ocid1.externalnoncontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: "enable_external_non_container_database_database_management"

- name: Perform action enable_external_non_container_database_operations_insights on external_non_container_database
  oci_database_external_non_container_database_actions:
    external_database_connector_id: "ocid1.externaldatabaseconnector..unique_ID"
    external_non_container_database_id: "ocid1.externalnoncontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: "enable_external_non_container_database_operations_insights"

"""

RETURN = """
external_non_container_database:
    description:
        - Details of the ExternalNonContainerDatabase resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
                    type: string
                    sample: ENABLING
                operations_insights_connector_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
                          L(external database connector,https://docs.cloud.oracle.com/en-
                          us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
                    returned: on success
                    type: string
                    sample: "ocid1.operationsinsightsconnector.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: string
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
            type: string
            sample: display_name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure external database
                  resource.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of the Oracle Cloud Infrastructure external database resource.
            returned: on success
            type: string
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the database was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        db_unique_name:
            description:
                - The `DB_UNIQUE_NAME` of the external database.
            returned: on success
            type: string
            sample: db_unique_name_example
        db_id:
            description:
                - The Oracle Database ID, which identifies an Oracle Database located outside of Oracle Cloud.
            returned: on success
            type: string
            sample: "ocid1.db.oc1..xxxxxxEXAMPLExxxxxx"
        database_version:
            description:
                - The Oracle Database version.
            returned: on success
            type: string
            sample: database_version_example
        database_edition:
            description:
                - The Oracle Database edition.
            returned: on success
            type: string
            sample: STANDARD_EDITION
        time_zone:
            description:
                - The time zone of the external database.
                  It is a time zone offset (a character type in the format '[+|-]TZH:TZM') or a time zone region name,
                  depending on how the time zone value was specified when the database was created / last altered.
            returned: on success
            type: string
            sample: time_zone_example
        character_set:
            description:
                - The character set of the external database.
            returned: on success
            type: string
            sample: character_set_example
        ncharacter_set:
            description:
                - The national character of the external database.
            returned: on success
            type: string
            sample: ncharacter_set_example
        db_packs:
            description:
                - The database packs licensed for the external Oracle Database.
            returned: on success
            type: string
            sample: db_packs_example
        database_configuration:
            description:
                - The Oracle Database configuration
            returned: on success
            type: string
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
                    type: string
                    sample: ENABLING
                database_management_connection_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
                          L(external database connector,https://docs.cloud.oracle.com/en-
                          us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
                    returned: on success
                    type: string
                    sample: "ocid1.databasemanagementconnection.oc1..xxxxxxEXAMPLExxxxxx"
                license_model:
                    description:
                        - The Oracle license model that applies to the external database.
                    returned: on success
                    type: string
                    sample: LICENSE_INCLUDED
    sample: {
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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import ChangeCompartmentDetails
    from oci.database.models import (
        EnableExternalNonContainerDatabaseDatabaseManagementDetails,
    )
    from oci.database.models import (
        EnableExternalNonContainerDatabaseOperationsInsightsDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalNonContainerDatabaseActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        disable_external_non_container_database_database_management
        disable_external_non_container_database_operations_insights
        enable_external_non_container_database_database_management
        enable_external_non_container_database_operations_insights
    """

    def __init__(self, *args, **kwargs):
        super(ExternalNonContainerDatabaseActionsHelperGen, self).__init__(
            *args, **kwargs
        )
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "external_non_container_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_non_container_database_id")

    def get_get_fn(self):
        return self.client.get_external_non_container_database

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_non_container_database,
            external_non_container_database_id=self.module.params.get(
                "external_non_container_database_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_external_non_container_database_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_compartment_details=action_details,
                external_non_container_database_id=self.module.params.get(
                    "external_non_container_database_id"
                ),
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

    def disable_external_non_container_database_database_management(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_external_non_container_database_database_management,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_non_container_database_id=self.module.params.get(
                    "external_non_container_database_id"
                ),
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

    def disable_external_non_container_database_operations_insights(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_external_non_container_database_operations_insights,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_non_container_database_id=self.module.params.get(
                    "external_non_container_database_id"
                ),
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

    def enable_external_non_container_database_database_management(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params,
            EnableExternalNonContainerDatabaseDatabaseManagementDetails,
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_external_non_container_database_database_management,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_non_container_database_id=self.module.params.get(
                    "external_non_container_database_id"
                ),
                enable_external_non_container_database_database_management_details=action_details,
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

    def enable_external_non_container_database_operations_insights(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params,
            EnableExternalNonContainerDatabaseOperationsInsightsDetails,
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_external_non_container_database_operations_insights,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_non_container_database_id=self.module.params.get(
                    "external_non_container_database_id"
                ),
                enable_external_non_container_database_operations_insights_details=action_details,
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


ExternalNonContainerDatabaseActionsHelperCustom = get_custom_class(
    "ExternalNonContainerDatabaseActionsHelperCustom"
)


class ResourceHelper(
    ExternalNonContainerDatabaseActionsHelperCustom,
    ExternalNonContainerDatabaseActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            external_non_container_database_id=dict(
                aliases=["id"], type="str", required=True
            ),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            external_database_connector_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "disable_external_non_container_database_database_management",
                    "disable_external_non_container_database_operations_insights",
                    "enable_external_non_container_database_database_management",
                    "enable_external_non_container_database_operations_insights",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="external_non_container_database",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
