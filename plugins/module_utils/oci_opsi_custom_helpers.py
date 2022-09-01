# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils


class DatabaseInsightsActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        return True

    # action module performs operations on underlying databases and not database insight.
    # database insight is not infrastructure resource. Hence get_resource is not applicable here.
    # This is dummy implementation so that other method works.
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(resource=None)


class HostInsightHelperCustom:
    def get_entity_type(self):
        return "opsidatabaseinsight"


class HostInsightActionsHelperCustom:
    ENABLE_ACTION_KEY = "enable"
    DISABLE_ACTION_KEY = "disable"
    RESOURCE_OPERATION_INSIGHTS_STATUS_ATTR = "status"
    STATUS_ENABLED = "ENABLED"
    STATUS_DISABLED = "DISABLED"

    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        if action == self.ENABLE_ACTION_KEY:
            if (
                getattr(resource, self.RESOURCE_OPERATION_INSIGHTS_STATUS_ATTR, None)
                == self.STATUS_ENABLED
            ):
                return False
            return True
        if action == self.DISABLE_ACTION_KEY:
            if (
                getattr(resource, self.RESOURCE_OPERATION_INSIGHTS_STATUS_ATTR, None)
                == self.STATUS_DISABLED
            ):
                return False
            return True
        return super(HostInsightActionsHelperCustom, self).is_action_necessary(
            action, resource
        )


class OperationsInsightsWarehouseHelperCustom:
    def get_entity_type(self):
        return "opsiwarehouse"


class OperationsInsightsWarehouseUserHelperCustom:
    def get_entity_type(self):
        return "opsiwarehouseuser"
