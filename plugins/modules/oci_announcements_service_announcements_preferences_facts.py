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
module: oci_announcements_service_announcements_preferences_facts
short_description: Fetches details about one or multiple AnnouncementsPreferences resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AnnouncementsPreferences resources in Oracle Cloud Infrastructure
    - Gets the current preferences of the tenancy regarding receiving announcements by email.
    - This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might
      throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service
      might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.
    - If I(preference_id) is specified, the details of a single AnnouncementsPreferences will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    preference_id:
        description:
            - The ID of the preference.
            - Required to get a specific announcements_preferences.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple announcements_preferences.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific announcements_preferences
  oci_announcements_service_announcements_preferences_facts:
    # required
    preference_id: "ocid1.preference.oc1..xxxxxxEXAMPLExxxxxx"

- name: List announcements_preferences
  oci_announcements_service_announcements_preferences_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
announcements_preferences:
    description:
        - List of AnnouncementsPreferences resources
    returned: on success
    type: complex
    contains:
        type:
            description:
                - The entity type, which specifies either an object or a summary object for announcement email preferences.
            returned: on success
            type: str
            sample: type_example
        compartment_id:
            description:
                - The OCID of the compartment for which the email preferences apply. Because announcements are
                  specific to a tenancy, specify the tenancy by providing the root compartment OCID.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The ID of the preferences.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        is_unsubscribed:
            description:
                - A Boolean value to indicate whether the specified compartment chooses to not to receive informational announcements by email.
                  (Manage preferences for receiving announcements by email by specifying the `preferenceType` attribute instead.)
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - When the preferences were set initially.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - When the preferences were last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        preference_type:
            description:
                - The string representing the user's preference regarding receiving announcements by email.
            returned: on success
            type: str
            sample: preference_type_example
        preferred_time_zone:
            description:
                - The time zone that the user prefers for announcement time stamps. Specify the preference with a value that uses the IANA Time Zone Database
                  format (x-obmcs-time-zone). For example America/Los_Angeles.
            returned: on success
            type: str
            sample: preferred_time_zone_example
    sample: [{
        "type": "type_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_unsubscribed": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "preference_type": "preference_type_example",
        "preferred_time_zone": "preferred_time_zone_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.announcements_service import AnnouncementsPreferencesClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AnnouncementsPreferencesFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "preference_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_announcements_preference,
            preference_id=self.module.params.get("preference_id"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_announcements_preferences,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AnnouncementsPreferencesFactsHelperCustom = get_custom_class(
    "AnnouncementsPreferencesFactsHelperCustom"
)


class ResourceFactsHelper(
    AnnouncementsPreferencesFactsHelperCustom, AnnouncementsPreferencesFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            preference_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="announcements_preferences",
        service_client_class=AnnouncementsPreferencesClient,
        namespace="announcements_service",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(announcements_preferences=result)


if __name__ == "__main__":
    main()
