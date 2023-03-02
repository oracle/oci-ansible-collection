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
module: oci_database_management_external_database_facts
short_description: Fetches details about one or multiple ExternalDatabase resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExternalDatabase resources in Oracle Cloud Infrastructure
    - Lists the external databases in the specified compartment or in the specified DB system.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
    external_db_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system.
        type: str
    display_name:
        description:
            - A filter to only return the resources that match the entire display name.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort information by. Only one sortOrder can be used. The default sort order
              for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending.
              The `DISPLAYNAME` sort order is case-sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The option to sort information in ascending (???ASC???) or descending (???DESC???) order. Ascending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List external_databases
  oci_database_management_external_database_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    external_db_system_id: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
external_databases:
    description:
        - List of ExternalDatabase resources
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
                - The user-friendly name for the database. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        db_unique_name:
            description:
                - The `DB_UNIQUE_NAME` of the external database.
            returned: on success
            type: str
            sample: db_unique_name_example
        database_type:
            description:
                - The type of Oracle Database installation.
            returned: on success
            type: str
            sample: EXTERNAL_SIDB
        database_sub_type:
            description:
                - The subtype of Oracle Database. Indicates whether the database is a Container Database,
                  Pluggable Database, or Non-container Database.
            returned: on success
            type: str
            sample: CDB
        external_container_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the parent Container Database (CDB)
                  if this is a Pluggable Database (PDB).
            returned: on success
            type: str
            sample: "ocid1.externalcontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
        external_db_home_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB home.
            returned: on success
            type: str
            sample: "ocid1.externaldbhome.oc1..xxxxxxEXAMPLExxxxxx"
        db_system_info:
            description:
                - ""
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
        db_management_config:
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
                connector_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external database connector.
                    returned: on success
                    type: str
                    sample: "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx"
                license_model:
                    description:
                        - The Oracle license model that applies to the external database.
                    returned: on success
                    type: str
                    sample: LICENSE_INCLUDED
        instance_details:
            description:
                - The list of database instances if the database is a RAC database.
            returned: on success
            type: complex
            contains:
                instance_number:
                    description:
                        - The instance number of the database instance.
                    returned: on success
                    type: int
                    sample: 56
                instance_name:
                    description:
                        - The name of the database instance.
                    returned: on success
                    type: str
                    sample: instance_name_example
                host_name:
                    description:
                        - The name of the host machine.
                    returned: on success
                    type: str
                    sample: host_name_example
        lifecycle_state:
            description:
                - The current lifecycle state of the external database resource.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time the external DB system was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "db_unique_name": "db_unique_name_example",
        "database_type": "EXTERNAL_SIDB",
        "database_sub_type": "CDB",
        "external_container_database_id": "ocid1.externalcontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_home_id": "ocid1.externaldbhome.oc1..xxxxxxEXAMPLExxxxxx",
        "db_system_info": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "db_management_config": {
            "database_management_status": "ENABLING",
            "connector_id": "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx",
            "license_model": "LICENSE_INCLUDED"
        },
        "instance_details": [{
            "instance_number": 56,
            "instance_name": "instance_name_example",
            "host_name": "host_name_example"
        }],
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalDatabaseFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "external_db_system_id",
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_external_databases, **optional_kwargs
        )


ExternalDatabaseFactsHelperCustom = get_custom_class(
    "ExternalDatabaseFactsHelperCustom"
)


class ResourceFactsHelper(
    ExternalDatabaseFactsHelperCustom, ExternalDatabaseFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            external_db_system_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="external_database",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(external_databases=result)


if __name__ == "__main__":
    main()
