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
module: oci_tenant_manager_control_plane_organization_tenancy_facts
short_description: Fetches details about one or multiple OrganizationTenancy resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OrganizationTenancy resources in Oracle Cloud Infrastructure
    - Gets a list of tenancies in the organization.
    - If I(tenancy_id) is specified, the details of a single OrganizationTenancy will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    tenancy_id:
        description:
            - OCID of the tenancy to retrieve.
            - Required to get a specific organization_tenancy.
        type: str
        aliases: ["id"]
    organization_id:
        description:
            - OCID of the organization.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: Get a specific organization_tenancy
  oci_tenant_manager_control_plane_organization_tenancy_facts:
    # required
    tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
    organization_id: "ocid1.organization.oc1..xxxxxxEXAMPLExxxxxx"

- name: List organization_tenancies
  oci_tenant_manager_control_plane_organization_tenancy_facts:
    # required
    organization_id: "ocid1.organization.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
organization_tenancies:
    description:
        - List of OrganizationTenancy resources
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
    sample: [{
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "lifecycle_state": "CREATING",
        "role": "PARENT",
        "time_joined": "2013-10-20T19:20:30+01:00",
        "time_left": "2013-10-20T19:20:30+01:00",
        "is_approved_for_transfer": true,
        "governance_status": "OPTED_IN"
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


class OrganizationTenancyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "organization_id",
            "tenancy_id",
        ]

    def get_required_params_for_list(self):
        return [
            "organization_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_organization_tenancy,
            organization_id=self.module.params.get("organization_id"),
            tenancy_id=self.module.params.get("tenancy_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_organization_tenancies,
            organization_id=self.module.params.get("organization_id"),
            **optional_kwargs
        )


OrganizationTenancyFactsHelperCustom = get_custom_class(
    "OrganizationTenancyFactsHelperCustom"
)


class ResourceFactsHelper(
    OrganizationTenancyFactsHelperCustom, OrganizationTenancyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            tenancy_id=dict(aliases=["id"], type="str"),
            organization_id=dict(type="str", required=True),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="organization_tenancy",
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

    module.exit_json(organization_tenancies=result)


if __name__ == "__main__":
    main()
