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
module: oci_file_storage_replication_target
short_description: Manage a ReplicationTarget resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to delete a ReplicationTarget resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    replication_target_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the replication target.
        type: str
        aliases: ["id"]
        required: true
    state:
        description:
            - The state of the ReplicationTarget.
            - Use I(state=absent) to delete a ReplicationTarget.
        type: str
        required: false
        default: 'present'
        choices: ["absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Delete replication_target
  oci_file_storage_replication_target:
    # required
    replication_target_id: "ocid1.replicationtarget.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
replication_target:
    description:
        - Details of the ReplicationTarget resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain the replication resource is in. May be unset
                  as a blank or NULL value.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the replication.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the replication.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of this replication.
            returned: on success
            type: str
            sample: CREATING
        display_name:
            description:
                - "A user-friendly name. This name is same as the replication display name for the associated resource.
                  Example: `My Replication`"
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - "The date and time the replication target was created in target region.
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                  Example: `2021-01-04T20:01:29.100Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of source filesystem.
            returned: on success
            type: str
            sample: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
        target_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of target filesystem.
            returned: on success
            type: str
            sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
        replication_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of replication.
            returned: on success
            type: str
            sample: "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx"
        last_snapshot_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last snapshot snapshot which was completely applied
                  to the target file system.
                  Empty while the initial snapshot is being applied.
            returned: on success
            type: str
            sample: "ocid1.lastsnapshot.oc1..xxxxxxEXAMPLExxxxxx"
        recovery_point_time:
            description:
                - "The snapshotTime of the most recent recoverable replication snapshot
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
        lifecycle_details:
            description:
                - Additional information about the current `lifecycleState`.
            returned: on success
            type: str
            sample: lifecycle_details_example
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
        "replication_id": "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx",
        "last_snapshot_id": "ocid1.lastsnapshot.oc1..xxxxxxEXAMPLExxxxxx",
        "recovery_point_time": "2013-10-20T19:20:30+01:00",
        "delta_status": "IDLE",
        "delta_progress": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "lifecycle_details": "lifecycle_details_example"
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

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ReplicationTargetHelperGen(OCIResourceHelperBase):
    """Supported operations: get, list and delete"""

    def get_possible_entity_types(self):
        return super(ReplicationTargetHelperGen, self).get_possible_entity_types() + [
            "replicationtarget",
            "replicationtargets",
            "fileStoragereplicationtarget",
            "fileStoragereplicationtargets",
            "replicationtargetresource",
            "replicationtargetsresource",
            "filestorage",
        ]

    def get_module_resource_id_param(self):
        return "replication_target_id"

    def get_module_resource_id(self):
        return self.module.params.get("replication_target_id")

    def get_get_fn(self):
        return self.client.get_replication_target

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_replication_target, replication_target_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_replication_target,
            replication_target_id=self.module.params.get("replication_target_id"),
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
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_replication_targets, **kwargs
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_replication_target,
            call_fn_args=(),
            call_fn_kwargs=dict(
                replication_target_id=self.module.params.get("replication_target_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ReplicationTargetHelperCustom = get_custom_class("ReplicationTargetHelperCustom")


class ResourceHelper(ReplicationTargetHelperCustom, ReplicationTargetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            replication_target_id=dict(aliases=["id"], type="str", required=True),
            state=dict(type="str", default="present", choices=["absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="replication_target",
        service_client_class=FileStorageClient,
        namespace="file_storage",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
