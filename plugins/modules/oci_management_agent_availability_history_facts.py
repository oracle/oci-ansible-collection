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
module: oci_management_agent_availability_history_facts
short_description: Fetches details about one or multiple AvailabilityHistory resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AvailabilityHistory resources in Oracle Cloud Infrastructure
    - Lists the availability history records of Management Agent
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    management_agent_id:
        description:
            - Unique Management Agent identifier
        type: str
        required: true
    time_availability_status_ended_greater_than:
        description:
            - Filter to limit the availability history results to that of time after the input time including the boundary record.
              Defaulted to current date minus one year.
              The date and time to be given as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 5.6.
        type: str
    time_availability_status_started_less_than:
        description:
            - Filter to limit the availability history results to that of time before the input time including the boundary record
              Defaulted to current date.
              The date and time to be given as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 5.6.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Default order for timeAvailabilityStatusStarted is descending.
        type: str
        choices:
            - "timeAvailabilityStatusStarted"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List availability_histories
  oci_management_agent_availability_history_facts:
    # required
    management_agent_id: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    time_availability_status_ended_greater_than: 2013-10-20T19:20:30+01:00
    time_availability_status_started_less_than: 2013-10-20T19:20:30+01:00
    sort_order: ASC
    sort_by: timeAvailabilityStatusStarted

"""

RETURN = """
availability_histories:
    description:
        - List of AvailabilityHistory resources
    returned: on success
    type: complex
    contains:
        management_agent_id:
            description:
                - agent identifier
            returned: on success
            type: str
            sample: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
        availability_status:
            description:
                - The availability status of managementAgent
            returned: on success
            type: str
            sample: ACTIVE
        time_availability_status_started:
            description:
                - The time at which the Management Agent moved to the availability status. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_availability_status_ended:
            description:
                - The time till which the Management Agent was known to be in the availability status. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "management_agent_id": "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_status": "ACTIVE",
        "time_availability_status_started": "2013-10-20T19:20:30+01:00",
        "time_availability_status_ended": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.management_agent import ManagementAgentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AvailabilityHistoryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "management_agent_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "time_availability_status_ended_greater_than",
            "time_availability_status_started_less_than",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_availability_histories,
            management_agent_id=self.module.params.get("management_agent_id"),
            **optional_kwargs
        )


AvailabilityHistoryFactsHelperCustom = get_custom_class(
    "AvailabilityHistoryFactsHelperCustom"
)


class ResourceFactsHelper(
    AvailabilityHistoryFactsHelperCustom, AvailabilityHistoryFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            management_agent_id=dict(type="str", required=True),
            time_availability_status_ended_greater_than=dict(type="str"),
            time_availability_status_started_less_than=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeAvailabilityStatusStarted"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="availability_history",
        service_client_class=ManagementAgentClient,
        namespace="management_agent",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(availability_histories=result)


if __name__ == "__main__":
    main()
