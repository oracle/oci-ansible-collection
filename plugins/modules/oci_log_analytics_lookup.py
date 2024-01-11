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
module: oci_log_analytics_lookup
short_description: Manage a LogAnalyticsLookup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete a LogAnalyticsLookup resource in Oracle Cloud Infrastructure
    - "This resource has the following action operations in the M(oracle.oci.oci_log_analytics_lookup_actions) module: append_lookup_data, update_lookup_data."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    default_match_value:
        description:
            - The default match value.
            - This parameter is updatable.
        type: str
    description:
        description:
            - The lookup description.
            - This parameter is updatable.
        type: str
    fields:
        description:
            - The lookup fields.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            common_field_name:
                description:
                    - The common field name.
                    - This parameter is updatable.
                type: str
            default_match_value:
                description:
                    - The default match value.
                    - This parameter is updatable.
                type: str
            display_name:
                description:
                    - The display name.
                    - This parameter is updatable.
                type: str
                aliases: ["name"]
            is_common_field:
                description:
                    - A flag indicating whether or not the field is a common field.
                    - This parameter is updatable.
                type: bool
            match_operator:
                description:
                    - The match operator.
                    - This parameter is updatable.
                type: str
            name:
                description:
                    - The field name.
                    - This parameter is updatable.
                type: str
            position:
                description:
                    - The position.
                    - This parameter is updatable.
                type: int
    max_matches:
        description:
            - The maximum number of matches.
            - This parameter is updatable.
        type: int
    categories:
        description:
            - An array of categories to assign to the lookup. Specifying the name attribute for each category would suffice.
              Oracle-defined category assignments cannot be removed.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - The unique name that identifies the category.
                    - This parameter is updatable.
                type: str
            description:
                description:
                    - The category description.
                    - This parameter is updatable.
                type: str
            display_name:
                description:
                    - The category display name.
                    - This parameter is updatable.
                type: str
                aliases: ["name"]
            type:
                description:
                    - "The category type. Values include \\"PRODUCT\\", \\"TIER\\", \\"VENDOR\\" and \\"GENERIC\\"."
                    - This parameter is updatable.
                type: str
            is_system:
                description:
                    - The system flag. A value of false denotes a user-created
                      category. A value of true denotes an Oracle-defined category.
                    - This parameter is updatable.
                type: bool
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
    is_force:
        description:
            - is force
        type: bool
    state:
        description:
            - The state of the LogAnalyticsLookup.
            - Use I(state=present) to update an existing a LogAnalyticsLookup.
            - Use I(state=absent) to delete a LogAnalyticsLookup.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update log_analytics_lookup
  oci_log_analytics_lookup:
    # required
    namespace_name: namespace_name_example
    lookup_name: lookup_name_example

    # optional
    default_match_value: default_match_value_example
    description: description_example
    fields:
    - # optional
      common_field_name: common_field_name_example
      default_match_value: default_match_value_example
      display_name: display_name_example
      is_common_field: true
      match_operator: match_operator_example
      name: name_example
      position: 56
    max_matches: 56
    categories:
    - # optional
      name: name_example
      description: description_example
      display_name: display_name_example
      type: type_example
      is_system: true

- name: Delete log_analytics_lookup
  oci_log_analytics_lookup:
    # required
    namespace_name: namespace_name_example
    lookup_name: lookup_name_example
    state: absent

    # optional
    is_force: true

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.log_analytics import LogAnalyticsClient
    from oci.log_analytics.models import UpdateLookupMetadataDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsLookupHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(LogAnalyticsLookupHelperGen, self).get_possible_entity_types() + [
            "loganalyticslookup",
            "loganalyticslookups",
            "logAnalyticsloganalyticslookup",
            "logAnalyticsloganalyticslookups",
            "loganalyticslookupresource",
            "loganalyticslookupsresource",
            "lookup",
            "lookups",
            "logAnalyticslookup",
            "logAnalyticslookups",
            "lookupresource",
            "lookupsresource",
            "loganalytics",
        ]

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "namespace_name",
            "type",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_lookups, **kwargs)

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def get_update_model_class(self):
        return UpdateLookupMetadataDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_lookup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                lookup_name=self.module.params.get("lookup_name"),
                update_lookup_metadata_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_lookup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                lookup_name=self.module.params.get("lookup_name"),
                is_force=self.module.params.get("is_force"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


LogAnalyticsLookupHelperCustom = get_custom_class("LogAnalyticsLookupHelperCustom")


class ResourceHelper(LogAnalyticsLookupHelperCustom, LogAnalyticsLookupHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            default_match_value=dict(type="str"),
            description=dict(type="str"),
            fields=dict(
                type="list",
                elements="dict",
                options=dict(
                    common_field_name=dict(type="str"),
                    default_match_value=dict(type="str"),
                    display_name=dict(aliases=["name"], type="str"),
                    is_common_field=dict(type="bool"),
                    match_operator=dict(type="str"),
                    name=dict(type="str"),
                    position=dict(type="int"),
                ),
            ),
            max_matches=dict(type="int"),
            categories=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str"),
                    description=dict(type="str"),
                    display_name=dict(aliases=["name"], type="str"),
                    type=dict(type="str"),
                    is_system=dict(type="bool"),
                ),
            ),
            namespace_name=dict(type="str", required=True),
            lookup_name=dict(type="str", required=True),
            is_force=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
