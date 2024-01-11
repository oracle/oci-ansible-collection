# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

try:
    import oci
    from oci.announcements_service.models import AnnouncementsCollection

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


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


class AnnouncementsPreferencesHelperCustom:
    # `type` received after getting the resource = `AnnouncementsPreferences`
    # `type` we input in module params = `UpdateAnnouncementsPreferencesDetails`
    # due to mismatch in type we are updating the type of existing resource by input param to handle idempotence
    def is_update_necessary(self, existing_resource_dict):
        existing_resource_dict["type"] = self.module.params.get("type")
        return super(AnnouncementsPreferencesHelperCustom, self).is_update_necessary(
            existing_resource_dict
        )
