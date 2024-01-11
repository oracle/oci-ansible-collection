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
module: oci_appmgmt_control_monitored_instance_actions
short_description: Perform actions on a MonitoredInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a MonitoredInstance resource in Oracle Cloud Infrastructure
    - For I(action=activate_monitoring_plugin), activates Resource Plugin for compute instance identified by the instance ocid.
      Stores monitored instances Id and its state. Tries to enable Resource Monitoring plugin by making
      remote calls to Oracle Cloud Agent and Management Agent Cloud Service.
    - For I(action=publish_top_processes_metrics), starts cpu and memory top processes collection.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    monitored_instance_id:
        description:
            - OCID of monitored instance.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the MonitoredInstance.
        type: str
        required: true
        choices:
            - "activate_monitoring_plugin"
            - "publish_top_processes_metrics"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action activate_monitoring_plugin on monitored_instance
  oci_appmgmt_control_monitored_instance_actions:
    # required
    monitored_instance_id: "ocid1.monitoredinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: activate_monitoring_plugin

- name: Perform action publish_top_processes_metrics on monitored_instance
  oci_appmgmt_control_monitored_instance_actions:
    # required
    monitored_instance_id: "ocid1.monitoredinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: publish_top_processes_metrics

"""

RETURN = """
monitored_instance:
    description:
        - Details of the MonitoredInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        instance_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of monitored instance.
            returned: on success
            type: str
            sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name of the monitored instance. It is binded to L(Compute
                  Instance,https://docs.cloud.oracle.com/Content/Compute/Concepts/computeoverview.htm).
                  DisplayName is fetched from L(Core Service API,https://docs.cloud.oracle.com/api/#/en/iaas/20160918/Instance/).
            returned: on success
            type: str
            sample: display_name_example
        management_agent_id:
            description:
                - Management Agent Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                  Used to invoke manage operations on Management Agent Cloud Service.
            returned: on success
            type: str
            sample: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the MonitoredInstance was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the MonitoredInstance was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        monitoring_state:
            description:
                - Monitoring status. Can be either enabled or disabled.
            returned: on success
            type: str
            sample: ENABLED
        lifecycle_state:
            description:
                - The current state of the monitored instance.
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
        "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "management_agent_id": "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "monitoring_state": "ENABLED",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example"
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
    from oci.appmgmt_control import AppmgmtControlClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MonitoredInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        activate_monitoring_plugin
        publish_top_processes_metrics
    """

    @staticmethod
    def get_module_resource_id_param():
        return "monitored_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("monitored_instance_id")

    def get_get_fn(self):
        return self.client.get_monitored_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_monitored_instance,
            monitored_instance_id=self.module.params.get("monitored_instance_id"),
        )

    def activate_monitoring_plugin(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.activate_monitoring_plugin,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitored_instance_id=self.module.params.get("monitored_instance_id"),
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

    def publish_top_processes_metrics(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.publish_top_processes_metrics,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitored_instance_id=self.module.params.get("monitored_instance_id"),
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


MonitoredInstanceActionsHelperCustom = get_custom_class(
    "MonitoredInstanceActionsHelperCustom"
)


class ResourceHelper(
    MonitoredInstanceActionsHelperCustom, MonitoredInstanceActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            monitored_instance_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["activate_monitoring_plugin", "publish_top_processes_metrics"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="monitored_instance",
        service_client_class=AppmgmtControlClient,
        namespace="appmgmt_control",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
