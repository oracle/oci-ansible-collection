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
module: oci_log_analytics_recalled_data_facts
short_description: Fetches details about one or multiple RecalledData resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RecalledData resources in Oracle Cloud Infrastructure
    - This API returns the list of recalled data of a tenancy.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    sort_by:
        description:
            - This is the query parameter of which field to sort by. Only one sort order may be provided. Default order for timeDataStarted
              is descending. If no value is specified timeDataStarted is default.
        type: str
        choices:
            - "timeStarted"
            - "timeDataStarted"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    time_data_started_greater_than_or_equal:
        description:
            - This is the start of the time range for recalled data
        type: str
    time_data_ended_less_than:
        description:
            - This is the end of the time range for recalled data
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List recalled_data
  oci_log_analytics_recalled_data_facts:
    # required
    namespace_name: namespace_name_example

    # optional
    sort_by: timeStarted
    sort_order: ASC
    time_data_started_greater_than_or_equal: 2013-10-20T19:20:30+01:00
    time_data_ended_less_than: 2013-10-20T19:20:30+01:00

"""

RETURN = """
recalled_data:
    description:
        - List of RecalledData resources
    returned: on success
    type: complex
    contains:
        time_data_ended:
            description:
                - This is the end of the time range of the related data
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_data_started:
            description:
                - This is the start of the time range of the related data
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_started:
            description:
                - This is the time when the first recall operation was started for this RecalledData
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        status:
            description:
                - This is the status of the recall
            returned: on success
            type: str
            sample: RECALLED
        recall_count:
            description:
                - This is the number of recall operations for this recall.  Note one RecalledData can be merged from the results
                  of several recall operations if the time duration of the results of the recall operations overlap.
            returned: on success
            type: int
            sample: 56
        storage_usage_in_bytes:
            description:
                - This is the size in bytes
            returned: on success
            type: int
            sample: 56
    sample: [{
        "time_data_ended": "2013-10-20T19:20:30+01:00",
        "time_data_started": "2013-10-20T19:20:30+01:00",
        "time_started": "2013-10-20T19:20:30+01:00",
        "status": "RECALLED",
        "recall_count": 56,
        "storage_usage_in_bytes": 56
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.log_analytics import LogAnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RecalledDataFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "namespace_name",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "time_data_started_greater_than_or_equal",
            "time_data_ended_less_than",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_recalled_data,
            namespace_name=self.module.params.get("namespace_name"),
            **optional_kwargs
        )


RecalledDataFactsHelperCustom = get_custom_class("RecalledDataFactsHelperCustom")


class ResourceFactsHelper(RecalledDataFactsHelperCustom, RecalledDataFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["timeStarted", "timeDataStarted"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            time_data_started_greater_than_or_equal=dict(type="str"),
            time_data_ended_less_than=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="recalled_data",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(recalled_data=result)


if __name__ == "__main__":
    main()
