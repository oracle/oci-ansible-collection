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
module: oci_os_management_hub_software_source_change_availability_actions
short_description: Perform actions on a SoftwareSourceChangeAvailability resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a SoftwareSourceChangeAvailability resource in Oracle Cloud Infrastructure
    - For I(action=change_availability_of_software_sources), updates the availability for a list of specified software sources.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    software_source_availabilities:
        description:
            - List of vendor software sources and their availability statuses.
        type: list
        elements: dict
        required: true
        suboptions:
            software_source_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the vendor software source.
                type: str
                required: true
            availability:
                description:
                    - Availability of the software source to instances in private data centers or third-party clouds.
                type: str
                choices:
                    - "AVAILABLE"
                    - "SELECTED"
                    - "RESTRICTED"
                    - "UNAVAILABLE"
            availability_at_oci:
                description:
                    - Availability of the software source to OCI instances.
                type: str
                choices:
                    - "AVAILABLE"
                    - "SELECTED"
                    - "RESTRICTED"
                    - "UNAVAILABLE"
    action:
        description:
            - The action to perform on the SoftwareSourceChangeAvailability.
        type: str
        required: true
        choices:
            - "change_availability_of_software_sources"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_availability_of_software_sources on software_source_change_availability
  oci_os_management_hub_software_source_change_availability_actions:
    # required
    software_source_availabilities:
    - # required
      software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      availability: AVAILABLE
      availability_at_oci: AVAILABLE
    action: change_availability_of_software_sources

"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.os_management_hub import SoftwareSourceClient
    from oci.os_management_hub.models import ChangeAvailabilityOfSoftwareSourcesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubSoftwareSourceChangeAvailabilityActionsHelperGen(
    OCIActionsHelperBase
):
    """
    Supported actions:
        change_availability_of_software_sources
    """

    def change_availability_of_software_sources(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeAvailabilityOfSoftwareSourcesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_availability_of_software_sources,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_availability_of_software_sources_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


OsManagementHubSoftwareSourceChangeAvailabilityActionsHelperCustom = get_custom_class(
    "OsManagementHubSoftwareSourceChangeAvailabilityActionsHelperCustom"
)


class ResourceHelper(
    OsManagementHubSoftwareSourceChangeAvailabilityActionsHelperCustom,
    OsManagementHubSoftwareSourceChangeAvailabilityActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            software_source_availabilities=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    software_source_id=dict(type="str", required=True),
                    availability=dict(
                        type="str",
                        choices=["AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"],
                    ),
                    availability_at_oci=dict(
                        type="str",
                        choices=["AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"],
                    ),
                ),
            ),
            action=dict(
                type="str",
                required=True,
                choices=["change_availability_of_software_sources"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="software_source_change_availability",
        service_client_class=SoftwareSourceClient,
        namespace="os_management_hub",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
