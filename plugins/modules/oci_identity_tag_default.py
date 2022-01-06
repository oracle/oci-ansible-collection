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
module: oci_identity_tag_default
short_description: Manage a TagDefault resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a TagDefault resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new tag default in the specified compartment for the specified tag definition.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment. The tag default will be applied to all new resources created in this compartment.
            - Required for create using I(state=present).
        type: str
    tag_definition_id:
        description:
            - The OCID of the tag definition. The tag default will always assign a default value for this tag definition.
            - Required for create using I(state=present).
        type: str
    value:
        description:
            - The default value for the tag definition. This will be applied to all new resources created in the compartment.
            - Required for create using I(state=present), update using I(state=present) with tag_default_id present.
        type: str
    tag_default_id:
        description:
            - The OCID of the tag default.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the TagDefault.
            - Use I(state=present) to create or update a TagDefault.
            - Use I(state=absent) to delete a TagDefault.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create tag_default
  oci_identity_tag_default:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    tag_definition_id: "ocid1.tagdefinition.oc1..xxxxxxEXAMPLExxxxxx"
    value: value_example

- name: Update tag_default
  oci_identity_tag_default:
    # required
    value: value_example
    tag_default_id: "ocid1.tagdefault.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete tag_default
  oci_identity_tag_default:
    # required
    tag_default_id: "ocid1.tagdefault.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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
    from oci.identity.models import CreateTagDefaultDetails
    from oci.identity.models import UpdateTagDefaultDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TagDefaultHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "tag_definition_id"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_tag_defaults, **kwargs
        )

    def get_create_model_class(self):
        return CreateTagDefaultDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_tag_default,
            call_fn_args=(),
            call_fn_kwargs=dict(create_tag_default_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateTagDefaultDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_tag_default,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_default_id=self.module.params.get("tag_default_id"),
                update_tag_default_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_tag_default,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_default_id=self.module.params.get("tag_default_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


TagDefaultHelperCustom = get_custom_class("TagDefaultHelperCustom")


class ResourceHelper(TagDefaultHelperCustom, TagDefaultHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            tag_definition_id=dict(type="str"),
            value=dict(type="str"),
            tag_default_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="tag_default",
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
