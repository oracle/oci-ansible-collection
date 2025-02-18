#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_os_management_hub_event_facts
short_description: Fetches details about one or multiple Event resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Event resources in Oracle Cloud Infrastructure
    - Lists events that match the specified criteria, such as compartment, state, and event type.
    - If I(event_id) is specified, the details of a single Event will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    event_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the event.
            - Required to get a specific event.
        type: str
        aliases: ["id"]
    event_summary:
        description:
            - A filter to return only events whose summary matches the given value.
        type: str
    event_summary_contains:
        description:
            - A filter to return only events with a summary that contains the value provided.
        type: str
    event_fingerprint:
        description:
            - The eventFingerprint of the KernelEventData.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
        type: str
    lifecycle_state:
        description:
            - A filter to return only events that match the state provided. The state value is case-insensitive.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    resource_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource. This filter returns resources associated
              with the specified resource.
        type: str
    type:
        description:
            - A filter to return only resources whose type matches the given value.
        type: list
        elements: str
        choices:
            - "KERNEL_OOPS"
            - "KERNEL_CRASH"
            - "EXPLOIT_ATTEMPT"
            - "SOFTWARE_UPDATE"
            - "KSPLICE_UPDATE"
            - "SOFTWARE_SOURCE"
            - "AGENT"
            - "MANAGEMENT_STATION"
    time_created_less_than:
        description:
            - "A filter that returns events that occurred on or before the date provided.
              Example: `2016-08-25T21:10:29.600Z`"
        type: str
    time_created_greater_than_or_equal_to:
        description:
            - "A filter that returns events that occurred on or after the date provided.
              Example: `2016-08-25T21:10:29.600Z`"
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated, timeOccurredAt and timeUpdated is descending. Default
              order for eventSummary is ascending.
        type: str
        choices:
            - "timeCreated"
            - "timeOccurredAt"
            - "timeUpdated"
            - "eventSummary"
    is_managed_by_autonomous_linux:
        description:
            - Indicates whether to list only resources managed by the Autonomous Linux service.
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific event
  oci_os_management_hub_event_facts:
    # required
    event_id: "ocid1.event.oc1..xxxxxxEXAMPLExxxxxx"

- name: List events
  oci_os_management_hub_event_facts:

    # optional
    event_summary: event_summary_example
    event_summary_contains: event_summary_contains_example
    event_fingerprint: event_fingerprint_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    resource_id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    type: [ "KERNEL_OOPS" ]
    time_created_less_than: 2013-10-20T19:20:30+01:00
    time_created_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    sort_order: ASC
    sort_by: timeCreated
    is_managed_by_autonomous_linux: true

