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
module: oci_os_management_hub_software_source
short_description: Manage a SoftwareSource resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a SoftwareSource resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new versioned or custom software source.
    - "This resource has the following action operations in the M(oracle.oci.oci_os_management_hub_software_source_actions) module: add_packages,
      change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    origin_software_source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the vendor software source in the root compartment that
              is being replicated.
            - Required when software_source_type is 'VENDOR'
        type: str
    software_source_version:
        description:
            - The version to assign to this custom software source.
            - Required when software_source_type is 'VERSIONED'
        type: str
    is_created_from_package_list:
        description:
            - Indicates whether the service should create the software source from a list of packages provided by the user.
            - Applicable when software_source_type is one of ['CUSTOM', 'VERSIONED']
        type: bool
    packages:
        description:
            - A property used for compatibility only. It doesn't provide a complete list of packages. See
              L(AddPackagesToSoftwareSourceDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/osmh/latest/datatypes/AddPackagesToSoftwareSourceDetails)
              for providing the list of packages used to create the software source when isCreatedFromPackageList is set to true.
            - Applicable when software_source_type is one of ['CUSTOM', 'VERSIONED']
        type: list
        elements: str
    vendor_software_sources:
        description:
            - List of vendor software sources.
            - This parameter is updatable.
            - Required when software_source_type is one of ['CUSTOM', 'VERSIONED']
        type: list
        elements: dict
        suboptions:
            id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that is immutable on creation.
                    - Required when software_source_type is 'CUSTOM'
                type: str
                required: true
            display_name:
                description:
                    - User-friendly name.
                    - Required when software_source_type is 'CUSTOM'
                type: str
                aliases: ["name"]
                required: true
    custom_software_source_filter:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when software_source_type is one of ['CUSTOM', 'VERSIONED']
        type: dict
        suboptions:
            package_filters:
                description:
                    - The list of package filters.
                    - Applicable when software_source_type is 'CUSTOM'
                type: list
                elements: dict
                suboptions:
                    package_name:
                        description:
                            - The package name.
                            - Applicable when software_source_type is 'CUSTOM'
                        type: str
                    package_name_pattern:
                        description:
                            - The package name pattern.
                            - Applicable when software_source_type is 'CUSTOM'
                        type: str
                    package_version:
                        description:
                            - The package version, which is denoted by 'version-release', or 'epoch:version-release'.
                            - Applicable when software_source_type is 'CUSTOM'
                        type: str
                    filter_type:
                        description:
                            - The type of the filter.
                            - Required when software_source_type is 'CUSTOM'
                        type: str
                        choices:
                            - "INCLUDE"
                            - "EXCLUDE"
                        required: true
            module_stream_profile_filters:
                description:
                    - The list of module stream/profile filters.
                    - Applicable when software_source_type is 'CUSTOM'
                type: list
                elements: dict
                suboptions:
                    module_name:
                        description:
                            - Module name.
                            - Required when software_source_type is 'CUSTOM'
                        type: str
                        required: true
                    profile_name:
                        description:
                            - Profile name.
                            - Applicable when software_source_type is 'CUSTOM'
                        type: str
                    stream_name:
                        description:
                            - Stream name.
                            - Applicable when software_source_type is 'CUSTOM'
                        type: str
                    filter_type:
                        description:
                            - The type of the filter.
                            - Required when software_source_type is 'CUSTOM'
                        type: str
                        choices:
                            - "INCLUDE"
                            - "EXCLUDE"
                        required: true
            package_group_filters:
                description:
                    - The list of group filters.
                    - Applicable when software_source_type is 'CUSTOM'
                type: list
                elements: dict
                suboptions:
                    package_groups:
                        description:
                            - List of package group names.
                            - Applicable when software_source_type is 'CUSTOM'
                        type: list
                        elements: str
                    filter_type:
                        description:
                            - The type of the filter.
                            - Required when software_source_type is 'CUSTOM'
                        type: str
                        choices:
                            - "INCLUDE"
                            - "EXCLUDE"
                        required: true
    is_automatically_updated:
        description:
            - Indicates whether the service should automatically update the custom software source to use the latest package versions available. The service
              reviews packages levels once a day.
            - This parameter is updatable.
            - Applicable when software_source_type is 'CUSTOM'
        type: bool
    is_auto_resolve_dependencies:
        description:
            - Indicates whether the service should automatically resolve package dependencies when including specific packages in the software source.
            - This parameter is updatable.
            - Applicable when software_source_type is one of ['CUSTOM', 'VERSIONED']
        type: bool
    is_latest_content_only:
        description:
            - "Indicates whether the software source will include only the latest versions of content from vendor software sources, while accounting for other
              constraints set in the custom or versioned custom software source (such as a package list or filters).
              * For a module filter that does not specify a stream, this will include all available streams, and within each stream only the latest version of
              packages.
              * For a module filter that does specify a stream, this will include only the latest version of packages for the specified stream.
              * For a package filter that does not specify a version, this will include only the latest available version of the package.
              * For a package filter that does specify a version, this will include only the specified version of the package (the isLatestContentOnly attribute
              is ignored).
              * For a package list, this will include only the specified version of packages and modules in the list (the isLatestContentOnly attribute is
              ignored)."
            - This parameter is updatable.
            - Applicable when software_source_type is one of ['CUSTOM', 'VERSIONED']
        type: bool
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the software source.
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when software_source_type is one of ['CUSTOM', 'VENDOR', 'VERSIONED']
        type: str
    display_name:
        description:
            - User-friendly name for the software source. Does not have to be unique and you can change the name later. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - User-specified description for the software source. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    software_source_type:
        description:
            - Type of software source.
            - Required for create using I(state=present), update using I(state=present) with software_source_id present.
            - Applicable when software_source_type is one of ['CUSTOM', 'VENDOR', 'VERSIONED']
        type: str
        choices:
            - "CUSTOM"
            - "VENDOR"
            - "VERSIONED"
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
    software_source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the SoftwareSource.
            - Use I(state=present) to create or update a SoftwareSource.
            - Use I(state=absent) to delete a SoftwareSource.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create software_source with software_source_type = CUSTOM
  oci_os_management_hub_software_source:
    # required
    software_source_type: CUSTOM

    # optional
    is_created_from_package_list: true
    packages: [ "packages_example" ]
    vendor_software_sources:
    - # required
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      display_name: display_name_example
    custom_software_source_filter:
      # optional
      package_filters:
      - # required
        filter_type: INCLUDE

        # optional
        package_name: package_name_example
        package_name_pattern: package_name_pattern_example
        package_version: package_version_example
      module_stream_profile_filters:
      - # required
        module_name: module_name_example
        filter_type: INCLUDE

        # optional
        profile_name: profile_name_example
        stream_name: stream_name_example
      package_group_filters:
      - # required
        filter_type: INCLUDE

        # optional
        package_groups: [ "package_groups_example" ]
    is_automatically_updated: true
    is_auto_resolve_dependencies: true
    is_latest_content_only: true
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create software_source with software_source_type = VENDOR
  oci_os_management_hub_software_source:
    # required
    origin_software_source_id: "ocid1.originsoftwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    software_source_type: VENDOR

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create software_source with software_source_type = VERSIONED
  oci_os_management_hub_software_source:
    # required
    software_source_version: software_source_version_example
    vendor_software_sources:
    - # required
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      display_name: display_name_example
    software_source_type: VERSIONED

    # optional
    is_created_from_package_list: true
    packages: [ "packages_example" ]
    custom_software_source_filter:
      # optional
      package_filters:
      - # required
        filter_type: INCLUDE

        # optional
        package_name: package_name_example
        package_name_pattern: package_name_pattern_example
        package_version: package_version_example
      module_stream_profile_filters:
      - # required
        module_name: module_name_example
        filter_type: INCLUDE

        # optional
        profile_name: profile_name_example
        stream_name: stream_name_example
      package_group_filters:
      - # required
        filter_type: INCLUDE

        # optional
        package_groups: [ "package_groups_example" ]
    is_auto_resolve_dependencies: true
    is_latest_content_only: true
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update software_source with software_source_type = CUSTOM
  oci_os_management_hub_software_source:
    # required
    software_source_type: CUSTOM

    # optional
    vendor_software_sources:
    - # required
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      display_name: display_name_example
    custom_software_source_filter:
      # optional
      package_filters:
      - # required
        filter_type: INCLUDE

        # optional
        package_name: package_name_example
        package_name_pattern: package_name_pattern_example
        package_version: package_version_example
      module_stream_profile_filters:
      - # required
        module_name: module_name_example
        filter_type: INCLUDE

        # optional
        profile_name: profile_name_example
        stream_name: stream_name_example
      package_group_filters:
      - # required
        filter_type: INCLUDE

        # optional
        package_groups: [ "package_groups_example" ]
    is_automatically_updated: true
    is_auto_resolve_dependencies: true
    is_latest_content_only: true
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update software_source with software_source_type = VENDOR
  oci_os_management_hub_software_source:
    # required
    software_source_type: VENDOR

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update software_source with software_source_type = VERSIONED
  oci_os_management_hub_software_source:
    # required
    vendor_software_sources:
    - # required
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      display_name: display_name_example
    software_source_type: VERSIONED

    # optional
    custom_software_source_filter:
      # optional
      package_filters:
      - # required
        filter_type: INCLUDE

        # optional
        package_name: package_name_example
        package_name_pattern: package_name_pattern_example
        package_version: package_version_example
      module_stream_profile_filters:
      - # required
        module_name: module_name_example
        filter_type: INCLUDE

        # optional
        profile_name: profile_name_example
        stream_name: stream_name_example
      package_group_filters:
      - # required
        filter_type: INCLUDE

        # optional
        package_groups: [ "package_groups_example" ]
    is_auto_resolve_dependencies: true
    is_latest_content_only: true
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update software_source using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with software_source_type = CUSTOM
  oci_os_management_hub_software_source:
    # required
    software_source_type: CUSTOM

    # optional
    vendor_software_sources:
    - # required
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      display_name: display_name_example
    custom_software_source_filter:
      # optional
      package_filters:
      - # required
        filter_type: INCLUDE

        # optional
        package_name: package_name_example
        package_name_pattern: package_name_pattern_example
        package_version: package_version_example
      module_stream_profile_filters:
      - # required
        module_name: module_name_example
        filter_type: INCLUDE

        # optional
        profile_name: profile_name_example
        stream_name: stream_name_example
      package_group_filters:
      - # required
        filter_type: INCLUDE

        # optional
        package_groups: [ "package_groups_example" ]
    is_automatically_updated: true
    is_auto_resolve_dependencies: true
    is_latest_content_only: true
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update software_source using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with software_source_type = VENDOR
  oci_os_management_hub_software_source:
    # required
    software_source_type: VENDOR

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update software_source using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with software_source_type = VERSIONED
  oci_os_management_hub_software_source:
    # required
    vendor_software_sources:
    - # required
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      display_name: display_name_example
    software_source_type: VERSIONED

    # optional
    custom_software_source_filter:
      # optional
      package_filters:
      - # required
        filter_type: INCLUDE

        # optional
        package_name: package_name_example
        package_name_pattern: package_name_pattern_example
        package_version: package_version_example
      module_stream_profile_filters:
      - # required
        module_name: module_name_example
        filter_type: INCLUDE

        # optional
        profile_name: profile_name_example
        stream_name: stream_name_example
      package_group_filters:
      - # required
        filter_type: INCLUDE

        # optional
        package_groups: [ "package_groups_example" ]
    is_auto_resolve_dependencies: true
    is_latest_content_only: true
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete software_source
  oci_os_management_hub_software_source:
    # required
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete software_source using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_hub_software_source:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
software_source:
    description:
        - Details of the SoftwareSource resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        is_automatically_updated:
            description:
                - Indicates whether the service should automatically update the custom software source to use the latest package versions available. The service
                  reviews packages levels once a day.
            returned: on success
            type: bool
            sample: true
        vendor_name:
            description:
                - Name of the vendor providing the software source.
            returned: on success
            type: str
            sample: ORACLE
        origin_software_source_id:
            description:
                - This property applies only to replicated vendor software sources. This is the
                  L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the vendor software source in the root compartment.
            returned: on success
            type: str
            sample: "ocid1.originsoftwaresource.oc1..xxxxxxEXAMPLExxxxxx"
        is_mandatory_for_autonomous_linux:
            description:
                - Indicates whether the software source is required for the Autonomous Linux service.
            returned: on success
            type: bool
            sample: true
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
        time_created:
            description:
                - The date and time the software source was created (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
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
        repo_id:
            description:
                - The repository ID for the software source.
            returned: on success
            type: str
            sample: "ocid1.repo.oc1..xxxxxxEXAMPLExxxxxx"
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
        lifecycle_state:
            description:
                - The current state of the software source.
            returned: on success
            type: str
            sample: CREATING
        package_count:
            description:
                - Number of packages the software source contains.
            returned: on success
            type: int
            sample: 56
        url:
            description:
                - URL for the repository. For vendor software sources, this is the URL to the regional yum server. For custom software sources, this is
                  'custom/<repoId>'.
            returned: on success
            type: str
            sample: url_example
        checksum_type:
            description:
                - The yum repository checksum type used by this software source.
            returned: on success
            type: str
            sample: SHA1
        gpg_key_url:
            description:
                - URL of the GPG key for this software source.
            returned: on success
            type: str
            sample: gpg_key_url_example
        gpg_key_id:
            description:
                - ID of the GPG key for this software source.
            returned: on success
            type: str
            sample: "ocid1.gpgkey.oc1..xxxxxxEXAMPLExxxxxx"
        gpg_key_fingerprint:
            description:
                - Fingerprint of the GPG key for this software source.
            returned: on success
            type: str
            sample: gpg_key_fingerprint_example
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
        vendor_software_sources:
            description:
                - List of vendor software sources that are used for the basis of the custom software source.
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
            returned: on success
            type: str
            sample: software_source_version_example
        is_auto_resolve_dependencies:
            description:
                - Indicates whether the service should automatically resolve package dependencies when including specific packages in the software source.
            returned: on success
            type: bool
            sample: true
        is_created_from_package_list:
            description:
                - Indicates whether the service should create the software source from a list of packages provided by the user.
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
            returned: on success
            type: bool
            sample: true
        packages:
            description:
                - The packages in the software source.
            returned: on success
            type: list
            sample: []
    sample: {
        "is_automatically_updated": true,
        "vendor_name": "ORACLE",
        "origin_software_source_id": "ocid1.originsoftwaresource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_mandatory_for_autonomous_linux": true,
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "description": "description_example",
        "software_source_type": "VENDOR",
        "availability": "AVAILABLE",
        "availability_at_oci": "AVAILABLE",
        "repo_id": "ocid1.repo.oc1..xxxxxxEXAMPLExxxxxx",
        "os_family": "ORACLE_LINUX_9",
        "arch_type": "X86_64",
        "lifecycle_state": "CREATING",
        "package_count": 56,
        "url": "url_example",
        "checksum_type": "SHA1",
        "gpg_key_url": "gpg_key_url_example",
        "gpg_key_id": "ocid1.gpgkey.oc1..xxxxxxEXAMPLExxxxxx",
        "gpg_key_fingerprint": "gpg_key_fingerprint_example",
        "size": 1.2,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
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
        "packages": []
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import WorkRequestClient
    from oci.os_management_hub import SoftwareSourceClient
    from oci.os_management_hub.models import CreateSoftwareSourceDetails
    from oci.os_management_hub.models import UpdateSoftwareSourceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubSoftwareSourceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_possible_entity_types(self):
        return super(
            OsManagementHubSoftwareSourceHelperGen, self
        ).get_possible_entity_types() + [
            "softwaresource",
            "softwaresources",
            "osManagementHubsoftwaresource",
            "osManagementHubsoftwaresources",
            "softwaresourceresource",
            "softwaresourcesresource",
            "osmanagementhub",
        ]

    def get_module_resource_id_param(self):
        return "software_source_id"

    def get_module_resource_id(self):
        return self.module.params.get("software_source_id")

    def get_get_fn(self):
        return self.client.get_software_source

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_software_source, software_source_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_software_source,
            software_source_id=self.module.params.get("software_source_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["software_source_id", "display_name"]
            if self._use_name_as_identifier()
            else ["compartment_id", "software_source_id", "display_name"]
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
        return oci_common_utils.list_all_resources(
            self.client.list_software_sources, **kwargs
        )

    def get_create_model_class(self):
        return CreateSoftwareSourceDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_software_source,
            call_fn_args=(),
            call_fn_kwargs=dict(create_software_source_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateSoftwareSourceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_software_source,
            call_fn_args=(),
            call_fn_kwargs=dict(
                software_source_id=self.module.params.get("software_source_id"),
                update_software_source_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_software_source,
            call_fn_args=(),
            call_fn_kwargs=dict(
                software_source_id=self.module.params.get("software_source_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


OsManagementHubSoftwareSourceHelperCustom = get_custom_class(
    "OsManagementHubSoftwareSourceHelperCustom"
)


class ResourceHelper(
    OsManagementHubSoftwareSourceHelperCustom, OsManagementHubSoftwareSourceHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            origin_software_source_id=dict(type="str"),
            software_source_version=dict(type="str"),
            is_created_from_package_list=dict(type="bool"),
            packages=dict(type="list", elements="str"),
            vendor_software_sources=dict(
                type="list",
                elements="dict",
                options=dict(
                    id=dict(type="str", required=True),
                    display_name=dict(aliases=["name"], type="str", required=True),
                ),
            ),
            custom_software_source_filter=dict(
                type="dict",
                options=dict(
                    package_filters=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            package_name=dict(type="str"),
                            package_name_pattern=dict(type="str"),
                            package_version=dict(type="str"),
                            filter_type=dict(
                                type="str",
                                required=True,
                                choices=["INCLUDE", "EXCLUDE"],
                            ),
                        ),
                    ),
                    module_stream_profile_filters=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            module_name=dict(type="str", required=True),
                            profile_name=dict(type="str"),
                            stream_name=dict(type="str"),
                            filter_type=dict(
                                type="str",
                                required=True,
                                choices=["INCLUDE", "EXCLUDE"],
                            ),
                        ),
                    ),
                    package_group_filters=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            package_groups=dict(type="list", elements="str"),
                            filter_type=dict(
                                type="str",
                                required=True,
                                choices=["INCLUDE", "EXCLUDE"],
                            ),
                        ),
                    ),
                ),
            ),
            is_automatically_updated=dict(type="bool"),
            is_auto_resolve_dependencies=dict(type="bool"),
            is_latest_content_only=dict(type="bool"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            software_source_type=dict(
                type="str", choices=["CUSTOM", "VENDOR", "VERSIONED"]
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            software_source_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="software_source",
        service_client_class=SoftwareSourceClient,
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
