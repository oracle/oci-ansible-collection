#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_marketplace_publication
short_description: Manage a Publication resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Publication resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a publication of the given type with an optional default package
    - "This resource has the following action operations in the M(oci_publication_actions) module: change_compartment."
version_added: "2.9"
author: Oracle (@oracle)
options:
    listing_type:
        description:
            - In which catalog the listing should exist.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        choices:
            - "COMMUNITY"
            - "PARTNER"
            - "PRIVATE"
    name:
        description:
            - The name of the listing.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
    short_description:
        description:
            - short description of the catalog listing
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    long_description:
        description:
            - short description of the catalog listing
            - This parameter is updatable.
        type: str
    support_contacts:
        description:
            - Contact information to use to get support from the publisher for the listing.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        suboptions:
            name:
                description:
                    - The name of the contact.
                type: str
            phone:
                description:
                    - The phone number of the contact.
                type: str
            email:
                description:
                    - The email of the contact.
                type: str
            subject:
                description:
                    - The email subject line to use when contacting support.
                type: str
    compartment_id:
        description:
            - The OCID of the compartment to create the resource within.
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
            package_version:
                description:
                    - The version of the package
                type: str
                required: true
            package_type:
                description:
                    - Type of the artifact of the listing
                type: str
                choices:
                    - "IMAGE"
                required: true
            operating_system:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    name:
                        description:
                            - name of the operating system
                        type: str
            eula:
                description:
                    - End User License Agreeement that a consumer of this listing has to accept
                type: list
                required: true
                suboptions:
                    eula_type:
                        description:
                            - the specified eula's type
                        type: str
                        choices:
                            - "TEXT"
                        required: true
                    license_text:
                        description:
                            - text of the eula
                        type: str
            image_id:
                description:
                    - base image id of the listing
                type: str
    is_agreement_acknowledged:
        description:
            - Acknowledgement that invoker has the right and authority to share this Community Image in accordance with their agreement with Oracle applicable
              to the Services and the related Service Specifications
            - Required for create using I(state=present).
        type: bool
    defined_tags:
        description:
            - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    publication_id:
        description:
            - The unique identifier for the listing.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Publication.
            - Use I(state=present) to create or update a Publication.
            - Use I(state=absent) to delete a Publication.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create publication
  oci_marketplace_publication:
    listing_type: COMMUNITY
    name: name_example
    short_description: short_description_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    package_details:
      package_version: package_version_example
      package_type: IMAGE
      eula:
      - eula_type: TEXT
    is_agreement_acknowledged: true

