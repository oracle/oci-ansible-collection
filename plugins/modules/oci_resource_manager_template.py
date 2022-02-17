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
module: oci_resource_manager_template
short_description: Manage a Template resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Template resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a private template in the specified compartment.
    - "This resource has the following action operations in the M(oracle.oci.oci_resource_manager_template_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing this template.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - The template's display name. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Description of the template. Avoid entering confidential information.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    long_description:
        description:
            - Detailed description of the template. This description is displayed in the Console page listing templates when the template is expanded. Avoid
              entering confidential information.
            - This parameter is updatable.
        type: str
    logo_file_base64_encoded:
        description:
            - "Base64-encoded logo to use as the template icon.
              Template icon file requirements: PNG format, 50 KB maximum, 110 x 110 pixels."
            - This parameter is updatable.
        type: str
    template_config_source:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            template_config_source_type:
                description:
                    - Specifies the `configSourceType` for uploading the Terraform configuration.
                    - This parameter is updatable.
                type: str
                choices:
                    - "ZIP_UPLOAD"
                required: true
            zip_file_base64_encoded:
                description:
                    - ""
                    - This parameter is updatable.
                    - Applicable when template_config_source_type is 'ZIP_UPLOAD'
                type: str
    freeform_tags:
        description:
            - "Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    template_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the template.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Template.
            - Use I(state=present) to create or update a Template.
            - Use I(state=absent) to delete a Template.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create template
  oci_resource_manager_template:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    template_config_source:
      # required
      template_config_source_type: ZIP_UPLOAD
      zip_file_base64_encoded: zip_file_base64_encoded_example

    # optional
    long_description: long_description_example
    logo_file_base64_encoded: logo_file_base64_encoded_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update template
  oci_resource_manager_template:
    # required
    template_id: "ocid1.template.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    long_description: long_description_example
    logo_file_base64_encoded: logo_file_base64_encoded_example
    template_config_source:
      # required
      template_config_source_type: ZIP_UPLOAD
      zip_file_base64_encoded: zip_file_base64_encoded_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update template using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_resource_manager_template:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    long_description: long_description_example
    logo_file_base64_encoded: logo_file_base64_encoded_example
    template_config_source:
      # required
      template_config_source_type: ZIP_UPLOAD
      zip_file_base64_encoded: zip_file_base64_encoded_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete template
  oci_resource_manager_template:
    # required
    template_id: "ocid1.template.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete template using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_resource_manager_template:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
template:
    description:
        - Details of the Template resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the template.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing this template.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        category_id:
            description:
                - Unique identifier for the category where the template is located.
                  Possible values are `0` (Quick Starts), `1` (Service), `2` (Architecture), and `3` (Private).
            returned: on success
            type: str
            sample: "ocid1.category.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Human-readable name of the template.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Brief description of the template.
            returned: on success
            type: str
            sample: description_example
        long_description:
            description:
                - Detailed description of the template. This description is displayed in the Console page listing templates when the template is expanded. Avoid
                  entering confidential information.
            returned: on success
            type: str
            sample: long_description_example
        is_free_tier:
            description:
                - whether the template will work for free tier tenancy.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - "The date and time at which the template was created.
                  Format is defined by RFC3339.
                  Example: `2020-11-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        template_config_source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                template_config_source_type:
                    description:
                        - The type of configuration source to use for the template configuration.
                    returned: on success
                    type: str
                    sample: ZIP_UPLOAD
        lifecycle_state:
            description:
                - The current lifecycle state of the template.
            returned: on success
            type: str
            sample: ACTIVE
        freeform_tags:
            description:
                - "Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "category_id": "ocid1.category.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "long_description": "long_description_example",
        "is_free_tier": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "template_config_source": {
            "template_config_source_type": "ZIP_UPLOAD"
        },
        "lifecycle_state": "ACTIVE",
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.resource_manager import ResourceManagerClient
    from oci.resource_manager.models import CreateTemplateDetails
    from oci.resource_manager.models import UpdateTemplateDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TemplateHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(TemplateHelperGen, self).get_possible_entity_types() + [
            "ormtemplate",
            "ormtemplates",
            "resourceManagerormtemplate",
            "resourceManagerormtemplates",
            "ormtemplateresource",
            "ormtemplatesresource",
            "template",
            "templates",
            "resourceManagertemplate",
            "resourceManagertemplates",
            "templateresource",
            "templatesresource",
            "resourcemanager",
        ]

    def get_module_resource_id_param(self):
        return "template_id"

    def get_module_resource_id(self):
        return self.module.params.get("template_id")

    def get_get_fn(self):
        return self.client.get_template

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_template, template_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_template, template_id=self.module.params.get("template_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "template_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_templates, **kwargs)

    def get_create_model_class(self):
        return CreateTemplateDetails

    def get_exclude_attributes(self):
        return ["logo_file_base64_encoded"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_template,
            call_fn_args=(),
            call_fn_kwargs=dict(create_template_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateTemplateDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_template,
            call_fn_args=(),
            call_fn_kwargs=dict(
                template_id=self.module.params.get("template_id"),
                update_template_details=update_details,
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
            call_fn=self.client.delete_template,
            call_fn_args=(),
            call_fn_kwargs=dict(template_id=self.module.params.get("template_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


TemplateHelperCustom = get_custom_class("TemplateHelperCustom")


class ResourceHelper(TemplateHelperCustom, TemplateHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            long_description=dict(type="str"),
            logo_file_base64_encoded=dict(type="str"),
            template_config_source=dict(
                type="dict",
                options=dict(
                    template_config_source_type=dict(
                        type="str", required=True, choices=["ZIP_UPLOAD"]
                    ),
                    zip_file_base64_encoded=dict(type="str"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            template_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="template",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
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
