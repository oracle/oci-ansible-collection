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
module: oci_file_storage_export
short_description: Manage an Export resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an Export resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new export in the specified export set, path, and
      file system.
version_added: "2.9"
author: Oracle (@oracle)
options:
    export_options:
        description:
            - "Export options for the new export. If left unspecified,
              defaults to:"
            - |
              "      [
                       {
                          \\"source\\" : \\"0.0.0.0/0\\",
                          \\"requirePrivilegedSourcePort\\" : false,
                          \\"access\\" : \\"READ_WRITE\\",
                          \\"identitySquash\\" : \\"NONE\\"
                        }
                     ]"
            - " **Note:** Mount targets do not have Internet-routable IP
                addresses.  Therefore they will not be reachable from the
                Internet, even if an associated `ClientOptions` item has
                a source of `0.0.0.0/0`."
            - " **If set to the empty array then the export will not be
                visible to any clients.**"
            -   The export's `exportOptions` can be changed after creation
                using the `UpdateExport` operation.
            - This parameter is updatable.
        type: list
        suboptions:
            source:
                description:
                    - Clients these options should apply to. Must be a either
                      single IPv4 address or single IPv4 CIDR block.
                    - "**Note:** Access will also be limited by any applicable VCN
                      security rules and the ability to route IP packets to the
                      mount target. Mount targets do not have Internet-routable IP addresses."
                type: str
                required: true
            require_privileged_source_port:
                description:
                    - If `true`, clients accessing the file system through this
                      export must connect from a privileged source port. If
                      unspecified, defaults to `true`.
                type: bool
            access:
                description:
                    - Type of access to grant clients using the file system
                      through this export. If unspecified defaults to `READ_ONLY`.
                type: str
                choices:
                    - "READ_WRITE"
                    - "READ_ONLY"
            identity_squash:
                description:
                    - Used when clients accessing the file system through this export
                      have their UID and GID remapped to 'anonymousUid' and
                      'anonymousGid'. If `ALL`, all users and groups are remapped;
                      if `ROOT`, only the root user and group (UID/GID 0) are
                      remapped; if `NONE`, no remapping is done. If unspecified,
                      defaults to `ROOT`.
                type: str
                choices:
                    - "NONE"
                    - "ROOT"
                    - "ALL"
            anonymous_uid:
                description:
                    - UID value to remap to when squashing a client UID (see
                      identitySquash for more details.) If unspecified, defaults
                      to `65534`.
                type: int
            anonymous_gid:
                description:
                    - GID value to remap to when squashing a client GID (see
                      identitySquash for more details.) If unspecified defaults
                      to `65534`.
                type: int
    export_set_id:
        description:
            - The OCID of this export's export set.
            - Required for create using I(state=present).
        type: str
    file_system_id:
        description:
            - The OCID of this export's file system.
            - Required for create using I(state=present).
        type: str
    path:
        description:
            - Path used to access the associated file system.
            - Avoid entering confidential information.
            - "Example: `/mediafiles`"
            - Required for create using I(state=present).
        type: str
    export_id:
        description:
            - The OCID of the export.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Export.
            - Use I(state=present) to create or update an Export.
            - Use I(state=absent) to delete an Export.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create export
  oci_file_storage_export:
    export_set_id: ocid1.exportset.oc1.phx.exampleaaaaacvbobuhqllhmfwwcotqnb4c2ylefuzaaaaa
    file_system_id: ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx
    path: /mediafiles

- name: Update export
  oci_file_storage_export:
    export_options:
    - source: source_example
    export_id: ocid1.export.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete export
  oci_file_storage_export:
    export_id: ocid1.export.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
