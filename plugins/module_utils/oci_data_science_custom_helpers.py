# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

logger = oci_common_utils.get_logger("oci_data_science_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


try:
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceModelArtifactHelperCustom:
    # there is no concept of idempotency for this module.
    # it re-executes create new model artifact every time module is invoked.
    def get_matching_resource(self):
        return None

    def is_create(self):
        return True

    def get_module_resource_id_param(self):
        return "model_id"

    def get_module_resource_id(self):
        return self.module.params.get("model_id")


class DataScienceModelDeploymentHelperCustom:
    # exclude the description attribute as the idempotence test does not return the description param
    def get_exclude_attributes(self):
        exclude_attributes = super(
            DataScienceModelDeploymentHelperCustom, self
        ).get_exclude_attributes()
        return exclude_attributes + [
            "description",
        ]


class DataScienceModelProvenanceHelperCustom:
    # Get will fail before create
    def get_matching_resource(self):
        return None

    # Use the Get return value to know if it is a create or update
    def is_create(self):
        if self.get_existing_resource_dict_for_update() == dict():
            return True
        return False

    # If you don't get 404, it is an update operation
    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        if self.get_existing_resource_dict_for_update() == dict():
            return False
        return True

    # Get will return a 404 if the Provenance is not created
    def get_existing_resource_dict_for_update(self):
        try:
            get_response = self.get_resource()
        except ServiceError as se:
            if se.status != 404:
                raise
            return dict()
        else:
            return to_dict(get_response.data)


class DataScienceJobHelperCustom:
    def get_resource_active_states(self):
        wait_for_states = super(
            DataScienceJobHelperCustom, self
        ).get_resource_active_states()
        wait_for_states.append("CREATING")
        return wait_for_states


class DataScienceJobRunActionsHelperCustom:
    # adding state 'CANCELING' to the list returned by `get_action_idempotent_states(action)` when performing
    # `cancel` operation.
    def get_action_idempotent_states(self, action):
        action_idempotent_states = super(
            DataScienceJobRunActionsHelperCustom, self
        ).get_action_idempotent_states(action)

        if action.lower() == "cancel":
            return action_idempotent_states + [
                "CANCELING",
            ]
        return action_idempotent_states
