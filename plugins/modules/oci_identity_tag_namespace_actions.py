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
module: oci_identity_tag_namespace_actions
short_description: Perform actions on a TagNamespace resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a TagNamespace resource in Oracle Cloud Infrastructure
    - "For I(action=cascade_delete), deletes the specified tag namespace. This operation triggers a process that removes all of the tags
      defined in the specified tag namespace from all resources in your tenancy and then deletes the tag namespace.
      After you start the delete operation:
        * New tag key definitions cannot be created under the namespace.
        * The state of the tag namespace changes to DELETING.
        * Tag removal from the resources begins.
      This process can take up to 48 hours depending on the number of tag definitions in the namespace, the number of resources
      that are tagged, and the locations of the regions in which those resources reside.
      After all tags are removed, the state changes to DELETED. You cannot restore a deleted tag namespace. After the deleted tag namespace
      changes its state to DELETED, you can use the name of the deleted tag namespace again.
      After you start this operation, you cannot start either the L(DeleteTag,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/Tag/DeleteTag)
      or the L(BulkDeleteTags,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/Tag/BulkDeleteTags) operation until this process completes.
      To delete a tag namespace, you must first retire it. Use L(UpdateTagNamespace,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/identity/20160918/TagNamespace/UpdateTagNamespace)
      to retire a tag namespace."
version_added: "2.9"
author: Oracle (@oracle)
options:
    tag_namespace_id:
        description:
            - The OCID of the tag namespace.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the TagNamespace.
        type: str
        required: true
        choices:
            - "cascade_delete"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action cascade_delete on tag_namespace
  oci_identity_tag_namespace_actions:
    tag_namespace_id: ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx
    action: cascade_delete

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

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TagNamespaceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cascade_delete
    """

    @staticmethod
    def get_module_resource_id_param():
        return "tag_namespace_id"

    def get_module_resource_id(self):
        return self.module.params.get("tag_namespace_id")

    def get_get_fn(self):
        return self.client.get_tag_namespace

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tag_namespace,
            tag_namespace_id=self.module.params.get("tag_namespace_id"),
        )

    def cascade_delete(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cascade_delete_tag_namespace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_namespace_id=self.module.params.get("tag_namespace_id"),
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


TagNamespaceActionsHelperCustom = get_custom_class("TagNamespaceActionsHelperCustom")


class ResourceHelper(TagNamespaceActionsHelperCustom, TagNamespaceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            tag_namespace_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["cascade_delete"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="tag_namespace",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
