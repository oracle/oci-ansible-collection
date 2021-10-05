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
module: oci_identity_compartment_actions
short_description: Perform actions on a Compartment resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Compartment resource in Oracle Cloud Infrastructure
    - For I(action=bulk_delete_resources), deletes multiple resources in the compartment. All resources must be in the same compartment. You must have the
      appropriate
      permissions to delete the resources in the request. This API can only be invoked from the tenancy's
      L(home region,https://docs.cloud.oracle.com/Content/Identity/Tasks/managingregions.htm#Home). This operation creates a
      L(WorkRequest,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/workrequests/20160918/WorkRequest/). Use the
      L(GetWorkRequest,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/workrequests/20160918/WorkRequest/GetWorkRequest)
      API to monitor the status of the bulk action.
    - For I(action=bulk_move_resources), moves multiple resources from one compartment to another. All resources must be in the same compartment.
      This API can only be invoked from the tenancy's L(home region,https://docs.cloud.oracle.com/Content/Identity/Tasks/managingregions.htm#Home).
      To move resources, you must have the appropriate permissions to move the resource in both the source and target
      compartments. This operation creates a L(WorkRequest,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/workrequests/20160918/WorkRequest/).
      Use the L(GetWorkRequest,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/workrequests/20160918/WorkRequest/GetWorkRequest) API to monitor the status of
      the bulk action.
    - "For I(action=move), move the compartment to a different parent compartment in the same tenancy. When you move a
      compartment, all its contents (subcompartments and resources) are moved with it. Note that
      the `CompartmentId` that you specify in the path is the compartment that you want to move.
      **IMPORTANT**: After you move a compartment to a new parent compartment, the access policies of
      the new parent take effect and the policies of the previous parent no longer apply. Ensure that you
      are aware of the implications for the compartment contents before you move it. For more
      information, see L(Moving a Compartment,https://docs.cloud.oracle.com/Content/Identity/Tasks/managingcompartments.htm#MoveCompartment)."
    - For I(action=recover), recover the compartment from DELETED state to ACTIVE state.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
        type: str
        aliases: ["id"]
        required: true
    resources:
        description:
            - The resources to be deleted.
            - Required for I(action=bulk_delete_resources), I(action=bulk_move_resources).
        type: list
        elements: dict
        suboptions:
            identifier:
                description:
                    - The resource OCID.
                type: str
                required: true
            entity_type:
                description:
                    - The resource-type. To get the list of supported resource-types use
                      L(ListBulkActionResourceTypes API,https://docs.cloud.oracle.com/en-
                      us/iaas/api/#/en/identity/20160918/BulkActionResourceTypeCollection/ListBulkActionResourceTypes/).
                type: str
                required: true
            metadata:
                description:
                    - Additional information that helps to identity the resource for bulk action.
                    - The APIs to delete and move most resource types only require the resource identifier (ocid).
                      But some resource-types require additional identifying information.
                    - This information is provided in the resource's public API document. It is also
                      available through the
                      L(ListBulkActionResourceTypes API,https://docs.cloud.oracle.com/en-
                      us/iaas/api/#/en/identity/20160918/BulkActionResourceTypeCollection/ListBulkActionResourceTypes/).
                    - "**Example**:
                      The APIs to delete or move the `buckets` resource-type require `namespaceName` and `bucketName` to identify the resource, as
                      shown in the APIs, L(DeleteBucket,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/objectstorage/20160918/Bucket/DeleteBucket) and
                      L(UpdateBucket,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/objectstorage/20160918/Bucket/UpdateBucket)."
                    - To add a bucket for bulk actions, specify `namespaceName` and `bucketName` in
                      the metadata property as shown in this example
                    - |
                      "   {
                            \\"identifier\\": \\"<OCID_of_bucket>\\"
                            \\"entityType\\": \\"bucket\\",
                            \\"metadata\\":
                            {
                              \\"namespaceName\\": \\"sampleNamespace\\",
                              \\"bucketName\\": \\"sampleBucket\\"
                            }
                          }"
                type: dict
    target_compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the destination compartment
              into which to move the resources.
            - Required for I(action=bulk_move_resources), I(action=move).
        type: str
    action:
        description:
            - The action to perform on the Compartment.
        type: str
        required: true
        choices:
            - "bulk_delete_resources"
            - "bulk_move_resources"
            - "move"
            - "recover"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action bulk_delete_resources on compartment
  oci_identity_compartment_actions:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    resources:
    - identifier: identifier_example
      entity_type: entity_type_example
    action: bulk_delete_resources

- name: Perform action bulk_move_resources on compartment
  oci_identity_compartment_actions:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    resources:
    - identifier: identifier_example
      entity_type: entity_type_example
    target_compartment_id: "ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: bulk_move_resources

- name: Perform action move on compartment
  oci_identity_compartment_actions:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    target_compartment_id: "ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: move

- name: Perform action recover on compartment
  oci_identity_compartment_actions:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: recover

"""

RETURN = """
compartment:
    description:
        - Details of the Compartment resource acted upon by the current operation
    returned: on success for actions [ "move", "recover" ]
    type: complex
    contains:
        id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the parent compartment containing the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name you assign to the compartment during creation. The name must be unique across all
                  compartments in the parent. Avoid entering confidential information.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - The description you assign to the compartment. Does not have to be unique, and it's changeable.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - Date and time the compartment was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        lifecycle_state:
            description:
                - The compartment's current state. After creating a compartment, make sure its `lifecycleState` changes from
                  CREATING to ACTIVE before using it.
            returned: on success
            type: str
            sample: CREATING
        inactive_status:
            description:
                - The detailed status of INACTIVE lifecycleState.
            returned: on success
            type: int
            sample: 56
        is_accessible:
            description:
                - Indicates whether or not the compartment is accessible for the user making the request.
                  Returns true when the user has INSPECT permissions directly on a resource in the
                  compartment or indirectly (permissions can be on a resource in a subcompartment).
            returned: on success
            type: bool
            sample: true
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "time_created": "2016-08-25T21:10:29.600Z",
        "lifecycle_state": "CREATING",
        "inactive_status": 56,
        "is_accessible": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.identity import IdentityClient
    from oci.identity.models import BulkDeleteResourcesDetails
    from oci.identity.models import BulkMoveResourcesDetails
    from oci.identity.models import MoveCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CompartmentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        bulk_delete_resources
        bulk_move_resources
        move
        recover
    """

    @staticmethod
    def get_module_resource_id_param():
        return "compartment_id"

    def get_module_resource_id(self):
        return self.module.params.get("compartment_id")

    def get_get_fn(self):
        return self.client.get_compartment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_compartment,
            compartment_id=self.module.params.get("compartment_id"),
        )

    def bulk_delete_resources(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, BulkDeleteResourcesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.bulk_delete_resources,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compartment_id=self.module.params.get("compartment_id"),
                bulk_delete_resources_details=action_details,
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

    def bulk_move_resources(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, BulkMoveResourcesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.bulk_move_resources,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compartment_id=self.module.params.get("compartment_id"),
                bulk_move_resources_details=action_details,
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

    def move(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, MoveCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.move_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compartment_id=self.module.params.get("compartment_id"),
                move_compartment_details=action_details,
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

    def recover(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.recover_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compartment_id=self.module.params.get("compartment_id"),
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


CompartmentActionsHelperCustom = get_custom_class("CompartmentActionsHelperCustom")


class ResourceHelper(CompartmentActionsHelperCustom, CompartmentActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(aliases=["id"], type="str", required=True),
            resources=dict(
                type="list",
                elements="dict",
                options=dict(
                    identifier=dict(type="str", required=True),
                    entity_type=dict(type="str", required=True),
                    metadata=dict(type="dict"),
                ),
            ),
            target_compartment_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "bulk_delete_resources",
                    "bulk_move_resources",
                    "move",
                    "recover",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="compartment",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
