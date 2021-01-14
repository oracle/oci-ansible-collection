# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


# BDS has a list of nodes. The update operation only updates the tags not the nodes.
# If the user updates the nodes count and reruns, nothing will happen
# because we exclude the nodes from the idempotency check.
# Some node types can be updated using actions.
class BdsInstanceHelperCustom:
    # exclude the attributes from the create model which are not present in the get model for idempotency check
    def get_exclude_attributes(self):
        exclude_attributes = super(
            BdsInstanceHelperCustom, self
        ).get_exclude_attributes()
        return exclude_attributes + [
            "cluster_public_key",
            "cluster_admin_password",
            "nodes",  # Nodes can have different number and types, update is not supported
        ]


class BdsInstanceActionsHelperCustom:
    # exclude the attributes from the action which are not present in the get model for idempotency check
    def get_exclude_attributes(self):
        exclude_attributes = super(
            BdsInstanceActionsHelperCustom, self
        ).get_exclude_attributes()
        return exclude_attributes + [
            "cluster_admin_password",
            "nodes",  # Nodes can have different number and types, update is not supported
        ]

    # We need to check the value of is_cloud_sql_configured to know if SQL is configured for idempotency check
    def is_action_necessary(self, action, resource):
        if (
            action.lower() == "add_cloud_sql"
            and resource.is_cloud_sql_configured is True
        ):
            return False
        if (
            action.lower() == "remove_cloud_sql"
            and resource.is_cloud_sql_configured is False
        ):
            return False
        return super(BdsInstanceActionsHelperCustom, self).is_action_necessary(
            action, resource
        )
