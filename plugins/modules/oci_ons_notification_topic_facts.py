#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_ons_notification_topic_facts
short_description: Fetches details about one or multiple NotificationTopic resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple NotificationTopic resources in Oracle Cloud Infrastructure
    - Lists topics in the specified compartment.
    - "Transactions Per Minute (TPM) per-tenancy limit for this operation: 120."
    - If I(topic_id) is specified, the details of a single NotificationTopic will be returned.
version_added: "2.5"
options:
    topic_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the topic to retrieve.
            - "Transactions Per Minute (TPM) per-tenancy limit for this operation: 120."
            - Required to get a specific notification_topic.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple notification_topics.
        type: str
    name:
        description:
            - A filter to only return resources that match the given name exactly.
        type: str
    sort_by:
        description:
            - The field to sort by. Only one field can be selected for sorting.
        type: str
        choices:
            - "TIMECREATED"
            - "LIFECYCLESTATE"
    sort_order:
        description:
            - The sort order to use (ascending or descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - Filter returned list by specified lifecycle state. This parameter is case-insensitive.
        type: str
        choices:
            - "ACTIVE"
            - "DELETING"
            - "CREATING"
author: Oracle (@oracle)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List notification_topics
  oci_ons_notification_topic_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific notification_topic
  oci_ons_notification_topic_facts:
    topic_id: ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
notification_topics:
    description:
        - List of NotificationTopic resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the topic.
            returned: on success
            type: string
            sample: name_example
        topic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the topic.
            returned: on success
            type: string
            sample: ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment for the topic.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The lifecycle state of the topic.
            returned: on success
            type: string
            sample: ACTIVE
        description:
            description:
                - The description of the topic.
            returned: on success
            type: string
            sample: description_example
        time_created:
            description:
                - The time the topic was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        etag:
            description:
                - For optimistic concurrency control. See `if-match`.
            returned: on success
            type: string
            sample: etag_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        api_endpoint:
            description:
                - The endpoint for managing subscriptions or publishing messages to the topic.
            returned: on success
            type: string
            sample: api_endpoint_example
    sample: [{
        "name": "name_example",
        "topic_id": "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "etag": "etag_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "api_endpoint": "api_endpoint_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.ons import NotificationControlPlaneClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NotificationTopicFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "topic_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_topic, topic_id=self.module.params.get("topic_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "id",
            "name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_topics,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


NotificationTopicFactsHelperCustom = get_custom_class(
    "NotificationTopicFactsHelperCustom"
)


class ResourceFactsHelper(
    NotificationTopicFactsHelperCustom, NotificationTopicFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            topic_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "LIFECYCLESTATE"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str", choices=["ACTIVE", "DELETING", "CREATING"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="notification_topic",
        service_client_class=NotificationControlPlaneClient,
        namespace="ons",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(notification_topics=result)


if __name__ == "__main__":
    main()
