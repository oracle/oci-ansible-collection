# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils


class DomainGovernanceHelperCustom:
    # After performing delete operation, we currently wait for only "TERMINATED", "DETACHED", "DELETED" state.
    # Adding INACTIVE state as a wait state.
    def get_wait_for_states_for_operation(self, operation):
        wait_for_states = super(
            DomainGovernanceHelperCustom, self
        ).get_wait_for_states_for_operation(operation)
        if operation == oci_common_utils.DELETE_OPERATION_KEY:
            wait_for_states.append("INACTIVE")
        return wait_for_states


class ChildTenancyHelperCustom:
    def get_get_fn(self):
        # This is just a dummy function so that the waiting logic does not thrown an error. The child tenancy does
        # not have implementation of this method.
        def get_fn(response_id):
            return oci_common_utils.get_default_response_from_resource(resource=None)

        return get_fn


class OrganizationGovernanceActionsHelperCustom:
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(resource=None)
