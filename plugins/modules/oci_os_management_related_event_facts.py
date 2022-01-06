#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_os_management_related_event_facts
short_description: Fetches details about one or multiple RelatedEvent resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RelatedEvent resources in Oracle Cloud Infrastructure
    - Returns a list of related events. For now pagination is not implemented.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    event_fingerprint:
        description:
            - Event fingerprint identifier
        type: str
        required: true
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for id is descending.
        type: str
        choices:
            - "instanceId"
            - "id"
            - "eventFingerprint"
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
- name: List related_events
  oci_os_management_related_event_facts:
    # required
    event_fingerprint: event_fingerprint_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: instanceId
    latest_timestamp_less_than: 2013-10-20T19:20:30+01:00
    latest_timestamp_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00

"""

RETURN = """
related_events:
    description:
        - List of RelatedEvent resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID identifier of the event
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        instance_id:
            description:
                - OCID identifier of the instance
            returned: on success
            type: str
            sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
        timestamp:
            description:
                - time occurence
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
        "timestamp": "2013-10-20T19:20:30+01:00"
    }]
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


class RelatedEventFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "event_fingerprint",
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "latest_timestamp_less_than",
            "latest_timestamp_greater_than_or_equal_to",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_related_events,
            event_fingerprint=self.module.params.get("event_fingerprint"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


RelatedEventFactsHelperCustom = get_custom_class("RelatedEventFactsHelperCustom")


class ResourceFactsHelper(RelatedEventFactsHelperCustom, RelatedEventFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            event_fingerprint=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["instanceId", "id", "eventFingerprint"]),
            latest_timestamp_less_than=dict(type="str"),
            latest_timestamp_greater_than_or_equal_to=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="related_event",
        service_client_class=EventClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(related_events=result)


if __name__ == "__main__":
    main()
