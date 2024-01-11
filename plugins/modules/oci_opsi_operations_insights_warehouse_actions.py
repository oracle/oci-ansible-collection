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
module: oci_opsi_operations_insights_warehouse_actions
short_description: Perform actions on an OperationsInsightsWarehouse resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OperationsInsightsWarehouse resource in Oracle Cloud Infrastructure
    - For I(action=download_operations_insights_warehouse_wallet), download the ADW wallet for Operations Insights Warehouse using which the Hub data is
      exposed.
    - For I(action=rotate_operations_insights_warehouse_wallet), rotate the ADW wallet for Operations Insights Warehouse using which the Hub data is exposed.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dest:
        description:
            - The destination file path to write the output. The file will be created if it does not exist. If the file already exists, the content will be
              overwritten.
            - Required for I(action=download_operations_insights_warehouse_wallet).
        type: str
    operations_insights_warehouse_wallet_password:
        description:
            - User provided ADW wallet password for the Operations Insights Warehouse.
            - Required for I(action=download_operations_insights_warehouse_wallet).
        type: str
    operations_insights_warehouse_id:
        description:
            - Unique Operations Insights Warehouse identifier
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the OperationsInsightsWarehouse.
        type: str
        required: true
        choices:
            - "download_operations_insights_warehouse_wallet"
            - "rotate_operations_insights_warehouse_wallet"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action download_operations_insights_warehouse_wallet on operations_insights_warehouse
  oci_opsi_operations_insights_warehouse_actions:
    # required
    dest: /tmp/myfile
    operations_insights_warehouse_wallet_password: example-password
    operations_insights_warehouse_id: "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx"
    action: download_operations_insights_warehouse_wallet

- name: Perform action rotate_operations_insights_warehouse_wallet on operations_insights_warehouse
  oci_opsi_operations_insights_warehouse_actions:
    # required
    operations_insights_warehouse_id: "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx"
    action: rotate_operations_insights_warehouse_wallet

"""

RETURN = """
operations_insights_warehouse:
    description:
        - Details of the OperationsInsightsWarehouse resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OPSI Warehouse OCID
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User-friedly name of Operations Insights Warehouse that does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        cpu_allocated:
            description:
                - Number of OCPUs allocated to OPSI Warehouse ADW.
            returned: on success
            type: float
            sample: 1.2
        cpu_used:
            description:
                - Number of OCPUs used by OPSI Warehouse ADW. Can be fractional.
            returned: on success
            type: float
            sample: 1.2
        storage_allocated_in_gbs:
            description:
                - Storage allocated to OPSI Warehouse ADW.
            returned: on success
            type: float
            sample: 1.2
        storage_used_in_gbs:
            description:
                - Storage by OPSI Warehouse ADW in GB.
            returned: on success
            type: float
            sample: 1.2
        dynamic_group_id:
            description:
                - OCID of the dynamic group created for the warehouse
            returned: on success
            type: str
            sample: "ocid1.dynamicgroup.oc1..xxxxxxEXAMPLExxxxxx"
        operations_insights_tenancy_id:
            description:
                - Tenancy Identifier of Operations Insights service
            returned: on success
            type: str
            sample: "ocid1.operationsinsightstenancy.oc1..xxxxxxEXAMPLExxxxxx"
        time_last_wallet_rotated:
            description:
                - The time at which the ADW wallet was last rotated for the Operations Insights Warehouse. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - The time at which the resource was first created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time at which the resource was last updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - Possible lifecycle states
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "cpu_allocated": 1.2,
        "cpu_used": 1.2,
        "storage_allocated_in_gbs": 1.2,
        "storage_used_in_gbs": 1.2,
        "dynamic_group_id": "ocid1.dynamicgroup.oc1..xxxxxxEXAMPLExxxxxx",
        "operations_insights_tenancy_id": "ocid1.operationsinsightstenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "time_last_wallet_rotated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example"
    }
"""

from ansible.module_utils._text import to_bytes
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
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import DownloadOperationsInsightsWarehouseWalletDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OperationsInsightsWarehouseActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        download_operations_insights_warehouse_wallet
        rotate_operations_insights_warehouse_wallet
    """

    @staticmethod
    def get_module_resource_id_param():
        return "operations_insights_warehouse_id"

    def get_module_resource_id(self):
        return self.module.params.get("operations_insights_warehouse_id")

    def get_get_fn(self):
        return self.client.get_operations_insights_warehouse

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_operations_insights_warehouse,
            operations_insights_warehouse_id=self.module.params.get(
                "operations_insights_warehouse_id"
            ),
        )

    def download_operations_insights_warehouse_wallet(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DownloadOperationsInsightsWarehouseWalletDetails
        )
        response = oci_wait_utils.call_and_wait(
            call_fn=self.client.download_operations_insights_warehouse_wallet,
            call_fn_args=(),
            call_fn_kwargs=dict(
                operations_insights_warehouse_id=self.module.params.get(
                    "operations_insights_warehouse_id"
                ),
                download_operations_insights_warehouse_wallet_details=action_details,
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
        dest = self.module.params.get("dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None

    def rotate_operations_insights_warehouse_wallet(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.rotate_operations_insights_warehouse_wallet,
            call_fn_args=(),
            call_fn_kwargs=dict(
                operations_insights_warehouse_id=self.module.params.get(
                    "operations_insights_warehouse_id"
                ),
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


OperationsInsightsWarehouseActionsHelperCustom = get_custom_class(
    "OperationsInsightsWarehouseActionsHelperCustom"
)


class ResourceHelper(
    OperationsInsightsWarehouseActionsHelperCustom,
    OperationsInsightsWarehouseActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            dest=dict(type="str"),
            operations_insights_warehouse_wallet_password=dict(type="str", no_log=True),
            operations_insights_warehouse_id=dict(
                aliases=["id"], type="str", required=True
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "download_operations_insights_warehouse_wallet",
                    "rotate_operations_insights_warehouse_wallet",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="operations_insights_warehouse",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
