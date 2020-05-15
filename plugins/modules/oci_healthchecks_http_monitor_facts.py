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
module: oci_healthchecks_http_monitor_facts
short_description: Fetches details about one or multiple HttpMonitor resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple HttpMonitor resources in Oracle Cloud Infrastructure
    - Gets a list of HTTP monitors.
    - If I(monitor_id) is specified, the details of a single HttpMonitor will be returned.
version_added: "2.5"
options:
    monitor_id:
        description:
            - The OCID of a monitor.
            - Required to get a specific http_monitor.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - Filters results by compartment.
            - Required to list multiple http_monitors.
        type: str
    sort_by:
        description:
            - The field to sort by when listing monitors.
        type: str
        choices:
            - "id"
            - "displayName"
            - "timeCreated"
    sort_order:
        description:
            - Controls the sort order of results.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - Filters results that exactly match the `displayName` field.
        type: str
        aliases: ["name"]
    home_region:
        description:
            - Filters results that match the `homeRegion`.
        type: str
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List http_monitors
  oci_healthchecks_http_monitor_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific http_monitor
  oci_healthchecks_http_monitor_facts:
    monitor_id: ocid1.monitor.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
http_monitors:
    description:
        - List of HttpMonitor resources
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
    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.healthchecks import HealthChecksClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HttpMonitorFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "monitor_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_http_monitor,
            monitor_id=self.module.params.get("monitor_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "display_name",
            "home_region",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_http_monitors,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


HttpMonitorFactsHelperCustom = get_custom_class("HttpMonitorFactsHelperCustom")


class ResourceFactsHelper(HttpMonitorFactsHelperCustom, HttpMonitorFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            monitor_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["id", "displayName", "timeCreated"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
            home_region=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="http_monitor",
        service_client_class=HealthChecksClient,
        namespace="healthchecks",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(http_monitors=result)


if __name__ == "__main__":
    main()
