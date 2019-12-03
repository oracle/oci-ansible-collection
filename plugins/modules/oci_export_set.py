#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
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
module: oci_export_set
short_description: Update a Export Set in OCI Filesystem Service.
description:
    - Update an OCI Export Set, if present, with a new display name
    - Update an OCI Export Set, if present, with new max_fs_stat_bytes
    - Update an OCI Export Set, if present, with new max_fs_stat_files
version_added: "2.5"
options:
    export_set_id:
        description: Identifier of the existing Export Set which required to be updated.
        required: false
        aliases: ['id']
    display_name:
        description: A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential
                     information.
        required: false
    max_fs_stat_bytes:
        description: Controls the maximum tbytes, fbytes, and abytes values reported by NFS FSSTAT calls through any associated
                     mount targets. This is an advanced feature. For most applications, use the default value. The tbytes value
                     reported by FSSTAT will be max_fs_stat_bytes. The value of fbytes and abytes will be max_fs_stat_bytes minus the
                     metered size of the file system. If the metered size is larger than max_fs_stat_bytes, then fbytes and abytes
                     will both be '0'.
        required: false
    max_fs_stat_files:
        description: Controls the maximum ffiles, ffiles, and afiles values reported by NFS FSSTAT calls through any associated
                     mount targets. This is an advanced feature. For most applications, use the default value. The tfiles value
                     reported by FSSTAT will be max_fs_stat_files. The value of ffiles and afiles will be max_fs_stat_files minus the
                     metered size of the file system. If the metered size is larger than max_fs_stat_files, then ffiles and afiles
                     will both be '0'.
        required: false
    state:
        description: Update Export Set. For I(state=present), it gets updated.
        required: false
        default: 'present'
        choices: ['present']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_wait_options ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.

# Update Export Set's display name
- name: Update Export Set's display name
  oci_export_set:
    export_set_id: 'ocid1.exportset.oc1..xxxxxEXAMPLExxxxx'
    display_name: 'updated_ansible_export_set'
    state: 'present'

# Update Export Set's max_fs_stat_bytes
- name: Update Export Set's max_fs_stat_bytes
  oci_export_set:
    export_set_id: 'ocid1.exportset.oc1..xxxxxEXAMPLExxxxx'
    max_fs_stat_bytes: 9223372036854775806
    state: 'present'

# Update Export Set's max_fs_stat_files
- name: Update Export Set's max_fs_stat_files
  oci_export_set:
    export_set_id: 'ocid1.exportset.oc1..xxxxxEXAMPLExxxxx'
    max_fs_stat_files: 9223372036854775806
    state: 'present'
"""

RETURN = """
    export_set:
        description: Attributes of the updated Export Set.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the Export Set
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..xxxxxEXAMPLExxxxx
            availability_domain:
                description: The availability domain the Export Set is in.
                returned: always
                type: string
                sample: IwGV:US-EXAMPLE-AD-1
            display_name:
                description: The user-friendly name for the Export Set.
                returned: always
                type: string
                sample: ansible-file-system
            id:
                description: The identifier of the Export Set
                returned: always
                type: string
                sample: ocid1.exportset.oc1.xzvf..xxxxxEXAMPLExxxxx
            lifecycle_state:
                description: The current state of the Export Set.
                returned: always
                type: string
                sample: ACTIVE
            max_fs_stat_bytes:
                description: Controls the maximum tbytes, fbytes, and abytes values reported by NFS FSSTAT calls
                             through any associated mount targets. This is an advanced feature. For most applications,
                             use the default value. The tbytes value reported by FSSTAT will be max_fs_stat_bytes. The
                             value of fbytes and abytes will be max_fs_stat_bytes minus the metered size of the file
                             system. If the metered size is larger than max_fs_stat_bytes, then fbytes and abytes
                             will both be '0'.
                returned: always
                type: int
                sample: 9223372036854775807
            max_fs_stat_files:
                description: Controls the maximum tfiles, ffiles, and afiles values reported by NFS FSSTAT calls
                             through any associated mount targets. This is an advanced feature. For most applications,
                             use the default value. The tfiles value reported by FSSTAT will be max_fs_stat_files. The
                             value of ffiles and afiles will be max_fs_stat_files minus the metered size of the file
                             system. If the metered size is larger than max_fs_stat_files, then ffiles and afiles
                             will both be '0'.
                returned: always
                type: int
                sample: 9223372036854775807
            time_created:
                description: Date and time when the Export Set was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2018-10-19T18:17:03.907000+00:00
            vcn_id:
                description: The identifier of the virtual cloud network (VCN) the export set is in.
                returned: always
                type: string
                sample: ocid1.vcn.oc1.xzvf..xxxxxEXAMPLExxxxx

        sample: {
                   "availability_domain":"IwGV:US-EXAMPLE-AD-1",
                   "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                   "display_name":"ansible_export_set",
                   "id":"ocid1.exportset.oc1.iad.xxxxxEXAMPLExxxxx",
                   "lifecycle_state":"ACTIVE",
                   "max_fs_stat_bytes":9223372036854775807,
                   "max_fs_stat_files":9223372036854775807,
                   "time_created":"2018-10-19T18:17:03.907000+00:00",
                   "vcn_id":"ocid1.vcn.oc1.iad.xxxxxEXAMPLExxxxx"
                }

"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.file_storage.file_storage_client import FileStorageClient
    from oci.exceptions import ServiceError, ClientError
    from oci.file_storage.models import UpdateExportSetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def update_export_set(file_storage_client, module):
    result = dict(changed=False, export_set="")
    try:
        result = oci_utils.check_and_update_resource(
            resource_type="export_set",
            get_fn=file_storage_client.get_export_set,
            kwargs_get={"export_set_id": module.params["export_set_id"]},
            update_fn=file_storage_client.update_export_set,
            client=file_storage_client,
            primitive_params_update=["export_set_id"],
            kwargs_non_primitive_update={
                UpdateExportSetDetails: "update_export_set_details"
            },
            module=module,
            update_attributes=UpdateExportSetDetails().attribute_map,
        )
    except ServiceError as ex:
        get_logger().error("Unable to update Export Set due to: %s", ex.message)
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error("Unable to update Export Set due to: %s", str(ex))
        module.fail_json(msg=str(ex))

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_export_set")
    set_logger(logger)

    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            max_fs_stat_bytes=dict(type=int, required=False),
            max_fs_stat_files=dict(type=int, required=False),
            export_set_id=dict(type="str", required=False, aliases=["id"]),
            display_name=dict(type="str", required=False),
            state=dict(
                type="str", required=False, default="present", choices=["present"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    file_storage_client = oci_utils.create_service_client(module, FileStorageClient)
    state = module.params["state"]

    if state == "present":
        result = update_export_set(file_storage_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
