#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
      tags from all resources in your tenancy.
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
version_added: "2.9"
author: Oracle (@oracle)
options:
    tag_definition_ids:
        description:
            - The OCIDs of the tag definitions to delete
        type: list
        required: true
    action:
        description:
            - The action to perform on the Tag.
        type: str
        required: true
        choices:
            - "bulk_delete"
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

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TagActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        bulk_delete
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


TagActionsHelperCustom = get_custom_class("TagActionsHelperCustom")


class ResourceHelper(TagActionsHelperCustom, TagActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            tag_definition_ids=dict(type="list", required=True),
            action=dict(type="str", required=True, choices=["bulk_delete"]),
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
