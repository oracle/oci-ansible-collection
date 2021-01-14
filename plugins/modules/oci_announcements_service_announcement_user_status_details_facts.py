#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_announcements_service_announcement_user_status_details_facts
short_description: Fetches details about a AnnouncementUserStatusDetails resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AnnouncementUserStatusDetails resource in Oracle Cloud Infrastructure
    - Gets information about whether a specific announcement was acknowledged by a user.
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
- name: Get a specific announcement_user_status_details
  oci_announcements_service_announcement_user_status_details_facts:
    announcement_id: ocid1.announcement.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
announcement_user_status_details:
    description:
        - AnnouncementUserStatusDetails resource
    returned: on success
    type: complex
    contains:
        user_status_announcement_id:
            description:
                - The OCID of the announcement that this status is associated with.
            returned: on success
            type: string
            sample: ocid1.userstatusannouncement.oc1..xxxxxxEXAMPLExxxxxx
        user_id:
            description:
                - The OCID of the user that this status is associated with.
            returned: on success
            type: string
            sample: ocid1.user.oc1..xxxxxxEXAMPLExxxxxx
        time_acknowledged:
            description:
                - "The date and time the announcement was acknowledged, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2019-01-01T17:43:01.389+0000`"
            returned: on success
            type: string
            sample: 2019-01-01T17:43:01.389+0000
    sample: {
        "user_status_announcement_id": "ocid1.userstatusannouncement.oc1..xxxxxxEXAMPLExxxxxx",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "time_acknowledged": "2019-01-01T17:43:01.389+0000"
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


class AnnouncementUserStatusDetailsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "announcement_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_announcement_user_status,
            announcement_id=self.module.params.get("announcement_id"),
        )


AnnouncementUserStatusDetailsFactsHelperCustom = get_custom_class(
    "AnnouncementUserStatusDetailsFactsHelperCustom"
)


class ResourceFactsHelper(
    AnnouncementUserStatusDetailsFactsHelperCustom,
    AnnouncementUserStatusDetailsFactsHelperGen,
):
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
        resource_type="announcement_user_status_details",
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

    module.exit_json(announcement_user_status_details=result)


if __name__ == "__main__":
    main()
