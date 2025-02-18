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
module: oci_os_management_hub_all_software_package_facts
short_description: Fetches details about one or multiple AllSoftwarePackage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AllSoftwarePackage resources in Oracle Cloud Infrastructure
    - Lists software packages available through the OS Management Hub service.  Filter the list against a variety of criteria
      including but not limited to its name.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - A filter to return resources that match the given user-friendly name.
        type: str
    display_name_contains:
        description:
            - A filter to return resources that may partially match the given display name.
        type: str
    version:
        description:
            - A filter to return software packages that match the given version.
        type: str
    architecture:
        description:
            - A filter to return software packages that match the given architecture.
        type: str
        choices:
            - "I386"
            - "I686"
            - "AARCH64"
            - "X86_64"
            - "SRC"
            - "NOARCH"
            - "OTHER"
    is_latest:
        description:
            - Indicates whether to list only the latest versions of packages, module streams, and stream profiles.
        type: bool
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
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort packages by. Only one sort order may be provided. Default order for displayName is ascending. If no value is specified
              displayName is default.
        type: str
        choices:
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List all_software_packages
  oci_os_management_hub_all_software_package_facts:

    # optional
    display_name: display_name_example
    display_name_contains: display_name_contains_example
    version: version_example
    architecture: I386
    is_latest: true
    os_family: ORACLE_LINUX_9
    sort_order: ASC
    sort_by: displayName

"""

RETURN = """
all_software_packages:
    description:
        - List of AllSoftwarePackage resources
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - Package name.
            returned: on success
            type: str
            sample: display_name_example
        name:
            description:
                - Unique identifier for the package. Note that this is not an OCID.
            returned: on success
            type: str
            sample: name_example
        type:
            description:
                - Type of the package.
            returned: on success
            type: str
            sample: type_example
        version:
            description:
                - Version of the package.
            returned: on success
            type: str
            sample: version_example
        architecture:
            description:
                - The architecture for which this software was built.
            returned: on success
            type: str
            sample: I386
        checksum:
            description:
                - Checksum of the package.
            returned: on success
            type: str
            sample: checksum_example
        checksum_type:
            description:
                - Type of the checksum.
            returned: on success
            type: str
            sample: checksum_type_example
        is_latest:
            description:
                - Indicates whether this package is the latest version.
            returned: on success
            type: bool
            sample: true
        software_sources:
            description:
                - List of software sources that provide the software package. This property is deprecated and it will be removed in a future API release.
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
        os_families:
            description:
                - The OS families the package belongs to.
            returned: on success
            type: list
            sample: []
    sample: [{
        "display_name": "display_name_example",
        "name": "name_example",
        "type": "type_example",
        "version": "version_example",
        "architecture": "I386",
        "checksum": "checksum_example",
        "checksum_type": "checksum_type_example",
        "is_latest": true,
        "software_sources": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "software_source_type": "VENDOR",
            "is_mandatory_for_autonomous_linux": true
        }],
        "os_families": []
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


class OsManagementHubAllSoftwarePackageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "display_name_contains",
            "version",
            "architecture",
            "is_latest",
            "os_family",
            "sort_order",
            "sort_by",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_all_software_packages, **optional_kwargs
        )


OsManagementHubAllSoftwarePackageFactsHelperCustom = get_custom_class(
    "OsManagementHubAllSoftwarePackageFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubAllSoftwarePackageFactsHelperCustom,
    OsManagementHubAllSoftwarePackageFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            display_name=dict(type="str"),
            display_name_contains=dict(type="str"),
            version=dict(type="str"),
            architecture=dict(
                type="str",
                choices=["I386", "I686", "AARCH64", "X86_64", "SRC", "NOARCH", "OTHER"],
            ),
            is_latest=dict(type="bool"),
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
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["displayName"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="all_software_package",
        service_client_class=SoftwareSourceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(all_software_packages=result)


if __name__ == "__main__":
    main()
