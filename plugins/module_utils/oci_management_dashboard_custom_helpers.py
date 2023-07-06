# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils


class ManagementDashboardActionsHelperCustom:
    # Management dashboard's import & export operations belong to different resource, but
    # long back, path overrides was added to add support for these operations in management
    # dashboard resource. Get operation was blacklisted for import & export operations to work.
    # Now, as we add support for get operation, existing actions will stop working.
    # So, raising NotImplementedError for existing operations to work.
    def get_resource(self):
        """Expected to be generated inside the module."""
        raise NotImplementedError("get not supported by {0}".format(self.resource_type))


class ChangeCompartmentActionsHelperCustom:
    # Change_compartment operation belongs to management_dashboard resource, but mvn build throws "Mismatch
    # in primary resource identifier" error during generation. So, We added change_compartment in new
    # resource and it doesn't have get operation. So, adding the get_resource implementation.
    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_dashboard,
            management_dashboard_id=self.module.params.get("management_dashboard_id"),
        )
