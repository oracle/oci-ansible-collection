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
module: oci_disaster_recovery_dr_protection_group
short_description: Manage a DrProtectionGroup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DrProtectionGroup resource in Oracle Cloud Infrastructure
    - For I(state=present), create a new DR Protection Group.
    - "This resource has the following action operations in the M(oracle.oci.oci_disaster_recovery_dr_protection_group_actions) module: associate,
      change_compartment, disassociate, update_dr_protection_group_role."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment in which to create the DR Protection Group.
            - "Example: `ocid1.compartment.oc1..exampleocid1`"
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    association:
        description:
            - ""
        type: dict
        suboptions:
            peer_id:
                description:
                    - The OCID of the peer (remote) DR Protection Group.
                    - "Example: `ocid1.drprotectiongroup.oc1.iad.exampleocid2`"
                type: str
            peer_region:
                description:
                    - The region of the peer (remote) DR Protection Group.
                    - "Example: `us-ashburn-1`"
                type: str
            role:
                description:
                    - The role of this DR Protection Group.
                type: str
                choices:
                    - "PRIMARY"
                    - "STANDBY"
                    - "UNCONFIGURED"
                required: true
    display_name:
        description:
            - The display name of the DR Protection Group.
            - "Example: `EBS PHX DRPG`"
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    log_location:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            namespace:
                description:
                    - "The namespace in Object Storage (Note - this is usually the tenancy name)."
                    - "Example: `myocitenancy`"
                    - This parameter is updatable.
                type: str
                required: true
            bucket:
                description:
                    - The bucket name inside the Object Storage namespace.
                    - "Example: `operation_logs`"
                    - This parameter is updatable.
                type: str
                required: true
    members:
        description:
            - A list of DR Protection Group members.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            is_movable:
                description:
                    - A flag indicating if this compute instance should be moved during DR operations.
                    - "Example: `false`"
                    - This parameter is updatable.
                    - Applicable when member_type is 'COMPUTE_INSTANCE'
                type: bool
            vnic_mapping:
                description:
                    - A list of Compute Instance VNIC mappings.
                    - Applicable when member_type is 'COMPUTE_INSTANCE'
                type: list
                elements: dict
                suboptions:
                    source_vnic_id:
                        description:
                            - The OCID of the VNIC.
                            - "Example: `ocid1.vnic.oc1.phx.exampleocid1`"
                            - Required when member_type is 'COMPUTE_INSTANCE'
                        type: str
                        required: true
                    destination_subnet_id:
                        description:
                            - The OCID of the destination (remote) subnet to which this VNIC should connect.
                            - "Example: `ocid1.subnet.oc1.iad.exampleocid2`"
                            - Required when member_type is 'COMPUTE_INSTANCE'
                        type: str
                        required: true
                    destination_nsg_id_list:
                        description:
                            - A list of destination region's network security group (NSG) Ids which this VNIC should use.
                            - "Example: `[ ocid1.networksecuritygroup.oc1.iad.abcd1, ocid1.networksecuritygroup.oc1.iad.wxyz2 ]`"
                            - Applicable when member_type is 'COMPUTE_INSTANCE'
                        type: list
                        elements: str
            destination_compartment_id:
                description:
                    - The OCID of the compartment for this compute instance in the destination region.
                    - "Example: `ocid1.compartment.oc1..exampleocid1`"
                    - This parameter is updatable.
                    - Applicable when member_type is 'COMPUTE_INSTANCE'
                type: str
            destination_dedicated_vm_host_id:
                description:
                    - The OCID of the dedicated VM Host in the destination region where this compute instance
                      should be launched
                    - "Example: `ocid1.dedicatedvmhost.oc1.iad.exampleocid2`"
                    - This parameter is updatable.
                    - Applicable when member_type is 'COMPUTE_INSTANCE'
                type: str
            member_id:
                description:
                    - The OCID of the member.
                    - "Example: `ocid1.instance.oc1.phx.exampleocid1`"
                    - This parameter is updatable.
                type: str
                required: true
            member_type:
                description:
                    - The type of the member.
                    - This parameter is updatable.
                type: str
                choices:
                    - "COMPUTE_INSTANCE"
                    - "DATABASE"
                    - "AUTONOMOUS_DATABASE"
                    - "VOLUME_GROUP"
                required: true
            password_vault_secret_id:
                description:
                    - The OCID of the vault secret where the database password is stored.
                    - "Example: `ocid1.vaultsecret.oc1.phx.exampleocid1`"
                    - This parameter is updatable.
                    - Applicable when member_type is 'DATABASE'
                type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    dr_protection_group_id:
        description:
            - The OCID of the DR Protection Group.
            - "Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`"
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DrProtectionGroup.
            - Use I(state=present) to create or update a DrProtectionGroup.
            - Use I(state=absent) to delete a DrProtectionGroup.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create dr_protection_group
  oci_disaster_recovery_dr_protection_group:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    log_location:
      # required
      namespace: namespace_example
      bucket: bucket_example

    # optional
    association:
      # required
      role: PRIMARY

      # optional
      peer_id: "ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx"
      peer_region: us-phoenix-1
    members:
    - # required
      member_id: "ocid1.member.oc1..xxxxxxEXAMPLExxxxxx"
      member_type: COMPUTE_INSTANCE

      # optional
      is_movable: true
      vnic_mapping:
      - # required
        source_vnic_id: "ocid1.sourcevnic.oc1..xxxxxxEXAMPLExxxxxx"
        destination_subnet_id: "ocid1.destinationsubnet.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        destination_nsg_id_list: [ "destination_nsg_id_list_example" ]
      destination_compartment_id: "ocid1.destinationcompartment.oc1..xxxxxxEXAMPLExxxxxx"
      destination_dedicated_vm_host_id: "ocid1.destinationdedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update dr_protection_group
  oci_disaster_recovery_dr_protection_group:
    # required
    dr_protection_group_id: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    log_location:
      # required
      namespace: namespace_example
      bucket: bucket_example
    members:
    - # required
      member_id: "ocid1.member.oc1..xxxxxxEXAMPLExxxxxx"
      member_type: COMPUTE_INSTANCE

      # optional
      is_movable: true
      vnic_mapping:
      - # required
        source_vnic_id: "ocid1.sourcevnic.oc1..xxxxxxEXAMPLExxxxxx"
        destination_subnet_id: "ocid1.destinationsubnet.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        destination_nsg_id_list: [ "destination_nsg_id_list_example" ]
      destination_compartment_id: "ocid1.destinationcompartment.oc1..xxxxxxEXAMPLExxxxxx"
      destination_dedicated_vm_host_id: "ocid1.destinationdedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update dr_protection_group using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_disaster_recovery_dr_protection_group:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    log_location:
      # required
      namespace: namespace_example
      bucket: bucket_example
    members:
    - # required
      member_id: "ocid1.member.oc1..xxxxxxEXAMPLExxxxxx"
      member_type: COMPUTE_INSTANCE

      # optional
      is_movable: true
      vnic_mapping:
      - # required
        source_vnic_id: "ocid1.sourcevnic.oc1..xxxxxxEXAMPLExxxxxx"
        destination_subnet_id: "ocid1.destinationsubnet.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        destination_nsg_id_list: [ "destination_nsg_id_list_example" ]
      destination_compartment_id: "ocid1.destinationcompartment.oc1..xxxxxxEXAMPLExxxxxx"
      destination_dedicated_vm_host_id: "ocid1.destinationdedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete dr_protection_group
  oci_disaster_recovery_dr_protection_group:
    # required
    dr_protection_group_id: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete dr_protection_group using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_disaster_recovery_dr_protection_group:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.disaster_recovery import DisasterRecoveryClient
    from oci.disaster_recovery.models import CreateDrProtectionGroupDetails
    from oci.disaster_recovery.models import UpdateDrProtectionGroupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrProtectionGroupHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DrProtectionGroupHelperGen, self).get_possible_entity_types() + [
            "drprotectiongroup",
            "drprotectiongroups",
            "disasterRecoverydrprotectiongroup",
            "disasterRecoverydrprotectiongroups",
            "drprotectiongroupresource",
            "drprotectiongroupsresource",
            "disasterrecovery",
        ]

    def get_module_resource_id_param(self):
        return "dr_protection_group_id"

    def get_module_resource_id(self):
        return self.module.params.get("dr_protection_group_id")

    def get_get_fn(self):
        return self.client.get_dr_protection_group

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_dr_protection_group,
            dr_protection_group_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dr_protection_group,
            dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["dr_protection_group_id", "display_name"]

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
            self.client.list_dr_protection_groups, **kwargs
        )

    def get_create_model_class(self):
        return CreateDrProtectionGroupDetails

    def get_exclude_attributes(self):
        return ["association"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_dr_protection_group,
            call_fn_args=(),
            call_fn_kwargs=dict(create_dr_protection_group_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDrProtectionGroupDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_dr_protection_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_dr_protection_group_details=update_details,
                dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_dr_protection_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DrProtectionGroupHelperCustom = get_custom_class("DrProtectionGroupHelperCustom")


class ResourceHelper(DrProtectionGroupHelperCustom, DrProtectionGroupHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            association=dict(
                type="dict",
                options=dict(
                    peer_id=dict(type="str"),
                    peer_region=dict(type="str"),
                    role=dict(
                        type="str",
                        required=True,
                        choices=["PRIMARY", "STANDBY", "UNCONFIGURED"],
                    ),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            log_location=dict(
                type="dict",
                options=dict(
                    namespace=dict(type="str", required=True),
                    bucket=dict(type="str", required=True),
                ),
            ),
            members=dict(
                type="list",
                elements="dict",
                options=dict(
                    is_movable=dict(type="bool"),
                    vnic_mapping=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            source_vnic_id=dict(type="str", required=True),
                            destination_subnet_id=dict(type="str", required=True),
                            destination_nsg_id_list=dict(type="list", elements="str"),
                        ),
                    ),
                    destination_compartment_id=dict(type="str"),
                    destination_dedicated_vm_host_id=dict(type="str"),
                    member_id=dict(type="str", required=True),
                    member_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "COMPUTE_INSTANCE",
                            "DATABASE",
                            "AUTONOMOUS_DATABASE",
                            "VOLUME_GROUP",
                        ],
                    ),
                    password_vault_secret_id=dict(type="str"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            dr_protection_group_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
