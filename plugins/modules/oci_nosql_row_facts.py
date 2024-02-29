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
module: oci_nosql_row_facts
short_description: Fetches details about a Row resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Row resource in Oracle Cloud Infrastructure
    - Get a single row from the table by primary key.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    table_name_or_id:
        description:
            - A table name within the compartment, or a table OCID.
        type: str
        aliases: ["id"]
        required: true
    key:
        description:
            - "An array of strings, each of the format \\"column-name:value\\",
              representing the primary key of the row."
        type: list
        elements: str
        required: true
    compartment_id:
        description:
            - The ID of a table's compartment. When a table is identified
              by name, the compartmentId is often needed to provide
              context for interpreting the name.
        type: str
    consistency:
        description:
            - Consistency requirement for a read operation.
        type: str
        choices:
            - "EVENTUAL"
            - "ABSOLUTE"
    timeout_in_ms:
        description:
            - Timeout setting for this operation.
        type: int
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific row
  oci_nosql_row_facts:
    # required
    table_name_or_id: "ocid1.tablenameor.oc1..xxxxxxEXAMPLExxxxxx"
    key: [ "key_example" ]

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    consistency: EVENTUAL
    timeout_in_ms: 56

"""

RETURN = """
row:
    description:
        - Row resource
    returned: on success
    type: complex
    contains:
        value:
            description:
                - The map of values from a row.
            returned: on success
            type: dict
            sample: {}
        time_of_expiration:
            description:
                - The expiration time of the row. A zero value indicates that
                  the row does not expire. An RFC3339 formatted datetime
                  string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        usage:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                read_units_consumed:
                    description:
                        - Read Units consumed by this operation.
                    returned: on success
                    type: int
                    sample: 56
                write_units_consumed:
                    description:
                        - Write Units consumed by this operation.
                    returned: on success
                    type: int
                    sample: 56
    sample: {
        "value": {},
        "time_of_expiration": "2013-10-20T19:20:30+01:00",
        "usage": {
            "read_units_consumed": 56,
            "write_units_consumed": 56
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.nosql import NosqlClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RowFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "table_name_or_id",
            "key",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "compartment_id",
            "consistency",
            "timeout_in_ms",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_row,
            table_name_or_id=self.module.params.get("table_name_or_id"),
            key=self.module.params.get("key"),
            **optional_kwargs
        )


RowFactsHelperCustom = get_custom_class("RowFactsHelperCustom")


class ResourceFactsHelper(RowFactsHelperCustom, RowFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            table_name_or_id=dict(aliases=["id"], type="str", required=True),
            key=dict(type="list", elements="str", required=True, no_log=True),
            compartment_id=dict(type="str"),
            consistency=dict(type="str", choices=["EVENTUAL", "ABSOLUTE"]),
            timeout_in_ms=dict(type="int"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="row",
        service_client_class=NosqlClient,
        namespace="nosql",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(row=result)


if __name__ == "__main__":
    main()
