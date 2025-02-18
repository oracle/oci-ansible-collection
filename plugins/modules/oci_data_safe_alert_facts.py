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
module: oci_data_safe_alert_facts
short_description: Fetches details about one or multiple Alert resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Alert resources in Oracle Cloud Infrastructure
    - Gets a list of all alerts.
    - If I(alert_id) is specified, the details of a single Alert will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    alert_id:
        description:
            - The OCID of alert.
            - Required to get a specific alert.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - A filter to return only resources that match the specified compartment OCID.
            - Required to list multiple alerts.
        type: str
    compartment_id_in_subtree:
        description:
            - Default is false.
              When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the
              'accessLevel' setting.
        type: bool
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
    field:
        description:
            - Specifies a subset of fields to be returned in the response.
        type: list
        elements: str
        choices:
            - "id"
            - "displayName"
            - "alertType"
            - "targetIds"
            - "targetNames"
            - "severity"
            - "status"
            - "operationTime"
            - "operation"
            - "operationStatus"
            - "timeCreated"
            - "timeUpdated"
            - "policyId"
            - "lifecycleState"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific alert
  oci_data_safe_alert_facts:
    # required
    alert_id: "ocid1.alert.oc1..xxxxxxEXAMPLExxxxxx"

- name: List alerts
  oci_data_safe_alert_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id_in_subtree: true
    access_level: RESTRICTED
    sort_order: ASC
    sort_by: displayName
    scim_query: scim_query_example
    field: [ "id" ]

"""

RETURN = """
alerts:
    description:
        - List of Alert resources
    returned: on success
    type: complex
    contains:
        resource_name:
            description:
                - The resource endpoint that triggered the alert.
                - Returned for get operation
            returned: on success
            type: str
            sample: resource_name_example
        comment:
            description:
                - A comment for the alert. Entered by the user.
                - Returned for get operation
            returned: on success
            type: str
            sample: comment_example
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        id:
            description:
                - The OCID of the alert.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - The status of the alert.
            returned: on success
            type: str
            sample: OPEN
        display_name:
            description:
                - The display name of the alert.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The description of the alert.
            returned: on success
            type: str
            sample: description_example
        severity:
            description:
                - Severity level of the alert.
            returned: on success
            type: str
            sample: CRITICAL
        operation_time:
            description:
                - Creation date and time of the operation that triggered alert, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        operation:
            description:
                - The operation (event) that triggered alert.
            returned: on success
            type: str
            sample: operation_example
        operation_status:
            description:
                - The result of the operation (event) that triggered alert.
            returned: on success
            type: str
            sample: SUCCEEDED
        target_ids:
            description:
                - Array of OCIDs of the target database which are associated with the alert.
            returned: on success
            type: list
            sample: []
        target_names:
            description:
                - Array of names of the target database.
            returned: on success
            type: list
            sample: []
        policy_id:
            description:
                - The OCID of the policy that triggered alert.
            returned: on success
            type: str
            sample: "ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx"
        alert_type:
            description:
                - Type of the alert. Indicates the Data Safe feature triggering the alert.
            returned: on success
            type: str
            sample: AUDITING
        compartment_id:
            description:
                - The OCID of the compartment that contains the alert.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Creation date and time of the alert, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Last date and time the alert was updated, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the alert.
            returned: on success
            type: str
            sample: UPDATING
        feature_details:
            description:
                - "Map that contains maps of values.
                   Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {}
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "resource_name": "resource_name_example",
        "comment": "comment_example",
        "system_tags": {},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "OPEN",
        "display_name": "display_name_example",
        "description": "description_example",
        "severity": "CRITICAL",
        "operation_time": "2013-10-20T19:20:30+01:00",
        "operation": "operation_example",
        "operation_status": "SUCCEEDED",
        "target_ids": [],
        "target_names": [],
        "policy_id": "ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx",
        "alert_type": "AUDITING",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "UPDATING",
        "feature_details": {},
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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


class DataSafeAlertFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "alert_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_alert, alert_id=self.module.params.get("alert_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id_in_subtree",
            "access_level",
            "sort_order",
            "sort_by",
            "scim_query",
            "field",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_alerts,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataSafeAlertFactsHelperCustom = get_custom_class("DataSafeAlertFactsHelperCustom")


class ResourceFactsHelper(DataSafeAlertFactsHelperCustom, DataSafeAlertFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            alert_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            compartment_id_in_subtree=dict(type="bool"),
            access_level=dict(type="str", choices=["RESTRICTED", "ACCESSIBLE"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["displayName", "timeCreated"]),
            scim_query=dict(type="str"),
            field=dict(
                type="list",
                elements="str",
                choices=[
                    "id",
                    "displayName",
                    "alertType",
                    "targetIds",
                    "targetNames",
                    "severity",
                    "status",
                    "operationTime",
                    "operation",
                    "operationStatus",
                    "timeCreated",
                    "timeUpdated",
                    "policyId",
                    "lifecycleState",
                ],
            ),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="alert",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(alerts=result)


if __name__ == "__main__":
    main()
