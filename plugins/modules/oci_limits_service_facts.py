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
module: oci_limits_service_facts
short_description: Fetches details about one or multiple Service resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Service resources in Oracle Cloud Infrastructure
    - Returns the list of supported services.
      This includes the programmatic service name, along with the friendly service name.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the parent compartment (remember that the tenancy is simply the root compartment).
        type: str
        required: true
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
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List services
  oci_limits_service_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: name
    sort_order: ASC

"""

RETURN = """
services:
    description:
        - List of Service resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The service name. Use this when calling other APIs.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - The friendly service name.
            returned: on success
            type: str
            sample: description_example
    sample: [{
        "name": "name_example",
        "description": "description_example"
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


class ServiceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_services,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ServiceFactsHelperCustom = get_custom_class("ServiceFactsHelperCustom")


class ResourceFactsHelper(ServiceFactsHelperCustom, ServiceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["name", "description"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="service",
        service_client_class=LimitsClient,
        namespace="limits",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(services=result)


if __name__ == "__main__":
    main()
