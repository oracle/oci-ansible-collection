#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_os_management_software_package_facts
short_description: Fetches details about one or multiple SoftwarePackage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SoftwarePackage resources in Oracle Cloud Infrastructure
    - Lists Software Packages in a Software Source
    - If I(software_package_name) is specified, the details of a single SoftwarePackage will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    software_source_id:
        description:
            - The OCID of the software source.
        type: str
        required: true
    software_package_name:
        description:
            - The id of the software package.
            - Required to get a specific software_package.
        type: str
    compartment_id:
        description:
            - The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is
              ascending. If no value is specified TIMECREATED is default.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List software_packages
  oci_os_management_software_package_facts:
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific software_package
  oci_os_management_software_package_facts:
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    software_package_name: software_package_name_example

"""

RETURN = """
software_packages:
    description:
        - List of SoftwarePackage resources
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - Package name
            returned: on success
            type: string
            sample: display_name_example
        name:
            description:
                - "Unique identifier for the package. NOTE - This is not an OCID"
            returned: on success
            type: string
            sample: name_example
        type:
            description:
                - Type of the package
            returned: on success
            type: string
            sample: type_example
        version:
            description:
                - Version of the package
            returned: on success
            type: string
            sample: version_example
        architecture:
            description:
                - the architecture for which this software was built
            returned: on success
            type: string
            sample: architecture_example
        last_modified_date:
            description:
                - date of the last update to the package
            returned: on success
            type: string
            sample: last_modified_date_example
        checksum:
            description:
                - checksum of the package
            returned: on success
            type: string
            sample: checksum_example
        checksum_type:
            description:
                - type of the checksum
            returned: on success
            type: string
            sample: checksum_type_example
        description:
            description:
                - description of the package
            returned: on success
            type: string
            sample: description_example
        size_in_bytes:
            description:
                - size of the package in bytes
            returned: on success
            type: int
            sample: 56
        dependencies:
            description:
                - list of dependencies for the software package
            returned: on success
            type: complex
            contains:
                dependency:
                    description:
                        - the software package's dependency
                    returned: on success
                    type: string
                    sample: dependency_example
                dependency_type:
                    description:
                        - the type of the dependency
                    returned: on success
                    type: string
                    sample: dependency_type_example
                dependency_modifier:
                    description:
                        - the modifier for the dependency
                    returned: on success
                    type: string
                    sample: dependency_modifier_example
        files:
            description:
                - list of files for the software package
            returned: on success
            type: complex
            contains:
                path:
                    description:
                        - file path
                    returned: on success
                    type: string
                    sample: path_example
                type:
                    description:
                        - type of the file
                    returned: on success
                    type: string
                    sample: type_example
                time_modified:
                    description:
                        - The date and time of the last modification to this file, as described
                          in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                checksum:
                    description:
                        - checksum of the file
                    returned: on success
                    type: string
                    sample: checksum_example
                checksum_type:
                    description:
                        - type of the checksum
                    returned: on success
                    type: string
                    sample: checksum_type_example
                size_in_bytes:
                    description:
                        - size of the file in bytes
                    returned: on success
                    type: int
                    sample: 56
        software_sources:
            description:
                - list of software sources that provide the software package
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - software source name
                    returned: on success
                    type: string
                    sample: name_example
                id:
                    description:
                        - software source identifier
                    returned: on success
                    type: string
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "display_name": "display_name_example",
        "name": "name_example",
        "type": "type_example",
        "version": "version_example",
        "architecture": "architecture_example",
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
            "name": "name_example",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.os_management import OsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SoftwarePackageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "software_source_id",
            "software_package_name",
        ]

    def get_required_params_for_list(self):
        return [
            "software_source_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_software_package,
            software_source_id=self.module.params.get("software_source_id"),
            software_package_name=self.module.params.get("software_package_name"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_software_source_packages,
            software_source_id=self.module.params.get("software_source_id"),
            **optional_kwargs
        )


SoftwarePackageFactsHelperCustom = get_custom_class("SoftwarePackageFactsHelperCustom")


class ResourceFactsHelper(
    SoftwarePackageFactsHelperCustom, SoftwarePackageFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            software_source_id=dict(type="str", required=True),
            software_package_name=dict(type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="software_package",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(software_packages=result)


if __name__ == "__main__":
    main()
