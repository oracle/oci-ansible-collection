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
module: oci_bds_api_key_actions
short_description: Perform actions on a BdsApiKey resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a BdsApiKey resource in Oracle Cloud Infrastructure
    - For I(action=test_bds_object_storage_connection), test access to specified Object Storage bucket using the API key.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    bds_instance_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
    api_key_id:
        description:
            - The API key identifier.
        type: str
        aliases: ["id"]
        required: true
    object_storage_uri:
        description:
            - An Oracle Cloud Infrastructure URI to which this connection must be attempted. See
              https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
        type: str
        required: true
    passphrase:
        description:
            - Base64 passphrase used to secure the private key which will be created on user behalf.
        type: str
        required: true
    object_storage_region:
        description:
            - The name of the region to establish the Object Storage endpoint. Example us-phoenix-1 .
        type: str
    action:
        description:
            - The action to perform on the BdsApiKey.
        type: str
        required: true
        choices:
            - "test_bds_object_storage_connection"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action test_bds_object_storage_connection on bds_api_key
  oci_bds_api_key_actions:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    api_key_id: "ocid1.apikey.oc1..xxxxxxEXAMPLExxxxxx"
    object_storage_uri: object_storage_uri_example
    passphrase: passphrase_example
    action: test_bds_object_storage_connection

    # optional
    object_storage_region: object_storage_region_example

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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.bds import BdsClient
    from oci.bds.models import TestBdsObjectStorageConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsApiKeyActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        test_bds_object_storage_connection
    """

    @staticmethod
    def get_module_resource_id_param():
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

    def test_bds_object_storage_connection(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, TestBdsObjectStorageConnectionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.test_bds_object_storage_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                api_key_id=self.module.params.get("api_key_id"),
                test_bds_object_storage_connection_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BdsApiKeyActionsHelperCustom = get_custom_class("BdsApiKeyActionsHelperCustom")


class ResourceHelper(BdsApiKeyActionsHelperCustom, BdsApiKeyActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            bds_instance_id=dict(type="str", required=True),
            api_key_id=dict(aliases=["id"], type="str", required=True),
            object_storage_uri=dict(type="str", required=True),
            passphrase=dict(type="str", required=True, no_log=True),
            object_storage_region=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=["test_bds_object_storage_connection"],
            ),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
