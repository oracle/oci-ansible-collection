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
module: oci_os_management_hub_event
short_description: Manage an Event resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete an Event resource in Oracle Cloud Infrastructure
    - "This resource has the following action operations in the M(oracle.oci.oci_os_management_hub_event_actions) module: change_compartment,
      import_event_content."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    event_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the event.
        type: str
        aliases: ["id"]
        required: true
    state:
        description:
            - The state of the Event.
            - Use I(state=present) to update an existing an Event.
            - Use I(state=absent) to delete an Event.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update event
  oci_os_management_hub_event:
    # required
    event_id: "ocid1.event.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete event
  oci_os_management_hub_event:
    # required
    event_id: "ocid1.event.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
event:
    description:
        - Details of the Event resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the event.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
        event_details:
            description:
                - Details of an event.
            returned: on success
            type: str
            sample: event_details_example
        resource_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance or resource where the event
                  occurred.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        system_details:
            description:
                - ""
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
        time_occurred:
            description:
                - The date and time that the event occurred.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        data:
            description:
                - ""
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "KERNEL_OOPS",
        "event_summary": "event_summary_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "event_details": "event_details_example",
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "system_details": {
            "architecture": "X86_64",
            "ksplice_effective_kernel_version": "ksplice_effective_kernel_version_example",
            "os_family": "ORACLE_LINUX_9",
            "os_name": "os_name_example",
            "os_kernel_release": "os_kernel_release_example",
            "os_kernel_version": "os_kernel_version_example",
            "os_system_version": "os_system_version_example"
        },
        "time_occurred": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "is_managed_by_autonomous_linux": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
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
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import WorkRequestClient
    from oci.os_management_hub import EventClient
    from oci.os_management_hub.models import UpdateEventDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubEventHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_possible_entity_types(self):
        return super(
            OsManagementHubEventHelperGen, self
        ).get_possible_entity_types() + [
            "event",
            "events",
            "osManagementHubevent",
            "osManagementHubevents",
            "eventresource",
            "eventsresource",
            "osmanagementhub",
        ]

    def get_module_resource_id_param(self):
        return "event_id"

    def get_module_resource_id(self):
        return self.module.params.get("event_id")

    def get_get_fn(self):
        return self.client.get_event

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_event, event_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_event, event_id=self.module.params.get("event_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_events, **kwargs)

    def get_update_model_class(self):
        return UpdateEventDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_event,
            call_fn_args=(),
            call_fn_kwargs=dict(
                event_id=self.module.params.get("event_id"),
                update_event_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_event,
            call_fn_args=(),
            call_fn_kwargs=dict(event_id=self.module.params.get("event_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OsManagementHubEventHelperCustom = get_custom_class("OsManagementHubEventHelperCustom")


class ResourceHelper(OsManagementHubEventHelperCustom, OsManagementHubEventHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            event_id=dict(aliases=["id"], type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="event",
        service_client_class=EventClient,
        namespace="os_management_hub",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
