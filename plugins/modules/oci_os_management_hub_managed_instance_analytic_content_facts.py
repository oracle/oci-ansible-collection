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
module: oci_os_management_hub_managed_instance_analytic_content_facts
short_description: Fetches details about a ManagedInstanceAnalyticContent resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ManagedInstanceAnalyticContent resource in Oracle Cloud Infrastructure
    - Returns a report of managed instances matching the given filters. You can select CSV, XML, or JSON format.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dest:
        description:
            - The destination file path to write the output. The file will be created if it does not exist. If the file already exists, the content will be
              overwritten.
        type: str
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
              This filter returns only resources contained within the specified compartment.
        type: str
    managed_instance_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group. This filter returns
              resources associated with this group.
        type: str
    lifecycle_environment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the lifecycle environment. This filter returns only
              resource contained with the specified lifecycle environment.
        type: str
    lifecycle_stage_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the lifecycle stage. This resource returns resources
              associated with this lifecycle stage.
        type: str
    status:
        description:
            - A filter to return only managed instances whose status matches the status provided.
        type: list
        elements: str
        choices:
            - "NORMAL"
            - "UNREACHABLE"
            - "ERROR"
            - "WARNING"
            - "REGISTRATION_ERROR"
            - "DELETING"
            - "ONBOARDING"
    display_name:
        description:
            - A filter to return resources that match the given display names.
        type: list
        elements: str
        aliases: ["name"]
    display_name_contains:
        description:
            - A filter to return resources that may partially match the given display name.
        type: str
    security_updates_available_equals_to:
        description:
            - A filter to return instances that have the specified number of available security updates.
        type: int
    bug_updates_available_equals_to:
        description:
            - A filter to return instances that have the specified number of available bug updates.
        type: int
    security_updates_available_greater_than:
        description:
            - A filter to return instances that have more available security updates than the number specified.
        type: int
    bug_updates_available_greater_than:
        description:
            - A filter to return instances that have more available bug updates than the number specified.
        type: int
    location:
        description:
            - A filter to return only resources whose location matches the given value.
        type: list
        elements: str
        choices:
            - "ON_PREMISE"
            - "OCI_COMPUTE"
            - "AZURE"
            - "EC2"
            - "GCP"
    location_not_equal_to:
        description:
            - A filter to return only resources whose location does not match the given value.
        type: list
        elements: str
        choices:
            - "ON_PREMISE"
            - "OCI_COMPUTE"
            - "AZURE"
            - "EC2"
            - "GCP"
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
    is_managed_by_autonomous_linux:
        description:
            - Indicates whether to list only resources managed by the Autonomous Linux service.
        type: bool
    report_format:
        description:
            - The format of the report to download. Default is CSV.
        type: str
        choices:
            - "csv"
            - "json"
            - "xml"
    report_type:
        description:
            - The type of the report the user wants to download. Default is ALL.
        type: str
        choices:
            - "SECURITY"
            - "BUGFIX"
            - "ACTIVITY"
            - "ALL"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific managed_instance_analytic_content
  oci_os_management_hub_managed_instance_analytic_content_facts:
    # required
    dest: /tmp/myfile

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_environment_id: "ocid1.lifecycleenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_stage_id: "ocid1.lifecyclestage.oc1..xxxxxxEXAMPLExxxxxx"
    status: [ "NORMAL" ]
    display_name: [ "display_name_example" ]
    display_name_contains: display_name_contains_example
    security_updates_available_equals_to: 56
    bug_updates_available_equals_to: 56
    security_updates_available_greater_than: 56
    bug_updates_available_greater_than: 56
    location: [ "ON_PREMISE" ]
    location_not_equal_to: [ "ON_PREMISE" ]
    os_family: [ "ORACLE_LINUX_9" ]
    is_managed_by_autonomous_linux: true
    report_format: csv
    report_type: SECURITY

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


class OsManagementHubManagedInstanceAnalyticContentFactsHelperGen(
    OCIResourceFactsHelperBase
):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return []

    def get_resource(self):
        optional_get_method_params = [
            "compartment_id",
            "managed_instance_group_id",
            "lifecycle_environment_id",
            "lifecycle_stage_id",
            "status",
            "display_name",
            "display_name_contains",
            "security_updates_available_equals_to",
            "bug_updates_available_equals_to",
            "security_updates_available_greater_than",
            "bug_updates_available_greater_than",
            "location",
            "location_not_equal_to",
            "os_family",
            "is_managed_by_autonomous_linux",
            "report_format",
            "report_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_instance_analytic_content, **optional_kwargs
        )

    def get(self):
        response = self.get_resource().data
        dest = self.module.params.get("dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None


OsManagementHubManagedInstanceAnalyticContentFactsHelperCustom = get_custom_class(
    "OsManagementHubManagedInstanceAnalyticContentFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubManagedInstanceAnalyticContentFactsHelperCustom,
    OsManagementHubManagedInstanceAnalyticContentFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dest=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            managed_instance_group_id=dict(type="str"),
            lifecycle_environment_id=dict(type="str"),
            lifecycle_stage_id=dict(type="str"),
            status=dict(
                type="list",
                elements="str",
                choices=[
                    "NORMAL",
                    "UNREACHABLE",
                    "ERROR",
                    "WARNING",
                    "REGISTRATION_ERROR",
                    "DELETING",
                    "ONBOARDING",
                ],
            ),
            display_name=dict(aliases=["name"], type="list", elements="str"),
            display_name_contains=dict(type="str"),
            security_updates_available_equals_to=dict(type="int"),
            bug_updates_available_equals_to=dict(type="int"),
            security_updates_available_greater_than=dict(type="int"),
            bug_updates_available_greater_than=dict(type="int"),
            location=dict(
                type="list",
                elements="str",
                choices=["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"],
            ),
            location_not_equal_to=dict(
                type="list",
                elements="str",
                choices=["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"],
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
            is_managed_by_autonomous_linux=dict(type="bool"),
            report_format=dict(type="str", choices=["csv", "json", "xml"]),
            report_type=dict(
                type="str", choices=["SECURITY", "BUGFIX", "ACTIVITY", "ALL"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="managed_instance_analytic_content",
        service_client_class=ReportingManagedInstanceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(managed_instance_analytic_content=result)


if __name__ == "__main__":
    main()
