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
module: oci_psql_connection_facts
short_description: Fetches details about a Connection resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Connection resource in Oracle Cloud Infrastructure
    - Gets the database system connection details.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_system_id:
        description:
            - A unique identifier for the database system.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific connection
  oci_psql_connection_facts:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
connection:
    description:
        - Connection resource
    returned: on success
    type: complex
    contains:
        ca_certificate:
            description:
                - The CA certificate to be used by the PosgreSQL client to connect to the database.
                  The CA certificate is used to authenticate the server identity.
                  It is issued by PostgreSQL Service Private CA.
            returned: on success
            type: str
            sample: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
        primary_db_endpoint:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                fqdn:
                    description:
                        - The FQDN of the endpoint.
                    returned: on success
                    type: str
                    sample: fqdn_example
                ip_address:
                    description:
                        - The IP address of the endpoint.
                    returned: on success
                    type: str
                    sample: ip_address_example
                port:
                    description:
                        - The port address of the endpoint.
                    returned: on success
                    type: int
                    sample: 56
        instance_endpoints:
            description:
                - The list of database instance node endpoints in the database system.
            returned: on success
            type: complex
            contains:
                db_instance_id:
                    description:
                        - Unique identifier of the database instance node.
                    returned: on success
                    type: str
                    sample: "ocid1.dbinstance.oc1..xxxxxxEXAMPLExxxxxx"
                endpoint:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        fqdn:
                            description:
                                - The FQDN of the endpoint.
                            returned: on success
                            type: str
                            sample: fqdn_example
                        ip_address:
                            description:
                                - The IP address of the endpoint.
                            returned: on success
                            type: str
                            sample: ip_address_example
                        port:
                            description:
                                - The port address of the endpoint.
                            returned: on success
                            type: int
                            sample: 56
    sample: {
        "ca_certificate": "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----",
        "primary_db_endpoint": {
            "fqdn": "fqdn_example",
            "ip_address": "ip_address_example",
            "port": 56
        },
        "instance_endpoints": [{
            "db_instance_id": "ocid1.dbinstance.oc1..xxxxxxEXAMPLExxxxxx",
            "endpoint": {
                "fqdn": "fqdn_example",
                "ip_address": "ip_address_example",
                "port": 56
            }
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.psql import PostgresqlClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PsqlConnectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "db_system_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection_details,
            db_system_id=self.module.params.get("db_system_id"),
        )


PsqlConnectionFactsHelperCustom = get_custom_class("PsqlConnectionFactsHelperCustom")


class ResourceFactsHelper(
    PsqlConnectionFactsHelperCustom, PsqlConnectionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(db_system_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="connection",
        service_client_class=PostgresqlClient,
        namespace="psql",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(connection=result)


if __name__ == "__main__":
    main()
