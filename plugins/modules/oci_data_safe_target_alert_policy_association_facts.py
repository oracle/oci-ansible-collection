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
module: oci_data_safe_target_alert_policy_association_facts
short_description: Fetches details about one or multiple TargetAlertPolicyAssociation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TargetAlertPolicyAssociation resources in Oracle Cloud Infrastructure
    - Gets a list of all target-alert policy associations.
    - If I(target_alert_policy_association_id) is specified, the details of a single TargetAlertPolicyAssociation will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - A filter to return only resources that match the specified compartment OCID.
            - Required to list multiple target_alert_policy_associations.
        type: str
    target_alert_policy_association_id:
        description:
            - The OCID of the target-alert policy association.
            - Required to get a specific target_alert_policy_association.
        type: str
        aliases: ["id"]
    alert_policy_id:
        description:
            - A filter to return policy by it's OCID.
        type: str
    target_id:
        description:
            - A filter to return only items related to a specific target OCID.
        type: str
    lifecycle_state:
        description:
            - An optional filter to return only alert policies that have the given life-cycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either ascending (ASC) or descending (DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided.
        type: str
        choices:
            - "DISPLAYNAME"
            - "TIMECREATED"
            - "TIMEUPDATED"
    time_created_greater_than_or_equal_to:
        description:
            - A filter to return only the resources that were created after the specified date and time, as defined by
              L(RFC3339,https://tools.ietf.org/html/rfc3339).
              Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date.
            - "**Example:** 2016-12-19T16:39:57.600Z"
        type: str
    time_created_less_than:
        description:
            - "Search for resources that were created before a specific date.
              Specifying this parameter corresponding `timeCreatedLessThan`
              parameter will retrieve all resources created before the
              specified created date, in \\"YYYY-MM-ddThh:mmZ\\" format with a Z offset, as
              defined by RFC 3339."
            - "**Example:** 2016-12-19T16:39:57.600Z"
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
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific target_alert_policy_association
  oci_data_safe_target_alert_policy_association_facts:
    # required
    target_alert_policy_association_id: "ocid1.targetalertpolicyassociation.oc1..xxxxxxEXAMPLExxxxxx"

- name: List target_alert_policy_associations
  oci_data_safe_target_alert_policy_association_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    target_alert_policy_association_id: "ocid1.targetalertpolicyassociation.oc1..xxxxxxEXAMPLExxxxxx"
    alert_policy_id: "ocid1.alertpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: DISPLAYNAME
    time_created_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_created_less_than: 2013-10-20T19:20:30+01:00
    compartment_id_in_subtree: true
    access_level: RESTRICTED

"""

RETURN = """
target_alert_policy_associations:
    description:
        - List of TargetAlertPolicyAssociation resources
    returned: on success
    type: complex
    contains:
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
                - The OCID of the target-alert policy association.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the target-alert policy association.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Describes the target-alert policy association.
            returned: on success
            type: str
            sample: description_example
        policy_id:
            description:
                - The OCID of the alert policy.
            returned: on success
            type: str
            sample: "ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx"
        target_id:
            description:
                - The OCID of the target on which alert policy is to be applied.
            returned: on success
            type: str
            sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
        is_enabled:
            description:
                - Indicates if the target-alert policy association is enabled or disabled.
            returned: on success
            type: bool
            sample: true
        compartment_id:
            description:
                - The OCID of the compartment that contains the policy.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Creation date and time of the alert policy, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Last date and time the alert policy was updated, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the target-alert policy association.
            returned: on success
            type: str
            sample: CREATING
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
        "system_tags": {},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "policy_id": "ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx",
        "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
        "is_enabled": true,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
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


class DataSafeTargetAlertPolicyAssociationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "target_alert_policy_association_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_alert_policy_association,
            target_alert_policy_association_id=self.module.params.get(
                "target_alert_policy_association_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "target_alert_policy_association_id",
            "alert_policy_id",
            "target_id",
            "lifecycle_state",
            "sort_order",
            "sort_by",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
            "compartment_id_in_subtree",
            "access_level",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_target_alert_policy_associations,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataSafeTargetAlertPolicyAssociationFactsHelperCustom = get_custom_class(
    "DataSafeTargetAlertPolicyAssociationFactsHelperCustom"
)


class ResourceFactsHelper(
    DataSafeTargetAlertPolicyAssociationFactsHelperCustom,
    DataSafeTargetAlertPolicyAssociationFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            target_alert_policy_association_id=dict(aliases=["id"], type="str"),
            alert_policy_id=dict(type="str"),
            target_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str", choices=["DISPLAYNAME", "TIMECREATED", "TIMEUPDATED"]
            ),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
            compartment_id_in_subtree=dict(type="bool"),
            access_level=dict(type="str", choices=["RESTRICTED", "ACCESSIBLE"]),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="target_alert_policy_association",
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

    module.exit_json(target_alert_policy_associations=result)


if __name__ == "__main__":
    main()
