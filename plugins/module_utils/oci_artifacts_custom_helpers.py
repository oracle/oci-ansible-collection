# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

try:

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ContainerConfigurationHelperCustom:
    # container configuration does not have the module resourceId.
    # It has only update flow. So not considering the check for resourceId to check is_update
    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return True


class ContainerImageActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        """ in remove_container_version, we need to check if the target version is already there in the available version of the resource(image)
        to decide if the remove_container_version action shoud be done """

        if action == "remove_container_version":
            if resource is None:
                return False
            versions = resource.versions
            version_to_delete = self.module.params.get("version")
            is_version_found = False
            for version in versions:
                if version.version == version_to_delete:
                    is_version_found = True
                    break

            if is_version_found:
                return True
            return False

        return super(ContainerImageActionsHelperCustom, self).is_action_necessary(
            action, resource
        )


# similar to BudgetAlertRuleHelperCustom (oci_budget_custom_helpers). Check the
# comments for that on why this is needed.
class ContainerImageSignatureHelperCustom:
    def get_exclude_attributes(self):
        exclude_attrs = super(
            ContainerImageSignatureHelperCustom, self
        ).get_exclude_attributes()
        remove_exclude_attributes = ["msg"]
        exclude_attrs = [x for x in exclude_attrs if x not in remove_exclude_attributes]
        exclude_attrs.append("message")
        return exclude_attrs
