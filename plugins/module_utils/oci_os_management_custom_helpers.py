# Copyright (c) 2020 Oracle and/or its affiliates.
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


logger = oci_common_utils.get_logger("oci_os_management_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


class ManagedInstanceActionsHelperCustom:
    def is_package_installed(self, package_name, list_packages_kwargs):
        installed_packages = oci_common_utils.list_all_resources(
            self.client.list_packages_installed_on_managed_instance,
            **list_packages_kwargs
        )

        return any(
            [True for package in installed_packages if package.name == package_name]
        )

    def is_action_necessary(self, action, resource=None):
        managed_instance = resource or self.get_resource().data
        package_to_act_on = self.module.params.get("software_package_name")

        # remove_package returns an error if you try to remove a package that is already removed
        if action == "remove_package":
            kwargs = {
                "managed_instance_id": self.module.params.get("managed_instance_id")
            }

            if not self.is_package_installed(package_to_act_on, kwargs):
                return False
        elif action == "install_package":
            kwargs = {
                "managed_instance_id": self.module.params.get("managed_instance_id")
            }

            # fetching all installed packages can take a while (several minutes) and many API calls
            # thus we try to search for the package to get its display name from its package name
            # if we get this successfully, we use it as a filter on the list_installed_packages call
            # to make it more efficient
            try:
                search_results = self.client.search_software_packages(
                    software_package_name=package_to_act_on
                ).data
                if search_results and len(search_results) == 1:
                    display_name_filter = search_results[0].display_name
                    kwargs["display_name"] = display_name_filter
            except ServiceError:
                pass

            if self.is_package_installed(package_to_act_on, kwargs):
                return False
        elif action == "install_package_update":
            kwargs = {
                "managed_instance_id": self.module.params.get("managed_instance_id")
            }

            # fetching all installed packages can take a while (several minutes) and many API calls
            # thus we try to search for the package to get its display name from its package name
            # if we get this successfully, we use it as a filter on the list_installed_packages call
            # to make it more efficient
            try:
                search_results = self.client.search_software_packages(
                    software_package_name=package_to_act_on
                ).data
                if search_results and len(search_results) == 1:
                    display_name_filter = search_results[0].display_name
                    kwargs["display_name"] = display_name_filter
            except ServiceError:
                pass

            if self.is_package_installed(package_to_act_on, kwargs):
                return False
        elif action == "install_windows_update":
            kwargs = {
                "managed_instance_id": self.module.params.get("managed_instance_id")
            }

            installed_updates = oci_common_utils.list_all_resources(
                self.client.list_windows_updates_installed_on_managed_instance, **kwargs
            )

            installed_updates_matching_name = [
                update
                for update in installed_updates
                if update.name == self.module.params.get("windows_update_name")
            ]
            update_is_installed = len(installed_updates_matching_name) != 0
            if update_is_installed:
                return False
        elif action == "install_all_windows_updates":
            kwargs = {
                "managed_instance_id": self.module.params.get("managed_instance_id")
            }

            available_windows_updates = oci_common_utils.list_all_resources(
                self.client.list_available_windows_updates_for_managed_instance,
                **kwargs
            )

            if len(available_windows_updates) == 0:
                return False
        elif action == "install_all_package_updates":
            kwargs = {
                "managed_instance_id": self.module.params.get("managed_instance_id")
            }

            available_updates = oci_common_utils.list_all_resources(
                self.client.list_available_updates_for_managed_instance, **kwargs
            )

            if len(available_updates) == 0:
                return False
        elif action == "attach_child_software_source":
            if managed_instance.child_software_sources:
                matching_software_sources = [
                    software_source
                    for software_source in managed_instance.child_software_sources
                    if software_source.id
                    == self.module.params.get("software_source_id")
                ]
                if len(matching_software_sources) > 0:
                    return False
        elif action == "detach_child_software_source":
            if not managed_instance.child_software_sources:
                return False

            matching_software_sources = [
                software_source
                for software_source in managed_instance.child_software_sources
                if software_source.id == self.module.params.get("software_source_id")
            ]
            if len(matching_software_sources) == 0:
                return False
        elif action == "attach_parent_software_source":
            if managed_instance.parent_software_source:
                if (
                    managed_instance.parent_software_source.id
                    == self.module.params.get("software_source_id")
                ):
                    return False
        elif action == "detach_parent_software_source":
            if not managed_instance.parent_software_source:
                # there can only be one parent software source
                # so if there is no current parent software source, we bypass the detach operation
                # if there *is* a parent software source with a different ID than "software_source_id" from the user
                # we will pass the request through to the service which will return an error. This is appropriate because
                # otherwise we are swallowing what is likely a mistake on the part of the user
                return False

        return True


class ManagedInstanceGroupActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        managed_instance_group = resource or self.get_resource().data
        managed_instance_id = self.module.params.get("managed_instance_id")
        matching_managed_instances = [
            managed_instance
            for managed_instance in managed_instance_group.managed_instances
            if managed_instance.id == managed_instance_id
        ]

        if action == "attach_managed_instance":
            if len(matching_managed_instances) > 0:
                return False
        if action == "detach_managed_instance":
            if len(matching_managed_instances) == 0:
                return False

        return True


class SoftwareSourceActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        software_source_packages = oci_common_utils.list_all_resources(
            self.client.list_software_source_packages,
            software_source_id=self.module.params.get("software_source_id"),
        )
        software_source_package_names = [
            software_source_package.name
            for software_source_package in software_source_packages
        ]
        if action == "add_packages":
            package_names_to_add = self.module.params.get("package_names")
            all_packages_already_added = True
            for package_name_to_add in package_names_to_add:
                if package_name_to_add not in software_source_package_names:
                    all_packages_already_added = False

            if all_packages_already_added:
                return False
        elif action == "remove_packages":
            package_names_to_remove = self.module.params.get("package_names")
            all_packages_already_absent = True
            for package_name_to_remove in package_names_to_remove:
                if package_name_to_remove in software_source_package_names:
                    all_packages_already_absent = False

            if all_packages_already_absent:
                return False

        return True
