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
module: oci_export_set_facts
short_description: Fetches details of the OCI Export Set instances
description:
    - Fetches details of the OCI Export Set instances.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment from which details of all OCI Export Set instances
                     must be fetched
        required: false
    availability_domain:
        description: Availability domain from which details of all OCI Export Set instances
                     must be fetched.
        required: false
    export_set_id:
        description: Identifier of the Export Set whose details needs to be fetched.
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
# Fetch Export Set
- name: List all Export Set in a compartment and availability domain
  oci_export_set_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      availability_domain: 'IwGV:US-EXAMPLE-AD-1'

# Fetch Export Set, filtered by Display Name
- name: List all Export Set in a compartment and availability domain, filtered by Display Name
  oci_export_set_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      availability_domain: 'IwGV:US-EXAMPLE-AD-1'
      display_name: 'ansible-export-set'

# Fetch Export Set, filtered by lifecycle state
- name: List all Export Set in a compartment and availability domain, filtered by lifecycle state
  oci_export_set_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      availability_domain: 'IwGV:US-EXAMPLE-AD-1'
      lifecycle_state: 'CREATING'

# Fetch specific Export Set
- name: List a specific Export Set
  oci_export_set_facts:
      export_set_id: 'ocid1.exportset..xxxxxEXAMPLExxxxx'
"""

RETURN = """
    export_sets:
        description: Attributes of the fetchedd Export Set.
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
                returned: when listed by export_set_id
                type: int
                sample: 9223372036854775807
            max_fs_stat_files:
                description: Controls the maximum tfiles, ffiles, and afiles values reported by NFS FSSTAT calls
                             through any associated mount targets. This is an advanced feature. For most applications,
                             use the default value. The tfiles value reported by FSSTAT will be max_fs_stat_files. The
                             value of ffiles and afiles will be max_fs_stat_files minus the metered size of the file
                             system. If the metered size is larger than max_fs_stat_files, then ffiles and afiles
                             will both be '0'.
                returned: when listed by export_set_id
                type: int
                sample: 9223372036854775807
            time_created:
                description: Date and time when the Export Set was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2018-10-19T18:12:54.027000+00:00
            vcn_id:
                description: The identifier of the virtual cloud network (VCN) the export set is in.
                returned: always
                type: string
                sample: ocid1.vcn.oc1.xzvf..xxxxxEXAMPLExxxxx

        sample: [
                   {
                     "availability_domain":"IwGV:US-EXAMPLE-AD-1",
                     "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                     "display_name":"ansible_export_set",
                     "id":"ocid1.exportset.oc1.iad.xxxxxEXAMPLExxxxx",
                     "lifecycle_state":"ACTIVE",
                     "time_created":"2018-10-19T18:12:54.027000+00:00",
                     "vcn_id":"ocid1.vcn.oc1.iad.xxxxxEXAMPLExxxxx"
                  }
                ]

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


def list_export_sets(file_storage_client, module):
    result = dict(export_sets="")
    compartment_id = module.params.get("compartment_id")
    availability_domain = module.params.get("availability_domain")
    export_set_id = module.params.get("export_set_id")
    try:
        if compartment_id and availability_domain:
            get_logger().debug(
                "Listing all Export Sets under compartment %s and availability domain %s",
                compartment_id,
                availability_domain,
            )
            optional_list_method_params = ["display_name", "lifecycle_state"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            existing_export_sets_summary = to_dict(
                oci_utils.list_all_resources(
                    file_storage_client.list_export_sets,
                    compartment_id=compartment_id,
                    availability_domain=availability_domain,
                    **optional_kwargs
                )
            )
            existing_export_sets = [
                oci_utils.call_with_backoff(
                    file_storage_client.get_export_set, export_set_id=export_set["id"]
                ).data
                for export_set in existing_export_sets_summary
            ]
        elif export_set_id:
            get_logger().debug("Listing Export Set %s", export_set_id)
            response = oci_utils.call_with_backoff(
                file_storage_client.get_export_set, export_set_id=export_set_id
            )
            existing_export_sets = [response.data]
        else:
            module.fail_json(
                msg="No value provided for either compartment_id and availability_domain"
                + "or export_set_id"
            )
    except ServiceError as ex:
        get_logger().error("Unable to list Export Set due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["export_sets"] = to_dict(existing_export_sets)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_export_set_facts")
    set_logger(logger)
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            availability_domain=dict(type="str", required=False),
            export_set_id=dict(type="str", required=False, aliases=["id"]),
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
            ["compartment_id", "export_set_id"],
            ["availability_domain", "export_set_id"],
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    file_storage_client = oci_utils.create_service_client(module, FileStorageClient)
    result = list_export_sets(file_storage_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
