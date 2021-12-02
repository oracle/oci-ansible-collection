# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = oci_common_utils.get_logger("oci_artifacts_custom_helpers")


def get_logger():
    return logger


def _debug(s):
    get_logger().debug(s)


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

        if action == "restore":
            if resource is None:
                return True
            return False

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

    def get_resource(self):
        """ hanlding the service error for 404 with code REPO_ID_UNKNOWN.
         This response means the resource does not exit"""
        try:
            return oci_common_utils.call_with_backoff(
                self.client.get_container_image,
                image_id=self.module.params.get("image_id"),
            )
        except ServiceError as se:
            if se.status == 404 and se.code == "REPO_ID_UNKNOWN":
                return oci_common_utils.get_default_response_from_resource(
                    resource=None
                )
            raise


# similar to BudgetAlertRuleHelperCustom (oci_budget_custom_helpers). Check the
# comments for that on why this is needed.
class ContainerImageSignatureHelperCustom:
    def get_create_model(self):
        create_model = super(
            ContainerImageSignatureHelperCustom, self
        ).get_create_model()
        if self.module.params.get("msg"):
            setattr(create_model, "message", self.module.params["msg"])
        return create_model

    def get_exclude_attributes(self):
        exclude_attrs = super(
            ContainerImageSignatureHelperCustom, self
        ).get_exclude_attributes()
        exclude_attrs.pop("msg", None)
        exclude_attrs.append("message")
        return exclude_attrs
