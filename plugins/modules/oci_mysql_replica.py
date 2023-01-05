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
module: oci_mysql_replica
short_description: Manage a Replica resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Replica resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a DB System read replica.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_system_id:
        description:
            - The OCID of the DB System the read replica is associated with.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - The user-friendly name for the read replica. It does not have to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - User provided description of the read replica.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    is_delete_protected:
        description:
            - Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow.
              Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If
              the DB System is delete protected, read replicas can still be deleted individually if they are not delete
              protected themselves.
            - This parameter is updatable.
        type: bool
    replica_id:
        description:
            - The Replica L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the Replica.
            - Use I(state=present) to create or update a Replica.
            - Use I(state=absent) to delete a Replica.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create replica
  oci_mysql_replica:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_delete_protected: true

- name: Update replica
  oci_mysql_replica:
    # required
    replica_id: "ocid1.replica.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_delete_protected: true

- name: Update replica using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_mysql_replica:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_delete_protected: true

- name: Delete replica
  oci_mysql_replica:
    # required
    replica_id: "ocid1.replica.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete replica using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_mysql_replica:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
replica:
    description:
        - Details of the Replica resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the read replica.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        db_system_id:
            description:
                - The OCID of the DB System the read replica is associated with.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that contains the read replica.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the read replica. It does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - User provided description of the read replica.
            returned: on success
            type: str
            sample: description_example
        lifecycle_state:
            description:
                - The state of the read replica.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the state of the read replica.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the read replica was created, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the read replica was last updated, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        mysql_version:
            description:
                - The MySQL version used by the read replica.
            returned: on success
            type: str
            sample: mysql_version_example
        availability_domain:
            description:
                - The name of the Availability Domain the read replica is located in.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        fault_domain:
            description:
                - The name of the Fault Domain the read replica is located in.
            returned: on success
            type: str
            sample: FAULT-DOMAIN-1
        ip_address:
            description:
                - The IP address the read replica is configured to listen on.
            returned: on success
            type: str
            sample: ip_address_example
        port:
            description:
                - The port the read replica is configured to listen on.
            returned: on success
            type: int
            sample: 56
        port_x:
            description:
                - The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.
            returned: on success
            type: int
            sample: 56
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
        is_delete_protected:
            description:
                - Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow.
                  Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If
                  the DB System is delete protected, read replicas can still be deleted individually if they are not delete
                  protected themselves.
            returned: on success
            type: bool
            sample: true
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "mysql_version": "mysql_version_example",
        "availability_domain": "Uocm:PHX-AD-1",
        "fault_domain": "FAULT-DOMAIN-1",
        "ip_address": "ip_address_example",
        "port": 56,
        "port_x": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "is_delete_protected": true
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.mysql import WorkRequestsClient
    from oci.mysql import ReplicasClient
    from oci.mysql.models import CreateReplicaDetails
    from oci.mysql.models import UpdateReplicaDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlReplicaHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestsClient)

    def get_possible_entity_types(self):
        return super(MysqlReplicaHelperGen, self).get_possible_entity_types() + [
            "replica",
            "replicas",
            "mysqlreplica",
            "mysqlreplicas",
            "replicaresource",
            "replicasresource",
            "mysql",
        ]

    def get_module_resource_id_param(self):
        return "replica_id"

    def get_module_resource_id(self):
        return self.module.params.get("replica_id")

    def get_get_fn(self):
        return self.client.get_replica

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_replica, replica_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_replica, replica_id=self.module.params.get("replica_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name", "db_system_id", "replica_id"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_replicas, **kwargs)

    def get_create_model_class(self):
        return CreateReplicaDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_replica,
            call_fn_args=(),
            call_fn_kwargs=dict(create_replica_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateReplicaDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_replica,
            call_fn_args=(),
            call_fn_kwargs=dict(
                replica_id=self.module.params.get("replica_id"),
                update_replica_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_replica,
            call_fn_args=(),
            call_fn_kwargs=dict(replica_id=self.module.params.get("replica_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MysqlReplicaHelperCustom = get_custom_class("MysqlReplicaHelperCustom")


class ResourceHelper(MysqlReplicaHelperCustom, MysqlReplicaHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            db_system_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            is_delete_protected=dict(type="bool"),
            replica_id=dict(aliases=["id"], type="str"),
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
        service_client_class=ReplicasClient,
        namespace="mysql",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
