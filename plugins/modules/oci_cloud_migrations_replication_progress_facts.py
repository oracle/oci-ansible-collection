#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_cloud_migrations_replication_progress_facts
short_description: Fetches details about a ReplicationProgress resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ReplicationProgress resource in Oracle Cloud Infrastructure
    - Gets the progress percentage of a migration asset's replication process.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    migration_asset_id:
        description:
            - Unique migration asset identifier
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific replication_progress
  oci_cloud_migrations_replication_progress_facts:
    # required
    migration_asset_id: "ocid1.migrationasset.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
replication_progress:
    description:
        - ReplicationProgress resource
    returned: on success
    type: complex
    contains:
        percentage:
            description:
                - Percentage of the current replication progress from 0 to 100.
            returned: on success
            type: int
            sample: 56
        status:
            description:
                - Status of the current replication progress. It can be None or InProgress.
            returned: on success
            type: str
            sample: NONE
        time_started:
            description:
                - Start time of the current replication process
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_oflast_replication_start:
            description:
                - Start time of the last replication process. It can be Completed or Failed.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_last_replication_end:
            description:
                - End time of the last replication process. It can be Completed or Failed.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_last_replication_success:
            description:
                - End time of the last successful replication process, which has been completed.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        last_replication_status:
            description:
                - Status of the last replication task. It can be Completed or Failed.
            returned: on success
            type: str
            sample: NONE
        last_replication_error:
            description:
                - Error message if the last finished replication failed.
            returned: on success
            type: str
            sample: last_replication_error_example
    sample: {
        "percentage": 56,
        "status": "NONE",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_oflast_replication_start": "2013-10-20T19:20:30+01:00",
        "time_of_last_replication_end": "2013-10-20T19:20:30+01:00",
        "time_of_last_replication_success": "2013-10-20T19:20:30+01:00",
        "last_replication_status": "NONE",
        "last_replication_error": "last_replication_error_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.cloud_migrations import MigrationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ReplicationProgressFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "migration_asset_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_replication_progress,
            migration_asset_id=self.module.params.get("migration_asset_id"),
        )


ReplicationProgressFactsHelperCustom = get_custom_class(
    "ReplicationProgressFactsHelperCustom"
)


class ResourceFactsHelper(
    ReplicationProgressFactsHelperCustom, ReplicationProgressFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(migration_asset_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="replication_progress",
        service_client_class=MigrationClient,
        namespace="cloud_migrations",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(replication_progress=result)


if __name__ == "__main__":
    main()
