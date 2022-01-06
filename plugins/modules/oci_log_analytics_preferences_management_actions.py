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
module: oci_log_analytics_preferences_management_actions
short_description: Perform actions on a PreferencesManagement resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a PreferencesManagement resource in Oracle Cloud Infrastructure
    - "For I(action=remove_preferences), removes the tenant preferences. Currently, only \\"DEFAULT_HOMEPAGE\\" is supported."
    - "For I(action=update_preferences), updates the tenant preferences. Currently, only \\"DEFAULT_HOMEPAGE\\" is supported."
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
            - An array of tenant preference details.
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - "The preference name. Currently, only \\"DEFAULT_HOMEPAGE\\" is supported."
                type: str
            value:
                description:
                    - The preference value.
                type: str
    action:
        description:
            - The action to perform on the PreferencesManagement.
        type: str
        required: true
        choices:
            - "remove_preferences"
            - "update_preferences"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action remove_preferences on preferences_management
  oci_log_analytics_preferences_management_actions:
    # required
    namespace_name: namespace_name_example
    action: remove_preferences

    # optional
    items:
    - # optional
      name: name_example
      value: value_example

- name: Perform action update_preferences on preferences_management
  oci_log_analytics_preferences_management_actions:
    # required
    namespace_name: namespace_name_example
    action: update_preferences

    # optional
    items:
    - # optional
      name: name_example
      value: value_example

"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.log_analytics import LogAnalyticsClient
    from oci.log_analytics.models import LogAnalyticsPreferenceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PreferencesManagementActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        remove_preferences
        update_preferences
    """

    @staticmethod
    def get_module_resource_id_param():
        return "namespace_name"

    def get_module_resource_id(self):
        return self.module.params.get("namespace_name")

    def remove_preferences(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, LogAnalyticsPreferenceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_preferences,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                remove_preferences_details=action_details,
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

    def update_preferences(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, LogAnalyticsPreferenceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_preferences,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                update_preferences_details=action_details,
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


PreferencesManagementActionsHelperCustom = get_custom_class(
    "PreferencesManagementActionsHelperCustom"
)


class ResourceHelper(
    PreferencesManagementActionsHelperCustom, PreferencesManagementActionsHelperGen
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
                options=dict(name=dict(type="str"), value=dict(type="str")),
            ),
            action=dict(
                type="str",
                required=True,
                choices=["remove_preferences", "update_preferences"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="preferences_management",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
