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
module: oci_announcements_service_announcement_subscription_facts
short_description: Fetches details about one or multiple AnnouncementSubscription resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AnnouncementSubscription resources in Oracle Cloud Infrastructure
    - Gets a list of all announcement subscriptions in the specified compartment.
    - This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might
      throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service
      might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.
    - If I(announcement_subscription_id) is specified, the details of a single AnnouncementSubscription will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    announcement_subscription_id:
        description:
            - The OCID of the announcement subscription.
            - Required to get a specific announcement_subscription.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple announcement_subscriptions.
        type: str
    lifecycle_state:
        description:
            - A filter to return only announcement subscriptions that match the given lifecycle state.
        type: str
        choices:
            - "ACTIVE"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, whether ascending ('ASC') or descending ('DESC').
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The criteria to sort by. You can specify only one sort order. The default sort order for the creation date of resources is descending. The default
              sort order for display names is ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific announcement_subscription
  oci_announcements_service_announcement_subscription_facts:
    # required
    announcement_subscription_id: "ocid1.announcementsubscription.oc1..xxxxxxEXAMPLExxxxxx"

- name: List announcement_subscriptions
  oci_announcements_service_announcement_subscription_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: ACTIVE
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
announcement_subscriptions:
    description:
        - List of AnnouncementSubscription resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - A description of the announcement subscription. Avoid entering confidential information.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        filter_groups:
            description:
                - A list of filter groups for the announcement subscription. A filter group is a combination of multiple filters applied to announcements for
                  matching purposes.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the group. The name must be unique and it cannot be changed. Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: name_example
                filters:
                    description:
                        - A list of filters against which the Announcements service matches announcements. You cannot combine the RESOURCE_ID filter with any
                          other type of filter within a given filter group. For filter types that support multiple values, specify the values individually.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - The type of filter. You cannot combine the RESOURCE_ID filter with any other type of filter within a given filter group. For
                                  filter types that support multiple values, specify the values individually.
                            returned: on success
                            type: str
                            sample: COMPARTMENT_ID
                        value:
                            description:
                                - The value of the filter.
                            returned: on success
                            type: str
                            sample: value_example
        preferred_language:
            description:
                - (For announcement subscriptions with SaaS configured as the platform type or Oracle Fusion Applications as the service, or both, only) The
                  language in which the user prefers to receive emailed announcements. Specify the preference with a value that uses the x-obmcs-human-language
                  format. For example fr-FR.
                - Returned for get operation
            returned: on success
            type: str
            sample: preferred_language_example
        preferred_time_zone:
            description:
                - "The time zone in which the user prefers to receive announcements. Specify the preference with a value that uses the IANA Time Zone Database
                  format (x-obmcs-time-zone). For example - America/Los_Angeles"
                - Returned for get operation
            returned: on success
            type: str
            sample: preferred_time_zone_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the announcement subscription.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name for the announcement subscription. Does not have to be unique, and it's changeable. Avoid entering confidential
                  information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment that contains the announcement subscription.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time that the announcement subscription was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time that the announcement subscription was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the announcement subscription.
            returned: on success
            type: str
            sample: ACTIVE
        lifecycle_details:
            description:
                - A message describing the current lifecycle state in more detail. For example, details might provide required or recommended actions for a
                  resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        ons_topic_id:
            description:
                - The OCID of the Notifications service topic that is the target for publishing announcements that match the configured announcement
                  subscription.
            returned: on success
            type: str
            sample: "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "description": "description_example",
        "filter_groups": {
            "name": "name_example",
            "filters": [{
                "type": "COMPARTMENT_ID",
                "value": "value_example"
            }]
        },
        "preferred_language": "preferred_language_example",
        "preferred_time_zone": "preferred_time_zone_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "ons_topic_id": "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.announcements_service import AnnouncementSubscriptionClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AnnouncementSubscriptionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "announcement_subscription_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_announcement_subscription,
            announcement_subscription_id=self.module.params.get(
                "announcement_subscription_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_announcement_subscriptions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AnnouncementSubscriptionFactsHelperCustom = get_custom_class(
    "AnnouncementSubscriptionFactsHelperCustom"
)


class ResourceFactsHelper(
    AnnouncementSubscriptionFactsHelperCustom, AnnouncementSubscriptionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            announcement_subscription_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED", "FAILED"]),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="announcement_subscription",
        service_client_class=AnnouncementSubscriptionClient,
        namespace="announcements_service",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(announcement_subscriptions=result)


if __name__ == "__main__":
    main()
