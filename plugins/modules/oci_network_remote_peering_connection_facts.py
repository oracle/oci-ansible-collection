#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_network_remote_peering_connection_facts
short_description: Fetches details about one or multiple RemotePeeringConnection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RemotePeeringConnection resources in Oracle Cloud Infrastructure
    - Lists the remote peering connections (RPCs) for the specified DRG and compartment
      (the RPC's compartment).
    - If I(remote_peering_connection_id) is specified, the details of a single RemotePeeringConnection will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    remote_peering_connection_id:
        description:
            - The OCID of the remote peering connection (RPC).
            - Required to get a specific remote_peering_connection.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple remote_peering_connections.
        type: str
    drg_id:
        description:
            - The OCID of the DRG.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List remote_peering_connections
  oci_network_remote_peering_connection_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific remote_peering_connection
  oci_network_remote_peering_connection_facts:
    remote_peering_connection_id: ocid1.remotepeeringconnection.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
remote_peering_connections:
    description:
        - List of RemotePeeringConnection resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment that contains the RPC.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        drg_id:
            description:
                - The OCID of the DRG that this RPC belongs to.
            returned: on success
            type: string
            sample: ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of the RPC.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        is_cross_tenancy_peering:
            description:
                - Whether the VCN at the other end of the peering is in a different tenancy.
                - "Example: `false`"
            returned: on success
            type: bool
            sample: false
        lifecycle_state:
            description:
                - The RPC's current lifecycle state.
            returned: on success
            type: string
            sample: AVAILABLE
        peer_id:
            description:
                - If this RPC is peered, this value is the OCID of the other RPC.
            returned: on success
            type: string
            sample: ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx
        peer_region_name:
            description:
                - If this RPC is peered, this value is the region that contains the other RPC.
                - "Example: `us-ashburn-1`"
            returned: on success
            type: string
            sample: us-ashburn-1
        peer_tenancy_id:
            description:
                - If this RPC is peered, this value is the OCID of the other RPC's tenancy.
            returned: on success
            type: string
            sample: ocid1.peertenancy.oc1..xxxxxxEXAMPLExxxxxx
        peering_status:
            description:
                - Whether the RPC is peered with another RPC. `NEW` means the RPC has not yet been
                  peered. `PENDING` means the peering is being established. `REVOKED` means the
                  RPC at the other end of the peering has been deleted.
            returned: on success
            type: string
            sample: INVALID
        time_created:
            description:
                - The date and time the RPC was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "drg_id": "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cross_tenancy_peering": false,
        "lifecycle_state": "AVAILABLE",
        "peer_id": "ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_region_name": "us-ashburn-1",
        "peer_tenancy_id": "ocid1.peertenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "peering_status": "INVALID",
        "time_created": "2016-08-25T21:10:29.600Z"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RemotePeeringConnectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "remote_peering_connection_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_remote_peering_connection,
            remote_peering_connection_id=self.module.params.get(
                "remote_peering_connection_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "drg_id",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_remote_peering_connections,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


RemotePeeringConnectionFactsHelperCustom = get_custom_class(
    "RemotePeeringConnectionFactsHelperCustom"
)


class ResourceFactsHelper(
    RemotePeeringConnectionFactsHelperCustom, RemotePeeringConnectionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            remote_peering_connection_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            drg_id=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="remote_peering_connection",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(remote_peering_connections=result)


if __name__ == "__main__":
    main()
