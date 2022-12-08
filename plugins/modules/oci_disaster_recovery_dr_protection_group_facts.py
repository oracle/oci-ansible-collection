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
module: oci_disaster_recovery_dr_protection_group_facts
short_description: Fetches details about one or multiple DrProtectionGroup resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DrProtectionGroup resources in Oracle Cloud Infrastructure
    - Gets a summary list of all DR Protection Groups in a compartment.
    - If I(dr_protection_group_id) is specified, the details of a single DrProtectionGroup will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID (OCID) of the compartment in which to list resources.
            - "Example: `ocid1.compartment.oc1..exampleocid1`"
            - Required to list multiple dr_protection_groups.
        type: str
    lifecycle_state:
        description:
            - A filter to return only DR Protection Groups that match the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
            - "NEEDS_ATTENTION"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    dr_protection_group_id:
        description:
            - The OCID of the DR Protection Group.
            - "Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`"
            - Required to get a specific dr_protection_group.
        type: str
        aliases: ["id"]
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
            - "Example: `MY UNIQUE DISPLAY NAME`"
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.
              Default order for displayName is ascending. If no value is specified timeCreated is default.
            - "Example: `displayName`"
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific dr_protection_group
  oci_disaster_recovery_dr_protection_group_facts:
    # required
    dr_protection_group_id: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"

- name: List dr_protection_groups
  oci_disaster_recovery_dr_protection_group_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    dr_protection_group_id: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
