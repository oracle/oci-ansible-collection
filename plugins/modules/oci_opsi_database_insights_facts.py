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
module: oci_opsi_database_insights_facts
short_description: Fetches details about one or multiple DatabaseInsights resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DatabaseInsights resources in Oracle Cloud Infrastructure
    - Lists database insight resources
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    database_type:
        description:
            - Filter by one or more database type.
              Possible values are ADW-S, ATP-S, ADW-D, ATP-D
        type: list
        choices:
            - "ADW-S"
            - "ATP-S"
            - "ADW-D"
            - "ATP-D"
    database_id:
        description:
            - Optional list of database L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
    fields:
        description:
            - Specifies the fields to return in a database summary response. By default all fields are returned if omitted.
        type: list
        choices:
            - "compartmentId"
            - "databaseName"
            - "databaseDisplayName"
            - "databaseType"
            - "databaseVersion"
            - "databaseHostNames"
            - "freeformTags"
            - "definedTags"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Database insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.
        type: str
        choices:
            - "databaseName"
            - "databaseDisplayName"
            - "databaseType"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List database_insights
  oci_opsi_database_insights_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
database_insights:
    description:
        - List of DatabaseInsights resources
    returned: on success
    type: complex
    contains:
        database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database.
            returned: on success
            type: string
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        database_name:
            description:
                - The database name. The database name is unique within the tenancy.
            returned: on success
            type: string
            sample: database_name_example
        database_display_name:
            description:
                - The user-friendly name for the database. The name does not have to be unique.
            returned: on success
            type: string
            sample: database_display_name_example
        database_type:
            description:
                - Operations Insights internal representation of the database type.
            returned: on success
            type: string
            sample: database_type_example
        database_version:
            description:
                - The version of the database.
            returned: on success
            type: string
            sample: database_version_example
        database_host_names:
            description:
                - The hostnames for the database.
            returned: on success
            type: list
            sample: []
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "database_name": "database_name_example",
        "database_display_name": "database_display_name_example",
        "database_type": "database_type_example",
        "database_version": "database_version_example",
        "database_host_names": [],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseInsightsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "database_type",
            "database_id",
            "fields",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_database_insights,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DatabaseInsightsFactsHelperCustom = get_custom_class(
    "DatabaseInsightsFactsHelperCustom"
)


class ResourceFactsHelper(
    DatabaseInsightsFactsHelperCustom, DatabaseInsightsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            database_type=dict(
                type="list", choices=["ADW-S", "ATP-S", "ADW-D", "ATP-D"]
            ),
            database_id=dict(type="list"),
            fields=dict(
                type="list",
                choices=[
                    "compartmentId",
                    "databaseName",
                    "databaseDisplayName",
                    "databaseType",
                    "databaseVersion",
                    "databaseHostNames",
                    "freeformTags",
                    "definedTags",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=["databaseName", "databaseDisplayName", "databaseType"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="database_insights",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(database_insights=result)


if __name__ == "__main__":
    main()
