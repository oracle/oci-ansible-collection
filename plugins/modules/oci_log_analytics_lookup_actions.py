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
module: oci_log_analytics_lookup_actions
short_description: Perform actions on a LogAnalyticsLookup resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a LogAnalyticsLookup resource in Oracle Cloud Infrastructure
    - For I(action=append_lookup_data), appends data to the lookup content. The csv file containing the content to be appended is passed in as binary data in
      the request.
    - For I(action=update_lookup_data), updates the lookup content. The csv file containing the content to be updated is passed in as binary data in the
      request.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    append_lookup_file_body:
        description:
            - The file to append.
            - Required for I(action=append_lookup_data).
        type: str
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    lookup_name:
        description:
            - The name of the lookup to operate on.
        type: str
        required: true
    update_lookup_file_body:
        description:
            - The file to use for the lookup update.
            - Required for I(action=update_lookup_data).
        type: str
    is_force:
        description:
            - is force
        type: bool
    char_encoding:
        description:
            - The character encoding of the uploaded file.
        type: str
    expect:
        description:
            - "A value of `100-continue` requests preliminary verification of the request method, path, and headers before the request body is sent.
              If no error results from such verification, the server will send a 100 (Continue) interim response to indicate readiness for the request body.
              The only allowed value for this parameter is \\"100-Continue\\" (case-insensitive)."
        type: str
    action:
        description:
            - The action to perform on the LogAnalyticsLookup.
        type: str
        required: true
        choices:
            - "append_lookup_data"
            - "update_lookup_data"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action append_lookup_data on log_analytics_lookup
  oci_log_analytics_lookup_actions:
    # required
    append_lookup_file_body: append_lookup_file_body_example
    namespace_name: namespace_name_example
    lookup_name: lookup_name_example
    action: append_lookup_data

    # optional
    is_force: true
    char_encoding: char_encoding_example
    expect: expect_example

- name: Perform action update_lookup_data on log_analytics_lookup
  oci_log_analytics_lookup_actions:
    # required
    namespace_name: namespace_name_example
    lookup_name: lookup_name_example
    update_lookup_file_body: update_lookup_file_body_example
    action: update_lookup_data

    # optional
    is_force: true
    char_encoding: char_encoding_example
    expect: expect_example

"""

RETURN = """
log_analytics_lookup:
    description:
        - Details of the LogAnalyticsLookup resource acted upon by the current operation
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
    sample: {
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
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.log_analytics import LogAnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsLookupActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        append_lookup_data
        update_lookup_data
    """

    @staticmethod
    def get_module_resource_id_param():
        return "lookup_name"

    def get_module_resource_id(self):
        return self.module.params.get("lookup_name")

    def get_get_fn(self):
        return self.client.get_lookup

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_lookup,
            namespace_name=self.module.params.get("namespace_name"),
            lookup_name=self.module.params.get("lookup_name"),
        )

    def append_lookup_data(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.append_lookup_data,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                lookup_name=self.module.params.get("lookup_name"),
                append_lookup_file_body=self.module.params.get(
                    "append_lookup_file_body"
                ),
                is_force=self.module.params.get("is_force"),
                char_encoding=self.module.params.get("char_encoding"),
                expect=self.module.params.get("expect"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def update_lookup_data(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_lookup_data,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                lookup_name=self.module.params.get("lookup_name"),
                update_lookup_file_body=self.module.params.get(
                    "update_lookup_file_body"
                ),
                is_force=self.module.params.get("is_force"),
                char_encoding=self.module.params.get("char_encoding"),
                expect=self.module.params.get("expect"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


LogAnalyticsLookupActionsHelperCustom = get_custom_class(
    "LogAnalyticsLookupActionsHelperCustom"
)


class ResourceHelper(
    LogAnalyticsLookupActionsHelperCustom, LogAnalyticsLookupActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            append_lookup_file_body=dict(type="str"),
            namespace_name=dict(type="str", required=True),
            lookup_name=dict(type="str", required=True),
            update_lookup_file_body=dict(type="str"),
            is_force=dict(type="bool"),
            char_encoding=dict(type="str"),
            expect=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=["append_lookup_data", "update_lookup_data"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="log_analytics_lookup",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
