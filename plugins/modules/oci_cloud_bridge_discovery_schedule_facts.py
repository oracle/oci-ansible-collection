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
module: oci_cloud_bridge_discovery_schedule_facts
short_description: Fetches details about one or multiple DiscoverySchedule resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DiscoverySchedule resources in Oracle Cloud Infrastructure
    - Lists discovery schedules.
    - If I(discovery_schedule_id) is specified, the details of a single DiscoverySchedule will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple discovery_schedules.
        type: str
    discovery_schedule_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the discovery schedule.
            - Required to get a specific discovery_schedule.
        type: str
        aliases: ["id"]
    lifecycle_state:
        description:
            - The current state of the discovery schedule.
        type: str
        choices:
            - "ACTIVE"
            - "DELETED"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. By default, the timeCreated is in descending order and displayName is in ascending
              order.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific discovery_schedule
  oci_cloud_bridge_discovery_schedule_facts:
    # required
    discovery_schedule_id: "ocid1.discoveryschedule.oc1..xxxxxxEXAMPLExxxxxx"

- name: List discovery_schedules
  oci_cloud_bridge_discovery_schedule_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    discovery_schedule_id: "ocid1.discoveryschedule.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: ACTIVE
    sort_by: timeCreated
    sort_order: ASC
    display_name: display_name_example

"""

RETURN = """
discovery_schedules:
    description:
        - List of DiscoverySchedule resources
    returned: on success
    type: complex
    contains:
        execution_recurrences:
            description:
                - Recurrence specification for the discovery schedule execution.
                - Returned for get operation
            returned: on success
            type: str
            sample: execution_recurrences_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the discovery schedule.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name for the discovery schedule. Does not have to be unique, and it's mutable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the discovery schedule exists.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - Current state of the discovery schedule.
            returned: on success
            type: str
            sample: ACTIVE
        lifecycle_details:
            description:
                - The detailed state of the discovery schedule.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The time when the discovery schedule was created in RFC3339 format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the discovery schedule was last updated in RFC3339 format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace/scope. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is
                  predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "execution_recurrences": "execution_recurrences_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
    from oci.cloud_bridge import DiscoveryClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DiscoveryScheduleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "discovery_schedule_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_discovery_schedule,
            discovery_schedule_id=self.module.params.get("discovery_schedule_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "discovery_schedule_id",
            "lifecycle_state",
            "sort_by",
            "sort_order",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_discovery_schedules,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DiscoveryScheduleFactsHelperCustom = get_custom_class(
    "DiscoveryScheduleFactsHelperCustom"
)


class ResourceFactsHelper(
    DiscoveryScheduleFactsHelperCustom, DiscoveryScheduleFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            discovery_schedule_id=dict(aliases=["id"], type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="discovery_schedule",
        service_client_class=DiscoveryClient,
        namespace="cloud_bridge",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(discovery_schedules=result)


if __name__ == "__main__":
    main()
