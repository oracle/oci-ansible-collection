#!/usr/bin/python
# Copyright (c) 2017, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


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
    - For I(state=present), creates a new Tag Default in the specified Compartment for the specified Tag Definition.
version_added: "2.5"
options:
    compartment_id:
        description:
            - The OCID of the Compartment. The Tag Default will apply to any resource contained in this Compartment.
            - Required for create using I(state=present).
    tag_definition_id:
        description:
            - The OCID of the Tag Definition. The Tag Default will always assign a default value for this Tag Definition.
            - Required for create using I(state=present).
    value:
        description:
            - The default value for the Tag Definition. This will be applied to all resources created in the Compartment.
            - Required for create using I(state=present), update using I(state=present) with tag_default_id present.
    tag_default_id:
        description:
            - The OCID of the Tag Default.
            - Required for update using I(state=present), I(state=absent).
        aliases: ["id"]
    state:
        description:
            - The state of the TagDefault.
            - Use I(state=present) to create or update a TagDefault.
            - Use I(state=absent) to delete a TagDefault.
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
- name: Create tag_default
  oci_identity_tag_default:
    compartment_id: ocid1.compartment.oc1..aaaaaaaamnuh3osn3n77vx2ofkx5zwpaqae5rox2zfoscd7z3uvnhpqf5f7q
    tag_definition_id: ocid1.tagdefinition.oc1..aaaaaaaash5swxlw2ppo2rjqy5cwknrggb3ogpdzmsk6f4kdjfcwwkys3zga
    value: such-default-wow

- name: Update tag_default
  oci_identity_tag_default:
    value: so-tagging
    tag_default_id: ocid1.tagdefault.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete tag_default
  oci_identity_tag_default:
    tag_default_id: ocid1.tagdefault.oc1..xxxxxxEXAMPLExxxxxx
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
                - The OCID of the Tag Default.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the Compartment. The Tag Default will apply to any resource contained in this Compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        tag_namespace_id:
            description:
                - The OCID of the Tag Namespace that contains the Tag Definition.
            returned: on success
            type: string
            sample: ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx
        tag_definition_id:
            description:
                - The OCID of the Tag Definition. The Tag Default will always assign a default value for this Tag Definition.
            returned: on success
            type: string
            sample: ocid1.tagdefinition.oc1..xxxxxxEXAMPLExxxxxx
        tag_definition_name:
            description:
                - The name used in the Tag Definition. This field is informational in the context of the Tag Default.
            returned: on success
            type: string
            sample: tag_definition_name_example
        value:
            description:
                - The default value for the Tag Definition. This will be applied to all resources created in the Compartment.
            returned: on success
            type: string
            sample: value_example
        time_created:
            description:
                - Date and time the `TagDefault` object was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        lifecycle_state:
            description:
                - The tag default's current state. After creating a tagdefault, make sure its `lifecycleState` is ACTIVE before using it.
            returned: on success
            type: string
            sample: ACTIVE
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "tag_namespace_id": "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx",
        "tag_definition_id": "ocid1.tagdefinition.oc1..xxxxxxEXAMPLExxxxxx",
        "tag_definition_name": "tag_definition_name_example",
        "value": "value_example",
        "time_created": "2016-08-25T21:10:29.600Z",
        "lifecycle_state": "ACTIVE"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
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

    @staticmethod
    def get_module_resource_id_param():
        return "tag_default_id"

    def get_module_resource_id(self):
        return self.module.params.get("tag_default_id")

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tag_default,
            tag_default_id=self.module.params.get("tag_default_id"),
        )

    def list_resources(self):
        required_list_method_params = []

        optional_list_method_params = ["compartment_id", "tag_definition_id"]

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

        return oci_common_utils.list_all_resources(
            self.client.list_tag_defaults, **kwargs
        )

    def get_create_model_class(self):
        return CreateTagDefaultDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_common_utils.call_with_backoff(
            self.client.create_tag_default, create_tag_default_details=create_details
        )

    def get_update_model_class(self):
        return UpdateTagDefaultDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_common_utils.call_with_backoff(
            self.client.update_tag_default,
            tag_default_id=self.module.params.get("tag_default_id"),
            update_tag_default_details=update_details,
        )

    def delete_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.delete_tag_default,
            tag_default_id=self.module.params.get("tag_default_id"),
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
        module=module, resource_type="tag_default", service_client_class=IdentityClient
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
