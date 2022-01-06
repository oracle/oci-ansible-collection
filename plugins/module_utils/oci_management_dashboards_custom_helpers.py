# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


try:
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagementDashboardActionsHelperCustom:
    """
    Customizes the ManagementDashboardActionsHelperGen.
    """

    def perform_action(self, action):
        """
        Overrides the base to invoke the actions for this
        resource as they dont need an explicit get_resource call.
        """

        action_fn = self.get_action_fn(action)
        if not action_fn:
            self.module.fail_json(msg="{0} not supported by the module.".format(action))

        if self.check_mode:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(action),
                resource=None,
            )

        try:
            action_return = action_fn()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            resource = None
            if action == "export_dashboard":
                # the export_dashboard action returns the
                # dashboard details for the dashboard exported
                resource = to_dict(action_return)

            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(action),
                resource=resource,
            )
