# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils


class ResourceActionActionsHelperCustom:
    """
    resource_action_id is required for get_operation which we do not pass as the model for the action, does not require
    that hence setting it non for get_resource()
    """

    def get_resource(self):
        if self.module.params.get("action") == "filter":
            return oci_common_utils.get_default_response_from_resource(resource=None)
        return super(ResourceActionActionsHelperCustom, self).get_resource()


class RecommendationActionsHelperCustom:
    BULK_APPLY_ACTION = "bulk_apply"

    # always preforming action operation and not checking idempotency
    # this action updates resource_actions related to the recommendation
    # which will require multiple GET api calls for idempotency check, skipping it for now
    def is_action_necessary(self, action, resource=None):
        if action == self.BULK_APPLY_ACTION:
            return True
