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
module: oci_bds_metastore_configuration_facts
short_description: Fetches details about one or multiple BdsMetastoreConfiguration resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BdsMetastoreConfiguration resources in Oracle Cloud Infrastructure
    - Returns a list of metastore configurations ssociated with this Big Data Service cluster.
    - If I(metastore_config_id) is specified, the details of a single BdsMetastoreConfiguration will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    metastore_config_id:
        description:
            - The metastore configuration ID
            - Required to get a specific bds_metastore_configuration.
        type: str
        aliases: ["id"]
    bds_instance_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
    metastore_type:
        description:
            - The type of the metastore in the metastore configuration
        type: str
        choices:
            - "LOCAL"
            - "EXTERNAL"
    metastore_id:
        description:
            - The OCID of the Data Catalog metastore in the metastore configuration
        type: str
    lifecycle_state:
        description:
            - The lifecycle state of the metastore in the metastore configuration
        type: str
        choices:
            - "CREATING"
            - "ACTIVATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "FAILED"
            - "DELETING"
            - "DELETED"
    bds_api_key_id:
        description:
            - The ID of the API key that is associated with the external metastore in the metastore configuration
        type: str
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific bds_metastore_configuration
  oci_bds_metastore_configuration_facts:
    # required
    metastore_config_id: "ocid1.metastoreconfig.oc1..xxxxxxEXAMPLExxxxxx"
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List bds_metastore_configurations
  oci_bds_metastore_configuration_facts:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    metastore_type: LOCAL
    metastore_id: "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    bds_api_key_id: "ocid1.bdsapikey.oc1..xxxxxxEXAMPLExxxxxx"
    sort_by: timeCreated
    sort_order: ASC
    display_name: display_name_example

"""

RETURN = """
bds_metastore_configurations:
    description:
        - List of BdsMetastoreConfiguration resources
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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "metastore_type": "LOCAL",
        "metastore_id": "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx",
        "bds_api_key_id": "ocid1.bdsapikey.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.bds import BdsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsMetastoreConfigurationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "bds_instance_id",
            "metastore_config_id",
        ]

    def get_required_params_for_list(self):
        return [
            "bds_instance_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bds_metastore_configuration,
            bds_instance_id=self.module.params.get("bds_instance_id"),
            metastore_config_id=self.module.params.get("metastore_config_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "metastore_type",
            "metastore_id",
            "lifecycle_state",
            "bds_api_key_id",
            "sort_by",
            "sort_order",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_bds_metastore_configurations,
            bds_instance_id=self.module.params.get("bds_instance_id"),
            **optional_kwargs
        )


BdsMetastoreConfigurationFactsHelperCustom = get_custom_class(
    "BdsMetastoreConfigurationFactsHelperCustom"
)


class ResourceFactsHelper(
    BdsMetastoreConfigurationFactsHelperCustom, BdsMetastoreConfigurationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            metastore_config_id=dict(aliases=["id"], type="str"),
            bds_instance_id=dict(type="str", required=True),
            metastore_type=dict(type="str", choices=["LOCAL", "EXTERNAL"]),
            metastore_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "FAILED",
                    "DELETING",
                    "DELETED",
                ],
            ),
            bds_api_key_id=dict(type="str"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="bds_metastore_configuration",
        service_client_class=BdsClient,
        namespace="bds",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(bds_metastore_configurations=result)


if __name__ == "__main__":
    main()
