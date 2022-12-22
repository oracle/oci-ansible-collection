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
module: oci_announcements_service_announcement_subscription
short_description: Manage an AnnouncementSubscription resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an AnnouncementSubscription resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new announcement subscription.
    - This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might
      throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service
      might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.
    - "This resource has the following action operations in the M(oracle.oci.oci_announcements_service_announcement_subscription_actions) module:
      change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment where you want to create the announcement
              subscription.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    filter_groups:
        description:
            - A list of filter groups for the announcement subscription. A filter group combines one or more filters that the Announcements service applies to
              announcements for matching purposes.
        type: dict
        suboptions:
            filters:
                description:
                    - A list of filters against which the Announcements service matches announcements. You cannot have more than one of any given filter type
                      within a filter group.
                type: list
                elements: dict
                required: true
                suboptions:
                    type:
                        description:
                            - The type of filter.
                        type: str
                        choices:
                            - "COMPARTMENT_ID"
                            - "PLATFORM_TYPE"
                            - "REGION"
                            - "SERVICE"
                            - "RESOURCE_ID"
                            - "ANNOUNCEMENT_TYPE"
                        required: true
                    value:
                        description:
                            - The value of the filter.
                        type: str
                        required: true
    display_name:
        description:
            - A user-friendly name for the announcement subscription. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A description of the announcement subscription. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    ons_topic_id:
        description:
            - The OCID of the Notifications service topic that is the target for publishing announcements that match the configured announcement subscription.
              The caller of the operation needs the ONS_TOPIC_PUBLISH permission for the targeted Notifications service topic. For more information about
              Notifications permissions, see L(Details for
              Notifications,https://docs.cloud.oracle.com/Content/Identity/policyreference/notificationpolicyreference.htm).
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    preferred_language:
        description:
            - (For announcement subscriptions with Oracle Fusion Applications configured as the service only) The language in which the user prefers to receive
              emailed announcements. Specify the preference with a value that uses the language tag format (x-obmcs-human-language). For example fr-FR.
            - This parameter is updatable.
        type: str
    preferred_time_zone:
        description:
            - The time zone that the user prefers for announcement time stamps. Specify the preference with a value that uses the IANA Time Zone Database format
              (x-obmcs-time-zone). For example America/Los_Angeles.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    announcement_subscription_id:
        description:
            - The OCID of the announcement subscription.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the AnnouncementSubscription.
            - Use I(state=present) to create or update an AnnouncementSubscription.
            - Use I(state=absent) to delete an AnnouncementSubscription.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create announcement_subscription
  oci_announcements_service_announcement_subscription:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    ons_topic_id: "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    filter_groups:
      # required
      filters:
      - # required
        type: COMPARTMENT_ID
        value: value_example
    description: description_example
    preferred_language: preferred_language_example
    preferred_time_zone: preferred_time_zone_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update announcement_subscription
  oci_announcements_service_announcement_subscription:
    # required
    announcement_subscription_id: "ocid1.announcementsubscription.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    ons_topic_id: "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx"
    preferred_language: preferred_language_example
    preferred_time_zone: preferred_time_zone_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update announcement_subscription using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_announcements_service_announcement_subscription:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    ons_topic_id: "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx"
    preferred_language: preferred_language_example
    preferred_time_zone: preferred_time_zone_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete announcement_subscription
  oci_announcements_service_announcement_subscription:
    # required
    announcement_subscription_id: "ocid1.announcementsubscription.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete announcement_subscription using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_announcements_service_announcement_subscription:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.announcements_service import AnnouncementSubscriptionClient
    from oci.announcements_service.models import CreateAnnouncementSubscriptionDetails
    from oci.announcements_service.models import UpdateAnnouncementSubscriptionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AnnouncementSubscriptionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            AnnouncementSubscriptionHelperGen, self
        ).get_possible_entity_types() + [
            "announcementsubscription",
            "announcementsubscriptions",
            "announcementsServiceannouncementsubscription",
            "announcementsServiceannouncementsubscriptions",
            "announcementsubscriptionresource",
            "announcementsubscriptionsresource",
            "announcementsservice",
        ]

    def get_module_resource_id_param(self):
        return "announcement_subscription_id"

    def get_module_resource_id(self):
        return self.module.params.get("announcement_subscription_id")

    def get_get_fn(self):
        return self.client.get_announcement_subscription

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_announcement_subscription,
            announcement_subscription_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_announcement_subscription,
            announcement_subscription_id=self.module.params.get(
                "announcement_subscription_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_announcement_subscriptions, **kwargs
        )

    def get_create_model_class(self):
        return CreateAnnouncementSubscriptionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_announcement_subscription,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_announcement_subscription_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateAnnouncementSubscriptionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_announcement_subscription,
            call_fn_args=(),
            call_fn_kwargs=dict(
                announcement_subscription_id=self.module.params.get(
                    "announcement_subscription_id"
                ),
                update_announcement_subscription_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_announcement_subscription,
            call_fn_args=(),
            call_fn_kwargs=dict(
                announcement_subscription_id=self.module.params.get(
                    "announcement_subscription_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


AnnouncementSubscriptionHelperCustom = get_custom_class(
    "AnnouncementSubscriptionHelperCustom"
)


class ResourceHelper(
    AnnouncementSubscriptionHelperCustom, AnnouncementSubscriptionHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            filter_groups=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            ons_topic_id=dict(type="str"),
            preferred_language=dict(type="str"),
            preferred_time_zone=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            announcement_subscription_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
