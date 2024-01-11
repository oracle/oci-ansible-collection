#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_database_external_container_database_actions
short_description: Perform actions on an ExternalContainerDatabase resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an ExternalContainerDatabase resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), move the L(external container database,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/database/latest/datatypes/CreateExternalContainerDatabaseDetails)
      and its dependent resources to the specified compartment.
      For more information about moving external container databases, see
      L(Moving Database Resources to a Different Compartment,https://docs.cloud.oracle.com/Content/Database/Concepts/databaseoverview.htm#moveRes).
    - For I(action=disable_external_container_database_database_management), disable Database Management service for the external container database.
    - For I(action=disable_external_container_database_stack_monitoring), disable Stack Monitoring for the external container database.
    - For I(action=enable_external_container_database_database_management), enables Database Management Service for the external container database.
      For more information about the Database Management Service, see
      L(Database Management Service,https://docs.cloud.oracle.com/Content/ExternalDatabase/Concepts/databasemanagementservice.htm).
    - For I(action=enable_external_container_database_stack_monitoring), enable Stack Monitoring for the external container database.
    - For I(action=scan_external_container_database_pluggable_databases), scans for pluggable databases in the specified external container database.
      This operation will return un-registered pluggable databases in the L(GetWorkRequest,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/workrequests/20160918/WorkRequest/GetWorkRequest) operation.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the resource to.
            - Required for I(action=change_compartment).
        type: str
    license_model:
        description:
            - The Oracle license model that applies to the external database.
            - Required for I(action=enable_external_container_database_database_management).
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    external_container_database_id:
        description:
            - The ExternalContainerDatabase L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    external_database_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
              L(external database connector,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
            - Required for I(action=enable_external_container_database_database_management), I(action=enable_external_container_database_stack_monitoring),
              I(action=scan_external_container_database_pluggable_databases).
        type: str
    action:
        description:
            - The action to perform on the ExternalContainerDatabase.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "disable_external_container_database_database_management"
            - "disable_external_container_database_stack_monitoring"
            - "enable_external_container_database_database_management"
            - "enable_external_container_database_stack_monitoring"
            - "scan_external_container_database_pluggable_databases"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on external_container_database
  oci_database_external_container_database_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    external_container_database_id: "ocid1.externalcontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action disable_external_container_database_database_management on external_container_database
  oci_database_external_container_database_actions:
    # required
    external_container_database_id: "ocid1.externalcontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: disable_external_container_database_database_management

- name: Perform action disable_external_container_database_stack_monitoring on external_container_database
  oci_database_external_container_database_actions:
    # required
    external_container_database_id: "ocid1.externalcontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: disable_external_container_database_stack_monitoring

- name: Perform action enable_external_container_database_database_management on external_container_database
  oci_database_external_container_database_actions:
    # required
    license_model: LICENSE_INCLUDED
    external_container_database_id: "ocid1.externalcontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    external_database_connector_id: "ocid1.externaldatabaseconnector.oc1..xxxxxxEXAMPLExxxxxx"
    action: enable_external_container_database_database_management

- name: Perform action enable_external_container_database_stack_monitoring on external_container_database
  oci_database_external_container_database_actions:
    # required
    external_container_database_id: "ocid1.externalcontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    external_database_connector_id: "ocid1.externaldatabaseconnector.oc1..xxxxxxEXAMPLExxxxxx"
    action: enable_external_container_database_stack_monitoring

- name: Perform action scan_external_container_database_pluggable_databases on external_container_database
  oci_database_external_container_database_actions:
    # required
    external_container_database_id: "ocid1.externalcontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    external_database_connector_id: "ocid1.externaldatabaseconnector.oc1..xxxxxxEXAMPLExxxxxx"
    action: scan_external_container_database_pluggable_databases

"""

RETURN = """
external_container_database:
    description:
        - Details of the ExternalContainerDatabase resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
        stack_monitoring_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                stack_monitoring_status:
                    description:
                        - The status of Stack Monitoring.
                    returned: on success
                    type: str
                    sample: ENABLING
                stack_monitoring_connector_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
                          L(external database connector,https://docs.cloud.oracle.com/en-
                          us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
                    returned: on success
                    type: str
                    sample: "ocid1.stackmonitoringconnector.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
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
        },
        "stack_monitoring_config": {
            "stack_monitoring_status": "ENABLING",
            "stack_monitoring_connector_id": "ocid1.stackmonitoringconnector.oc1..xxxxxxEXAMPLExxxxxx"
        }
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
    from oci.database.models import ChangeCompartmentDetails
    from oci.database.models import (
        EnableExternalContainerDatabaseDatabaseManagementDetails,
    )
    from oci.database.models import (
        EnableExternalContainerDatabaseStackMonitoringDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalContainerDatabaseActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        disable_external_container_database_database_management
        disable_external_container_database_stack_monitoring
        enable_external_container_database_database_management
        enable_external_container_database_stack_monitoring
        scan_external_container_database_pluggable_databases
    """

    def __init__(self, *args, **kwargs):
        super(ExternalContainerDatabaseActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = oci_config_utils.create_service_client(
            self.module, WorkRequestClient
        )

    @staticmethod
    def get_module_resource_id_param():
        return "external_container_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_container_database_id")

    def get_get_fn(self):
        return self.client.get_external_container_database

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_container_database,
            external_container_database_id=self.module.params.get(
                "external_container_database_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_external_container_database_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_compartment_details=action_details,
                external_container_database_id=self.module.params.get(
                    "external_container_database_id"
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

    def disable_external_container_database_database_management(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_external_container_database_database_management,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_container_database_id=self.module.params.get(
                    "external_container_database_id"
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

    def disable_external_container_database_stack_monitoring(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_external_container_database_stack_monitoring,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_container_database_id=self.module.params.get(
                    "external_container_database_id"
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

    def enable_external_container_database_database_management(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, EnableExternalContainerDatabaseDatabaseManagementDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_external_container_database_database_management,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_container_database_id=self.module.params.get(
                    "external_container_database_id"
                ),
                enable_external_container_database_database_management_details=action_details,
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

    def enable_external_container_database_stack_monitoring(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, EnableExternalContainerDatabaseStackMonitoringDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_external_container_database_stack_monitoring,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_container_database_id=self.module.params.get(
                    "external_container_database_id"
                ),
                enable_external_container_database_stack_monitoring_details=action_details,
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

    def scan_external_container_database_pluggable_databases(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.scan_external_container_database_pluggable_databases,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_container_database_id=self.module.params.get(
                    "external_container_database_id"
                ),
                external_database_connector_id=self.module.params.get(
                    "external_database_connector_id"
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


ExternalContainerDatabaseActionsHelperCustom = get_custom_class(
    "ExternalContainerDatabaseActionsHelperCustom"
)


class ResourceHelper(
    ExternalContainerDatabaseActionsHelperCustom,
    ExternalContainerDatabaseActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            external_container_database_id=dict(
                aliases=["id"], type="str", required=True
            ),
            external_database_connector_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "disable_external_container_database_database_management",
                    "disable_external_container_database_stack_monitoring",
                    "enable_external_container_database_database_management",
                    "enable_external_container_database_stack_monitoring",
                    "scan_external_container_database_pluggable_databases",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="external_container_database",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
