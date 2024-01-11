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
module: oci_opsi_exadata_insights_actions
short_description: Perform actions on an ExadataInsights resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an ExadataInsights resource in Oracle Cloud Infrastructure
    - For I(action=change), moves an Exadata insight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values
      of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    exadata_insight_id:
        description:
            - Unique Exadata insight identifier
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment into which the resource should be
              moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the ExadataInsights.
        type: str
        required: true
        choices:
            - "change"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change on exadata_insights
  oci_opsi_exadata_insights_actions:
    # required
    exadata_insight_id: "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change

"""

RETURN = """
exadata_insights:
    description:
        - Details of the ExadataInsights resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        enterprise_manager_identifier:
            description:
                - Enterprise Manager Unique Identifier
            returned: on success
            type: str
            sample: enterprise_manager_identifier_example
        enterprise_manager_entity_name:
            description:
                - Enterprise Manager Entity Name
            returned: on success
            type: str
            sample: enterprise_manager_entity_name_example
        enterprise_manager_entity_type:
            description:
                - Enterprise Manager Entity Type
            returned: on success
            type: str
            sample: enterprise_manager_entity_type_example
        enterprise_manager_entity_identifier:
            description:
                - Enterprise Manager Entity Unique Identifier
            returned: on success
            type: str
            sample: enterprise_manager_entity_identifier_example
        enterprise_manager_entity_display_name:
            description:
                - Enterprise Manager Entity Display Name
            returned: on success
            type: str
            sample: enterprise_manager_entity_display_name_example
        enterprise_manager_bridge_id:
            description:
                - OPSI Enterprise Manager Bridge OCID
            returned: on success
            type: str
            sample: "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx"
        is_auto_sync_enabled:
            description:
                - Set to true to enable automatic enablement and disablement of related targets from Enterprise Manager. New resources (e.g. Database Insights)
                  will be placed in the same compartment as the related Exadata Insight.
            returned: on success
            type: bool
            sample: true
        entity_source:
            description:
                - Source of the Exadata system.
            returned: on success
            type: str
            sample: EM_MANAGED_EXTERNAL_EXADATA
        id:
            description:
                - Exadata insight identifier
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment identifier of the Exadata insight resource
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        exadata_name:
            description:
                - The Exadata system name. If the Exadata systems managed by Enterprise Manager, the name is unique amongst the Exadata systems managed by the
                  same Enterprise Manager.
            returned: on success
            type: str
            sample: exadata_name_example
        exadata_display_name:
            description:
                - The user-friendly name for the Exadata system. The name does not have to be unique.
            returned: on success
            type: str
            sample: exadata_display_name_example
        exadata_type:
            description:
                - Operations Insights internal representation of the the Exadata system type.
            returned: on success
            type: str
            sample: DBMACHINE
        exadata_rack_type:
            description:
                - Exadata rack type.
            returned: on success
            type: str
            sample: FULL
        is_virtualized_exadata:
            description:
                - true if virtualization is used in the Exadata system
            returned: on success
            type: bool
            sample: true
        status:
            description:
                - Indicates the status of an Exadata insight in Operations Insights
            returned: on success
            type: str
            sample: DISABLED
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - The time the the Exadata insight was first enabled. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the Exadata insight was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Exadata insight.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        exadata_infra_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata Infrastructure.
            returned: on success
            type: str
            sample: "ocid1.exadatainfra.oc1..xxxxxxEXAMPLExxxxxx"
        exadata_infra_resource_type:
            description:
                - OCI exadata infrastructure resource type
            returned: on success
            type: str
            sample: cloudExadataInfrastructure
        exadata_shape:
            description:
                - The shape of the Exadata Infrastructure.
            returned: on success
            type: str
            sample: exadata_shape_example
    sample: {
        "enterprise_manager_identifier": "enterprise_manager_identifier_example",
        "enterprise_manager_entity_name": "enterprise_manager_entity_name_example",
        "enterprise_manager_entity_type": "enterprise_manager_entity_type_example",
        "enterprise_manager_entity_identifier": "enterprise_manager_entity_identifier_example",
        "enterprise_manager_entity_display_name": "enterprise_manager_entity_display_name_example",
        "enterprise_manager_bridge_id": "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx",
        "is_auto_sync_enabled": true,
        "entity_source": "EM_MANAGED_EXTERNAL_EXADATA",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "exadata_name": "exadata_name_example",
        "exadata_display_name": "exadata_display_name_example",
        "exadata_type": "DBMACHINE",
        "exadata_rack_type": "FULL",
        "is_virtualized_exadata": true,
        "status": "DISABLED",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "exadata_infra_id": "ocid1.exadatainfra.oc1..xxxxxxEXAMPLExxxxxx",
        "exadata_infra_resource_type": "cloudExadataInfrastructure",
        "exadata_shape": "exadata_shape_example"
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
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import ChangeExadataInsightCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExadataInsightsActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change
    """

    @staticmethod
    def get_module_resource_id_param():
        return "exadata_insight_id"

    def get_module_resource_id(self):
        return self.module.params.get("exadata_insight_id")

    def get_get_fn(self):
        return self.client.get_exadata_insight

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_exadata_insight,
            exadata_insight_id=self.module.params.get("exadata_insight_id"),
        )

    def change(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeExadataInsightCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_exadata_insight_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_insight_id=self.module.params.get("exadata_insight_id"),
                change_exadata_insight_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ExadataInsightsActionsHelperCustom = get_custom_class(
    "ExadataInsightsActionsHelperCustom"
)


class ResourceHelper(
    ExadataInsightsActionsHelperCustom, ExadataInsightsActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            exadata_insight_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="exadata_insights",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
