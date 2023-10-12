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
module: oci_logging_unified_agent_configuration
short_description: Manage an UnifiedAgentConfiguration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an UnifiedAgentConfiguration resource in Oracle Cloud Infrastructure
    - For I(state=present), create unified agent configuration registration.
    - "This resource has the following action operations in the M(oracle.oci.oci_logging_unified_agent_configuration_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment that the resource belongs to.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - The user-friendly display name. This must be unique within the enclosing resource,
              and it's changeable. Avoid entering confidential information.
            - Required for update using I(state=present) with unified_agent_configuration_id present.
            - Required for create, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    is_enabled:
        description:
            - Whether or not this resource is currently enabled.
            - Required for create using I(state=present), update using I(state=present) with unified_agent_configuration_id present.
        type: bool
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    description:
        description:
            - Description for this resource.
            - This parameter is updatable.
        type: str
    service_configuration:
        description:
            - ""
            - Required for create using I(state=present), update using I(state=present) with unified_agent_configuration_id present.
        type: dict
        suboptions:
            configuration_type:
                description:
                    - Type of Unified Agent service configuration.
                type: str
                choices:
                    - "LOGGING"
                required: true
            sources:
                description:
                    - Logging source object.
                type: list
                elements: dict
                required: true
                suboptions:
                    channels:
                        description:
                            - Windows event log channels.
                            - Required when source_type is 'WINDOWS_EVENT_LOG'
                        type: list
                        elements: str
                    name:
                        description:
                            - unique name for the source
                        type: str
                        required: true
                    source_type:
                        description:
                            - Unified schema logging source type.
                        type: str
                        choices:
                            - "WINDOWS_EVENT_LOG"
                            - "LOG_TAIL"
                        required: true
                    paths:
                        description:
                            - Absolute paths for log source files. Wildcard can be used.
                            - Required when source_type is 'LOG_TAIL'
                        type: list
                        elements: str
                    parser:
                        description:
                            - ""
                            - Applicable when source_type is 'LOG_TAIL'
                        type: dict
                        suboptions:
                            multi_line_start_regexp:
                                description:
                                    - Multiline start regexp pattern.
                                    - Applicable when parser_type is 'MULTILINE_GROK'
                                type: str
                            time_type:
                                description:
                                    - Time type of JSON parser.
                                    - Applicable when parser_type is 'JSON'
                                type: str
                                choices:
                                    - "FLOAT"
                                    - "UNIXTIME"
                                    - "STRING"
                            grok_name_key:
                                description:
                                    - grok name key.
                                    - Applicable when parser_type is one of ['GROK', 'MULTILINE_GROK']
                                type: str
                            grok_failure_key:
                                description:
                                    - grok failure key.
                                    - Applicable when parser_type is one of ['GROK', 'MULTILINE_GROK']
                                type: str
                            patterns:
                                description:
                                    - grok pattern object.
                                    - Required when parser_type is one of ['GROK', 'MULTILINE_GROK']
                                type: list
                                elements: dict
                                suboptions:
                                    pattern:
                                        description:
                                            - The grok pattern.
                                            - Required when parser_type is 'MULTILINE_GROK'
                                        type: str
                                        required: true
                                    name:
                                        description:
                                            - The name key to tag this grok pattern.
                                            - Applicable when parser_type is 'MULTILINE_GROK'
                                        type: str
                                    field_time_key:
                                        description:
                                            - Specify the time field for the event time. If the event doesn't have this field, the current time is used.
                                            - Applicable when parser_type is 'MULTILINE_GROK'
                                        type: str
                                    field_time_format:
                                        description:
                                            - Process value using the specified format. This is available only when time_type is a string.
                                            - Applicable when parser_type is 'MULTILINE_GROK'
                                        type: str
                                    field_time_zone:
                                        description:
                                            - Use the specified time zone. The time value can be parsed or formatted in the specified time zone.
                                            - Applicable when parser_type is 'MULTILINE_GROK'
                                        type: str
                            message_key:
                                description:
                                    - Specifies the field name to contain logs.
                                    - Applicable when parser_type is 'NONE'
                                type: str
                            rfc5424_time_format:
                                description:
                                    - rfc5424 time format.
                                    - Applicable when parser_type is 'SYSLOG'
                                type: str
                            message_format:
                                description:
                                    - Message format of syslog.
                                    - Applicable when parser_type is 'SYSLOG'
                                type: str
                                choices:
                                    - "RFC3164"
                                    - "RFC5424"
                                    - "AUTO"
                            is_with_priority:
                                description:
                                    - With priority or not.
                                    - Applicable when parser_type is 'SYSLOG'
                                type: bool
                            is_support_colonless_ident:
                                description:
                                    - Support colonless ident or not.
                                    - Applicable when parser_type is 'SYSLOG'
                                type: bool
                            syslog_parser_type:
                                description:
                                    - Syslog parser type.
                                    - Applicable when parser_type is 'SYSLOG'
                                type: str
                                choices:
                                    - "STRING"
                                    - "REGEXP"
                            expression:
                                description:
                                    - Regex pattern.
                                    - Required when parser_type is 'REGEXP'
                                type: str
                            time_format:
                                description:
                                    - Process time value using the specified format.
                                    - Applicable when parser_type is one of ['REGEXP', 'SYSLOG', 'JSON']
                                type: str
                            format_firstline:
                                description:
                                    - First line pattern format.
                                    - Applicable when parser_type is 'MULTILINE'
                                type: str
                            format:
                                description:
                                    - Mutiline pattern format.
                                    - Required when parser_type is 'MULTILINE'
                                type: list
                                elements: str
                            is_merge_cri_fields:
                                description:
                                    - If you don't need stream/logtag fields, set this to false.
                                    - Applicable when parser_type is 'CRI'
                                type: bool
                            nested_parser:
                                description:
                                    - Optional nested JSON Parser for CRI Parser. Supported fields are fieldTimeKey, timeFormat, and isKeepTimeKey.
                                    - Applicable when parser_type is 'CRI'
                                type: dict
                                suboptions:
                                    parser_type:
                                        description:
                                            - Type of fluent parser.
                                            - Required when parser_type is 'CRI'
                                        type: str
                                        choices:
                                            - "AUDITD"
                                            - "CRI"
                                            - "JSON"
                                            - "TSV"
                                            - "CSV"
                                            - "NONE"
                                            - "SYSLOG"
                                            - "APACHE2"
                                            - "APACHE_ERROR"
                                            - "MSGPACK"
                                            - "REGEXP"
                                            - "MULTILINE"
                                            - "GROK"
                                            - "MULTILINE_GROK"
                                        required: true
                                    field_time_key:
                                        description:
                                            - Specify time field for the event time. If the event doesn't have this field, the current time is used.
                                            - Applicable when parser_type is 'CRI'
                                        type: str
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
                                            - Applicable when parser_type is 'CRI'
                                        type: dict
                                    null_value_pattern:
                                        description:
                                            - Specify the null value pattern.
                                            - Applicable when parser_type is 'CRI'
                                        type: str
                                    is_null_empty_string:
                                        description:
                                            - If true, an empty string field is replaced with nil.
                                            - Applicable when parser_type is 'CRI'
                                        type: bool
                                    is_estimate_current_event:
                                        description:
                                            - If true, use Fluent::EventTime.now(current time) as a timestamp when time_key is specified.
                                            - Applicable when parser_type is 'CRI'
                                        type: bool
                                    is_keep_time_key:
                                        description:
                                            - If true, keep time field in the record.
                                            - Applicable when parser_type is 'CRI'
                                        type: bool
                                    timeout_in_milliseconds:
                                        description:
                                            - Specify the timeout for parse processing. This is mainly for detecting an incorrect regexp pattern.
                                            - Applicable when parser_type is 'CRI'
                                        type: int
                                    time_type:
                                        description:
                                            - Time type of JSON parser.
                                            - Applicable when parser_type is 'CRI'
                                        type: str
                                        choices:
                                            - "FLOAT"
                                            - "UNIXTIME"
                                            - "STRING"
                                    time_format:
                                        description:
                                            - Process time value using the specified format.
                                            - Applicable when parser_type is 'CRI'
                                        type: str
                            parser_type:
                                description:
                                    - Type of fluent parser.
                                type: str
                                choices:
                                    - "MULTILINE_GROK"
                                    - "JSON"
                                    - "GROK"
                                    - "NONE"
                                    - "SYSLOG"
                                    - "AUDITD"
                                    - "APACHE2"
                                    - "REGEXP"
                                    - "MULTILINE"
                                    - "TSV"
                                    - "CRI"
                                    - "APACHE_ERROR"
                                    - "MSGPACK"
                                    - "CSV"
                                required: true
                            field_time_key:
                                description:
                                    - Specify time field for the event time. If the event doesn't have this field, the current time is used.
                                type: str
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
                                type: dict
                            null_value_pattern:
                                description:
                                    - Specify the null value pattern.
                                type: str
                            is_null_empty_string:
                                description:
                                    - If true, an empty string field is replaced with nil.
                                type: bool
                            is_estimate_current_event:
                                description:
                                    - If true, use Fluent::EventTime.now(current time) as a timestamp when time_key is specified.
                                type: bool
                            is_keep_time_key:
                                description:
                                    - If true, keep time field in the record.
                                type: bool
                            timeout_in_milliseconds:
                                description:
                                    - Specify the timeout for parse processing. This is mainly for detecting an incorrect regexp pattern.
                                type: int
                            delimiter:
                                description:
                                    - tsv delimiter.
                                    - Applicable when parser_type is one of ['TSV', 'CSV']
                                type: str
                            keys:
                                description:
                                    - tsv keys.
                                    - Required when parser_type is one of ['TSV', 'CSV']
                                type: list
                                elements: str
            destination:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    log_object_id:
                        description:
                            - The OCID of the resource.
                        type: str
                        required: true
    group_association:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            group_list:
                description:
                    - list of group/dynamic group ids associated with this configuration.
                type: list
                elements: str
    unified_agent_configuration_id:
        description:
            - The OCID of the Unified Agent configuration.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the UnifiedAgentConfiguration.
            - Use I(state=present) to create or update an UnifiedAgentConfiguration.
            - Use I(state=absent) to delete an UnifiedAgentConfiguration.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create unified_agent_configuration
  oci_logging_unified_agent_configuration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    is_enabled: true
    service_configuration:
      # required
      configuration_type: LOGGING
      sources:
      - # required
        channels: [ "channels_example" ]
        name: name_example
        source_type: WINDOWS_EVENT_LOG
      destination:
        # required
        log_object_id: "ocid1.logobject.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    description: description_example
    group_association:
      # optional
      group_list: [ "group_list_example" ]

