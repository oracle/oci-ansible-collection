# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class CustomTableHelperCustom:
    def get_get_model_from_summary_model(self, summary_model):
        get_model = super(
            CustomTableHelperCustom, self
        ).get_get_model_from_summary_model(summary_model)

        # compartment_depth property comes as null in GET resource
        # but in list resources compartment_depth is populated.
        # to maintain idempotency, we again call list api to get all the resources
        # and set the compartment_depth in the get model
        if not get_model.saved_custom_table.compartment_depth:
            resource_list = self.list_resources()
            for resource in resource_list:
                if resource.id == get_model.id:
                    get_model.saved_custom_table.compartment_depth = (
                        resource.saved_custom_table.compartment_depth
                    )
                    break

        return get_model


class ScheduleHelperCustom:
    def get_resource_terminated_states(self):
        return super(ScheduleHelperCustom, self).get_resource_terminated_states() + [
            "INACTIVE"
        ]

    def is_resource_dead(self, resource):
        if super(ScheduleHelperCustom, self).is_resource_dead(resource):
            return True
        if hasattr(resource, "lifecycle_state") and (
            resource.lifecycle_state in ["INACTIVE"]
        ):
            return True
        return False
