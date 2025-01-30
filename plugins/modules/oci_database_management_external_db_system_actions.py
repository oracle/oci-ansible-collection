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
module: oci_database_management_external_db_system_actions
short_description: Perform actions on an ExternalDbSystem resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an ExternalDbSystem resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the external DB system and its related resources (excluding databases) to the specified compartment.
    - For I(action=disable_external_db_system_database_management), disables Database Management service for all the components of the specified
      external DB system (except databases).
    - For I(action=enable_external_db_system_database_management), enables Database Management service for all the components of the specified
      external DB system (except databases).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
              compartment to move the external DB system to.
            - Required for I(action=change_compartment).
        type: str
    external_db_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system.
        type: str
        aliases: ["id"]
        required: true
    license_model:
        description:
            - The Oracle license model that applies to the external database.
            - Required for I(action=enable_external_db_system_database_management).
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    action:
        description:
            - The action to perform on the ExternalDbSystem.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "disable_external_db_system_database_management"
            - "enable_external_db_system_database_management"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on external_db_system
  oci_database_management_external_db_system_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    external_db_system_id: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action disable_external_db_system_database_management on external_db_system
  oci_database_management_external_db_system_actions:
    # required
    external_db_system_id: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    action: disable_external_db_system_database_management

- name: Perform action enable_external_db_system_database_management on external_db_system
  oci_database_management_external_db_system_actions:
    # required
    external_db_system_id: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    license_model: LICENSE_INCLUDED
    action: enable_external_db_system_database_management

"""

RETURN = """
external_db_system:
    description:
        - Details of the ExternalDbSystem resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the DB system. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        db_system_discovery_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system discovery.
            returned: on success
            type: str
            sample: "ocid1.dbsystemdiscovery.oc1..xxxxxxEXAMPLExxxxxx"
        discovery_agent_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the management agent used during the discovery of the DB
                  system.
            returned: on success
            type: str
            sample: "ocid1.discoveryagent.oc1..xxxxxxEXAMPLExxxxxx"
        is_cluster:
            description:
                - Indicates whether the DB system is a cluster DB system or not.
            returned: on success
            type: bool
            sample: true
        home_directory:
            description:
                - The Oracle Grid home directory in case of cluster-based DB system and
                  Oracle home directory in case of single instance-based DB system.
            returned: on success
            type: str
            sample: home_directory_example
        database_management_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                license_model:
                    description:
                        - The Oracle license model that applies to the external database.
                    returned: on success
                    type: str
                    sample: LICENSE_INCLUDED
        lifecycle_state:
            description:
                - The current lifecycle state of the external DB system resource.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the external DB system was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the external DB system was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "db_system_discovery_id": "ocid1.dbsystemdiscovery.oc1..xxxxxxEXAMPLExxxxxx",
        "discovery_agent_id": "ocid1.discoveryagent.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cluster": true,
        "home_directory": "home_directory_example",
        "database_management_config": {
            "license_model": "LICENSE_INCLUDED"
        },
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient
    from oci.database_management.models import ChangeExternalDbSystemCompartmentDetails
    from oci.database_management.models import (
        EnableExternalDbSystemDatabaseManagementDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalDbSystemActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        disable_external_db_system_database_management
        enable_external_db_system_database_management
    """

    @staticmethod
    def get_module_resource_id_param():
        return "external_db_system_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_db_system_id")

    def get_get_fn(self):
        return self.client.get_external_db_system

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_db_system,
            external_db_system_id=self.module.params.get("external_db_system_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeExternalDbSystemCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_external_db_system_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_db_system_id=self.module.params.get("external_db_system_id"),
                change_external_db_system_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def disable_external_db_system_database_management(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_external_db_system_database_management,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_db_system_id=self.module.params.get("external_db_system_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def enable_external_db_system_database_management(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, EnableExternalDbSystemDatabaseManagementDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_external_db_system_database_management,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_db_system_id=self.module.params.get("external_db_system_id"),
                enable_external_db_system_database_management_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ExternalDbSystemActionsHelperCustom = get_custom_class(
    "ExternalDbSystemActionsHelperCustom"
)


class ResourceHelper(
    ExternalDbSystemActionsHelperCustom, ExternalDbSystemActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            external_db_system_id=dict(aliases=["id"], type="str", required=True),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "disable_external_db_system_database_management",
                    "enable_external_db_system_database_management",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="external_db_system",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