"""

RETURN = """
events:
    description:
        - List of Event resources
    returned: on success
    type: complex
    contains:
        event_details:
            description:
                - Details of an event.
                - Returned for get operation
            returned: on success
            type: str
            sample: event_details_example
        system_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                architecture:
                    description:
                        - Architecture type.
                    returned: on success
                    type: str
                    sample: X86_64
                ksplice_effective_kernel_version:
                    description:
                        - Version of the Ksplice effective kernel.
                    returned: on success
                    type: str
                    sample: ksplice_effective_kernel_version_example
                os_family:
                    description:
                        - Operating system type.
                    returned: on success
                    type: str
                    sample: ORACLE_LINUX_9
                os_name:
                    description:
                        - Name of the operating system.
                    returned: on success
                    type: str
                    sample: os_name_example
                os_kernel_release:
                    description:
                        - Release of the kernel.
                    returned: on success
                    type: str
                    sample: os_kernel_release_example
                os_kernel_version:
                    description:
                        - Version of the kernel.
                    returned: on success
                    type: str
                    sample: os_kernel_version_example
                os_system_version:
                    description:
                        - Version of the operating system.
                    returned: on success
                    type: str
                    sample: os_system_version_example
        data:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                operation_type:
                    description:
                        - Type of agent operation.
                    returned: on success
                    type: str
                    sample: LIST_PACKAGES
                status:
                    description:
                        - Status of the agent operation.
                    returned: on success
                    type: str
                    sample: SUCCEEDED
                additional_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        initiator_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that triggered the
                                  event, such as scheduled job id.
                            returned: on success
                            type: str
                            sample: "ocid1.initiator.oc1..xxxxxxEXAMPLExxxxxx"
                        work_request_ids:
                            description:
                                - List of all work request L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) associated with
                                  the event.
                            returned: on success
                            type: list
                            sample: []
                        exploit_cves:
                            description:
                                - List of CVEs in the exploit.
                            returned: on success
                            type: list
                            sample: []
                        vmcore:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                backtrace:
                                    description:
                                        - Kernel vmcore backtrace.
                                    returned: on success
                                    type: str
                                    sample: backtrace_example
                                component:
                                    description:
                                        - Kernel vmcore component.
                                    returned: on success
                                    type: str
                                    sample: component_example
                content:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - "Event type:
                                    * `KERNEL` - Used to identify a kernel oops/crash content
                                    * `EXPLOIT_ATTEMPT` - Used to identify a known exploit detection content"
                            returned: on success
                            type: str
                            sample: KERNEL
                        exploit_detection_log_content:
                            description:
                                - The content of the exploit detection log.
                            returned: on success
                            type: str
                            sample: exploit_detection_log_content_example
                        exploit_object_store_location:
                            description:
                                - The location of the exploit detection log within object storage.
                            returned: on success
                            type: str
                            sample: exploit_object_store_location_example
                        content_availability:
                            description:
                                - "Crash content availability status:
                                      * 'NOT_AVAILABLE' indicates the content is not available on the instance nor in the service
                                      * 'AVAILABLE_ON_INSTANCE' indicates the content is only available on the instance.
                                      * 'AVAILABLE_ON_SERVICE' indicates the content is only available on the service.
                                      * 'AVAILABLE_ON_INSTANCE_AND_SERVICE' indicates the content is available both on the instance and the service
                                      * 'AVAILABLE_ON_INSTANCE_UPLOAD_IN_PROGRESS' indicates the content is available on the instance and its upload to the
                                      service is in progress."
                            returned: on success
                            type: str
                            sample: NOT_AVAILABLE
                        content_location:
                            description:
                                - Location of the Kernel event content.
                            returned: on success
                            type: str
                            sample: content_location_example
                        size:
                            description:
                                - Size of the event content.
                            returned: on success
                            type: int
                            sample: 56
                count:
                    description:
                        - Number of times the event has occurred.
                    returned: on success
                    type: int
                    sample: 56
                event_fingerprint:
                    description:
                        - Fingerprint of the event.
                    returned: on success
                    type: str
                    sample: event_fingerprint_example
                reason:
                    description:
                        - Reason for the event.
                    returned: on success
                    type: str
                    sample: reason_example
                time_first_occurred:
                    description:
                        - The date and time that the event first occurred.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the event.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        event_summary:
            description:
                - Summary of the event.
            returned: on success
            type: str
            sample: event_summary_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - "Event type:
                    * `KERNEL_OOPS` - Used to identify a kernel panic condition event
                    * `KERNEL_CRASH` - Used to identify an internal fatal kernel error that cannot be safely recovered from
                    * `EXPLOIT_ATTEMPT` - Used to identify a known exploit detection as identified by Ksplice
                    * `SOFTWARE_UPDATE` - Software updates - Packages
                    * `KSPLICE_UPDATE` - Ksplice updates
                    * `SOFTWARE_SOURCE` - Software source
                    * `AGENT` - Agent
                    * `MANAGEMENT_STATION` - Management Station"
            returned: on success
            type: str
            sample: KERNEL_OOPS
        resource_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance or resource where the event
                  occurred.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the Event was created, in the format defined by L(RFC 3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The date and time that the event was updated (in L(RFC 3339,https://tools.ietf.org/html/rfc3339) format).
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_occurred:
            description:
                - The date and time that the event occurred.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the event.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Describes the current state of the event in more detail. For example, the
                  message can provide actionable information for a resource in the 'FAILED' state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        is_managed_by_autonomous_linux:
            description:
                - Indicates whether the event occurred on a resource that is managed by the Autonomous Linux service.
            returned: on success
            type: bool
            sample: true
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "event_details": "event_details_example",
        "system_details": {
            "architecture": "X86_64",
            "ksplice_effective_kernel_version": "ksplice_effective_kernel_version_example",
            "os_family": "ORACLE_LINUX_9",
            "os_name": "os_name_example",
            "os_kernel_release": "os_kernel_release_example",
            "os_kernel_version": "os_kernel_version_example",
            "os_system_version": "os_system_version_example"
        },
        "data": {
            "operation_type": "LIST_PACKAGES",
            "status": "SUCCEEDED",
            "additional_details": {
                "initiator_id": "ocid1.initiator.oc1..xxxxxxEXAMPLExxxxxx",
                "work_request_ids": [],
                "exploit_cves": [],
                "vmcore": {
                    "backtrace": "backtrace_example",
                    "component": "component_example"
                }
            },
            "content": {
                "type": "KERNEL",
                "exploit_detection_log_content": "exploit_detection_log_content_example",
                "exploit_object_store_location": "exploit_object_store_location_example",
                "content_availability": "NOT_AVAILABLE",
                "content_location": "content_location_example",
                "size": 56
            },
            "count": 56,
            "event_fingerprint": "event_fingerprint_example",
            "reason": "reason_example",
            "time_first_occurred": "2013-10-20T19:20:30+01:00"
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "event_summary": "event_summary_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "KERNEL_OOPS",
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_occurred": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "is_managed_by_autonomous_linux": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import EventClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubEventFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "event_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_event, event_id=self.module.params.get("event_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "event_summary",
            "event_summary_contains",
            "event_fingerprint",
            "compartment_id",
            "lifecycle_state",
            "resource_id",
            "type",
            "time_created_less_than",
            "time_created_greater_than_or_equal_to",
            "sort_order",
            "sort_by",
            "is_managed_by_autonomous_linux",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_events, **optional_kwargs
        )


OsManagementHubEventFactsHelperCustom = get_custom_class(
    "OsManagementHubEventFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubEventFactsHelperCustom, OsManagementHubEventFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            event_id=dict(aliases=["id"], type="str"),
            event_summary=dict(type="str"),
            event_summary_contains=dict(type="str"),
            event_fingerprint=dict(type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            resource_id=dict(type="str"),
            type=dict(
                type="list",
                elements="str",
                choices=[
                    "KERNEL_OOPS",
                    "KERNEL_CRASH",
                    "EXPLOIT_ATTEMPT",
                    "SOFTWARE_UPDATE",
                    "KSPLICE_UPDATE",
                    "SOFTWARE_SOURCE",
                    "AGENT",
                    "MANAGEMENT_STATION",
                ],
            ),
            time_created_less_than=dict(type="str"),
            time_created_greater_than_or_equal_to=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=[
                    "timeCreated",
                    "timeOccurredAt",
                    "timeUpdated",
                    "eventSummary",
                ],
            ),
            is_managed_by_autonomous_linux=dict(type="bool"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="event",
        service_client_class=EventClient,
        namespace="os_management_hub",
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
