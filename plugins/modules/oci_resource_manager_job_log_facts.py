#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_resource_manager_job_log_facts
short_description: Fetches details about one or multiple JobLog resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple JobLog resources in Oracle Cloud Infrastructure
    - Returns console log entries for the specified job in JSON format.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    job_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job.
        type: str
        required: true
    type:
        description:
            - A filter that returns only logs of a specified type.
        type: list
        elements: str
    level_greater_than_or_equal_to:
        description:
            - A filter that returns only log entries that match a given severity level or greater.
        type: str
        choices:
            - "TRACE"
            - "DEBUG"
            - "INFO"
            - "WARN"
            - "ERROR"
            - "FATAL"
    sort_order:
        description:
            - The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    timestamp_greater_than_or_equal_to:
        description:
            - "Time stamp specifying the lower time limit for which logs are returned in a query.
              Format is defined by RFC3339.
              Example: `2020-01-01T12:00:00.000Z`"
        type: str
    timestamp_less_than_or_equal_to:
        description:
            - "Time stamp specifying the upper time limit for which logs are returned in a query.
              Format is defined by RFC3339.
              Example: `2020-02-01T12:00:00.000Z`"
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List job_logs
  oci_resource_manager_job_log_facts:
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
job_logs:
    description:
        - List of JobLog resources
    returned: on success
    type: complex
    contains:
        type:
            description:
                - Specifies the log type for the log entry.
            returned: on success
            type: str
            sample: TERRAFORM_CONSOLE
        level:
            description:
                - Specifies the severity level of the log entry.
            returned: on success
            type: str
            sample: TRACE
        timestamp:
            description:
                - "The date and time of the log entry.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2020-01-25T21:10:29.600Z"
        message:
            description:
                - The log entry value.
            returned: on success
            type: str
            sample: message_example
    sample: [{
        "type": "TERRAFORM_CONSOLE",
        "level": "TRACE",
        "timestamp": "2020-01-25T21:10:29.600Z",
        "message": "message_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.resource_manager import ResourceManagerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class JobLogFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "job_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "type",
            "level_greater_than_or_equal_to",
            "sort_order",
            "timestamp_greater_than_or_equal_to",
            "timestamp_less_than_or_equal_to",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.get_job_logs,
            job_id=self.module.params.get("job_id"),
            **optional_kwargs
        )


JobLogFactsHelperCustom = get_custom_class("JobLogFactsHelperCustom")


class ResourceFactsHelper(JobLogFactsHelperCustom, JobLogFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            job_id=dict(type="str", required=True),
            type=dict(type="list", elements="str"),
            level_greater_than_or_equal_to=dict(
                type="str", choices=["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"]
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            timestamp_greater_than_or_equal_to=dict(type="str"),
            timestamp_less_than_or_equal_to=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="job_log",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(job_logs=result)


if __name__ == "__main__":
    main()
