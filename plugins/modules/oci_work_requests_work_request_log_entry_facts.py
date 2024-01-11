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
module: oci_work_requests_work_request_log_entry_facts
short_description: Fetches details about one or multiple WorkRequestLogEntry resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple WorkRequestLogEntry resources in Oracle Cloud Infrastructure
    - Gets the logs for a work request.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    work_request_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the work request.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List work_request_log_entries
  oci_work_requests_work_request_log_entry_facts:
    # required
    work_request_id: "ocid1.workrequest.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC

"""

RETURN = """
work_request_log_entries:
    description:
        - List of WorkRequestLogEntry resources
    returned: on success
    type: complex
    contains:
        message:
            description:
                - A human-readable log message.
            returned: on success
            type: str
            sample: message_example
        timestamp:
            description:
                - The date and time the log message was written.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "message": "message_example",
        "timestamp": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.work_requests import WorkRequestClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WorkRequestLogEntryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "work_request_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_work_request_logs,
            work_request_id=self.module.params.get("work_request_id"),
            **optional_kwargs
        )


WorkRequestLogEntryFactsHelperCustom = get_custom_class(
    "WorkRequestLogEntryFactsHelperCustom"
)


class ResourceFactsHelper(
    WorkRequestLogEntryFactsHelperCustom, WorkRequestLogEntryFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            work_request_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="work_request_log_entry",
        service_client_class=WorkRequestClient,
        namespace="work_requests",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(work_request_log_entries=result)


if __name__ == "__main__":
    main()
