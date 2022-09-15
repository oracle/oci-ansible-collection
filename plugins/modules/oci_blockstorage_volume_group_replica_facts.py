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
module: oci_blockstorage_volume_group_replica_facts
short_description: Fetches details about one or multiple VolumeGroupReplica resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VolumeGroupReplica resources in Oracle Cloud Infrastructure
    - Lists the volume group replicas in the specified compartment. You can filter the results by volume group.
      For more information, see L(Volume Group Replication,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroupreplication.htm).
    - If I(volume_group_replica_id) is specified, the details of a single VolumeGroupReplica will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    volume_group_replica_id:
        description:
            - The OCID of the volume replica group.
            - Required to get a specific volume_group_replica.
        type: str
        aliases: ["id"]
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
            - Required to list multiple volume_group_replicas.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple volume_group_replicas.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "ACTIVATING"
            - "TERMINATING"
            - "TERMINATED"
            - "FAULTY"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific volume_group_replica
  oci_blockstorage_volume_group_replica_facts:
    # required
    volume_group_replica_id: "ocid1.volumegroupreplica.oc1..xxxxxxEXAMPLExxxxxx"

- name: List volume_group_replicas
  oci_blockstorage_volume_group_replica_facts:
    # required
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: PROVISIONING

"""

RETURN = """
volume_group_replicas:
    description:
        - List of VolumeGroupReplica resources
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain of the volume group replica.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment that contains the volume group replica.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID for the volume group replica.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of a volume group.
            returned: on success
            type: str
            sample: PROVISIONING
        size_in_gbs:
            description:
                - The aggregate size of the volume group replica in GBs.
            returned: on success
            type: int
            sample: 56
        volume_group_id:
            description:
                - The OCID of the source volume group.
            returned: on success
            type: str
            sample: "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the volume group replica was created. Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        member_replicas:
            description:
                - Volume replicas within this volume group replica.
            returned: on success
            type: complex
            contains:
                volume_replica_id:
                    description:
                        - The volume replica ID.
                    returned: on success
                    type: str
                    sample: "ocid1.volumereplica.oc1..xxxxxxEXAMPLExxxxxx"
                membership_state:
                    description:
                        - Membership state of the volume replica in relation to the volume group replica.
                    returned: on success
                    type: str
                    sample: ADD_PENDING
        time_last_synced:
            description:
                - The date and time the volume group replica was last synced from the source volume group.
                  Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "size_in_gbs": 56,
        "volume_group_id": "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "member_replicas": [{
            "volume_replica_id": "ocid1.volumereplica.oc1..xxxxxxEXAMPLExxxxxx",
            "membership_state": "ADD_PENDING"
        }],
        "time_last_synced": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import BlockstorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeGroupReplicaFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "volume_group_replica_id",
        ]

    def get_required_params_for_list(self):
        return [
            "availability_domain",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume_group_replica,
            volume_group_replica_id=self.module.params.get("volume_group_replica_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_volume_group_replicas,
            availability_domain=self.module.params.get("availability_domain"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


VolumeGroupReplicaFactsHelperCustom = get_custom_class(
    "VolumeGroupReplicaFactsHelperCustom"
)


class ResourceFactsHelper(
    VolumeGroupReplicaFactsHelperCustom, VolumeGroupReplicaFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            volume_group_replica_id=dict(aliases=["id"], type="str"),
            availability_domain=dict(type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "AVAILABLE",
                    "ACTIVATING",
                    "TERMINATING",
                    "TERMINATED",
                    "FAULTY",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="volume_group_replica",
        service_client_class=BlockstorageClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(volume_group_replicas=result)


if __name__ == "__main__":
    main()
