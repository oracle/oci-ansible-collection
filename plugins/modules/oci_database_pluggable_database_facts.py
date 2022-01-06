#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_database_pluggable_database_facts
short_description: Fetches details about one or multiple PluggableDatabase resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PluggableDatabase resources in Oracle Cloud Infrastructure
    - Gets a list of the pluggable databases in a database or compartment. You must provide either a `databaseId` or `compartmentId` value.
    - If I(pluggable_database_id) is specified, the details of a single PluggableDatabase will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    pluggable_database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific pluggable_database.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
    database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database.
        type: str
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for PDBNAME is
              ascending. The PDBNAME sort order is case sensitive.
        type: str
        choices:
            - "PDBNAME"
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
            - A filter to return only resources that match the given lifecycle state exactly.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "TERMINATING"
            - "TERMINATED"
            - "UPDATING"
            - "FAILED"
    pdb_name:
        description:
            - A filter to return only pluggable databases that match the entire name given. The match is not case sensitive.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific pluggable_database
  oci_database_pluggable_database_facts:
    # required
    pluggable_database_id: "ocid1.pluggabledatabase.oc1..xxxxxxEXAMPLExxxxxx"

- name: List pluggable_databases
  oci_database_pluggable_database_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    sort_by: PDBNAME
    sort_order: ASC
    lifecycle_state: PROVISIONING
    pdb_name: pdb_name_example

"""

RETURN = """
pluggable_databases:
    description:
        - List of PluggableDatabase resources
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
                - The mode that pluggable database is in. Open mode can only be changed to READ_ONLY or MIGRATE directly from the backend (within the Oracle
                  Database software).
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
    sample: [{
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
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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


class PluggableDatabaseFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "pluggable_database_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_pluggable_database,
            pluggable_database_id=self.module.params.get("pluggable_database_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "database_id",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "pdb_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_pluggable_databases, **optional_kwargs
        )


PluggableDatabaseFactsHelperCustom = get_custom_class(
    "PluggableDatabaseFactsHelperCustom"
)


class ResourceFactsHelper(
    PluggableDatabaseFactsHelperCustom, PluggableDatabaseFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            pluggable_database_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            database_id=dict(type="str"),
            sort_by=dict(type="str", choices=["PDBNAME", "TIMECREATED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "AVAILABLE",
                    "TERMINATING",
                    "TERMINATED",
                    "UPDATING",
                    "FAILED",
                ],
            ),
            pdb_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="pluggable_database",
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

    module.exit_json(pluggable_databases=result)


if __name__ == "__main__":
    main()
