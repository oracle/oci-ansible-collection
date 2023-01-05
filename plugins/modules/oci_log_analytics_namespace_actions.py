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
module: oci_log_analytics_namespace_actions
short_description: Perform actions on a Namespace resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Namespace resource in Oracle Cloud Infrastructure
    - For I(action=offboard), off-boards a tenant from Logging Analytics
    - For I(action=onboard), on-boards a tenant to Logging Analytics.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Namespace.
        type: str
        required: true
        choices:
            - "offboard"
            - "onboard"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action offboard on namespace
  oci_log_analytics_namespace_actions:
    # required
    namespace_name: namespace_name_example
    action: offboard

- name: Perform action onboard on namespace
  oci_log_analytics_namespace_actions:
    # required
    namespace_name: namespace_name_example
    action: onboard

"""

RETURN = """
namespace:
    description:
        - Details of the Namespace resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        namespace_name:
            description:
                - This is the namespace name of a tenancy
            returned: on success
            type: str
            sample: namespace_name_example
        compartment_id:
            description:
                - The is the tenancy ID
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        is_onboarded:
            description:
                - This indicates if the tenancy is onboarded to Logging Analytics
            returned: on success
            type: bool
            sample: true
        is_log_set_enabled:
            description:
                - This indicates if the log set feature is enabled for the tenancy
            returned: on success
            type: bool
            sample: true
        is_data_ever_ingested:
            description:
                - This indicates if data has ever been ingested for the tenancy in Logging Analytics
            returned: on success
            type: bool
            sample: true
    sample: {
        "namespace_name": "namespace_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_onboarded": true,
        "is_log_set_enabled": true,
        "is_data_ever_ingested": true
    }
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

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NamespaceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        offboard
        onboard
    """

    @staticmethod
    def get_module_resource_id_param():
        return "namespace_name"

    def get_module_resource_id(self):
        return self.module.params.get("namespace_name")

    def get_get_fn(self):
        return self.client.get_namespace

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_namespace,
            namespace_name=self.module.params.get("namespace_name"),
        )

    def offboard(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.offboard_namespace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def onboard(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.onboard_namespace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NamespaceActionsHelperCustom = get_custom_class("NamespaceActionsHelperCustom")


class ResourceHelper(NamespaceActionsHelperCustom, NamespaceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["offboard", "onboard"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="namespace",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
