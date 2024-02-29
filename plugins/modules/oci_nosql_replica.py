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
module: oci_nosql_replica
short_description: Manage a Replica resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a Replica resource in Oracle Cloud Infrastructure
    - For I(state=present), add a replica for this table
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    max_read_units:
        description:
            - Maximum sustained read throughput limit for the new replica table.
              If not specified, the local table's read limit is used.
        type: int
    max_write_units:
        description:
            - Maximum sustained write throughput limit for the new replica table.
              If not specified, the local table's write limit is used.
        type: int
    table_name_or_id:
        description:
            - A table name within the compartment, or a table OCID.
        type: str
        required: true
    region:
        description:
            - Name of the remote region in standard OCI format, i.e. us-ashburn-1
        type: str
        required: true
    compartment_id:
        description:
            - The OCID of the table's compartment.  Required
              if the tableNameOrId path parameter is a table name.
              Optional if tableNameOrId is an OCID.  If tableNameOrId
              is an OCID, and compartmentId is supplied, the latter
              must match the identified table's compartmentId.
        type: str
    state:
        description:
            - The state of the Replica.
            - Use I(state=present) to create a Replica.
            - Use I(state=absent) to delete a Replica.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create replica
  oci_nosql_replica:
    # required
    table_name_or_id: "ocid1.tablenameor.oc1..xxxxxxEXAMPLExxxxxx"
    region: us-phoenix-1

    # optional
    max_read_units: 56
    max_write_units: 56
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete replica
  oci_nosql_replica:
    # required
    table_name_or_id: "ocid1.tablenameor.oc1..xxxxxxEXAMPLExxxxxx"
    region: us-phoenix-1
    state: absent

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

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
    from oci.nosql import NosqlClient
    from oci.nosql.models import CreateReplicaDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ReplicaHelperGen(OCIResourceHelperBase):
    """Supported operations: create and delete"""

    def get_possible_entity_types(self):
        return super(ReplicaHelperGen, self).get_possible_entity_types() + [
            "replica",
            "replicas",
            "nosqlreplica",
            "nosqlreplicas",
            "replicaresource",
            "replicasresource",
            "nosql",
        ]

    def get_module_resource_id_param(self):
        return "region"

    def get_module_resource_id(self):
        return self.module.params.get("region")

    def get_create_model_class(self):
        return CreateReplicaDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_replica,
            call_fn_args=(),
            call_fn_kwargs=dict(
                table_name_or_id=self.module.params.get("table_name_or_id"),
                create_replica_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_replica,
            call_fn_args=(),
            call_fn_kwargs=dict(
                table_name_or_id=self.module.params.get("table_name_or_id"),
                region=self.module.params.get("region"),
                compartment_id=self.module.params.get("compartment_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ReplicaHelperCustom = get_custom_class("ReplicaHelperCustom")


class ResourceHelper(ReplicaHelperCustom, ReplicaHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            max_read_units=dict(type="int"),
            max_write_units=dict(type="int"),
            table_name_or_id=dict(type="str", required=True),
            region=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="replica",
        service_client_class=NosqlClient,
        namespace="nosql",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
