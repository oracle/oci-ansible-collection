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
module: oci_os_management_hub_managed_instance_analytic_facts
short_description: Fetches details about one or multiple ManagedInstanceAnalytic resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagedInstanceAnalytic resources in Oracle Cloud Infrastructure
    - Returns a list of user specified metrics for a collection of managed instances.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    metric_names:
        description:
            - A filter to return only metrics whose name matches the given metric names.
        type: list
        elements: str
        choices:
            - "TOTAL_INSTANCE_COUNT"
            - "INSTANCE_WITH_AVAILABLE_SECURITY_UPDATES_COUNT"
            - "INSTANCE_WITH_AVAILABLE_BUGFIX_UPDATES_COUNT"
            - "NORMAL_INSTANCE_COUNT"
            - "ERROR_INSTANCE_COUNT"
            - "WARNING_INSTANCE_COUNT"
            - "UNREACHABLE_INSTANCE_COUNT"
            - "REGISTRATION_FAILED_INSTANCE_COUNT"
            - "DELETING_INSTANCE_COUNT"
            - "ONBOARDING_INSTANCE_COUNT"
            - "INSTANCE_SECURITY_UPDATES_COUNT"
            - "INSTANCE_BUGFIX_UPDATES_COUNT"
            - "INSTANCE_SECURITY_ADVISORY_COUNT"
            - "INSTANCE_BUGFIX_ADVISORY_COUNT"
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
    display_name:
        description:
            - A filter to return resources that match the given display names.
        type: list
        elements: str
    display_name_contains:
        description:
            - A filter to return resources that may partially match the given display name.
        type: str
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. The default is to sort in ascending order by metricName (previously name, which is now
              depricated).
              You can also sort by displayName (default is ascending order).
        type: str
        choices:
            - "name"
            - "metricName"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List managed_instance_analytics
  oci_os_management_hub_managed_instance_analytic_facts:
    # required
    metric_names: [ "TOTAL_INSTANCE_COUNT" ]

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_environment_id: "ocid1.lifecycleenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_stage_id: "ocid1.lifecyclestage.oc1..xxxxxxEXAMPLExxxxxx"
    status: [ "NORMAL" ]
    location: [ "ON_PREMISE" ]
    location_not_equal_to: [ "ON_PREMISE" ]
    os_family: [ "ORACLE_LINUX_9" ]
    is_managed_by_autonomous_linux: true
    display_name: [ "display_name_example" ]
    display_name_contains: display_name_contains_example
    sort_by: name
    sort_order: ASC

"""

RETURN = """
managed_instance_analytics:
    description:
        - List of ManagedInstanceAnalytic resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of this metric.
            returned: on success
            type: str
            sample: TOTAL_INSTANCE_COUNT
        dimensions:
            description:
                - Qualifiers provided in a metric definition. Available dimensions vary by metric namespace.
                  Each dimension takes the form of a key-value pair.
                - "Example: `\\"managedInstanceId\\": \\"ocid1.managementagent.123\\"`"
            returned: on success
            type: dict
            sample: {}
        count:
            description:
                - The value of this metric.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "name": "TOTAL_INSTANCE_COUNT",
        "dimensions": {},
        "count": 56
    }]
"""

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


class OsManagementHubManagedInstanceAnalyticFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "metric_names",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "managed_instance_group_id",
            "lifecycle_environment_id",
            "lifecycle_stage_id",
            "status",
            "location",
            "location_not_equal_to",
            "os_family",
            "is_managed_by_autonomous_linux",
            "display_name",
            "display_name_contains",
            "sort_by",
            "sort_order",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_managed_instance_analytics,
            metric_names=self.module.params.get("metric_names"),
            **optional_kwargs
        )


OsManagementHubManagedInstanceAnalyticFactsHelperCustom = get_custom_class(
    "OsManagementHubManagedInstanceAnalyticFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubManagedInstanceAnalyticFactsHelperCustom,
    OsManagementHubManagedInstanceAnalyticFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            metric_names=dict(
                type="list",
                elements="str",
                required=True,
                choices=[
                    "TOTAL_INSTANCE_COUNT",
                    "INSTANCE_WITH_AVAILABLE_SECURITY_UPDATES_COUNT",
                    "INSTANCE_WITH_AVAILABLE_BUGFIX_UPDATES_COUNT",
                    "NORMAL_INSTANCE_COUNT",
                    "ERROR_INSTANCE_COUNT",
                    "WARNING_INSTANCE_COUNT",
                    "UNREACHABLE_INSTANCE_COUNT",
                    "REGISTRATION_FAILED_INSTANCE_COUNT",
                    "DELETING_INSTANCE_COUNT",
                    "ONBOARDING_INSTANCE_COUNT",
                    "INSTANCE_SECURITY_UPDATES_COUNT",
                    "INSTANCE_BUGFIX_UPDATES_COUNT",
                    "INSTANCE_SECURITY_ADVISORY_COUNT",
                    "INSTANCE_BUGFIX_ADVISORY_COUNT",
                ],
            ),
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
            display_name=dict(type="list", elements="str"),
            display_name_contains=dict(type="str"),
            sort_by=dict(type="str", choices=["name", "metricName", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="managed_instance_analytic",
        service_client_class=ReportingManagedInstanceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(managed_instance_analytics=result)


if __name__ == "__main__":
    main()
