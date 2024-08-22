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
module: oci_os_management_hub_lifecycle_environment
short_description: Manage a LifecycleEnvironment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a LifecycleEnvironment resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a lifecycle environment. A lifecycle environment is a user-defined pipeline to deliver curated, versioned content in a
      prescribed, methodical manner.
    - "This resource has the following action operations in the M(oracle.oci.oci_os_management_hub_lifecycle_environment_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the lifecycle
              environment.
            - Required for create using I(state=present).
        type: str
    arch_type:
        description:
            - The CPU architecture of the managed instances in the lifecycle environment.
            - Required for create using I(state=present).
        type: str
        choices:
            - "X86_64"
            - "AARCH64"
            - "I686"
            - "NOARCH"
            - "SRC"
    os_family:
        description:
            - The operating system of the managed instances in the lifecycle environment.
            - Required for create using I(state=present).
        type: str
        choices:
            - "ORACLE_LINUX_9"
            - "ORACLE_LINUX_8"
            - "ORACLE_LINUX_7"
            - "ORACLE_LINUX_6"
            - "WINDOWS_SERVER_2016"
            - "WINDOWS_SERVER_2019"
            - "WINDOWS_SERVER_2022"
            - "ALL"
    vendor_name:
        description:
            - The vendor of the operating system used by the managed instances in the lifecycle environment.
            - Required for create using I(state=present).
        type: str
        choices:
            - "ORACLE"
            - "MICROSOFT"
    location:
        description:
            - The location of managed instances attached to the lifecycle environment. If no location is provided, the default is 'ON_PREMISE.'
        type: str
        choices:
            - "ON_PREMISE"
            - "OCI_COMPUTE"
            - "AZURE"
            - "EC2"
            - "GCP"
    display_name:
        description:
            - A user-friendly name for the lifecycle environment. Does not have to be unique and you can change the name later. Avoid entering confidential
              information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - User-specified information about the lifecycle environment. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    stages:
        description:
            - User-specified list of ranked lifecycle stages used within the lifecycle environment.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            rank:
                description:
                    - User-specified rank for the lifecycle stage. Rank determines the hierarchy of the lifecycle stages within the lifecycle environment.
                type: int
            id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the lifecycle stage.
                    - This parameter is updatable.
                type: str
            display_name:
                description:
                    - A user-friendly name for the lifecycle stage. Does not have to be unique and you can change the name later. Avoid entering confidential
                      information.
                    - This parameter is updatable.
                type: str
                aliases: ["name"]
            freeform_tags:
                description:
                    - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                      For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                      Example: `{\\"Department\\": \\"Finance\\"}`"
                    - This parameter is updatable.
                type: dict
            defined_tags:
                description:
                    - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                      For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                      Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                    - This parameter is updatable.
                type: dict
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    lifecycle_environment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the lifecycle environment.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the LifecycleEnvironment.
            - Use I(state=present) to create or update a LifecycleEnvironment.
            - Use I(state=absent) to delete a LifecycleEnvironment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create lifecycle_environment
  oci_os_management_hub_lifecycle_environment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    arch_type: X86_64
    os_family: ORACLE_LINUX_9
    vendor_name: ORACLE
    display_name: display_name_example
    stages:
    - # optional
      rank: 56
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      display_name: display_name_example
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}

    # optional
    location: ON_PREMISE
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update lifecycle_environment
  oci_os_management_hub_lifecycle_environment:
    # required
    lifecycle_environment_id: "ocid1.lifecycleenvironment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    stages:
    - # optional
      rank: 56
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      display_name: display_name_example
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update lifecycle_environment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_hub_lifecycle_environment:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    stages:
    - # optional
      rank: 56
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      display_name: display_name_example
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete lifecycle_environment
  oci_os_management_hub_lifecycle_environment:
    # required
    lifecycle_environment_id: "ocid1.lifecycleenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete lifecycle_environment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_hub_lifecycle_environment:
    # required
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import LifecycleEnvironmentClient
    from oci.os_management_hub.models import CreateLifecycleEnvironmentDetails
    from oci.os_management_hub.models import UpdateLifecycleEnvironmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LifecycleEnvironmentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            LifecycleEnvironmentHelperGen, self
        ).get_possible_entity_types() + [
            "osmhlifecycleenvironment",
            "osmhlifecycleenvironments",
            "osManagementHubosmhlifecycleenvironment",
            "osManagementHubosmhlifecycleenvironments",
            "osmhlifecycleenvironmentresource",
            "osmhlifecycleenvironmentsresource",
            "lifecycleenvironment",
            "lifecycleenvironments",
            "osManagementHublifecycleenvironment",
            "osManagementHublifecycleenvironments",
            "lifecycleenvironmentresource",
            "lifecycleenvironmentsresource",
            "osmanagementhub",
        ]

    def get_module_resource_id_param(self):
        return "lifecycle_environment_id"

    def get_module_resource_id(self):
        return self.module.params.get("lifecycle_environment_id")

    def get_get_fn(self):
        return self.client.get_lifecycle_environment

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_lifecycle_environment,
            lifecycle_environment_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_lifecycle_environment,
            lifecycle_environment_id=self.module.params.get("lifecycle_environment_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "compartment_id",
            "lifecycle_environment_id",
            "arch_type",
            "os_family",
        ]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_lifecycle_environments, **kwargs
        )

    def get_create_model_class(self):
        return CreateLifecycleEnvironmentDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_lifecycle_environment,
            call_fn_args=(),
            call_fn_kwargs=dict(create_lifecycle_environment_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateLifecycleEnvironmentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_lifecycle_environment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                lifecycle_environment_id=self.module.params.get(
                    "lifecycle_environment_id"
                ),
                update_lifecycle_environment_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_lifecycle_environment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                lifecycle_environment_id=self.module.params.get(
                    "lifecycle_environment_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


LifecycleEnvironmentHelperCustom = get_custom_class("LifecycleEnvironmentHelperCustom")


class ResourceHelper(LifecycleEnvironmentHelperCustom, LifecycleEnvironmentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            arch_type=dict(
                type="str", choices=["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
            ),
            os_family=dict(
                type="str",
                choices=[
                    "ORACLE_LINUX_9",
                    "ORACLE_LINUX_8",
                    "ORACLE_LINUX_7",
                    "ORACLE_LINUX_6",
                    "WINDOWS_SERVER_2016",
                    "WINDOWS_SERVER_2019",
                    "WINDOWS_SERVER_2022",
                    "ALL",
                ],
            ),
            vendor_name=dict(type="str", choices=["ORACLE", "MICROSOFT"]),
            location=dict(
                type="str", choices=["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]
            ),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            stages=dict(
                type="list",
                elements="dict",
                options=dict(
                    rank=dict(type="int"),
                    id=dict(type="str"),
                    display_name=dict(aliases=["name"], type="str"),
                    freeform_tags=dict(type="dict"),
                    defined_tags=dict(type="dict"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            lifecycle_environment_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
