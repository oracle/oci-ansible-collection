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
module: oci_identity_tag_default_actions
short_description: Perform actions on a TagDefault resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a TagDefault resource in Oracle Cloud Infrastructure
    - For I(action=add_tag_default_lock), add a resource lock to a tag default.
    - For I(action=remove_tag_default_lock), remove a resource lock from a tag default.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    related_resource_id:
        description:
            - The ID of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.
            - Applicable only for I(action=add_tag_default_lock).
        type: str
    msg:
        description:
            - A message added by the creator of the lock. This is typically used to give an
              indication of why the resource is locked.
            - Applicable only for I(action=add_tag_default_lock).
        type: str
        aliases: ["message"]
    tag_default_id:
        description:
            - The OCID of the tag default.
        type: str
        aliases: ["id"]
        required: true
    type:
        description:
            - Type of the lock.
        type: str
        choices:
            - "FULL"
            - "DELETE"
        required: true
    action:
        description:
            - The action to perform on the TagDefault.
        type: str
        required: true
        choices:
            - "add_tag_default_lock"
            - "remove_tag_default_lock"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_tag_default_lock on tag_default
  oci_identity_tag_default_actions:
    # required
    tag_default_id: "ocid1.tagdefault.oc1..xxxxxxEXAMPLExxxxxx"
    type: FULL
    action: add_tag_default_lock

    # optional
    related_resource_id: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
    msg: msg_example

- name: Perform action remove_tag_default_lock on tag_default
  oci_identity_tag_default_actions:
    # required
    tag_default_id: "ocid1.tagdefault.oc1..xxxxxxEXAMPLExxxxxx"
    type: FULL
    action: remove_tag_default_lock

"""

RETURN = """
tag_default:
    description:
        - Details of the TagDefault resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the tag default.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment. The tag default applies to all new resources that get created in the
                  compartment. Resources that existed before the tag default was created are not tagged.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        tag_namespace_id:
            description:
                - The OCID of the tag namespace that contains the tag definition.
            returned: on success
            type: str
            sample: "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx"
        tag_definition_id:
            description:
                - The OCID of the tag definition. The tag default will always assign a default value for this tag definition.
            returned: on success
            type: str
            sample: "ocid1.tagdefinition.oc1..xxxxxxEXAMPLExxxxxx"
        tag_definition_name:
            description:
                - The name used in the tag definition. This field is informational in the context of the tag default.
            returned: on success
            type: str
            sample: tag_definition_name_example
        value:
            description:
                - The default value for the tag definition. This will be applied to all resources created in the compartment.
            returned: on success
            type: str
            sample: value_example
        time_created:
            description:
                - Date and time the `TagDefault` object was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The tag default's current state. After creating a `TagDefault`, make sure its `lifecycleState` is ACTIVE before using it.
            returned: on success
            type: str
            sample: ACTIVE
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "tag_namespace_id": "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx",
        "tag_definition_id": "ocid1.tagdefinition.oc1..xxxxxxEXAMPLExxxxxx",
        "tag_definition_name": "tag_definition_name_example",
        "value": "value_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE"
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
    from oci.identity import IdentityClient
    from oci.identity.models import AddLockDetails
    from oci.identity.models import RemoveLockDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TagDefaultActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_tag_default_lock
        remove_tag_default_lock
    """

    @staticmethod
    def get_module_resource_id_param():
        return "tag_default_id"

    def get_module_resource_id(self):
        return self.module.params.get("tag_default_id")

    def get_get_fn(self):
        return self.client.get_tag_default

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tag_default,
            tag_default_id=self.module.params.get("tag_default_id"),
        )

    def add_tag_default_lock(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddLockDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_tag_default_lock,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_default_id=self.module.params.get("tag_default_id"),
                add_lock_details=action_details,
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

    def remove_tag_default_lock(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveLockDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_tag_default_lock,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_default_id=self.module.params.get("tag_default_id"),
                remove_lock_details=action_details,
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


TagDefaultActionsHelperCustom = get_custom_class("TagDefaultActionsHelperCustom")


class ResourceHelper(TagDefaultActionsHelperCustom, TagDefaultActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            related_resource_id=dict(type="str"),
            msg=dict(aliases=["message"], type="str"),
            tag_default_id=dict(aliases=["id"], type="str", required=True),
            type=dict(type="str", required=True, choices=["FULL", "DELETE"]),
            action=dict(
                type="str",
                required=True,
                choices=["add_tag_default_lock", "remove_tag_default_lock"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="tag_default",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
