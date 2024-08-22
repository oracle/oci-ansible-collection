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
module: oci_os_management_hub_software_source_facts
short_description: Fetches details about one or multiple SoftwareSource resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SoftwareSource resources in Oracle Cloud Infrastructure
    - Lists software sources that match the specified tenancy or software source
      L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Filter the list against a
      variety of criteria including but not limited to its name, status, architecture, and OS family.
    - If I(software_source_id) is specified, the details of a single SoftwareSource will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
        type: str
    software_source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source.
            - Required to get a specific software_source.
        type: str
        aliases: ["id"]
    software_source_type:
        description:
            - The type of the software source.
        type: list
        elements: str
        choices:
            - "VENDOR"
            - "CUSTOM"
            - "VERSIONED"
    vendor_name:
        description:
            - A filter to return only resources that match the given vendor name.
        type: str
        choices:
            - "ORACLE"
            - "MICROSOFT"
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
    is_mandatory_for_autonomous_linux:
        description:
            - Indicates whether the software source is mandatory for the Autonomous Linux service.
        type: bool
    display_name:
        description:
            - A filter to return resources that match the given user-friendly name.
        type: str
        aliases: ["name"]
    display_name_contains:
        description:
            - A filter to return resources that may partially match the given display name.
        type: str
    display_name_not_equal_to:
        description:
            - A multi filter to return resources that do not contains the given display names.
        type: list
        elements: str
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
- name: Get a specific software_source
  oci_os_management_hub_software_source_facts:
    # required
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"

- name: List software_sources
  oci_os_management_hub_software_source_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    software_source_type: [ "VENDOR" ]
    vendor_name: ORACLE
    os_family: [ "ORACLE_LINUX_9" ]
    arch_type: [ "X86_64" ]
    availability: [ "AVAILABLE" ]
    availability_at_oci: [ "AVAILABLE" ]
    availability_anywhere: [ "AVAILABLE" ]
    is_mandatory_for_autonomous_linux: true
    display_name: display_name_example
    display_name_contains: display_name_contains_example
    display_name_not_equal_to: [ "display_name_not_equal_to_example" ]
    sort_order: ASC
    sort_by: timeCreated
    lifecycle_state: [ "lifecycle_state_example" ]

