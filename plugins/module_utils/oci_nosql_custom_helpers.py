# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class IndexHelperCustom:
    def is_create(self):
        return self.module.params.get("state") == "present"

    def get_matching_resource(self):
        # if is_if_not_exists is explicitly set to False that means the user wants to disable idempotency
        # which will attmept to create the index and fail if it already exists
        if_not_exists_param_value = self.module.params.get("is_if_not_exists")
        if if_not_exists_param_value is not None and not if_not_exists_param_value:
            return None

        return super(IndexHelperCustom, self).get_matching_resource()


class TableActionsHelperCustom:
    # the super method assumes that the parameter name of the target compartment OCID is compartment_id.
    # But in this case it is to_compartment_id.
    def is_change_compartment_necessary(self, resource):
        if not hasattr(resource, "compartment_id"):
            return False
        if self.module.params.get("to_compartment_id") == resource.compartment_id:
            return False
        return True
