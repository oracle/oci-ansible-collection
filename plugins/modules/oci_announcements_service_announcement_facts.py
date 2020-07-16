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
module: oci_announcements_service_announcement_facts
short_description: Fetches details about a Announcement resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Announcement resource in Oracle Cloud Infrastructure
    - Gets the details of a specific announcement.
version_added: "2.9"
author: Oracle (@oracle)
options:
    announcement_id:
        description:
            - The OCID of the announcement.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific announcement
  oci_announcements_service_announcement_facts:
    announcement_id: ocid1.announcement.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
announcement:
    description:
        - Announcement resource
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the announcement.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        type:
            description:
                - The entity type.
            returned: on success
            type: string
            sample: type_example
        reference_ticket_number:
            description:
                - The reference Jira ticket number.
            returned: on success
            type: string
            sample: reference_ticket_number_example
        summary:
            description:
                - A summary of the issue. A summary might appear in the console banner view of the announcement or in
                  an email subject line. Avoid entering confidential information.
            returned: on success
            type: string
            sample: summary_example
        time_one_title:
            description:
                - "The label associated with an initial time value.
                  Example: `Time Started`"
            returned: on success
            type: string
            sample: Time Started
        time_one_value:
            description:
                - The actual value of the first time value for the event. Typically, this is the time an event started, but the meaning
                  can vary, depending on the announcement type.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_two_title:
            description:
                - "The label associated with a second time value.
                  Example: `Time Ended`"
            returned: on success
            type: string
            sample: Time Ended
        time_two_value:
            description:
                - The actual value of the second time value. Typically, this is the time an event ended, but the meaning
                  can vary, depending on the announcement type.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
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
            type: string
            sample: ACTION_RECOMMENDED
        lifecycle_state:
            description:
                - The current lifecycle state of the announcement.
            returned: on success
            type: string
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
            type: string
            sample: 2019-01-01T17:43:01.389+0000
        time_updated:
            description:
                - "The date and time the announcement was last updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2019-01-01T17:43:01.389+0000`"
            returned: on success
            type: string
            sample: 2019-01-01T17:43:01.389+0000
        description:
            description:
                - A detailed explanation of the event, expressed by using Markdown language. Avoid entering
                  confidential information.
            returned: on success
            type: string
            sample: description_example
        additional_information:
            description:
                - Additional information about the event, expressed by using Markdown language and included in the
                  details view of an announcement. Additional information might include remediation steps or
                  answers to frequently asked questions. Avoid entering confidential information.
            returned: on success
            type: string
            sample: additional_information_example
        affected_resources:
            description:
                - The list of resources, if any, affected by the event described in the announcement.
            returned: on success
            type: complex
            contains:
                resource_id:
                    description:
                        - The OCID of the affected resource.
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                resource_name:
                    description:
                        - The friendly name of the resource.
                    returned: on success
                    type: string
                    sample: resource_name_example
                region:
                    description:
                        - The region where the affected resource exists.
                    returned: on success
                    type: string
                    sample: region_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "type_example",
        "reference_ticket_number": "reference_ticket_number_example",
        "summary": "summary_example",
        "time_one_title": "Time Started",
        "time_one_value": "2013-10-20T19:20:30+01:00",
        "time_two_title": "Time Ended",
        "time_two_value": "2013-10-20T19:20:30+01:00",
        "services": [],
        "affected_regions": [],
        "announcement_type": "ACTION_RECOMMENDED",
        "lifecycle_state": "ACTIVE",
        "is_banner": true,
        "time_created": "2019-01-01T17:43:01.389+0000",
        "time_updated": "2019-01-01T17:43:01.389+0000",
        "description": "description_example",
        "additional_information": "additional_information_example",
        "affected_resources": [{
            "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "resource_name": "resource_name_example",
            "region": "region_example"
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.announcements_service import AnnouncementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AnnouncementFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "announcement_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_announcement,
            announcement_id=self.module.params.get("announcement_id"),
        )


AnnouncementFactsHelperCustom = get_custom_class("AnnouncementFactsHelperCustom")


class ResourceFactsHelper(AnnouncementFactsHelperCustom, AnnouncementFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(announcement_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="announcement",
        service_client_class=AnnouncementClient,
        namespace="announcements_service",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(announcement=result)


if __name__ == "__main__":
    main()
