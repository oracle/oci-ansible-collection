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
module: oci_identity_tag_namespace
short_description: Manage a TagNamespace resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a TagNamespace resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new tag namespace in the specified compartment.
    - You must specify the compartment ID in the request object (remember that the tenancy is simply the root
      compartment).
    - "You must also specify a *name* for the namespace, which must be unique across all namespaces in your tenancy
      and cannot be changed. The name can contain any ASCII character except the space (_) or period (.).
      Names are case insensitive. That means, for example, \\"myNamespace\\" and \\"mynamespace\\" are not allowed
      in the same tenancy. Once you created a namespace, you cannot change the name.
      If you specify a name that's already in use in the tenancy, a 409 error is returned."
    - "You must also specify a *description* for the namespace.
      It does not have to be unique, and you can change it with
      L(UpdateTagNamespace,https://docs.cloud.oracle.com/#/en/identity/latest/TagNamespace/UpdateTagNamespace)."
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the tenancy containing the tag namespace.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    name:
        description:
            - The name you assign to the tag namespace during creation. It must be unique across all tag namespaces in the tenancy and cannot be changed.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - The description you assign to the tag namespace during creation.
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
    tag_namespace_id:
        description:
            - The OCID of the tag namespace.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    is_retired:
        description:
            - Whether the tag namespace is retired.
              See L(Retiring Key Definitions and Namespace Definitions,https://docs.cloud.oracle.com/Content/Identity/Concepts/taggingoverview.htm#Retiring).
        type: bool
    state:
        description:
            - The state of the TagNamespace.
            - Use I(state=present) to create or update a TagNamespace.
            - Use I(state=absent) to delete a TagNamespace.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create tag_namespace
  oci_identity_tag_namespace:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    name: name_example
    description: description_example

- name: Update tag_namespace using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_identity_tag_namespace:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    name: name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_retired: true

- name: Update tag_namespace
  oci_identity_tag_namespace:
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    tag_namespace_id: ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete tag_namespace
  oci_identity_tag_namespace:
    tag_namespace_id: ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete tag_namespace using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_identity_tag_namespace:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    name: name_example
    state: absent

"""

RETURN = """
tag_namespace:
    description:
        - Details of the TagNamespace resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the tag namespace.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment that contains the tag namespace.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        name:
            description:
                - The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.
            returned: on success
            type: string
            sample: name_example
        description:
            description:
                - The description you assign to the tag namespace.
            returned: on success
            type: string
            sample: description_example
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
        is_retired:
            description:
                - Whether the tag namespace is retired.
                  See L(Retiring Key Definitions and Namespace
                  Definitions,https://docs.cloud.oracle.com/Content/Identity/Concepts/taggingoverview.htm#Retiring).
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The tagnamespace's current state. After creating a tagnamespace, make sure its `lifecycleState` is ACTIVE before using it. After retiring a
                  tagnamespace, make sure its `lifecycleState` is INACTIVE before using it.
            returned: on success
            type: string
            sample: ACTIVE
        time_created:
            description:
                - "Date and time the tagNamespace was created, in the format defined by RFC3339.
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "is_retired": true,
        "lifecycle_state": "ACTIVE",
        "time_created": "2016-08-25T21:10:29.600Z"
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
    from oci.identity.models import CreateTagNamespaceDetails
    from oci.identity.models import UpdateTagNamespaceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TagNamespaceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_tag_namespaces, **kwargs
        )

    def get_create_model_class(self):
        return CreateTagNamespaceDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_tag_namespace,
            call_fn_args=(),
            call_fn_kwargs=dict(create_tag_namespace_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateTagNamespaceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_tag_namespace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_namespace_id=self.module.params.get("tag_namespace_id"),
                update_tag_namespace_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_tag_namespace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_namespace_id=self.module.params.get("tag_namespace_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


TagNamespaceHelperCustom = get_custom_class("TagNamespaceHelperCustom")


class ResourceHelper(TagNamespaceHelperCustom, TagNamespaceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            tag_namespace_id=dict(aliases=["id"], type="str"),
            is_retired=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
