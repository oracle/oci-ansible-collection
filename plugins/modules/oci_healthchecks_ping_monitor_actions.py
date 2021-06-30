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
module: oci_healthchecks_ping_monitor_actions
short_description: Perform actions on a PingMonitor resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a PingMonitor resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a monitor into a different compartment. When provided, `If-Match` is checked
      against ETag values of the resource.
version_added: "2.9"
author: Oracle (@oracle)
options:
    monitor_id:
        description:
            - The OCID of a monitor.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the PingMonitor.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on ping_monitor
  oci_healthchecks_ping_monitor_actions:
    monitor_id: "ocid1.monitor.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
ping_monitor:
    description:
        - Details of the PingMonitor resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the resource.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        results_url:
            description:
                - A URL for fetching the probe results.
            returned: on success
            type: string
            sample: results_url_example
        home_region:
            description:
                - The region where updates must be made and where results must be fetched from.
            returned: on success
            type: string
            sample: home_region_example
        time_created:
            description:
                - The RFC 3339-formatted creation date and time of the probe.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        targets:
            description:
                - A list of targets (hostnames or IP addresses) of the probe.
            returned: on success
            type: list
            sample: []
        vantage_point_names:
            description:
                - A list of names of vantage points from which to execute the probe.
            returned: on success
            type: list
            sample: []
        port:
            description:
                - The port on which to probe endpoints. If unspecified, probes will use the
                  default port of their protocol.
            returned: on success
            type: int
            sample: 56
        timeout_in_seconds:
            description:
                - "The probe timeout in seconds. Valid values: 10, 20, 30, and 60.
                  The probe timeout must be less than or equal to `intervalInSeconds` for monitors."
            returned: on success
            type: int
            sample: 56
        protocol:
            description:
                - ""
            returned: on success
            type: string
            sample: ICMP
        display_name:
            description:
                - A user-friendly and mutable name suitable for display in a user interface.
            returned: on success
            type: string
            sample: display_name_example
        interval_in_seconds:
            description:
                - "The monitor interval in seconds. Valid values: 10, 30, and 60."
            returned: on success
            type: int
            sample: 56
        is_enabled:
            description:
                - Enables or disables the monitor. Set to 'true' to launch monitoring.
            returned: on success
            type: bool
            sample: true
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace.  For more information,
                  see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "results_url": "results_url_example",
        "home_region": "home_region_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "targets": [],
        "vantage_point_names": [],
        "port": 56,
        "timeout_in_seconds": 56,
        "protocol": "ICMP",
        "display_name": "display_name_example",
        "interval_in_seconds": 56,
        "is_enabled": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
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
    from oci.healthchecks import HealthChecksClient
    from oci.healthchecks.models import ChangePingMonitorCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PingMonitorActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "monitor_id"

    def get_module_resource_id(self):
        return self.module.params.get("monitor_id")

    def get_get_fn(self):
        return self.client.get_ping_monitor

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ping_monitor,
            monitor_id=self.module.params.get("monitor_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangePingMonitorCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_ping_monitor_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitor_id=self.module.params.get("monitor_id"),
                change_ping_monitor_compartment_details=action_details,
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


PingMonitorActionsHelperCustom = get_custom_class("PingMonitorActionsHelperCustom")


class ResourceHelper(PingMonitorActionsHelperCustom, PingMonitorActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            monitor_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ping_monitor",
        service_client_class=HealthChecksClient,
        namespace="healthchecks",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
