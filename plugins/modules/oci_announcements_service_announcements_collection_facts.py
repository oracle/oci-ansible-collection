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
module: oci_announcements_service_announcements_collection_facts
short_description: Fetches details about one or multiple AnnouncementsCollection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AnnouncementsCollection resources in Oracle Cloud Infrastructure
    - Gets a list of announcements for the current tenancy.
    - This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might
      throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service
      might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
        type: str
        required: true
    announcement_type:
        description:
            - The type of announcement.
        type: str
    lifecycle_state:
        description:
            - The announcement's current lifecycle state.
        type: str
        choices:
            - "ACTIVE"
            - "INACTIVE"
    is_banner:
        description:
            - Whether the announcement is displayed as a console banner.
        type: bool
    sort_by:
        description:
            - The criteria to sort by. You can specify only one sort order.
        type: str
        choices:
            - "timeOneValue"
            - "timeTwoValue"
            - "timeCreated"
            - "referenceTicketNumber"
            - "summary"
            - "announcementType"
    sort_order:
        description:
            - The sort order to use. (Sorting by `announcementType` orders the announcements list according to importance.)
        type: str
        choices:
            - "ASC"
            - "DESC"
    time_one_earliest_time:
        description:
            - The boundary for the earliest `timeOneValue` date on announcements that you want to see.
        type: str
    time_one_latest_time:
        description:
            - The boundary for the latest `timeOneValue` date on announcements that you want to see.
        type: str
    environment_name:
        description:
            - A filter to return only announcements that match a specific environment name.
        type: str
    service:
        description:
            - A filter to return only announcements affecting a specific service.
        type: str
    platform_type:
        description:
            - A filter to return only announcements affecting a specific platform.
        type: str
        choices:
            - "IAAS"
            - "SAAS"
    exclude_announcement_types:
        description:
            - Exclude The type of announcement.
        type: list
        elements: str
    should_show_only_latest_in_chain:
        description:
            - A filter to display only the latest announcement in a chain.
        type: bool
    chain_id:
        description:
            - A filter to return only announcements belonging to the specified announcement chain ID.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List announcements_collection
  oci_announcements_service_announcements_collection_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    announcement_type: announcement_type_example
    lifecycle_state: ACTIVE
    is_banner: true
    sort_by: timeOneValue
    sort_order: ASC
    time_one_earliest_time: 2013-10-20T19:20:30+01:00
    time_one_latest_time: 2013-10-20T19:20:30+01:00
    environment_name: environment_name_example
    service: service_example
    platform_type: IAAS
    exclude_announcement_types: [ "exclude_announcement_types_example" ]
    should_show_only_latest_in_chain: true
    chain_id: "ocid1.chain.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
