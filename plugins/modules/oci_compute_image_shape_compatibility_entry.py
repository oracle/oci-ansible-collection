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
module: oci_compute_image_shape_compatibility_entry
short_description: Manage an ImageShapeCompatibilityEntry resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete an ImageShapeCompatibilityEntry resource in Oracle Cloud Infrastructure
version_added: "2.9"
author: Oracle (@oracle)
options:
    image_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the image.
        type: str
        required: true
    shape_name:
        description:
            - Shape name.
        type: str
        required: true
    ocpu_constraints:
        description:
            - ""
        type: dict
        suboptions:
            min:
                description:
                    - The minimum number of OCPUs supported for this image and shape.
                type: int
            max:
                description:
                    - The maximum number of OCPUs supported for this image and shape.
                type: int
    state:
        description:
            - The state of the ImageShapeCompatibilityEntry.
            - Use I(state=present) to update an existing an ImageShapeCompatibilityEntry.
            - Use I(state=absent) to delete an ImageShapeCompatibilityEntry.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update image_shape_compatibility_entry
  oci_compute_image_shape_compatibility_entry:
    image_id: ocid1.image.oc1..xxxxxxEXAMPLExxxxxx
    shape_name: shape_name_example

- name: Delete image_shape_compatibility_entry
  oci_compute_image_shape_compatibility_entry:
    image_id: ocid1.image.oc1..xxxxxxEXAMPLExxxxxx
    shape_name: shape_name_example
    state: absent

"""

RETURN = """
image_shape_compatibility_entry:
    description:
        - Details of the ImageShapeCompatibilityEntry resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        image_id:
            description:
                - The image OCID.
            returned: on success
            type: string
            sample: ocid1.image.oc1..xxxxxxEXAMPLExxxxxx
        shape:
            description:
                - The shape name.
            returned: on success
            type: string
            sample: shape_example
        ocpu_constraints:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                min:
                    description:
                        - The minimum number of OCPUs supported for this image and shape.
                    returned: on success
                    type: int
                    sample: 56
                max:
                    description:
                        - The maximum number of OCPUs supported for this image and shape.
                    returned: on success
                    type: int
                    sample: 56
    sample: {
        "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
        "shape": "shape_example",
        "ocpu_constraints": {
            "min": 56,
            "max": 56
        }
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
    from oci.core import ComputeClient
    from oci.core.models import AddImageShapeCompatibilityEntryDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ImageShapeCompatibilityEntryHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "shape_name"

    def get_module_resource_id(self):
        return self.module.params.get("shape_name")

    def get_get_fn(self):
        return self.client.get_image_shape_compatibility_entry

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_image_shape_compatibility_entry,
            image_id=self.module.params.get("image_id"),
            shape_name=self.module.params.get("shape_name"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "image_id",
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
            self.client.list_image_shape_compatibility_entries, **kwargs
        )

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def get_update_model_class(self):
        return AddImageShapeCompatibilityEntryDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_image_shape_compatibility_entry,
            call_fn_args=(),
            call_fn_kwargs=dict(
                image_id=self.module.params.get("image_id"),
                shape_name=self.module.params.get("shape_name"),
                add_image_shape_compatibility_entry_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_image_shape_compatibility_entry,
            call_fn_args=(),
            call_fn_kwargs=dict(
                image_id=self.module.params.get("image_id"),
                shape_name=self.module.params.get("shape_name"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


ImageShapeCompatibilityEntryHelperCustom = get_custom_class(
    "ImageShapeCompatibilityEntryHelperCustom"
)


class ResourceHelper(
    ImageShapeCompatibilityEntryHelperCustom, ImageShapeCompatibilityEntryHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            image_id=dict(type="str", required=True),
            shape_name=dict(type="str", required=True),
            ocpu_constraints=dict(
                type="dict", options=dict(min=dict(type="int"), max=dict(type="int"))
            ),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="image_shape_compatibility_entry",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
