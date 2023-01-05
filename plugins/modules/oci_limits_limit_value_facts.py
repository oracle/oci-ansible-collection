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
module: oci_limits_limit_value_facts
short_description: Fetches details about one or multiple LimitValue resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LimitValue resources in Oracle Cloud Infrastructure
    - Includes a full list of resource limits belonging to a given service.
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
        required: true
    scope_type:
        description:
            - Filter entries by scope type.
        type: str
        choices:
            - "GLOBAL"
            - "REGION"
            - "AD"
    availability_domain:
        description:
            - Filter entries by availability domain. This implies that only AD-specific values are returned.
        type: str
    name:
        description:
            - Optional field, can be used to see a specific resource limit value.
        type: str
    sort_by:
        description:
            - The field to sort by. The sorting is by availabilityDomain, as a second level field, if available.
        type: str
        choices:
            - "name"
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
- name: List limit_values
  oci_limits_limit_value_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    service_name: service_name_example

    # optional
    scope_type: GLOBAL
    availability_domain: Uocm:PHX-AD-1
    name: name_example
    sort_by: name
    sort_order: ASC

"""

RETURN = """
limit_values:
    description:
        - List of LimitValue resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The resource limit name. To be used for writing policies (in case of quotas) or other programmatic calls.
            returned: on success
            type: str
            sample: name_example
        scope_type:
            description:
                - The scope type of the limit.
            returned: on success
            type: str
            sample: GLOBAL
        availability_domain:
            description:
                - If present, the returned value is only specific to this availability domain.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        value:
            description:
                - The resource limit value.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "name": "name_example",
        "scope_type": "GLOBAL",
        "availability_domain": "Uocm:PHX-AD-1",
        "value": 56
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


class LimitValueFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "service_name",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "scope_type",
            "availability_domain",
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
            self.client.list_limit_values,
            compartment_id=self.module.params.get("compartment_id"),
            service_name=self.module.params.get("service_name"),
            **optional_kwargs
        )


LimitValueFactsHelperCustom = get_custom_class("LimitValueFactsHelperCustom")


class ResourceFactsHelper(LimitValueFactsHelperCustom, LimitValueFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            service_name=dict(type="str", required=True),
            scope_type=dict(type="str", choices=["GLOBAL", "REGION", "AD"]),
            availability_domain=dict(type="str"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["name"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="limit_value",
        service_client_class=LimitsClient,
        namespace="limits",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(limit_values=result)


if __name__ == "__main__":
    main()
