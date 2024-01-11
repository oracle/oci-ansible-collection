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
module: oci_log_analytics_lookup_facts
short_description: Fetches details about one or multiple LogAnalyticsLookup resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LogAnalyticsLookup resources in Oracle Cloud Infrastructure
    - Returns a list of lookups, containing detailed information about them. You may limit the number of results, provide sorting order, and filter by
      information such as lookup name, description and type.
    - If I(lookup_name) is specified, the details of a single LogAnalyticsLookup will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    lookup_name:
        description:
            - The name of the lookup to operate on.
            - Required to get a specific log_analytics_lookup.
        type: str
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    type:
        description:
            - The lookup type.  Valid values are Lookup or Dictionary.
            - Required to list multiple log_analytics_lookups.
        type: str
        choices:
            - "Lookup"
            - "Dictionary"
    lookup_display_text:
        description:
            - The lookup text used for filtering.  Only lookups with the specified name
              or description will be returned.
        type: str
    is_system:
        description:
            - The system value used for filtering.  Only items with the specified system value
              will be returned.  Valid values are built in, custom (for user defined items), or
              all (for all items, regardless of system value).
        type: str
        choices:
            - "ALL"
            - "CUSTOM"
            - "BUILT_IN"
    sort_by:
        description:
            - sort by field
        type: str
        choices:
            - "displayName"
            - "status"
            - "type"
            - "updatedTime"
            - "creationType"
    status:
        description:
            - The lookup status used for filtering when fetching a list of lookups.
        type: str
        choices:
            - "ALL"
            - "SUCCESSFUL"
            - "FAILED"
            - "INPROGRESS"
    categories:
        description:
            - A comma-separated list of categories used for filtering
        type: str
    is_hide_special:
        description:
            - A flag indicating whether or not to return OMC annotated or hidden lookups.
        type: bool
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: Get a specific log_analytics_lookup
  oci_log_analytics_lookup_facts:
    # required
    lookup_name: lookup_name_example
    namespace_name: namespace_name_example

- name: List log_analytics_lookups
  oci_log_analytics_lookup_facts:
    # required
    namespace_name: namespace_name_example
    type: Lookup

    # optional
    lookup_display_text: lookup_display_text_example
    is_system: ALL
    sort_by: displayName
    status: ALL
    categories: categories_example
    is_hide_special: true
    sort_order: ASC

