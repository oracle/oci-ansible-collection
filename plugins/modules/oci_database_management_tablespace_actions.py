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
module: oci_database_management_tablespace_actions
short_description: Perform actions on a Tablespace resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Tablespace resource in Oracle Cloud Infrastructure
    - For I(action=add_data_files), adds data files or temp files to the tablespace.
    - For I(action=drop), drops the tablespace specified by tablespaceName within the Managed Database specified by managedDatabaseId.
    - For I(action=remove_data_file), removes a data file or temp file from the tablespace.
    - For I(action=resize_data_file), resizes a data file or temp file within the tablespace.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    data_files:
        description:
            - The list of data files or temp files added to the tablespace.
            - Applicable only for I(action=add_data_files).
        type: list
        elements: str
    file_count:
        description:
            - The number of data files or temp files to be added for the tablespace. This is for Oracle Managed Files only.
            - Applicable only for I(action=add_data_files).
        type: int
    is_reusable:
        description:
            - Specifies whether Oracle can reuse the data file or temp file. Reuse is only allowed when the file name is provided.
            - Applicable only for I(action=add_data_files).
        type: bool
    is_including_contents:
        description:
            - Specifies whether all the contents of the tablespace being dropped should be dropped.
            - Applicable only for I(action=drop).
        type: bool
    is_dropping_data_files:
        description:
            - Specifies whether all the associated data files of the tablespace being dropped should be dropped.
            - Applicable only for I(action=drop).
        type: bool
    is_cascade_constraints:
        description:
            - Specifies whether all the constraints on the tablespace being dropped should be dropped.
            - Applicable only for I(action=drop).
        type: bool
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    tablespace_name:
        description:
            - The name of the tablespace.
        type: str
        required: true
    credential_details:
        description:
            - ""
        type: dict
        required: true
        suboptions:
            password:
                description:
                    - The database user's password encoded using BASE64 scheme.
                    - Required when tablespace_admin_credential_type is 'PASSWORD'
                type: str
            tablespace_admin_credential_type:
                description:
                    - The type of the credential for tablespace administration tasks.
                type: str
                choices:
                    - "PASSWORD"
                    - "SECRET"
                required: true
            username:
                description:
                    - The user to connect to the database.
                type: str
                required: true
            role:
                description:
                    - The role of the database user.
                type: str
                choices:
                    - "NORMAL"
                    - "SYSDBA"
                required: true
            password_secret_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Secret
                      where the database password is stored.
                    - Required when tablespace_admin_credential_type is 'SECRET'
                type: str
    file_type:
        description:
            - Specifies whether the file is a data file or temp file.
            - Required for I(action=add_data_files), I(action=remove_data_file), I(action=resize_data_file).
        type: str
        choices:
            - "DATAFILE"
            - "TEMPFILE"
    data_file:
        description:
            - Name of the data file or temp file to be removed from the tablespace.
            - Required for I(action=remove_data_file), I(action=resize_data_file).
        type: str
    file_size:
        description:
            - The size of each data file or temp file.
            - Applicable only for I(action=add_data_files)I(action=resize_data_file).
        type: dict
        suboptions:
            size:
                description:
                    - Storage size number in bytes, kilobytes, megabytes, gigabytes, or terabytes.
                type: float
                required: true
            unit:
                description:
                    - "Storage size unit: bytes, kilobytes, megabytes, gigabytes, or terabytes."
                type: str
                choices:
                    - "BYTES"
                    - "KILOBYTES"
                    - "MEGABYTES"
                    - "GIGABYTES"
                    - "TERABYTES"
    is_auto_extensible:
        description:
            - Specifies whether the data file or temp file can be extended automatically.
            - Applicable only for I(action=add_data_files)I(action=resize_data_file).
        type: bool
    auto_extend_next_size:
        description:
            - The size of the next increment of disk space to be allocated automatically when more extents are required.
            - Applicable only for I(action=add_data_files)I(action=resize_data_file).
        type: dict
        suboptions:
            size:
                description:
                    - Storage size number in bytes, kilobytes, megabytes, gigabytes, or terabytes.
                type: float
                required: true
            unit:
                description:
                    - "Storage size unit: bytes, kilobytes, megabytes, gigabytes, or terabytes."
                type: str
                choices:
                    - "BYTES"
                    - "KILOBYTES"
                    - "MEGABYTES"
                    - "GIGABYTES"
                    - "TERABYTES"
    auto_extend_max_size:
        description:
            - The maximum disk space allowed for automatic extension of the data files or temp files.
            - Applicable only for I(action=add_data_files)I(action=resize_data_file).
        type: dict
        suboptions:
            size:
                description:
                    - Storage size number in bytes, kilobytes, megabytes, gigabytes, or terabytes.
                type: float
                required: true
            unit:
                description:
                    - "Storage size unit: bytes, kilobytes, megabytes, gigabytes, or terabytes."
                type: str
                choices:
                    - "BYTES"
                    - "KILOBYTES"
                    - "MEGABYTES"
                    - "GIGABYTES"
                    - "TERABYTES"
    is_max_size_unlimited:
        description:
            - Specifies whether the disk space of the data file or temp file can be limited.
            - Applicable only for I(action=add_data_files)I(action=resize_data_file).
        type: bool
    action:
        description:
            - The action to perform on the Tablespace.
        type: str
        required: true
        choices:
            - "add_data_files"
            - "drop"
            - "remove_data_file"
            - "resize_data_file"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action add_data_files on tablespace
  oci_database_management_tablespace_actions:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    tablespace_name: tablespace_name_example
    credential_details:
      # required
      password: example-password
      tablespace_admin_credential_type: PASSWORD
      username: username_example
      role: NORMAL
    file_type: DATAFILE
    action: add_data_files

    # optional
    data_files: [ "data_files_example" ]
    file_count: 56
    is_reusable: true
    file_size:
      # required
      size: 3.4

      # optional
      unit: BYTES
    is_auto_extensible: true
    auto_extend_next_size:
      # required
      size: 3.4

      # optional
      unit: BYTES
    auto_extend_max_size:
      # required
      size: 3.4

      # optional
      unit: BYTES
    is_max_size_unlimited: true

