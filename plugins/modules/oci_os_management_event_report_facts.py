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
module: oci_os_management_event_report_facts
short_description: Fetches details about a EventReport resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a EventReport resource in Oracle Cloud Infrastructure
    - Get summary information about events on this instance.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_instance_id:
        description:
            - Instance Oracle Cloud identifier (ocid)
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
        required: true
    latest_timestamp_less_than:
        description:
            - "filter event occurrence. Selecting only those last occurred before given date in ISO 8601 format
              Example: 2017-07-14T02:40:00.000Z"
        type: str
    latest_timestamp_greater_than_or_equal_to:
        description:
            - "filter event occurrence. Selecting only those last occurred on or after given date in ISO 8601 format
              Example: 2017-07-14T02:40:00.000Z"
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific event_report
  oci_os_management_event_report_facts:
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
event_report:
    description:
        - EventReport resource
    returned: on success
    type: complex
    contains:
        count:
            description:
                - count of events currently registered on the system.
            returned: on success
            type: int
            sample: 56
    sample: {
        "count": 56
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.os_management import EventClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EventReportFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "managed_instance_id",
            "compartment_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "latest_timestamp_less_than",
            "latest_timestamp_greater_than_or_equal_to",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_event_report,
            managed_instance_id=self.module.params.get("managed_instance_id"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


EventReportFactsHelperCustom = get_custom_class("EventReportFactsHelperCustom")


class ResourceFactsHelper(EventReportFactsHelperCustom, EventReportFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_instance_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            latest_timestamp_less_than=dict(type="str"),
            latest_timestamp_greater_than_or_equal_to=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="event_report",
        service_client_class=EventClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(event_report=result)


if __name__ == "__main__":
    main()
