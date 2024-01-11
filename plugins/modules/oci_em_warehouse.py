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
module: oci_em_warehouse
short_description: Manage an EmWarehouse resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an EmWarehouse resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new EmWarehouse.
    - "This resource has the following action operations in the M(oracle.oci.oci_em_warehouse_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - EmWarehouse Identifier
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    operations_insights_warehouse_id:
        description:
            - operations Insights Warehouse Identifier
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - Compartment Identifier
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    em_bridge_id:
        description:
            - EMBridge Identifier
            - Required for create using I(state=present).
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
    em_warehouse_id:
        description:
            - unique EmWarehouse identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the EmWarehouse.
            - Use I(state=present) to create or update an EmWarehouse.
            - Use I(state=absent) to delete an EmWarehouse.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create em_warehouse
  oci_em_warehouse:
    # required
    operations_insights_warehouse_id: "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    em_bridge_id: "ocid1.embridge.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update em_warehouse
  oci_em_warehouse:
    # required
    em_warehouse_id: "ocid1.emwarehouse.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    em_bridge_id: "ocid1.embridge.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update em_warehouse using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_em_warehouse:
    # required
    display_name: display_name_example

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    em_bridge_id: "ocid1.embridge.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete em_warehouse
  oci_em_warehouse:
    # required
    em_warehouse_id: "ocid1.emwarehouse.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete em_warehouse using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_em_warehouse:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
em_warehouse:
    description:
        - Details of the EmWarehouse resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        operations_insights_warehouse_id:
            description:
                - operations Insights Warehouse Identifier
            returned: on success
            type: str
            sample: "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx"
        latest_etl_run_status:
            description:
                - Data Flow Run Status
            returned: on success
            type: str
            sample: latest_etl_run_status_example
        latest_etl_run_message:
            description:
                - Data Flow Run Status Message
            returned: on success
            type: str
            sample: latest_etl_run_message_example
        latest_etl_run_time:
            description:
                - Data Flow Run Total Time
            returned: on success
            type: str
            sample: latest_etl_run_time_example
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - EmWarehouse Identifier, can be renamed
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        em_warehouse_type:
            description:
                - Type of the EmWarehouse.
            returned: on success
            type: str
            sample: em_warehouse_type_example
        em_bridge_id:
            description:
                - EMBridge Identifier
            returned: on success
            type: str
            sample: "ocid1.embridge.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the the EmWarehouse was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the EmWarehouse was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the EmWarehouse.
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
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "operations_insights_warehouse_id": "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx",
        "latest_etl_run_status": "latest_etl_run_status_example",
        "latest_etl_run_message": "latest_etl_run_message_example",
        "latest_etl_run_time": "latest_etl_run_time_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "em_warehouse_type": "em_warehouse_type_example",
        "em_bridge_id": "ocid1.embridge.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.em_warehouse import EmWarehouseClient
    from oci.em_warehouse.models import CreateEmWarehouseDetails
    from oci.em_warehouse.models import UpdateEmWarehouseDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EmWarehouseHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(EmWarehouseHelperGen, self).get_possible_entity_types() + [
            "emwarehouse",
            "emwarehouses",
            "emWarehouseemwarehouse",
            "emWarehouseemwarehouses",
            "emwarehouseresource",
            "emwarehousesresource",
        ]

    def get_module_resource_id_param(self):
        return "em_warehouse_id"

    def get_module_resource_id(self):
        return self.module.params.get("em_warehouse_id")

    def get_get_fn(self):
        return self.client.get_em_warehouse

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_em_warehouse, em_warehouse_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_em_warehouse,
            em_warehouse_id=self.module.params.get("em_warehouse_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name", "operations_insights_warehouse_id"]
            if self._use_name_as_identifier()
            else ["compartment_id", "display_name", "operations_insights_warehouse_id"]
        )

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
            self.client.list_em_warehouses, **kwargs
        )

    def get_create_model_class(self):
        return CreateEmWarehouseDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_em_warehouse,
            call_fn_args=(),
            call_fn_kwargs=dict(create_em_warehouse_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateEmWarehouseDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_em_warehouse,
            call_fn_args=(),
            call_fn_kwargs=dict(
                em_warehouse_id=self.module.params.get("em_warehouse_id"),
                update_em_warehouse_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_em_warehouse,
            call_fn_args=(),
            call_fn_kwargs=dict(
                em_warehouse_id=self.module.params.get("em_warehouse_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


EmWarehouseHelperCustom = get_custom_class("EmWarehouseHelperCustom")


class ResourceHelper(EmWarehouseHelperCustom, EmWarehouseHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            operations_insights_warehouse_id=dict(type="str"),
            compartment_id=dict(type="str"),
            em_bridge_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            em_warehouse_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="em_warehouse",
        service_client_class=EmWarehouseClient,
        namespace="em_warehouse",
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
