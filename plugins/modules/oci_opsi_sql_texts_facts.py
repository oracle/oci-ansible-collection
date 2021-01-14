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
module: oci_opsi_sql_texts_facts
short_description: Fetches details about one or multiple SqlTexts resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SqlTexts resources in Oracle Cloud Infrastructure
    - Query SQL Warehouse to get the full SQL Text for a SQL.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    sql_identifier:
        description:
            - "One or more unique SQL_IDs for a SQL Statement.
              Example: `6rgjh9bjmy2s7`"
        type: list
        required: true
    database_id:
        description:
            - Optional list of database L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List sql_texts
  oci_opsi_sql_texts_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    sql_identifier: [ "6rgjh9bjmy2s7" ]

"""

RETURN = """
sql_texts:
    description:
        - List of SqlTexts resources
    returned: on success
    type: complex
    contains:
        sql_identifier:
            description:
                - Unique SQL_ID for a SQL Statement.
            returned: on success
            type: string
            sample: sql_identifier_example
        database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database.
            returned: on success
            type: string
            sample: ocid1.database.oc1..xxxxxxEXAMPLExxxxxx
        sql_text:
            description:
                - SQL Text
            returned: on success
            type: string
            sample: sql_text_example
    sample: [{
        "sql_identifier": "sql_identifier_example",
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "sql_text": "sql_text_example"
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


class SqlTextsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "sql_identifier",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "database_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_sql_texts,
            compartment_id=self.module.params.get("compartment_id"),
            sql_identifier=self.module.params.get("sql_identifier"),
            **optional_kwargs
        )


SqlTextsFactsHelperCustom = get_custom_class("SqlTextsFactsHelperCustom")


class ResourceFactsHelper(SqlTextsFactsHelperCustom, SqlTextsFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            sql_identifier=dict(type="list", required=True),
            database_id=dict(type="list"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sql_texts",
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

    module.exit_json(sql_texts=result)


if __name__ == "__main__":
    main()
