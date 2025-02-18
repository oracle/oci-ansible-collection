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
module: oci_os_management_hub_software_package_by_name_facts
short_description: Fetches details about a SoftwarePackageByName resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a SoftwarePackageByName resource in Oracle Cloud Infrastructure
    - Returns information about the specified software package based on its fully qualified name.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    software_package_name:
        description:
            - The name of the software package.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific software_package_by_name
  oci_os_management_hub_software_package_by_name_facts:
    # required
    software_package_name: software_package_name_example

"""

RETURN = """
software_package_by_name:
    description:
        - SoftwarePackageByName resource
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
                - The architecture for which this software was built
            returned: on success
            type: str
            sample: I386
        last_modified_date:
            description:
                - The date and time the package was last modified (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: last_modified_date_example
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
        description:
            description:
                - Description of the package.
            returned: on success
            type: str
            sample: description_example
        size_in_bytes:
            description:
                - Size of the package in bytes.
            returned: on success
            type: int
            sample: 56
        dependencies:
            description:
                - List of dependencies for the software package.
            returned: on success
            type: complex
            contains:
                dependency:
                    description:
                        - The software package's dependency.
                    returned: on success
                    type: str
                    sample: dependency_example
                dependency_type:
                    description:
                        - The type of the dependency.
                    returned: on success
                    type: str
                    sample: dependency_type_example
                dependency_modifier:
                    description:
                        - The modifier for the dependency.
                    returned: on success
                    type: str
                    sample: dependency_modifier_example
        files:
            description:
                - List of files for the software package.
            returned: on success
            type: complex
            contains:
                path:
                    description:
                        - File path.
                    returned: on success
                    type: str
                    sample: path_example
                type:
                    description:
                        - Type of the file.
                    returned: on success
                    type: str
                    sample: type_example
                time_modified:
                    description:
                        - The date and time the file was last modified (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                checksum:
                    description:
                        - Checksum of the file.
                    returned: on success
                    type: str
                    sample: checksum_example
                checksum_type:
                    description:
                        - Type of the checksum.
                    returned: on success
                    type: str
                    sample: checksum_type_example
                size_in_bytes:
                    description:
                        - Size of the file in bytes.
                    returned: on success
                    type: int
                    sample: 56
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
        is_latest:
            description:
                - Indicates whether this package is the latest version.
            returned: on success
            type: bool
            sample: true
        os_families:
            description:
                - The OS families the package belongs to.
            returned: on success
            type: list
            sample: []
    sample: {
        "display_name": "display_name_example",
        "name": "name_example",
        "type": "type_example",
        "version": "version_example",
        "architecture": "I386",
        "last_modified_date": "last_modified_date_example",
        "checksum": "checksum_example",
        "checksum_type": "checksum_type_example",
        "description": "description_example",
        "size_in_bytes": 56,
        "dependencies": [{
            "dependency": "dependency_example",
            "dependency_type": "dependency_type_example",
            "dependency_modifier": "dependency_modifier_example"
        }],
        "files": [{
            "path": "path_example",
            "type": "type_example",
            "time_modified": "2013-10-20T19:20:30+01:00",
            "checksum": "checksum_example",
            "checksum_type": "checksum_type_example",
            "size_in_bytes": 56
        }],
        "software_sources": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "software_source_type": "VENDOR",
            "is_mandatory_for_autonomous_linux": true
        }],
        "is_latest": true,
        "os_families": []
    }
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


class OsManagementHubSoftwarePackageByNameFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "software_package_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_software_package_by_name,
            software_package_name=self.module.params.get("software_package_name"),
        )


OsManagementHubSoftwarePackageByNameFactsHelperCustom = get_custom_class(
    "OsManagementHubSoftwarePackageByNameFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubSoftwarePackageByNameFactsHelperCustom,
    OsManagementHubSoftwarePackageByNameFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            software_package_name=dict(type="str", required=True),
            name=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="software_package_by_name",
        service_client_class=SoftwareSourceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(software_package_by_name=result)


if __name__ == "__main__":
    main()
