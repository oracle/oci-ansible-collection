#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_opsi_operations_insights_warehouse_user
short_description: Manage an OperationsInsightsWarehouseUser resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an OperationsInsightsWarehouseUser resource in Oracle Cloud Infrastructure
    - For I(state=present), create a Operations Insights Warehouse user resource for the tenant in Operations Insights.
      This resource will be created in root compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    operations_insights_warehouse_id:
        description:
            - OPSI Warehouse OCID
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
        type: str
    name:
        description:
            - Username for schema which would have access to AWR Data,  Enterprise Manager Data and Operations Insights OPSI Hub.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    connection_password:
        description:
            - User provided connection password for the AWR Data,  Enterprise Manager Data and Operations Insights OPSI Hub.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    is_awr_data_access:
        description:
            - Indicate whether user has access to AWR data.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: bool
    is_em_data_access:
        description:
            - Indicate whether user has access to EM data.
            - This parameter is updatable.
        type: bool
    is_opsi_data_access:
        description:
            - Indicate whether user has access to OPSI data.
            - This parameter is updatable.
        type: bool
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
    operations_insights_warehouse_user_id:
        description:
            - Unique Operations Insights Warehouse User identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the OperationsInsightsWarehouseUser.
            - Use I(state=present) to create or update an OperationsInsightsWarehouseUser.
            - Use I(state=absent) to delete an OperationsInsightsWarehouseUser.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create operations_insights_warehouse_user
  oci_opsi_operations_insights_warehouse_user:
    # required
    operations_insights_warehouse_id: "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    connection_password: example-password
    is_awr_data_access: true

    # optional
    is_em_data_access: true
    is_opsi_data_access: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update operations_insights_warehouse_user
  oci_opsi_operations_insights_warehouse_user:
    # required
    operations_insights_warehouse_user_id: "ocid1.operationsinsightswarehouseuser.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    connection_password: example-password
    is_awr_data_access: true
    is_em_data_access: true
    is_opsi_data_access: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update operations_insights_warehouse_user using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_opsi_operations_insights_warehouse_user:
    # required
    operations_insights_warehouse_id: "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    connection_password: example-password
    is_awr_data_access: true
    is_em_data_access: true
    is_opsi_data_access: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete operations_insights_warehouse_user
  oci_opsi_operations_insights_warehouse_user:
    # required
    operations_insights_warehouse_user_id: "ocid1.operationsinsightswarehouseuser.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete operations_insights_warehouse_user using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_opsi_operations_insights_warehouse_user:
    # required
    operations_insights_warehouse_id: "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    state: absent

"""

RETURN = """
operations_insights_warehouse_user:
    description:
        - Details of the OperationsInsightsWarehouseUser resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        operations_insights_warehouse_id:
            description:
                - OPSI Warehouse OCID
            returned: on success
            type: str
            sample: "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - Hub User OCID
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Username for schema which would have access to AWR Data,  Enterprise Manager Data and Operations Insights OPSI Hub.
            returned: on success
            type: str
            sample: name_example
        connection_password:
            description:
                - User provided connection password for the AWR Data,  Enterprise Manager Data and Operations Insights OPSI Hub.
            returned: on success
            type: str
            sample: example-password
        is_awr_data_access:
            description:
                - Indicate whether user has access to AWR data.
            returned: on success
            type: bool
            sample: true
        is_em_data_access:
            description:
                - Indicate whether user has access to EM data.
            returned: on success
            type: bool
            sample: true
        is_opsi_data_access:
            description:
                - Indicate whether user has access to OPSI data.
            returned: on success
            type: bool
            sample: true
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
        time_created:
            description:
                - The time at which the resource was first created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time at which the resource was last updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - Possible lifecycle states
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
    sample: {
        "operations_insights_warehouse_id": "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "connection_password": "example-password",
        "is_awr_data_access": true,
        "is_em_data_access": true,
        "is_opsi_data_access": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example"
    }
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
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import CreateOperationsInsightsWarehouseUserDetails
    from oci.opsi.models import UpdateOperationsInsightsWarehouseUserDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OperationsInsightsWarehouseUserHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            OperationsInsightsWarehouseUserHelperGen, self
        ).get_possible_entity_types() + [
            "operationsinsightswarehouseuser",
            "operationsinsightswarehouseusers",
            "opsioperationsinsightswarehouseuser",
            "opsioperationsinsightswarehouseusers",
            "operationsinsightswarehouseuserresource",
            "operationsinsightswarehouseusersresource",
            "opsi",
        ]

    def get_module_resource_id_param(self):
        return "operations_insights_warehouse_user_id"

    def get_module_resource_id(self):
        return self.module.params.get("operations_insights_warehouse_user_id")

    def get_get_fn(self):
        return self.client.get_operations_insights_warehouse_user

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_operations_insights_warehouse_user,
            operations_insights_warehouse_user_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_operations_insights_warehouse_user,
            operations_insights_warehouse_user_id=self.module.params.get(
                "operations_insights_warehouse_user_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "operations_insights_warehouse_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id"]

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
            self.client.list_operations_insights_warehouse_users, **kwargs
        )

    def get_create_model_class(self):
        return CreateOperationsInsightsWarehouseUserDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_operations_insights_warehouse_user,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_operations_insights_warehouse_user_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateOperationsInsightsWarehouseUserDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_operations_insights_warehouse_user,
            call_fn_args=(),
            call_fn_kwargs=dict(
                operations_insights_warehouse_user_id=self.module.params.get(
                    "operations_insights_warehouse_user_id"
                ),
                update_operations_insights_warehouse_user_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_operations_insights_warehouse_user,
            call_fn_args=(),
            call_fn_kwargs=dict(
                operations_insights_warehouse_user_id=self.module.params.get(
                    "operations_insights_warehouse_user_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OperationsInsightsWarehouseUserHelperCustom = get_custom_class(
    "OperationsInsightsWarehouseUserHelperCustom"
)


class ResourceHelper(
    OperationsInsightsWarehouseUserHelperCustom,
    OperationsInsightsWarehouseUserHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            operations_insights_warehouse_id=dict(type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            connection_password=dict(type="str", no_log=True),
            is_awr_data_access=dict(type="bool"),
            is_em_data_access=dict(type="bool"),
            is_opsi_data_access=dict(type="bool"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            operations_insights_warehouse_user_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="operations_insights_warehouse_user",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
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
