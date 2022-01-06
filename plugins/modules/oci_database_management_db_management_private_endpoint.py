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
module: oci_database_management_db_management_private_endpoint
short_description: Manage a DbManagementPrivateEndpoint resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DbManagementPrivateEndpoint resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Database Management private endpoint.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_management_db_management_private_endpoint_actions) module:
      change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - The display name of the Database Management private endpoint.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    is_cluster:
        description:
            - Specifies whether the Database Management private endpoint will be used for Oracle Databases in a cluster.
        type: bool
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet.
            - Required for create using I(state=present).
        type: str
    description:
        description:
            - The description of the private endpoint.
            - This parameter is updatable.
        type: str
    nsg_ids:
        description:
            - The OCIDs of the Network Security Groups to which the Database Management private endpoint belongs.
            - This parameter is updatable.
        type: list
        elements: str
    db_management_private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Management private endpoint.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DbManagementPrivateEndpoint.
            - Use I(state=present) to create or update a DbManagementPrivateEndpoint.
            - Use I(state=absent) to delete a DbManagementPrivateEndpoint.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create db_management_private_endpoint
  oci_database_management_db_management_private_endpoint:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_cluster: true
    description: description_example
    nsg_ids: [ "nsg_ids_example" ]

- name: Update db_management_private_endpoint
  oci_database_management_db_management_private_endpoint:
    # required
    db_management_private_endpoint_id: "ocid1.dbmanagementprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    description: description_example
    nsg_ids: [ "nsg_ids_example" ]

- name: Update db_management_private_endpoint using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_management_db_management_private_endpoint:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    nsg_ids: [ "nsg_ids_example" ]

- name: Delete db_management_private_endpoint
  oci_database_management_db_management_private_endpoint:
    # required
    db_management_private_endpoint_id: "ocid1.dbmanagementprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete db_management_private_endpoint using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_management_db_management_private_endpoint:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
db_management_private_endpoint:
    description:
        - Details of the DbManagementPrivateEndpoint resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Management private endpoint.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The display name of the Database Management private endpoint.
            returned: on success
            type: str
            sample: name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        is_cluster:
            description:
                - Specifies whether the Database Management private endpoint can be used for Oracle Databases in a cluster.
            returned: on success
            type: bool
            sample: true
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        private_ip:
            description:
                - The IP addresses assigned to the Database Management private endpoint.
            returned: on success
            type: str
            sample: private_ip_example
        description:
            description:
                - The description of the Database Management private endpoint.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The date and time the Database Managament private endpoint was created, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the Database Management private endpoint.
            returned: on success
            type: str
            sample: CREATING
        nsg_ids:
            description:
                - The OCIDs of the Network Security Groups to which the Database Management private endpoint belongs.
            returned: on success
            type: list
            sample: []
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cluster": true,
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "private_ip": "private_ip_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "nsg_ids": []
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient
    from oci.database_management.models import CreateDbManagementPrivateEndpointDetails
    from oci.database_management.models import UpdateDbManagementPrivateEndpointDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DbManagementPrivateEndpointHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "db_management_private_endpoint_id"

    def get_module_resource_id(self):
        return self.module.params.get("db_management_private_endpoint_id")

    def get_get_fn(self):
        return self.client.get_db_management_private_endpoint

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_management_private_endpoint,
            db_management_private_endpoint_id=self.module.params.get(
                "db_management_private_endpoint_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name", "is_cluster"]

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
        return oci_common_utils.list_all_resources(
            self.client.list_db_management_private_endpoints, **kwargs
        )

    def get_create_model_class(self):
        return CreateDbManagementPrivateEndpointDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_db_management_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_db_management_private_endpoint_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDbManagementPrivateEndpointDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_db_management_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_management_private_endpoint_id=self.module.params.get(
                    "db_management_private_endpoint_id"
                ),
                update_db_management_private_endpoint_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_db_management_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_management_private_endpoint_id=self.module.params.get(
                    "db_management_private_endpoint_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DbManagementPrivateEndpointHelperCustom = get_custom_class(
    "DbManagementPrivateEndpointHelperCustom"
)


class ResourceHelper(
    DbManagementPrivateEndpointHelperCustom, DbManagementPrivateEndpointHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            compartment_id=dict(type="str"),
            is_cluster=dict(type="bool"),
            subnet_id=dict(type="str"),
            description=dict(type="str"),
            nsg_ids=dict(type="list", elements="str"),
            db_management_private_endpoint_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="db_management_private_endpoint",
        service_client_class=DbManagementClient,
        namespace="database_management",
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
