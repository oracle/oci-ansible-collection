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
module: oci_network_remote_peering_connection
short_description: Manage a RemotePeeringConnection resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a RemotePeeringConnection resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new remote peering connection (RPC) for the specified DRG.
    - "This resource has the following action operations in the M(oracle.oci.oci_network_remote_peering_connection_actions) module: change_compartment,
      connect."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the RPC.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    drg_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG the RPC belongs to.
            - Required for create using I(state=present).
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    remote_peering_connection_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the remote peering connection (RPC).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the RemotePeeringConnection.
            - Use I(state=present) to create or update a RemotePeeringConnection.
            - Use I(state=absent) to delete a RemotePeeringConnection.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create remote_peering_connection
  oci_network_remote_peering_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    drg_id: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}

- name: Update remote_peering_connection
  oci_network_remote_peering_connection:
    # required
    remote_peering_connection_id: "ocid1.remotepeeringconnection.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}

- name: Update remote_peering_connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_remote_peering_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Delete remote_peering_connection
  oci_network_remote_peering_connection:
    # required
    remote_peering_connection_id: "ocid1.remotepeeringconnection.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete remote_peering_connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_remote_peering_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
remote_peering_connection:
    description:
        - Details of the RemotePeeringConnection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the RPC.
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
        drg_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG that this RPC belongs to.
            returned: on success
            type: str
            sample: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
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
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the RPC.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        is_cross_tenancy_peering:
            description:
                - Whether the VCN at the other end of the peering is in a different tenancy.
                - "Example: `false`"
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The RPC's current lifecycle state.
            returned: on success
            type: str
            sample: AVAILABLE
        peer_id:
            description:
                - If this RPC is peered, this value is the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the other RPC.
            returned: on success
            type: str
            sample: "ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx"
        peer_region_name:
            description:
                - If this RPC is peered, this value is the region that contains the other RPC.
                - "Example: `us-ashburn-1`"
            returned: on success
            type: str
            sample: us-phoenix-1
        peer_tenancy_id:
            description:
                - If this RPC is peered, this value is the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the other
                  RPC's tenancy.
            returned: on success
            type: str
            sample: "ocid1.peertenancy.oc1..xxxxxxEXAMPLExxxxxx"
        peering_status:
            description:
                - Whether the RPC is peered with another RPC. `NEW` means the RPC has not yet been
                  peered. `PENDING` means the peering is being established. `REVOKED` means the
                  RPC at the other end of the peering has been deleted.
            returned: on success
            type: str
            sample: INVALID
        time_created:
            description:
                - The date and time the RPC was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "drg_id": "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cross_tenancy_peering": true,
        "lifecycle_state": "AVAILABLE",
        "peer_id": "ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_region_name": "us-phoenix-1",
        "peer_tenancy_id": "ocid1.peertenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "peering_status": "INVALID",
        "time_created": "2013-10-20T19:20:30+01:00"
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateRemotePeeringConnectionDetails
    from oci.core.models import UpdateRemotePeeringConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RemotePeeringConnectionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            RemotePeeringConnectionHelperGen, self
        ).get_possible_entity_types() + [
            "remotepeeringconnection",
            "remotepeeringconnections",
            "coreremotepeeringconnection",
            "coreremotepeeringconnections",
            "remotepeeringconnectionresource",
            "remotepeeringconnectionsresource",
            "core",
        ]

    def get_module_resource_id_param(self):
        return "remote_peering_connection_id"

    def get_module_resource_id(self):
        return self.module.params.get("remote_peering_connection_id")

    def get_get_fn(self):
        return self.client.get_remote_peering_connection

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_remote_peering_connection,
            remote_peering_connection_id=self.module.params.get(
                "remote_peering_connection_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["drg_id"]

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
            self.client.list_remote_peering_connections, **kwargs
        )

    def get_create_model_class(self):
        return CreateRemotePeeringConnectionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_remote_peering_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_remote_peering_connection_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateRemotePeeringConnectionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_remote_peering_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                remote_peering_connection_id=self.module.params.get(
                    "remote_peering_connection_id"
                ),
                update_remote_peering_connection_details=update_details,
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
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_remote_peering_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                remote_peering_connection_id=self.module.params.get(
                    "remote_peering_connection_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


RemotePeeringConnectionHelperCustom = get_custom_class(
    "RemotePeeringConnectionHelperCustom"
)


class ResourceHelper(
    RemotePeeringConnectionHelperCustom, RemotePeeringConnectionHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            drg_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            remote_peering_connection_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="remote_peering_connection",
        service_client_class=VirtualNetworkClient,
        namespace="core",
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
