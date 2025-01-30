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
module: oci_os_management_hub_managed_instance_content_facts
short_description: Fetches details about a ManagedInstanceContent resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ManagedInstanceContent resource in Oracle Cloud Infrastructure
    - Returns a report for a single managed instance whose associated erratas match the given filters. You can select CSV, XML, or JSON format.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dest:
        description:
            - The destination file path to write the output. The file will be created if it does not exist. If the file already exists, the content will be
              overwritten.
        type: str
        required: true
    managed_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance.
        type: str
        aliases: ["id"]
        required: true
    vulnerability_type:
        description:
            - A filter to return only vulnerabilities matching the given types.
        type: list
        elements: str
        choices:
            - "SECURITY"
            - "BUGFIX"
            - "ENHANCEMENT"
            - "OTHER"
            - "ALL"
        required: true
    advisory_name:
        description:
            - The assigned erratum name. It's unique and not changeable.
            - "Example: `ELSA-2020-5804`"
        type: list
        elements: str
    advisory_name_contains:
        description:
            - A filter to return resources that may partially match the erratum advisory name given.
        type: str
    advisory_type:
        description:
            - A filter to return only errata that match the given advisory types.
        type: list
        elements: str
        choices:
            - "SECURITY"
            - "BUGFIX"
            - "ENHANCEMENT"
    vulnerability_name:
        description:
            - A filter to return vulnerabilities that match the given name. For Linux instances, this refers to the advisory name. For Windows instances, this
              refers to the Windows update display name.
        type: list
        elements: str
    vulnerability_name_contains:
        description:
            - A filter to return vulnerabilities that partially match the given name. For Linux instances, this refers to the advisory name. For Windows
              instances, this refers to the Windows update display name.
        type: str
    report_format:
        description:
            - The format of the report to download. Default is CSV.
        type: str
        choices:
            - "csv"
            - "json"
            - "xml"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific managed_instance_content
  oci_os_management_hub_managed_instance_content_facts:
    # required
    dest: /tmp/myfile
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    vulnerability_type: [ "SECURITY" ]

    # optional
    advisory_name: [ "advisory_name_example" ]
    advisory_name_contains: advisory_name_contains_example
    advisory_type: [ "SECURITY" ]
    vulnerability_name: [ "vulnerability_name_example" ]
    vulnerability_name_contains: vulnerability_name_contains_example
    report_format: csv

"""


from ansible.module_utils._text import to_bytes
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import ReportingManagedInstanceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubManagedInstanceContentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "managed_instance_id",
            "vulnerability_type",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "advisory_name",
            "advisory_name_contains",
            "advisory_type",
            "vulnerability_name",
            "vulnerability_name_contains",
            "report_format",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_instance_content,
            managed_instance_id=self.module.params.get("managed_instance_id"),
            vulnerability_type=self.module.params.get("vulnerability_type"),
            **optional_kwargs
        )

    def get(self):
        response = self.get_resource().data
        dest = self.module.params.get("dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None


OsManagementHubManagedInstanceContentFactsHelperCustom = get_custom_class(
    "OsManagementHubManagedInstanceContentFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubManagedInstanceContentFactsHelperCustom,
    OsManagementHubManagedInstanceContentFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dest=dict(type="str", required=True),
            managed_instance_id=dict(aliases=["id"], type="str", required=True),
            vulnerability_type=dict(
                type="list",
                elements="str",
                required=True,
                choices=["SECURITY", "BUGFIX", "ENHANCEMENT", "OTHER", "ALL"],
            ),
            advisory_name=dict(type="list", elements="str"),
            advisory_name_contains=dict(type="str"),
            advisory_type=dict(
                type="list",
                elements="str",
                choices=["SECURITY", "BUGFIX", "ENHANCEMENT"],
            ),
            vulnerability_name=dict(type="list", elements="str"),
            vulnerability_name_contains=dict(type="str"),
            report_format=dict(type="str", choices=["csv", "json", "xml"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="managed_instance_content",
        service_client_class=ReportingManagedInstanceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(managed_instance_content=result)


if __name__ == "__main__":
    main()
