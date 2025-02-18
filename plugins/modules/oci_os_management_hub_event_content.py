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
module: oci_os_management_hub_event_content
short_description: Manage an EventContent resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to delete an EventContent resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    event_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the event.
        type: str
        aliases: ["id"]
        required: true
    state:
        description:
            - The state of the EventContent.
            - Use I(state=absent) to delete an EventContent.
        type: str
        required: false
        default: 'present'
        choices: ["absent"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Delete event_content
  oci_os_management_hub_event_content:
    # required
    event_id: "ocid1.event.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import EventClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubEventContentHelperGen(OCIResourceHelperBase):
    """Supported operations: get and delete"""

    def get_possible_entity_types(self):
        return super(
            OsManagementHubEventContentHelperGen, self
        ).get_possible_entity_types() + [
            "eventcontent",
            "eventcontents",
            "osManagementHubeventcontent",
            "osManagementHubeventcontents",
            "eventcontentresource",
            "eventcontentsresource",
            "content",
            "contents",
            "osManagementHubcontent",
            "osManagementHubcontents",
            "contentresource",
            "contentsresource",
            "osmanagementhub",
        ]

    def get_module_resource_id_param(self):
        return "event_id"

    def get_module_resource_id(self):
        return self.module.params.get("event_id")

    def get_get_fn(self):
        return self.client.get_event_content

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_event_content, event_id=self.module.params.get("event_id"),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_event_content,
            call_fn_args=(),
            call_fn_kwargs=dict(event_id=self.module.params.get("event_id"),),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


OsManagementHubEventContentHelperCustom = get_custom_class(
    "OsManagementHubEventContentHelperCustom"
)


class ResourceHelper(
    OsManagementHubEventContentHelperCustom, OsManagementHubEventContentHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            event_id=dict(aliases=["id"], type="str", required=True),
            state=dict(type="str", default="present", choices=["absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="event_content",
        service_client_class=EventClient,
        namespace="os_management_hub",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
