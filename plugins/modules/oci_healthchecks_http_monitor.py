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
module: oci_healthchecks_http_monitor
short_description: Manage a HttpMonitor resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a HttpMonitor resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an HTTP monitor. Vantage points will be automatically selected if not specified,
      and probes will be initiated from each vantage point to each of the targets at the frequency
      specified by `intervalInSeconds`.
version_added: "2.5"
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
        type: list
    vantage_point_names:
        description:
            - A list of names of vantage points from which to execute the probe.
        type: list
    port:
        description:
            - The port on which to probe endpoints. If unspecified, probes will use the
              default port of their protocol.
        type: int
    timeout_in_seconds:
        description:
            - "The probe timeout in seconds. Valid values: 10, 20, 30, and 60.
              The probe timeout must be less than or equal to `intervalInSeconds` for monitors."
        type: int
    protocol:
        description:
            - ""
            - Required for create using I(state=present).
        type: str
        choices:
            - "HTTP"
            - "HTTPS"
    method:
        description:
            - ""
        type: str
        choices:
            - "GET"
            - "HEAD"
    path:
        description:
            - The optional URL path to probe, including query parameters.
        type: str
    headers:
        description:
            - A dictionary of HTTP request headers.
            - "*Note:* Monitors and probes do not support the use of the `Authorization` HTTP header."
        type: dict
    display_name:
        description:
            - A user-friendly and mutable name suitable for display in a user interface.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    interval_in_seconds:
        description:
            - "The monitor interval in seconds. Valid values: 10, 30, and 60."
            - Required for create using I(state=present).
        type: int
    is_enabled:
        description:
            - Enables or disables the monitor. Set to 'true' to launch monitoring.
        type: bool
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace.  For more information,
              see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
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
            - The state of the HttpMonitor.
            - Use I(state=present) to create or update a HttpMonitor.
            - Use I(state=absent) to delete a HttpMonitor.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create http_monitor
  oci_healthchecks_http_monitor:
    compartment_id: ocid1.tenancy.oc1....
    targets:
    - 192.0.2.0
    protocol: HTTP
    display_name: test
    interval_in_seconds: 300

- name: Update http_monitor using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_healthchecks_http_monitor:
    protocol: HTTPS
    port: 443

- name: Update http_monitor
  oci_healthchecks_http_monitor:
    protocol: HTTPS
    port: 443
    monitor_id: ocid1.monitor.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete http_monitor
  oci_healthchecks_http_monitor:
    monitor_id: ocid1.monitor.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete http_monitor using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_healthchecks_http_monitor:
    compartment_id: ocid1.tenancy.oc1....
    display_name: test
    state: absent

"""

RETURN = """
http_monitor:
    description:
        - Details of the HttpMonitor resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the resource.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
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
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
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
            sample: HTTP
        method:
            description:
                - ""
            returned: on success
            type: string
            sample: GET
        path:
            description:
                - The optional URL path to probe, including query parameters.
            returned: on success
            type: string
            sample: path_example
        headers:
            description:
                - A dictionary of HTTP request headers.
                - "*Note:* Monitors and probes do not support the use of the `Authorization` HTTP header."
            returned: on success
            type: dict
            sample: {}
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
        "protocol": "HTTP",
        "method": "GET",
        "path": "path_example",
        "headers": {},
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
    from oci.healthchecks.models import CreateHttpMonitorDetails
    from oci.healthchecks.models import UpdateHttpMonitorDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HttpMonitorHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "monitor_id"

    def get_module_resource_id(self):
        return self.module.params.get("monitor_id")

    def get_get_fn(self):
        return self.client.get_http_monitor

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_http_monitor,
            monitor_id=self.module.params.get("monitor_id"),
        )

    def list_resources(self):
        required_list_method_params = [
            "compartment_id",
        ]

        optional_list_method_params = [
            "display_name",
        ]

        required_kwargs = dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

        return oci_common_utils.list_all_resources(
            self.client.list_http_monitors, **kwargs
        )

    def get_create_model_class(self):
        return CreateHttpMonitorDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_http_monitor,
            call_fn_args=(),
            call_fn_kwargs=dict(create_http_monitor_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateHttpMonitorDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_http_monitor,
            call_fn_args=(),
            call_fn_kwargs=dict(
                monitor_id=self.module.params.get("monitor_id"),
                update_http_monitor_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_http_monitor,
            call_fn_args=(),
            call_fn_kwargs=dict(monitor_id=self.module.params.get("monitor_id"),),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


HttpMonitorHelperCustom = get_custom_class("HttpMonitorHelperCustom")


class ResourceHelper(HttpMonitorHelperCustom, HttpMonitorHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            targets=dict(type="list"),
            vantage_point_names=dict(type="list"),
            port=dict(type="int"),
            timeout_in_seconds=dict(type="int"),
            protocol=dict(type="str", choices=["HTTP", "HTTPS"]),
            method=dict(type="str", choices=["GET", "HEAD"]),
            path=dict(type="str"),
            headers=dict(type="dict"),
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
        resource_type="http_monitor",
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
