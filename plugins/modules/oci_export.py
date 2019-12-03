#!/usr/bin/python
# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
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
module: oci_export
short_description: Create, update and delete a Export in OCI Filesystem Service.
description:
    - Create an OCI Export
    - Update an OCI Export, if present, with a new display name
    - Delete an OCI Export, if present.
version_added: "2.5"
options:
    export_set_id:
        description: Identifier of the export set of this Export. Mandatory for create operation.
        required: false
    file_system_id:
        description: Identifier of the file system of this Export. Mandatory for create operation.
        required: false
    export_id:
        description: Identifier of the existing Export which required to be updated, deleted.
                     Mandatory for update and delete.
        required: false
        aliases: ['id']
    export_options:
        description: Export options for this Export.
        required: false
        suboptions:
           source:
              description: Clients these options should apply to. Must be a either single IPv4 address or single
                           IPv4 CIDR block.
              required: true
           require_privileged_source_port:
              description: If true, clients accessing the file system through this export must connect from a
                           privileged source port. If unspecified, defaults to true.
              required: false
           access:
              description: Type of access to grant clients using the file system through this export.
                           If unspecified defaults to READ_ONLY. Allowed values are READ_WRITE and READ-ONLY.
              required: false
           identity_squash:
              description: Used when clients accessing the file system through this export have their UID and GID remapped
                           to 'anonymousUid' and 'anonymousGid'. If ALL, all users and groups are remapped; if ROOT, only the
                           root user and group (UID/GID 0) are remapped; if NONE, no remapping is done. If unspecified, defaults
                           to ROOT. Allowed values are NONE, ROOT and ALL.
              required: false
           anonymous_uid:
              description: UID value to remap to when squashing a client UID (see identitySquash for more details.) If unspecified,
                           defaults to 65534.
              required: false
           anonymous_gid:
              description: GID value to remap to when squashing a client GID (see identitySquash for more details.) If unspecified,
                           defaults to 65534.
              required: false
    purge_export_options:
        description: Purge any export options in the  Export that is not specified in I(export_options).
                     If I(purge_export_options=no), provided export options would be appended to existing
                     export options. I(purge_export_options) and I(delete_export_options) are
                     mutually exclusive.
        required: false
        default: 'yes'
        type: bool
    delete_export_options:
        description: Delete any export options in the Export that is specified in I(export_options).
                     If I(delete_export_options=yes), export options provided by I(export_options)
                     would be deleted from existing export options, if they are part of existing export
                     options. If they are not part of existing export options, they will be ignored.
                     I(delete_export_options) and I(purge_export_options) are mutually exclusive.
        required: false
        default: 'no'
        type: bool
    path:
        description: Path used to access the associated file system. Avoid entering confidential information. Mandatory for create operation.
        required: false
    state:
        description: Create, update and delete Export. For I(state=present), if it does not exist, it gets created.
                     If it exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create Export
- name: Create Export
  oci_export:
    file_system_id: 'ocid1.filesystem.oc1..xxxxxEXAMPLExxxxx'
    export_set_id: 'ocid1.exportset.oc1..xxxxxEXAMPLExxxxx'
    export_options:
          - source: '10.0.0.0/16'
            require_privileged_source_port: False
            access: 'READ_WRITE'
            identity_squash: 'NONE'
    path: '/ansibletestpath'
    state: 'present'

# Update Export's Export Options
- name: Update Export's Export Options
  oci_export:
    export_id: 'ocid1.export.oc1..xxxxxEXAMPLExxxxx'
    export_options:
          - source: '10.0.0.0/16'
            require_privileged_source_port: False
            access: 'READ_ONLY'
            identity_squash: 'ROOT'
    state: 'present'

# Update Export's Export Options by appending a new Export Options
- name: Update Export's Export Options by appending a new Export Options
  oci_export:
    export_id: 'ocid1.export.oc1..xxxxxEXAMPLExxxxx'
    export_options:
          - source: '10.0.0.100'
            require_privileged_source_port: False
            access: 'READ_ONLY'
            identity_squash: 'ALL'
    purge_export_options: False
    state: 'present'

