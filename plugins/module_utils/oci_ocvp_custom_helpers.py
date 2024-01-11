# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

try:

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SddcActionsHelperCustom:
    CANCEL_DOWNGRADE_HCX_ACTION_KEY = "cancel_downgrade_hcx"
    DOWNGRADE_HCX_ACTION_KEY = "downgrade_hcx"
    UPGRADE_HCX_ACTION_KEY = "upgrade_hcx"

    def is_action_necessary(self, action, resource=None):
        if action == self.DOWNGRADE_HCX_ACTION_KEY:
            if hasattr(resource, "is_hcx_enterprise_enabled") and hasattr(
                resource, "is_hcx_pending_downgrade"
            ):
                if (
                    resource.is_hcx_enterprise_enabled
                    and not resource.is_hcx_pending_downgrade
                ):
                    return True
                return False
            return True
        elif action == self.CANCEL_DOWNGRADE_HCX_ACTION_KEY:
            if hasattr(resource, "is_hcx_pending_downgrade") and hasattr(
                resource, "is_hcx_enterprise_enabled"
            ):
                if (
                    resource.is_hcx_enterprise_enabled
                    and resource.is_hcx_pending_downgrade
                ):
                    return True
                return False
            return True
        elif action == self.UPGRADE_HCX_ACTION_KEY:
            if hasattr(resource, "is_hcx_enterprise_enabled") and hasattr(
                resource, "is_hcx_pending_downgrade"
            ):
                if (
                    resource.is_hcx_enterprise_enabled
                    and not resource.is_hcx_pending_downgrade
                ):
                    return False
                return True
            return True
        return super(SddcActionsHelperCustom, self).is_action_necessary(
            action, resource
        )
