#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_monitoring_suppression_actions
short_description: Perform actions on a Suppression resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Suppression resource in Oracle Cloud Infrastructure
    - For I(action=remove_alarm), removes any existing suppression for the specified alarm.
      For important limits information, see L(Limits on
      Monitoring,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits).
      This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
      Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
      or transactions, per second (TPS) for a given tenancy.
version_added: "2.9"
author: Oracle (@oracle)
options:
    alarm_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of an alarm.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the Suppression.
        type: str
        required: true
        choices:
            - "remove_alarm"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action remove_alarm on suppression
  oci_monitoring_suppression_actions:
    alarm_id: ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx
    action: remove_alarm

"""

RETURN = """
suppression:
    description:
        - Details of the Suppression resource acted upon by the current operation
    returned: on success
    type: complex
    contains: TODO - No response model found or could be returning binary data.
    sample: TODO - No response model found or could be returning binary data.
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
    from oci.monitoring import MonitoringClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SuppressionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        remove_alarm
    """

    @staticmethod
    def get_module_resource_id_param():
        return "alarm_id"

    def get_module_resource_id(self):
        return self.module.params.get("alarm_id")

    def remove_alarm(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_alarm_suppression,
            call_fn_args=(),
            call_fn_kwargs=dict(alarm_id=self.module.params.get("alarm_id"),),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


SuppressionActionsHelperCustom = get_custom_class("SuppressionActionsHelperCustom")


class ResourceHelper(SuppressionActionsHelperCustom, SuppressionActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            alarm_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["remove_alarm"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="suppression",
        service_client_class=MonitoringClient,
        namespace="monitoring",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
