# Copyright (c) 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.oracle import oci_common_utils, oci_waas_utils


try:
    import oci

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


class WaasPolicyHelperCustom:
    def list_resources(self):
        return [
            oci_common_utils.call_with_backoff(
                self.client.get_waas_policy, waas_policy_id=waas_policy_summary.id
            ).data
            for waas_policy_summary in super(
                WaasPolicyHelperCustom, self
            ).list_resources()
        ]

    def create_wait(self, create_response):
        work_request_response = self.wait_for_work_request(
            create_response, oci_common_utils.WORK_REQUEST_COMPLETED_STATES
        )
        for work_request_resource in work_request_response.data.resources:
            if (
                work_request_resource.entity_type == "waas"
                and work_request_resource.action_type == "CREATED"
            ):
                waas_policy_id = work_request_resource.identifier
                break
        if not waas_policy_id:
            self.module.fail_json(
                msg="Cound not get the waas policy id from the work request."
            )
        waas_policy = oci_common_utils.call_with_backoff(
            self.client.get_waas_policy, waas_policy_id=waas_policy_id
        ).data
        if not waas_policy:
            self.module.fail_json(
                "Could not get the waas policy resource after creation."
            )
        if waas_policy.lifecycle_state in oci_common_utils.DEAD_STATES:
            self.module.fail_json(
                msg="WAAS policy created but in {0} state.".format(
                    waas_policy.lifecycle_state
                )
            )
        return waas_policy
