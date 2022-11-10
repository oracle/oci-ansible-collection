#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_tenant_manager_control_plane_link
short_description: Manage a Link resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to delete a Link resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    link_id:
        description:
            - OCID of the link to terminate.
        type: str
        aliases: ["id"]
        required: true
    state:
        description:
            - The state of the Link.
            - Use I(state=absent) to delete a Link.
        type: str
        required: false
        default: 'present'
        choices: ["absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Delete link
  oci_tenant_manager_control_plane_link:
    # required
    link_id: "ocid1.link.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
link:
    description:
        - Details of the Link resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID of the link.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        parent_tenancy_id:
            description:
                - OCID of the parent tenancy.
            returned: on success
            type: str
            sample: "ocid1.parenttenancy.oc1..xxxxxxEXAMPLExxxxxx"
        child_tenancy_id:
            description:
                - OCID of the child tenancy.
            returned: on success
            type: str
            sample: "ocid1.childtenancy.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - Lifecycle state of the link.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - Date-time when this link was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Date-time when this link was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_terminated:
            description:
                - Date-time when this link was terminated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "parent_tenancy_id": "ocid1.parenttenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "child_tenancy_id": "ocid1.childtenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_terminated": "2013-10-20T19:20:30+01:00"
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
    from oci.tenant_manager_control_plane import WorkRequestClient
    from oci.tenant_manager_control_plane import LinkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LinkHelperGen(OCIResourceHelperBase):
    """Supported operations: get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_possible_entity_types(self):
        return super(LinkHelperGen, self).get_possible_entity_types() + [
            "link",
            "links",
            "tenantManagerControlPlanelink",
            "tenantManagerControlPlanelinks",
            "linkresource",
            "linksresource",
            "tenantmanagercontrolplane",
        ]

    def get_module_resource_id_param(self):
        return "link_id"

    def get_module_resource_id(self):
        return self.module.params.get("link_id")

    def get_get_fn(self):
        return self.client.get_link

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_link, link_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_link, link_id=self.module.params.get("link_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_links, **kwargs)

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_link,
            call_fn_args=(),
            call_fn_kwargs=dict(link_id=self.module.params.get("link_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


LinkHelperCustom = get_custom_class("LinkHelperCustom")


class ResourceHelper(LinkHelperCustom, LinkHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            link_id=dict(aliases=["id"], type="str", required=True),
            state=dict(type="str", default="present", choices=["absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="link",
        service_client_class=LinkClient,
        namespace="tenant_manager_control_plane",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
