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
module: oci_db_system_patch_facts
short_description: Fetches details of one or more DB System Patches
description:
    - Fetches details of one or more  DB System Patches.
version_added: "2.5"
options:
    db_system_id:
        description: Identifier of the  DB System for which the Patches are
                     supported.
        required: true
    patch_id:
        description: Identifier of a Patch whose details needs to be fetched.
        required: false
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""
EXAMPLES = """
#Fetch all DB System Patches
- name: List DB System Patches
  oci_db_system_patch_facts:
    db_system_id: "ocid1.dbsystem.aaaa"
#Fetch a specific DB System Patch
- name: List a specific DB System Patch
  oci_db_system_patch_facts:
    db_system_id: "ocid1.dbsystem.aaaa"
    patch_id: "ocid1.dbpatch.aaaa"
"""

RETURN = """
    db_system_patches:
        description: Attributes of the DB System Patch.
        returned: success
        type: complex
        contains:
            available_actions :
                description: Actions that can possibly be performed using this patch.
                returned: always
                type: string
                sample: APPLY
            description:
                description: The  text describing this patch package.
                returned: always
                type: string
                sample: Oct 2017 12.2 Database patch
            id:
                description: Identifier of the DB Home Patch.
                returned: always
                type: string
                sample: ocid1.dbpatch.oc1.iad.xxxxxEXAMPLExxxxx
            last_action:
                description: Action that is currently being performed or was completed last.
                returned: always
                type: string
                sample: PRECHECK
            lifecycle_details:
                description: A descriptive text associated with the lifecycle_state. Typically
                             can contain additional displayable text.
                returned: always
                type: string
                sample: DCS-10001:Internal error encountered
            lifecycle_state:
                description: The current state of the patch as a result of last_action.
                returned: always
                type: string
                sample: AVAILABLE
            time_released:
                description: The date and time that the patch was released.
                returned: always
                type: string
                sample: 2018-01-29T01:00:00+00:00
            version:
                description: The version of this patch package.
                returned: always
                type: string
                sample: 12.2.0.1.171017

        sample: [{
                    "available_actions":[
                                            "APPLY",
                                            "PRECHECK"
                                        ],
                    "description":"Oct 2017 12.2 Database patch",
                    "id":"ocid1.dbpatch.oc1.iad.xxxxxEXAMPLExxxxx",
                    "last_action":"PRECHECK",
                    "lifecycle_details":"Operation was successful",
                    "lifecycle_state":"PRECHECK",
                    "time_released":"2018-01-29T01:00:00+00:00",
                    "version":"12.2.0.1.171017"
                }]

"""
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.database.database_client import DatabaseClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def list_db_system_patches(db_client, module):
    result = dict(db_system_patches="")
    db_system_id = module.params.get("db_system_id")
    patch_id = module.params.get("patch_id")
    try:
        if patch_id:
            get_logger().debug(
                "Listing DB System Patch for Patch ID  %s of DB System %s",
                patch_id,
                db_system_id,
            )
            response = oci_utils.call_with_backoff(
                db_client.get_db_system_patch,
                db_system_id=db_system_id,
                patch_id=patch_id,
            )
            db_system_patches = [response.data]
        else:
            get_logger().debug(
                "Listing all DB System Patches of DB System %s", db_system_id
            )
            db_system_patches = oci_utils.list_all_resources(
                db_client.list_db_system_patches, db_system_id=db_system_id
            )
    except ServiceError as ex:
        get_logger().error("Unable to list DB System Patches due to %s", ex.message)
        module.fail_json(msg=ex.message)

    result["db_system_patches"] = to_dict(db_system_patches)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_db_system_patch_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            db_system_id=dict(type="str", required=True),
            patch_id=dict(type="str", required=False),
        )
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)
    result = list_db_system_patches(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
