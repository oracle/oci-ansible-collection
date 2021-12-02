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
module: oci_ai_anomaly_detection_data_asset
short_description: Manage a DataAsset resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DataAsset resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new DataAsset.
    - "This resource has the following action operations in the M(oracle.oci.oci_ai_anomaly_detection_data_asset_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    compartment_id:
        description:
            - The OCID for the data asset's compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    project_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the data asset.
            - Required for create using I(state=present).
        type: str
    description:
        description:
            - A short description of the Ai data asset
            - This parameter is updatable.
        type: str
    data_source_details:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            data_source_type:
                description:
                    - Data source type where actually data asset is being stored
                type: str
                choices:
                    - "ORACLE_OBJECT_STORAGE"
                    - "INFLUX"
                    - "ORACLE_ATP"
                required: true
            namespace:
                description:
                    - Object storage namespace
                    - Applicable when data_source_type is 'ORACLE_OBJECT_STORAGE'
                type: str
            bucket_name:
                description:
                    - Object storage bucket name
                    - Applicable when data_source_type is 'ORACLE_OBJECT_STORAGE'
                type: str
            object_name:
                description:
                    - File name
                    - Applicable when data_source_type is 'ORACLE_OBJECT_STORAGE'
                type: str
            version_specific_details:
                description:
                    - ""
                    - Required when data_source_type is 'INFLUX'
                type: dict
                suboptions:
                    influx_version:
                        description:
                            - Data source type where actually data asset is being stored
                        type: str
                        choices:
                            - "V_1_8"
                            - "V_2_0"
                        required: true
                    database_name:
                        description:
                            - DB Name for influx connection
                            - Required when influx_version is 'V_1_8'
                        type: str
                    retention_policy_name:
                        description:
                            - retention policy is how long the bucket would last
                            - Applicable when influx_version is 'V_1_8'
                        type: str
                    bucket_name:
                        description:
                            - Bucket Name for influx connection
                            - Required when influx_version is 'V_2_0'
                        type: str
                    organization_name:
                        description:
                            - Org name for the influx db
                            - Required when influx_version is 'V_2_0'
                        type: str
            user_name:
                description:
                    - Username for connection to Influx
                    - Required when data_source_type is 'INFLUX'
                type: str
            password_secret_id:
                description:
                    - Password Secret Id for the influx connection
                    - Required when data_source_type is 'INFLUX'
                type: str
            measurement_name:
                description:
                    - Measurement name for influx
                    - Required when data_source_type is 'INFLUX'
                type: str
            url:
                description:
                    - public IP address and port to influx DB
                    - Required when data_source_type is 'INFLUX'
                type: str
            wallet_password_secret_id:
                description:
                    - wallet password Secret ID in String format
                    - Applicable when data_source_type is 'ORACLE_ATP'
                type: str
            atp_user_name:
                description:
                    - atp db user name
                    - Applicable when data_source_type is 'ORACLE_ATP'
                type: str
            atp_password_secret_id:
                description:
                    - atp db password Secret Id
                    - Applicable when data_source_type is 'ORACLE_ATP'
                type: str
            cwallet_file_secret_id:
                description:
                    - OCID of the secret containing the containers certificates of ATP wallet
                    - Applicable when data_source_type is 'ORACLE_ATP'
                type: str
            ewallet_file_secret_id:
                description:
                    - OCID of the secret containing the PDB'S certificates of ATP wallet
                    - Applicable when data_source_type is 'ORACLE_ATP'
                type: str
            key_store_file_secret_id:
                description:
                    - OCID of the secret containing Keystore.jks file of the ATP wallet
                    - Applicable when data_source_type is 'ORACLE_ATP'
                type: str
            ojdbc_file_secret_id:
                description:
                    - OCID of the secret that contains jdbc properties file of ATP wallet
                    - Applicable when data_source_type is 'ORACLE_ATP'
                type: str
            tnsnames_file_secret_id:
                description:
                    - OCID of the secret that contains the tnsnames file of ATP wallet
                    - Applicable when data_source_type is 'ORACLE_ATP'
                type: str
            truststore_file_secret_id:
                description:
                    - OCID of the secret containing truststore.jks file of the ATP wallet
                    - Applicable when data_source_type is 'ORACLE_ATP'
                type: str
            database_name:
                description:
                    - atp database name
                    - Applicable when data_source_type is 'ORACLE_ATP'
                type: str
            table_name:
                description:
                    - atp database table name
                    - Applicable when data_source_type is 'ORACLE_ATP'
                type: str
    private_endpoint_id:
        description:
            - OCID of Private Endpoint.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    data_asset_id:
        description:
            - The OCID of the Data Asset.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DataAsset.
            - Use I(state=present) to create or update a DataAsset.
            - Use I(state=absent) to delete a DataAsset.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create data_asset
  oci_ai_anomaly_detection_data_asset:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    data_source_details:
      # required
      data_source_type: ORACLE_OBJECT_STORAGE

      # optional
      namespace: namespace_example
      bucket_name: bucket_name_example
      object_name: object_name_example

    # optional
    display_name: display_name_example
    description: description_example
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update data_asset
  oci_ai_anomaly_detection_data_asset:
    # required
    data_asset_id: "ocid1.dataasset.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update data_asset using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_ai_anomaly_detection_data_asset:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete data_asset
  oci_ai_anomaly_detection_data_asset:
    # required
    data_asset_id: "ocid1.dataasset.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete data_asset using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_ai_anomaly_detection_data_asset:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.ai_anomaly_detection import AnomalyDetectionClient
    from oci.ai_anomaly_detection.models import CreateDataAssetDetails
    from oci.ai_anomaly_detection.models import UpdateDataAssetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataAssetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["project_id", "display_name"]

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
            self.client.list_data_assets, **kwargs
        )

    def get_create_model_class(self):
        return CreateDataAssetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_data_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(create_data_asset_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateDataAssetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_data_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                data_asset_id=self.module.params.get("data_asset_id"),
                update_data_asset_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_data_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(data_asset_id=self.module.params.get("data_asset_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DataAssetHelperCustom = get_custom_class("DataAssetHelperCustom")


class ResourceHelper(DataAssetHelperCustom, DataAssetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            compartment_id=dict(type="str"),
            project_id=dict(type="str"),
            description=dict(type="str"),
            data_source_details=dict(
                type="dict",
                options=dict(
                    data_source_type=dict(
                        type="str",
                        required=True,
                        choices=["ORACLE_OBJECT_STORAGE", "INFLUX", "ORACLE_ATP"],
                    ),
                    namespace=dict(type="str"),
                    bucket_name=dict(type="str"),
                    object_name=dict(type="str"),
                    version_specific_details=dict(
                        type="dict",
                        options=dict(
                            influx_version=dict(
                                type="str", required=True, choices=["V_1_8", "V_2_0"]
                            ),
                            database_name=dict(type="str"),
                            retention_policy_name=dict(type="str"),
                            bucket_name=dict(type="str"),
                            organization_name=dict(type="str"),
                        ),
                    ),
                    user_name=dict(type="str"),
                    password_secret_id=dict(type="str"),
                    measurement_name=dict(type="str"),
                    url=dict(type="str"),
                    wallet_password_secret_id=dict(type="str"),
                    atp_user_name=dict(type="str"),
                    atp_password_secret_id=dict(type="str"),
                    cwallet_file_secret_id=dict(type="str"),
                    ewallet_file_secret_id=dict(type="str"),
                    key_store_file_secret_id=dict(type="str"),
                    ojdbc_file_secret_id=dict(type="str"),
                    tnsnames_file_secret_id=dict(type="str"),
                    truststore_file_secret_id=dict(type="str"),
                    database_name=dict(type="str"),
                    table_name=dict(type="str"),
                ),
            ),
            private_endpoint_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            data_asset_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
