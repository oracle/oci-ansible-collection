#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_bds_metastore_configuration_actions
short_description: Perform actions on a BdsMetastoreConfiguration resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a BdsMetastoreConfiguration resource in Oracle Cloud Infrastructure
    - For I(action=activate), activate specified metastore configuration.
    - For I(action=test), test specified metastore configuration.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    bds_api_key_passphrase:
        description:
            - Base-64 encoded passphrase of the BDS Api Key. Set only if metastore's type is EXTERNAL.
            - Applicable only for I(action=activate).
        type: str
    bds_instance_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
    metastore_config_id:
        description:
            - The metastore configuration ID
        type: str
        aliases: ["id"]
        required: true
    cluster_admin_password:
        description:
            - Base-64 encoded password for the cluster admin user.
        type: str
        required: true
    action:
        description:
            - The action to perform on the BdsMetastoreConfiguration.
        type: str
        required: true
        choices:
            - "activate"
            - "test"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action activate on bds_metastore_configuration
  oci_bds_metastore_configuration_actions:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    metastore_config_id: "ocid1.metastoreconfig.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: activate

    # optional
    bds_api_key_passphrase: bds_api_key_passphrase_example

- name: Perform action test on bds_metastore_configuration
  oci_bds_metastore_configuration_actions:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    metastore_config_id: "ocid1.metastoreconfig.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: test

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

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.bds import BdsClient
    from oci.bds.models import ActivateBdsMetastoreConfigurationDetails
    from oci.bds.models import TestBdsMetastoreConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsMetastoreConfigurationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        activate
        test
    """

    @staticmethod
    def get_module_resource_id_param():
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

    def activate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ActivateBdsMetastoreConfigurationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.activate_bds_metastore_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                metastore_config_id=self.module.params.get("metastore_config_id"),
                activate_bds_metastore_configuration_details=action_details,
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

    def test(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, TestBdsMetastoreConfigurationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.test_bds_metastore_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                metastore_config_id=self.module.params.get("metastore_config_id"),
                test_bds_metastore_configuration_details=action_details,
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


BdsMetastoreConfigurationActionsHelperCustom = get_custom_class(
    "BdsMetastoreConfigurationActionsHelperCustom"
)


class ResourceHelper(
    BdsMetastoreConfigurationActionsHelperCustom,
    BdsMetastoreConfigurationActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            bds_api_key_passphrase=dict(type="str", no_log=True),
            bds_instance_id=dict(type="str", required=True),
            metastore_config_id=dict(aliases=["id"], type="str", required=True),
            cluster_admin_password=dict(type="str", required=True, no_log=True),
            action=dict(type="str", required=True, choices=["activate", "test"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="bds_metastore_configuration",
        service_client_class=BdsClient,
        namespace="bds",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