- name: Perform action drop on tablespace
  oci_database_management_tablespace_actions:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    tablespace_name: tablespace_name_example
    credential_details:
      # required
      password: example-password
      tablespace_admin_credential_type: PASSWORD
      username: username_example
      role: NORMAL
    action: drop

    # optional
    is_including_contents: true
    is_dropping_data_files: true
    is_cascade_constraints: true

- name: Perform action remove_data_file on tablespace
  oci_database_management_tablespace_actions:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    tablespace_name: tablespace_name_example
    credential_details:
      # required
      password: example-password
      tablespace_admin_credential_type: PASSWORD
      username: username_example
      role: NORMAL
    file_type: DATAFILE
    data_file: data_file_example
    action: remove_data_file

- name: Perform action resize_data_file on tablespace
  oci_database_management_tablespace_actions:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    tablespace_name: tablespace_name_example
    credential_details:
      # required
      password: example-password
      tablespace_admin_credential_type: PASSWORD
      username: username_example
      role: NORMAL
    file_type: DATAFILE
    data_file: data_file_example
    action: resize_data_file

    # optional
    file_size:
      # required
      size: 3.4

      # optional
      unit: BYTES
    is_auto_extensible: true
    auto_extend_next_size:
      # required
      size: 3.4

      # optional
      unit: BYTES
    auto_extend_max_size:
      # required
      size: 3.4

      # optional
      unit: BYTES
    is_max_size_unlimited: true