"""

RETURN = """
log_analytics_lookups:
    description:
        - List of LogAnalyticsLookup resources
    returned: on success
    type: complex
    contains:
        active_edit_version:
            description:
                - The active edit version.
            returned: on success
            type: int
            sample: 56
        canonical_link:
            description:
                - The canonical link.
            returned: on success
            type: str
            sample: canonical_link_example
        description:
            description:
                - The lookup description.
            returned: on success
            type: str
            sample: description_example
        edit_version:
            description:
                - The edit version.
            returned: on success
            type: int
            sample: 56
        fields:
            description:
                - The lookup fields.
            returned: on success
            type: complex
            contains:
                common_field_name:
                    description:
                        - The common field name.
                    returned: on success
                    type: str
                    sample: common_field_name_example
                default_match_value:
                    description:
                        - The default match value.
                    returned: on success
                    type: str
                    sample: default_match_value_example
                display_name:
                    description:
                        - The field display name.
                    returned: on success
                    type: str
                    sample: display_name_example
                is_common_field:
                    description:
                        - A flag indicating whether or not the lookup field is a common field.
                    returned: on success
                    type: bool
                    sample: true
                match_operator:
                    description:
                        - The match operator.
                    returned: on success
                    type: str
                    sample: match_operator_example
                name:
                    description:
                        - The field name.
                    returned: on success
                    type: str
                    sample: name_example
                position:
                    description:
                        - THe field position.
                    returned: on success
                    type: int
                    sample: 56
        lookup_reference:
            description:
                - The lookup reference as an integer.
            returned: on success
            type: int
            sample: 56
        lookup_reference_string:
            description:
                - The lookup reference as a string.
            returned: on success
            type: str
            sample: lookup_reference_string_example
        type:
            description:
                - The lookup type.  Valid values are LOOKUP or DICTIONARY.
            returned: on success
            type: str
            sample: Lookup
        name:
            description:
                - The lookup name.
            returned: on success
            type: str
            sample: name_example
        is_built_in:
            description:
                - A flag indicating if the lookup is custom (user-defined) or
                  built in.
            returned: on success
            type: int
            sample: 56
        is_hidden:
            description:
                - A flag indicating if the lookup is hidden or not.  A hidden lookup will
                  not be returned in list operations by default.
            returned: on success
            type: bool
            sample: true
        lookup_display_name:
            description:
                - The lookup display name.
            returned: on success
            type: str
            sample: lookup_display_name_example
        referring_sources:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                canonical_link:
                    description:
                        - The canonical link.
                    returned: on success
                    type: str
                    sample: canonical_link_example
                total_count:
                    description:
                        - The total count.
                    returned: on success
                    type: int
                    sample: 56
        status_summary:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                chunks_processed:
                    description:
                        - The number of chunks processed.
                    returned: on success
                    type: int
                    sample: 56
                failure_details:
                    description:
                        - The failure details, if any.
                    returned: on success
                    type: str
                    sample: failure_details_example
                filename:
                    description:
                        - The filename.
                    returned: on success
                    type: str
                    sample: filename_example
                status:
                    description:
                        - The status.
                    returned: on success
                    type: str
                    sample: status_example
                total_chunks:
                    description:
                        - The total number of chunks.
                    returned: on success
                    type: int
                    sample: 56
        time_updated:
            description:
                - The last updated date.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        categories:
            description:
                - An array of categories assigned to this lookup.
                  The isSystem flag denotes if each category assignment is user-created or Oracle-defined.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The unique name that identifies the category.
                    returned: on success
                    type: str
                    sample: name_example
                description:
                    description:
                        - The category description.
                    returned: on success
                    type: str
                    sample: description_example
                display_name:
                    description:
                        - The category display name.
                    returned: on success
                    type: str
                    sample: display_name_example
                type:
                    description:
                        - "The category type. Values include \\"PRODUCT\\", \\"TIER\\", \\"VENDOR\\" and \\"GENERIC\\"."
                    returned: on success
                    type: str
                    sample: type_example
                is_system:
                    description:
                        - The system flag. A value of false denotes a user-created
                          category. A value of true denotes an Oracle-defined category.
                    returned: on success
                    type: bool
                    sample: true
    sample: [{
        "active_edit_version": 56,
        "canonical_link": "canonical_link_example",
        "description": "description_example",
        "edit_version": 56,
        "fields": [{
            "common_field_name": "common_field_name_example",
            "default_match_value": "default_match_value_example",
            "display_name": "display_name_example",
            "is_common_field": true,
            "match_operator": "match_operator_example",
            "name": "name_example",
            "position": 56
        }],
        "lookup_reference": 56,
        "lookup_reference_string": "lookup_reference_string_example",
        "type": "Lookup",
        "name": "name_example",
        "is_built_in": 56,
        "is_hidden": true,
        "lookup_display_name": "lookup_display_name_example",
        "referring_sources": {
            "canonical_link": "canonical_link_example",
            "total_count": 56
        },
        "status_summary": {
            "chunks_processed": 56,
            "failure_details": "failure_details_example",
            "filename": "filename_example",
            "status": "status_example",
            "total_chunks": 56
        },
        "time_updated": "2013-10-20T19:20:30+01:00",
        "categories": [{
            "name": "name_example",
            "description": "description_example",
            "display_name": "display_name_example",
            "type": "type_example",
            "is_system": true
        }]
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


class LogAnalyticsLookupFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
            "lookup_name",
        ]

    def get_required_params_for_list(self):
        return [
            "namespace_name",
            "type",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_lookup,
            namespace_name=self.module.params.get("namespace_name"),
            lookup_name=self.module.params.get("lookup_name"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lookup_display_text",
            "is_system",
            "sort_by",
            "status",
            "categories",
            "is_hide_special",
            "sort_order",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_lookups,
            namespace_name=self.module.params.get("namespace_name"),
            type=self.module.params.get("type"),
            **optional_kwargs
        )


LogAnalyticsLookupFactsHelperCustom = get_custom_class(
    "LogAnalyticsLookupFactsHelperCustom"
)


class ResourceFactsHelper(
    LogAnalyticsLookupFactsHelperCustom, LogAnalyticsLookupFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            lookup_name=dict(type="str"),
            namespace_name=dict(type="str", required=True),
            type=dict(type="str", choices=["Lookup", "Dictionary"]),
            lookup_display_text=dict(type="str"),
            is_system=dict(type="str", choices=["ALL", "CUSTOM", "BUILT_IN"]),
            sort_by=dict(
                type="str",
                choices=[
                    "displayName",
                    "status",
                    "type",
                    "updatedTime",
                    "creationType",
                ],
            ),
            status=dict(
                type="str", choices=["ALL", "SUCCESSFUL", "FAILED", "INPROGRESS"]
            ),
            categories=dict(type="str"),
            is_hide_special=dict(type="bool"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="log_analytics_lookup",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(log_analytics_lookups=result)


if __name__ == "__main__":
    main()
