#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_governance_rules_control_plane_inclusion_criterion
short_description: Manage an InclusionCriterion resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete an InclusionCriterion resource in Oracle Cloud Infrastructure
    - For I(state=present), create inclusion criterion of type tenancy or tag for the governance rule.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    governance_rule_id:
        description:
            - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the governance rule. Every inclusion criterion
              is associated with a governance rule.
            - Required for create using I(state=present).
        type: str
    type:
        description:
            - "Type of inclusion criterion - TENANCY, ALL or TAG. We support TENANCY and ALL for now."
            - Required for create using I(state=present).
        type: str
    association:
        description:
            - ""
        type: dict
        suboptions:
            type:
                description:
                    - Type of Association, can be one of TENANCY, ALL or TAG. We support only TENANCY for now.
                    - "Example: `TENANCY`"
                type: str
                choices:
                    - "TENANCY"
                required: true
            tenancy_id:
                description:
                    - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the tenancy to which the governance rule
                      will be applied as part of this tenancy inclusion criterion.
                type: str
                required: true
    inclusion_criterion_id:
        description:
            - Unique inclusion criterion identifier.
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the InclusionCriterion.
            - Use I(state=present) to create an InclusionCriterion.
            - Use I(state=absent) to delete an InclusionCriterion.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create inclusion_criterion
  oci_governance_rules_control_plane_inclusion_criterion:
    # required
    governance_rule_id: "ocid1.governancerule.oc1..xxxxxxEXAMPLExxxxxx"
    type: type_example

    # optional
    association:
      # required
      type: TENANCY
      tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete inclusion_criterion
  oci_governance_rules_control_plane_inclusion_criterion:
    # required
    inclusion_criterion_id: "ocid1.inclusioncriterion.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
inclusion_criterion:
    description:
        - Details of the InclusionCriterion resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the inclusion criterion.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        governance_rule_id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the governance rule. Every inclusion
                  criterion is associated with a governance rule.
            returned: on success
            type: str
            sample: "ocid1.governancerule.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - "Type of inclusion criterion - TENANCY, ALL or TAG. We support TENANCY and ALL for now."
            returned: on success
            type: str
            sample: TENANCY
        association:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Type of Association, can be one of TENANCY, ALL or TAG. We support only TENANCY for now.
                        - "Example: `TENANCY`"
                    returned: on success
                    type: str
                    sample: TENANCY
                tenancy_id:
                    description:
                        - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the tenancy to which the governance
                          rule will be applied as part of this tenancy inclusion criterion.
                    returned: on success
                    type: str
                    sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the inclusion criterion.
            returned: on success
            type: str
            sample: ACTIVE
        time_created:
            description:
                - Date and time the inclusion criterion was created. An RFC3339 formatted datetime string.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Date and time the inclusion criterion was updated. An RFC3339 formatted datetime string.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "governance_rule_id": "ocid1.governancerule.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "TENANCY",
        "association": {
            "type": "TENANCY",
            "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.governance_rules_control_plane import WorkRequestClient
    from oci.governance_rules_control_plane import GovernanceRuleClient
    from oci.governance_rules_control_plane.models import (
        CreateInclusionCriterionDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InclusionCriterionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_possible_entity_types(self):
        return super(InclusionCriterionHelperGen, self).get_possible_entity_types() + [
            "organizationsinclusioncriterion",
            "organizationsinclusioncriterions",
            "governanceRulesControlPlaneorganizationsinclusioncriterion",
            "governanceRulesControlPlaneorganizationsinclusioncriterions",
            "organizationsinclusioncriterionresource",
            "organizationsinclusioncriterionsresource",
            "inclusioncriterion",
            "inclusioncriterions",
            "governanceRulesControlPlaneinclusioncriterion",
            "governanceRulesControlPlaneinclusioncriterions",
            "inclusioncriterionresource",
            "inclusioncriterionsresource",
            "inclusioncriteria",
            "inclusioncriterias",
            "governanceRulesControlPlaneinclusioncriteria",
            "governanceRulesControlPlaneinclusioncriterias",
            "inclusioncriteriaresource",
            "inclusioncriteriasresource",
            "governancerulescontrolplane",
        ]

    def get_module_resource_id_param(self):
        return "inclusion_criterion_id"

    def get_module_resource_id(self):
        return self.module.params.get("inclusion_criterion_id")

    def get_get_fn(self):
        return self.client.get_inclusion_criterion

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_inclusion_criterion,
            inclusion_criterion_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_inclusion_criterion,
            inclusion_criterion_id=self.module.params.get("inclusion_criterion_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "governance_rule_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["inclusion_criterion_id"]

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
            self.client.list_inclusion_criteria, **kwargs
        )

    def get_create_model_class(self):
        return CreateInclusionCriterionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_inclusion_criterion,
            call_fn_args=(),
            call_fn_kwargs=dict(create_inclusion_criterion_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_inclusion_criterion,
            call_fn_args=(),
            call_fn_kwargs=dict(
                inclusion_criterion_id=self.module.params.get("inclusion_criterion_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


InclusionCriterionHelperCustom = get_custom_class("InclusionCriterionHelperCustom")


class ResourceHelper(InclusionCriterionHelperCustom, InclusionCriterionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            governance_rule_id=dict(type="str"),
            type=dict(type="str"),
            association=dict(
                type="dict",
                options=dict(
                    type=dict(type="str", required=True, choices=["TENANCY"]),
                    tenancy_id=dict(type="str", required=True),
                ),
            ),
            inclusion_criterion_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="inclusion_criterion",
        service_client_class=GovernanceRuleClient,
        namespace="governance_rules_control_plane",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
