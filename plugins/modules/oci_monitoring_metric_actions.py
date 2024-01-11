#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_monitoring_metric_actions
short_description: Perform actions on a Metric resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Metric resource in Oracle Cloud Infrastructure
    - "For I(action=list), returns metric definitions that match the criteria specified in the request. Compartment OCID required.
      For more information, see
      L(Listing Metric Definitions,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/list-metric.htm).
      For information about metrics, see
      L(Metrics Overview,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MetricsOverview).
      For important limits information, see
      L(Limits on Monitoring,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits).
      Transactions Per Second (TPS) per-tenancy limit for this operation: 10."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the
              resources monitored by the metric that you are searching for. Use tenancyId to search in
              the root compartment.
            - "Example: `ocid1.compartment.oc1..exampleuniqueID`"
        type: str
        required: true
    name:
        description:
            - The metric name to use when searching for metric definitions.
            - "Example: `CpuUtilization`"
        type: str
    namespace:
        description:
            - The source service or application to use when searching for metric definitions.
            - "Example: `oci_computeagent`"
        type: str
    resource_group:
        description:
            - Resource group that you want to match. A null value returns only metric data that has no resource groups. The specified resource group must exist
              in the definition of the posted metric. Only one resource group can be applied per metric.
              A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens
              (-), and dollar signs ($).
            - "Example: `frontend-fleet`"
        type: str
    dimension_filters:
        description:
            - Qualifiers that you want to use when searching for metric definitions.
              Available dimensions vary by metric namespace. Each dimension takes the form of a key-value pair.
            - "Example: `\\"resourceId\\": \\"ocid1.instance.region1.phx.exampleuniqueID\\"`"
        type: dict
    group_by:
        description:
            - "Group metrics by these fields in the response. For example, to list all metric namespaces available
                        in a compartment, groupBy the \\"namespace\\" field. Supported fields: namespace, name, resourceGroup.
              If `groupBy` is used, then `dimensionFilters` is ignored."
            - "Example - group by namespace:
              `[ \\"namespace\\" ]`"
        type: list
        elements: str
    sort_by:
        description:
            - The field to use when sorting returned metric definitions. Only one sorting level is provided.
            - "Example: `NAMESPACE`"
        type: str
        choices:
            - "NAMESPACE"
            - "NAME"
            - "RESOURCEGROUP"
    sort_order:
        description:
            - The sort order to use when sorting returned metric definitions. Ascending (ASC) or
              descending (DESC).
            - "Example: `ASC`"
        type: str
        choices:
            - "ASC"
            - "DESC"
    compartment_id_in_subtree:
        description:
            - When true, returns resources from all compartments and subcompartments. The parameter can
              only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment).
              A true value requires the user to have tenancy-level permissions. If this requirement is not met,
              then the call is rejected. When false, returns resources from only the compartment specified in
              compartmentId. Default is false.
        type: bool
    action:
        description:
            - The action to perform on the Metric.
        type: str
        required: true
        choices:
            - "list"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action list on metric
  oci_monitoring_metric_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: list

    # optional
    name: name_example
    namespace: namespace_example
    resource_group: resource_group_example
    dimension_filters: null
    group_by: [ "group_by_example" ]
    sort_by: NAMESPACE
    sort_order: ASC
    compartment_id_in_subtree: true

"""

RETURN = """
metric:
    description:
        - Details of the Metric resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the metric.
                - "Example: `CpuUtilization`"
            returned: on success
            type: str
            sample: name_example
        namespace:
            description:
                - The source service or application emitting the metric.
                - "Example: `oci_computeagent`"
            returned: on success
            type: str
            sample: namespace_example
        resource_group:
            description:
                - Resource group provided with the posted metric. A resource group is a custom string that you can match when retrieving custom metrics. Only
                  one resource group can be applied per metric.
                  A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_),
                  hyphens (-), and dollar signs ($).
                - "Example: `frontend-fleet`"
            returned: on success
            type: str
            sample: resource_group_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing
                  the resources monitored by the metric.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        dimensions:
            description:
                - Qualifiers provided in a metric definition. Available dimensions vary by metric namespace.
                  Each dimension takes the form of a key-value pair.
                - "Example: `\\"resourceId\\": \\"ocid1.instance.region1.phx.exampleuniqueID\\"`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "name": "name_example",
        "namespace": "namespace_example",
        "resource_group": "resource_group_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "dimensions": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.monitoring import MonitoringClient
    from oci.monitoring.models import ListMetricsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MetricActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        list
    """

    def list(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ListMetricsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.list_metrics,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compartment_id=self.module.params.get("compartment_id"),
                list_metrics_details=action_details,
                compartment_id_in_subtree=self.module.params.get(
                    "compartment_id_in_subtree"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


MetricActionsHelperCustom = get_custom_class("MetricActionsHelperCustom")


class ResourceHelper(MetricActionsHelperCustom, MetricActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            name=dict(type="str"),
            namespace=dict(type="str"),
            resource_group=dict(type="str"),
            dimension_filters=dict(type="dict"),
            group_by=dict(type="list", elements="str"),
            sort_by=dict(type="str", choices=["NAMESPACE", "NAME", "RESOURCEGROUP"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            compartment_id_in_subtree=dict(type="bool"),
            action=dict(type="str", required=True, choices=["list"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="metric",
        service_client_class=MonitoringClient,
        namespace="monitoring",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
