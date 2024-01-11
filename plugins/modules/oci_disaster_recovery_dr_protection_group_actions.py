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
module: oci_disaster_recovery_dr_protection_group_actions
short_description: Perform actions on a DrProtectionGroup resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DrProtectionGroup resource in Oracle Cloud Infrastructure
    - "For I(action=associate), create an association between the DR Protection Group identified by *drProtectionGroupId* and
      another DR Protection Group in a different region."
    - "For I(action=change_compartment), move the DR Protection Group identified by *drProtectionGroupId* to a different compartment."
    - "For I(action=disassociate), delete the association between the DR Protection Group identified by *drProtectionGroupId*.
      and its peer DR Protection Group."
    - "For I(action=update_dr_protection_group_role), update the role of the DR Protection Group identified by *drProtectionGroupId*."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    peer_id:
        description:
            - The OCID of the peer (remote) DR Protection Group.
            - "Example: `ocid1.drprotectiongroup.oc1.iad.&lt;unique_id&gt;`"
            - Applicable only for I(action=associate).
        type: str
    peer_region:
        description:
            - The region of the peer (remote) DR Protection Group.
            - "Example: `us-ashburn-1`"
            - Applicable only for I(action=associate).
        type: str
    compartment_id:
        description:
            - The OCID of the compartment to which the DR Protection Group should be moved.
            - "Example: `ocid1.compartment.oc1..&lt;unique_id&gt;`"
            - Required for I(action=change_compartment).
        type: str
    type:
        description:
            - The default type (required for forward compatibility).
            - Required for I(action=disassociate).
        type: str
        choices:
            - "DEFAULT"
    role:
        description:
            - The role of this DR Protection Group.
            - Required for I(action=associate), I(action=update_dr_protection_group_role).
        type: str
        choices:
            - "PRIMARY"
            - "STANDBY"
            - "UNCONFIGURED"
    dr_protection_group_id:
        description:
            - The OCID of the DR Protection Group.
            - "Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`"
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the DrProtectionGroup.
        type: str
        required: true
        choices:
            - "associate"
            - "change_compartment"
            - "disassociate"
            - "update_dr_protection_group_role"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action associate on dr_protection_group
  oci_disaster_recovery_dr_protection_group_actions:
    # required
    role: PRIMARY
    dr_protection_group_id: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: associate

    # optional
    peer_id: "ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx"
    peer_region: us-phoenix-1

- name: Perform action change_compartment on dr_protection_group
  oci_disaster_recovery_dr_protection_group_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    dr_protection_group_id: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action disassociate on dr_protection_group with type = DEFAULT
  oci_disaster_recovery_dr_protection_group_actions:
    # required
    type: DEFAULT

- name: Perform action update_dr_protection_group_role on dr_protection_group
  oci_disaster_recovery_dr_protection_group_actions:
    # required
    role: PRIMARY
    dr_protection_group_id: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: update_dr_protection_group_role

