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
module: oci_os_management_event_facts
short_description: Fetches details about one or multiple Event resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Event resources in Oracle Cloud Infrastructure
    - Returns a list of Events.
    - If I(event_id) is specified, the details of a single Event will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_instance_id:
        description:
            - Instance Oracle Cloud identifier (ocid)
        type: str
        required: true
    event_id:
        description:
            - Unique Event identifier (OCID)
            - Required to get a specific event.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is
              ascending. If no value is specified TIMECREATED is default.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    event_type:
        description:
            - A filter to return only event of given type.
        type: str
        choices:
            - "KERNEL_OOPS"
            - "KERNEL_CRASH"
            - "CRASH"
            - "EXPLOIT_ATTEMPT"
            - "COMPLIANCE"
            - "TUNING_SUGGESTION"
            - "TUNING_APPLIED"
            - "SECURITY"
            - "ERROR"
            - "WARNING"
    latest_timestamp_less_than:
        description:
            - "filter event occurrence. Selecting only those last occurred before given date in ISO 8601 format
              Example: 2017-07-14T02:40:00.000Z"
        type: str
    latest_timestamp_greater_than_or_equal_to:
        description:
            - "filter event occurrence. Selecting only those last occurred on or after given date in ISO 8601 format
              Example: 2017-07-14T02:40:00.000Z"
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List events
  oci_os_management_event_facts:
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific event
  oci_os_management_event_facts:
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    event_id: "ocid1.event.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
events:
    description:
        - List of Event resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID identifier of the event
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        instance_id:
            description:
                - OCI identifier of the instance where the event occurred
            returned: on success
            type: str
            sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - OCI identifier of the compartement where the instance is
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        tenancy_id:
            description:
                - OCID identifier of the instance tenancy.
            returned: on success
            type: str
            sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        summary:
            description:
                - human readable description of the event
            returned: on success
            type: str
            sample: summary_example
        timestamp:
            description:
                - Time of the occurrence of the event
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        event_fingerprint:
            description:
                - Unique ID used to group event with the same characteristics together.
                  The list of such groups of event can be retrieved via /recurringEvents/{EventFingerprint}
            returned: on success
            type: str
            sample: event_fingerprint_example
        count:
            description:
                - Event occurrence count. Number of time the event has happen on the system.
            returned: on success
            type: int
            sample: 56
        event_type:
            description:
                - Type of the Event.
            returned: on success
            type: str
            sample: KERNEL_OOPS
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        reason:
            description:
                - reason of the crash
            returned: on success
            type: str
            sample: reason_example
        time_first_occurred:
            description:
                - First occurrence time of the event
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vmcore:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                component:
                    description:
                        - Kernel module responsible of the crash.
                    returned: on success
                    type: str
                    sample: component_example
                backtrace:
                    description:
                        - Crash backtrace.
                    returned: on success
                    type: str
                    sample: backtrace_example
        content:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                content_availability:
                    description:
                        - Status of the event content
                    returned: on success
                    type: str
                    sample: NOT_AVAILABLE
                instance_path:
                    description:
                        - Path to the event content on the instance
                    returned: on success
                    type: str
                    sample: instance_path_example
                size:
                    description:
                        - size in bytes of the event content (size of the zip file uploaded)
                    returned: on success
                    type: int
                    sample: 56
        system:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                architecture:
                    description:
                        - system architecture
                    returned: on success
                    type: str
                    sample: IA_32
                ksplice_effective_kernel_version:
                    description:
                        - Active ksplice kernel version (uptrack-uname -r)
                    returned: on success
                    type: str
                    sample: ksplice_effective_kernel_version_example
                os_family:
                    description:
                        - The Operating System type of the managed instance.
                    returned: on success
                    type: str
                    sample: LINUX
                os_name:
                    description:
                        - Operating System Name (OCA value)
                    returned: on success
                    type: str
                    sample: os_name_example
                os_kernel_release:
                    description:
                        - Operating System Kernel Release (uname -v)
                    returned: on success
                    type: str
                    sample: os_kernel_release_example
                os_kernel_version:
                    description:
                        - Operating System Kernel Version (uname -r)
                    returned: on success
                    type: str
                    sample: os_kernel_version_example
                os_system_version:
                    description:
                        - Version of the OS (VERSION from /etc/os-release)
                    returned: on success
                    type: str
                    sample: os_system_version_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "summary": "summary_example",
        "timestamp": "2013-10-20T19:20:30+01:00",
        "event_fingerprint": "event_fingerprint_example",
        "count": 56,
        "event_type": "KERNEL_OOPS",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "reason": "reason_example",
        "time_first_occurred": "2013-10-20T19:20:30+01:00",
        "vmcore": {
            "component": "component_example",
            "backtrace": "backtrace_example"
        },
        "content": {
            "content_availability": "NOT_AVAILABLE",
            "instance_path": "instance_path_example",
            "size": 56
        },
        "system": {
            "architecture": "IA_32",
            "ksplice_effective_kernel_version": "ksplice_effective_kernel_version_example",
            "os_family": "LINUX",
            "os_name": "os_name_example",
            "os_kernel_release": "os_kernel_release_example",
            "os_kernel_version": "os_kernel_version_example",
            "os_system_version": "os_system_version_example"
        }
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.os_management import EventClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EventFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "managed_instance_id",
            "event_id",
            "compartment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "managed_instance_id",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_event,
            managed_instance_id=self.module.params.get("managed_instance_id"),
            event_id=self.module.params.get("event_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "event_id",
            "sort_order",
            "sort_by",
            "event_type",
            "latest_timestamp_less_than",
            "latest_timestamp_greater_than_or_equal_to",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_events,
            managed_instance_id=self.module.params.get("managed_instance_id"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


EventFactsHelperCustom = get_custom_class("EventFactsHelperCustom")


class ResourceFactsHelper(EventFactsHelperCustom, EventFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_instance_id=dict(type="str", required=True),
            event_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            event_type=dict(
                type="str",
                choices=[
                    "KERNEL_OOPS",
                    "KERNEL_CRASH",
                    "CRASH",
                    "EXPLOIT_ATTEMPT",
                    "COMPLIANCE",
                    "TUNING_SUGGESTION",
                    "TUNING_APPLIED",
                    "SECURITY",
                    "ERROR",
                    "WARNING",
                ],
            ),
            latest_timestamp_less_than=dict(type="str"),
            latest_timestamp_greater_than_or_equal_to=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="event",
        service_client_class=EventClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(events=result)


if __name__ == "__main__":
    main()