# Update Export's Export Options by deleting an Export Options
- name: Update Export's Export Options by deleting an Export Options
  oci_export:
    export_id: 'ocid1.export.oc1..xxxxxEXAMPLExxxxx'
    export_options:
          - source: '10.0.0.100'
            require_privileged_source_port: False
            access: 'READ_ONLY'
            identity_squash: 'ALL'
    delete_export_options: True
    state: 'present'

# Delete Export
- name: Delete Export
  oci_export:
    id: 'ocid1.export.oc1..xxxxxEXAMPLExxxxx'
    state: 'absent'
"""

RETURN = """
    export:
        description: Attributes of the created/updated Export. For delete, deleted Export
                     description will be returned.
        returned: success
        type: complex
        contains:
            export_options:
                description: Policies that apply to NFS requests made through this export.
                returned: always
                type: list
                sample: [{"access": "READ_WRITE", "anonymous_gid": 65534, "anonymous_uid": 65534,
                          "identity_squash": "NONE", "require_privileged_source_port": false,
                          "source": "0.0.0.0/0"}]
            export_set_id:
                description: Identifier of the export set of this Export.
                returned: always
                type: string
                sample: ocid1.exportset.oc1.xzvf..xxxxxEXAMPLExxxxx
            file_system_id:
                description: Identifier of the file system of this Export.
                returned: always
                type: string
                sample: ocid1.filesystem.oc1.xzvf..xxxxxEXAMPLExxxxx
            id:
                description: The identifier of the Export
                returned: always
                type: string
                sample: ocid1.export.oc1.xzvf..xxxxxEXAMPLExxxxx
            lifecycle_state:
                description: The current state of the Export
                returned: always
                type: string
                sample: ACTIVE
            path:
                description: Path used to access the associated file system.
                returned: always
                type: string
                sample: /ansibletestpath
            time_created:
                description: Date and time when the Export was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2018-10-18T11:40:52.483000+00:00

        sample: {
                  "export_options":[
                                    {
                                      "access":"READ_WRITE",
                                      "anonymous_gid":65534,
                                      "anonymous_uid":65534,
                                      "identity_squash":"NONE",
                                      "require_privileged_source_port":false,
                                      "source":"10.0.0.10"
                                    },
                                    {
                                      "access":"READ_ONLY",
                                      "anonymous_gid":65534,
                                      "anonymous_uid":65534,
                                      "identity_squash":"ROOT",
                                      "require_privileged_source_port":true,
                                      "source":"10.0.2.0/24"
                                    }
                                   ],
                  "export_set_id":"ocid1.exportset.oc1.iad.xxxxxEXAMPLExxxxx",
                  "file_system_id":"ocid1.filesystem.oc1.iad.xxxxxEXAMPLExxxxx",
                  "id":"ocid1.export.oc1.iad.xxxxxEXAMPLExxxxx",
                  "lifecycle_state":"ACTIVE",
                  "path":"/ansibletestpath",
                  "time_created":"2018-10-18T11:40:52.483000+00:00"
                }


"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.file_storage.file_storage_client import FileStorageClient
    from oci.exceptions import ServiceError, ClientError
    from oci.util import to_dict
    from oci.file_storage.models import (
        CreateExportDetails,
        UpdateExportDetails,
        ClientOptions,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_or_update_export(file_storage_client, module):
    result = dict(changed=False, export="")
    export_id = module.params.get("export_id")
    try:
        if export_id:
            export = oci_utils.get_existing_resource(
                file_storage_client.get_export, module, export_id=export_id
            )
            result = update_export(file_storage_client, module, export)
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="export",
                create_fn=create_export,
                kwargs_create={
                    "file_storage_client": file_storage_client,
                    "module": module,
                },
                list_fn=file_storage_client.list_exports,
                kwargs_list={"file_system_id": module.params.get("file_system_id")},
                module=module,
                model=CreateExportDetails(),
            )
    except ServiceError as ex:
        get_logger().error("Unable to create/update Export due to: %s", ex.message)
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error("Unable to launch/update Export due to: %s", str(ex))
        module.fail_json(msg=str(ex))

    return result


