# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils._text import to_text
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.util import to_dict
    from oci.container_engine.models import UpdateClusterEndpointConfigDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class KubeconfigHelperCustom:
    def create_resource(self):
        response_data = super(KubeconfigHelperCustom, self).create_resource()
        return to_text(response_data.content)


class ClusterHelperCustom:
    def get_default_module_wait_timeout(self):
        return 1800


class ClusterActionsHelperCustom:
    UPDATE_CLUSTER_ENDPOINT_CONFIG_KEY = "update_cluster_endpoint_config"

    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        if action == self.UPDATE_CLUSTER_ENDPOINT_CONFIG_KEY:
            action_details = oci_common_utils.convert_input_data_to_model_class(
                self.module.params, UpdateClusterEndpointConfigDetails
            )
            return not oci_common_utils.compare_dicts(
                to_dict(action_details),
                to_dict(getattr(resource, "endpoint_config", None)),
            )
        return super(ClusterActionsHelperCustom, self).is_action_necessary(
            action, resource
        )
