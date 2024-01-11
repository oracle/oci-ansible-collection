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
module: oci_file_storage_replication_target_facts
short_description: Fetches details about one or multiple ReplicationTarget resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ReplicationTarget resources in Oracle Cloud Infrastructure
    - Lists the replication target resources in the specified compartment.
    - If I(replication_target_id) is specified, the details of a single ReplicationTarget will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    replication_target_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the replication target.
            - Required to get a specific replication_target.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple replication_targets.
        type: str
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
            - Required to list multiple replication_targets.
        type: str
    lifecycle_state:
        description:
            - Filter results by the specified lifecycle state. Must be a valid
              state for the resource type.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A user-friendly name. It does not have to be unique, and it is changeable.
            - "Example: `My resource`"
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort by. You can choose either value, but not both.
              By default, when you sort by `timeCreated`, results are shown
              in descending order. When you sort by `displayName`, results are
              shown in ascending order.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc', where 'asc' is
              ascending and 'desc' is descending. The default order is 'desc'
              except for numeric values.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific replication_target
  oci_file_storage_replication_target_facts:
    # required
    replication_target_id: "ocid1.replicationtarget.oc1..xxxxxxEXAMPLExxxxxx"

- name: List replication_targets
  oci_file_storage_replication_target_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1

    # optional
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_by: timeCreated
    sort_order: ASC

"""

RETURN = """
replication_targets:
    description:
        - List of ReplicationTarget resources
    returned: on success
    type: complex
    contains:
        source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of source filesystem.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
        target_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of target filesystem.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
        replication_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of replication.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx"
        last_snapshot_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last snapshot snapshot which was completely applied
                  to the target file system.
                  Empty while the initial snapshot is being applied.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.lastsnapshot.oc1..xxxxxxEXAMPLExxxxxx"
        delta_status:
            description:
                - The current state of the snapshot during replication operations.
                - Returned for get operation
            returned: on success
            type: str
            sample: IDLE
        delta_progress:
            description:
                - Percentage progress of the current replication cycle.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
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
        recovery_point_time:
            description:
                - "The snapshotTime of the most recent recoverable replication snapshot
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                  Example: `2021-04-04T20:01:29.100Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
        "replication_id": "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx",
        "last_snapshot_id": "ocid1.lastsnapshot.oc1..xxxxxxEXAMPLExxxxxx",
        "delta_status": "IDLE",
        "delta_progress": 56,
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "lifecycle_details": "lifecycle_details_example",
        "recovery_point_time": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.file_storage import FileStorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ReplicationTargetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "replication_target_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "availability_domain",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_replication_target,
            replication_target_id=self.module.params.get("replication_target_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_replication_targets,
            compartment_id=self.module.params.get("compartment_id"),
            availability_domain=self.module.params.get("availability_domain"),
            **optional_kwargs
        )


ReplicationTargetFactsHelperCustom = get_custom_class(
    "ReplicationTargetFactsHelperCustom"
)


class ResourceFactsHelper(
    ReplicationTargetFactsHelperCustom, ReplicationTargetFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            replication_target_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            availability_domain=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="replication_target",
        service_client_class=FileStorageClient,
        namespace="file_storage",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(replication_targets=result)


if __name__ == "__main__":
    main()
