# Copyright (c) 2017, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.oracle import oci_common_utils


try:
    import oci

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


class ConfigurationHelperCustom:
    ## This is one of the cases where the module does not have a resource_id.
    ## base class is_update method depends on having a resource_id. So override this method to return True
    ## as this is the only operation supported by the module oci_configuration
    def is_update(self):
        return True

    def update_resource(self):
        ## The update operation currently returns a work request id but the AuditClient currently does not support
        ## waiting for the work request. So wait until the configuration is updated by checking the value.
        super(ConfigurationHelperCustom, self).update_resource()
        get_response = self.get_resource()
        waiter_response = oci.wait_until(
            self.client,
            get_response,
            evaluate_response=lambda r: r.data.retention_period_days
            == self.module.params.get("retention_period_days"),
            max_wait_seconds=self.module.params.get(
                "wait_timeout", oci_common_utils.MAX_WAIT_TIMEOUT_IN_SECONDS
            ),
        )
        return waiter_response.data
