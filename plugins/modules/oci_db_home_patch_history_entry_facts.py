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
module: oci_db_home_patch_history_entry_facts
short_description: Fetches details of one or more DB Home Patch History Entries
description:
    - Fetches details of one or more  DB Home Patch History Entries.
version_added: "2.5"
options:
    db_home_id:
        description: Identifier of the  DB Home whose Patch History Entries needs
                     to be fetched
        required: true
    patch_history_entry_id:
        description: Identifier of a Patch History Entry whose details needs to be fetched.
        required: false
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""
EXAMPLES = """
#Fetch all DB Home Patch History Entries
- name: List DB Home Patch History Entries
  oci_db_Home_patch_history_entry_facts:
    db_Home_id: 'ocid1.dbhome.aaaa'
#Fetch a specific DB Home Patch History Entry
- name: List a specific DB Home Patch History Entry
  oci_db_Home_patch_history_entry_facts:
    db_Home_id: 'ocid1.dbhome.aaaa'
    patch_history_entry_id: 'ocid1.dbpatchhistory.oc1.ad.abu'
"""

RETURN = """
    db_home_patch_history_entries:
        description: Attributes of the DB Home Patch History Entry
        returned: success
        type: complex
        contains:
            action :
                description: The action being performed or was completed.
                returned: always
                type: string
                sample: APPLY
            id:
                description: Identifier of the DB Home Patch History Entry.
                returned: always
                type: string
                sample: ocid1.dbpatchhistory.oc1.iad.xxxxxEXAMPLExxxxx
            lifecycle_details:
                description: A descriptive text associated with the lifecycle_state. Typically
                             can contain additional displayable text.
                returned: always
                type: string
                sample: DCS-10001:Internal error encountered
            lifecycle_state:
                description: The current state of the action.
                returned: always
                type: string
                sample: SUCCEEDED
            patch_id:
                description: Identifier of the Patch whose history is fetched
                returned: always
                type: string
                sample: ocid1.dbpatch.oc1.iad.xxxxxEXAMPLExxxxx
            time_ended:
                description: The date and time when the patch action completed.
                returned: always
                type: string
                sample: 2018-01-29T01:00:00+00:00
            time_started:
                description: The date and time when the patch action started.
                returned: always
                type: string
                sample: 2018-01-29T12:30:00+00:00

        sample: [{
                    "action":"PRECHECK",
                    "id":"ocid1.dbpatchhistory.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_details":"Action was successful",
                    "lifecycle_state":"SUCCEEDED",
                    "patch_id":"ocid1.dbpatch.oc1.iad.xxxxxEXAMPLExxxxx",
                    "time_ended":"2018-02-24T18:28:52.198000+00:00",
                    "time_started":"2018-02-24T18:25:06.151000+00:00"
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


def list_db_home_patch_history_entries(db_client, module):
    result = dict(db_home_patch_history_entries="")
    db_home_id = module.params.get("db_home_id")
    patch_history_entry_id = module.params.get("patch_history_entry_id")
    try:
        if patch_history_entry_id:
            get_logger().debug(
                "Listing DB Home Patch History Entry for ID  %s of DB Home %s",
                patch_history_entry_id,
                db_home_id,
            )
            response = oci_utils.call_with_backoff(
                db_client.get_db_home_patch_history_entry,
                db_home_id=db_home_id,
                patch_history_entry_id=patch_history_entry_id,
            )
            db_home_patch_history_entries = [response.data]
        else:
            get_logger().debug(
                "Listing all DB Home Patch History Entries of DB Home %s", db_home_id
            )
            db_home_patch_history_entries = oci_utils.list_all_resources(
                db_client.list_db_home_patch_history_entries, db_home_id=db_home_id
            )
    except ServiceError as ex:
        get_logger().error(
            "Unable to list DB Home Patch History Entries due to %s", ex.message
        )
        module.fail_json(msg=ex.message)

    result["db_home_patch_history_entries"] = to_dict(db_home_patch_history_entries)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_db_home_patch_history_entry_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            db_home_id=dict(type="str", required=True),
            patch_history_entry_id=dict(type="str", required=False),
        )
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)
    result = list_db_home_patch_history_entries(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
