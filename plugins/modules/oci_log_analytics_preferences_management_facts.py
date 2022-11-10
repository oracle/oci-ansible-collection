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
module: oci_log_analytics_preferences_management_facts
short_description: Fetches details about one or multiple PreferencesManagement resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PreferencesManagement resources in Oracle Cloud Infrastructure
    - "Lists the preferences of the tenant. Currently, only \\"DEFAULT_HOMEPAGE\\" is supported."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The attribute used to sort the returned preferences.
        type: str
        choices:
            - "name"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List log_analytics_preference_collection
  oci_log_analytics_preferences_management_facts:
    # required
    namespace_name: namespace_name_example

    # optional
    sort_order: ASC
    sort_by: name

"""

RETURN = """
log_analytics_preference_collection:
    description:
        - List of PreferencesManagement resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - "The preference name. Currently, only \\"DEFAULT_HOMEPAGE\\" is supported."
            returned: on success
            type: str
            sample: name_example
        value:
            description:
                - The preference value.
            returned: on success
            type: str
            sample: value_example
    sample: [{
        "name": "name_example",
        "value": "value_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.log_analytics import LogAnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PreferencesManagementFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "namespace_name",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.get_preferences,
            namespace_name=self.module.params.get("namespace_name"),
            **optional_kwargs
        )


PreferencesManagementFactsHelperCustom = get_custom_class(
    "PreferencesManagementFactsHelperCustom"
)


class ResourceFactsHelper(
    PreferencesManagementFactsHelperCustom, PreferencesManagementFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["name"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="preferences_management",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(log_analytics_preference_collection=result)


if __name__ == "__main__":
    main()
