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
module: oci_os_management_event
short_description: Manage an Event resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an Event resource in Oracle Cloud Infrastructure
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
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
        required: true
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    state:
        description:
            - The state of the Event.
            - Use I(state=present) to update an existing an Event.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update event
  oci_os_management_event:
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    event_id: "ocid1.event.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

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
    sample: {
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
    from oci.os_management import EventClient
    from oci.os_management.models import UpdateEventDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EventHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_module_resource_id_param(self):
        return "event_id"

    def get_module_resource_id(self):
        return self.module.params.get("event_id")

    def get_get_fn(self):
        return self.client.get_event

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_event,
            managed_instance_id=self.module.params.get("managed_instance_id"),
            event_id=self.module.params.get("event_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "managed_instance_id",
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["event_id"]

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
        return oci_common_utils.list_all_resources(self.client.list_events, **kwargs)

    def get_update_model_class(self):
        return UpdateEventDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_event,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                event_id=self.module.params.get("event_id"),
                compartment_id=self.module.params.get("compartment_id"),
                update_event_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


EventHelperCustom = get_custom_class("EventHelperCustom")


class ResourceHelper(EventHelperCustom, EventHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            managed_instance_id=dict(type="str", required=True),
            event_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="event",
        service_client_class=EventClient,
        namespace="os_management",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
