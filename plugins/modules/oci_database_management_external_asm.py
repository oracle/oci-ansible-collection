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
module: oci_database_management_external_asm
short_description: Manage an ExternalAsm resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an ExternalAsm resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_asm_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external ASM.
        type: str
        aliases: ["id"]
        required: true
    external_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external connector.
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the ExternalAsm.
            - Use I(state=present) to update an existing an ExternalAsm.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update external_asm
  oci_database_management_external_asm:
    # required
    external_asm_id: "ocid1.externalasm.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    external_connector_id: "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
external_asm:
    description:
        - Details of the ExternalAsm resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external ASM.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the external ASM. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        component_name:
            description:
                - The name of the external ASM.
            returned: on success
            type: str
            sample: component_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        external_db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system that the ASM is a part of.
            returned: on success
            type: str
            sample: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        external_connector_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external connector.
            returned: on success
            type: str
            sample: "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx"
        grid_home:
            description:
                - The directory in which ASM is installed. This is the same directory in which Oracle Grid Infrastructure is installed.
            returned: on success
            type: str
            sample: grid_home_example
        is_cluster:
            description:
                - Indicates whether the ASM is a cluster ASM or not.
            returned: on success
            type: bool
            sample: true
        is_flex_enabled:
            description:
                - Indicates whether Oracle Flex ASM is enabled or not.
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The current lifecycle state of the external ASM.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        serviced_databases:
            description:
                - The list of databases that are serviced by the ASM.
            returned: on success
            type: complex
            contains:
                disk_groups:
                    description:
                        - The list of ASM disk groups used by the database.
                    returned: on success
                    type: list
                    sample: []
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external database.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - The user-friendly name for the database. The name does not have to be unique.
                    returned: on success
                    type: str
                    sample: display_name_example
                db_unique_name:
                    description:
                        - The unique name of the external database.
                    returned: on success
                    type: str
                    sample: db_unique_name_example
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the external database
                          resides.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                database_type:
                    description:
                        - The type of Oracle Database installation.
                    returned: on success
                    type: str
                    sample: EXTERNAL_SIDB
                database_sub_type:
                    description:
                        - The subtype of Oracle Database. Indicates whether the database is a Container Database,
                          Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.
                    returned: on success
                    type: str
                    sample: CDB
                is_managed:
                    description:
                        - Indicates whether the database is a Managed Database or not.
                    returned: on success
                    type: bool
                    sample: true
        additional_details:
            description:
                - "The additional details of the external ASM defined in `{\\"key\\": \\"value\\"}` format.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - The date and time the external ASM was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the external ASM was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        version:
            description:
                - The ASM version.
            returned: on success
            type: str
            sample: version_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "component_name": "component_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_system_id": "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "external_connector_id": "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx",
        "grid_home": "grid_home_example",
        "is_cluster": true,
        "is_flex_enabled": true,
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "serviced_databases": [{
            "disk_groups": [],
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "db_unique_name": "db_unique_name_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "database_type": "EXTERNAL_SIDB",
            "database_sub_type": "CDB",
            "is_managed": true
        }],
        "additional_details": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "version": "version_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient
    from oci.database_management.models import UpdateExternalAsmDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalAsmHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_possible_entity_types(self):
        return super(ExternalAsmHelperGen, self).get_possible_entity_types() + [
            "externalasm",
            "externalasms",
            "databaseManagementexternalasm",
            "databaseManagementexternalasms",
            "externalasmresource",
            "externalasmsresource",
            "databasemanagement",
        ]

    def get_module_resource_id_param(self):
        return "external_asm_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_asm_id")

    def get_get_fn(self):
        return self.client.get_external_asm

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_asm, external_asm_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_asm,
            external_asm_id=self.module.params.get("external_asm_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_external_asms, **kwargs
        )

    def get_update_model_class(self):
        return UpdateExternalAsmDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_external_asm,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_asm_id=self.module.params.get("external_asm_id"),
                update_external_asm_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ExternalAsmHelperCustom = get_custom_class("ExternalAsmHelperCustom")


class ResourceHelper(ExternalAsmHelperCustom, ExternalAsmHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            external_asm_id=dict(aliases=["id"], type="str", required=True),
            external_connector_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="external_asm",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
