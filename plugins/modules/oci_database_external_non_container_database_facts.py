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
module: oci_database_external_non_container_database_facts
short_description: Fetches details about one or multiple ExternalNonContainerDatabase resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExternalNonContainerDatabase resources in Oracle Cloud Infrastructure
    - Gets a list of the ExternalNonContainerDatabases in the specified compartment.
    - If I(external_non_container_database_id) is specified, the details of a single ExternalNonContainerDatabase will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    external_non_container_database_id:
        description:
            - The external non-container database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific external_non_container_database.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple external_non_container_databases.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`).
              Default order for TIMECREATED is descending.
              Default order for DISPLAYNAME is ascending.
              The DISPLAYNAME sort order is case sensitive.
        type: str
        choices:
            - "DISPLAYNAME"
            - "TIMECREATED"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to return only resources that match the specified lifecycle state.
        type: str
        choices:
            - "PROVISIONING"
            - "NOT_CONNECTED"
            - "AVAILABLE"
            - "UPDATING"
            - "TERMINATING"
            - "TERMINATED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List external_non_container_databases
  oci_database_external_non_container_database_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific external_non_container_database
  oci_database_external_non_container_database_facts:
    external_non_container_database_id: "ocid1.externalnoncontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
external_non_container_databases:
    description:
        - List of ExternalNonContainerDatabase resources
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
    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalNonContainerDatabaseFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "external_non_container_database_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_non_container_database,
            external_non_container_database_id=self.module.params.get(
                "external_non_container_database_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_external_non_container_databases,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ExternalNonContainerDatabaseFactsHelperCustom = get_custom_class(
    "ExternalNonContainerDatabaseFactsHelperCustom"
)


class ResourceFactsHelper(
    ExternalNonContainerDatabaseFactsHelperCustom,
    ExternalNonContainerDatabaseFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_non_container_database_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["DISPLAYNAME", "TIMECREATED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "NOT_CONNECTED",
                    "AVAILABLE",
                    "UPDATING",
                    "TERMINATING",
                    "TERMINATED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="external_non_container_database",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(external_non_container_databases=result)


if __name__ == "__main__":
    main()
