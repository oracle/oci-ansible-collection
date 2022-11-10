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
module: oci_log_analytics_resource_categories_actions
short_description: Perform actions on a ResourceCategories resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ResourceCategories resource in Oracle Cloud Infrastructure
    - For I(action=remove), removes the category assignments of DASHBOARD and SAVEDSEARCH resources.
    - For I(action=update), updates the category assignments of DASHBOARD and SAVEDSEARCH resources.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    items:
        description:
            - An array of resources and their corresponding category assignments to update.
        type: list
        elements: dict
        suboptions:
            resource_id:
                description:
                    - The unique identifier of the resource, usually a name or ocid.
                type: str
            resource_type:
                description:
                    - The resource type.
                type: str
            category_name:
                description:
                    - The category name to which this resource belongs.
                type: str
            is_system:
                description:
                    - The system flag. A value of false denotes a user-created category assignment.
                      A value of true denotes an Oracle-defined category assignment.
                type: bool
    action:
        description:
            - The action to perform on the ResourceCategories.
        type: str
        required: true
        choices:
            - "remove"
            - "update"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action remove on resource_categories
  oci_log_analytics_resource_categories_actions:
    # required
    namespace_name: namespace_name_example
    action: remove

    # optional
    items:
    - # optional
      resource_id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      resource_type: resource_type_example
      category_name: category_name_example
      is_system: true

- name: Perform action update on resource_categories
  oci_log_analytics_resource_categories_actions:
    # required
    namespace_name: namespace_name_example
    action: update

    # optional
    items:
    - # optional
      resource_id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      resource_type: resource_type_example
      category_name: category_name_example
      is_system: true

"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.log_analytics import LogAnalyticsClient
    from oci.log_analytics.models import LogAnalyticsResourceCategoryDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResourceCategoriesActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        remove
        update
    """

    @staticmethod
    def get_module_resource_id_param():
        return "namespace_name"

    def get_module_resource_id(self):
        return self.module.params.get("namespace_name")

    def remove(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, LogAnalyticsResourceCategoryDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_resource_categories,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                remove_resource_categories_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def update(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, LogAnalyticsResourceCategoryDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_resource_categories,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                update_resource_categories_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


ResourceCategoriesActionsHelperCustom = get_custom_class(
    "ResourceCategoriesActionsHelperCustom"
)


class ResourceHelper(
    ResourceCategoriesActionsHelperCustom, ResourceCategoriesActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            items=dict(
                type="list",
                elements="dict",
                options=dict(
                    resource_id=dict(type="str"),
                    resource_type=dict(type="str"),
                    category_name=dict(type="str"),
                    is_system=dict(type="bool"),
                ),
            ),
            action=dict(type="str", required=True, choices=["remove", "update"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="resource_categories",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
