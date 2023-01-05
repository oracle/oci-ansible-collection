#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_os_management_software_package_search_facts
short_description: Fetches details about one or multiple SoftwarePackageSearch resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SoftwarePackageSearch resources in Oracle Cloud Infrastructure
    - Searches all of the available Software Sources and returns any/all Software Packages matching
      the search criteria.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    software_package_name:
        description:
            - the identifier for the software package (not an OCID)
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
    cve_name:
        description:
            - "The name of the CVE as published.
              Example: `CVE-2006-4535`"
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
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List software_package_searches
  oci_os_management_software_package_search_facts:

    # optional
    software_package_name: software_package_name_example
    display_name: display_name_example
    cve_name: cve_name_example
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
software_package_searches:
    description:
        - List of SoftwarePackageSearch resources
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - Package name
            returned: on success
            type: str
            sample: display_name_example
        name:
            description:
                - "Unique identifier for the package. NOTE - This is not an OCID"
            returned: on success
            type: str
            sample: name_example
        type:
            description:
                - Type of the package
            returned: on success
            type: str
            sample: type_example
        version:
            description:
                - Version of the package
            returned: on success
            type: str
            sample: version_example
        architecture:
            description:
                - the architecture for which this software was built
            returned: on success
            type: str
            sample: architecture_example
        summary:
            description:
                - a summary description of the software package
            returned: on success
            type: str
            sample: summary_example
        advisory_type:
            description:
                - Type of the erratum.
            returned: on success
            type: str
            sample: SECURITY
        errata:
            description:
                - List of errata containing this software package
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - unique identifier that is immutable on creation
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User friendly name
                    returned: on success
                    type: str
                    sample: display_name_example
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
                    type: str
                    sample: name_example
                id:
                    description:
                        - software source identifier
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "display_name": "display_name_example",
        "name": "name_example",
        "type": "type_example",
        "version": "version_example",
        "architecture": "architecture_example",
        "summary": "summary_example",
        "advisory_type": "SECURITY",
        "errata": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "software_sources": [{
            "name": "name_example",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management import OsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SoftwarePackageSearchFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "software_package_name",
            "display_name",
            "cve_name",
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
            self.client.search_software_packages, **optional_kwargs
        )


SoftwarePackageSearchFactsHelperCustom = get_custom_class(
    "SoftwarePackageSearchFactsHelperCustom"
)


class ResourceFactsHelper(
    SoftwarePackageSearchFactsHelperCustom, SoftwarePackageSearchFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            software_package_name=dict(type="str"),
            display_name=dict(type="str"),
            cve_name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="software_package_search",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(software_package_searches=result)


if __name__ == "__main__":
    main()
