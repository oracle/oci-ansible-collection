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
module: oci_volume_backup_policy_facts
short_description: Retrieve information of volume backup policies in OCI Block Volume service
description:
    - This module retrieves information of the specified volume backup policy or all volume backup policies available
      to the caller.
version_added: "2.5"
options:
    policy_id:
        description: The OCID of the volume backup policy.
        required: false
        aliases: ['id']
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get information of a volume backup policy
  oci_volume_backup_policy_facts:
    id: ocid1.volumebackuppolicy.oc1..xxxxxEXAMPLExxxxx

- name: Get information of all available volume backup policies
  oci_volume_backup_policy_assignment_facts:
"""

RETURN = """
volume_backup_polices:
    description: List of volume backup policies
    returned: on success
    type: complex
    contains:
        display_name:
            description: A user-friendly name for the volume backup policy. Does not have to be unique and it's
                         changeable. Avoid entering confidential information.
            returned: always
            type: string
            sample: gold
        id:
            description: The OCID of the volume backup policy.
            returned: always
            type: string
            sample: ocid1.volumebackuppolicy.oc1..xxxxxEXAMPLExxxxx
        schedules:
            description: The collection of schedules that this policy will apply.
            returned: always
            type: list
            sample: [
                {
                  "backup-type": "INCREMENTAL",
                  "offset-seconds": 0,
                  "period": "ONE_DAY",
                  "retention-seconds": 604800
                },
                {
                  "backup-type": "INCREMENTAL",
                  "offset-seconds": 0,
                  "period": "ONE_WEEK",
                  "retention-seconds": 2419200
                },
                {
                  "backup-type": "INCREMENTAL",
                  "offset-seconds": 0,
                  "period": "ONE_MONTH",
                  "retention-seconds": 31560000
                },
                {
                  "backup-type": "FULL",
                  "offset-seconds": 0,
                  "period": "ONE_YEAR",
                  "retention-seconds": 157680000
                }
            ]
        time_created:
            description: The date and time the volume backup policy was created. Format defined by RFC3339.
            returned: always
            type: string
            sample: 2017-12-22T15:40:53.219000+00:00
    sample: [{
                "display_name": "silver",
                "id": "ocid1.volumebackuppolicy.oc1..xxxxxEXAMPLExxxxx",
                "schedules": [
                    {
                        "backup_type": "INCREMENTAL",
                        "offset_seconds": 0,
                        "period": "ONE_WEEK",
                        "retention_seconds": 2419200
                    },
                    {
                        "backup_type": "INCREMENTAL",
                        "offset_seconds": 0,
                        "period": "ONE_MONTH",
                        "retention_seconds": 31560000
                    },
                    {
                        "backup_type": "FULL",
                        "offset_seconds": 0,
                        "period": "ONE_YEAR",
                        "retention_seconds": 157680000
                    }
                ],
                "time_created": "2017-10-01T00:00:00+00:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.blockstorage_client import BlockstorageClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(dict(policy_id=dict(type="str", required=False, aliases=["id"])))

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    block_storage_client = oci_utils.create_service_client(module, BlockstorageClient)

    policy_id = module.params["policy_id"]

    try:
        if policy_id:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        block_storage_client.get_volume_backup_policy,
                        policy_id=policy_id,
                    ).data
                )
            ]
        else:
            optional_list_method_params = ["display_name"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            result = to_dict(
                oci_utils.call_with_backoff(
                    block_storage_client.list_volume_backup_policies, **optional_kwargs
                ).data
            )

    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(volume_backup_policies=result)


if __name__ == "__main__":
    main()
