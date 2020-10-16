# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.log_analytics.models import Namespace
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NamespaceActionsHelperCustom:
    # As per API documentation `GetNamespace` gets the namespace details of a tenancy already on-boarded.
    # if tenancy is off-boarded API returns 404.
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            resource=oci_common_utils.convert_input_data_to_model_class(
                self.module.params, Namespace
            )
        )

    def is_action_necessary(self, action, resource=None):

        # check if tenancy is already on-boarded
        if action == "onboard":
            try:
                oci_common_utils.call_with_backoff(
                    self.client.get_namespace,
                    namespace_name=self.module.params.get("namespace_name"),
                )
                return False
            except ServiceError as se:
                if se.status == 404:
                    return True
                self.module.fail_json(msg=se.message)

        # check if tenancy is already off-boarded
        elif action == "offboard":
            try:
                oci_common_utils.call_with_backoff(
                    self.client.get_namespace,
                    namespace_name=self.module.params.get("namespace_name"),
                )
                return True
            except ServiceError as se:
                if se.status == 404:
                    return False
                self.module.fail_json(msg=se.message)

        return super(NamespaceActionsHelperCustom, self).is_action_necessary(
            action, resource
        )
