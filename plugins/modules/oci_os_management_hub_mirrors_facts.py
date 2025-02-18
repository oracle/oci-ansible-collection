#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_os_management_hub_mirrors_facts
short_description: Fetches details about one or multiple Mirrors resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Mirrors resources in Oracle Cloud Infrastructure
    - Lists all software source mirrors associated with a specified management station.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    management_station_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station.
        type: str
        required: true
    display_name:
        description:
            - A filter to return resources that match the given user-friendly name.
        type: str
        aliases: ["name"]
    display_name_contains:
        description:
            - A filter to return resources that may partially match the given display name.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    mirror_states:
        description:
            - List of Mirror state to filter by
        type: list
        elements: str
        choices:
            - "UNSYNCED"
            - "QUEUED"
            - "SYNCING"
            - "SYNCED"
            - "FAILED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List mirrors
  oci_os_management_hub_mirrors_facts:
    # required
    management_station_id: "ocid1.managementstation.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    display_name_contains: display_name_contains_example
    sort_order: ASC
    sort_by: timeCreated
    mirror_states: [ "UNSYNCED" ]

"""

RETURN = """
mirrors:
    description:
        - List of Mirrors resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID of a software source
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Display name of the mirror
            returned: on success
            type: str
            sample: display_name_example
        type:
            description:
                - Type of the mirror
            returned: on success
            type: str
            sample: CUSTOM
        os_family:
            description:
                - The OS family the Software Source belongs to
            returned: on success
            type: str
            sample: ORACLE_LINUX_9
        arch_type:
            description:
                - The architecture type supported by the Software Source
            returned: on success
            type: str
            sample: X86_64
        state:
            description:
                - Current state of the mirror
            returned: on success
            type: str
            sample: UNSYNCED
        percentage:
            description:
                - A decimal number representing the completness percentage
            returned: on success
            type: int
            sample: 56
        time_last_synced:
            description:
                - Timestamp of the last time the mirror was sync
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        log:
            description:
                - The current log from the management station plugin.
            returned: on success
            type: str
            sample: log_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "type": "CUSTOM",
        "os_family": "ORACLE_LINUX_9",
        "arch_type": "X86_64",
        "state": "UNSYNCED",
        "percentage": 56,
        "time_last_synced": "2013-10-20T19:20:30+01:00",
        "log": "log_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import ManagementStationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubMirrorsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "management_station_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "display_name_contains",
            "sort_order",
            "sort_by",
            "mirror_states",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_mirrors,
            management_station_id=self.module.params.get("management_station_id"),
            **optional_kwargs
        )


OsManagementHubMirrorsFactsHelperCustom = get_custom_class(
    "OsManagementHubMirrorsFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubMirrorsFactsHelperCustom, OsManagementHubMirrorsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            management_station_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            display_name_contains=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            mirror_states=dict(
                type="list",
                elements="str",
                choices=["UNSYNCED", "QUEUED", "SYNCING", "SYNCED", "FAILED"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="mirrors",
        service_client_class=ManagementStationClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(mirrors=result)


if __name__ == "__main__":
    main()
