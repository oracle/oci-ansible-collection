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
module: oci_file_system
short_description: Create, update and delete a File System in OCI Filesystem Service.
description:
    - Create an OCI File System
    - Update an OCI File System, if present, with a new display name
    - Delete an OCI File System, if present.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which this File System would be created.
                     Mandatory for create operation.
        required: false
    availability_domain:
        description: The availability domain in which to create the File System. Mandatory for create operation.
        required: false
    file_system_id:
        description: Identifier of the existing File System which required to be updated, deleted.
                     Mandatory for update and delete.
        required: false
        aliases: ['id']
    display_name:
        description: A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential
                     information.
        required: false
    state:
        description: Create, update and delete File System. For I(state=present), if it does not exist, it gets created.
                     If it exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create File System
- name: Create File System
  oci_file_system:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    availability_domain: 'IwGV:US-EXAMPLE-AD-1'
    display_name: 'ansible_file_system'
    freeform_tags:
        deployment: 'production'
    defined_tags:
        target_users:
            division: 'documentation'
    state: 'present'

# Update File System's display name
- name: Update File System's display name
  oci_file_system:
    file_system_id: 'ocid1.filesystem.oc1..xxxxxEXAMPLExxxxx'
    display_name: 'updated_ansible_file_system'
    state: 'present'

# Update File System's Freeform Tags
- name: Update File System's Freeform Tags
  oci_file_system:
    file_system_id: 'ocid1.filesystem.oc1..xxxxxEXAMPLExxxxx'
    freeform_tags:
        deployment: 'trial'
    state: 'present'

# Update File System's Defined Tags
- name: Update File System's Defined Tags
  oci_file_system:
    file_system_id: 'ocid1.filesystem.oc1..xxxxxEXAMPLExxxxx'
    defined_tags:
        target_users:
            division: 'development'
    state: 'present'

# Delete File System
- name: Delete File System
  oci_file_system:
    id: 'ocid1.filesystem.oc1..xxxxxEXAMPLExxxxx'
    state: 'absent'
"""

RETURN = """
    file_system:
        description: Attributes of the created/updated File System. For delete, deleted File System
                     description will be returned.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the File System
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..xxxxxEXAMPLExxxxx
            availability_domain:
                description: The availability domain the File System is in.
                returned: always
                type: string
                sample: IwGV:US-EXAMPLE-AD-1
            display_name:
                description: The user-friendly name for the File System.
                returned: always
                type: string
                sample: ansible-file-system
            defined_tags:
                description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
                             For more information, see
                             U(https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm).
                returned: always
                type: dict
                sample: {"Department": "Finance"}
            freeform_tags:
                description: Free-form tags for this resource. Each tag is a simple key-value pair with no
                             predefined name, type, or namespace. For more information, see
                             U(https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm).
                returned: always
                type: dict
                sample: {"Operations": {"CostCenter": "42"}}
            id:
                description: The identifier of the File System
                returned: always
                type: string
                sample: ocid1.filesystem.oc1.xzvf..xxxxxEXAMPLExxxxx
            lifecycle_state:
                description: The current state of the File System.
                returned: always
                type: string
                sample: ACTIVE
            metered_bytes:
                description: The number of bytes consumed by the File System, including any snapshots. This number
                             reflects the metered size of the File System and is updated asynchronously with respect
                             to updates to the File system.
                returned: always
                type: int
                sample: 582
            time_created:
                description: Date and time when the File System was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2018-10-16T09:43:00.051000+00:00

        sample: {
                   "availability_domain":"IwGV:US-EXAMPLE-AD-1",
                   "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                   "display_name":"ansible_file_system",
                   "defined_tags":{
                                   "ansible_tag_namespace_integration_test_1":{
                                   "ansible_tag_1":"initial"
                                 }
                                },
                   "freeform_tags":{
                                   "system_license":"trial"
                                  },
                   "id":"ocid1.filesystem.oc1.iad.xxxxxEXAMPLExxxxx",
                   "lifecycle_state":"ACTIVE",
                   "metered_bytes":100,
                   "time_created":"2018-10-16T09:43:00.051000+00:00"
                }

"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.file_storage.file_storage_client import FileStorageClient
    from oci.exceptions import ServiceError, ClientError
    from oci.file_storage.models import CreateFileSystemDetails, UpdateFileSystemDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_or_update_file_system(file_storage_client, module):
    result = dict(changed=False, file_system="")
    file_system_id = module.params.get("file_system_id")
    try:
        if file_system_id:
            result = update_file_system(file_storage_client, module)
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="file_system",
                create_fn=create_file_system,
                kwargs_create={
                    "file_storage_client": file_storage_client,
                    "module": module,
                },
                list_fn=file_storage_client.list_file_systems,
                kwargs_list={
                    "compartment_id": module.params.get("compartment_id"),
                    "availability_domain": module.params.get("availability_domain"),
                },
                module=module,
                model=CreateFileSystemDetails(),
            )
    except ServiceError as ex:
        get_logger().error("Unable to create/update File System due to: %s", ex.message)
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error("Unable to launch/update File System due to: %s", str(ex))
        module.fail_json(msg=str(ex))

    return result


def create_file_system(file_storage_client, module):
    create_file_system_details = CreateFileSystemDetails()
    for attribute in create_file_system_details.attribute_map:
        create_file_system_details.__setattr__(attribute, module.params.get(attribute))

    result = oci_utils.create_and_wait(
        resource_type="file_system",
        create_fn=file_storage_client.create_file_system,
        kwargs_create={"create_file_system_details": create_file_system_details},
        client=file_storage_client,
        get_fn=file_storage_client.get_file_system,
        get_param="file_system_id",
        module=module,
    )
    return result


def update_file_system(file_storage_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type="file_system",
        get_fn=file_storage_client.get_file_system,
        kwargs_get={"file_system_id": module.params["file_system_id"]},
        update_fn=file_storage_client.update_file_system,
        client=file_storage_client,
        primitive_params_update=["file_system_id"],
        kwargs_non_primitive_update={
            UpdateFileSystemDetails: "update_file_system_details"
        },
        module=module,
        update_attributes=UpdateFileSystemDetails().attribute_map,
    )
    return result


def delete_file_system(file_storage_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="file_system",
        client=file_storage_client,
        get_fn=file_storage_client.get_file_system,
        kwargs_get={"file_system_id": module.params["file_system_id"]},
        delete_fn=file_storage_client.delete_file_system,
        kwargs_delete={"file_system_id": module.params["file_system_id"]},
        module=module,
    )

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_file_system")
    set_logger(logger)

    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            availability_domain=dict(type="str", required=False),
            file_system_id=dict(type="str", required=False, aliases=["id"]),
            display_name=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    file_storage_client = oci_utils.create_service_client(module, FileStorageClient)
    state = module.params["state"]

    if state == "present":
        result = create_or_update_file_system(file_storage_client, module)
    elif state == "absent":
        result = delete_file_system(file_storage_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
