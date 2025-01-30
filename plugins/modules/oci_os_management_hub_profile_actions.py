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
module: oci_os_management_hub_profile_actions
short_description: Perform actions on a Profile resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Profile resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the profile to a different compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    profile_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the registration profile.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the profile to.
        type: str
    action:
        description:
            - The action to perform on the Profile.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on profile
  oci_os_management_hub_profile_actions:
    # required
    profile_id: "ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
profile:
    description:
        - Details of the Profile resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        managed_instance_group:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Managed instance group name.
                    returned: on success
                    type: str
                    sample: display_name_example
        lifecycle_environment:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the lifecycle environment.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Lifecycle environment name.
                    returned: on success
                    type: str
                    sample: display_name_example
        lifecycle_stage:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the lifecycle stage.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Lifecycle stage name.
                    returned: on success
                    type: str
                    sample: display_name_example
        software_sources:
            description:
                - The list of software sources that the registration profile will use.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Software source name.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Software source description.
                    returned: on success
                    type: str
                    sample: description_example
                software_source_type:
                    description:
                        - Type of the software source.
                    returned: on success
                    type: str
                    sample: VENDOR
                is_mandatory_for_autonomous_linux:
                    description:
                        - Indicates whether this is a required software source for Autonomous Linux instances. If true, the user can't unselect it.
                    returned: on success
                    type: bool
                    sample: true
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the registration profile.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the registration
                  profile.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name for the profile.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The description of the registration profile.
            returned: on success
            type: str
            sample: description_example
        management_station_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station to associate with an
                  instance once registered. Associating with a management station applies only to non-OCI instances.
            returned: on success
            type: str
            sample: "ocid1.managementstation.oc1..xxxxxxEXAMPLExxxxxx"
        profile_type:
            description:
                - The type of profile.
            returned: on success
            type: str
            sample: SOFTWARESOURCE
        vendor_name:
            description:
                - The vendor of the operating system for the instance.
            returned: on success
            type: str
            sample: ORACLE
        os_family:
            description:
                - The operating system family.
            returned: on success
            type: str
            sample: ORACLE_LINUX_9
        arch_type:
            description:
                - The architecture type.
            returned: on success
            type: str
            sample: X86_64
        time_created:
            description:
                - The time the registration profile was created (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the registration profile.
            returned: on success
            type: str
            sample: CREATING
        registration_type:
            description:
                - The type of instance to register.
            returned: on success
            type: str
            sample: OCI_LINUX
        is_default_profile:
            description:
                - Indicates if the profile is set as the default. There is exactly one default profile for a specified architecture, OS family, registration
                  type, and vendor. When registering an instance with the corresonding characteristics, the default profile is used, unless another profile is
                  specified.
            returned: on success
            type: bool
            sample: true
        is_service_provided_profile:
            description:
                - Indicates if the profile was created by the service. OS Management Hub provides a limited set of standardized profiles that can be used to
                  register Autonomous Linux or Windows instances.
            returned: on success
            type: bool
            sample: true
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
    sample: {
        "managed_instance_group": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        },
        "lifecycle_environment": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        },
        "lifecycle_stage": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        },
        "software_sources": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "software_source_type": "VENDOR",
            "is_mandatory_for_autonomous_linux": true
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "management_station_id": "ocid1.managementstation.oc1..xxxxxxEXAMPLExxxxxx",
        "profile_type": "SOFTWARESOURCE",
        "vendor_name": "ORACLE",
        "os_family": "ORACLE_LINUX_9",
        "arch_type": "X86_64",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "registration_type": "OCI_LINUX",
        "is_default_profile": true,
        "is_service_provided_profile": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
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
    from oci.os_management_hub import OnboardingClient
    from oci.os_management_hub.models import ChangeProfileCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubProfileActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "profile_id"

    def get_module_resource_id(self):
        return self.module.params.get("profile_id")

    def get_get_fn(self):
        return self.client.get_profile

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_profile, profile_id=self.module.params.get("profile_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeProfileCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_profile_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                profile_id=self.module.params.get("profile_id"),
                change_profile_compartment_details=action_details,
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


OsManagementHubProfileActionsHelperCustom = get_custom_class(
    "OsManagementHubProfileActionsHelperCustom"
)


class ResourceHelper(
    OsManagementHubProfileActionsHelperCustom, OsManagementHubProfileActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            profile_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="profile",
        service_client_class=OnboardingClient,
        namespace="os_management_hub",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
