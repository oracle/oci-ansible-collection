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
module: oci_file_storage_replication
short_description: Manage a Replication resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Replication resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new replication in the specified compartment.
      Replications are the primary resource that governs the policy of cross-region replication between source
      and target file systems. Replications are associated with a secondary resource called a L(`ReplicationTarget`,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/iaas/latest/ReplicationTarget)
      located in another availability domain.
      The associated replication target resource is automatically created along with the replication resource.
      The replication retrieves the delta of data between two snapshots of a source file system
      and sends it to the associated `ReplicationTarget`, which retrieves the delta and applies it to the target
      file system.
      Only unexported file systems can be used as target file systems.
      For more information, see L(Using Replication,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/FSreplication.htm).
    - For information about access control and compartments, see
      L(Overview of the IAM
      Service,https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm).
    - For information about availability domains, see L(Regions and
      Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm).
      To get a list of availability domains, use the
      `ListAvailabilityDomains` operation in the Identity and Access
      Management Service API.
    - All Oracle Cloud Infrastructure Services resources, including
      replications, get an Oracle-assigned, unique ID called an
      Oracle Cloud Identifier (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)).
      When you create a resource, you can find its OCID in the response.
      You can also retrieve a resource's OCID by using a List API operation on that resource
      type, or by viewing the resource in the Console.
    - "This resource has the following action operations in the M(oracle.oci.oci_file_storage_replication_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the replication.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source file system.
            - Required for create using I(state=present).
        type: str
    target_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the target file system.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - "A user-friendly name. It does not have to be unique, and it is changeable.
              Avoid entering confidential information.
              An associated replication target will also created with the same `displayName`.
              Example: `My replication`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    replication_interval:
        description:
            - Duration in minutes between replication snapshots.
            - This parameter is updatable.
        type: int
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair
               with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    replication_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the replication.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    delete_mode:
        description:
            - "You can choose a mode for deleting the replication resource.
              - `FINISH_CYCLE_IF_CAPTURING_OR_APPLYING` Before deleting, complete the current delta cycle. If cycle is idle, delete immediately. Safest option.
              - `ONE_MORE_CYCLE` Before deleting, complete the current delta cycle, and initiate one more cycle. If cycle is idle, initiate one more cycle. Use
                for lossless failover.
              - `FINISH_CYCLE_IF_APPLYING` Before deleting, finish applying. If cycle is idle or capturing, delete immediately. Fastest option."
        type: str
        choices:
            - "FINISH_CYCLE_IF_CAPTURING_OR_APPLYING"
            - "ONE_MORE_CYCLE"
            - "FINISH_CYCLE_IF_APPLYING"
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the Replication.
            - Use I(state=present) to create or update a Replication.
            - Use I(state=absent) to delete a Replication.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create replication
  oci_file_storage_replication:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    source_id: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    replication_interval: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update replication
  oci_file_storage_replication:
    # required
    replication_id: "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    replication_interval: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update replication using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_file_storage_replication:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    availability_domain: Uocm:PHX-AD-1

    # optional
    replication_interval: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete replication
  oci_file_storage_replication:
    # required
    replication_id: "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    delete_mode: FINISH_CYCLE_IF_CAPTURING_OR_APPLYING

- name: Delete replication using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_file_storage_replication:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    availability_domain: Uocm:PHX-AD-1
    state: absent

"""

RETURN = """
replication:
    description:
        - Details of the Replication resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the replication.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        availability_domain:
            description:
                - "The availability domain that contains the replication. May be unset as a blank or `NULL` value.
                  Example: `Uocm:PHX-AD-2`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the replication.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current lifecycle state of the replication.
            returned: on success
            type: str
            sample: CREATING
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
                - "Example: `My replication`"
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The date and time the replication was created
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2021-01-04T20:01:29.100Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source file system.
            returned: on success
            type: str
            sample: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
        target_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the target file system.
            returned: on success
            type: str
            sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
        replication_target_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
                  L(`ReplicationTarget`,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/ReplicationTarget).
            returned: on success
            type: str
            sample: "ocid1.replicationtarget.oc1..xxxxxxEXAMPLExxxxxx"
        replication_interval:
            description:
                - Duration in minutes between replication snapshots.
            returned: on success
            type: int
            sample: 56
        last_snapshot_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last snapshot that has been replicated completely.
                  Empty if the copy of the initial snapshot is not complete.
            returned: on success
            type: str
            sample: "ocid1.lastsnapshot.oc1..xxxxxxEXAMPLExxxxxx"
        recovery_point_time:
            description:
                - "The L(`snapshotTime`,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Snapshot/snapshotTime) of the most recent recoverable
                  replication snapshot
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                  Example: `2021-04-04T20:01:29.100Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        delta_status:
            description:
                - The current state of the snapshot during replication operations.
            returned: on success
            type: str
            sample: IDLE
        lifecycle_details:
            description:
                - Additional information about the current 'lifecycleState'.
            returned: on success
            type: str
            sample: lifecycle_details_example
        delta_progress:
            description:
                - Percentage progress of the current replication cycle.
            returned: on success
            type: int
            sample: 56
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair
                   with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_domain": "Uocm:PHX-AD-1",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
        "replication_target_id": "ocid1.replicationtarget.oc1..xxxxxxEXAMPLExxxxxx",
        "replication_interval": 56,
        "last_snapshot_id": "ocid1.lastsnapshot.oc1..xxxxxxEXAMPLExxxxxx",
        "recovery_point_time": "2013-10-20T19:20:30+01:00",
        "delta_status": "IDLE",
        "lifecycle_details": "lifecycle_details_example",
        "delta_progress": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.file_storage import FileStorageClient
    from oci.file_storage.models import CreateReplicationDetails
    from oci.file_storage.models import UpdateReplicationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ReplicationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ReplicationHelperGen, self).get_possible_entity_types() + [
            "replication",
            "replications",
            "fileStoragereplication",
            "fileStoragereplications",
            "replicationresource",
            "replicationsresource",
            "filestorage",
        ]

    def get_module_resource_id_param(self):
        return "replication_id"

    def get_module_resource_id(self):
        return self.module.params.get("replication_id")

    def get_get_fn(self):
        return self.client.get_replication

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_replication, replication_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_replication,
            replication_id=self.module.params.get("replication_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "availability_domain",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_replications, **kwargs
        )

    def get_create_model_class(self):
        return CreateReplicationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_replication,
            call_fn_args=(),
            call_fn_kwargs=dict(create_replication_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateReplicationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_replication,
            call_fn_args=(),
            call_fn_kwargs=dict(
                replication_id=self.module.params.get("replication_id"),
                update_replication_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        optional_enum_params = [
            "delete_mode",
        ]
        optional_enum_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_enum_params
            if self.module.params.get(param) is not None
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_replication,
            call_fn_args=(),
            call_fn_kwargs=dict(
                replication_id=self.module.params.get("replication_id"),
                **optional_enum_kwargs
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ReplicationHelperCustom = get_custom_class("ReplicationHelperCustom")


class ResourceHelper(ReplicationHelperCustom, ReplicationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            source_id=dict(type="str"),
            target_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            replication_interval=dict(type="int"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            replication_id=dict(aliases=["id"], type="str"),
            delete_mode=dict(
                type="str",
                choices=[
                    "FINISH_CYCLE_IF_CAPTURING_OR_APPLYING",
                    "ONE_MORE_CYCLE",
                    "FINISH_CYCLE_IF_APPLYING",
                ],
            ),
            availability_domain=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="replication",
        service_client_class=FileStorageClient,
        namespace="file_storage",
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
