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
module: oci_announcements_service_announcement_subscription_actions
short_description: Perform actions on an AnnouncementSubscription resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AnnouncementSubscription resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the specified announcement subscription from one compartment to another compartment. When provided, If-Match is
      checked against ETag values of the resource.
      This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might
      throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service
      might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    announcement_subscription_id:
        description:
            - The OCID of the announcement subscription.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which you want to move the announcement subscription.
        type: str
        required: true
    action:
        description:
            - The action to perform on the AnnouncementSubscription.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on announcement_subscription
  oci_announcements_service_announcement_subscription_actions:
    # required
    announcement_subscription_id: "ocid1.announcementsubscription.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
announcement_subscription:
    description:
        - Details of the AnnouncementSubscription resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
        description:
            description:
                - A description of the announcement subscription. Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
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
        filter_groups:
            description:
                - A list of filter groups for the announcement subscription. A filter group is a combination of multiple filters applied to announcements for
                  matching purposes.
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
                        - A list of filters against which the Announcements service matches announcements. You cannot have more than one of any given filter
                          type within a filter group. You also cannot combine the RESOURCE_ID filter with any other type of filter within a given filter group.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - The type of filter.
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
                - (For announcement subscriptions with Oracle Fusion Applications configured as the service only) The language in which the user prefers to
                  receive emailed announcements. Specify the preference with a value that uses the language tag format (x-obmcs-human-language). For example fr-
                  FR.
            returned: on success
            type: str
            sample: preferred_language_example
        preferred_time_zone:
            description:
                - The time zone that the user prefers for announcement time stamps. Specify the preference with a value that uses the IANA Time Zone Database
                  format (x-obmcs-time-zone). For example America/Los_Angeles.
            returned: on success
            type: str
            sample: preferred_time_zone_example
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "ons_topic_id": "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx",
        "filter_groups": {
            "name": "name_example",
            "filters": [{
                "type": "COMPARTMENT_ID",
                "value": "value_example"
            }]
        },
        "preferred_language": "preferred_language_example",
        "preferred_time_zone": "preferred_time_zone_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.announcements_service import AnnouncementSubscriptionClient
    from oci.announcements_service.models import (
        ChangeAnnouncementSubscriptionCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AnnouncementSubscriptionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "announcement_subscription_id"

    def get_module_resource_id(self):
        return self.module.params.get("announcement_subscription_id")

    def get_get_fn(self):
        return self.client.get_announcement_subscription

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_announcement_subscription,
            announcement_subscription_id=self.module.params.get(
                "announcement_subscription_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeAnnouncementSubscriptionCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_announcement_subscription_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                announcement_subscription_id=self.module.params.get(
                    "announcement_subscription_id"
                ),
                change_announcement_subscription_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


AnnouncementSubscriptionActionsHelperCustom = get_custom_class(
    "AnnouncementSubscriptionActionsHelperCustom"
)


class ResourceHelper(
    AnnouncementSubscriptionActionsHelperCustom,
    AnnouncementSubscriptionActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            announcement_subscription_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="announcement_subscription",
        service_client_class=AnnouncementSubscriptionClient,
        namespace="announcements_service",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
