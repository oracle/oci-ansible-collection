#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_tenant_manager_control_plane_organization_governance_actions
short_description: Perform actions on an OrganizationGovernance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OrganizationGovernance resource in Oracle Cloud Infrastructure
    - For I(action=add_governance), starts a work request to opt the tenancy in to governance rules.
    - For I(action=remove_governance), starts a work request to opt the tenancy out of governance rules.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    organization_id:
        description:
            - OCID of the organization.
        type: str
        required: true
    organization_tenancy_id:
        description:
            - OCID of tenancy that is opting in to governance rules.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the OrganizationGovernance.
        type: str
        required: true
        choices:
            - "add_governance"
            - "remove_governance"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_governance on organization_governance
  oci_tenant_manager_control_plane_organization_governance_actions:
    # required
    organization_id: "ocid1.organization.oc1..xxxxxxEXAMPLExxxxxx"
    organization_tenancy_id: "ocid1.organizationtenancy.oc1..xxxxxxEXAMPLExxxxxx"
    action: add_governance

- name: Perform action remove_governance on organization_governance
  oci_tenant_manager_control_plane_organization_governance_actions:
    # required
    organization_id: "ocid1.organization.oc1..xxxxxxEXAMPLExxxxxx"
    organization_tenancy_id: "ocid1.organizationtenancy.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_governance

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
    from oci.tenant_manager_control_plane import GovernanceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OrganizationGovernanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_governance
        remove_governance
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "organization_tenancy_id"

    def get_module_resource_id(self):
        return self.module.params.get("organization_tenancy_id")

    def add_governance(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_governance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                organization_id=self.module.params.get("organization_id"),
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

    def remove_governance(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_governance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                organization_id=self.module.params.get("organization_id"),
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


OrganizationGovernanceActionsHelperCustom = get_custom_class(
    "OrganizationGovernanceActionsHelperCustom"
)


class ResourceHelper(
    OrganizationGovernanceActionsHelperCustom, OrganizationGovernanceActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            organization_id=dict(type="str", required=True),
            organization_tenancy_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["add_governance", "remove_governance"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="organization_governance",
        service_client_class=GovernanceClient,
        namespace="tenant_manager_control_plane",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
