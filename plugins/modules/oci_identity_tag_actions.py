#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_identity_tag_actions
short_description: Perform actions on a Tag resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Tag resource in Oracle Cloud Infrastructure
    - "For I(action=bulk_delete), deletes the specified tag key definitions. This operation triggers a process that removes the
      tags from all resources in your tenancy. The tag key definitions must be within the same tag namespace.
      The following actions happen immediately:
        * If the tag is a cost-tracking tag, the tag no longer counts against your
        10 cost-tracking tags limit, even if you do not disable the tag before running this operation.
        * If the tag is used with dynamic groups, the rules that contain the tag are no longer
        evaluated against the tag.
      After you start this operation, the state of the tag changes to DELETING, and tag removal
      from resources begins. This process can take up to 48 hours depending on the number of resources that
      are tagged and the regions in which those resources reside.
      When all tags have been removed, the state changes to DELETED. You cannot restore a deleted tag. After the tag state
      changes to DELETED, you can use the same tag name again.
      After you start this operation, you cannot start either the L(DeleteTag,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/Tag/DeleteTag)
      or the L(CascadeDeleteTagNamespace,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/TagNamespace/CascadeDeleteTagNamespace) operation
      until this process completes.
      In order to delete tags, you must first retire the tags. Use L(UpdateTag,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/identity/20160918/Tag/UpdateTag)
      to retire a tag."
    - "For I(action=bulk_edit), edits the specified list of tag key definitions for the selected resources.
      This operation triggers a process that edits the tags on all selected resources. The possible actions are:
        * Add a defined tag when the tag does not already exist on the resource.
        * Update the value for a defined tag when the tag is present on the resource.
        * Add a defined tag when it does not already exist on the resource or update the value for a defined tag when the tag is present on the resource.
        * Remove a defined tag from a resource. The tag is removed from the resource regardless of the tag value.
      See L(BulkEditOperationDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/latest/datatypes/BulkEditOperationDetails) for more information.
      The edits can include a combination of operations and tag sets.
      However, multiple operations cannot apply to one key definition in the same request.
      For example, if one request adds `tag set-1` to a resource and sets a tag value to `tag set-2`,
      `tag set-1` and `tag set-2` cannot have any common tag definitions."
version_added: "2.9"
author: Oracle (@oracle)
options:
    tag_definition_ids:
        description:
            - The OCIDs of the tag definitions to delete
            - Required for I(action=bulk_delete).
        type: list
    compartment_id:
        description:
            - The OCID of the compartment where the bulk tag edit request is submitted.
            - Required for I(action=bulk_edit).
        type: str
    resources:
        description:
            - The resources to be updated.
            - Required for I(action=bulk_edit).
        type: list
        suboptions:
            id:
                description:
                    - The unique OCID of the resource.
                type: str
                required: true
            resource_type:
                description:
                    - The type of resource. See L(BulkEditResourceTypes,https://docs.cloud.oracle.com/en-
                      us/iaas/api/#/en/identity/latest/Tags/BulkEditResourceTypes).
                type: str
                required: true
            metadata:
                description:
                    - Additional information that identifies the resource for bulk editing of tags. This information is provided in the resource's API
                      documentation.
                type: dict
    bulk_edit_operations:
        description:
            - The operations associated with the request to bulk edit tags.
            - Required for I(action=bulk_edit).
        type: list
        suboptions:
            operation_type:
                description:
                    - An enum-like description of the type of operation.
                    - "* `ADD_WHERE_ABSENT` adds a defined tag only if the tag does not already exist on the resource.
                      * `SET_WHERE_PRESENT` updates the value for a defined tag only if the tag is present on the resource.
                      * `ADD_OR_SET` combines the first two operations to add a defined tag if it does not already exist on the resource
                      or update the value for a defined tag only if the tag is present on the resource.
                      * `REMOVE` removes the defined tag from the resource. The tag is removed from the resource regardless of the tag value."
                type: str
                choices:
                    - "ADD_WHERE_ABSENT"
                    - "SET_WHERE_PRESENT"
                    - "ADD_OR_SET"
                    - "REMOVE"
                required: true
            defined_tags:
                description:
                    - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                      For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                      Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                type: dict
                required: true
    action:
        description:
            - The action to perform on the Tag.
        type: str
        required: true
        choices:
            - "bulk_delete"
            - "bulk_edit"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action bulk_delete on tag
  oci_identity_tag_actions:
    tag_definition_ids:
    - ocid1.tagdefinition.oc1..unique_ID_1
    - ocid1.tagdefinition.oc1..unique_ID_2
    - ocid1.tagdefinition.oc1..unique_ID_3
    action: bulk_delete

- name: Perform action bulk_edit on tag
  oci_identity_tag_actions:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    resources:
    - id: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
      resource_type: resource_type_example
    bulk_edit_operations:
    - operation_type: ADD_WHERE_ABSENT
      defined_tags: {'Operations': {'CostCenter': 'US'}}
    action: bulk_edit

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
    from oci.identity.models import BulkDeleteTagsDetails
    from oci.identity.models import BulkEditTagsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TagActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        bulk_delete
        bulk_edit
    """

    def get_get_fn(self):
        return self.client.get_tag

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tag,
            tag_namespace_id=self.module.params.get("tag_namespace_id"),
            tag_name=self.module.params.get("tag_name"),
        )

    def bulk_delete(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, BulkDeleteTagsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.bulk_delete_tags,
            call_fn_args=(),
            call_fn_kwargs=dict(bulk_delete_tags_details=action_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def bulk_edit(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, BulkEditTagsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.bulk_edit_tags,
            call_fn_args=(),
            call_fn_kwargs=dict(bulk_edit_tags_details=action_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


TagActionsHelperCustom = get_custom_class("TagActionsHelperCustom")


class ResourceHelper(TagActionsHelperCustom, TagActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            tag_definition_ids=dict(type="list"),
            compartment_id=dict(type="str"),
            resources=dict(
                type="list",
                elements="dict",
                options=dict(
                    id=dict(type="str", required=True),
                    resource_type=dict(type="str", required=True),
                    metadata=dict(type="dict"),
                ),
            ),
            bulk_edit_operations=dict(
                type="list",
                elements="dict",
                options=dict(
                    operation_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "ADD_WHERE_ABSENT",
                            "SET_WHERE_PRESENT",
                            "ADD_OR_SET",
                            "REMOVE",
                        ],
                    ),
                    defined_tags=dict(type="dict", required=True),
                ),
            ),
            action=dict(
                type="str", required=True, choices=["bulk_delete", "bulk_edit"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="tag",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