announcements_collection:
    description:
        - List of AnnouncementsCollection resources
    returned: on success
    type: complex
    contains:
        items:
            description:
                - A collection of announcements.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The OCID of the announcement.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                type:
                    description:
                        - The entity type, which is either an announcement or the summary representation of an announcement.
                    returned: on success
                    type: str
                    sample: type_example
                reference_ticket_number:
                    description:
                        - The reference Jira ticket number.
                    returned: on success
                    type: str
                    sample: reference_ticket_number_example
                summary:
                    description:
                        - A summary of the issue. A summary might appear in the console banner view of the announcement or in
                          an email subject line. Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: summary_example
                time_one_title:
                    description:
                        - "The label associated with an initial time value.
                          Example: `Time Started`"
                    returned: on success
                    type: str
                    sample: time_one_title_example
                time_one_type:
                    description:
                        - "The type of a time associated with an initial time value. If the `timeOneTitle` attribute is present, then the `timeOneTitle`
                          attribute contains a label of `timeOneType` in English.
                          Example: `START_TIME`"
                    returned: on success
                    type: str
                    sample: ACTION_REQUIRED_BY
                time_one_value:
                    description:
                        - The actual value of the first time value for the event. Typically, this denotes the time an event started, but the meaning
                          can vary, depending on the announcement type. The `timeOneType` attribute describes the meaning.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_two_title:
                    description:
                        - "The label associated with a second time value.
                          Example: `Time Ended`"
                    returned: on success
                    type: str
                    sample: time_two_title_example
                time_two_type:
                    description:
                        - "The type of a time associated with second time value. If the `timeTwoTitle` attribute is present, then the `timeTwoTitle` attribute
                          contains a label of `timeTwoType` in English.
                          Example: `END_TIME`"
                    returned: on success
                    type: str
                    sample: END_TIME
                time_two_value:
                    description:
                        - The actual value of the second time value. Typically, this denotes the time an event ended, but the meaning
                          can vary, depending on the announcement type. The `timeTwoType` attribute describes the meaning.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                services:
                    description:
                        - Impacted Oracle Cloud Infrastructure services.
                    returned: on success
                    type: list
                    sample: []
                affected_regions:
                    description:
                        - Impacted regions.
                    returned: on success
                    type: list
                    sample: []
                announcement_type:
                    description:
                        - The type of announcement. An announcement's type signals its severity.
                    returned: on success
                    type: str
                    sample: ACTION_RECOMMENDED
                lifecycle_state:
                    description:
                        - The current lifecycle state of the announcement.
                    returned: on success
                    type: str
                    sample: ACTIVE
                is_banner:
                    description:
                        - Whether the announcement is displayed as a banner in the console.
                    returned: on success
                    type: bool
                    sample: true
                time_created:
                    description:
                        - "The date and time the announcement was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                          Example: `2019-01-01T17:43:01.389+0000`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - "The date and time the announcement was last updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                          Example: `2019-01-01T17:43:01.389+0000`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                environment_name:
                    description:
                        - The name of the environment that this announcement pertains to.
                    returned: on success
                    type: str
                    sample: environment_name_example
                platform_type:
                    description:
                        - The platform type that this announcement pertains to.
                    returned: on success
                    type: str
                    sample: IAAS
                chain_id:
                    description:
                        - The sequence of connected announcements, or announcement chain, that this announcement belongs to. Related announcements share the
                          same chain ID.
                    returned: on success
                    type: str
                    sample: "ocid1.chain.oc1..xxxxxxEXAMPLExxxxxx"
        user_statuses:
            description:
                - The user-specific status for found announcements.
            returned: on success
            type: complex
            contains:
                user_status_announcement_id:
                    description:
                        - The OCID of the announcement that this status is associated with.
                    returned: on success
                    type: str
                    sample: "ocid1.userstatusannouncement.oc1..xxxxxxEXAMPLExxxxxx"
                user_id:
                    description:
                        - The OCID of the user that this status is associated with.
                    returned: on success
                    type: str
                    sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
                time_acknowledged:
                    description:
                        - "The date and time the announcement was acknowledged, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                          Example: `2019-01-01T17:43:01.389+0000`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "items": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "type": "type_example",
            "reference_ticket_number": "reference_ticket_number_example",
            "summary": "summary_example",
            "time_one_title": "time_one_title_example",
            "time_one_type": "ACTION_REQUIRED_BY",
            "time_one_value": "2013-10-20T19:20:30+01:00",
            "time_two_title": "time_two_title_example",
            "time_two_type": "END_TIME",
            "time_two_value": "2013-10-20T19:20:30+01:00",
            "services": [],
            "affected_regions": [],
            "announcement_type": "ACTION_RECOMMENDED",
            "lifecycle_state": "ACTIVE",
            "is_banner": true,
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "environment_name": "environment_name_example",
            "platform_type": "IAAS",
            "chain_id": "ocid1.chain.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "user_statuses": [{
            "user_status_announcement_id": "ocid1.userstatusannouncement.oc1..xxxxxxEXAMPLExxxxxx",
            "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
            "time_acknowledged": "2013-10-20T19:20:30+01:00"
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.announcements_service import AnnouncementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AnnouncementsCollectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "announcement_type",
            "lifecycle_state",
            "is_banner",
            "sort_by",
            "sort_order",
            "time_one_earliest_time",
            "time_one_latest_time",
            "environment_name",
            "service",
            "platform_type",
            "exclude_announcement_types",
            "should_show_only_latest_in_chain",
            "chain_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_announcements,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AnnouncementsCollectionFactsHelperCustom = get_custom_class(
    "AnnouncementsCollectionFactsHelperCustom"
)


class ResourceFactsHelper(
    AnnouncementsCollectionFactsHelperCustom, AnnouncementsCollectionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            announcement_type=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "INACTIVE"]),
            is_banner=dict(type="bool"),
            sort_by=dict(
                type="str",
                choices=[
                    "timeOneValue",
                    "timeTwoValue",
                    "timeCreated",
                    "referenceTicketNumber",
                    "summary",
                    "announcementType",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            time_one_earliest_time=dict(type="str"),
            time_one_latest_time=dict(type="str"),
            environment_name=dict(type="str"),
            service=dict(type="str"),
            platform_type=dict(type="str", choices=["IAAS", "SAAS"]),
            exclude_announcement_types=dict(type="list", elements="str"),
            should_show_only_latest_in_chain=dict(type="bool"),
            chain_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="announcements_collection",
        service_client_class=AnnouncementClient,
        namespace="announcements_service",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(announcements_collection=result)


if __name__ == "__main__":
    main()