- name: Update publication using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_marketplace_publication:
    listing_type: COMMUNITY
    name: name_example
    short_description: short_description_example
    long_description: long_description_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update publication
  oci_marketplace_publication:
    name: name_example
    short_description: short_description_example
    publication_id: "ocid1.publication.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete publication
  oci_marketplace_publication:
    publication_id: "ocid1.publication.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete publication using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_marketplace_publication:
    listing_type: COMMUNITY
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
publication:
    description:
        - Details of the Publication resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        lifecycle_state:
            description:
                - The state of the listing in its lifecycle
            returned: on success
            type: string
            sample: CREATING
        compartment_id:
            description:
                - The Compartment id where the listings exists
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The unique identifier for the listing in Marketplace.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the listing.
            returned: on success
            type: string
            sample: name_example
        short_description:
            description:
                - A short description of the listing.
            returned: on success
            type: string
            sample: short_description_example
        long_description:
            description:
                - A long description of the listing.
            returned: on success
            type: string
            sample: long_description_example
        support_contacts:
            description:
                - Contact information to use to get support from the publisher for the listing.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the contact.
                    returned: on success
                    type: string
                    sample: name_example
                phone:
                    description:
                        - The phone number of the contact.
                    returned: on success
                    type: string
                    sample: phone_example
                email:
                    description:
                        - The email of the contact.
                    returned: on success
                    type: string
                    sample: email_example
                subject:
                    description:
                        - The email subject line to use when contacting support.
                    returned: on success
                    type: string
                    sample: subject_example
        icon:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name used to refer to the upload data.
                    returned: on success
                    type: string
                    sample: name_example
                content_url:
                    description:
                        - The content URL of the upload data.
                    returned: on success
                    type: string
                    sample: content_url_example
                mime_type:
                    description:
                        - The MIME type of the upload data.
                    returned: on success
                    type: string
                    sample: mime_type_example
                file_extension:
                    description:
                        - The file extension of the upload data.
                    returned: on success
                    type: string
                    sample: file_extension_example
        package_type:
            description:
                - The listing's package type.
            returned: on success
            type: string
            sample: ORCHESTRATION
        listing_type:
            description:
                - In which catalog the listing should exist.
            returned: on success
            type: string
            sample: COMMUNITY
        supported_operating_systems:
            description:
                - List of operating systems supprted.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - name of the operating system
                    returned: on success
                    type: string
                    sample: name_example
        time_created:
            description:
                - The date and time this publication was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        defined_tags:
            description:
                - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
    sample: {
        "lifecycle_state": "CREATING",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "short_description": "short_description_example",
        "long_description": "long_description_example",
        "support_contacts": [{
            "name": "name_example",
            "phone": "phone_example",
            "email": "email_example",
            "subject": "subject_example"
        }],
        "icon": {
            "name": "name_example",
            "content_url": "content_url_example",
            "mime_type": "mime_type_example",
            "file_extension": "file_extension_example"
        },
        "package_type": "ORCHESTRATION",
        "listing_type": "COMMUNITY",
        "supported_operating_systems": [{
            "name": "name_example"
        }],
        "time_created": "2016-08-25T21:10:29.600Z",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'}
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
    from oci.marketplace import MarketplaceClient
    from oci.marketplace.models import CreatePublicationDetails
    from oci.marketplace.models import UpdatePublicationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PublicationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "publication_id"

    def get_module_resource_id(self):
        return self.module.params.get("publication_id")

    def get_get_fn(self):
        return self.client.get_publication

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_publication,
            publication_id=self.module.params.get("publication_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "listing_type",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name", "publication_id"]

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
            self.client.list_publications, **kwargs
        )

    def get_create_model_class(self):
        return CreatePublicationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_publication,
            call_fn_args=(),
            call_fn_kwargs=dict(create_publication_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdatePublicationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_publication,
            call_fn_args=(),
            call_fn_kwargs=dict(
                publication_id=self.module.params.get("publication_id"),
                update_publication_details=update_details,
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
            call_fn=self.client.delete_publication,
            call_fn_args=(),
            call_fn_kwargs=dict(
                publication_id=self.module.params.get("publication_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


PublicationHelperCustom = get_custom_class("PublicationHelperCustom")


class ResourceHelper(PublicationHelperCustom, PublicationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            listing_type=dict(type="str", choices=["COMMUNITY", "PARTNER", "PRIVATE"]),
            name=dict(type="str"),
            short_description=dict(type="str"),
            long_description=dict(type="str"),
            support_contacts=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str"),
                    phone=dict(type="str"),
                    email=dict(type="str"),
                    subject=dict(type="str"),
                ),
            ),
            compartment_id=dict(type="str"),
            package_details=dict(
                type="dict",
                options=dict(
                    package_version=dict(type="str", required=True),
                    package_type=dict(type="str", required=True, choices=["IMAGE"]),
                    operating_system=dict(
                        type="dict", required=True, options=dict(name=dict(type="str"))
                    ),
                    eula=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            eula_type=dict(type="str", required=True, choices=["TEXT"]),
                            license_text=dict(type="str"),
                        ),
                    ),
                    image_id=dict(type="str"),
                ),
            ),
            is_agreement_acknowledged=dict(type="bool"),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            publication_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="publication",
        service_client_class=MarketplaceClient,
        namespace="marketplace",
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
