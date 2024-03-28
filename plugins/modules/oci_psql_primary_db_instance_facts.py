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
module: oci_psql_primary_db_instance_facts
short_description: Fetches details about a PrimaryDbInstance resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a PrimaryDbInstance resource in Oracle Cloud Infrastructure
    - Gets the primary database instance node details.
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
- name: Get a specific primary_db_instance
  oci_psql_primary_db_instance_facts:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
primary_db_instance:
    description:
        - PrimaryDbInstance resource
    returned: on success
    type: complex
    contains:
        db_instance_id:
            description:
                - A unique identifier for the primary database instance node.
            returned: on success
            type: str
            sample: "ocid1.dbinstance.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "db_instance_id": "ocid1.dbinstance.oc1..xxxxxxEXAMPLExxxxxx"
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


class PsqlPrimaryDbInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "db_system_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_primary_db_instance,
            db_system_id=self.module.params.get("db_system_id"),
        )


PsqlPrimaryDbInstanceFactsHelperCustom = get_custom_class(
    "PsqlPrimaryDbInstanceFactsHelperCustom"
)


class ResourceFactsHelper(
    PsqlPrimaryDbInstanceFactsHelperCustom, PsqlPrimaryDbInstanceFactsHelperGen
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
        resource_type="primary_db_instance",
        service_client_class=PostgresqlClient,
        namespace="psql",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(primary_db_instance=result)


if __name__ == "__main__":
    main()
