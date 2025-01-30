# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils


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


class TableHelperCustom:
    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_table, table_name_or_id=summary_model.id,
        ).data


class ReplicaHelperCustom:
    def get_get_fn(self):
        # This is just a dummy function so that the waiting logic does not thrown an error. The replica does
        # not have implementation of this method.
        def get_fn(response_id):
            return oci_common_utils.get_default_response_from_resource(resource=None)

        return get_fn

    # resource does not have a get operation. Dummy implementation to make
    # the base class work. This also means that the delete is not idempotent.
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(resource=None)
