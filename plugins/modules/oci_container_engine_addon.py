#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_container_engine_addon
short_description: Manage an Addon resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an Addon resource in Oracle Cloud Infrastructure
    - For I(state=present), install the specified addon for a cluster.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    version:
        description:
            - The version of addon to be installed.
            - This parameter is updatable.
        type: str
    configurations:
        description:
            - Addon configuration details.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            key:
                description:
                    - configuration key name
                type: str
            value:
                description:
                    - configuration value name
                type: str
    cluster_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
    addon_name:
        description:
            - The name of the addon.
        type: str
        required: true
    is_remove_existing_add_on:
        description:
            - Whether existing addon resources should be deleted or not. True would remove the underlying resources completely.
            - Required for delete using I(state=absent).
        type: bool
    state:
        description:
            - The state of the Addon.
            - Use I(state=present) to create or update an Addon.
            - Use I(state=absent) to delete an Addon.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create addon
  oci_container_engine_addon:
    # required
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    addon_name: addon_name_example

    # optional
    version: version_example
    configurations:
    - # optional
      key: key_example
      value: value_example

- name: Update addon
  oci_container_engine_addon:
    # required
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    addon_name: addon_name_example

    # optional
    version: version_example
    configurations:
    - # optional
      key: key_example
      value: value_example

- name: Delete addon
  oci_container_engine_addon:
    # required
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    addon_name: addon_name_example
    is_remove_existing_add_on: true
    state: absent

"""

RETURN = """
addon:
    description:
        - Details of the Addon resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the addon.
            returned: on success
            type: str
            sample: name_example
        version:
            description:
                - selected addon version, or null indicates autoUpdate
            returned: on success
            type: str
            sample: version_example
        current_installed_version:
            description:
                - current installed version of the addon
            returned: on success
            type: str
            sample: current_installed_version_example
        time_created:
            description:
                - The time the cluster was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The state of the addon.
            returned: on success
            type: str
            sample: CREATING
        configurations:
            description:
                - Addon configuration details.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - configuration key name
                    returned: on success
                    type: str
                    sample: key_example
                value:
                    description:
                        - configuration value name
                    returned: on success
                    type: str
                    sample: value_example
        addon_error:
            description:
                - The error info of the addon.
            returned: on success
            type: complex
            contains:
                code:
                    description:
                        - A short error code that defines the upstream error, meant for programmatic parsing. See L(API Errors,https://docs.us-
                          phoenix-1.oraclecloud.com/Content/API/References/apierrors.htm).
                    returned: on success
                    type: str
                    sample: code_example
                message:
                    description:
                        - A human-readable error string of the upstream error.
                    returned: on success
                    type: str
                    sample: message_example
                status:
                    description:
                        - The status of the HTTP response encountered in the upstream error.
                    returned: on success
                    type: str
                    sample: status_example
    sample: {
        "name": "name_example",
        "version": "version_example",
        "current_installed_version": "current_installed_version_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "configurations": [{
            "key": "key_example",
            "value": "value_example"
        }],
        "addon_error": {
            "code": "code_example",
            "message": "message_example",
            "status": "status_example"
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.container_engine import ContainerEngineClient
    from oci.container_engine.models import InstallAddonDetails
    from oci.container_engine.models import UpdateAddonDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AddonHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(AddonHelperGen, self).get_possible_entity_types() + [
            "cluster",
            "clusters",
            "containerEnginecluster",
            "containerEngineclusters",
            "clusterresource",
            "clustersresource",
            "addon",
            "addons",
            "containerEngineaddon",
            "containerEngineaddons",
            "addonresource",
            "addonsresource",
            "containerengine",
        ]

    def get_module_resource_id_param(self):
        return "addon_name"

    def get_module_resource_id(self):
        return self.module.params.get("addon_name")

    def get_get_fn(self):
        return self.client.get_addon

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_addon,
            addon_name=summary_model.name,
            cluster_id=self.module.params.get("cluster_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_addon,
            cluster_id=self.module.params.get("cluster_id"),
            addon_name=self.module.params.get("addon_name"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "cluster_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_addons, **kwargs)

    def get_create_model_class(self):
        return InstallAddonDetails

    def get_exclude_attributes(self):
        return ["addon_name"]

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_addon,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_id=self.module.params.get("cluster_id"),
                install_addon_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateAddonDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_addon,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_id=self.module.params.get("cluster_id"),
                addon_name=self.module.params.get("addon_name"),
                update_addon_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_addon,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_id=self.module.params.get("cluster_id"),
                addon_name=self.module.params.get("addon_name"),
                is_remove_existing_add_on=self.module.params.get(
                    "is_remove_existing_add_on"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AddonHelperCustom = get_custom_class("AddonHelperCustom")


class ResourceHelper(AddonHelperCustom, AddonHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            version=dict(type="str"),
            configurations=dict(
                type="list",
                elements="dict",
                options=dict(key=dict(type="str", no_log=True), value=dict(type="str")),
            ),
            cluster_id=dict(type="str", required=True),
            addon_name=dict(type="str", required=True),
            is_remove_existing_add_on=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="addon",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
