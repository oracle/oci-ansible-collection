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
module: oci_file_storage_file_system
short_description: Manage a FileSystem resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a FileSystem resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new file system in the specified compartment and
      availability domain. Instances can mount file systems in
      another availability domain, but doing so might increase
      latency when compared to mounting instances in the same
      availability domain.
    - After you create a file system, you can associate it with a mount
      target. Instances can then mount the file system by connecting to the
      mount target's IP address. You can associate a file system with
      more than one mount target at a time.
    - For information about access control and compartments, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm).
    - For information about availability domains, see L(Regions and
      Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm).
      To get a list of availability domains, use the
      `ListAvailabilityDomains` operation in the Identity and Access
      Management Service API.
    - All Oracle Cloud Infrastructure resources, including
      file systems, get an Oracle-assigned, unique ID called an Oracle
      Cloud Identifier (OCID).  When you create a resource, you can
      find its OCID in the response. You can also retrieve a
      resource's OCID by using a List API operation on that resource
      type or by viewing the resource in the Console.
version_added: "2.9"
author: Oracle (@oracle)
options:
    availability_domain:
        description:
            - The availability domain to create the file system in.
            - "Example: `Uocm:PHX-AD-1`"
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment to create the file system in.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - A user-friendly name. It does not have to be unique, and it is changeable.
              Avoid entering confidential information.
            - "Example: `My file system`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair
               with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    file_system_id:
        description:
            - The OCID of the file system.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the FileSystem.
            - Use I(state=present) to create or update a FileSystem.
            - Use I(state=absent) to delete a FileSystem.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create file_system
  oci_file_storage_file_system:
    availability_domain: Uocm:PHX-AD-1
    compartment_id: ocid1.compartment.oc1..examplea4ssrz2joq66nyomcvb4ydlbfmn2qg7wow5neo2ytcdznohhsyca
    display_name: media-files-1

- name: Update file_system using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_file_storage_file_system:
    availability_domain: Uocm:PHX-AD-1
    compartment_id: ocid1.compartment.oc1..examplea4ssrz2joq66nyomcvb4ydlbfmn2qg7wow5neo2ytcdznohhsyca
    display_name: media-files-1
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update file_system
  oci_file_storage_file_system:
    display_name: media-files-1
    freeform_tags: {'Department': 'Finance'}
    file_system_id: ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete file_system
  oci_file_storage_file_system:
    file_system_id: ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete file_system using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_file_storage_file_system:
    availability_domain: Uocm:PHX-AD-1
    compartment_id: ocid1.compartment.oc1..examplea4ssrz2joq66nyomcvb4ydlbfmn2qg7wow5neo2ytcdznohhsyca
    display_name: media-files-1
    state: absent

"""

RETURN = """
file_system:
    description:
        - Details of the FileSystem resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain the file system is in. May be unset
                  as a blank or NULL value.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        metered_bytes:
            description:
                - The number of bytes consumed by the file system, including
                  any snapshots. This number reflects the metered size of the file
                  system and is updated asynchronously with respect to
                  updates to the file system.
            returned: on success
            type: int
            sample: 56
        compartment_id:
            description:
                - The OCID of the compartment that contains the file system.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
                - "Example: `My file system`"
            returned: on success
            type: string
            sample: My file system
        id:
            description:
                - The OCID of the file system.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of the file system.
            returned: on success
            type: string
            sample: CREATING
        time_created:
            description:
                - The date and time the file system was created, expressed in
                  L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair
                   with no predefined name, type, or namespace.
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
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "metered_bytes": 56,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "My file system",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2016-08-25T21:10:29.600Z",
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
    from oci.file_storage import FileStorageClient
    from oci.file_storage.models import CreateFileSystemDetails
    from oci.file_storage.models import UpdateFileSystemDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FileSystemHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "file_system_id"

    def get_module_resource_id(self):
        return self.module.params.get("file_system_id")

    def get_get_fn(self):
        return self.client.get_file_system

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_file_system,
            file_system_id=self.module.params.get("file_system_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "availability_domain",
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
            self.client.list_file_systems, **kwargs
        )

    def get_create_model_class(self):
        return CreateFileSystemDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_file_system,
            call_fn_args=(),
            call_fn_kwargs=dict(create_file_system_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateFileSystemDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_file_system,
            call_fn_args=(),
            call_fn_kwargs=dict(
                file_system_id=self.module.params.get("file_system_id"),
                update_file_system_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_file_system,
            call_fn_args=(),
            call_fn_kwargs=dict(
                file_system_id=self.module.params.get("file_system_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


FileSystemHelperCustom = get_custom_class("FileSystemHelperCustom")


class ResourceHelper(FileSystemHelperCustom, FileSystemHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            availability_domain=dict(type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            file_system_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="file_system",
        service_client_class=FileStorageClient,
        namespace="file_storage",
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
