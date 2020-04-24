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
module: oci_identity_tag
short_description: Manage a Tag resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Tag resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new tag in the specified tag namespace.
    - The tag requires either the OCID or the name of the tag namespace that will contain this
      tag definition.
    - "You must specify a *name* for the tag, which must be unique across all tags in the tag namespace
      and cannot be changed. The name can contain any ASCII character except the space (_) or period (.) characters.
      Names are case insensitive. That means, for example, \\"myTag\\" and \\"mytag\\" are not allowed in the same namespace.
      If you specify a name that's already in use in the tag namespace, a 409 error is returned."
    - "The tag must have a *description*. It does not have to be unique, and you can change it with
      L(UpdateTag,https://docs.cloud.oracle.com/#/en/identity/latest/Tag/UpdateTag)."
version_added: "2.5"
options:
    tag_namespace_id:
        description:
            - The OCID of the tag namespace.
        type: str
        required: true
    name:
        description:
            - The name you assign to the tag during creation. The name must be unique within the tag namespace and cannot be changed.
        type: str
        required: true
    description:
        description:
            - The description you assign to the tag during creation.
            - Required for create using I(state=present).
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    is_cost_tracking:
        description:
            - Indicates whether the tag is enabled for cost tracking.
        type: bool
    is_retired:
        description:
            - Whether the tag is retired.
              See L(Retiring Key Definitions and Namespace Definitions,https://docs.cloud.oracle.com/Content/Identity/Concepts/taggingoverview.htm#Retiring).
        type: bool
    state:
        description:
            - The state of the Tag.
            - Use I(state=present) to create or update a Tag.
            - Use I(state=absent) to delete a Tag.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create tag
  oci_identity_tag:
    tag_namespace_id: ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx
    name: CostCenter
    description: This tag will show the cost center that will be used for billing of associated resources.

- name: Update tag
  oci_identity_tag:
    tag_namespace_id: ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx
    name: CostCenter

- name: Delete tag
  oci_identity_tag:
    tag_namespace_id: ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx
    name: CostCenter
    state: absent

"""

RETURN = """
tag:
    description:
        - Details of the Tag resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment that contains the tag definition.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        tag_namespace_id:
            description:
                - The OCID of the namespace that contains the tag definition.
            returned: on success
            type: string
            sample: ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx
        tag_namespace_name:
            description:
                - The name of the tag namespace that contains the tag definition.
            returned: on success
            type: string
            sample: tag_namespace_name_example
        id:
            description:
                - The OCID of the tag definition.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        name:
            description:
                - The name of the tag. The name must be unique across all tags in the namespace and can't be changed.
            returned: on success
            type: string
            sample: name_example
        description:
            description:
                - The description you assign to the tag.
            returned: on success
            type: string
            sample: description_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        is_retired:
            description:
                - Indicates whether the tag is retired.
                  See L(Retiring Key Definitions and Namespace
                  Definitions,https://docs.cloud.oracle.com/Content/Identity/Concepts/taggingoverview.htm#Retiring).
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The tag's current state. After creating a tag, make sure its `lifecycleState` is ACTIVE before using it. After retiring a tag, make sure its
                  `lifecycleState` is INACTIVE before using it. If you delete a tag, you cannot delete another tag until the deleted tag's `lifecycleState`
                  changes from DELETING to DELETED.
            returned: on success
            type: string
            sample: ACTIVE
        time_created:
            description:
                - Date and time the tag was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        is_cost_tracking:
            description:
                - Indicates whether the tag is enabled for cost tracking.
            returned: on success
            type: bool
            sample: true
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "tag_namespace_id": "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx",
        "tag_namespace_name": "tag_namespace_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "is_retired": true,
        "lifecycle_state": "ACTIVE",
        "time_created": "2016-08-25T21:10:29.600Z",
        "is_cost_tracking": true
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient
    from oci.identity.models import CreateTagDetails
    from oci.identity.models import UpdateTagDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TagHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_tag

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tag,
            tag_namespace_id=self.module.params.get("tag_namespace_id"),
            tag_name=self.module.params.get("name"),
        )

    def list_resources(self):
        required_list_method_params = [
            "tag_namespace_id",
        ]

        optional_list_method_params = []

        required_kwargs = dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

        return oci_common_utils.list_all_resources(self.client.list_tags, **kwargs)

    def get_create_model_class(self):
        return CreateTagDetails

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_tag,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_namespace_id=self.module.params.get("tag_namespace_id"),
                create_tag_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateTagDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_tag,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_namespace_id=self.module.params.get("tag_namespace_id"),
                tag_name=self.module.params.get("name"),
                update_tag_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_tag,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_namespace_id=self.module.params.get("tag_namespace_id"),
                tag_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or oci_common_utils.get_work_request_completed_states(),
        )


TagHelperCustom = get_custom_class("TagHelperCustom")


class ResourceHelper(TagHelperCustom, TagHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            tag_namespace_id=dict(type="str", required=True),
            name=dict(type="str", required=True),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            is_cost_tracking=dict(type="bool"),
            is_retired=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
