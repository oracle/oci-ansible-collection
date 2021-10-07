#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_log_analytics_entity_type
short_description: Manage a LogAnalyticsEntityType resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a LogAnalyticsEntityType resource in Oracle Cloud Infrastructure
    - For I(state=present), add custom log analytics entity type.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    name:
        description:
            - Log analytics entity type name.
        type: str
        required: true
    category:
        description:
            - Log analytics entity type category. Category will be used for grouping and filtering.
            - This parameter is updatable.
        type: str
    properties:
        description:
            - Log analytics entity type property definition.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - Log analytics entity type property name.
                type: str
                required: true
            description:
                description:
                    - Description for the log analytics entity type property.
                type: str
    state:
        description:
            - The state of the LogAnalyticsEntityType.
            - Use I(state=present) to create or update a LogAnalyticsEntityType.
            - Use I(state=absent) to delete a LogAnalyticsEntityType.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create log_analytics_entity_type
  oci_log_analytics_entity_type:
    namespace_name: namespace_name_example
    name: name_example

- name: Update log_analytics_entity_type
  oci_log_analytics_entity_type:
    namespace_name: namespace_name_example
    name: name_example

- name: Delete log_analytics_entity_type
  oci_log_analytics_entity_type:
    namespace_name: namespace_name_example
    name: name_example
    state: absent

"""

RETURN = """
log_analytics_entity_type:
    description:
        - Details of the LogAnalyticsEntityType resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Log analytics entity type name.
            returned: on success
            type: str
            sample: name_example
        internal_name:
            description:
                - Internal name for the log analytics entity type.
            returned: on success
            type: str
            sample: internal_name_example
        compartment_id:
            description:
                - Compartment Identifier L(OCID],https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        category:
            description:
                - Log analytics entity type category. Category will be used for grouping and filtering.
            returned: on success
            type: str
            sample: category_example
        cloud_type:
            description:
                - Log analytics entity type group. That can be CLOUD (OCI) or NON_CLOUD otherwise.
            returned: on success
            type: str
            sample: CLOUD
        properties:
            description:
                - The parameters used in file patterns specified in log sources for this log analytics entity type.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Log analytics entity type property name.
                    returned: on success
                    type: str
                    sample: name_example
                description:
                    description:
                        - Description for the log analytics entity type property.
                    returned: on success
                    type: str
                    sample: description_example
        lifecycle_state:
            description:
                - The current lifecycle state of the log analytics entity.
            returned: on success
            type: str
            sample: ACTIVE
        time_created:
            description:
                - Time the log analytics entity type was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time the log analytics entity type was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        management_agent_eligibility_status:
            description:
                - This field indicates whether logs for entities of this type can be collected using a management agent.
            returned: on success
            type: str
            sample: ELIGIBLE
    sample: {
        "name": "name_example",
        "internal_name": "internal_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "category": "category_example",
        "cloud_type": "CLOUD",
        "properties": [{
            "name": "name_example",
            "description": "description_example"
        }],
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "management_agent_eligibility_status": "ELIGIBLE"
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
    from oci.log_analytics import LogAnalyticsClient
    from oci.log_analytics.models import CreateLogAnalyticsEntityTypeDetails
    from oci.log_analytics.models import UpdateLogAnalyticsEntityTypeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsEntityTypeHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_log_analytics_entity_type

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_entity_type,
            namespace_name=self.module.params.get("namespace_name"),
            entity_type_name=self.module.params.get("name"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "namespace_name",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

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
            self.client.list_log_analytics_entity_types, **kwargs
        )

    def get_create_model_class(self):
        return CreateLogAnalyticsEntityTypeDetails

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_log_analytics_entity_type,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                create_log_analytics_entity_type_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateLogAnalyticsEntityTypeDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_log_analytics_entity_type,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                update_log_analytics_entity_type_details=update_details,
                entity_type_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_log_analytics_entity_type,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                entity_type_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


LogAnalyticsEntityTypeHelperCustom = get_custom_class(
    "LogAnalyticsEntityTypeHelperCustom"
)


class ResourceHelper(
    LogAnalyticsEntityTypeHelperCustom, LogAnalyticsEntityTypeHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            name=dict(type="str", required=True),
            category=dict(type="str"),
            properties=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True), description=dict(type="str")
                ),
            ),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="log_analytics_entity_type",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
