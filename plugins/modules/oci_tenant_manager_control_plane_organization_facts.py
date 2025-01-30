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
module: oci_tenant_manager_control_plane_organization_facts
short_description: Fetches details about one or multiple Organization resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Organization resources in Oracle Cloud Infrastructure
    - Lists organizations associated with the caller.
    - If I(organization_id) is specified, the details of a single Organization will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    organization_id:
        description:
            - OCID of the organization to retrieve.
            - Required to get a specific organization.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple organizations.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific organization
  oci_tenant_manager_control_plane_organization_facts:
    # required
    organization_id: "ocid1.organization.oc1..xxxxxxEXAMPLExxxxxx"

- name: List organizations
  oci_tenant_manager_control_plane_organization_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
organizations:
    description:
        - List of Organization resources
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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "parent_name": "parent_name_example",
        "default_ucm_subscription_id": "ocid1.defaultucmsubscription.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.tenant_manager_control_plane import OrganizationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OrganizationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "organization_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_organization,
            organization_id=self.module.params.get("organization_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_organizations,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OrganizationFactsHelperCustom = get_custom_class("OrganizationFactsHelperCustom")


class ResourceFactsHelper(OrganizationFactsHelperCustom, OrganizationFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            organization_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="organization",
        service_client_class=OrganizationClient,
        namespace="tenant_manager_control_plane",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(organizations=result)


if __name__ == "__main__":
    main()
