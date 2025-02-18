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
module: oci_functions_triggers_facts
short_description: Fetches details about one or multiple Triggers resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Triggers resources in Oracle Cloud Infrastructure
    - Returns a list of Triggers.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - A filter to return only resources that match the service trigger source of a PBF.
        type: str
    sort_order:
        description:
            - Specifies sort order.
            - "* **ASC:** Ascending sort order.
              * **DESC:** Descending sort order."
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List triggers
  oci_functions_triggers_facts:

    # optional
    name: name_example
    sort_order: ASC

"""

RETURN = """
triggers:
    description:
        - List of Triggers resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - A brief descriptive name for the PBF trigger.
            returned: on success
            type: str
            sample: name_example
    sample: [{
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
    from oci.functions import FunctionsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TriggersFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_triggers, **optional_kwargs
        )


TriggersFactsHelperCustom = get_custom_class("TriggersFactsHelperCustom")


class ResourceFactsHelper(TriggersFactsHelperCustom, TriggersFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            name=dict(type="str"), sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="triggers",
        service_client_class=FunctionsManagementClient,
        namespace="functions",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(triggers=result)


if __name__ == "__main__":
    main()
