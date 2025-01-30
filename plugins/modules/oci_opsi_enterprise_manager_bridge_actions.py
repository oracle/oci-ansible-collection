#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_opsi_enterprise_manager_bridge_actions
short_description: Perform actions on an EnterpriseManagerBridge resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an EnterpriseManagerBridge resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a EnterpriseManagerBridge resource from one compartment to another. When provided, If-Match is checked against
      ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    enterprise_manager_bridge_id:
        description:
            - Unique Enterprise Manager bridge identifier
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The OCID of the compartment into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the EnterpriseManagerBridge.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on enterprise_manager_bridge
  oci_opsi_enterprise_manager_bridge_actions:
    # required
    enterprise_manager_bridge_id: "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
enterprise_manager_bridge:
    description:
        - Details of the EnterpriseManagerBridge resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Enterprise Manager bridge identifier
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment identifier of the Enterprise Manager bridge
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User-friedly name of Enterprise Manager Bridge that does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of Enterprise Manager Bridge
            returned: on success
            type: str
            sample: description_example
        object_storage_namespace_name:
            description:
                - Object Storage Namespace Name
            returned: on success
            type: str
            sample: object_storage_namespace_name_example
        object_storage_bucket_name:
            description:
                - Object Storage Bucket Name
            returned: on success
            type: str
            sample: object_storage_bucket_name_example
        object_storage_bucket_status_details:
            description:
                - A message describing status of the object storage bucket of this resource. For example, it can be used to provide actionable information about
                  the permission and content validity of the bucket.
            returned: on success
            type: str
            sample: object_storage_bucket_status_details_example
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
                - The time the the Enterprise Manager bridge was first created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the Enterprise Manager bridge was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Enterprise Manager bridge.
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
        "description": "description_example",
        "object_storage_namespace_name": "object_storage_namespace_name_example",
        "object_storage_bucket_name": "object_storage_bucket_name_example",
        "object_storage_bucket_status_details": "object_storage_bucket_status_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example"
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
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import ChangeEnterpriseManagerBridgeCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EnterpriseManagerBridgeActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "enterprise_manager_bridge_id"

    def get_module_resource_id(self):
        return self.module.params.get("enterprise_manager_bridge_id")

    def get_get_fn(self):
        return self.client.get_enterprise_manager_bridge

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_enterprise_manager_bridge,
            enterprise_manager_bridge_id=self.module.params.get(
                "enterprise_manager_bridge_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeEnterpriseManagerBridgeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_enterprise_manager_bridge_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                enterprise_manager_bridge_id=self.module.params.get(
                    "enterprise_manager_bridge_id"
                ),
                change_enterprise_manager_bridge_compartment_details=action_details,
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


EnterpriseManagerBridgeActionsHelperCustom = get_custom_class(
    "EnterpriseManagerBridgeActionsHelperCustom"
)


class ResourceHelper(
    EnterpriseManagerBridgeActionsHelperCustom, EnterpriseManagerBridgeActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            enterprise_manager_bridge_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="enterprise_manager_bridge",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
