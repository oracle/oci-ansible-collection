# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

from datetime import datetime

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_config_utils,
)

try:
    import oci
    from oci.announcements_service.models import AnnouncementsCollection
    from oci.announcements_service import AnnouncementsPreferencesClient
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False

logger = oci_common_utils.get_logger("oci_announcements_service_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


def utc_now():
    return " " + str(datetime.utcnow()) + ": "


def deserialize_response(data, base_client, class_type):
    x = base_client._BaseClient__deserialize(data, class_type)
    return x


class AnnouncementsCollectionFactsHelperCustom:
    # generated `list_resources` uses pagination supported by Python SDK.
    # Pagination supported by Python SDK strips off the attribute `userStatuses` from response.
    # Thus operation `ListAnnouncements` requires custom pagination.
    # function `list_call_get_all_results_generator` lazily loads results (either all results, or up to a given limit).
    def list_resources(self):
        items = []
        user_statuses = []
        compartment_id = self.module.params.get("compartment_id")
        for response in oci.pagination.list_call_get_all_results_generator(
            self.client.list_announcements, "response", compartment_id
        ):
            items.extend(response.data.items)
            user_statuses.extend(response.data.user_statuses)

        announcements = AnnouncementsCollection()
        announcements.items = items
        announcements.user_statuses = user_statuses
        return announcements


# Deserializing by ourselves as there is issue from service end
# refer: https://jira-sd.mc1.oracleiaas.com/projects/AS/queues/custom/1532/AS-6572
class AnnouncementsPreferencesHelperCustom:
    # As there is error in the spec so we are setting the `skip_deserialization`
    # flag to do de-serialization by ourselves
    def __init__(self, module, resource_type, service_client_class, namespace):
        super(AnnouncementsPreferencesHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )
        self.client = oci_config_utils.create_service_client(
            module,
            AnnouncementsPreferencesClient,
            client_kwargs={"skip_deserialization": True},
        )

    def update_resource(self):
        data = super(AnnouncementsPreferencesHelperCustom, self).update_resource()
        base_client = self.client.base_client
        return base_client._BaseClient__deserialize(
            data, "AnnouncementsPreferencesSummary"
        )

    def get_resource(self):
        resource = super(AnnouncementsPreferencesHelperCustom, self).get_resource()
        base_client = self.client.base_client
        resource.data = base_client._BaseClient__deserialize(
            resource.data, "AnnouncementsPreferences"
        )
        return resource

    # `type` received after getting the resource = `AnnouncementsPreferences`
    # `type` we input in module params = `UpdateAnnouncementsPreferencesDetails`
    # due to mismatch in type we are updating the type of existing resource by input param to handle idempotence
    def is_update_necessary(self, existing_resource_dict):
        logger.debug("Existing Dict {0}".format(existing_resource_dict))
        existing_resource_dict["type"] = self.module.params.get("type")
        return super(AnnouncementsPreferencesHelperCustom, self).is_update_necessary(
            existing_resource_dict
        )


class AnnouncementsPreferencesFactsHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        super(AnnouncementsPreferencesFactsHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )
        self.client = oci_config_utils.create_service_client(
            module,
            AnnouncementsPreferencesClient,
            client_kwargs={"skip_deserialization": True},
        )

    def get_resource(self):
        resource = super(AnnouncementsPreferencesFactsHelperCustom, self).get_resource()
        base_client = self.client.base_client
        resource.data = base_client._BaseClient__deserialize(
            resource.data, "AnnouncementsPreferences"
        )
        return resource

    # When we call the update_resource we get the type as `AnnouncementsPreferences`, so setting same here
    def list_resources(self):
        resource = super(
            AnnouncementsPreferencesFactsHelperCustom, self
        ).list_resources()
        for res in resource:
            if res.get("type") is None:
                res["type"] = "AnnouncementsPreferences"
        base_client = self.client.base_client
        return base_client._BaseClient__deserialize(
            resource, "list[AnnouncementsPreferencesSummary]"
        )


class AnnouncementUserStatusDetailsHelperCustom:
    # Operation `UpdateAnnouncementUserStatus` returns response with no body content.
    # Thus we are returning `AnnouncementUserStatusDetails` of the announcement on which user just performed
    # the update action.
    def update_resource(self):
        super(AnnouncementUserStatusDetailsHelperCustom, self).update_resource()
        return to_dict(self.get_resource().data)
