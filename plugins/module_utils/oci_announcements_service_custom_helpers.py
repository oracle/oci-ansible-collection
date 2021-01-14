# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

try:
    import oci
    from oci.announcements_service.models import AnnouncementsCollection
    from oci.util import to_dict

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


class AnnouncementUserStatusDetailsHelperCustom:
    # Operation `UpdateAnnouncementUserStatus` returns response with no body content.
    # Thus we are returning `AnnouncementUserStatusDetails` of the announcement on which user just performed
    # the update action.
    def update_resource(self):
        super(AnnouncementUserStatusDetailsHelperCustom, self).update_resource()
        return to_dict(self.get_resource().data)
