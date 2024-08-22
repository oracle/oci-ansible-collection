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
module: oci_os_management_hub_profile_facts
short_description: Fetches details about one or multiple Profile resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Profile resources in Oracle Cloud Infrastructure
    - Lists registration profiles that match the specified compartment or profile OCID. Filter the list against a
      variety of criteria including but not limited to its name, status, vendor name, and architecture type.
    - If I(profile_id) is specified, the details of a single Profile will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
        type: str
    display_name:
        description:
            - A filter to return resources that match the given display names.
        type: list
        elements: str
        aliases: ["name"]
    display_name_contains:
        description:
            - A filter to return resources that may partially match the given display name.
        type: str
    profile_type:
        description:
            - A filter to return registration profiles that match the given profile type.
        type: list
        elements: str
        choices:
            - "SOFTWARESOURCE"
            - "GROUP"
            - "LIFECYCLE"
            - "STATION"
            - "WINDOWS_STANDALONE"
    profile_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the registration profile.
            - Required to get a specific profile.
        type: str
        aliases: ["id"]
    os_family:
        description:
            - A filter to return only resources that match the given operating system family.
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
            - A filter to return only profiles that match the given archType.
        type: str
        choices:
            - "X86_64"
            - "AARCH64"
            - "I686"
            - "NOARCH"
            - "SRC"
    registration_type:
        description:
            - A filter to return profiles that match the given instance type.
        type: list
        elements: str
    is_default_profile:
        description:
            - A boolean variable that is used to list only the default profile resources.
        type: bool
    is_service_provided_profile:
        description:
            - A filter to return only service-provided profiles.
        type: bool
    vendor_name:
        description:
            - A filter to return only resources that match the given vendor name.
        type: str
        choices:
            - "ORACLE"
            - "MICROSOFT"
    lifecycle_state:
        description:
            - A filter to return only registration profiles in the given state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided.
              Default order for timeCreated is descending.
              Default order for displayName is ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific profile
  oci_os_management_hub_profile_facts:
    # required
    profile_id: "ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx"

- name: List profiles
  oci_os_management_hub_profile_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: [ "display_name_example" ]
    display_name_contains: display_name_contains_example
    profile_type: [ "SOFTWARESOURCE" ]
    profile_id: "ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx"
    os_family: ORACLE_LINUX_9
    arch_type: X86_64
    registration_type: [ "registration_type_example" ]
    is_default_profile: true
    is_service_provided_profile: true
    vendor_name: ORACLE
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
profiles:
    description:
        - List of Profile resources
    returned: on success
    type: complex
    contains:
        managed_instance_group:
            description:
                - ""
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
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
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the registration
                  profile.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
        registration_type:
            description:
                - The type of instance to register.
            returned: on success
            type: str
            sample: OCI_LINUX
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
    sample: [{
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
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "management_station_id": "ocid1.managementstation.oc1..xxxxxxEXAMPLExxxxxx",
        "profile_type": "SOFTWARESOURCE",
        "registration_type": "OCI_LINUX",
        "vendor_name": "ORACLE",
        "os_family": "ORACLE_LINUX_9",
        "arch_type": "X86_64",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "is_default_profile": true,
        "is_service_provided_profile": true,
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
    from oci.os_management_hub import OnboardingClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProfileFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "profile_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_profile, profile_id=self.module.params.get("profile_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "display_name_contains",
            "profile_type",
            "profile_id",
            "os_family",
            "arch_type",
            "registration_type",
            "is_default_profile",
            "is_service_provided_profile",
            "vendor_name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_profiles, **optional_kwargs
        )


ProfileFactsHelperCustom = get_custom_class("ProfileFactsHelperCustom")


class ResourceFactsHelper(ProfileFactsHelperCustom, ProfileFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="list", elements="str"),
            display_name_contains=dict(type="str"),
            profile_type=dict(
                type="list",
                elements="str",
                choices=[
                    "SOFTWARESOURCE",
                    "GROUP",
                    "LIFECYCLE",
                    "STATION",
                    "WINDOWS_STANDALONE",
                ],
            ),
            profile_id=dict(aliases=["id"], type="str"),
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
            registration_type=dict(type="list", elements="str"),
            is_default_profile=dict(type="bool"),
            is_service_provided_profile=dict(type="bool"),
            vendor_name=dict(type="str", choices=["ORACLE", "MICROSOFT"]),
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
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="profile",
        service_client_class=OnboardingClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(profiles=result)


if __name__ == "__main__":
    main()
