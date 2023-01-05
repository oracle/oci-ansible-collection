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
module: oci_apm_traces_quick_pick_facts
short_description: Fetches details about one or multiple QuickPick resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple QuickPick resources in Oracle Cloud Infrastructure
    - Returns a list of predefined Quick Pick queries intended to assist the user
      to choose a query to run.  There is no sorting applied on the results.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    apm_domain_id:
        description:
            - The APM Domain ID the request is intended for.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List quick_picks
  oci_apm_traces_quick_pick_facts:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
quick_picks:
    description:
        - List of QuickPick resources
    returned: on success
    type: complex
    contains:
        quick_pick_name:
            description:
                - Quick Pick name for the query.
            returned: on success
            type: str
            sample: quick_pick_name_example
        quick_pick_query:
            description:
                - Query for the Quick Pick.
            returned: on success
            type: str
            sample: quick_pick_query_example
    sample: [{
        "quick_pick_name": "quick_pick_name_example",
        "quick_pick_query": "quick_pick_query_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.apm_traces import QueryClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class QuickPickFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "apm_domain_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_quick_picks,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            **optional_kwargs
        )


QuickPickFactsHelperCustom = get_custom_class("QuickPickFactsHelperCustom")


class ResourceFactsHelper(QuickPickFactsHelperCustom, QuickPickFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(apm_domain_id=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="quick_pick",
        service_client_class=QueryClient,
        namespace="apm_traces",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(quick_picks=result)


if __name__ == "__main__":
    main()