def create_export(file_storage_client, module):
    create_export_details = CreateExportDetails()
    for attribute in create_export_details.attribute_map:
        create_export_details.__setattr__(attribute, module.params.get(attribute))
    create_export_details.export_options = get_export_options(
        module.params.get("export_options", None)
    )
    result = oci_utils.create_and_wait(
        resource_type="export",
        create_fn=file_storage_client.create_export,
        kwargs_create={"create_export_details": create_export_details},
        client=file_storage_client,
        get_fn=file_storage_client.get_export,
        get_param="export_id",
        module=module,
    )
    return result


def get_export_options(export_options):
    if export_options is None:
        return None
    HashedClientOptions = oci_utils.generate_subclass(ClientOptions)
    result_client_options = []
    for export_option_entry in export_options:
        client_options = HashedClientOptions()
        if export_option_entry.get("source") is None:
            raise ClientError(
                "Export Options attribute source must contain a valid value"
            )
        client_options.source = export_option_entry.get("source")
        client_options.require_privileged_source_port = export_option_entry.get(
            "require_privileged_source_port", True
        )
        client_options.access = export_option_entry.get("access", "READ_ONLY")
        client_options.identity_squash = export_option_entry.get(
            "identity_squash", "ROOT"
        )
        client_options.anonymous_uid = export_option_entry.get("anonymous_uid", 65534)
        client_options.anonymous_gid = export_option_entry.get("anonymous_gid", 65534)
        result_client_options.append(client_options)
    return result_client_options


def update_export(file_storage_client, module, export):
    result = dict(export=to_dict(export), changed=False)
    update_export_details = UpdateExportDetails()
    purge_export_options = module.params.get("purge_export_options")
    delete_export_options = module.params.get("delete_export_options")
    input_export_options = get_export_options(module.params.get("export_options", None))
    existing_export_options = oci_utils.get_hashed_object_list(
        ClientOptions, export.export_options
    )
    export_option_changed = False
    if input_export_options is not None:
        export_options, export_option_changed = oci_utils.check_and_return_component_list_difference(
            input_export_options,
            existing_export_options,
            purge_export_options,
            delete_export_options,
        )
    if export_option_changed:
        update_export_details.export_options = export_options
    else:
        update_export_details.export_options = existing_export_options
    if export_option_changed:
        result = oci_utils.update_and_wait(
            resource_type="export",
            update_fn=file_storage_client.update_export,
            kwargs_update={
                "export_id": export.id,
                "update_export_details": update_export_details,
            },
            client=file_storage_client,
            get_fn=file_storage_client.get_export,
            get_param="export_id",
            module=module,
        )
    return result


def delete_export(file_storage_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="export",
        client=file_storage_client,
        get_fn=file_storage_client.get_export,
        kwargs_get={"export_id": module.params["export_id"]},
        delete_fn=file_storage_client.delete_export,
        kwargs_delete={"export_id": module.params["export_id"]},
        module=module,
    )

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_export")
    set_logger(logger)

    module_args = oci_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            export_options=dict(type=list, required=False),
            export_set_id=dict(type="str", required=False),
            file_system_id=dict(type="str", required=False),
            export_id=dict(type="str", required=False, aliases=["id"]),
            path=dict(type="str", required=False),
            purge_export_options=dict(type="bool", required=False, default=True),
            delete_export_options=dict(type="bool", required=False, default=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["purge_export_options", "delete_export_options"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    file_storage_client = oci_utils.create_service_client(module, FileStorageClient)
    state = module.params["state"]

    if state == "present":
        result = create_or_update_export(file_storage_client, module)
    elif state == "absent":
        result = delete_export(file_storage_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
