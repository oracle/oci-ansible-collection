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
module: oci_export_facts
short_description: Fetches details of the OCI Export instances
description:
    - Fetches details of the OCI Export instances.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment from which details of all OCI Export instances
                     must be fetched.
        required: false
    export_set_id:
        description: Identifier of the export set from which details of all OCI Export instances
                     must be fetched
        required: false
    file_system_id:
        description: Identifier of the file system from which details of all OCI Export instances
                     must be fetched
        required: false
    export_id:
        description: Identifier of the Export whose details needs to be fetched.
        required: false
        aliases: ['id']
    lifecycle_state:
        description: A filter to only return resources that match the given lifecycle state.  The state value is
                     case-insensitive.
        required: false
        choices: ['CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
# Fetch Export by Compartment Identifier
- name: List all Export in a compartment
  oci_export_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'

# Fetch Export by File System Identifier
- name: List all Export of a File System
  oci_export_facts:
      file_system_id: 'ocid1.filesystem..xxxxxEXAMPLExxxxx'

# Fetch Export by Export Set Identifier
- name: List all Export of an Export Set
  oci_export_facts:
      export_set_id: 'ocid1.exportset..xxxxxEXAMPLExxxxx'

# Fetch Export, filtered by lifecycle state
- name: List all Mount Target in a compartment, filtered by lifecycle state
  oci_export_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      lifecycle_state: 'CREATING'

# Fetch specific Export
- name: List a specific Export
  oci_export_facts:
      export_id: 'ocid1.export..xxxxxEXAMPLExxxxx'
"""

RETURN = """
    exports:
        description: Attributes of the fetched Export.
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

        sample: [{
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


def list_exports(file_storage_client, module):
    result = dict(exports="")
    compartment_id = module.params.get("compartment_id")
    export_set_id = module.params.get("export_set_id")
    file_system_id = module.params.get("file_system_id")
    export_id = module.params.get("export_id")
    try:
        if compartment_id or export_set_id or file_system_id:
            get_logger().debug("Listing all Exports under given Identifier")
            optional_list_method_params = ["lifecycle_state"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            existing_exports_summary = to_dict(
                oci_utils.list_all_resources(
                    file_storage_client.list_exports,
                    compartment_id=compartment_id,
                    export_set_id=export_set_id,
                    file_system_id=file_system_id,
                    **optional_kwargs
                )
            )
            existing_exports = [
                oci_utils.call_with_backoff(
                    file_storage_client.get_export, export_id=export["id"]
                ).data
                for export in existing_exports_summary
            ]
        elif export_id:
            get_logger().debug("Listing Export %s", file_system_id)
            response = oci_utils.call_with_backoff(
                file_storage_client.get_export, export_id=export_id
            )
            existing_exports = [response.data]
        else:
            module.fail_json(
                msg="No value provided for either compartment_id, export_set_id"
                + "and file_system_id or export_id"
            )
    except ServiceError as ex:
        get_logger().error("Unable to list Exports due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["exports"] = to_dict(existing_exports)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_file_system_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            export_set_id=dict(type="str", required=False),
            file_system_id=dict(type="str", required=False),
            export_id=dict(type="str", required=False, aliases=["id"]),
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
            ["export_set_id", "file_system_id"],
            ["export_set_id", "compartment_id"],
            ["export_id", "compartment_id"],
            ["export_id", "file_system_id"],
            ["export_id", "export_set_id"],
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    file_storage_client = oci_utils.create_service_client(module, FileStorageClient)
    result = list_exports(file_storage_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