"""

RETURN = """
tablespace_admin_status:
    description:
        - Details of the Tablespace resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        status:
            description:
                - The status of a tablespace admin action.
            returned: on success
            type: str
            sample: SUCCEEDED
        error_code:
            description:
                - "The error code that denotes failure if the tablespace admin action is not successful. The error code is \\"null\\" if the admin action is
                  successful."
            returned: on success
            type: int
            sample: 56
        error_message:
            description:
                - "The error message that indicates the reason for failure if the tablespace admin action is not successful. The error message is \\"null\\" if
                  the admin action is successful."
            returned: on success
            type: str
            sample: error_message_example
    sample: {
        "status": "SUCCEEDED",
        "error_code": 56,
        "error_message": "error_message_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient
    from oci.database_management.models import AddDataFilesDetails
    from oci.database_management.models import DropTablespaceDetails
    from oci.database_management.models import RemoveDataFileDetails
    from oci.database_management.models import ResizeDataFileDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TablespaceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_data_files
        drop
        remove_data_file
        resize_data_file
    """

    @staticmethod
    def get_module_resource_id_param():
        return "tablespace_name"

    def get_module_resource_id(self):
        return self.module.params.get("tablespace_name")

    def get_get_fn(self):
        return self.client.get_tablespace

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tablespace,
            managed_database_id=self.module.params.get("managed_database_id"),
            tablespace_name=self.module.params.get("tablespace_name"),
        )

    def get_response_field_name(self, action):
        response_fields = dict(
            add_data_files="tablespace_admin_status",
            drop="tablespace_admin_status",
            remove_data_file="tablespace_admin_status",
            resize_data_file="tablespace_admin_status",
        )
        return response_fields.get(action, "tablespace")

    def add_data_files(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddDataFilesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_data_files,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                tablespace_name=self.module.params.get("tablespace_name"),
                add_data_files_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def drop(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DropTablespaceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.drop_tablespace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                tablespace_name=self.module.params.get("tablespace_name"),
                drop_tablespace_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def remove_data_file(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveDataFileDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_data_file,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                tablespace_name=self.module.params.get("tablespace_name"),
                remove_data_file_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def resize_data_file(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ResizeDataFileDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.resize_data_file,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                tablespace_name=self.module.params.get("tablespace_name"),
                resize_data_file_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


TablespaceActionsHelperCustom = get_custom_class("TablespaceActionsHelperCustom")


class ResourceHelper(TablespaceActionsHelperCustom, TablespaceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            data_files=dict(type="list", elements="str"),
            file_count=dict(type="int"),
            is_reusable=dict(type="bool"),
            is_including_contents=dict(type="bool"),
            is_dropping_data_files=dict(type="bool"),
            is_cascade_constraints=dict(type="bool"),
            managed_database_id=dict(type="str", required=True),
            tablespace_name=dict(type="str", required=True),
            credential_details=dict(
                type="dict",
                required=True,
                options=dict(
                    password=dict(type="str", no_log=True),
                    tablespace_admin_credential_type=dict(
                        type="str", required=True, choices=["PASSWORD", "SECRET"]
                    ),
                    username=dict(type="str", required=True),
                    role=dict(type="str", required=True, choices=["NORMAL", "SYSDBA"]),
                    password_secret_id=dict(type="str"),
                ),
            ),
            file_type=dict(type="str", choices=["DATAFILE", "TEMPFILE"]),
            data_file=dict(type="str"),
            file_size=dict(
                type="dict",
                options=dict(
                    size=dict(type="float", required=True),
                    unit=dict(
                        type="str",
                        choices=[
                            "BYTES",
                            "KILOBYTES",
                            "MEGABYTES",
                            "GIGABYTES",
                            "TERABYTES",
                        ],
                    ),
                ),
            ),
            is_auto_extensible=dict(type="bool"),
            auto_extend_next_size=dict(
                type="dict",
                options=dict(
                    size=dict(type="float", required=True),
                    unit=dict(
                        type="str",
                        choices=[
                            "BYTES",
                            "KILOBYTES",
                            "MEGABYTES",
                            "GIGABYTES",
                            "TERABYTES",
                        ],
                    ),
                ),
            ),
            auto_extend_max_size=dict(
                type="dict",
                options=dict(
                    size=dict(type="float", required=True),
                    unit=dict(
                        type="str",
                        choices=[
                            "BYTES",
                            "KILOBYTES",
                            "MEGABYTES",
                            "GIGABYTES",
                            "TERABYTES",
                        ],
                    ),
                ),
            ),
            is_max_size_unlimited=dict(type="bool"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_data_files",
                    "drop",
                    "remove_data_file",
                    "resize_data_file",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="tablespace",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
