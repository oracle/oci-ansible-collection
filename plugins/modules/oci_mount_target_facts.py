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
module: oci_mount_target_facts
short_description: Fetches details of the OCI Mount Target instances
description:
    - Fetches details of the OCI Mount Target instances.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment from which details of all OCI Mount Target instances
                     must be fetched
        required: false
    availability_domain:
        description: Availability domain from which details of all OCI Mount Target instances
                     must be fetched.
        required: false
    mount_target_id:
        description: Identifier of the Mount Target whose details needs to be fetched.
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
# Fetch Mount Target
- name: List all Mount Target in a compartment and availability domain
  oci_mount_target_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      availability_domain: 'IwGV:US-EXAMPLE-AD-1'

# Fetch Mount Target, filtered by Display Name
- name: List all Mount Target in a compartment and availability domain, filtered by Display Name
  oci_mount_target_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      availability_domain: 'IwGV:US-EXAMPLE-AD-1'
      display_name: 'ansible-mount-target'

# Fetch Mount Target, filtered by lifecycle state
- name: List all Mount Target in a compartment and availability domain, filtered by lifecycle state
  oci_mount_target_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      availability_domain: 'IwGV:US-EXAMPLE-AD-1'
      lifecycle_state: 'CREATING'

# Fetch specific Mount Target
- name: List a specific Mount Target
  oci_mount_target_facts:
      mount_target_id: 'ocid1.mounttarget..xxxxxEXAMPLExxxxx'
"""

RETURN = """
    mount_targets:
        description: Attributes of the fetchedd Mount Target.
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
        sample: [{
                   "availability_domain":"IwGV:US-EXAMPLE-AD-1",
                   "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                   "display_name":"ansible_mount_target",
                   "defined_tags":{
                                   "ansible_tag_namespace_integration_test_1":{
                                   "ansible_tag_1":"initial"
                                 }
                                },
                   "freeform_tags":{
                                   "system_license":"trial"
                                  },
                   "export_set_id":"ocid1.exportset.oc1.iad.xxxxxEXAMPLExxxxx",
                   "id":"ocid1.mounttarget.oc1.iad.xxxxxEXAMPLExxxxx",
                   "lifecycle_details":"",
                   "lifecycle_state":"ACTIVE",
                   "private_ip_ids":[
                                      "ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx"
                                    ],
                   "subnet_id":"ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx",
                   "time_created":"2018-10-16T09:42:33.673000+00:00"
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


def list_mount_targets(file_storage_client, module):
    result = dict(mount_targets="")
    compartment_id = module.params.get("compartment_id")
    availability_domain = module.params.get("availability_domain")
    mount_target_id = module.params.get("mount_target_id")
    try:
        if compartment_id and availability_domain:
            get_logger().debug(
                "Listing all Mount Targets under compartment %s and availability domain %s",
                compartment_id,
                availability_domain,
            )
            optional_list_method_params = ["display_name", "lifecycle_state"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            existing_mount_targets_summary = to_dict(
                oci_utils.list_all_resources(
                    file_storage_client.list_mount_targets,
                    compartment_id=compartment_id,
                    availability_domain=availability_domain,
                    **optional_kwargs
                )
            )
            existing_mount_targets = [
                oci_utils.call_with_backoff(
                    file_storage_client.get_mount_target,
                    mount_target_id=mount_target["id"],
                ).data
                for mount_target in existing_mount_targets_summary
            ]
        elif mount_target_id:
            get_logger().debug("Listing Mount Target %s", mount_target_id)
            response = oci_utils.call_with_backoff(
                file_storage_client.get_mount_target, mount_target_id=mount_target_id
            )
            existing_mount_targets = [response.data]
        else:
            module.fail_json(
                msg="No value provided for either compartment_id and availability_domain"
                + "or mount_target_id"
            )
    except ServiceError as ex:
        get_logger().error("Unable to list Mount Target due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["mount_targets"] = to_dict(existing_mount_targets)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_mount_target_facts")
    set_logger(logger)
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            availability_domain=dict(type="str", required=False),
            mount_target_id=dict(type="str", required=False, aliases=["id"]),
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
            ["compartment_id", "mount_target_id"],
            ["availability_domain", "mount_target_id"],
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    file_storage_client = oci_utils.create_service_client(module, FileStorageClient)
    result = list_mount_targets(file_storage_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
