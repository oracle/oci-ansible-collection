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
module: oci_psql_db_system_db_instance
short_description: Manage a DbSystemDbInstance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a DbSystemDbInstance resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_system_id:
        description:
            - A unique identifier for the database system.
        type: str
        required: true
    db_instance_id:
        description:
            - A unique identifier for the database instance node.
        type: str
        aliases: ["id"]
        required: true
    display_name:
        description:
            - A user-friendly display name of the database instance node. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
        aliases: ["name"]
    description:
        description:
            - A user-provided description of the database instance node.
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the DbSystemDbInstance.
            - Use I(state=present) to update an existing a DbSystemDbInstance.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update db_system_db_instance
  oci_psql_db_system_db_instance:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    db_instance_id: "ocid1.dbinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example

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
    from oci.psql import PostgresqlClient
    from oci.psql.models import UpdateDbSystemDbInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PsqlDbSystemDbInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: update"""

    def get_possible_entity_types(self):
        return super(
            PsqlDbSystemDbInstanceHelperGen, self
        ).get_possible_entity_types() + [
            "dbsystemdbinstance",
            "dbsystemdbinstances",
            "psqldbsystemdbinstance",
            "psqldbsystemdbinstances",
            "dbsystemdbinstanceresource",
            "dbsystemdbinstancesresource",
            "dbinstance",
            "dbinstances",
            "psqldbinstance",
            "psqldbinstances",
            "dbinstanceresource",
            "dbinstancesresource",
            "psql",
        ]

    def get_module_resource_id_param(self):
        return "db_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("db_instance_id")

    def get_update_model_class(self):
        return UpdateDbSystemDbInstanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_db_system_db_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_system_id=self.module.params.get("db_system_id"),
                db_instance_id=self.module.params.get("db_instance_id"),
                update_db_system_db_instance_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


PsqlDbSystemDbInstanceHelperCustom = get_custom_class(
    "PsqlDbSystemDbInstanceHelperCustom"
)


class ResourceHelper(
    PsqlDbSystemDbInstanceHelperCustom, PsqlDbSystemDbInstanceHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            db_system_id=dict(type="str", required=True),
            db_instance_id=dict(aliases=["id"], type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="db_system_db_instance",
        service_client_class=PostgresqlClient,
        namespace="psql",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
