#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_tenant_manager_control_plane_organization_tenancy_actions
short_description: Perform actions on an OrganizationTenancy resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OrganizationTenancy resource in Oracle Cloud Infrastructure
    - For I(action=approve_organization_tenancy_for_transfer), approve an organization's child tenancy for transfer.
    - For I(action=restore), an asynchronous API to restore a tenancy.
    - For I(action=unapprove_organization_tenancy_for_transfer), cancel an organization's child tenancy for transfer.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required for I(action=approve_organization_tenancy_for_transfer), I(action=unapprove_organization_tenancy_for_transfer).
        type: str
    organization_tenancy_id:
        description:
            - OCID of the child tenancy.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the OrganizationTenancy.
        type: str
        required: true
        choices:
            - "approve_organization_tenancy_for_transfer"
            - "restore"
            - "unapprove_organization_tenancy_for_transfer"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action approve_organization_tenancy_for_transfer on organization_tenancy
  oci_tenant_manager_control_plane_organization_tenancy_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    organization_tenancy_id: "ocid1.organizationtenancy.oc1..xxxxxxEXAMPLExxxxxx"
    action: approve_organization_tenancy_for_transfer

- name: Perform action restore on organization_tenancy
  oci_tenant_manager_control_plane_organization_tenancy_actions:
    # required
    organization_tenancy_id: "ocid1.organizationtenancy.oc1..xxxxxxEXAMPLExxxxxx"
    action: restore

- name: Perform action unapprove_organization_tenancy_for_transfer on organization_tenancy
  oci_tenant_manager_control_plane_organization_tenancy_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    organization_tenancy_id: "ocid1.organizationtenancy.oc1..xxxxxxEXAMPLExxxxxx"
    action: unapprove_organization_tenancy_for_transfer

"""

RETURN = """
organization_tenancy:
    description:
        - Details of the OrganizationTenancy resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        tenancy_id:
            description:
                - OCID of the tenancy.
            returned: on success
            type: str
            sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Name of the tenancy.
            returned: on success
            type: str
            sample: name_example
        lifecycle_state:
            description:
                - Lifecycle state of the organization tenancy.
            returned: on success
            type: str
            sample: CREATING
        role:
            description:
                - Role of the organization tenancy.
            returned: on success
            type: str
            sample: PARENT
        time_joined:
            description:
                - Date and time when the tenancy joined the organization.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_left:
            description:
                - Date and time when the tenancy left the organization.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_approved_for_transfer:
            description:
                - Parameter to indicate the tenancy is approved for transfer to another organization.
            returned: on success
            type: bool
            sample: true
        governance_status:
            description:
                - The governance status of the tenancy.
            returned: on success
            type: str
            sample: OPTED_IN
    sample: {
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "lifecycle_state": "CREATING",
        "role": "PARENT",
        "time_joined": "2013-10-20T19:20:30+01:00",
        "time_left": "2013-10-20T19:20:30+01:00",
        "is_approved_for_transfer": true,
        "governance_status": "OPTED_IN"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.tenant_manager_control_plane import WorkRequestClient
    from oci.tenant_manager_control_plane import OrganizationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OrganizationTenancyActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        approve_organization_tenancy_for_transfer
        restore
        unapprove_organization_tenancy_for_transfer
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "organization_tenancy_id"

    def get_module_resource_id(self):
        return self.module.params.get("organization_tenancy_id")

    def get_get_fn(self):
        return self.client.get_organization_tenancy

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_organization_tenancy,
            organization_id=self.module.params.get("organization_id"),
            tenancy_id=self.module.params.get("tenancy_id"),
        )

    def approve_organization_tenancy_for_transfer(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.approve_organization_tenancy_for_transfer,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compartment_id=self.module.params.get("compartment_id"),
                organization_tenancy_id=self.module.params.get(
                    "organization_tenancy_id"
                ),
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

    def restore(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.restore_organization_tenancy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                organization_tenancy_id=self.module.params.get(
                    "organization_tenancy_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def unapprove_organization_tenancy_for_transfer(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.unapprove_organization_tenancy_for_transfer,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compartment_id=self.module.params.get("compartment_id"),
                organization_tenancy_id=self.module.params.get(
                    "organization_tenancy_id"
                ),
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


OrganizationTenancyActionsHelperCustom = get_custom_class(
    "OrganizationTenancyActionsHelperCustom"
)


class ResourceHelper(
    OrganizationTenancyActionsHelperCustom, OrganizationTenancyActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            organization_tenancy_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "approve_organization_tenancy_for_transfer",
                    "restore",
                    "unapprove_organization_tenancy_for_transfer",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="organization_tenancy",
        service_client_class=OrganizationClient,
        namespace="tenant_manager_control_plane",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
