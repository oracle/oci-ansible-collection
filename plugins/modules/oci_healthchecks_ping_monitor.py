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
module: oci_healthchecks_ping_monitor
short_description: Manage a PingMonitor resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a PingMonitor resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a ping monitor. Vantage points will be automatically selected if not specified,
      and probes will be initiated from each vantage point to each of the targets at the frequency
      specified by `intervalInSeconds`.
    - "This resource has the following action operations in the M(oracle.oci.oci_healthchecks_ping_monitor_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    targets:
        description:
            - A list of targets (hostnames or IP addresses) of the probe.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: str
    vantage_point_names:
        description:
            - A list of names of vantage points from which to execute the probe.
            - This parameter is updatable.
        type: list
        elements: str
    port:
        description:
            - The port on which to probe endpoints. If unspecified, probes will use the
              default port of their protocol.
            - This parameter is updatable.
        type: int
    timeout_in_seconds:
        description:
            - "The probe timeout in seconds. Valid values: 10, 20, 30, and 60.
              The probe timeout must be less than or equal to `intervalInSeconds` for monitors."
            - This parameter is updatable.
        type: int
    protocol:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "ICMP"
            - "TCP"
    display_name:
        description:
            - A user-friendly and mutable name suitable for display in a user interface.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    interval_in_seconds:
        description:
            - "The monitor interval in seconds. Valid values: 10, 30, and 60."
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    is_enabled:
        description:
            - Enables or disables the monitor. Set to 'true' to launch monitoring.
            - This parameter is updatable.
        type: bool
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace.  For more information,
              see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    monitor_id:
        description:
            - The OCID of a monitor.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the PingMonitor.
            - Use I(state=present) to create or update a PingMonitor.
            - Use I(state=absent) to delete a PingMonitor.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create ping_monitor
  oci_healthchecks_ping_monitor:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    targets: [ "targets_example" ]
    protocol: ICMP
    display_name: display_name_example
    interval_in_seconds: 56

    # optional
    vantage_point_names: [ "vantage_point_names_example" ]
    port: 56
    timeout_in_seconds: 56
    is_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update ping_monitor
  oci_healthchecks_ping_monitor:
    # required
    monitor_id: "ocid1.monitor.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    targets: [ "targets_example" ]
    vantage_point_names: [ "vantage_point_names_example" ]
    port: 56
    timeout_in_seconds: 56
    protocol: ICMP
    display_name: display_name_example
    interval_in_seconds: 56
    is_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update ping_monitor using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_healthchecks_ping_monitor:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    targets: [ "targets_example" ]
    vantage_point_names: [ "vantage_point_names_example" ]
    port: 56
    timeout_in_seconds: 56
    protocol: ICMP
    interval_in_seconds: 56
    is_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete ping_monitor
  oci_healthchecks_ping_monitor:
    # required
    monitor_id: "ocid1.monitor.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete ping_monitor using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_healthchecks_ping_monitor:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        results_url:
            description:
                - A URL for fetching the probe results.
            returned: on success
            type: str
            sample: results_url_example
        home_region:
            description:
                - The region where updates must be made and where results must be fetched from.
            returned: on success
            type: str
            sample: us-phoenix-1
        time_created:
            description:
                - The RFC 3339-formatted creation date and time of the probe.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
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
            type: str
            sample: ICMP
        display_name:
            description:
                - A user-friendly and mutable name suitable for display in a user interface.
            returned: on success
            type: str
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
        "home_region": "us-phoenix-1",
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.healthchecks import HealthChecksClient
    from oci.healthchecks.models import CreatePingMonitorDetails
    from oci.healthchecks.models import UpdatePingMonitorDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PingMonitorHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_ping_monitors, **kwargs
        )

    def get_create_model_class(self):
        return CreatePingMonitorDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_ping_monitor,
            call_fn_args=(),
            call_fn_kwargs=dict(create_ping_monitor_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdatePingMonitorDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_ping_monitor,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitor_id=self.module.params.get("monitor_id"),
                update_ping_monitor_details=update_details,
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
            call_fn=self.client.delete_ping_monitor,
            call_fn_args=(),
            call_fn_kwargs=dict(monitor_id=self.module.params.get("monitor_id"),),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


PingMonitorHelperCustom = get_custom_class("PingMonitorHelperCustom")


class ResourceHelper(PingMonitorHelperCustom, PingMonitorHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            targets=dict(type="list", elements="str"),
            vantage_point_names=dict(type="list", elements="str"),
            port=dict(type="int"),
            timeout_in_seconds=dict(type="int"),
            protocol=dict(type="str", choices=["ICMP", "TCP"]),
            display_name=dict(aliases=["name"], type="str"),
            interval_in_seconds=dict(type="int"),
            is_enabled=dict(type="bool"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            monitor_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
