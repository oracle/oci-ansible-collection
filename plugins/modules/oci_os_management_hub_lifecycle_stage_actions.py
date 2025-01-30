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
module: oci_os_management_hub_lifecycle_stage_actions
short_description: Perform actions on a LifecycleStage resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a LifecycleStage resource in Oracle Cloud Infrastructure
    - For I(action=attach_managed_instances), attaches (adds) managed instances to a lifecycle stage. Once added, you can apply operations to all managed
      instances in the lifecycle stage.
    - For I(action=detach_managed_instances), detaches (removes) a managed instance from a lifecycle stage.
    - For I(action=promote_software_source), updates the versioned custom software source content to the specified lifecycle stage.
      A versioned custom software source OCID (softwareSourceId) is required when promoting content to the first lifecycle stage. You must promote content to
      the first stage before promoting to subsequent stages, otherwise the service returns an error.
      The softwareSourceId is optional when promoting content to the second, third, forth, or fifth stages. If you provide a softwareSourceId, the service
      validates that it matches the softwareSourceId of the previous stage. If it does not match, the service returns an error. If you don't provide a
      softwareSourceId, the service promotes the versioned software source from the previous lifecycle stage. If the previous lifecycle stage has no software
      source, the service returns an error.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_instance_details:
        description:
            - ""
            - Applicable only for I(action=attach_managed_instances)I(action=detach_managed_instances).
        type: dict
        suboptions:
            managed_instances:
                description:
                    - The list of managed instance OCIDs to be attached/detached.
                type: list
                elements: str
                required: true
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
    lifecycle_stage_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the lifecycle stage.
        type: str
        aliases: ["id"]
        required: true
    work_request_details:
        description:
            - ""
            - Applicable only for I(action=promote_software_source).
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
    software_source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source. This filter returns resources
              associated with this software source.
            - Applicable only for I(action=promote_software_source).
        type: str
    action:
        description:
            - The action to perform on the LifecycleStage.
        type: str
        required: true
        choices:
            - "attach_managed_instances"
            - "detach_managed_instances"
            - "promote_software_source"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action attach_managed_instances on lifecycle_stage
  oci_os_management_hub_lifecycle_stage_actions:
    # required
    lifecycle_stage_id: "ocid1.lifecyclestage.oc1..xxxxxxEXAMPLExxxxxx"
    action: attach_managed_instances

    # optional
    managed_instance_details:
      # required
      managed_instances: [ "managed_instances_example" ]

      # optional
      work_request_details:
        # optional
        display_name: display_name_example
        description: description_example

- name: Perform action detach_managed_instances on lifecycle_stage
  oci_os_management_hub_lifecycle_stage_actions:
    # required
    lifecycle_stage_id: "ocid1.lifecyclestage.oc1..xxxxxxEXAMPLExxxxxx"
    action: detach_managed_instances

    # optional
    managed_instance_details:
      # required
      managed_instances: [ "managed_instances_example" ]

      # optional
      work_request_details:
        # optional
        display_name: display_name_example
        description: description_example

- name: Perform action promote_software_source on lifecycle_stage
  oci_os_management_hub_lifecycle_stage_actions:
    # required
    lifecycle_stage_id: "ocid1.lifecyclestage.oc1..xxxxxxEXAMPLExxxxxx"
    action: promote_software_source

    # optional
    work_request_details:
      # optional
      display_name: display_name_example
      description: description_example
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
lifecycle_stage:
    description:
        - Details of the LifecycleStage resource acted upon by the current operation
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
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the lifecycle stage.
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
    sample: {
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
    }
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
    from oci.os_management_hub import LifecycleEnvironmentClient
    from oci.os_management_hub.models import (
        AttachManagedInstancesToLifecycleStageDetails,
    )
    from oci.os_management_hub.models import (
        DetachManagedInstancesFromLifecycleStageDetails,
    )
    from oci.os_management_hub.models import (
        PromoteSoftwareSourceToLifecycleStageDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubLifecycleStageActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        attach_managed_instances
        detach_managed_instances
        promote_software_source
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "lifecycle_stage_id"

    def get_module_resource_id(self):
        return self.module.params.get("lifecycle_stage_id")

    def get_get_fn(self):
        return self.client.get_lifecycle_stage

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_lifecycle_stage,
            lifecycle_stage_id=self.module.params.get("lifecycle_stage_id"),
        )

    def attach_managed_instances(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AttachManagedInstancesToLifecycleStageDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_managed_instances_to_lifecycle_stage,
            call_fn_args=(),
            call_fn_kwargs=dict(
                lifecycle_stage_id=self.module.params.get("lifecycle_stage_id"),
                attach_managed_instances_to_lifecycle_stage_details=action_details,
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

    def detach_managed_instances(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetachManagedInstancesFromLifecycleStageDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_managed_instances_from_lifecycle_stage,
            call_fn_args=(),
            call_fn_kwargs=dict(
                lifecycle_stage_id=self.module.params.get("lifecycle_stage_id"),
                detach_managed_instances_from_lifecycle_stage_details=action_details,
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

    def promote_software_source(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, PromoteSoftwareSourceToLifecycleStageDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.promote_software_source_to_lifecycle_stage,
            call_fn_args=(),
            call_fn_kwargs=dict(
                lifecycle_stage_id=self.module.params.get("lifecycle_stage_id"),
                promote_software_source_to_lifecycle_stage_details=action_details,
                software_source_id=self.module.params.get("software_source_id"),
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


OsManagementHubLifecycleStageActionsHelperCustom = get_custom_class(
    "OsManagementHubLifecycleStageActionsHelperCustom"
)


class ResourceHelper(
    OsManagementHubLifecycleStageActionsHelperCustom,
    OsManagementHubLifecycleStageActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            managed_instance_details=dict(
                type="dict",
                options=dict(
                    managed_instances=dict(type="list", elements="str", required=True),
                    work_request_details=dict(
                        type="dict",
                        options=dict(
                            display_name=dict(aliases=["name"], type="str"),
                            description=dict(type="str"),
                        ),
                    ),
                ),
            ),
            lifecycle_stage_id=dict(aliases=["id"], type="str", required=True),
            work_request_details=dict(
                type="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str"),
                    description=dict(type="str"),
                ),
            ),
            software_source_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "attach_managed_instances",
                    "detach_managed_instances",
                    "promote_software_source",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="lifecycle_stage",
        service_client_class=LifecycleEnvironmentClient,
        namespace="os_management_hub",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
