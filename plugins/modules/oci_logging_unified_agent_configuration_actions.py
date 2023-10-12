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
module: oci_logging_unified_agent_configuration_actions
short_description: Perform actions on an UnifiedAgentConfiguration resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an UnifiedAgentConfiguration resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the unified agent configuration into a different compartment within the same tenancy.  When provided, the If-Match
      is checked against the ETag values of the resource.
      For information about moving resources between compartments, see L(Moving Resources Between
      Compartments,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    unified_agent_configuration_id:
        description:
            - The OCID of the Unified Agent configuration.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The OCID the compartment into which the resource should be moved.
        type: str
    action:
        description:
            - The action to perform on the UnifiedAgentConfiguration.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on unified_agent_configuration
  oci_logging_unified_agent_configuration_actions:
    # required
    unified_agent_configuration_id: "ocid1.unifiedagentconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
unified_agent_configuration:
    description:
        - Details of the UnifiedAgentConfiguration resource acted upon by the current operation
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
        display_name:
            description:
                - The user-friendly display name. This must be unique within the enclosing resource,
                  and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description for this resource.
            returned: on success
            type: str
            sample: description_example
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
        lifecycle_state:
            description:
                - The pipeline state.
            returned: on success
            type: str
            sample: CREATING
        is_enabled:
            description:
                - Whether or not this resource is currently enabled.
            returned: on success
            type: bool
            sample: true
        configuration_state:
            description:
                - State of unified agent service configuration.
            returned: on success
            type: str
            sample: VALID
        service_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                configuration_type:
                    description:
                        - Type of Unified Agent service configuration.
                    returned: on success
                    type: str
                    sample: LOGGING
                sources:
                    description:
                        - Logging source object.
                    returned: on success
                    type: complex
                    contains:
                        paths:
                            description:
                                - Absolute paths for log source files. Wildcard can be used.
                            returned: on success
                            type: list
                            sample: []
                        parser:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                is_merge_cri_fields:
                                    description:
                                        - If you don't need stream/logtag fields, set this to false.
                                    returned: on success
                                    type: bool
                                    sample: true
                                nested_parser:
                                    description:
                                        - Optional nested JSON Parser for CRI Parser. Supported fields are fieldTimeKey, timeFormat, and isKeepTimeKey.
                                    returned: on success
                                    type: complex
                                    contains:
                                        parser_type:
                                            description:
                                                - Type of fluent parser.
                                            returned: on success
                                            type: str
                                            sample: AUDITD
                                        field_time_key:
                                            description:
                                                - Specify time field for the event time. If the event doesn't have this field, the current time is used.
                                            returned: on success
                                            type: str
                                            sample: field_time_key_example
                                        types:
                                            description:
                                                - "Specify types for converting a field into another type.
                                                  For example,
                                                    With this configuration:
                                                        <parse>
                                                          @type csv
                                                          keys time,host,req_id,user
                                                          time_key time
                                                        </parse>"
                                                - " This incoming event:
                                                      \\"2013/02/28 12:00:00,192.168.0.1,111,-\\""
                                                - " is parsed as:
                                                      1362020400 (2013/02/28/ 12:00:00)"
                                                - |
                                                  "   record:
                                                      {
                                                        \\"host\\"   : \\"192.168.0.1\\",
                                                        \\"req_id\\" : \\"111\\",
                                                        \\"user\\"   : \\"-\\"
                                                      }"
                                            returned: on success
                                            type: dict
                                            sample: {}
                                        null_value_pattern:
                                            description:
                                                - Specify the null value pattern.
                                            returned: on success
                                            type: str
                                            sample: null_value_pattern_example
                                        is_null_empty_string:
                                            description:
                                                - If true, an empty string field is replaced with nil.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        is_estimate_current_event:
                                            description:
                                                - If true, use Fluent::EventTime.now(current time) as a timestamp when time_key is specified.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        is_keep_time_key:
                                            description:
                                                - If true, keep time field in the record.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        timeout_in_milliseconds:
                                            description:
                                                - Specify the timeout for parse processing. This is mainly for detecting an incorrect regexp pattern.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        time_type:
                                            description:
                                                - Time type of JSON parser.
                                            returned: on success
                                            type: str
                                            sample: FLOAT
                                        time_format:
                                            description:
                                                - Process time value using the specified format.
                                            returned: on success
                                            type: str
                                            sample: time_format_example
                                time_type:
                                    description:
                                        - Time type of JSON parser.
                                    returned: on success
                                    type: str
                                    sample: FLOAT
                                format_firstline:
                                    description:
                                        - First line pattern format.
                                    returned: on success
                                    type: str
                                    sample: format_firstline_example
                                format:
                                    description:
                                        - Mutiline pattern format.
                                    returned: on success
                                    type: list
                                    sample: []
                                grok_name_key:
                                    description:
                                        - grok name key.
                                    returned: on success
                                    type: str
                                    sample: grok_name_key_example
                                grok_failure_key:
                                    description:
                                        - grok failure key.
                                    returned: on success
                                    type: str
                                    sample: grok_failure_key_example
                                multi_line_start_regexp:
                                    description:
                                        - Multiline start regexp pattern.
                                    returned: on success
                                    type: str
                                    sample: multi_line_start_regexp_example
                                patterns:
                                    description:
                                        - grok pattern object.
                                    returned: on success
                                    type: complex
                                    contains:
                                        pattern:
                                            description:
                                                - The grok pattern.
                                            returned: on success
                                            type: str
                                            sample: pattern_example
                                        name:
                                            description:
                                                - The name key to tag this grok pattern.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        field_time_key:
                                            description:
                                                - Specify the time field for the event time. If the event doesn't have this field, the current time is used.
                                            returned: on success
                                            type: str
                                            sample: field_time_key_example
                                        field_time_format:
                                            description:
                                                - Process value using the specified format. This is available only when time_type is a string.
                                            returned: on success
                                            type: str
                                            sample: field_time_format_example
                                        field_time_zone:
                                            description:
                                                - Use the specified time zone. The time value can be parsed or formatted in the specified time zone.
                                            returned: on success
                                            type: str
                                            sample: field_time_zone_example
                                message_key:
                                    description:
                                        - Specifies the field name to contain logs.
                                    returned: on success
                                    type: str
                                    sample: message_key_example
                                expression:
                                    description:
                                        - Regex pattern.
                                    returned: on success
                                    type: str
                                    sample: expression_example
                                time_format:
                                    description:
                                        - Process time value using the specified format.
                                    returned: on success
                                    type: str
                                    sample: time_format_example
                                rfc5424_time_format:
                                    description:
                                        - rfc5424 time format.
                                    returned: on success
                                    type: str
                                    sample: rfc5424_time_format_example
                                message_format:
                                    description:
                                        - Message format of syslog.
                                    returned: on success
                                    type: str
                                    sample: RFC3164
                                is_with_priority:
                                    description:
                                        - With priority or not.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_support_colonless_ident:
                                    description:
                                        - Support colonless ident or not.
                                    returned: on success
                                    type: bool
                                    sample: true
                                syslog_parser_type:
                                    description:
                                        - Syslog parser type.
                                    returned: on success
                                    type: str
                                    sample: STRING
                                parser_type:
                                    description:
                                        - Type of fluent parser.
                                    returned: on success
                                    type: str
                                    sample: AUDITD
                                field_time_key:
                                    description:
                                        - Specify time field for the event time. If the event doesn't have this field, the current time is used.
                                    returned: on success
                                    type: str
                                    sample: field_time_key_example
                                types:
                                    description:
                                        - "Specify types for converting a field into another type.
                                          For example,
                                            With this configuration:
                                                <parse>
                                                  @type csv
                                                  keys time,host,req_id,user
                                                  time_key time
                                                </parse>"
                                        - " This incoming event:
                                              \\"2013/02/28 12:00:00,192.168.0.1,111,-\\""
                                        - " is parsed as:
                                              1362020400 (2013/02/28/ 12:00:00)"
                                        - |
                                          "   record:
                                              {
                                                \\"host\\"   : \\"192.168.0.1\\",
                                                \\"req_id\\" : \\"111\\",
                                                \\"user\\"   : \\"-\\"
                                              }"
                                    returned: on success
                                    type: dict
                                    sample: {}
                                null_value_pattern:
                                    description:
                                        - Specify the null value pattern.
                                    returned: on success
                                    type: str
                                    sample: null_value_pattern_example
                                is_null_empty_string:
                                    description:
                                        - If true, an empty string field is replaced with nil.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_estimate_current_event:
                                    description:
                                        - If true, use Fluent::EventTime.now(current time) as a timestamp when time_key is specified.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_keep_time_key:
                                    description:
                                        - If true, keep time field in the record.
                                    returned: on success
                                    type: bool
                                    sample: true
                                timeout_in_milliseconds:
                                    description:
                                        - Specify the timeout for parse processing. This is mainly for detecting an incorrect regexp pattern.
                                    returned: on success
                                    type: int
                                    sample: 56
                                delimiter:
                                    description:
                                        - csv delimiter.
                                    returned: on success
                                    type: str
                                    sample: delimiter_example
                                keys:
                                    description:
                                        - csv keys.
                                    returned: on success
                                    type: list
                                    sample: []
                        name:
                            description:
                                - unique name for the source
                            returned: on success
                            type: str
                            sample: name_example
                        source_type:
                            description:
                                - Unified schema logging source type.
                            returned: on success
                            type: str
                            sample: LOG_TAIL
                        channels:
                            description:
                                - Windows event log channels.
                            returned: on success
                            type: list
                            sample: []
                destination:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        log_object_id:
                            description:
                                - The OCID of the resource.
                            returned: on success
                            type: str
                            sample: "ocid1.logobject.oc1..xxxxxxEXAMPLExxxxxx"
        group_association:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                group_list:
                    description:
                        - list of group/dynamic group ids associated with this configuration.
                    returned: on success
                    type: list
                    sample: []
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_last_modified": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "is_enabled": true,
        "configuration_state": "VALID",
        "service_configuration": {
            "configuration_type": "LOGGING",
            "sources": [{
                "paths": [],
                "parser": {
                    "is_merge_cri_fields": true,
                    "nested_parser": {
                        "parser_type": "AUDITD",
                        "field_time_key": "field_time_key_example",
                        "types": {},
                        "null_value_pattern": "null_value_pattern_example",
                        "is_null_empty_string": true,
                        "is_estimate_current_event": true,
                        "is_keep_time_key": true,
                        "timeout_in_milliseconds": 56,
                        "time_type": "FLOAT",
                        "time_format": "time_format_example"
                    },
                    "time_type": "FLOAT",
                    "format_firstline": "format_firstline_example",
                    "format": [],
                    "grok_name_key": "grok_name_key_example",
                    "grok_failure_key": "grok_failure_key_example",
                    "multi_line_start_regexp": "multi_line_start_regexp_example",
                    "patterns": [{
                        "pattern": "pattern_example",
                        "name": "name_example",
                        "field_time_key": "field_time_key_example",
                        "field_time_format": "field_time_format_example",
                        "field_time_zone": "field_time_zone_example"
                    }],
                    "message_key": "message_key_example",
                    "expression": "expression_example",
                    "time_format": "time_format_example",
                    "rfc5424_time_format": "rfc5424_time_format_example",
                    "message_format": "RFC3164",
                    "is_with_priority": true,
                    "is_support_colonless_ident": true,
                    "syslog_parser_type": "STRING",
                    "parser_type": "AUDITD",
                    "field_time_key": "field_time_key_example",
                    "types": {},
                    "null_value_pattern": "null_value_pattern_example",
                    "is_null_empty_string": true,
                    "is_estimate_current_event": true,
                    "is_keep_time_key": true,
                    "timeout_in_milliseconds": 56,
                    "delimiter": "delimiter_example",
                    "keys": []
                },
                "name": "name_example",
                "source_type": "LOG_TAIL",
                "channels": []
            }],
            "destination": {
                "log_object_id": "ocid1.logobject.oc1..xxxxxxEXAMPLExxxxxx"
            }
        },
        "group_association": {
            "group_list": []
        }
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
    from oci.logging import LoggingManagementClient
    from oci.logging.models import ChangeUnifiedAgentConfigurationCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UnifiedAgentConfigurationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "unified_agent_configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("unified_agent_configuration_id")

    def get_get_fn(self):
        return self.client.get_unified_agent_configuration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_unified_agent_configuration,
            unified_agent_configuration_id=self.module.params.get(
                "unified_agent_configuration_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeUnifiedAgentConfigurationCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_unified_agent_configuration_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                unified_agent_configuration_id=self.module.params.get(
                    "unified_agent_configuration_id"
                ),
                change_unified_agent_configuration_compartment_details=action_details,
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


UnifiedAgentConfigurationActionsHelperCustom = get_custom_class(
    "UnifiedAgentConfigurationActionsHelperCustom"
)


class ResourceHelper(
    UnifiedAgentConfigurationActionsHelperCustom,
    UnifiedAgentConfigurationActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            unified_agent_configuration_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="unified_agent_configuration",
        service_client_class=LoggingManagementClient,
        namespace="logging",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
