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
module: oci_logging_log_saved_search_facts
short_description: Fetches details about one or multiple LogSavedSearch resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LogSavedSearch resources in Oracle Cloud Infrastructure
    - Lists LogSavedSearches for this compartment.
    - If I(log_saved_search_id) is specified, the details of a single LogSavedSearch will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment OCID to list resources in. See compartmentIdInSubtree
                   for nested compartments traversal.
            - Required to list multiple log_saved_searches.
        type: str
    log_saved_search_id:
        description:
            - OCID of the logSavedSearch.
            - Required to get a specific log_saved_search.
        type: str
        aliases: ["id"]
    name:
        description:
            - Resource name.
        type: str
    sort_by:
        description:
            - The field to sort by (one column only). Default sort order is
              ascending exception of `timeCreated` and `timeLastModified` columns (descending).
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, whether 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific log_saved_search
  oci_logging_log_saved_search_facts:
    # required
    log_saved_search_id: "ocid1.logsavedsearch.oc1..xxxxxxEXAMPLExxxxxx"

- name: List log_saved_searches
  oci_logging_log_saved_search_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    log_saved_search_id: "ocid1.logsavedsearch.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    sort_by: timeCreated
    sort_order: ASC

"""

RETURN = """
log_saved_searches:
    description:
        - List of LogSavedSearch resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that the resource belongs to.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The user-friendly display name. This must be unique within the enclosing resource,
                  and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: name_example
        time_created:
            description:
                - Time the resource was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_modified:
            description:
                - Time the resource was last modified.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        description:
            description:
                - Description for this resource.
            returned: on success
            type: str
            sample: description_example
        query:
            description:
                - The search query that is saved.
            returned: on success
            type: str
            sample: query_example
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        lifecycle_state:
            description:
                - The state of the LogSavedSearch
            returned: on success
            type: str
            sample: CREATING
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_last_modified": "2013-10-20T19:20:30+01:00",
        "description": "description_example",
        "query": "query_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "lifecycle_state": "CREATING"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.logging import LoggingManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogSavedSearchFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "log_saved_search_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_saved_search,
            log_saved_search_id=self.module.params.get("log_saved_search_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "log_saved_search_id",
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
            self.client.list_log_saved_searches,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


LogSavedSearchFactsHelperCustom = get_custom_class("LogSavedSearchFactsHelperCustom")


class ResourceFactsHelper(
    LogSavedSearchFactsHelperCustom, LogSavedSearchFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            log_saved_search_id=dict(aliases=["id"], type="str"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="log_saved_search",
        service_client_class=LoggingManagementClient,
        namespace="logging",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(log_saved_searches=result)


if __name__ == "__main__":
    main()
