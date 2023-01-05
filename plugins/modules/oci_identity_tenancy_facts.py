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
module: oci_identity_tenancy_facts
short_description: Fetches details about a Tenancy resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Tenancy resource in Oracle Cloud Infrastructure
    - Get the specified tenancy's information.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    tenancy_id:
        description:
            - The OCID of the tenancy.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: Get a specific tenancy
  oci_identity_tenancy_facts:
    # required
    tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
tenancy:
    description:
        - Tenancy resource
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the tenancy.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the tenancy.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - The description of the tenancy.
            returned: on success
            type: str
            sample: description_example
        home_region_key:
            description:
                - The region key for the tenancy's home region. For the full list of supported regions, see
                  L(Regions and Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm).
                - "Example: `PHX`"
            returned: on success
            type: str
            sample: home_region_key_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "home_region_key": "home_region_key_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TenancyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "tenancy_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tenancy, tenancy_id=self.module.params.get("tenancy_id"),
        )


TenancyFactsHelperCustom = get_custom_class("TenancyFactsHelperCustom")


class ResourceFactsHelper(TenancyFactsHelperCustom, TenancyFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            tenancy_id=dict(aliases=["id"], type="str", required=True),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="tenancy",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(tenancy=result)


if __name__ == "__main__":
    main()
