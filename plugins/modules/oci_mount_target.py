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
module: oci_mount_target
short_description: Create, update and delete a Mount Target in OCI Filesystem Service.
description:
    - Create an OCI Mount Target
    - Update an OCI Mount Target, if present, with a new display name
    - Delete an OCI Mount Target, if present.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which this Mount Target would be created.
                     Mandatory for create operation.
        required: false
    availability_domain:
        description: The availability domain in which to create the Mount Target. Mandatory for create operation.
        required: false
    mount_target_id:
        description: Identifier of the existing Mount Target which required to be updated, deleted.
                     Mandatory for update and delete.
        required: false
        aliases: ['id']
    hostname_label:
        description: The hostname for the mount target's IP address, used for DNS resolution. The value is the hostname
                     portion of the private IP address's fully qualified domain name (FQDN). For example, files-1 in the
                     FQDN files-1.subnet123.vcn1.oraclevcn.com. Must be unique across all VNICs in the subnet and comply
                     with RFC 952 and RFC 1123.
        required: false
    display_name:
        description: A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential
                     information.
        required: false
    ip_address:
        description: A private IP address of your choice. Must be an available IP address within the subnet's CIDR.
                     If you don't specify a value, Oracle automatically assigns a private IP address from the subnet.
        required: false
    subnet_id:
        description: The Identifier of the subnet in which to create the Mount Target.
        required: false
    state:
        description: Create, update and delete Mount Target. For I(state=present), if it does not exist, it gets created.
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
# Create Mount Target
- name: Create Mount Target
  oci_mount_target:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    availability_domain: 'IwGV:US-EXAMPLE-AD-1'
    hostname_label: 'ansiblemt'
    display_name: 'ansible_mount_target'
    ip_address: '10.0.0.0'
    subnet_id: 'ocid1.subnet.oc1..xxxxxEXAMPLExxxxx'
    freeform_tags:
        deployment: 'production'
    defined_tags:
        target_users:
            division: 'documentation'
    state: 'present'

# Update Mount Target's Freeform Tags
- name: Update Mount Target's Freeform Tags
  oci_mount_target:
    mount_target_id: 'ocid1.mounttarget.oc1..xxxxxEXAMPLExxxxx'
    freeform_tags:
        deployment: 'trial'
    state: 'present'

# Update Mount Target's Defined Tags
- name: Update Mount Target's Defined Tags
  oci_mount_target:
    mount_target_id: 'ocid1.mounttarget.oc1..xxxxxEXAMPLExxxxx'
    defined_tags:
        target_users:
            division: 'development'
    state: 'present'

# Update Mount Target's display name
- name: Update Mount Target's display name
  oci_mount_target:
    mount_target_id: 'ocid1.mounttarget.oc1..xxxxxEXAMPLExxxxx'
    display_name: 'updated_ansible_mount_target'
    state: 'present'

# Delete Mount Target
- name: Delete Mount Target
  oci_mount_target:
    id: 'ocid1.mounttarget.oc1..xxxxxEXAMPLExxxxx'
    state: 'absent'
"""

RETURN = """
    mount_target:
        description: Attributes of the created/updated Mount Target. For delete, deleted Mount Target
                     description will be returned.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the Mount Target
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..xxxxxEXAMPLExxxxx
            availability_domain:
                description: The availability domain the mount target is in.
                returned: always
                type: string
                sample: IwGV:US-EXAMPLE-AD-1
            display_name:
                description: The user-friendly name for the Mount Target.
                returned: always
                type: string
                sample: ansible-mount-target
            export_set_id:
                description: The identifier of the associated export set. Controls what file
                             systems will be exported through Network File System (NFS)
                             protocol on this mount target.
                returned: always
                type: string
                sample: ocid1.exportset.oc1.xzvf..xxxxxEXAMPLExxxxx
            id:
                description: The identifier of the Mount Target
                returned: always
                type: string
                sample: ocid1.mounttarget.oc1.xzvf..xxxxxEXAMPLExxxxx
            lifecycle_details:
                description: Additional information about the current lifecycle state.
                returned: always
                type: string
                sample: details
            lifecycle_state:
                description: The current state of the Mount Target.
                returned: always
                type: string
                sample: AVAILABLE
            time_created:
                description: Date and time when the Mount Target was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2018-10-16T09:42:33.673000+00:00
            private_ip_ids:
                description: The OCIDs of the private IP addresses associated with this mount target.
                returned: always
                type: list
                sample: [ ocid1.privateip.oc1.xzvf..xxxxxEXAMPLExxxxx ]
            subnet_id:
                description: The OCID of the subnet the Mount Target is in.
                returned: always
                type: string
                sample: ocid1.subnet.oc1.xzvf..xxxxxEXAMPLExxxxx
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

        sample: {
                   "availability_domain":"IwGV:US-EXAMPLE-AD-1",
                   "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                   "display_name":"ansible_mount_target",
                   "export_set_id":"ocid1.exportset.oc1.iad.xxxxxEXAMPLExxxxx",
                   "defined_tags":{
                                   "ansible_tag_namespace_integration_test_1":{
                                   "ansible_tag_1":"initial"
                                 }
                                },
                   "freeform_tags":{
                                   "system_license":"trial"
                                  },
                   "id":"ocid1.mounttarget.oc1.iad.xxxxxEXAMPLExxxxx",
                   "lifecycle_details":"",
                   "lifecycle_state":"ACTIVE",
                   "private_ip_ids":[
                                      "ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx"
                                    ],
                   "subnet_id":"ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx",
                   "time_created":"2018-10-16T09:42:33.673000+00:00"
                }

