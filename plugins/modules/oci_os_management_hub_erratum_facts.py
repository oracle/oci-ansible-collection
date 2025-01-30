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
module: oci_os_management_hub_erratum_facts
short_description: Fetches details about one or multiple Erratum resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Erratum resources in Oracle Cloud Infrastructure
    - Lists all of the currently available errata. Filter the list against a variety of criteria including but not
      limited to its name, classification type, advisory severity, and OS family.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment. This parameter is required and returns
              only resources contained within the specified compartment.
        type: str
        required: true
    name:
        description:
            - The assigned erratum name. It's unique and not changeable.
            - "Example: `ELSA-2020-5804`"
        type: list
        elements: str
    name_contains:
        description:
            - A filter to return resources that may partially match the erratum name given.
        type: str
    classification_type:
        description:
            - A filter to return only packages that match the given update classification type.
        type: list
        elements: str
        choices:
            - "SECURITY"
            - "BUGFIX"
            - "ENHANCEMENT"
            - "OTHER"
    advisory_type:
        description:
            - A filter to return only errata that match the given advisory types.
        type: list
        elements: str
        choices:
            - "SECURITY"
            - "BUGFIX"
            - "ENHANCEMENT"
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
    advisory_severity:
        description:
            - The advisory severity.
        type: list
        elements: str
        choices:
            - "LOW"
            - "MODERATE"
            - "IMPORTANT"
            - "CRITICAL"
    time_issue_date_start:
        description:
            - The issue date after which to list all errata, in ISO 8601 format
            - "Example: 2017-07-14T02:40:00.000Z"
        type: str
    time_issue_date_end:
        description:
            - The issue date before which to list all errata, in ISO 8601 format
            - "Example: 2017-07-14T02:40:00.000Z"
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
            - The field to sort errata by. Only one sort order may be provided. Default order for timeIssued is descending. Default order for name is ascending.
              If no value is specified timeIssued is default.
        type: str
        choices:
            - "timeIssued"
            - "name"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List erratums
  oci_os_management_hub_erratum_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: [ "name_example" ]
    name_contains: name_contains_example
    classification_type: [ "SECURITY" ]
    advisory_type: [ "SECURITY" ]
    os_family: ORACLE_LINUX_9
    advisory_severity: [ "LOW" ]
    time_issue_date_start: 2013-10-20T19:20:30+01:00
    time_issue_date_end: 2013-10-20T19:20:30+01:00
    sort_order: ASC
    sort_by: timeIssued

"""

RETURN = """
erratums:
    description:
        - List of Erratum resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Advisory name.
            returned: on success
            type: str
            sample: name_example
        synopsis:
            description:
                - Summary description of the erratum.
            returned: on success
            type: str
            sample: synopsis_example
        time_issued:
            description:
                - The date and time the erratum was issued (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the erratum was updated (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        classification_type:
            description:
                - Type of the erratum. This property is deprecated and it will be removed in a future API release. Please refer to the advisoryType property
                  instead.
            returned: on success
            type: str
            sample: SECURITY
        related_cves:
            description:
                - List of CVEs applicable to this erratum.
            returned: on success
            type: list
            sample: []
        os_families:
            description:
                - List of affected OS families.
            returned: on success
            type: list
            sample: []
        advisory_severity:
            description:
                - The severity advisory. Only valid for security type advisories.
            returned: on success
            type: str
            sample: LOW
        advisory_type:
            description:
                - The advisory type of the erratum.
            returned: on success
            type: str
            sample: SECURITY
    sample: [{
        "name": "name_example",
        "synopsis": "synopsis_example",
        "time_issued": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "classification_type": "SECURITY",
        "related_cves": [],
        "os_families": [],
        "advisory_severity": "LOW",
        "advisory_type": "SECURITY"
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


class OsManagementHubErratumFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "name_contains",
            "classification_type",
            "advisory_type",
            "os_family",
            "advisory_severity",
            "time_issue_date_start",
            "time_issue_date_end",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_errata,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OsManagementHubErratumFactsHelperCustom = get_custom_class(
    "OsManagementHubErratumFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubErratumFactsHelperCustom, OsManagementHubErratumFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            name=dict(type="list", elements="str"),
            name_contains=dict(type="str"),
            classification_type=dict(
                type="list",
                elements="str",
                choices=["SECURITY", "BUGFIX", "ENHANCEMENT", "OTHER"],
            ),
            advisory_type=dict(
                type="list",
                elements="str",
                choices=["SECURITY", "BUGFIX", "ENHANCEMENT"],
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
            advisory_severity=dict(
                type="list",
                elements="str",
                choices=["LOW", "MODERATE", "IMPORTANT", "CRITICAL"],
            ),
            time_issue_date_start=dict(type="str"),
            time_issue_date_end=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeIssued", "name"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="erratum",
        service_client_class=SoftwareSourceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(erratums=result)


if __name__ == "__main__":
    main()
