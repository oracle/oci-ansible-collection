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
module: oci_queue_stats_facts
short_description: Fetches details about a QueueStats resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a QueueStats resource in Oracle Cloud Infrastructure
    - Gets the statistics for the queue and its dead letter queue.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    queue_id:
        description:
            - unique Queue identifier
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific queue_stats
  oci_queue_stats_facts:
    # required
    queue_id: "ocid1.queue.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
queue_stats:
    description:
        - QueueStats resource
    returned: on success
    type: complex
    contains:
        queue:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                visible_messages:
                    description:
                        - The approximate number of visible messages (available for delivery) currently in the queue.
                    returned: on success
                    type: int
                    sample: 56
                in_flight_messages:
                    description:
                        - The approximate number of messages delivered to a consumer but not yet deleted and so unavailable for re-delivery.
                    returned: on success
                    type: int
                    sample: 56
                size_in_bytes:
                    description:
                        - The approximate size of the queue in bytes. Sum of the size of visible of in-flight messages.
                    returned: on success
                    type: int
                    sample: 56
        dlq:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                visible_messages:
                    description:
                        - The approximate number of visible messages (available for delivery) currently in the queue.
                    returned: on success
                    type: int
                    sample: 56
                in_flight_messages:
                    description:
                        - The approximate number of messages delivered to a consumer but not yet deleted and so unavailable for re-delivery.
                    returned: on success
                    type: int
                    sample: 56
                size_in_bytes:
                    description:
                        - The approximate size of the queue in bytes. Sum of the size of visible of in-flight messages.
                    returned: on success
                    type: int
                    sample: 56
    sample: {
        "queue": {
            "visible_messages": 56,
            "in_flight_messages": 56,
            "size_in_bytes": 56
        },
        "dlq": {
            "visible_messages": 56,
            "in_flight_messages": 56,
            "size_in_bytes": 56
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.queue import QueueClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class QueueStatsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "queue_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_stats, queue_id=self.module.params.get("queue_id"),
        )


QueueStatsFactsHelperCustom = get_custom_class("QueueStatsFactsHelperCustom")


class ResourceFactsHelper(QueueStatsFactsHelperCustom, QueueStatsFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(queue_id=dict(aliases=["id"], type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="queue_stats",
        service_client_class=QueueClient,
        namespace="queue",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(queue_stats=result)


if __name__ == "__main__":
    main()
