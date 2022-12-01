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
module: oci_cloud_bridge_asset_source_facts
short_description: Fetches details about one or multiple AssetSource resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AssetSource resources in Oracle Cloud Infrastructure
    - Returns a list of asset sources.
    - If I(asset_source_id) is specified, the details of a single AssetSource will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple asset_sources.
        type: str
    asset_source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the asset source.
            - Required to get a specific asset_source.
        type: str
        aliases: ["id"]
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. By default, the timeCreated is in descending order and displayName is in ascending
              order.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    lifecycle_state:
        description:
            - The current state of the asset source.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "UPDATING"
            - "NEEDS_ATTENTION"
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
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
- name: Get a specific asset_source
  oci_cloud_bridge_asset_source_facts:
    # required
    asset_source_id: "ocid1.assetsource.oc1..xxxxxxEXAMPLExxxxxx"

- name: List asset_sources
  oci_cloud_bridge_asset_source_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    asset_source_id: "ocid1.assetsource.oc1..xxxxxxEXAMPLExxxxxx"
    sort_by: timeCreated
    lifecycle_state: CREATING
    sort_order: ASC
    display_name: display_name_example

"""

RETURN = """
asset_sources:
    description:
        - List of AssetSource resources
    returned: on success
    type: complex
    contains:
        discovery_schedule_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of an attached discovery schedule.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.discoveryschedule.oc1..xxxxxxEXAMPLExxxxxx"
        vcenter_endpoint:
            description:
                - Endpoint for VMware asset discovery and replication in the form of ```https://<host>:<port>/sdk```
                - Returned for get operation
            returned: on success
            type: str
            sample: vcenter_endpoint_example
        discovery_credentials:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Authentication type
                    returned: on success
                    type: str
                    sample: BASIC
                secret_id:
                    description:
                        - "The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret in a vault.
                          If the the type of the credentials is BASIC`, the secret must contain the username and
                          password in JSON format, which is in the form of `{ \\"username\\": \\"<VMwareUser>\\", \\"password\\": \\"<VMwarePassword>\\" }`."
                    returned: on success
                    type: str
                    sample: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        replication_credentials:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Authentication type
                    returned: on success
                    type: str
                    sample: BASIC
                secret_id:
                    description:
                        - "The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret in a vault.
                          If the the type of the credentials is BASIC`, the secret must contain the username and
                          password in JSON format, which is in the form of `{ \\"username\\": \\"<VMwareUser>\\", \\"password\\": \\"<VMwarePassword>\\" }`."
                    returned: on success
                    type: str
                    sample: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        are_historical_metrics_collected:
            description:
                - Flag indicating whether historical metrics are collected for assets, originating from this asset source.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        are_realtime_metrics_collected:
            description:
                - Flag indicating whether real-time metrics are collected for assets, originating from this asset source.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        type:
            description:
                - The type of asset source. Indicates external origin of the assets that are read by assigning this asset source.
            returned: on success
            type: str
            sample: VMWARE
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment for the resource.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        environment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the environment.
            returned: on success
            type: str
            sample: "ocid1.environment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name for the asset source. Does not have to be unique, and it's mutable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        lifecycle_state:
            description:
                - The current state of the asset source.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - The detailed state of the asset source.
            returned: on success
            type: str
            sample: lifecycle_details_example
        inventory_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the inventory that will contain created assets.
            returned: on success
            type: str
            sample: "ocid1.inventory.oc1..xxxxxxEXAMPLExxxxxx"
        assets_compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that is going to be used to create
                  assets.
            returned: on success
            type: str
            sample: "ocid1.assetscompartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time when the asset source was created in the RFC3339 format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The point in time that the asset source was last updated in the RFC3339 format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace/scope. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is
                  predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "discovery_schedule_id": "ocid1.discoveryschedule.oc1..xxxxxxEXAMPLExxxxxx",
        "vcenter_endpoint": "vcenter_endpoint_example",
        "discovery_credentials": {
            "type": "BASIC",
            "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "replication_credentials": {
            "type": "BASIC",
            "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "are_historical_metrics_collected": true,
        "are_realtime_metrics_collected": true,
        "type": "VMWARE",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "environment_id": "ocid1.environment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "inventory_id": "ocid1.inventory.oc1..xxxxxxEXAMPLExxxxxx",
        "assets_compartment_id": "ocid1.assetscompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.cloud_bridge import DiscoveryClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AssetSourceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "asset_source_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_asset_source,
            asset_source_id=self.module.params.get("asset_source_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "asset_source_id",
            "sort_by",
            "lifecycle_state",
            "sort_order",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_asset_sources,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AssetSourceFactsHelperCustom = get_custom_class("AssetSourceFactsHelperCustom")


class ResourceFactsHelper(AssetSourceFactsHelperCustom, AssetSourceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            asset_source_id=dict(aliases=["id"], type="str"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "UPDATING",
                    "NEEDS_ATTENTION",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="asset_source",
        service_client_class=DiscoveryClient,
        namespace="cloud_bridge",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(asset_sources=result)


if __name__ == "__main__":
    main()
