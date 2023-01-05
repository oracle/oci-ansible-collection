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
module: oci_tenant_manager_control_plane_child_tenancy
short_description: Manage a ChildTenancy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a ChildTenancy resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a child tenancy asynchronously.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The tenancy ID of the parent tenancy.
        type: str
        required: true
    tenancy_name:
        description:
            - The tenancy name to use for the child tenancy.
        type: str
        required: true
    home_region:
        description:
            - The home region to use for the child tenancy. This must be a region where the parent tenancy is subscribed.
        type: str
        required: true
    admin_email:
        description:
            - The email address of the administrator of the child tenancy.
        type: str
        required: true
    policy_name:
        description:
            - The name to use for the administrator policy in the child tenancy. Must contain only letters and underscores.
        type: str
    state:
        description:
            - The state of the ChildTenancy.
            - Use I(state=present) to create a ChildTenancy.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create child_tenancy
  oci_tenant_manager_control_plane_child_tenancy:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    tenancy_name: tenancy_name_example
    home_region: us-phoenix-1
    admin_email: admin_email_example

    # optional
    policy_name: policy_name_example

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
    from oci.tenant_manager_control_plane.models import CreateChildTenancyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ChildTenancyHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_possible_entity_types(self):
        return super(ChildTenancyHelperGen, self).get_possible_entity_types() + [
            "organizationtenancy",
            "organizationtenancies",
            "tenantManagerControlPlaneorganizationtenancy",
            "tenantManagerControlPlaneorganizationtenancies",
            "organizationtenancyresource",
            "organizationtenanciesresource",
            "childtenancy",
            "childtenancies",
            "tenantManagerControlPlanechildtenancy",
            "tenantManagerControlPlanechildtenancies",
            "childtenancyresource",
            "childtenanciesresource",
            "tenantmanagercontrolplane",
        ]

    def get_module_resource_id(self):
        return None

    # There is no idempotency for this module (no get or list ops)
    def get_matching_resource(self):
        return None

    def get_create_model_class(self):
        return CreateChildTenancyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_child_tenancy,
            call_fn_args=(),
            call_fn_kwargs=dict(create_child_tenancy_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ChildTenancyHelperCustom = get_custom_class("ChildTenancyHelperCustom")


class ResourceHelper(ChildTenancyHelperCustom, ChildTenancyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            tenancy_name=dict(type="str", required=True),
            home_region=dict(type="str", required=True),
            admin_email=dict(type="str", required=True),
            policy_name=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="child_tenancy",
        service_client_class=OrganizationClient,
        namespace="tenant_manager_control_plane",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
