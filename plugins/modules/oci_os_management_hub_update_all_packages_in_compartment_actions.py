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
module: oci_os_management_hub_update_all_packages_in_compartment_actions
short_description: Perform actions on an UpdateAllPackagesInCompartment resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an UpdateAllPackagesInCompartment resource in Oracle Cloud Infrastructure
    - For I(action=update_all_packages_on_managed_instances_in_compartment), install all of the available package updates for all of the managed instances in a
      compartment. This applies only to standalone non-Windows instances. This will not update instances that belong to a group or lifecycle environment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    update_types:
        description:
            - The types of updates to be applied.
        type: list
        elements: str
        choices:
            - "SECURITY"
            - "BUGFIX"
            - "ENHANCEMENT"
            - "OTHER"
            - "KSPLICE_KERNEL"
            - "KSPLICE_USERSPACE"
            - "ALL"
    work_request_details:
        description:
            - ""
        type: dict
        suboptions:
            display_name:
                description:
                    - A user-friendly name for the job. The name does not have to be unique. Avoid entering confidential information.
                type: str
                aliases: ["name"]
            description:
                description:
                    - User-specified information about the job. Avoid entering confidential information.
                type: str
    action:
        description:
            - The action to perform on the UpdateAllPackagesInCompartment.
        type: str
        required: true
        choices:
            - "update_all_packages_on_managed_instances_in_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action update_all_packages_on_managed_instances_in_compartment on update_all_packages_in_compartment
  oci_os_management_hub_update_all_packages_in_compartment_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: update_all_packages_on_managed_instances_in_compartment

    # optional
    update_types: [ "SECURITY" ]
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example

"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.os_management_hub import WorkRequestClient
    from oci.os_management_hub import ManagedInstanceClient
    from oci.os_management_hub.models import (
        UpdateAllPackagesOnManagedInstancesInCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubUpdateAllPackagesInCompartmentActionsHelperGen(
    OCIActionsHelperBase
):
    """
    Supported actions:
        update_all_packages_on_managed_instances_in_compartment
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def update_all_packages_on_managed_instances_in_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpdateAllPackagesOnManagedInstancesInCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_all_packages_on_managed_instances_in_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_all_packages_on_managed_instances_in_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OsManagementHubUpdateAllPackagesInCompartmentActionsHelperCustom = get_custom_class(
    "OsManagementHubUpdateAllPackagesInCompartmentActionsHelperCustom"
)


class ResourceHelper(
    OsManagementHubUpdateAllPackagesInCompartmentActionsHelperCustom,
    OsManagementHubUpdateAllPackagesInCompartmentActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            update_types=dict(
                type="list",
                elements="str",
                choices=[
                    "SECURITY",
                    "BUGFIX",
                    "ENHANCEMENT",
                    "OTHER",
                    "KSPLICE_KERNEL",
                    "KSPLICE_USERSPACE",
                    "ALL",
                ],
            ),
            work_request_details=dict(
                type="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str"),
                    description=dict(type="str"),
                ),
            ),
            action=dict(
                type="str",
                required=True,
                choices=["update_all_packages_on_managed_instances_in_compartment"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="update_all_packages_in_compartment",
        service_client_class=ManagedInstanceClient,
        namespace="os_management_hub",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
