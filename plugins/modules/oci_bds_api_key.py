#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_bds_api_key
short_description: Manage a BdsApiKey resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a BdsApiKey resource in Oracle Cloud Infrastructure
    - For I(state=present), create an API key on behalf of the specified user.
    - "This resource has the following action operations in the M(oracle.oci.oci_bds_api_key_actions) module: test_bds_object_storage_connection."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    bds_instance_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
    user_id:
        description:
            - The OCID of the user for whom this new generated API key pair will be created.
            - Required for create using I(state=present).
        type: str
    passphrase:
        description:
            - Base64 passphrase used to secure the private key which will be created on user behalf.
            - Required for create using I(state=present).
        type: str
    default_region:
        description:
            - The name of the region to establish the Object Storage endpoint. See https://docs.oracle.com/en-us/iaas/api/#/en/identity/20160918/Region/
              for additional information.
        type: str
    key_alias:
        description:
            - User friendly identifier used to uniquely differentiate between different API keys associated with this Big Data Service cluster.
              Only ASCII alphanumeric characters with no spaces allowed.
            - Required for create using I(state=present).
        type: str
    api_key_id:
        description:
            - The API key identifier.
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the BdsApiKey.
            - Use I(state=present) to create a BdsApiKey.
            - Use I(state=absent) to delete a BdsApiKey.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create bds_api_key
  oci_bds_api_key:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    passphrase: passphrase_example
    key_alias: key_alias_example

    # optional
    default_region: default_region_example

- name: Delete bds_api_key
  oci_bds_api_key:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    api_key_id: "ocid1.apikey.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
bds_api_key:
    description:
        - Details of the BdsApiKey resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Identifier of the user's API key.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        user_id:
            description:
                - The user OCID for which this API key was created.
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        key_alias:
            description:
                - User friendly identifier used to uniquely differentiate between different API keys.
                  Only ASCII alphanumeric characters with no spaces allowed.
            returned: on success
            type: str
            sample: key_alias_example
        default_region:
            description:
                - The name of the region to establish the Object Storage endpoint. Example us-phoenix-1 .
            returned: on success
            type: str
            sample: default_region_example
        tenant_id:
            description:
                - The OCID of your tenancy.
            returned: on success
            type: str
            sample: "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx"
        fingerprint:
            description:
                - The fingerprint that corresponds to the public API key requested.
            returned: on success
            type: str
            sample: fingerprint_example
        pemfilepath:
            description:
                - The full path and file name of the private key used for authentication. This location will be automatically selected
                  on the BDS local file system.
            returned: on success
            type: str
            sample: pemfilepath_example
        time_created:
            description:
                - The time the API key was created, shown as an RFC 3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2019-03-29T09:36:42.000+0000"
        lifecycle_state:
            description:
                - The state of the key.
            returned: on success
            type: str
            sample: CREATING
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "key_alias": "key_alias_example",
        "default_region": "default_region_example",
        "tenant_id": "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx",
        "fingerprint": "fingerprint_example",
        "pemfilepath": "pemfilepath_example",
        "time_created": "2019-03-29T09:36:42.000+0000",
        "lifecycle_state": "CREATING"
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
    from oci.bds.models import CreateBdsApiKeyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsApiKeyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_module_resource_id_param(self):
        return "api_key_id"

    def get_module_resource_id(self):
        return self.module.params.get("api_key_id")

    def get_get_fn(self):
        return self.client.get_bds_api_key

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bds_api_key,
            bds_instance_id=self.module.params.get("bds_instance_id"),
            api_key_id=self.module.params.get("api_key_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "bds_instance_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["user_id"]

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
            self.client.list_bds_api_keys, **kwargs
        )

    def get_create_model_class(self):
        return CreateBdsApiKeyDetails

    def get_exclude_attributes(self):
        return ["passphrase"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_bds_api_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                create_bds_api_key_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_bds_api_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                api_key_id=self.module.params.get("api_key_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BdsApiKeyHelperCustom = get_custom_class("BdsApiKeyHelperCustom")


class ResourceHelper(BdsApiKeyHelperCustom, BdsApiKeyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            bds_instance_id=dict(type="str", required=True),
            user_id=dict(type="str"),
            passphrase=dict(type="str", no_log=True),
            default_region=dict(type="str"),
            key_alias=dict(type="str", no_log=True),
            api_key_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="bds_api_key",
        service_client_class=BdsClient,
        namespace="bds",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
