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
module: oci_os_management_hub_lifecycle_environment_facts
short_description: Fetches details about one or multiple LifecycleEnvironment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LifecycleEnvironment resources in Oracle Cloud Infrastructure
    - Lists lifecycle environments that match the specified compartment or lifecycle environment OCID. Filter the list
      against a variety of criteria including but not limited to its name, status, architecture, and OS family.
    - If I(lifecycle_environment_id) is specified, the details of a single LifecycleEnvironment will be returned.
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
    lifecycle_environment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the lifecycle environment.
            - Required to get a specific lifecycle_environment.
        type: str
        aliases: ["id"]
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
    location:
        description:
            - A filter to return only resources whose location matches the given value.
        type: list
        elements: str
        choices:
            - "ON_PREMISE"
            - "OCI_COMPUTE"
            - "AZURE"
            - "EC2"
            - "GCP"
    location_not_equal_to:
        description:
            - A filter to return only resources whose location does not match the given value.
        type: list
        elements: str
        choices:
            - "ON_PREMISE"
            - "OCI_COMPUTE"
            - "AZURE"
            - "EC2"
            - "GCP"
    lifecycle_state:
        description:
            - A filter to return only the lifecycle environments that match the display name given.
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
              Default order for timeCreated is descending. Default order for displayName is ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific lifecycle_environment
  oci_os_management_hub_lifecycle_environment_facts:
    # required
    lifecycle_environment_id: "ocid1.lifecycleenvironment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List lifecycle_environments
  oci_os_management_hub_lifecycle_environment_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: [ "display_name_example" ]
    display_name_contains: display_name_contains_example
    lifecycle_environment_id: "ocid1.lifecycleenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    arch_type: X86_64
    os_family: ORACLE_LINUX_9
    location: [ "ON_PREMISE" ]
    location_not_equal_to: [ "ON_PREMISE" ]
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
lifecycle_environments:
    description:
        - List of LifecycleEnvironment resources
    returned: on success
    type: complex
    contains:
        managed_instance_ids:
            description:
                - List of managed instance L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) assigned to the lifecycle stage.
                - Returned for get operation
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
                lifecycle_environment_display_name:
                    description:
                        - The user-friendly name for the lifecycle environment. Does not have to be unique, and it's changeable. Avoid entering confidential
                          information.
                    returned: on success
                    type: str
                    sample: lifecycle_environment_display_name_example
                managed_instances:
                    description:
                        - The list of managed instances associated with the lifecycle stage.
                    returned: on success
                    type: int
                    sample: 56
        lifecycle_state:
            description:
                - The current state of the lifecycle environment.
            returned: on success
            type: str
            sample: CREATING
        arch_type:
            description:
                - The CPU architecture of the managed instances in the lifecycle environment.
            returned: on success
            type: str
            sample: X86_64
        os_family:
            description:
                - The operating system of the managed instances in the lifecycle environment.
            returned: on success
            type: str
            sample: ORACLE_LINUX_9
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
    sample: [{
        "managed_instance_ids": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
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
            "system_tags": {},
            "lifecycle_environment_display_name": "lifecycle_environment_display_name_example",
            "managed_instances": 56
        }],
        "lifecycle_state": "CREATING",
        "arch_type": "X86_64",
        "os_family": "ORACLE_LINUX_9",
        "vendor_name": "ORACLE",
        "location": "ON_PREMISE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_modified": "2013-10-20T19:20:30+01:00",
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
    from oci.os_management_hub import LifecycleEnvironmentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LifecycleEnvironmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "lifecycle_environment_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_lifecycle_environment,
            lifecycle_environment_id=self.module.params.get("lifecycle_environment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "display_name_contains",
            "lifecycle_environment_id",
            "arch_type",
            "os_family",
            "location",
            "location_not_equal_to",
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
            self.client.list_lifecycle_environments, **optional_kwargs
        )


LifecycleEnvironmentFactsHelperCustom = get_custom_class(
    "LifecycleEnvironmentFactsHelperCustom"
)


class ResourceFactsHelper(
    LifecycleEnvironmentFactsHelperCustom, LifecycleEnvironmentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="list", elements="str"),
            display_name_contains=dict(type="str"),
            lifecycle_environment_id=dict(aliases=["id"], type="str"),
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
            location=dict(
                type="list",
                elements="str",
                choices=["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"],
            ),
            location_not_equal_to=dict(
                type="list",
                elements="str",
                choices=["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"],
            ),
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
        resource_type="lifecycle_environment",
        service_client_class=LifecycleEnvironmentClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(lifecycle_environments=result)


if __name__ == "__main__":
    main()