"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.file_storage.file_storage_client import FileStorageClient
    from oci.exceptions import ServiceError, ClientError
    from oci.file_storage.models import (
        CreateMountTargetDetails,
        UpdateMountTargetDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_or_update_mount_target(file_storage_client, module):
    result = dict(changed=False, mount_target="")
    mount_target_id = module.params.get("mount_target_id")
    try:
        if mount_target_id:
            result = update_mount_target(file_storage_client, module)
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="mount_target",
                create_fn=create_mount_target,
                kwargs_create={
                    "file_storage_client": file_storage_client,
                    "module": module,
                },
                list_fn=file_storage_client.list_mount_targets,
                kwargs_list={
                    "compartment_id": module.params.get("compartment_id"),
                    "availability_domain": module.params.get("availability_domain"),
                },
                module=module,
                model=CreateMountTargetDetails(),
            )
    except ServiceError as ex:
        get_logger().error(
            "Unable to create/update Mount Target due to: %s", ex.message
        )
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error("Unable to launch/update Mount Target due to: %s", str(ex))
        module.fail_json(msg=str(ex))

    return result


def create_mount_target(file_storage_client, module):
    create_mount_target_details = CreateMountTargetDetails()
    for attribute in create_mount_target_details.attribute_map:
        create_mount_target_details.__setattr__(attribute, module.params.get(attribute))

    result = oci_utils.create_and_wait(
        resource_type="mount_target",
        create_fn=file_storage_client.create_mount_target,
        kwargs_create={"create_mount_target_details": create_mount_target_details},
        client=file_storage_client,
        get_fn=file_storage_client.get_mount_target,
        get_param="mount_target_id",
        module=module,
    )
    return result


def update_mount_target(file_storage_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type="mount_target",
        get_fn=file_storage_client.get_mount_target,
        kwargs_get={"mount_target_id": module.params["mount_target_id"]},
        update_fn=file_storage_client.update_mount_target,
        client=file_storage_client,
        primitive_params_update=["mount_target_id"],
        kwargs_non_primitive_update={
            UpdateMountTargetDetails: "update_mount_target_details"
        },
        module=module,
        update_attributes=UpdateMountTargetDetails().attribute_map,
    )
    return result


def delete_mount_target(file_storage_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="mount_target",
        client=file_storage_client,
        get_fn=file_storage_client.get_mount_target,
        kwargs_get={"mount_target_id": module.params["mount_target_id"]},
        delete_fn=file_storage_client.delete_mount_target,
        kwargs_delete={"mount_target_id": module.params["mount_target_id"]},
        module=module,
    )

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_mount_target")
    set_logger(logger)

    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            availability_domain=dict(type="str", required=False),
            mount_target_id=dict(type="str", required=False, aliases=["id"]),
            hostname_label=dict(type="str", required=False),
            display_name=dict(type="str", required=False),
            ip_address=dict(type="str", required=False),
            subnet_id=dict(type="str", required=False),
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
        result = create_or_update_mount_target(file_storage_client, module)
    elif state == "absent":
        result = delete_mount_target(file_storage_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
