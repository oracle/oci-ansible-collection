#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_service_catalog_private_application
short_description: Manage a PrivateApplication resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a PrivateApplication resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a private application along with a single package to be hosted.
    - "This resource has the following action operations in the M(oracle.oci.oci_service_catalog_private_application_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment where you want to create the private
              application.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    package_details:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            package_type:
                description:
                    - The package's type.
                type: str
                choices:
                    - "STACK"
                required: true
            version:
                description:
                    - The package version.
                type: str
                required: true
            zip_file_base64_encoded:
                description:
                    - Base-64 payload of the Terraform zip package.
                type: str
    display_name:
        description:
            - The name of the private application.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    short_description:
        description:
            - A short description of the private application.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    long_description:
        description:
            - A long description of the private application.
            - This parameter is updatable.
        type: str
    logo_file_base64_encoded:
        description:
            - "Base64-encoded logo to use as the private application icon.
              Template icon file requirements: PNG format, 50 KB maximum, 130 x 130 pixels."
            - This parameter is updatable.
        type: str
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    private_application_id:
        description:
            - The unique identifier for the private application.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the PrivateApplication.
            - Use I(state=present) to create or update a PrivateApplication.
            - Use I(state=absent) to delete a PrivateApplication.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create private_application
  oci_service_catalog_private_application:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    package_details:
      # required
      package_type: STACK
      version: version_example

      # optional
      zip_file_base64_encoded: zip_file_base64_encoded_example
    display_name: display_name_example
    short_description: short_description_example

    # optional
    long_description: long_description_example
    logo_file_base64_encoded: logo_file_base64_encoded_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update private_application
  oci_service_catalog_private_application:
    # required
    private_application_id: "ocid1.privateapplication.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    short_description: short_description_example
    long_description: long_description_example
    logo_file_base64_encoded: logo_file_base64_encoded_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update private_application using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_service_catalog_private_application:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    short_description: short_description_example
    long_description: long_description_example
    logo_file_base64_encoded: logo_file_base64_encoded_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Delete private_application
  oci_service_catalog_private_application:
    # required
    private_application_id: "ocid1.privateapplication.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete private_application using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_service_catalog_private_application:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
private_application:
    description:
        - Details of the PrivateApplication resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        lifecycle_state:
            description:
                - The lifecycle state of the private application.
            returned: on success
            type: str
            sample: CREATING
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment where the private application resides.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The unique identifier for the private application in Marketplace.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the private application.
            returned: on success
            type: str
            sample: display_name_example
        short_description:
            description:
                - A short description of the private application.
            returned: on success
            type: str
            sample: short_description_example
        long_description:
            description:
                - A long description of the private application.
            returned: on success
            type: str
            sample: long_description_example
        logo:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                display_name:
                    description:
                        - The name used to refer to the uploaded data.
                    returned: on success
                    type: str
                    sample: display_name_example
                content_url:
                    description:
                        - The content URL of the uploaded data.
                    returned: on success
                    type: str
                    sample: content_url_example
                mime_type:
                    description:
                        - The MIME type of the uploaded data.
                    returned: on success
                    type: str
                    sample: mime_type_example
        package_type:
            description:
                - Type of packages within this private application.
            returned: on success
            type: str
            sample: STACK
        time_created:
            description:
                - The date and time the private application was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2021-05-26T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the private application was last modified, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2021-12-10T05:10:29.721Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
    sample: {
        "lifecycle_state": "CREATING",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "short_description": "short_description_example",
        "long_description": "long_description_example",
        "logo": {
            "display_name": "display_name_example",
            "content_url": "content_url_example",
            "mime_type": "mime_type_example"
        },
        "package_type": "STACK",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.service_catalog import ServiceCatalogClient
    from oci.service_catalog.models import CreatePrivateApplicationDetails
    from oci.service_catalog.models import UpdatePrivateApplicationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PrivateApplicationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(PrivateApplicationHelperGen, self).get_possible_entity_types() + [
            "privateapplication",
            "privateapplications",
            "serviceCatalogprivateapplication",
            "serviceCatalogprivateapplications",
            "privateapplicationresource",
            "privateapplicationsresource",
            "servicecatalog",
        ]

    def get_module_resource_id_param(self):
        return "private_application_id"

    def get_module_resource_id(self):
        return self.module.params.get("private_application_id")

    def get_get_fn(self):
        return self.client.get_private_application

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_application,
            private_application_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_application,
            private_application_id=self.module.params.get("private_application_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["private_application_id", "display_name"]

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
            self.client.list_private_applications, **kwargs
        )

    def get_create_model_class(self):
        return CreatePrivateApplicationDetails

    def get_exclude_attributes(self):
        return ["logo_file_base64_encoded", "package_details"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_private_application,
            call_fn_args=(),
            call_fn_kwargs=dict(create_private_application_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdatePrivateApplicationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_private_application,
            call_fn_args=(),
            call_fn_kwargs=dict(
                private_application_id=self.module.params.get("private_application_id"),
                update_private_application_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_private_application,
            call_fn_args=(),
            call_fn_kwargs=dict(
                private_application_id=self.module.params.get("private_application_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


PrivateApplicationHelperCustom = get_custom_class("PrivateApplicationHelperCustom")


class ResourceHelper(PrivateApplicationHelperCustom, PrivateApplicationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            package_details=dict(
                type="dict",
                options=dict(
                    package_type=dict(type="str", required=True, choices=["STACK"]),
                    version=dict(type="str", required=True),
                    zip_file_base64_encoded=dict(type="str"),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            short_description=dict(type="str"),
            long_description=dict(type="str"),
            logo_file_base64_encoded=dict(type="str"),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            private_application_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="private_application",
        service_client_class=ServiceCatalogClient,
        namespace="service_catalog",
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