"""

RETURN = """
software_sources:
    description:
        - List of SoftwareSource resources
    returned: on success
    type: complex
    contains:
        is_automatically_updated:
            description:
                - Indicates whether the service should automatically update the custom software source to use the latest package versions available. The service
                  reviews packages levels once a day.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        vendor_name:
            description:
                - Name of the vendor providing the software source.
                - Returned for get operation
            returned: on success
            type: str
            sample: ORACLE
        origin_software_source_id:
            description:
                - This property applies only to replicated vendor software sources. This is the
                  L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the vendor software source in the root compartment.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.originsoftwaresource.oc1..xxxxxxEXAMPLExxxxxx"
        is_mandatory_for_autonomous_linux:
            description:
                - Indicates whether the software source is required for the Autonomous Linux service.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        checksum_type:
            description:
                - The yum repository checksum type used by this software source.
                - Returned for get operation
            returned: on success
            type: str
            sample: SHA1
        gpg_key_url:
            description:
                - URL of the GPG key for this software source.
                - Returned for get operation
            returned: on success
            type: str
            sample: gpg_key_url_example
        gpg_key_id:
            description:
                - ID of the GPG key for this software source.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.gpgkey.oc1..xxxxxxEXAMPLExxxxxx"
        gpg_key_fingerprint:
            description:
                - Fingerprint of the GPG key for this software source.
                - Returned for get operation
            returned: on success
            type: str
            sample: gpg_key_fingerprint_example
        vendor_software_sources:
            description:
                - List of vendor software sources that are used for the basis of the custom software source.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that is immutable on creation.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User-friendly name.
                    returned: on success
                    type: str
                    sample: display_name_example
        custom_software_source_filter:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                package_filters:
                    description:
                        - The list of package filters.
                    returned: on success
                    type: complex
                    contains:
                        package_name:
                            description:
                                - The package name.
                            returned: on success
                            type: str
                            sample: package_name_example
                        package_name_pattern:
                            description:
                                - The package name pattern.
                            returned: on success
                            type: str
                            sample: package_name_pattern_example
                        package_version:
                            description:
                                - The package version, which is denoted by 'version-release', or 'epoch:version-release'.
                            returned: on success
                            type: str
                            sample: package_version_example
                        filter_type:
                            description:
                                - The type of the filter.
                            returned: on success
                            type: str
                            sample: INCLUDE
                module_stream_profile_filters:
                    description:
                        - The list of module stream/profile filters.
                    returned: on success
                    type: complex
                    contains:
                        module_name:
                            description:
                                - Module name.
                            returned: on success
                            type: str
                            sample: module_name_example
                        profile_name:
                            description:
                                - Profile name.
                            returned: on success
                            type: str
                            sample: profile_name_example
                        stream_name:
                            description:
                                - Stream name.
                            returned: on success
                            type: str
                            sample: stream_name_example
                        filter_type:
                            description:
                                - The type of the filter.
                            returned: on success
                            type: str
                            sample: INCLUDE
                package_group_filters:
                    description:
                        - The list of group filters.
                    returned: on success
                    type: complex
                    contains:
                        package_groups:
                            description:
                                - List of package group names.
                            returned: on success
                            type: list
                            sample: []
                        filter_type:
                            description:
                                - The type of the filter.
                            returned: on success
                            type: str
                            sample: INCLUDE
        software_source_version:
            description:
                - The version to assign to this custom software source.
                - Returned for get operation
            returned: on success
            type: str
            sample: software_source_version_example
        is_auto_resolve_dependencies:
            description:
                - Indicates whether the service should automatically resolve package dependencies when including specific packages in the software source.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        is_created_from_package_list:
            description:
                - Indicates whether the service should create the software source from a list of packages provided by the user.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        is_latest_content_only:
            description:
                - "Indicates whether the software source will include only the latest versions of content from vendor software sources, while accounting for
                  other constraints set in the custom or versioned custom software source (such as a package list or filters).
                  * For a module filter that does not specify a stream, this will include all available streams, and within each stream only the latest version
                  of packages.
                  * For a module filter that does specify a stream, this will include only the latest version of packages for the specified stream.
                  * For a package filter that does not specify a version, this will include only the latest available version of the package.
                  * For a package filter that does specify a version, this will include only the specified version of the package (the isLatestContentOnly
                  attribute is ignored).
                  * For a package list, this will include only the specified version of packages and modules in the list (the isLatestContentOnly attribute is
                  ignored)."
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        packages:
            description:
                - The packages in the software source.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
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
                - Returned for list operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        description:
            description:
                - User-specified description for the software source.
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
            sample: CREATING
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
        "is_automatically_updated": true,
        "vendor_name": "ORACLE",
        "origin_software_source_id": "ocid1.originsoftwaresource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_mandatory_for_autonomous_linux": true,
        "checksum_type": "SHA1",
        "gpg_key_url": "gpg_key_url_example",
        "gpg_key_id": "ocid1.gpgkey.oc1..xxxxxxEXAMPLExxxxxx",
        "gpg_key_fingerprint": "gpg_key_fingerprint_example",
        "vendor_software_sources": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "custom_software_source_filter": {
            "package_filters": [{
                "package_name": "package_name_example",
                "package_name_pattern": "package_name_pattern_example",
                "package_version": "package_version_example",
                "filter_type": "INCLUDE"
            }],
            "module_stream_profile_filters": [{
                "module_name": "module_name_example",
                "profile_name": "profile_name_example",
                "stream_name": "stream_name_example",
                "filter_type": "INCLUDE"
            }],
            "package_group_filters": [{
                "package_groups": [],
                "filter_type": "INCLUDE"
            }]
        },
        "software_source_version": "software_source_version_example",
        "is_auto_resolve_dependencies": true,
        "is_created_from_package_list": true,
        "is_latest_content_only": true,
        "packages": [],
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
        "lifecycle_state": "CREATING",
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


class SoftwareSourceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "software_source_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_software_source,
            software_source_id=self.module.params.get("software_source_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "software_source_id",
            "software_source_type",
            "vendor_name",
            "os_family",
            "arch_type",
            "availability",
            "availability_at_oci",
            "availability_anywhere",
            "is_mandatory_for_autonomous_linux",
            "display_name",
            "display_name_contains",
            "display_name_not_equal_to",
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
            self.client.list_software_sources, **optional_kwargs
        )


SoftwareSourceFactsHelperCustom = get_custom_class("SoftwareSourceFactsHelperCustom")


class ResourceFactsHelper(
    SoftwareSourceFactsHelperCustom, SoftwareSourceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            software_source_id=dict(aliases=["id"], type="str"),
            software_source_type=dict(
                type="list", elements="str", choices=["VENDOR", "CUSTOM", "VERSIONED"]
            ),
            vendor_name=dict(type="str", choices=["ORACLE", "MICROSOFT"]),
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
            is_mandatory_for_autonomous_linux=dict(type="bool"),
            display_name=dict(aliases=["name"], type="str"),
            display_name_contains=dict(type="str"),
            display_name_not_equal_to=dict(type="list", elements="str"),
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
        resource_type="software_source",
        service_client_class=SoftwareSourceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(software_sources=result)


if __name__ == "__main__":
    main()
