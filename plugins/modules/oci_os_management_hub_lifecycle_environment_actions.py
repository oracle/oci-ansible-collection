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
module: oci_os_management_hub_lifecycle_environment_actions
short_description: Perform actions on a LifecycleEnvironment resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a LifecycleEnvironment resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a lifecycle environment into a different compartment within the same tenancy. For information about moving
      resources between compartments, see L(Moving Resources to a Different
      Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    lifecycle_environment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the lifecycle environment.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to move the lifecycle environment to.
        type: str
    action:
        description:
            - The action to perform on the LifecycleEnvironment.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on lifecycle_environment
  oci_os_management_hub_lifecycle_environment_actions:
    # required
    lifecycle_environment_id: "ocid1.lifecycleenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
lifecycle_environment:
    description:
        - Details of the LifecycleEnvironment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the lifecycle environment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the lifecycle
                  environment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the lifecycle environment.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - User-specified information about the lifecycle environment.
            returned: on success
            type: str
            sample: description_example
        stages:
            description:
                - User-specified list of lifecycle stages used within the lifecycle environment.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the lifecycle stage.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the lifecycle
                          stage.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - The user-friendly name for the lifecycle stage.
                    returned: on success
                    type: str
                    sample: display_name_example
                lifecycle_environment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the lifecycle environment that contains the
                          lifecycle stage.
                    returned: on success
                    type: str
                    sample: "ocid1.lifecycleenvironment.oc1..xxxxxxEXAMPLExxxxxx"
                rank:
                    description:
                        - User-specified rank for the lifecycle stage. Rank determines the hierarchy of the lifecycle stages within the lifecycle environment.
                    returned: on success
                    type: int
                    sample: 56
                os_family:
                    description:
                        - The operating system of the managed instances in the lifecycle stage.
                    returned: on success
                    type: str
                    sample: ORACLE_LINUX_9
                arch_type:
                    description:
                        - The CPU architecture of the managed instances in the lifecycle stage.
                    returned: on success
                    type: str
                    sample: X86_64
                vendor_name:
                    description:
                        - The vendor of the operating system used by the managed instances in the lifecycle stage.
                    returned: on success
                    type: str
                    sample: ORACLE
                managed_instance_ids:
                    description:
                        - The list of managed instances associated with the lifecycle stage.
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - Managed instance name.
                            returned: on success
                            type: str
                            sample: display_name_example
                location:
                    description:
                        - The location of managed instances associated with the lifecycle stage.
                    returned: on success
                    type: str
                    sample: ON_PREMISE
                software_source_id:
                    description:
                        - ""
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
                time_created:
                    description:
                        - The time the lifecycle stage was created (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_modified:
                    description:
                        - The time the lifecycle stage was last modified (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                lifecycle_state:
                    description:
                        - The current state of the lifecycle stage.
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
        managed_instance_ids:
            description:
                - List of managed instance L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) assigned to the lifecycle stage.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Managed instance name.
                    returned: on success
                    type: str
                    sample: display_name_example
        lifecycle_state:
            description:
                - The current state of the lifecycle environment.
            returned: on success
            type: str
            sample: CREATING
        os_family:
            description:
                - The operating system of the managed instances in the lifecycle environment.
            returned: on success
            type: str
            sample: ORACLE_LINUX_9
        arch_type:
            description:
                - The CPU architecture of the managed instances in the lifecycle environment.
            returned: on success
            type: str
            sample: X86_64
        vendor_name:
            description:
                - The vendor of the operating system used by the managed instances in the lifecycle environment.
            returned: on success
            type: str
            sample: ORACLE
        location:
            description:
                - The location of managed instances attached to the lifecycle environment.
            returned: on success
            type: str
            sample: ON_PREMISE
        time_created:
            description:
                - The time the lifecycle environment was created (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_modified:
            description:
                - The time the lifecycle environment was last modified (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "stages": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "lifecycle_environment_id": "ocid1.lifecycleenvironment.oc1..xxxxxxEXAMPLExxxxxx",
            "rank": 56,
            "os_family": "ORACLE_LINUX_9",
            "arch_type": "X86_64",
            "vendor_name": "ORACLE",
            "managed_instance_ids": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "display_name": "display_name_example"
            }],
            "location": "ON_PREMISE",
            "software_source_id": {
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "display_name": "display_name_example",
                "description": "description_example",
                "software_source_type": "VENDOR",
                "is_mandatory_for_autonomous_linux": true
            },
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_modified": "2013-10-20T19:20:30+01:00",
            "lifecycle_state": "CREATING",
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}},
            "system_tags": {}
        }],
        "managed_instance_ids": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "lifecycle_state": "CREATING",
        "os_family": "ORACLE_LINUX_9",
        "arch_type": "X86_64",
        "vendor_name": "ORACLE",
        "location": "ON_PREMISE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_modified": "2013-10-20T19:20:30+01:00",
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
    from oci.os_management_hub import LifecycleEnvironmentClient
    from oci.os_management_hub.models import (
        ChangeLifecycleEnvironmentCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubLifecycleEnvironmentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "lifecycle_environment_id"

    def get_module_resource_id(self):
        return self.module.params.get("lifecycle_environment_id")

    def get_get_fn(self):
        return self.client.get_lifecycle_environment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_lifecycle_environment,
            lifecycle_environment_id=self.module.params.get("lifecycle_environment_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeLifecycleEnvironmentCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_lifecycle_environment_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                lifecycle_environment_id=self.module.params.get(
                    "lifecycle_environment_id"
                ),
                change_lifecycle_environment_compartment_details=action_details,
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


OsManagementHubLifecycleEnvironmentActionsHelperCustom = get_custom_class(
    "OsManagementHubLifecycleEnvironmentActionsHelperCustom"
)


class ResourceHelper(
    OsManagementHubLifecycleEnvironmentActionsHelperCustom,
    OsManagementHubLifecycleEnvironmentActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            lifecycle_environment_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="lifecycle_environment",
        service_client_class=LifecycleEnvironmentClient,
        namespace="os_management_hub",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
