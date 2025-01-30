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
module: oci_os_management_hub_profile
short_description: Manage a Profile resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Profile resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a registration profile. A profile defines the content applied to the instance when registering it with the service.
    - "This resource has the following action operations in the M(oracle.oci.oci_os_management_hub_profile_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_instance_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group that the instance will join
              after registration.
            - Required when profile_type is 'GROUP'
        type: str
    vendor_name:
        description:
            - The vendor of the operating system for the instance.
            - Applicable when profile_type is 'STATION'
            - Required when profile_type is 'SOFTWARESOURCE'
        type: str
        choices:
            - "ORACLE"
            - "MICROSOFT"
    os_family:
        description:
            - The operating system family.
            - Applicable when profile_type is 'STATION'
            - Required when profile_type is 'SOFTWARESOURCE'
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
    arch_type:
        description:
            - The architecture type.
            - Applicable when profile_type is 'STATION'
            - Required when profile_type is 'SOFTWARESOURCE'
        type: str
        choices:
            - "X86_64"
            - "AARCH64"
            - "I686"
            - "NOARCH"
            - "SRC"
    software_source_ids:
        description:
            - The list of software source L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that the registration profile
              will use.
            - Applicable when profile_type is 'SOFTWARESOURCE'
        type: list
        elements: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the registration profile.
            - Required for create using I(state=present).
        type: str
    management_station_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station to associate with an instance
              once registered. Associating with a management station applies only to non-OCI instances.
        type: str
    profile_type:
        description:
            - The type of profile.
            - Required for create using I(state=present).
        type: str
        choices:
            - "GROUP"
            - "STATION"
            - "SOFTWARESOURCE"
            - "LIFECYCLE"
    registration_type:
        description:
            - The type of instance to register.
        type: str
    lifecycle_stage_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the lifecycle stage that the instance will be
              associated with.
            - Required when profile_type is 'LIFECYCLE'
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - User-specified description of the registration profile.
            - This parameter is updatable.
        type: str
    is_default_profile:
        description:
            - Indicates if the profile is set as the default. There is exactly one default profile for a specified architecture, OS family, registration type,
              and vendor. When registering an instance with the corresonding characteristics, the default profile is used, unless another profile is specified.
            - This parameter is updatable.
        type: bool
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
    profile_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the registration profile.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Profile.
            - Use I(state=present) to create or update a Profile.
            - Use I(state=absent) to delete a Profile.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create profile with profile_type = GROUP
  oci_os_management_hub_profile:
    # required
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    profile_type: GROUP
    display_name: display_name_example

    # optional
    management_station_id: "ocid1.managementstation.oc1..xxxxxxEXAMPLExxxxxx"
    registration_type: registration_type_example
    description: description_example
    is_default_profile: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create profile with profile_type = STATION
  oci_os_management_hub_profile:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    profile_type: STATION
    display_name: display_name_example

    # optional
    vendor_name: ORACLE
    os_family: ORACLE_LINUX_9
    arch_type: X86_64
    management_station_id: "ocid1.managementstation.oc1..xxxxxxEXAMPLExxxxxx"
    registration_type: registration_type_example
    description: description_example
    is_default_profile: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create profile with profile_type = SOFTWARESOURCE
  oci_os_management_hub_profile:
    # required
    vendor_name: ORACLE
    os_family: ORACLE_LINUX_9
    arch_type: X86_64
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    profile_type: SOFTWARESOURCE
    display_name: display_name_example

    # optional
    software_source_ids: [ "software_source_ids_example" ]
    management_station_id: "ocid1.managementstation.oc1..xxxxxxEXAMPLExxxxxx"
    registration_type: registration_type_example
    description: description_example
    is_default_profile: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create profile with profile_type = LIFECYCLE
  oci_os_management_hub_profile:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    profile_type: LIFECYCLE
    lifecycle_stage_id: "ocid1.lifecyclestage.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    management_station_id: "ocid1.managementstation.oc1..xxxxxxEXAMPLExxxxxx"
    registration_type: registration_type_example
    description: description_example
    is_default_profile: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update profile
  oci_os_management_hub_profile:
    # required
    profile_id: "ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    is_default_profile: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update profile using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_hub_profile:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    is_default_profile: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete profile
  oci_os_management_hub_profile:
    # required
    profile_id: "ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete profile using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_hub_profile:
    # required
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import OnboardingClient
    from oci.os_management_hub.models import CreateProfileDetails
    from oci.os_management_hub.models import UpdateProfileDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubProfileHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            OsManagementHubProfileHelperGen, self
        ).get_possible_entity_types() + [
            "profile",
            "profiles",
            "osManagementHubprofile",
            "osManagementHubprofiles",
            "profileresource",
            "profilesresource",
            "osmanagementhub",
        ]

    def get_module_resource_id_param(self):
        return "profile_id"

    def get_module_resource_id(self):
        return self.module.params.get("profile_id")

    def get_get_fn(self):
        return self.client.get_profile

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_profile, profile_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_profile, profile_id=self.module.params.get("profile_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["compartment_id", "profile_id", "os_family", "arch_type", "vendor_name"]
            if self._use_name_as_identifier()
            else [
                "compartment_id",
                "profile_id",
                "os_family",
                "arch_type",
                "is_default_profile",
                "vendor_name",
            ]
        )

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
        return oci_common_utils.list_all_resources(self.client.list_profiles, **kwargs)

    def get_create_model_class(self):
        return CreateProfileDetails

    def get_exclude_attributes(self):
        return [
            "lifecycle_stage_id",
            "software_source_ids",
            "managed_instance_group_id",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_profile,
            call_fn_args=(),
            call_fn_kwargs=dict(create_profile_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateProfileDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_profile,
            call_fn_args=(),
            call_fn_kwargs=dict(
                profile_id=self.module.params.get("profile_id"),
                update_profile_details=update_details,
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
            call_fn=self.client.delete_profile,
            call_fn_args=(),
            call_fn_kwargs=dict(profile_id=self.module.params.get("profile_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


OsManagementHubProfileHelperCustom = get_custom_class(
    "OsManagementHubProfileHelperCustom"
)


class ResourceHelper(
    OsManagementHubProfileHelperCustom, OsManagementHubProfileHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            managed_instance_group_id=dict(type="str"),
            vendor_name=dict(type="str", choices=["ORACLE", "MICROSOFT"]),
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
            arch_type=dict(
                type="str", choices=["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
            ),
            software_source_ids=dict(type="list", elements="str"),
            compartment_id=dict(type="str"),
            management_station_id=dict(type="str"),
            profile_type=dict(
                type="str", choices=["GROUP", "STATION", "SOFTWARESOURCE", "LIFECYCLE"]
            ),
            registration_type=dict(type="str"),
            lifecycle_stage_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            is_default_profile=dict(type="bool"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            profile_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
