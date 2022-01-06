#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_bds_metastore_configuration
short_description: Manage a BdsMetastoreConfiguration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a BdsMetastoreConfiguration resource in Oracle Cloud Infrastructure
    - For I(state=present), create and activate external metastore configuration.
    - "This resource has the following action operations in the M(oracle.oci.oci_bds_metastore_configuration_actions) module: activate, test."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    bds_instance_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
    display_name:
        description:
            - The display name of the metastore configuration
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    metastore_id:
        description:
            - The OCID of the Data Catalog metastore.
            - Required for create using I(state=present).
        type: str
    bds_api_key_id:
        description:
            - The ID of BDS Api Key used for Data Catalog metastore integration.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    bds_api_key_passphrase:
        description:
            - Base-64 encoded passphrase of the BDS Api Key.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    cluster_admin_password:
        description:
            - Base-64 encoded password for the cluster admin user.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    metastore_config_id:
        description:
            - The metastore configuration ID
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the BdsMetastoreConfiguration.
            - Use I(state=present) to create or update a BdsMetastoreConfiguration.
            - Use I(state=absent) to delete a BdsMetastoreConfiguration.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create bds_metastore_configuration
  oci_bds_metastore_configuration:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    metastore_id: "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx"
    bds_api_key_id: "ocid1.bdsapikey.oc1..xxxxxxEXAMPLExxxxxx"
    bds_api_key_passphrase: bds_api_key_passphrase_example
    cluster_admin_password: example-password

    # optional
    display_name: display_name_example

- name: Update bds_metastore_configuration
  oci_bds_metastore_configuration:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    metastore_config_id: "ocid1.metastoreconfig.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    bds_api_key_id: "ocid1.bdsapikey.oc1..xxxxxxEXAMPLExxxxxx"
    bds_api_key_passphrase: bds_api_key_passphrase_example
    cluster_admin_password: example-password

- name: Update bds_metastore_configuration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_bds_metastore_configuration:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    bds_api_key_id: "ocid1.bdsapikey.oc1..xxxxxxEXAMPLExxxxxx"
    bds_api_key_passphrase: bds_api_key_passphrase_example
    cluster_admin_password: example-password

- name: Delete bds_metastore_configuration
  oci_bds_metastore_configuration:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    metastore_config_id: "ocid1.metastoreconfig.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete bds_metastore_configuration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_bds_metastore_configuration:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
bds_metastore_configuration:
    description:
        - Details of the BdsMetastoreConfiguration resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The ID of the metastore configuration
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of metastore configuration
            returned: on success
            type: str
            sample: display_name_example
        metastore_type:
            description:
                - The type of the metastore in the metastore configuration.
            returned: on success
            type: str
            sample: LOCAL
        metastore_id:
            description:
                - The OCID of the Data Catalog metastore. Set only if metastore's type is EXTERNAL.
            returned: on success
            type: str
            sample: "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx"
        bds_api_key_id:
            description:
                - The ID of BDS API Key used for metastore configuration. Set only if metastore's type is EXTERNAL.
            returned: on success
            type: str
            sample: "ocid1.bdsapikey.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - the lifecycle state of the metastore configuration.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The time when the configuration was created, shown as an RFC 3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the configuration was updated, shown as an RFC 3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "metastore_type": "LOCAL",
        "metastore_id": "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx",
        "bds_api_key_id": "ocid1.bdsapikey.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.bds import BdsClient
    from oci.bds.models import CreateBdsMetastoreConfigurationDetails
    from oci.bds.models import UpdateBdsMetastoreConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsMetastoreConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "metastore_config_id"

    def get_module_resource_id(self):
        return self.module.params.get("metastore_config_id")

    def get_get_fn(self):
        return self.client.get_bds_metastore_configuration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bds_metastore_configuration,
            bds_instance_id=self.module.params.get("bds_instance_id"),
            metastore_config_id=self.module.params.get("metastore_config_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "bds_instance_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["metastore_id", "display_name"]
            if self._use_name_as_identifier()
            else ["metastore_id", "bds_api_key_id", "display_name"]
        )

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_bds_metastore_configurations, **kwargs
        )

    def get_create_model_class(self):
        return CreateBdsMetastoreConfigurationDetails

    def get_exclude_attributes(self):
        return ["bds_api_key_passphrase", "cluster_admin_password"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_bds_metastore_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                create_bds_metastore_configuration_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateBdsMetastoreConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_bds_metastore_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                metastore_config_id=self.module.params.get("metastore_config_id"),
                update_bds_metastore_configuration_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_bds_metastore_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                metastore_config_id=self.module.params.get("metastore_config_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BdsMetastoreConfigurationHelperCustom = get_custom_class(
    "BdsMetastoreConfigurationHelperCustom"
)


class ResourceHelper(
    BdsMetastoreConfigurationHelperCustom, BdsMetastoreConfigurationHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            bds_instance_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            metastore_id=dict(type="str"),
            bds_api_key_id=dict(type="str"),
            bds_api_key_passphrase=dict(type="str", no_log=True),
            cluster_admin_password=dict(type="str", no_log=True),
            metastore_config_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="bds_metastore_configuration",
        service_client_class=BdsClient,
        namespace="bds",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