- name: Update unified_agent_configuration
  oci_logging_unified_agent_configuration:
    # required
    display_name: display_name_example
    is_enabled: true
    service_configuration:
      # required
      configuration_type: LOGGING
      sources:
      - # required
        channels: [ "channels_example" ]
        name: name_example
        source_type: WINDOWS_EVENT_LOG
      destination:
        # required
        log_object_id: "ocid1.logobject.oc1..xxxxxxEXAMPLExxxxxx"
    unified_agent_configuration_id: "ocid1.unifiedagentconfiguration.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    description: description_example
    group_association:
      # optional
      group_list: [ "group_list_example" ]

- name: Update unified_agent_configuration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_logging_unified_agent_configuration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    is_enabled: true
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    description: description_example
    service_configuration:
      # required
      configuration_type: LOGGING
      sources:
      - # required
        channels: [ "channels_example" ]
        name: name_example
        source_type: WINDOWS_EVENT_LOG
      destination:
        # required
        log_object_id: "ocid1.logobject.oc1..xxxxxxEXAMPLExxxxxx"
    group_association:
      # optional
      group_list: [ "group_list_example" ]

- name: Delete unified_agent_configuration
  oci_logging_unified_agent_configuration:
    # required
    unified_agent_configuration_id: "ocid1.unifiedagentconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete unified_agent_configuration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_logging_unified_agent_configuration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.logging import LoggingManagementClient
    from oci.logging.models import CreateUnifiedAgentConfigurationDetails
    from oci.logging.models import UpdateUnifiedAgentConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UnifiedAgentConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            UnifiedAgentConfigurationHelperGen, self
        ).get_possible_entity_types() + [
            "unifiedagentconfiguration",
            "unifiedagentconfigurations",
            "loggingunifiedagentconfiguration",
            "loggingunifiedagentconfigurations",
            "unifiedagentconfigurationresource",
            "unifiedagentconfigurationsresource",
            "logging",
        ]

    def get_module_resource_id_param(self):
        return "unified_agent_configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("unified_agent_configuration_id")

    def get_get_fn(self):
        return self.client.get_unified_agent_configuration

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_unified_agent_configuration,
            unified_agent_configuration_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_unified_agent_configuration,
            unified_agent_configuration_id=self.module.params.get(
                "unified_agent_configuration_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_unified_agent_configurations, **kwargs
        )

    def get_create_model_class(self):
        return CreateUnifiedAgentConfigurationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_unified_agent_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_unified_agent_configuration_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateUnifiedAgentConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_unified_agent_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                unified_agent_configuration_id=self.module.params.get(
                    "unified_agent_configuration_id"
                ),
                update_unified_agent_configuration_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_unified_agent_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                unified_agent_configuration_id=self.module.params.get(
                    "unified_agent_configuration_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


UnifiedAgentConfigurationHelperCustom = get_custom_class(
    "UnifiedAgentConfigurationHelperCustom"
)


class ResourceHelper(
    UnifiedAgentConfigurationHelperCustom, UnifiedAgentConfigurationHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            is_enabled=dict(type="bool"),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            description=dict(type="str"),
            service_configuration=dict(
                type="dict",
                options=dict(
                    configuration_type=dict(
                        type="str", required=True, choices=["LOGGING"]
                    ),
                    sources=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            channels=dict(type="list", elements="str"),
                            name=dict(type="str", required=True),
                            source_type=dict(
                                type="str",
                                required=True,
                                choices=["WINDOWS_EVENT_LOG", "LOG_TAIL"],
                            ),
                            paths=dict(type="list", elements="str"),
                            parser=dict(
                                type="dict",
                                options=dict(
                                    multi_line_start_regexp=dict(type="str"),
                                    time_type=dict(
                                        type="str",
                                        choices=["FLOAT", "UNIXTIME", "STRING"],
                                    ),
                                    grok_name_key=dict(type="str", no_log=True),
                                    grok_failure_key=dict(type="str", no_log=True),
                                    patterns=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            pattern=dict(type="str", required=True),
                                            name=dict(type="str"),
                                            field_time_key=dict(
                                                type="str", no_log=True
                                            ),
                                            field_time_format=dict(type="str"),
                                            field_time_zone=dict(type="str"),
                                        ),
                                    ),
                                    message_key=dict(type="str", no_log=True),
                                    rfc5424_time_format=dict(type="str"),
                                    message_format=dict(
                                        type="str",
                                        choices=["RFC3164", "RFC5424", "AUTO"],
                                    ),
                                    is_with_priority=dict(type="bool"),
                                    is_support_colonless_ident=dict(type="bool"),
                                    syslog_parser_type=dict(
                                        type="str", choices=["STRING", "REGEXP"]
                                    ),
                                    expression=dict(type="str"),
                                    time_format=dict(type="str"),
                                    format_firstline=dict(type="str"),
                                    format=dict(type="list", elements="str"),
                                    is_merge_cri_fields=dict(type="bool"),
                                    nested_parser=dict(
                                        type="dict",
                                        options=dict(
                                            parser_type=dict(
                                                type="str",
                                                required=True,
                                                choices=[
                                                    "AUDITD",
                                                    "CRI",
                                                    "JSON",
                                                    "TSV",
                                                    "CSV",
                                                    "NONE",
                                                    "SYSLOG",
                                                    "APACHE2",
                                                    "APACHE_ERROR",
                                                    "MSGPACK",
                                                    "REGEXP",
                                                    "MULTILINE",
                                                    "GROK",
                                                    "MULTILINE_GROK",
                                                ],
                                            ),
                                            field_time_key=dict(
                                                type="str", no_log=True
                                            ),
                                            types=dict(type="dict"),
                                            null_value_pattern=dict(type="str"),
                                            is_null_empty_string=dict(type="bool"),
                                            is_estimate_current_event=dict(type="bool"),
                                            is_keep_time_key=dict(
                                                type="bool", no_log=True
                                            ),
                                            timeout_in_milliseconds=dict(type="int"),
                                            time_type=dict(
                                                type="str",
                                                choices=["FLOAT", "UNIXTIME", "STRING"],
                                            ),
                                            time_format=dict(type="str"),
                                        ),
                                    ),
                                    parser_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "MULTILINE_GROK",
                                            "JSON",
                                            "GROK",
                                            "NONE",
                                            "SYSLOG",
                                            "AUDITD",
                                            "APACHE2",
                                            "REGEXP",
                                            "MULTILINE",
                                            "TSV",
                                            "CRI",
                                            "APACHE_ERROR",
                                            "MSGPACK",
                                            "CSV",
                                        ],
                                    ),
                                    field_time_key=dict(type="str", no_log=True),
                                    types=dict(type="dict"),
                                    null_value_pattern=dict(type="str"),
                                    is_null_empty_string=dict(type="bool"),
                                    is_estimate_current_event=dict(type="bool"),
                                    is_keep_time_key=dict(type="bool", no_log=True),
                                    timeout_in_milliseconds=dict(type="int"),
                                    delimiter=dict(type="str"),
                                    keys=dict(type="list", elements="str", no_log=True),
                                ),
                            ),
                        ),
                    ),
                    destination=dict(
                        type="dict",
                        required=True,
                        options=dict(log_object_id=dict(type="str", required=True)),
                    ),
                ),
            ),
            group_association=dict(
                type="dict", options=dict(group_list=dict(type="list", elements="str"))
            ),
            unified_agent_configuration_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
