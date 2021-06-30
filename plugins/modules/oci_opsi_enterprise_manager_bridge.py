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
module: oci_opsi_enterprise_manager_bridge
short_description: Manage an EnterpriseManagerBridge resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an EnterpriseManagerBridge resource in Oracle Cloud Infrastructure
    - For I(state=present), create a Enterprise Manager bridge in Operations Insights.
    - "This resource has the following action operations in the M(oci_enterprise_manager_bridge_actions) module: change_compartment."
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment identifier of the Enterprise Manager bridge
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - User-friedly name of Enterprise Manager Bridge that does not have to be unique.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Description of Enterprise Manager Bridge
            - This parameter is updatable.
        type: str
    object_storage_bucket_name:
        description:
            - Object Storage Bucket Name
            - Required for create using I(state=present).
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
    enterprise_manager_bridge_id:
        description:
            - Unique Enterprise Manager bridge identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the EnterpriseManagerBridge.
            - Use I(state=present) to create or update an EnterpriseManagerBridge.
            - Use I(state=absent) to delete an EnterpriseManagerBridge.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create enterprise_manager_bridge
  oci_opsi_enterprise_manager_bridge:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    object_storage_bucket_name: object_storage_bucket_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update enterprise_manager_bridge using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_opsi_enterprise_manager_bridge:
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update enterprise_manager_bridge
  oci_opsi_enterprise_manager_bridge:
    display_name: display_name_example
    description: description_example
    enterprise_manager_bridge_id: "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete enterprise_manager_bridge
  oci_opsi_enterprise_manager_bridge:
    enterprise_manager_bridge_id: "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete enterprise_manager_bridge using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_opsi_enterprise_manager_bridge:
    display_name: display_name_example
    state: absent

"""

RETURN = """
enterprise_manager_bridge:
    description:
        - Details of the EnterpriseManagerBridge resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Enterprise Manager bridge identifier
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment identifier of the Enterprise Manager bridge
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User-friedly name of Enterprise Manager Bridge that does not have to be unique.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - Description of Enterprise Manager Bridge
            returned: on success
            type: string
            sample: description_example
        object_storage_namespace_name:
            description:
                - Object Storage Namespace Name
            returned: on success
            type: string
            sample: object_storage_namespace_name_example
        object_storage_bucket_name:
            description:
                - Object Storage Bucket Name
            returned: on success
            type: string
            sample: object_storage_bucket_name_example
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
                - The time the the Enterprise Manager bridge was first created. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time the Enterprise Manager bridge was updated. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the Enterprise Manager bridge.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: string
            sample: lifecycle_details_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "object_storage_namespace_name": "object_storage_namespace_name_example",
        "object_storage_bucket_name": "object_storage_bucket_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example"
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
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import CreateEnterpriseManagerBridgeDetails
    from oci.opsi.models import UpdateEnterpriseManagerBridgeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EnterpriseManagerBridgeHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "enterprise_manager_bridge_id"

    def get_module_resource_id(self):
        return self.module.params.get("enterprise_manager_bridge_id")

    def get_get_fn(self):
        return self.client.get_enterprise_manager_bridge

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_enterprise_manager_bridge,
            enterprise_manager_bridge_id=self.module.params.get(
                "enterprise_manager_bridge_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "display_name"]

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
            self.client.list_enterprise_manager_bridges, **kwargs
        )

    def get_create_model_class(self):
        return CreateEnterpriseManagerBridgeDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_enterprise_manager_bridge,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_enterprise_manager_bridge_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateEnterpriseManagerBridgeDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_enterprise_manager_bridge,
            call_fn_args=(),
            call_fn_kwargs=dict(
                enterprise_manager_bridge_id=self.module.params.get(
                    "enterprise_manager_bridge_id"
                ),
                update_enterprise_manager_bridge_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_enterprise_manager_bridge,
            call_fn_args=(),
            call_fn_kwargs=dict(
                enterprise_manager_bridge_id=self.module.params.get(
                    "enterprise_manager_bridge_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


EnterpriseManagerBridgeHelperCustom = get_custom_class(
    "EnterpriseManagerBridgeHelperCustom"
)


class ResourceHelper(
    EnterpriseManagerBridgeHelperCustom, EnterpriseManagerBridgeHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            object_storage_bucket_name=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            enterprise_manager_bridge_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="enterprise_manager_bridge",
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
