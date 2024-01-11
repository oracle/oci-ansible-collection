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
module: oci_cloud_bridge_asset_source_actions
short_description: Perform actions on an AssetSource resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AssetSource resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource.
    - For I(action=refresh), initiates the process of asset metadata synchronization with the related asset source.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the resource should be moved.
            - Required for I(action=change_compartment).
        type: str
    asset_source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the asset source.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the AssetSource.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "refresh"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on asset_source
  oci_cloud_bridge_asset_source_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    asset_source_id: "ocid1.assetsource.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action refresh on asset_source
  oci_cloud_bridge_asset_source_actions:
    # required
    asset_source_id: "ocid1.assetsource.oc1..xxxxxxEXAMPLExxxxxx"
    action: refresh

"""

RETURN = """
asset_source:
    description:
        - Details of the AssetSource resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
        display_name:
            description:
                - A user-friendly name for the asset source. Does not have to be unique, and it's mutable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        environment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the environment.
            returned: on success
            type: str
            sample: "ocid1.environment.oc1..xxxxxxEXAMPLExxxxxx"
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
        discovery_schedule_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of an attached discovery schedule.
            returned: on success
            type: str
            sample: "ocid1.discoveryschedule.oc1..xxxxxxEXAMPLExxxxxx"
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
        vcenter_endpoint:
            description:
                - Endpoint for VMware asset discovery and replication in the form of ```https://<host>:<port>/sdk```
            returned: on success
            type: str
            sample: vcenter_endpoint_example
        discovery_credentials:
            description:
                - ""
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
            returned: on success
            type: bool
            sample: true
        are_realtime_metrics_collected:
            description:
                - Flag indicating whether real-time metrics are collected for assets, originating from this asset source.
            returned: on success
            type: bool
            sample: true
    sample: {
        "type": "VMWARE",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "environment_id": "ocid1.environment.oc1..xxxxxxEXAMPLExxxxxx",
        "inventory_id": "ocid1.inventory.oc1..xxxxxxEXAMPLExxxxxx",
        "assets_compartment_id": "ocid1.assetscompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "discovery_schedule_id": "ocid1.discoveryschedule.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
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
        "are_realtime_metrics_collected": true
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
    from oci.cloud_bridge import DiscoveryClient
    from oci.cloud_bridge.models import ChangeAssetSourceCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AssetSourceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        refresh
    """

    @staticmethod
    def get_module_resource_id_param():
        return "asset_source_id"

    def get_module_resource_id(self):
        return self.module.params.get("asset_source_id")

    def get_get_fn(self):
        return self.client.get_asset_source

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_asset_source,
            asset_source_id=self.module.params.get("asset_source_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeAssetSourceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_asset_source_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                asset_source_id=self.module.params.get("asset_source_id"),
                change_asset_source_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
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

    def refresh(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.refresh_asset_source,
            call_fn_args=(),
            call_fn_kwargs=dict(
                asset_source_id=self.module.params.get("asset_source_id"),
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


AssetSourceActionsHelperCustom = get_custom_class("AssetSourceActionsHelperCustom")


class ResourceHelper(AssetSourceActionsHelperCustom, AssetSourceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            asset_source_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str", required=True, choices=["change_compartment", "refresh"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="asset_source",
        service_client_class=DiscoveryClient,
        namespace="cloud_bridge",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