"""

RETURN = """
dr_protection_group:
    description:
        - Details of the DrProtectionGroup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the DR Protection Group.
                - "Example: `ocid1.drprotectiongroup.oc1.phx.&lt;unique_id&gt;`"
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the DR Protection Group.
                - "Example: `ocid1.compartment.oc1..&lt;unique_id&gt;`"
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
                - "Example: `ocid1.drprotectiongroup.oc1.iad.&lt;unique_id&gt;`"
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
        log_location:
            description:
                - ""
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
                is_retain_fault_domain:
                    description:
                        - A flag indicating if this compute instance should be moved to the same fault domain.
                          Compute instance launch will fail if this flag is set to true and capacity is not available in that specific fault domain in the
                          destination region.
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: true
                destination_capacity_reservation_id:
                    description:
                        - The OCID of the capacity reservation in the destination region using which this compute instance
                          should be launched.
                        - "Example: `ocid1.capacityreservation.oc1..&lt;unique_id&gt;`"
                    returned: on success
                    type: str
                    sample: "ocid1.destinationcapacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
                vnic_mappings:
                    description:
                        - A list of compute instance VNIC mappings.
                    returned: on success
                    type: complex
                    contains:
                        source_vnic_id:
                            description:
                                - The OCID of the VNIC.
                                - "Example: `ocid1.vnic.oc1..&lt;unique_id&gt;`"
                            returned: on success
                            type: str
                            sample: "ocid1.sourcevnic.oc1..xxxxxxEXAMPLExxxxxx"
                        destination_subnet_id:
                            description:
                                - The OCID of the destination (remote) subnet to which this VNIC should connect.
                                - "Example: `ocid1.subnet.oc1..&lt;unique_id&gt;`"
                            returned: on success
                            type: str
                            sample: "ocid1.destinationsubnet.oc1..xxxxxxEXAMPLExxxxxx"
                        destination_primary_private_ip_address:
                            description:
                                - The primary private IP address to assign. This address must belong to the destination subnet.
                                - "Example: `10.0.3.3`"
                            returned: on success
                            type: str
                            sample: destination_primary_private_ip_address_example
                        destination_primary_private_ip_hostname_label:
                            description:
                                - The hostname to assign for this primary private IP.
                                  The value is the hostname portion of the private IP's fully qualified domain name (FQDN)
                                  (for example, bminstance1 in FQDN bminstance1.subnet123.vcn1.oraclevcn.com).
                                - "Example: `bminstance1`"
                            returned: on success
                            type: str
                            sample: destination_primary_private_ip_hostname_label_example
                        destination_nsg_id_list:
                            description:
                                - A list of destination region's network security group (NSG) OCIDs which this VNIC should use.
                                - "Example: `[ ocid1.networksecuritygroup.oc1..&lt;unique_id&gt;, ocid1.networksecuritygroup.oc1..&lt;unique_id&gt; ]`"
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
                        - "Example: `ocid1.instance.oc1.phx.&lt;unique_id&gt;`"
                    returned: on success
                    type: str
                    sample: "ocid1.member.oc1..xxxxxxEXAMPLExxxxxx"
                member_type:
                    description:
                        - The type of the member.
                    returned: on success
                    type: str
                    sample: COMPUTE_INSTANCE
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "role": "PRIMARY",
        "peer_id": "ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_region": "us-phoenix-1",
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
            "is_retain_fault_domain": true,
            "destination_capacity_reservation_id": "ocid1.destinationcapacityreservation.oc1..xxxxxxEXAMPLExxxxxx",
            "vnic_mappings": [{
                "source_vnic_id": "ocid1.sourcevnic.oc1..xxxxxxEXAMPLExxxxxx",
                "destination_subnet_id": "ocid1.destinationsubnet.oc1..xxxxxxEXAMPLExxxxxx",
                "destination_primary_private_ip_address": "destination_primary_private_ip_address_example",
                "destination_primary_private_ip_hostname_label": "destination_primary_private_ip_hostname_label_example",
                "destination_nsg_id_list": []
            }],
            "destination_compartment_id": "ocid1.destinationcompartment.oc1..xxxxxxEXAMPLExxxxxx",
            "destination_dedicated_vm_host_id": "ocid1.destinationdedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx",
            "password_vault_secret_id": "ocid1.passwordvaultsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "member_id": "ocid1.member.oc1..xxxxxxEXAMPLExxxxxx",
            "member_type": "COMPUTE_INSTANCE"
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "life_cycle_details": "life_cycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.disaster_recovery import DisasterRecoveryClient
    from oci.disaster_recovery.models import AssociateDrProtectionGroupDetails
    from oci.disaster_recovery.models import ChangeDrProtectionGroupCompartmentDetails
    from oci.disaster_recovery.models import DisassociateDrProtectionGroupDetails
    from oci.disaster_recovery.models import UpdateDrProtectionGroupRoleDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrProtectionGroupActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        associate
        change_compartment
        disassociate
        update_dr_protection_group_role
    """

    @staticmethod
    def get_module_resource_id_param():
        return "dr_protection_group_id"

    def get_module_resource_id(self):
        return self.module.params.get("dr_protection_group_id")

    def get_get_fn(self):
        return self.client.get_dr_protection_group

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dr_protection_group,
            dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
        )

    def associate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AssociateDrProtectionGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.associate_dr_protection_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                associate_dr_protection_group_details=action_details,
                dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDrProtectionGroupCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_dr_protection_group_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_dr_protection_group_compartment_details=action_details,
                dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
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

    def disassociate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DisassociateDrProtectionGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disassociate_dr_protection_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                disassociate_dr_protection_group_details=action_details,
                dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
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

    def update_dr_protection_group_role(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpdateDrProtectionGroupRoleDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_dr_protection_group_role,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_dr_protection_group_role_details=action_details,
                dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
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


DrProtectionGroupActionsHelperCustom = get_custom_class(
    "DrProtectionGroupActionsHelperCustom"
)


class ResourceHelper(
    DrProtectionGroupActionsHelperCustom, DrProtectionGroupActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            peer_id=dict(type="str"),
            peer_region=dict(type="str"),
            compartment_id=dict(type="str"),
            type=dict(type="str", choices=["DEFAULT"]),
            role=dict(type="str", choices=["PRIMARY", "STANDBY", "UNCONFIGURED"]),
            dr_protection_group_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "associate",
                    "change_compartment",
                    "disassociate",
                    "update_dr_protection_group_role",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="dr_protection_group",
        service_client_class=DisasterRecoveryClient,
        namespace="disaster_recovery",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