export:
    description:
        - Details of the Export resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        export_options:
            description:
                - Policies that apply to NFS requests made through this
                  export. `exportOptions` contains a sequential list of
                  `ClientOptions`. Each `ClientOptions` item defines the
                  export options that are applied to a specified
                  set of clients.
                - For each NFS request, the first `ClientOptions` option
                  in the list whose `source` attribute matches the source
                  IP address of the request is applied.
                - If a client source IP address does not match the `source`
                  property of any `ClientOptions` in the list, then the
                  export will be invisible to that client. This export will
                  not be returned by `MOUNTPROC_EXPORT` calls made by the client
                  and any attempt to mount or access the file system through
                  this export will result in an error.
                - "**Exports without defined `ClientOptions` are invisible to all clients.**"
                - If one export is invisible to a particular client, associated file
                  systems may still be accessible through other exports on the same
                  or different mount targets.
                  To completely deny client access to a file system, be sure that the client
                  source IP address is not included in any export for any mount target
                  associated with the file system.
            returned: on success
            type: complex
            contains:
                source:
                    description:
                        - Clients these options should apply to. Must be a either
                          single IPv4 address or single IPv4 CIDR block.
                        - "**Note:** Access will also be limited by any applicable VCN
                          security rules and the ability to route IP packets to the
                          mount target. Mount targets do not have Internet-routable IP addresses."
                    returned: on success
                    type: string
                    sample: source_example
                require_privileged_source_port:
                    description:
                        - If `true`, clients accessing the file system through this
                          export must connect from a privileged source port. If
                          unspecified, defaults to `true`.
                    returned: on success
                    type: bool
                    sample: true
                access:
                    description:
                        - Type of access to grant clients using the file system
                          through this export. If unspecified defaults to `READ_ONLY`.
                    returned: on success
                    type: string
                    sample: READ_WRITE
                identity_squash:
                    description:
                        - Used when clients accessing the file system through this export
                          have their UID and GID remapped to 'anonymousUid' and
                          'anonymousGid'. If `ALL`, all users and groups are remapped;
                          if `ROOT`, only the root user and group (UID/GID 0) are
                          remapped; if `NONE`, no remapping is done. If unspecified,
                          defaults to `ROOT`.
                    returned: on success
                    type: string
                    sample: NONE
                anonymous_uid:
                    description:
                        - UID value to remap to when squashing a client UID (see
                          identitySquash for more details.) If unspecified, defaults
                          to `65534`.
                    returned: on success
                    type: int
                    sample: 56
                anonymous_gid:
                    description:
                        - GID value to remap to when squashing a client GID (see
                          identitySquash for more details.) If unspecified defaults
                          to `65534`.
                    returned: on success
                    type: int
                    sample: 56
        export_set_id:
            description:
                - The OCID of this export's export set.
            returned: on success
            type: string
            sample: ocid1.exportset.oc1..xxxxxxEXAMPLExxxxxx
        file_system_id:
            description:
                - The OCID of this export's file system.
            returned: on success
            type: string
            sample: ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx
        id:
            description:
                - The OCID of this export.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of this export.
            returned: on success
            type: string
            sample: CREATING
        path:
            description:
                - Path used to access the associated file system.
                - Avoid entering confidential information.
                - "Example: `/accounting`"
            returned: on success
            type: string
            sample: /accounting
        time_created:
            description:
                - The date and time the export was created, expressed
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: {
        "export_options": [{
            "source": "source_example",
            "require_privileged_source_port": true,
            "access": "READ_WRITE",
            "identity_squash": "NONE",
            "anonymous_uid": 56,
            "anonymous_gid": 56
        }],
        "export_set_id": "ocid1.exportset.oc1..xxxxxxEXAMPLExxxxxx",
        "file_system_id": "ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "path": "/accounting",
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
    from oci.file_storage import FileStorageClient
    from oci.file_storage.models import CreateExportDetails
    from oci.file_storage.models import UpdateExportDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExportHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "export_id"

    def get_module_resource_id(self):
        return self.module.params.get("export_id")

    def get_get_fn(self):
        return self.client.get_export

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_export, export_id=self.module.params.get("export_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["export_set_id", "file_system_id"]

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
        return oci_common_utils.list_all_resources(self.client.list_exports, **kwargs)

    def get_create_model_class(self):
        return CreateExportDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_export,
            call_fn_args=(),
            call_fn_kwargs=dict(create_export_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateExportDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_export,
            call_fn_args=(),
            call_fn_kwargs=dict(
                export_id=self.module.params.get("export_id"),
                update_export_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_export,
            call_fn_args=(),
            call_fn_kwargs=dict(export_id=self.module.params.get("export_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


ExportHelperCustom = get_custom_class("ExportHelperCustom")


class ResourceHelper(ExportHelperCustom, ExportHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            export_options=dict(
                type="list",
                elements="dict",
                options=dict(
                    source=dict(type="str", required=True),
                    require_privileged_source_port=dict(type="bool"),
                    access=dict(type="str", choices=["READ_WRITE", "READ_ONLY"]),
                    identity_squash=dict(type="str", choices=["NONE", "ROOT", "ALL"]),
                    anonymous_uid=dict(type="int"),
                    anonymous_gid=dict(type="int"),
                ),
            ),
            export_set_id=dict(type="str"),
            file_system_id=dict(type="str"),
            path=dict(type="str"),
            export_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="export",
        service_client_class=FileStorageClient,
        namespace="file_storage",
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
