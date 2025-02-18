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
module: oci_os_management_hub_software_package_software_source_facts
short_description: Fetches details about one or multiple SoftwarePackageSoftwareSource resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SoftwarePackageSoftwareSource resources in Oracle Cloud Infrastructure
    - Lists the software sources in the tenancy that contain the software package. Filter the list against a
      variety of criteria including but not limited to its name, type, architecture, and OS family.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    software_package_name:
        description:
            - The name of the software package.
        type: str
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment. This parameter is required and returns
              only resources contained within the specified compartment.
        type: str
        required: true
    software_source_type:
        description:
            - The type of the software source.
        type: list
        elements: str
        choices:
            - "VENDOR"
            - "CUSTOM"
            - "VERSIONED"
    os_family:
        description:
            - A filter to return only resources that match the given operating system family.
        type: list
        elements: str
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
            - A filter to return only instances whose architecture type matches the given architecture.
        type: list
        elements: str
        choices:
            - "X86_64"
            - "AARCH64"
            - "I686"
            - "NOARCH"
            - "SRC"
    availability:
        description:
            - The availabilities of the software source in a non-OCI environment for a tenancy.
        type: list
        elements: str
        choices:
            - "AVAILABLE"
            - "SELECTED"
            - "RESTRICTED"
            - "UNAVAILABLE"
    availability_at_oci:
        description:
            - The availabilities of the software source in an OCI environment for a tenancy.
        type: list
        elements: str
        choices:
            - "AVAILABLE"
            - "SELECTED"
            - "RESTRICTED"
            - "UNAVAILABLE"
    availability_anywhere:
        description:
            - The availabilities of the software source. Use this query parameter to filter across availabilities in different environments.
        type: list
        elements: str
        choices:
            - "AVAILABLE"
            - "SELECTED"
            - "RESTRICTED"
            - "UNAVAILABLE"
    display_name:
        description:
            - A filter to return resources that match the given user-friendly name.
        type: str
        aliases: ["name"]
    display_name_contains:
        description:
            - A filter to return resources that may partially match the given display name.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    lifecycle_state:
        description:
            - A filter to return only software sources whose state matches the given state.
        type: list
        elements: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List software_package_software_sources
  oci_os_management_hub_software_package_software_source_facts:
    # required
    software_package_name: software_package_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    software_source_type: [ "VENDOR" ]
    os_family: [ "ORACLE_LINUX_9" ]
    arch_type: [ "X86_64" ]
    availability: [ "AVAILABLE" ]
    availability_at_oci: [ "AVAILABLE" ]
    availability_anywhere: [ "AVAILABLE" ]
    display_name: display_name_example
    display_name_contains: display_name_contains_example
    sort_order: ASC
    sort_by: timeCreated
    lifecycle_state: [ "lifecycle_state_example" ]

"""

RETURN = """
software_package_software_sources:
    description:
        - List of SoftwarePackageSoftwareSource resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the software source.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User-friendly name for the software source.
            returned: on success
            type: str
            sample: display_name_example
        repo_id:
            description:
                - The repository ID for the software source.
            returned: on success
            type: str
            sample: "ocid1.repo.oc1..xxxxxxEXAMPLExxxxxx"
        url:
            description:
                - URL for the repository. For vendor software sources, this is the URL to the regional yum server. For custom software sources, this is
                  'custom/<repoId>'.
            returned: on success
            type: str
            sample: url_example
        time_created:
            description:
                - The date and time the software source was created (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the software source was updated (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        description:
            description:
                - Description of the software source. For custom software sources, this is user-specified.
            returned: on success
            type: str
            sample: description_example
        software_source_type:
            description:
                - Type of software source.
            returned: on success
            type: str
            sample: VENDOR
        availability:
            description:
                - Availability of the software source (for non-OCI environments).
            returned: on success
            type: str
            sample: AVAILABLE
        availability_at_oci:
            description:
                - Availability of the software source (for OCI environments).
            returned: on success
            type: str
            sample: AVAILABLE
        os_family:
            description:
                - The OS family the software source belongs to.
            returned: on success
            type: str
            sample: ORACLE_LINUX_9
        arch_type:
            description:
                - The architecture type supported by the software source.
            returned: on success
            type: str
            sample: X86_64
        package_count:
            description:
                - Number of packages the software source contains.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of the software source.
            returned: on success
            type: str
            sample: lifecycle_state_example
        size:
            description:
                - The size of the software source in gigabytes (GB).
            returned: on success
            type: float
            sample: 1.2
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "repo_id": "ocid1.repo.oc1..xxxxxxEXAMPLExxxxxx",
        "url": "url_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "description": "description_example",
        "software_source_type": "VENDOR",
        "availability": "AVAILABLE",
        "availability_at_oci": "AVAILABLE",
        "os_family": "ORACLE_LINUX_9",
        "arch_type": "X86_64",
        "package_count": 56,
        "lifecycle_state": "lifecycle_state_example",
        "size": 1.2,
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
    from oci.os_management_hub import SoftwareSourceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubSoftwarePackageSoftwareSourceFactsHelperGen(
    OCIResourceFactsHelperBase
):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "software_package_name",
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "software_source_type",
            "os_family",
            "arch_type",
            "availability",
            "availability_at_oci",
            "availability_anywhere",
            "display_name",
            "display_name_contains",
            "sort_order",
            "sort_by",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_software_package_software_sources,
            software_package_name=self.module.params.get("software_package_name"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OsManagementHubSoftwarePackageSoftwareSourceFactsHelperCustom = get_custom_class(
    "OsManagementHubSoftwarePackageSoftwareSourceFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubSoftwarePackageSoftwareSourceFactsHelperCustom,
    OsManagementHubSoftwarePackageSoftwareSourceFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            software_package_name=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            software_source_type=dict(
                type="list", elements="str", choices=["VENDOR", "CUSTOM", "VERSIONED"]
            ),
            os_family=dict(
                type="list",
                elements="str",
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
                type="list",
                elements="str",
                choices=["X86_64", "AARCH64", "I686", "NOARCH", "SRC"],
            ),
            availability=dict(
                type="list",
                elements="str",
                choices=["AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"],
            ),
            availability_at_oci=dict(
                type="list",
                elements="str",
                choices=["AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"],
            ),
            availability_anywhere=dict(
                type="list",
                elements="str",
                choices=["AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"],
            ),
            display_name=dict(aliases=["name"], type="str"),
            display_name_contains=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            lifecycle_state=dict(type="list", elements="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="software_package_software_source",
        service_client_class=SoftwareSourceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(software_package_software_sources=result)


if __name__ == "__main__":
    main()
