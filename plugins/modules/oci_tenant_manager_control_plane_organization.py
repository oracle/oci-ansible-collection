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
module: oci_tenant_manager_control_plane_organization
short_description: Manage an Organization resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an Organization resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    organization_id:
        description:
            - OCID of the organization.
        type: str
        aliases: ["id"]
        required: true
    default_ucm_subscription_id:
        description:
            - OCID of the default Universal Credits Model subscription. Any tenancy joining the organization will automatically get assigned this subscription,
              if a subscription is not explictly assigned.
        type: str
        required: true
    state:
        description:
            - The state of the Organization.
            - Use I(state=present) to update an existing an Organization.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update organization
  oci_tenant_manager_control_plane_organization:
    # required
    organization_id: "ocid1.organization.oc1..xxxxxxEXAMPLExxxxxx"
    default_ucm_subscription_id: "ocid1.defaultucmsubscription.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
organization:
    description:
        - Details of the Organization resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID of the organization.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A display name for the organization. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - OCID of the compartment containing the organization. Always a tenancy OCID.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        parent_name:
            description:
                - The name of the tenancy that is the organization parent.
            returned: on success
            type: str
            sample: parent_name_example
        default_ucm_subscription_id:
            description:
                - OCID of the default Universal Credits Model subscription. Any tenancy joining the organization will automatically get assigned this
                  subscription, if a subscription is not explictly assigned.
            returned: on success
            type: str
            sample: "ocid1.defaultucmsubscription.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - Lifecycle state of the organization.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - Date and time when the organization was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Date and time when the organization was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "parent_name": "parent_name_example",
        "default_ucm_subscription_id": "ocid1.defaultucmsubscription.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
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
    from oci.tenant_manager_control_plane.models import UpdateOrganizationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OrganizationHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_possible_entity_types(self):
        return super(OrganizationHelperGen, self).get_possible_entity_types() + [
            "organization",
            "organizations",
            "tenantManagerControlPlaneorganization",
            "tenantManagerControlPlaneorganizations",
            "organizationresource",
            "organizationsresource",
            "tenantmanagercontrolplane",
        ]

    def get_module_resource_id_param(self):
        return "organization_id"

    def get_module_resource_id(self):
        return self.module.params.get("organization_id")

    def get_get_fn(self):
        return self.client.get_organization

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_organization, organization_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_organization,
            organization_id=self.module.params.get("organization_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
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
            self.client.list_organizations, **kwargs
        )

    def get_update_model_class(self):
        return UpdateOrganizationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_organization,
            call_fn_args=(),
            call_fn_kwargs=dict(
                organization_id=self.module.params.get("organization_id"),
                update_organization_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OrganizationHelperCustom = get_custom_class("OrganizationHelperCustom")


class ResourceHelper(OrganizationHelperCustom, OrganizationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            organization_id=dict(aliases=["id"], type="str", required=True),
            default_ucm_subscription_id=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="organization",
        service_client_class=OrganizationClient,
        namespace="tenant_manager_control_plane",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
