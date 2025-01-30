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
module: oci_identity_region_facts
short_description: Fetches details about one or multiple Region resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Region resources in Oracle Cloud Infrastructure
    - Lists all the regions offered by Oracle Cloud Infrastructure.
version_added: "2.9.0"
author: Oracle (@oracle)
options: {}
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List regions
  oci_identity_region_facts:

"""

RETURN = """
regions:
    description:
        - List of Region resources
    returned: on success
    type: complex
    contains:
        key:
            description:
                - The key of the region. See L(Regions and Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm) for
                  the full list of supported 3-letter region codes.
                - "Example: `PHX`"
            returned: on success
            type: str
            sample: key_example
        name:
            description:
                - The name of the region. See L(Regions and Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm)
                  for the full list of supported region names.
                - "Example: `us-phoenix-1`"
            returned: on success
            type: str
            sample: name_example
    sample: [{
        "key": "key_example",
        "name": "name_example"
    }]
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


class RegionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

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
            self.client.list_regions, **optional_kwargs
        )


RegionFactsHelperCustom = get_custom_class("RegionFactsHelperCustom")


class ResourceFactsHelper(RegionFactsHelperCustom, RegionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(name=dict(type="str"),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="region",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(regions=result)


if __name__ == "__main__":
    main()
