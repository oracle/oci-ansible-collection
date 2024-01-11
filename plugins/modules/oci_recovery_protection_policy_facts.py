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
module: oci_recovery_protection_policy_facts
short_description: Fetches details about one or multiple ProtectionPolicy resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ProtectionPolicy resources in Oracle Cloud Infrastructure
    - Gets a list of protection policies based on the specified parameters.
    - If I(protection_policy_id) is specified, the details of a single ProtectionPolicy will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment OCID.
            - Required to list multiple protection_policies.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire 'displayname' given.
        type: str
        aliases: ["name"]
    protection_policy_id:
        description:
            - The protection policy OCID.
            - Required to get a specific protection_policy.
        type: str
        aliases: ["id"]
    owner:
        description:
            - A filter to return only the policies that match the owner as 'Customer' or 'Oracle'.
        type: str
        choices:
            - "oracle"
            - "customer"
    sort_order:
        description:
            - "The sort order to use, either ascending (ASC) or descending (DESC).
              Allowed values are:
                - ASC
                - DESC"
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - "The field to sort by. You can provide one sort order (sortOrder). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is
              ascending. If you do not specify a value, then TIMECREATED is used as the default sort order.
              Allowed values are:
                - TIMECREATED
                - DISPLAYNAME"
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific protection_policy
  oci_recovery_protection_policy_facts:
    # required
    protection_policy_id: "ocid1.protectionpolicy.oc1..xxxxxxEXAMPLExxxxxx"

- name: List protection_policies
  oci_recovery_protection_policy_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    display_name: display_name_example
    protection_policy_id: "ocid1.protectionpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    owner: oracle
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
protection_policies:
    description:
        - List of ProtectionPolicy resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The protection policy OCID.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user provided name for the protection policy.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment that contains the protection policy.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        backup_retention_period_in_days:
            description:
                - The maximum number of days to retain backups for a protected database. Specify a period ranging from a minimum 14 days to a maximum 95 days.
                  For example, specify the value 55 if you want to retain backups for 55 days.
            returned: on success
            type: int
            sample: 56
        is_predefined_policy:
            description:
                - Set to TRUE if the policy is Oracle-defined, and FALSE for a user-defined custom policy. You can modify only the custom policies.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - "An RFC3339 formatted datetime string that indicates the created time for the protection policy. For example: '2020-05-22T21:10:29.600Z'."
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "An RFC3339 formatted datetime string that indicates the updated time for the protection policy. For example: '2020-05-22T21:10:29.600Z'."
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - "The current state of the protection policy. Allowed values are:
                    - CREATING
                    - UPDATING
                    - ACTIVE
                    - DELETING
                    - DELETED
                    - FAILED"
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Detailed description about the current lifecycle state of the protection policy. For example, it can be used to provide actionable information
                  for a resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
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
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`. For more information, see L(Resource Tags,https://docs.oracle.com/en-
                  us/iaas/Content/General/Concepts/resourcetags.htm)"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`. For more information, see L(Resource Tags,https://docs.oracle.com/en-
                  us/iaas/Content/General/Concepts/resourcetags.htm)"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "backup_retention_period_in_days": 56,
        "is_predefined_policy": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.recovery import DatabaseRecoveryClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProtectionPolicyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "protection_policy_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_protection_policy,
            protection_policy_id=self.module.params.get("protection_policy_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "protection_policy_id",
            "owner",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_protection_policies,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ProtectionPolicyFactsHelperCustom = get_custom_class(
    "ProtectionPolicyFactsHelperCustom"
)


class ResourceFactsHelper(
    ProtectionPolicyFactsHelperCustom, ProtectionPolicyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
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
            display_name=dict(aliases=["name"], type="str"),
            protection_policy_id=dict(aliases=["id"], type="str"),
            owner=dict(type="str", choices=["oracle", "customer"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="protection_policy",
        service_client_class=DatabaseRecoveryClient,
        namespace="recovery",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(protection_policies=result)


if __name__ == "__main__":
    main()