dr_protection_groups:
    description:
        - List of DrProtectionGroup resources
    returned: on success
    type: complex
    contains:
        log_location:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                namespace:
                    description:
                        - "The namespace in Object Storage (Note - this is usually the tenancy name)."
                        - "Example: `myocitenancy`"
                    returned: on success
                    type: str
                    sample: namespace_example
                bucket:
                    description:
                        - The bucket name inside the Object Storage namespace.
                        - "Example: `operation_logs`"
                    returned: on success
                    type: str
                    sample: bucket_example
                object:
                    description:
                        - The object name inside the Object Storage bucket.
                        - "Example: `switchover_plan_executions`"
                    returned: on success
                    type: str
                    sample: object_example
        members:
            description:
                - A list of DR Protection Group members.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                is_movable:
                    description:
                        - A flag indicating if this compute instance should be moved during DR operations.
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: true
                vnic_mapping:
                    description:
                        - A list of compute instance VNIC mappings.
                    returned: on success
                    type: complex
                    contains:
                        source_vnic_id:
                            description:
                                - The OCID of the VNIC.
                                - "Example: `ocid1.vnic.oc1.phx.exampleocid`"
                            returned: on success
                            type: str
                            sample: "ocid1.sourcevnic.oc1..xxxxxxEXAMPLExxxxxx"
                        destination_subnet_id:
                            description:
                                - The OCID of the destination (remote) subnet to which this VNIC should connect.
                                - "Example: `ocid1.subnet.oc1.iad.exampleocid`"
                            returned: on success
                            type: str
                            sample: "ocid1.destinationsubnet.oc1..xxxxxxEXAMPLExxxxxx"
                        destination_nsg_id_list:
                            description:
                                - A list of destination region's network security group (NSG) OCIDs which this VNIC should use.
                                - "Example: `[ ocid1.networksecuritygroup.oc1.iad.exampleocid1, ocid1.networksecuritygroup.oc1.iad.exampleocid2 ]`"
                            returned: on success
                            type: list
                            sample: []
                destination_compartment_id:
                    description:
                        - The OCID of the compartment for this compute instance in the destination region.
                        - "Example: `ocid1.compartment.oc1..exampleocid`"
                    returned: on success
                    type: str
                    sample: "ocid1.destinationcompartment.oc1..xxxxxxEXAMPLExxxxxx"
                destination_dedicated_vm_host_id:
                    description:
                        - The OCID of the dedicated VM Host for this compute instance in the destination region.
                        - "Example: `ocid1.dedicatedvmhost.oc1.iad.exampleocid`"
                    returned: on success
                    type: str
                    sample: "ocid1.destinationdedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
                password_vault_secret_id:
                    description:
                        - The ID of the vault secret where the database password is stored.
                        - "Example: `ocid1.vaultsecret.oc1.phx.exampleocid1`"
                    returned: on success
                    type: str
                    sample: "ocid1.passwordvaultsecret.oc1..xxxxxxEXAMPLExxxxxx"
                member_id:
                    description:
                        - The OCID of the member.
                        - "Example: `ocid1.instance.oc1.phx.exampleocid1`"
                    returned: on success
                    type: str
                    sample: "ocid1.member.oc1..xxxxxxEXAMPLExxxxxx"
                member_type:
                    description:
                        - The type of the member.
                    returned: on success
                    type: str
                    sample: COMPUTE_INSTANCE
        id:
            description:
                - The OCID of the DR Protection Group.
                - "Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid1`"
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the DR Protection Group.
                - "Example: `ocid1.compartment.oc1..exampleocid1`"
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the DR Protection Group.
                - "Example: `EBS PHX DRPG`"
            returned: on success
            type: str
            sample: display_name_example
        role:
            description:
                - The role of the DR Protection Group.
            returned: on success
            type: str
            sample: PRIMARY
        peer_id:
            description:
                - The OCID of the peer (remote) DR Protection Group.
                - "Example: `ocid1.drprotectiongroup.oc1.iad.exampleocid2`"
            returned: on success
            type: str
            sample: "ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx"
        peer_region:
            description:
                - The region of the peer (remote) DR Protection Group.
                - "Example: `us-ashburn-1`"
            returned: on success
            type: str
            sample: us-phoenix-1
        time_created:
            description:
                - The date and time the DR Protection Group was created. An RFC3339 formatted datetime string.
                - "Example: `2019-03-29T09:36:42Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the DR Protection Group was updated. An RFC3339 formatted datetime string.
                - "Example: `2019-03-29T09:36:42Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the DR Protection Group.
            returned: on success
            type: str
            sample: CREATING
        life_cycle_details:
            description:
                - A message describing the DR Protection Group's current state in more detail.
            returned: on success
            type: str
            sample: life_cycle_details_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "log_location": {
            "namespace": "namespace_example",
            "bucket": "bucket_example",
            "object": "object_example"
        },
        "members": [{
            "is_movable": true,
            "vnic_mapping": [{
                "source_vnic_id": "ocid1.sourcevnic.oc1..xxxxxxEXAMPLExxxxxx",
                "destination_subnet_id": "ocid1.destinationsubnet.oc1..xxxxxxEXAMPLExxxxxx",
                "destination_nsg_id_list": []
            }],
            "destination_compartment_id": "ocid1.destinationcompartment.oc1..xxxxxxEXAMPLExxxxxx",
            "destination_dedicated_vm_host_id": "ocid1.destinationdedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx",
            "password_vault_secret_id": "ocid1.passwordvaultsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "member_id": "ocid1.member.oc1..xxxxxxEXAMPLExxxxxx",
            "member_type": "COMPUTE_INSTANCE"
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "role": "PRIMARY",
        "peer_id": "ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_region": "us-phoenix-1",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "life_cycle_details": "life_cycle_details_example",
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
    from oci.disaster_recovery import DisasterRecoveryClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrProtectionGroupFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "dr_protection_group_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dr_protection_group,
            dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "dr_protection_group_id",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_dr_protection_groups,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DrProtectionGroupFactsHelperCustom = get_custom_class(
    "DrProtectionGroupFactsHelperCustom"
)


class ResourceFactsHelper(
    DrProtectionGroupFactsHelperCustom, DrProtectionGroupFactsHelperGen
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
                    "ACTIVE",
                    "UPDATING",
                    "NEEDS_ATTENTION",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            dr_protection_group_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="dr_protection_group",
        service_client_class=DisasterRecoveryClient,
        namespace="disaster_recovery",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(dr_protection_groups=result)


if __name__ == "__main__":
    main()
