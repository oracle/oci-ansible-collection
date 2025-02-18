# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_config_utils

try:
    from oci.cloud_bridge.common_client import CommonClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AgentActionsHelperCustom:
    def get_waiter_client(self):
        # agent resource has a separate client but uses CommonClient for work request.
        return oci_config_utils.create_service_client(self.module, CommonClient)


class AgentDependencyHelperCustom:
    def get_waiter_client(self):
        # agent_dependency resource has a separate client but uses CommonClient for work request.
        return oci_config_utils.create_service_client(self.module, CommonClient)


class AssetSourceHelperCustom:
    def get_waiter_client(self):
        # asset_source resource has a separate client but uses CommonClient for work request.
        return oci_config_utils.create_service_client(self.module, CommonClient)


class AssetSourceActionsHelperCustom:
    def get_waiter_client(self):
        # asset_source resource has a separate client but uses CommonClient for work request.
        return oci_config_utils.create_service_client(self.module, CommonClient)


class EnvironmentActionsHelperCustom:
    def get_waiter_client(self):
        # environment resource has a separate client but uses CommonClient for work request.
        return oci_config_utils.create_service_client(self.module, CommonClient)


class InventoryHelperCustom:
    def get_waiter_client(self):
        # inventory resource has a separate client but uses CommonClient for work request.
        return oci_config_utils.create_service_client(self.module, CommonClient)


class InventoryActionsHelperCustom:
    def get_waiter_client(self):
        # inventory resource has a separate client but uses CommonClient for work request.
        return oci_config_utils.create_service_client(self.module, CommonClient)
