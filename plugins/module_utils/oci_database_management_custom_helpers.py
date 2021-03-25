# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

logger = oci_common_utils.get_logger("oci_database_management_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def _info(s):
    get_logger().info(s)


def get_logger():
    return logger


class ManagedDatabaseGroupActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        managed_dbs_list = getattr(resource, "managed_databases", None) or []
        _debug(
            "MDB Resource details {0} {1} {2}".format(
                managed_dbs_list, action, self.module.params.get("managed_database_id")
            )
        )
        if action == "add_managed_database":
            if managed_dbs_list:
                managed_db_ids = [
                    getattr(managed_db, "id", None) for managed_db in managed_dbs_list
                ]
                if (
                    managed_db_ids
                    and self.module.params.get("managed_database_id") in managed_db_ids
                ):
                    return False
                else:
                    return True
            else:
                return True
        elif action == "remove_managed_database":
            if managed_dbs_list:
                managed_db_ids = [
                    getattr(managed_db, "id", None) for managed_db in managed_dbs_list
                ]
                if (
                    managed_db_ids
                    and self.module.params.get("managed_database_id") in managed_db_ids
                ):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return super(
                ManagedDatabaseGroupActionsHelperCustom, self
            ).is_action_necessary(action, resource)
