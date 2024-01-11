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
module: oci_tenant_manager_control_plane_organization_tenancy
short_description: Manage an OrganizationTenancy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to delete an OrganizationTenancy resource in Oracle Cloud Infrastructure
    - "This resource has the following action operations in the M(oracle.oci.oci_tenant_manager_control_plane_organization_tenancy_actions) module:
      approve_organization_tenancy_for_transfer, restore, unapprove_organization_tenancy_for_transfer."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    organization_tenancy_id:
        description:
            - OCID of the tenancy to be terminated.
        type: str
        aliases: ["id"]
        required: true
    state:
        description:
            - The state of the OrganizationTenancy.
            - Use I(state=absent) to delete an OrganizationTenancy.
        type: str
        required: false
        default: 'present'
        choices: ["absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Delete organization_tenancy
  oci_tenant_manager_control_plane_organization_tenancy:
    # required
    organization_tenancy_id: "ocid1.organizationtenancy.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.tenant_manager_control_plane import WorkRequestClient
    from oci.tenant_manager_control_plane import OrganizationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OrganizationTenancyHelperGen(OCIResourceHelperBase):
    """Supported operations: get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_possible_entity_types(self):
        return super(OrganizationTenancyHelperGen, self).get_possible_entity_types() + [
            "organizationtenancy",
            "organizationtenancies",
            "tenantManagerControlPlaneorganizationtenancy",
            "tenantManagerControlPlaneorganizationtenancies",
            "organizationtenancyresource",
            "organizationtenanciesresource",
            "tenancy",
            "tenancies",
            "tenantManagerControlPlanetenancy",
            "tenantManagerControlPlanetenancies",
            "tenancyresource",
            "tenanciesresource",
            "tenantmanagercontrolplane",
        ]

    def get_module_resource_id_param(self):
        return "organization_tenancy_id"

    def get_module_resource_id(self):
        return self.module.params.get("organization_tenancy_id")

    def get_get_fn(self):
        return self.client.get_organization_tenancy

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_organization_tenancy,
            tenancy_id=summary_model.tenancy_id,
            organization_id=self.module.params.get("organization_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_organization_tenancy,
            organization_id=self.module.params.get("organization_id"),
            tenancy_id=self.module.params.get("tenancy_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "organization_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_organization_tenancies, **kwargs
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_organization_tenancy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                organization_tenancy_id=self.module.params.get(
                    "organization_tenancy_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OrganizationTenancyHelperCustom = get_custom_class("OrganizationTenancyHelperCustom")


class ResourceHelper(OrganizationTenancyHelperCustom, OrganizationTenancyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            organization_tenancy_id=dict(aliases=["id"], type="str", required=True),
            state=dict(type="str", default="present", choices=["absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
