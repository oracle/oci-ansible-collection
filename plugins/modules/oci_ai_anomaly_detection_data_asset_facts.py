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
module: oci_ai_anomaly_detection_data_asset_facts
short_description: Fetches details about one or multiple DataAsset resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DataAsset resources in Oracle Cloud Infrastructure
    - Returns a list of DataAssets.
    - If I(data_asset_id) is specified, the details of a single DataAsset will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    data_asset_id:
        description:
            - The OCID of the Data Asset.
            - Required to get a specific data_asset.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple data_assets.
        type: str
    project_id:
        description:
            - The ID of the project for which to list the objects.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - <b>Filter</b> results by the specified lifecycle state. Must be a valid
              state for the resource type.
        type: str
        choices:
            - "ACTIVE"
            - "DELETED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific data_asset
  oci_ai_anomaly_detection_data_asset_facts:
    # required
    data_asset_id: "ocid1.dataasset.oc1..xxxxxxEXAMPLExxxxxx"

- name: List data_assets
  oci_ai_anomaly_detection_data_asset_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: ACTIVE
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
data_assets:
    description:
        - List of DataAsset resources
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
                - Returned for get operation
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
        data_source_type:
            description:
                - Data source type where actually data asset is being stored
                - Returned for list operation
            returned: on success
            type: str
            sample: ORACLE_OBJECT_STORAGE
    sample: [{
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
        "system_tags": {},
        "data_source_type": "ORACLE_OBJECT_STORAGE"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.ai_anomaly_detection import AnomalyDetectionClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataAssetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "data_asset_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_asset,
            data_asset_id=self.module.params.get("data_asset_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "project_id",
            "display_name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_data_assets,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataAssetFactsHelperCustom = get_custom_class("DataAssetFactsHelperCustom")


class ResourceFactsHelper(DataAssetFactsHelperCustom, DataAssetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            data_asset_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            project_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="data_asset",
        service_client_class=AnomalyDetectionClient,
        namespace="ai_anomaly_detection",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(data_assets=result)


if __name__ == "__main__":
    main()
