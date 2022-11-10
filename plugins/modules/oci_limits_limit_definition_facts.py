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
module: oci_limits_limit_definition_facts
short_description: Fetches details about one or multiple LimitDefinition resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LimitDefinition resources in Oracle Cloud Infrastructure
    - Includes a list of resource limits that are currently supported.
      If the 'areQuotasSupported' property is true, you can create quota policies on top of this limit at the
      compartment level.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the parent compartment (remember that the tenancy is simply the root compartment).
        type: str
        required: true
    service_name:
        description:
            - The target service name.
        type: str
    name:
        description:
            - Optional field, filter for a specific resource limit.
        type: str
    sort_by:
        description:
            - The field to sort by.
        type: str
        choices:
            - "name"
            - "description"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'. By default, it is ascending.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List limit_definitions
  oci_limits_limit_definition_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    service_name: service_name_example
    name: name_example
    sort_by: name
    sort_order: ASC

"""

RETURN = """
limit_definitions:
    description:
        - List of LimitDefinition resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The resource limit name. To be used for writing policies (in case of quotas) or other programmatic calls.
            returned: on success
            type: str
            sample: name_example
        service_name:
            description:
                - The service name of the limit.
            returned: on success
            type: str
            sample: service_name_example
        description:
            description:
                - The limit description.
            returned: on success
            type: str
            sample: description_example
        scope_type:
            description:
                - Reflects the scope of the resource limit, whether Global (across all regions), regional, or availability domain-specific.
            returned: on success
            type: str
            sample: GLOBAL
        are_quotas_supported:
            description:
                - If true, quota policies can be created on top of this resource limit.
            returned: on success
            type: bool
            sample: true
        is_resource_availability_supported:
            description:
                - Reflects whether or not the GetResourceAvailability API is supported for this limit.
                  If not, the API returns an empty JSON response.
            returned: on success
            type: bool
            sample: true
        is_deprecated:
            description:
                - Indicates if the limit has been deprecated.
            returned: on success
            type: bool
            sample: true
        is_eligible_for_limit_increase:
            description:
                - Indicates if the customer can request a limit increase for this resource.
            returned: on success
            type: bool
            sample: true
        is_dynamic:
            description:
                - The limit for this resource has a dynamic value that is based on consumption across all OCI services.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "name": "name_example",
        "service_name": "service_name_example",
        "description": "description_example",
        "scope_type": "GLOBAL",
        "are_quotas_supported": true,
        "is_resource_availability_supported": true,
        "is_deprecated": true,
        "is_eligible_for_limit_increase": true,
        "is_dynamic": true
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.limits import LimitsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LimitDefinitionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "service_name",
            "name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_limit_definitions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


LimitDefinitionFactsHelperCustom = get_custom_class("LimitDefinitionFactsHelperCustom")


class ResourceFactsHelper(
    LimitDefinitionFactsHelperCustom, LimitDefinitionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            service_name=dict(type="str"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["name", "description"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="limit_definition",
        service_client_class=LimitsClient,
        namespace="limits",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(limit_definitions=result)


if __name__ == "__main__":
    main()
