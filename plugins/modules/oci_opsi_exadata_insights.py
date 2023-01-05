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
module: oci_opsi_exadata_insights
short_description: Manage an ExadataInsights resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an ExadataInsights resource in Oracle Cloud Infrastructure
    - For I(state=present), create an Exadata insight resource for an Exadata system in Operations Insights. The Exadata system will be enabled in Operations
      Insights. Exadata-related metric collection and analysis will be started.
    - "This resource has the following action operations in the M(oracle.oci.oci_opsi_exadata_insights_actions) module: change."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment Identifier of Exadata insight
            - Required for create using I(state=present).
        type: str
    enterprise_manager_identifier:
        description:
            - Enterprise Manager Unique Identifier
            - Required for create using I(state=present).
        type: str
    enterprise_manager_bridge_id:
        description:
            - OPSI Enterprise Manager Bridge OCID
            - Required for create using I(state=present).
        type: str
    enterprise_manager_entity_identifier:
        description:
            - Enterprise Manager Entity Unique Identifier
            - Required for create using I(state=present).
        type: str
    member_entity_details:
        description:
            - ""
        type: list
        elements: dict
        suboptions:
            enterprise_manager_entity_identifier:
                description:
                    - Enterprise Manager Entity Unique Identifier
                type: str
                required: true
            compartment_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
                type: str
                required: true
    entity_source:
        description:
            - Source of the Exadata system.
            - Required for create using I(state=present), update using I(state=present) with exadata_insight_id present.
        type: str
        choices:
            - "EM_MANAGED_EXTERNAL_EXADATA"
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    is_auto_sync_enabled:
        description:
            - Set to true to enable automatic enablement and disablement of related targets from Enterprise Manager. New resources (e.g. Database Insights) will
              be placed in the same compartment as the related Exadata Insight.
            - This parameter is updatable.
        type: bool
    exadata_insight_id:
        description:
            - Unique Exadata insight identifier
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ExadataInsights.
            - Use I(state=present) to create or update an ExadataInsights.
            - Use I(state=absent) to delete an ExadataInsights.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create exadata_insights with entity_source = EM_MANAGED_EXTERNAL_EXADATA
  oci_opsi_exadata_insights:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    enterprise_manager_identifier: enterprise_manager_identifier_example
    enterprise_manager_bridge_id: "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx"
    enterprise_manager_entity_identifier: enterprise_manager_entity_identifier_example
    entity_source: EM_MANAGED_EXTERNAL_EXADATA

    # optional
    member_entity_details:
    - # required
      enterprise_manager_entity_identifier: enterprise_manager_entity_identifier_example
      compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_auto_sync_enabled: true

- name: Update exadata_insights with entity_source = EM_MANAGED_EXTERNAL_EXADATA
  oci_opsi_exadata_insights:
    # required
    entity_source: EM_MANAGED_EXTERNAL_EXADATA

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_auto_sync_enabled: true

- name: Delete exadata_insights
  oci_opsi_exadata_insights:
    # required
    exadata_insight_id: "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
exadata_insights:
    description:
        - Details of the ExadataInsights resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
    sample: {
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
        "enterprise_manager_identifier": "enterprise_manager_identifier_example",
        "enterprise_manager_entity_name": "enterprise_manager_entity_name_example",
        "enterprise_manager_entity_type": "enterprise_manager_entity_type_example",
        "enterprise_manager_entity_identifier": "enterprise_manager_entity_identifier_example",
        "enterprise_manager_entity_display_name": "enterprise_manager_entity_display_name_example",
        "enterprise_manager_bridge_id": "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx",
        "is_auto_sync_enabled": true
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import CreateExadataInsightDetails
    from oci.opsi.models import UpdateExadataInsightDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExadataInsightsHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ExadataInsightsHelperGen, self).get_possible_entity_types() + [
            "exadatainsights",
            "exadatainsight",
            "opsiexadatainsights",
            "opsiexadatainsight",
            "exadatainsightsresource",
            "exadatainsightresource",
            "opsi",
        ]

    def get_module_resource_id_param(self):
        return "exadata_insight_id"

    def get_module_resource_id(self):
        return self.module.params.get("exadata_insight_id")

    def get_get_fn(self):
        return self.client.get_exadata_insight

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_exadata_insight, exadata_insight_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_exadata_insight,
            exadata_insight_id=self.module.params.get("exadata_insight_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "enterprise_manager_bridge_id"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_exadata_insights, **kwargs
        )

    def get_create_model_class(self):
        return CreateExadataInsightDetails

    def get_exclude_attributes(self):
        return ["member_entity_details"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_exadata_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(create_exadata_insight_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateExadataInsightDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_exadata_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_insight_id=self.module.params.get("exadata_insight_id"),
                update_exadata_insight_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_exadata_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(
                exadata_insight_id=self.module.params.get("exadata_insight_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ExadataInsightsHelperCustom = get_custom_class("ExadataInsightsHelperCustom")


class ResourceHelper(ExadataInsightsHelperCustom, ExadataInsightsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            enterprise_manager_identifier=dict(type="str"),
            enterprise_manager_bridge_id=dict(type="str"),
            enterprise_manager_entity_identifier=dict(type="str"),
            member_entity_details=dict(
                type="list",
                elements="dict",
                options=dict(
                    enterprise_manager_entity_identifier=dict(
                        type="str", required=True
                    ),
                    compartment_id=dict(type="str", required=True),
                ),
            ),
            entity_source=dict(type="str", choices=["EM_MANAGED_EXTERNAL_EXADATA"]),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            is_auto_sync_enabled=dict(type="bool"),
            exadata_insight_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
