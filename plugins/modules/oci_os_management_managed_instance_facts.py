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
module: oci_os_management_managed_instance_facts
short_description: Fetches details about one or multiple ManagedInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagedInstance resources in Oracle Cloud Infrastructure
    - Returns a list of all Managed Instances.
    - If I(managed_instance_id) is specified, the details of a single ManagedInstance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_instance_id:
        description:
            - OCID for the managed instance
            - Required to get a specific managed_instance.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple managed_instances.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is
              ascending. If no value is specified TIMECREATED is default.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    os_family:
        description:
            - The OS family for which to list resources.
        type: str
        choices:
            - "LINUX"
            - "WINDOWS"
            - "ALL"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific managed_instance
  oci_os_management_managed_instance_facts:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List managed_instances
  oci_os_management_managed_instance_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_order: ASC
    sort_by: TIMECREATED
    os_family: LINUX

"""

RETURN = """
managed_instances:
    description:
        - List of ManagedInstance resources
    returned: on success
    type: complex
    contains:
        os_name:
            description:
                - Operating System Name
                - Returned for get operation
            returned: on success
            type: str
            sample: os_name_example
        os_version:
            description:
                - Operating System Version
                - Returned for get operation
            returned: on success
            type: str
            sample: os_version_example
        os_kernel_version:
            description:
                - Operating System Kernel Version
                - Returned for get operation
            returned: on success
            type: str
            sample: os_kernel_version_example
        parent_software_source:
            description:
                - the parent (base) Software Source attached to the Managed Instance
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - software source name
                    returned: on success
                    type: str
                    sample: name_example
                id:
                    description:
                        - software source identifier
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        child_software_sources:
            description:
                - list of child Software Sources attached to the Managed Instance
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - software source name
                    returned: on success
                    type: str
                    sample: name_example
                id:
                    description:
                        - software source identifier
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        managed_instance_groups:
            description:
                - The ids of the managed instance groups of which this instance is a
                  member.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - unique identifier that is immutable on creation
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User friendly name
                    returned: on success
                    type: str
                    sample: display_name_example
        notification_topic_id:
            description:
                - OCID of the ONS topic used to send notification to users
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx"
        ksplice_effective_kernel_version:
            description:
                - The ksplice effective kernel version
                - Returned for get operation
            returned: on success
            type: str
            sample: ksplice_effective_kernel_version_example
        is_data_collection_authorized:
            description:
                - True if user allow data collection for this instance
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        autonomous:
            description:
                - if present, indicates the Managed Instance is an autonomous instance. Holds all the Autonomous specific information
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                is_auto_update_enabled:
                    description:
                        - True if daily updates are enabled
                    returned: on success
                    type: bool
                    sample: true
        security_updates_available:
            description:
                - Number of security type updates available to be installed
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        bug_updates_available:
            description:
                - Number of bug fix type updates available to be installed
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        enhancement_updates_available:
            description:
                - Number of enhancement type updates available to be installed
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        other_updates_available:
            description:
                - Number of non-classified updates available to be installed
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        scheduled_job_count:
            description:
                - Number of scheduled jobs associated with this instance
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        work_request_count:
            description:
                - Number of work requests associated with this instance
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        display_name:
            description:
                - Managed Instance identifier
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - OCID for the managed instance
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        last_checkin:
            description:
                - Time at which the instance last checked in
            returned: on success
            type: str
            sample: last_checkin_example
        last_boot:
            description:
                - Time at which the instance last booted
            returned: on success
            type: str
            sample: last_boot_example
        updates_available:
            description:
                - Number of updates available to be installed
            returned: on success
            type: int
            sample: 56
        compartment_id:
            description:
                - OCID for the Compartment
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Information specified by the user about the managed instance
            returned: on success
            type: str
            sample: description_example
        status:
            description:
                - status of the managed instance.
            returned: on success
            type: str
            sample: NORMAL
        os_family:
            description:
                - The Operating System type of the managed instance.
            returned: on success
            type: str
            sample: LINUX
        is_reboot_required:
            description:
                - Indicates whether a reboot is required to complete installation of updates.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "os_name": "os_name_example",
        "os_version": "os_version_example",
        "os_kernel_version": "os_kernel_version_example",
        "parent_software_source": {
            "name": "name_example",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "child_software_sources": [{
            "name": "name_example",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "managed_instance_groups": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "notification_topic_id": "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx",
        "ksplice_effective_kernel_version": "ksplice_effective_kernel_version_example",
        "is_data_collection_authorized": true,
        "autonomous": {
            "is_auto_update_enabled": true
        },
        "security_updates_available": 56,
        "bug_updates_available": 56,
        "enhancement_updates_available": 56,
        "other_updates_available": 56,
        "scheduled_job_count": 56,
        "work_request_count": 56,
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "last_checkin": "last_checkin_example",
        "last_boot": "last_boot_example",
        "updates_available": 56,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "status": "NORMAL",
        "os_family": "LINUX",
        "is_reboot_required": true
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management import OsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "managed_instance_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_instance,
            managed_instance_id=self.module.params.get("managed_instance_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_order",
            "sort_by",
            "os_family",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_managed_instances,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ManagedInstanceFactsHelperCustom = get_custom_class("ManagedInstanceFactsHelperCustom")


class ResourceFactsHelper(
    ManagedInstanceFactsHelperCustom, ManagedInstanceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_instance_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            os_family=dict(type="str", choices=["LINUX", "WINDOWS", "ALL"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="managed_instance",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(managed_instances=result)


if __name__ == "__main__":
    main()
