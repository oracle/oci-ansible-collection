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
module: oci_database_management_alert_log_facts
short_description: Fetches details about one or multiple AlertLog resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AlertLog resources in Oracle Cloud Infrastructure
    - Lists the alert logs for the specified Managed Database.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    time_greater_than_or_equal_to:
        description:
            - The optional greater than or equal to timestamp to filter the logs.
        type: str
    time_less_than_or_equal_to:
        description:
            - The optional less than or equal to timestamp to filter the logs.
        type: str
    level_filter:
        description:
            - The optional parameter to filter the alert logs by log level.
        type: str
        choices:
            - "CRITICAL"
            - "SEVERE"
            - "IMPORTANT"
            - "NORMAL"
            - "ALL"
    type_filter:
        description:
            - The optional parameter to filter the attention or alert logs by type.
        type: str
        choices:
            - "UNKNOWN"
            - "INCIDENT_ERROR"
            - "ERROR"
            - "WARNING"
            - "NOTIFICATION"
            - "TRACE"
            - "ALL"
    log_search_text:
        description:
            - The optional query parameter to filter the attention or alert logs by search text.
        type: str
    is_regular_expression:
        description:
            - The flag to indicate whether the search text is regular expression or not.
        type: bool
    sort_by:
        description:
            - The possible sortBy values of attention logs.
        type: str
        choices:
            - "LEVEL"
            - "TYPE"
            - "MESSAGE"
            - "TIMESTAMP"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Ascending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List alert_logs
  oci_database_management_alert_log_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    time_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    level_filter: CRITICAL
    type_filter: UNKNOWN
    log_search_text: log_search_text_example
    is_regular_expression: true
    sort_by: LEVEL
    sort_order: ASC

"""

RETURN = """
alert_logs:
    description:
        - List of AlertLog resources
    returned: on success
    type: complex
    contains:
        message_level:
            description:
                - The level of the alert log.
            returned: on success
            type: str
            sample: CRITICAL
        message_type:
            description:
                - The type of alert log message.
            returned: on success
            type: str
            sample: UNKNOWN
        message_content:
            description:
                - The contents of the alert log message.
            returned: on success
            type: str
            sample: message_content_example
        timestamp:
            description:
                - The date and time the alert log was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        supplemental_detail:
            description:
                - The supplemental details of the alert log.
            returned: on success
            type: str
            sample: supplemental_detail_example
        file_location:
            description:
                - The alert log file location.
            returned: on success
            type: str
            sample: file_location_example
    sample: [{
        "message_level": "CRITICAL",
        "message_type": "UNKNOWN",
        "message_content": "message_content_example",
        "timestamp": "2013-10-20T19:20:30+01:00",
        "supplemental_detail": "supplemental_detail_example",
        "file_location": "file_location_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DiagnosabilityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AlertLogFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "level_filter",
            "type_filter",
            "log_search_text",
            "is_regular_expression",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_alert_logs,
            managed_database_id=self.module.params.get("managed_database_id"),
            **optional_kwargs
        )


AlertLogFactsHelperCustom = get_custom_class("AlertLogFactsHelperCustom")


class ResourceFactsHelper(AlertLogFactsHelperCustom, AlertLogFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            time_greater_than_or_equal_to=dict(type="str"),
            time_less_than_or_equal_to=dict(type="str"),
            level_filter=dict(
                type="str", choices=["CRITICAL", "SEVERE", "IMPORTANT", "NORMAL", "ALL"]
            ),
            type_filter=dict(
                type="str",
                choices=[
                    "UNKNOWN",
                    "INCIDENT_ERROR",
                    "ERROR",
                    "WARNING",
                    "NOTIFICATION",
                    "TRACE",
                    "ALL",
                ],
            ),
            log_search_text=dict(type="str"),
            is_regular_expression=dict(type="bool"),
            sort_by=dict(type="str", choices=["LEVEL", "TYPE", "MESSAGE", "TIMESTAMP"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="alert_log",
        service_client_class=DiagnosabilityClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(alert_logs=result)


if __name__ == "__main__":
    main()
