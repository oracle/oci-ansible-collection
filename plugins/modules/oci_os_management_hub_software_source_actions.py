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
module: oci_os_management_hub_software_source_actions
short_description: Perform actions on a SoftwareSource resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a SoftwareSource resource in Oracle Cloud Infrastructure
    - For I(action=add_packages), adds packages to a software source. This operation can only be done for custom and versioned custom software sources that are
      not created using filters.
      For a versioned custom software source, you can only add packages when the source is created. Once content is added to a versioned custom software source,
      it is immutable.
    - For I(action=change_compartment), moves the specified software sources to a different compartment within the same tenancy.
      For information about moving resources between compartments, see L(Moving Resources to a Different
      Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    packages:
        description:
            - List of packages specified by the full package name (NEVRA.rpm).
            - Required for I(action=add_packages).
        type: list
        elements: str
    software_source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the software source to.
            - Required for I(action=change_compartment).
        type: str
    action:
        description:
            - The action to perform on the SoftwareSource.
        type: str
        required: true
        choices:
            - "add_packages"
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_packages on software_source
  oci_os_management_hub_software_source_actions:
    # required
    packages: [ "packages_example" ]
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    action: add_packages

- name: Perform action change_compartment on software_source
  oci_os_management_hub_software_source_actions:
    # required
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.os_management_hub import WorkRequestClient
    from oci.os_management_hub import SoftwareSourceClient
    from oci.os_management_hub.models import AddPackagesToSoftwareSourceDetails
    from oci.os_management_hub.models import ChangeSoftwareSourceCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubSoftwareSourceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_packages
        change_compartment
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "software_source_id"

    def get_module_resource_id(self):
        return self.module.params.get("software_source_id")

    def get_get_fn(self):
        return self.client.get_software_source

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_software_source,
            software_source_id=self.module.params.get("software_source_id"),
        )

    def add_packages(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddPackagesToSoftwareSourceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_packages_to_software_source,
            call_fn_args=(),
            call_fn_kwargs=dict(
                software_source_id=self.module.params.get("software_source_id"),
                add_packages_to_software_source_details=action_details,
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeSoftwareSourceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_software_source_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                software_source_id=self.module.params.get("software_source_id"),
                change_software_source_compartment_details=action_details,
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


OsManagementHubSoftwareSourceActionsHelperCustom = get_custom_class(
    "OsManagementHubSoftwareSourceActionsHelperCustom"
)


class ResourceHelper(
    OsManagementHubSoftwareSourceActionsHelperCustom,
    OsManagementHubSoftwareSourceActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            packages=dict(type="list", elements="str"),
            software_source_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=["add_packages", "change_compartment"],
            ),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
