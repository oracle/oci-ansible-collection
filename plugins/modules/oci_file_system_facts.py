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
module: oci_file_system_facts
short_description: Fetches details of the OCI File System instances
description:
    - Fetches details of the OCI File System instances.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment from which details of all OCI File System instances
                     must be fetched
        required: false
    availability_domain:
        description: Availability domain from which details of all OCI File System instances
                     must be fetched.
        required: false
    file_system_id:
        description: Identifier of the File System whose details needs to be fetched.
        required: false
        aliases: ['id']
    lifecycle_state:
        description: A filter to only return resources that match the given lifecycle state.  The state value is
                     case-insensitive.
        required: false
        choices: ['CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
# Fetch File System
- name: List all File System in a compartment and availability domain
  oci_file_system_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      availability_domain: 'IwGV:US-EXAMPLE-AD-1'

# Fetch File System, filtered by Display Name
- name: List all File System in a compartment and availability domain, filtered by Display Name
  oci_file_system_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      availability_domain: 'IwGV:US-EXAMPLE-AD-1'
      display_name: 'ansible-mount-target'

# Fetch File System, filtered by lifecycle state
- name: List all File System in a compartment and availability domain, filtered by lifecycle state
  oci_file_system_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      availability_domain: 'IwGV:US-EXAMPLE-AD-1'
      lifecycle_state: 'CREATING'

# Fetch specific File System
- name: List a specific File System
  oci_file_system_facts:
      file_system_id: 'ocid1.filesystem..xxxxxEXAMPLExxxxx'
"""

RETURN = """
    file_systems:
        description: Attributes of the fetchedd File System.
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
                description: The number of bytes consumed by the file system, including any snapshots. This number
                             reflects the metered size of the file system and is updated asynchronously with respect
                             to updates to the file system.
                returned: always
                type: int
                sample: 582
            time_created:
                description: Date and time when the File System was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2018-10-16T09:43:00.051000+00:00

        sample: [{
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
                }]

"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.file_storage.file_storage_client import FileStorageClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def list_file_systems(file_storage_client, module):
    result = dict(file_systems="")
    compartment_id = module.params.get("compartment_id")
    availability_domain = module.params.get("availability_domain")
    file_system_id = module.params.get("file_system_id")
    try:
        if compartment_id and availability_domain:
            get_logger().debug(
                "Listing all File Systems under compartment %s and availability domain %s",
                compartment_id,
                availability_domain,
            )
            optional_list_method_params = ["display_name", "lifecycle_state"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            existing_file_systems_summary = to_dict(
                oci_utils.list_all_resources(
                    file_storage_client.list_file_systems,
                    compartment_id=compartment_id,
                    availability_domain=availability_domain,
                    **optional_kwargs
                )
            )
            existing_file_systems = [
                oci_utils.call_with_backoff(
                    file_storage_client.get_file_system,
                    file_system_id=file_system["id"],
                ).data
                for file_system in existing_file_systems_summary
            ]
        elif file_system_id:
            get_logger().debug("Listing File System %s", file_system_id)
            response = oci_utils.call_with_backoff(
                file_storage_client.get_file_system, file_system_id=file_system_id
            )
            existing_file_systems = [response.data]
        else:
            module.fail_json(
                msg="No value provided for either compartment_id and availability_domain"
                + "or file_system_id"
            )
    except ServiceError as ex:
        get_logger().error("Unable to list File Systems due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["file_systems"] = to_dict(existing_file_systems)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_file_system_facts")
    set_logger(logger)
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            availability_domain=dict(type="str", required=False),
            file_system_id=dict(type="str", required=False, aliases=["id"]),
            lifecycle_state=dict(
                type="str",
                required=False,
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"],
            ),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[
            ["compartment_id", "file_system_id"],
            ["availability_domain", "file_system_id"],
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    file_storage_client = oci_utils.create_service_client(module, FileStorageClient)
    result = list_file_systems(file_storage_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
