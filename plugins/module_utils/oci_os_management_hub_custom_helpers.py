# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils


class OsManagementHubInstallAllWindowsUpdatesInCompartmentActionsHelperCustom:
    # resource does not have a get operation. Dummy implementation to make
    # the base class work. This also means that the delete is not idempotent.
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(resource=None)


class OsManagementHubUpdateAllPackagesInCompartmentActionsHelperCustom:
    # resource does not have a get operation. Dummy implementation to make
    # the base class work. This also means that the delete is not idempotent.
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(resource=None)


class OsManagementHubManagementStationsMirrorActionsHelperCustom:
    # resource does not have a get operation. Dummy implementation to make
    # the base class work. This also means that the delete is not idempotent.
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(resource=None)
