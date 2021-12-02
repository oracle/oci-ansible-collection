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
module: oci_ai_anomaly_detection_data_asset_actions
short_description: Perform actions on a DataAsset resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DataAsset resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), changing the compartment of a data asset.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    data_asset_id:
        description:
            - The OCID of the Data Asset.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the DataAsset.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on data_asset
  oci_ai_anomaly_detection_data_asset_actions:
    # required
    data_asset_id: "ocid1.dataasset.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
data_asset:
    description:
        - Details of the DataAsset resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The Unique Oracle ID (OCID) that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the DataAsset.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A short description of the data asset.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The time the the DataAsset was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the the DataAsset was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The lifecycle state of the Data Asset.
            returned: on success
            type: str
            sample: ACTIVE
        project_id:
            description:
                - The Unique project id which is created at project creation that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        data_source_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                data_source_type:
                    description:
                        - Data source type where actually data asset is being stored
                    returned: on success
                    type: str
                    sample: ORACLE_OBJECT_STORAGE
                version_specific_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        influx_version:
                            description:
                                - Data source type where actually data asset is being stored
                            returned: on success
                            type: str
                            sample: V_1_8
                        database_name:
                            description:
                                - DB Name for influx connection
                            returned: on success
                            type: str
                            sample: database_name_example
                        retention_policy_name:
                            description:
                                - retention policy is how long the bucket would last
                            returned: on success
                            type: str
                            sample: retention_policy_name_example
                        bucket_name:
                            description:
                                - Bucket Name for influx connection
                            returned: on success
                            type: str
                            sample: bucket_name_example
                        organization_name:
                            description:
                                - Org name for the influx db
                            returned: on success
                            type: str
                            sample: organization_name_example
                user_name:
                    description:
                        - Username for connection to Influx
                    returned: on success
                    type: str
                    sample: user_name_example
                password_secret_id:
                    description:
                        - Password Secret Id for the influx connection
                    returned: on success
                    type: str
                    sample: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
                measurement_name:
                    description:
                        - Measurement name for influx
                    returned: on success
                    type: str
                    sample: measurement_name_example
                url:
                    description:
                        - public IP address and port to influx DB
                    returned: on success
                    type: str
                    sample: url_example
                wallet_password_secret_id:
                    description:
                        - wallet password Secret ID in String format
                    returned: on success
                    type: str
                    sample: "ocid1.walletpasswordsecret.oc1..xxxxxxEXAMPLExxxxxx"
                atp_user_name:
                    description:
                        - atp db user name
                    returned: on success
                    type: str
                    sample: atp_user_name_example
                atp_password_secret_id:
                    description:
                        - atp db password Secret Id
                    returned: on success
                    type: str
                    sample: "ocid1.atppasswordsecret.oc1..xxxxxxEXAMPLExxxxxx"
                cwallet_file_secret_id:
                    description:
                        - OCID of the secret containing the containers certificates of ATP wallet
                    returned: on success
                    type: str
                    sample: "ocid1.cwalletfilesecret.oc1..xxxxxxEXAMPLExxxxxx"
                ewallet_file_secret_id:
                    description:
                        - OCID of the secret containing the PDB'S certificates of ATP wallet
                    returned: on success
                    type: str
                    sample: "ocid1.ewalletfilesecret.oc1..xxxxxxEXAMPLExxxxxx"
                key_store_file_secret_id:
                    description:
                        - OCID of the secret containing Keystore.jks file of the ATP wallet
                    returned: on success
                    type: str
                    sample: "ocid1.keystorefilesecret.oc1..xxxxxxEXAMPLExxxxxx"
                ojdbc_file_secret_id:
                    description:
                        - OCID of the secret that contains jdbc properties file of ATP wallet
                    returned: on success
                    type: str
                    sample: "ocid1.ojdbcfilesecret.oc1..xxxxxxEXAMPLExxxxxx"
                tnsnames_file_secret_id:
                    description:
                        - OCID of the secret that contains the tnsnames file of ATP wallet
                    returned: on success
                    type: str
                    sample: "ocid1.tnsnamesfilesecret.oc1..xxxxxxEXAMPLExxxxxx"
                truststore_file_secret_id:
                    description:
                        - OCID of the secret containing truststore.jks file of the ATP wallet
                    returned: on success
                    type: str
                    sample: "ocid1.truststorefilesecret.oc1..xxxxxxEXAMPLExxxxxx"
                database_name:
                    description:
                        - atp database name
                    returned: on success
                    type: str
                    sample: database_name_example
                table_name:
                    description:
                        - atp database table name
                    returned: on success
                    type: str
                    sample: table_name_example
                namespace:
                    description:
                        - Object storage namespace
                    returned: on success
                    type: str
                    sample: namespace_example
                bucket_name:
                    description:
                        - Object storage bucket name
                    returned: on success
                    type: str
                    sample: bucket_name_example
                object_name:
                    description:
                        - File name
                    returned: on success
                    type: str
                    sample: object_name_example
        private_endpoint_id:
            description:
                - OCID of Private Endpoint.
            returned: on success
            type: str
            sample: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "data_source_details": {
            "data_source_type": "ORACLE_OBJECT_STORAGE",
            "version_specific_details": {
                "influx_version": "V_1_8",
                "database_name": "database_name_example",
                "retention_policy_name": "retention_policy_name_example",
                "bucket_name": "bucket_name_example",
                "organization_name": "organization_name_example"
            },
            "user_name": "user_name_example",
            "password_secret_id": "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "measurement_name": "measurement_name_example",
            "url": "url_example",
            "wallet_password_secret_id": "ocid1.walletpasswordsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "atp_user_name": "atp_user_name_example",
            "atp_password_secret_id": "ocid1.atppasswordsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "cwallet_file_secret_id": "ocid1.cwalletfilesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "ewallet_file_secret_id": "ocid1.ewalletfilesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "key_store_file_secret_id": "ocid1.keystorefilesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "ojdbc_file_secret_id": "ocid1.ojdbcfilesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "tnsnames_file_secret_id": "ocid1.tnsnamesfilesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "truststore_file_secret_id": "ocid1.truststorefilesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "database_name": "database_name_example",
            "table_name": "table_name_example",
            "namespace": "namespace_example",
            "bucket_name": "bucket_name_example",
            "object_name": "object_name_example"
        },
        "private_endpoint_id": "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.ai_anomaly_detection import AnomalyDetectionClient
    from oci.ai_anomaly_detection.models import ChangeDataAssetCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataAssetActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "data_asset_id"

    def get_module_resource_id(self):
        return self.module.params.get("data_asset_id")

    def get_get_fn(self):
        return self.client.get_data_asset

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_asset,
            data_asset_id=self.module.params.get("data_asset_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDataAssetCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_data_asset_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                data_asset_id=self.module.params.get("data_asset_id"),
                change_data_asset_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


DataAssetActionsHelperCustom = get_custom_class("DataAssetActionsHelperCustom")


class ResourceHelper(DataAssetActionsHelperCustom, DataAssetActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            data_asset_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="data_asset",
        service_client_class=AnomalyDetectionClient,
        namespace="ai_anomaly_detection",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
