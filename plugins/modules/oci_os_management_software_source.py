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
module: oci_os_management_software_source
short_description: Manage a SoftwareSource resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a SoftwareSource resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new custom Software Source on the management system.
      This will not contain any packages after it is first created,
      and they must be added later.
    - "This resource has the following action operations in the M(oracle.oci.oci_os_management_software_source_actions) module: add_packages,
      change_compartment, remove_packages."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - OCID for the Compartment
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    arch_type:
        description:
            - The architecture type supported by the Software Source
            - Required for create using I(state=present).
        type: str
        choices:
            - "IA_32"
            - "X86_64"
            - "AARCH64"
            - "SPARC"
            - "AMD64_DEBIAN"
    parent_id:
        description:
            - OCID for the parent software source, if there is one
        type: str
    display_name:
        description:
            - User friendly name for the software source
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Information specified by the user about the software source
            - This parameter is updatable.
        type: str
    maintainer_name:
        description:
            - Name of the person maintaining this software source
            - This parameter is updatable.
        type: str
    maintainer_email:
        description:
            - Email address of the person maintaining this software source
            - This parameter is updatable.
        type: str
    maintainer_phone:
        description:
            - Phone number of the person maintaining this software source
            - This parameter is updatable.
        type: str
    checksum_type:
        description:
            - The yum repository checksum type used by this software source
            - This parameter is updatable.
        type: str
        choices:
            - "SHA1"
            - "SHA256"
            - "SHA384"
            - "SHA512"
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    software_source_id:
        description:
            - The OCID of the software source.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the SoftwareSource.
            - Use I(state=present) to create or update a SoftwareSource.
            - Use I(state=absent) to delete a SoftwareSource.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create software_source
  oci_os_management_software_source:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    arch_type: IA_32
    display_name: display_name_example

    # optional
    parent_id: "ocid1.parent.oc1..xxxxxxEXAMPLExxxxxx"
    description: description_example
    maintainer_name: maintainer_name_example
    maintainer_email: maintainer_email_example
    maintainer_phone: maintainer_phone_example
    checksum_type: SHA1
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update software_source
  oci_os_management_software_source:
    # required
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    maintainer_name: maintainer_name_example
    maintainer_email: maintainer_email_example
    maintainer_phone: maintainer_phone_example
    checksum_type: SHA1
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update software_source using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_software_source:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    maintainer_name: maintainer_name_example
    maintainer_email: maintainer_email_example
    maintainer_phone: maintainer_phone_example
    checksum_type: SHA1
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete software_source
  oci_os_management_software_source:
    # required
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete software_source using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_software_source:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
software_source:
    description:
        - Details of the SoftwareSource resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID for the Software Source
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - OCID for the Compartment
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User friendly name for the software source
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Information specified by the user about the software source
            returned: on success
            type: str
            sample: description_example
        repo_type:
            description:
                - Type of the Software Source
            returned: on success
            type: str
            sample: repo_type_example
        arch_type:
            description:
                - The architecture type supported by the Software Source
            returned: on success
            type: str
            sample: IA_32
        url:
            description:
                - URL for the repostiory
            returned: on success
            type: str
            sample: url_example
        parent_id:
            description:
                - OCID for the parent software source, if there is one
            returned: on success
            type: str
            sample: "ocid1.parent.oc1..xxxxxxEXAMPLExxxxxx"
        parent_name:
            description:
                - Display name the parent software source, if there is one
            returned: on success
            type: str
            sample: parent_name_example
        checksum_type:
            description:
                - The yum repository checksum type used by this software source
            returned: on success
            type: str
            sample: SHA1
        maintainer_name:
            description:
                - Name of the person maintaining this software source
            returned: on success
            type: str
            sample: maintainer_name_example
        maintainer_email:
            description:
                - Email address of the person maintaining this software source
            returned: on success
            type: str
            sample: maintainer_email_example
        maintainer_phone:
            description:
                - Phone number of the person maintaining this software source
            returned: on success
            type: str
            sample: maintainer_phone_example
        gpg_key_url:
            description:
                - URL of the GPG key for this software source
            returned: on success
            type: str
            sample: gpg_key_url_example
        gpg_key_id:
            description:
                - ID of the GPG key for this software source
            returned: on success
            type: str
            sample: "ocid1.gpgkey.oc1..xxxxxxEXAMPLExxxxxx"
        gpg_key_fingerprint:
            description:
                - Fingerprint of the GPG key for this software source
            returned: on success
            type: str
            sample: gpg_key_fingerprint_example
        status:
            description:
                - status of the software source.
            returned: on success
            type: str
            sample: NORMAL
        lifecycle_state:
            description:
                - The current state of the Software Source.
            returned: on success
            type: str
            sample: CREATING
        packages:
            description:
                - Number of packages
            returned: on success
            type: int
            sample: 56
        associated_managed_instances:
            description:
                - list of the Managed Instances associated with this Software Sources
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - unique identifier that is immutable on creation
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User friendly name
                    returned: on success
                    type: str
                    sample: display_name_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "repo_type": "repo_type_example",
        "arch_type": "IA_32",
        "url": "url_example",
        "parent_id": "ocid1.parent.oc1..xxxxxxEXAMPLExxxxxx",
        "parent_name": "parent_name_example",
        "checksum_type": "SHA1",
        "maintainer_name": "maintainer_name_example",
        "maintainer_email": "maintainer_email_example",
        "maintainer_phone": "maintainer_phone_example",
        "gpg_key_url": "gpg_key_url_example",
        "gpg_key_id": "ocid1.gpgkey.oc1..xxxxxxEXAMPLExxxxxx",
        "gpg_key_fingerprint": "gpg_key_fingerprint_example",
        "status": "NORMAL",
        "lifecycle_state": "CREATING",
        "packages": 56,
        "associated_managed_instances": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
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
    from oci.os_management import OsManagementClient
    from oci.os_management.models import CreateSoftwareSourceDetails
    from oci.os_management.models import UpdateSoftwareSourceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SoftwareSourceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(SoftwareSourceHelperGen, self).get_possible_entity_types() + [
            "softwaresource",
            "softwaresources",
            "osManagementsoftwaresource",
            "osManagementsoftwaresources",
            "softwaresourceresource",
            "softwaresourcesresource",
            "osmanagement",
        ]

    def get_module_resource_id_param(self):
        return "software_source_id"

    def get_module_resource_id(self):
        return self.module.params.get("software_source_id")

    def get_get_fn(self):
        return self.client.get_software_source

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_software_source, software_source_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_software_source,
            software_source_id=self.module.params.get("software_source_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_software_sources, **kwargs
        )

    def get_create_model_class(self):
        return CreateSoftwareSourceDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_software_source,
            call_fn_args=(),
            call_fn_kwargs=dict(create_software_source_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateSoftwareSourceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_software_source,
            call_fn_args=(),
            call_fn_kwargs=dict(
                software_source_id=self.module.params.get("software_source_id"),
                update_software_source_details=update_details,
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
            call_fn=self.client.delete_software_source,
            call_fn_args=(),
            call_fn_kwargs=dict(
                software_source_id=self.module.params.get("software_source_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


SoftwareSourceHelperCustom = get_custom_class("SoftwareSourceHelperCustom")


class ResourceHelper(SoftwareSourceHelperCustom, SoftwareSourceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            arch_type=dict(
                type="str",
                choices=["IA_32", "X86_64", "AARCH64", "SPARC", "AMD64_DEBIAN"],
            ),
            parent_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            maintainer_name=dict(type="str"),
            maintainer_email=dict(type="str"),
            maintainer_phone=dict(type="str"),
            checksum_type=dict(
                type="str", choices=["SHA1", "SHA256", "SHA384", "SHA512"]
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            software_source_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="software_source",
        service_client_class=OsManagementClient,
        namespace="os_management",
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
