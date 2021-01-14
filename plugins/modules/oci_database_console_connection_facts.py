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
module: oci_database_console_connection_facts
short_description: Fetches details about one or multiple ConsoleConnection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ConsoleConnection resources in Oracle Cloud Infrastructure
    - Lists the console connections for the specified database node.
    - If I(console_connection_id) is specified, the details of a single ConsoleConnection will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    db_node_id:
        description:
            - The database node L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    console_connection_id:
        description:
            - The OCID of the console connection.
            - Required to get a specific console_connection.
        type: str
        aliases: ["id"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List console_connections
  oci_database_console_connection_facts:
    db_node_id: ocid1.dbnode.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific console_connection
  oci_database_console_connection_facts:
    db_node_id: ocid1.dbnode.oc1..xxxxxxEXAMPLExxxxxx
    console_connection_id: ocid1.consoleconnection.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
console_connections:
    description:
        - List of ConsoleConnection resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the console connection.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment to contain the console connection.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        db_node_id:
            description:
                - The OCID of the database node.
            returned: on success
            type: string
            sample: ocid1.dbnode.oc1..xxxxxxEXAMPLExxxxxx
        connection_string:
            description:
                - The SSH connection string for the console connection.
            returned: on success
            type: string
            sample: connection_string_example
        fingerprint:
            description:
                - The SSH public key fingerprint for the console connection.
            returned: on success
            type: string
            sample: fingerprint_example
        lifecycle_state:
            description:
                - The current state of the console connection.
            returned: on success
            type: string
            sample: ACTIVE
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "db_node_id": "ocid1.dbnode.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_string": "connection_string_example",
        "fingerprint": "fingerprint_example",
        "lifecycle_state": "ACTIVE"
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


class ConsoleConnectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "db_node_id",
            "console_connection_id",
        ]

    def get_required_params_for_list(self):
        return [
            "db_node_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_console_connection,
            db_node_id=self.module.params.get("db_node_id"),
            console_connection_id=self.module.params.get("console_connection_id"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_console_connections,
            db_node_id=self.module.params.get("db_node_id"),
            **optional_kwargs
        )


ConsoleConnectionFactsHelperCustom = get_custom_class(
    "ConsoleConnectionFactsHelperCustom"
)


class ResourceFactsHelper(
    ConsoleConnectionFactsHelperCustom, ConsoleConnectionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            db_node_id=dict(type="str", required=True),
            console_connection_id=dict(aliases=["id"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="console_connection",
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

    module.exit_json(console_connections=result)


if __name__ == "__main__":
    main()
