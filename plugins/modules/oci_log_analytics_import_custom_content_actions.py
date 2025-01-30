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
module: oci_log_analytics_import_custom_content_actions
short_description: Perform actions on an ImportCustomContent resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an ImportCustomContent resource in Oracle Cloud Infrastructure
    - For I(action=import_custom_content), imports the specified custom content from the input in zip format.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    import_custom_content_file_body_input_file:
        description:
            - The file to upload which contains the custom content.
        type: str
        required: true
    is_overwrite:
        description:
            - A flag indicating whether or not to overwrite existing content if a conflict is
              found during import content operation.
        type: bool
    expect:
        description:
            - "A value of `100-continue` requests preliminary verification of the request method, path, and headers before the request body is sent.
              If no error results from such verification, the server will send a 100 (Continue) interim response to indicate readiness for the request body.
              The only allowed value for this parameter is \\"100-Continue\\" (case-insensitive)."
        type: str
    action:
        description:
            - The action to perform on the ImportCustomContent.
        type: str
        required: true
        choices:
            - "import_custom_content"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action import_custom_content on import_custom_content
  oci_log_analytics_import_custom_content_actions:
    # required
    namespace_name: namespace_name_example
    import_custom_content_file_body_input_file: import_custom_content_file_body_input_file_example
    action: import_custom_content

    # optional
    is_overwrite: true
    expect: expect_example

"""

RETURN = """
import_custom_content:
    description:
        - Details of the ImportCustomContent resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        parser_names:
            description:
                - The parser names.
            returned: on success
            type: list
            sample: []
        source_names:
            description:
                - The source names.
            returned: on success
            type: list
            sample: []
        field_names:
            description:
                - The field names.
            returned: on success
            type: list
            sample: []
        change_list:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                created_parser_names:
                    description:
                        - An array of created parser names.
                    returned: on success
                    type: list
                    sample: []
                updated_parser_names:
                    description:
                        - An array of updated parser names.
                    returned: on success
                    type: list
                    sample: []
                created_source_names:
                    description:
                        - An array of created source names.
                    returned: on success
                    type: list
                    sample: []
                updated_source_names:
                    description:
                        - An array of updated source names.
                    returned: on success
                    type: list
                    sample: []
                created_field_display_names:
                    description:
                        - An array of created field display names.
                    returned: on success
                    type: list
                    sample: []
                updated_field_display_names:
                    description:
                        - An array of updated field display names.
                    returned: on success
                    type: list
                    sample: []
                conflict_parser_names:
                    description:
                        - A list of parser names with conflicts.
                    returned: on success
                    type: list
                    sample: []
                conflict_source_names:
                    description:
                        - A list of source names with conflicts.
                    returned: on success
                    type: list
                    sample: []
                conflict_field_display_names:
                    description:
                        - A list of field display names with conflicts.
                    returned: on success
                    type: list
                    sample: []
        content_name:
            description:
                - The content name.
            returned: on success
            type: str
            sample: content_name_example
    sample: {
        "parser_names": [],
        "source_names": [],
        "field_names": [],
        "change_list": {
            "created_parser_names": [],
            "updated_parser_names": [],
            "created_source_names": [],
            "updated_source_names": [],
            "created_field_display_names": [],
            "updated_field_display_names": [],
            "conflict_parser_names": [],
            "conflict_source_names": [],
            "conflict_field_display_names": []
        },
        "content_name": "content_name_example"
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


class ImportCustomContentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        import_custom_content
    """

    @staticmethod
    def get_module_resource_id_param():
        return "namespace_name"

    def get_module_resource_id(self):
        return self.module.params.get("namespace_name")

    def import_custom_content(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.import_custom_content,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                import_custom_content_file_body=self.module.params.get(
                    "import_custom_content_file_body"
                ),
                is_overwrite=self.module.params.get("is_overwrite"),
                expect=self.module.params.get("expect"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


ImportCustomContentActionsHelperCustom = get_custom_class(
    "ImportCustomContentActionsHelperCustom"
)


class ResourceHelper(
    ImportCustomContentActionsHelperCustom, ImportCustomContentActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            import_custom_content_file_body_input_file=dict(type="str", required=True),
            is_overwrite=dict(type="bool"),
            expect=dict(type="str"),
            action=dict(type="str", required=True, choices=["import_custom_content"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="import_custom_content",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
