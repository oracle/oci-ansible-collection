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
module: oci_data_safe_alert_analytics_facts
short_description: Fetches details about one or multiple AlertAnalytics resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AlertAnalytics resources in Oracle Cloud Infrastructure
    - Returns the aggregation details of the alerts.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - A filter to return only resources that match the specified compartment OCID.
        type: str
        required: true
    compartment_id_in_subtree:
        description:
            - Default is false.
              When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the
              'accessLevel' setting.
        type: bool
    time_started:
        description:
            - An optional filter to return audit events whose creation time in the database is greater than and equal to the date-time specified,
              in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
        type: str
    time_ended:
        description:
            - An optional filter to return audit events whose creation time in the database is less than and equal to the date-time specified,
              in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
        type: str
    query_time_zone:
        description:
            - Default time zone is UTC if no time zone provided. The date-time considerations of the resource will be in accordance with the specified time
              zone.
        type: str
    sort_order:
        description:
            - The sort order to use, either ascending (ASC) or descending (DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is
              default.
        type: str
        choices:
            - "displayName"
            - "timeCreated"
    access_level:
        description:
            - Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED.
              Setting this to ACCESSIBLE returns only those compartments for which the
              user has INSPECT permissions directly or indirectly (permissions can be on a
              resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
        type: str
        choices:
            - "RESTRICTED"
            - "ACCESSIBLE"
    scim_query:
        description:
            - The scimQuery query parameter accepts filter expressions that use the syntax described in Section 3.2.2.2
              of the System for Cross-Domain Identity Management (SCIM) specification, which is available
              at L(RFC3339,https://tools.ietf.org/html/draft-ietf-scim-api-12). In SCIM filtering expressions,
              text, date, and time values must be enclosed in quotation marks, with date and time values using ISO-8601 format.
              (Numeric and boolean values should not be quoted.)
            - "**Example:** |
              query=(timeCreated ge '2021-06-04T01-00-26') and (targetNames eq 'target_1')
              query=(featureDetails.userName eq \\"user\\") and (targetNames eq \\"target_1\\")
              Supported fields:
              severity
              status
              alertType
              targetIds
              targetNames
              operationTime
              lifecycleState
              displayName
              timeCreated
              timeUpdated
              featureDetails.* (* can be any field in nestedStrMap in Feature Attributes in Alert Summary. For example -
              userName,object,clientHostname,osUserName,clientIPs,clientId,commandText,commandParam,clientProgram,objectType,targetOwner)"
        type: str
    summary_field:
        description:
            - Specifies a subset of summarized fields to be returned in the response.
        type: list
        elements: str
        choices:
            - "alertType"
            - "targetIds"
            - "targetNames"
            - "alertSeverity"
            - "alertStatus"
            - "timeCreated"
            - "policyId"
            - "open"
            - "closed"
            - "critical"
            - "high"
            - "medium"
            - "low"
            - "alertcount"
    group_by:
        description:
            - A groupBy can only be used in combination with summaryField parameter.
              A groupBy value has to be a subset of the values mentioned in summaryField parameter.
        type: list
        elements: str
        choices:
            - "alertType"
            - "targetIds"
            - "targetNames"
            - "alertSeverity"
            - "alertStatus"
            - "timeCreated"
            - "policyId"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List alert_analytics
  oci_data_safe_alert_analytics_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id_in_subtree: true
    time_started: 2013-10-20T19:20:30+01:00
    time_ended: 2013-10-20T19:20:30+01:00
    query_time_zone: query_time_zone_example
    sort_order: ASC
    sort_by: displayName
    access_level: RESTRICTED
    scim_query: scim_query_example
    summary_field: [ "alertType" ]
    group_by: [ "alertType" ]

"""

RETURN = """
alert_analytics:
    description:
        - List of AlertAnalytics resources
    returned: on success
    type: complex
    contains:
        metric_name:
            description:
                - The name of the aggregation.
            returned: on success
            type: str
            sample: metric_name_example
        time_started:
            description:
                - The time at which the aggregation started.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ended:
            description:
                - The time at which the aggregation ended.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        count:
            description:
                - Total count of aggregated values.
            returned: on success
            type: int
            sample: 56
        dimensions:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                group_by:
                    description:
                        - GroupBy value used in aggregation.
                    returned: on success
                    type: dict
                    sample: {}
    sample: [{
        "metric_name": "metric_name_example",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_ended": "2013-10-20T19:20:30+01:00",
        "count": 56,
        "dimensions": {
            "group_by": {}
        }
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_safe import DataSafeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeAlertAnalyticsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id_in_subtree",
            "time_started",
            "time_ended",
            "query_time_zone",
            "sort_order",
            "sort_by",
            "access_level",
            "scim_query",
            "summary_field",
            "group_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_alert_analytics,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataSafeAlertAnalyticsFactsHelperCustom = get_custom_class(
    "DataSafeAlertAnalyticsFactsHelperCustom"
)


class ResourceFactsHelper(
    DataSafeAlertAnalyticsFactsHelperCustom, DataSafeAlertAnalyticsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            compartment_id_in_subtree=dict(type="bool"),
            time_started=dict(type="str"),
            time_ended=dict(type="str"),
            query_time_zone=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["displayName", "timeCreated"]),
            access_level=dict(type="str", choices=["RESTRICTED", "ACCESSIBLE"]),
            scim_query=dict(type="str"),
            summary_field=dict(
                type="list",
                elements="str",
                choices=[
                    "alertType",
                    "targetIds",
                    "targetNames",
                    "alertSeverity",
                    "alertStatus",
                    "timeCreated",
                    "policyId",
                    "open",
                    "closed",
                    "critical",
                    "high",
                    "medium",
                    "low",
                    "alertcount",
                ],
            ),
            group_by=dict(
                type="list",
                elements="str",
                choices=[
                    "alertType",
                    "targetIds",
                    "targetNames",
                    "alertSeverity",
                    "alertStatus",
                    "timeCreated",
                    "policyId",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="alert_analytics",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(alert_analytics=result)


if __name__ == "__main__":
    main()
