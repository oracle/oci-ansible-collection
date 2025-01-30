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
module: oci_os_management_hub_management_station_facts
short_description: Fetches details about one or multiple ManagementStation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagementStation resources in Oracle Cloud Infrastructure
    - Lists management stations in a compartment.
    - If I(management_station_id) is specified, the details of a single ManagementStation will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    management_station_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station.
            - Required to get a specific management_station.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
        type: str
    display_name:
        description:
            - A filter to return resources that match the given user-friendly name.
        type: str
        aliases: ["name"]
    display_name_contains:
        description:
            - A filter to return resources that may partially match the given display name.
        type: str
    lifecycle_state:
        description:
            - A filter that returns information for management stations in the specified state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    managed_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance. This filter returns resources
              associated with this managed instance.
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific management_station
  oci_os_management_hub_management_station_facts:
    # required
    management_station_id: "ocid1.managementstation.oc1..xxxxxxEXAMPLExxxxxx"

- name: List management_stations
  oci_os_management_hub_management_station_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    display_name_contains: display_name_contains_example
    lifecycle_state: CREATING
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
management_stations:
    description:
        - List of ManagementStation resources
    returned: on success
    type: complex
    contains:
        total_mirrors:
            description:
                - The number of software sources that the station is mirroring.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        mirror_sync_status:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                unsynced:
                    description:
                        - Total number of software sources that have not yet been synced.
                    returned: on success
                    type: int
                    sample: 56
                queued:
                    description:
                        - Total number of software sources that are queued for sync.
                    returned: on success
                    type: int
                    sample: 56
                syncing:
                    description:
                        - Total number of software sources currently syncing.
                    returned: on success
                    type: int
                    sample: 56
                synced:
                    description:
                        - Total number of software sources that successfully synced.
                    returned: on success
                    type: int
                    sample: 56
                failed:
                    description:
                        - Total number of software sources that failed to sync.
                    returned: on success
                    type: int
                    sample: 56
        proxy:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                is_enabled:
                    description:
                        - Indicates if the proxy should be enabled or disabled. Default is enabled.
                    returned: on success
                    type: bool
                    sample: true
                hosts:
                    description:
                        - List of hosts.
                    returned: on success
                    type: list
                    sample: []
                port:
                    description:
                        - Listening port used for the proxy.
                    returned: on success
                    type: str
                    sample: port_example
                forward:
                    description:
                        - The URL the proxy will forward to.
                    returned: on success
                    type: str
                    sample: forward_example
        mirror:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                directory:
                    description:
                        - Path to the data volume on the management station where software source mirrors are stored.
                    returned: on success
                    type: str
                    sample: directory_example
                port:
                    description:
                        - Default mirror listening port for http.
                    returned: on success
                    type: str
                    sample: port_example
                sslport:
                    description:
                        - Default mirror listening port for https.
                    returned: on success
                    type: str
                    sample: sslport_example
                sslcert:
                    description:
                        - Path to the SSL cerfificate.
                    returned: on success
                    type: str
                    sample: sslcert_example
        health:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                state:
                    description:
                        - Overall health status of the management station.
                    returned: on success
                    type: str
                    sample: HEALTHY
                description:
                    description:
                        - Explanation of the health status.
                    returned: on success
                    type: str
                    sample: description_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        managed_instance_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance that is acting as the management
                  station.
            returned: on success
            type: str
            sample: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the management
                  station.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        profile_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the registration profile used for the management
                  station.
            returned: on success
            type: str
            sample: "ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx"
        scheduled_job_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the scheduled job for the mirror sync.
            returned: on success
            type: str
            sample: "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
        time_next_execution:
            description:
                - The date and time of the next scheduled mirror sync (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
                - Returned for list operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        display_name:
            description:
                - A user-friendly name for the management station.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - User-specified description for the management station.
            returned: on success
            type: str
            sample: description_example
        hostname:
            description:
                - Hostname of the management station.
            returned: on success
            type: str
            sample: hostname_example
        overall_state:
            description:
                - Current state of the mirror sync for the management station.
            returned: on success
            type: str
            sample: NORMAL
        health_state:
            description:
                - Overall health status of the managment station.
                - Returned for list operation
            returned: on success
            type: str
            sample: HEALTHY
        overall_percentage:
            description:
                - A decimal number representing the progress of the current mirror sync.
            returned: on success
            type: int
            sample: 56
        mirror_capacity:
            description:
                - A decimal number representing the amount of mirror capacity used by the sync.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of the management station.
            returned: on success
            type: str
            sample: CREATING
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "total_mirrors": 56,
        "mirror_sync_status": {
            "unsynced": 56,
            "queued": 56,
            "syncing": 56,
            "synced": 56,
            "failed": 56
        },
        "proxy": {
            "is_enabled": true,
            "hosts": [],
            "port": "port_example",
            "forward": "forward_example"
        },
        "mirror": {
            "directory": "directory_example",
            "port": "port_example",
            "sslport": "sslport_example",
            "sslcert": "sslcert_example"
        },
        "health": {
            "state": "HEALTHY",
            "description": "description_example"
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "managed_instance_id": "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "profile_id": "ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx",
        "scheduled_job_id": "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx",
        "time_next_execution": "2013-10-20T19:20:30+01:00",
        "display_name": "display_name_example",
        "description": "description_example",
        "hostname": "hostname_example",
        "overall_state": "NORMAL",
        "health_state": "HEALTHY",
        "overall_percentage": 56,
        "mirror_capacity": 56,
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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


class OsManagementHubManagementStationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "management_station_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_station,
            management_station_id=self.module.params.get("management_station_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "display_name_contains",
            "lifecycle_state",
            "managed_instance_id",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_management_stations, **optional_kwargs
        )


OsManagementHubManagementStationFactsHelperCustom = get_custom_class(
    "OsManagementHubManagementStationFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubManagementStationFactsHelperCustom,
    OsManagementHubManagementStationFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            management_station_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            display_name_contains=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            managed_instance_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="management_station",
        service_client_class=ManagementStationClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(management_stations=result)


if __name__ == "__main__":
    main()
