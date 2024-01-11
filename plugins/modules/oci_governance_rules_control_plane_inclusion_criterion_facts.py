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
module: oci_governance_rules_control_plane_inclusion_criterion_facts
short_description: Fetches details about one or multiple InclusionCriterion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple InclusionCriterion resources in Oracle Cloud Infrastructure
    - List inclusion criteria associated with a governance rule. Governance rule id must be supplied.
      An optional inclusion criterion id or a lifecycle state can also be supplied.
    - If I(inclusion_criterion_id) is specified, the details of a single InclusionCriterion will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    governance_rule_id:
        description:
            - Unique governance rule identifier.
            - Required to list multiple inclusion_criterions.
        type: str
    inclusion_criterion_id:
        description:
            - Unique inclusion criterion identifier.
            - Required to get a specific inclusion_criterion.
        type: str
        aliases: ["id"]
    lifecycle_state:
        description:
            - A filter to return only resources when their lifecycle state matches the given lifecycle state.
        type: str
        choices:
            - "ACTIVE"
            - "DELETED"
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific inclusion_criterion
  oci_governance_rules_control_plane_inclusion_criterion_facts:
    # required
    inclusion_criterion_id: "ocid1.inclusioncriterion.oc1..xxxxxxEXAMPLExxxxxx"

- name: List inclusion_criterions
  oci_governance_rules_control_plane_inclusion_criterion_facts:
    # required
    governance_rule_id: "ocid1.governancerule.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    inclusion_criterion_id: "ocid1.inclusioncriterion.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: ACTIVE
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
inclusion_criterions:
    description:
        - List of InclusionCriterion resources
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
    sample: [{
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
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.governance_rules_control_plane import GovernanceRuleClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InclusionCriterionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "inclusion_criterion_id",
        ]

    def get_required_params_for_list(self):
        return [
            "governance_rule_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_inclusion_criterion,
            inclusion_criterion_id=self.module.params.get("inclusion_criterion_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "inclusion_criterion_id",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_inclusion_criteria,
            governance_rule_id=self.module.params.get("governance_rule_id"),
            **optional_kwargs
        )


InclusionCriterionFactsHelperCustom = get_custom_class(
    "InclusionCriterionFactsHelperCustom"
)


class ResourceFactsHelper(
    InclusionCriterionFactsHelperCustom, InclusionCriterionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            governance_rule_id=dict(type="str"),
            inclusion_criterion_id=dict(aliases=["id"], type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="inclusion_criterion",
        service_client_class=GovernanceRuleClient,
        namespace="governance_rules_control_plane",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(inclusion_criterions=result)


if __name__ == "__main__":
    main()
