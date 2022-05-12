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
module: oci_network_vtap
short_description: Manage a Vtap resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Vtap resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a virtual test access point (VTAP) in the specified compartment.
    - For the purposes of access control, you must provide the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
      that contains the VTAP.
      For more information about compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
      For information about OCIDs, see L(Resource Identifiers,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    - "You may optionally specify a *display name* for the VTAP, otherwise a default is provided.
      It does not have to be unique, and you can change it."
    - "This resource has the following action operations in the M(oracle.oci.oci_network_vtap_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the `Vtap` resource.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN containing the `Vtap` resource.
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
    source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source point where packets are captured.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    target_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the destination resource where mirrored packets are sent.
            - This parameter is updatable.
        type: str
    target_ip:
        description:
            - The IP address of the destination resource where mirrored packets are sent.
            - This parameter is updatable.
        type: str
    capture_filter_id:
        description:
            - The capture filter's Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)).
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    encapsulation_protocol:
        description:
            - Defines an encapsulation header type for the VTAP's mirrored traffic.
            - This parameter is updatable.
        type: str
        choices:
            - "VXLAN"
    vxlan_network_identifier:
        description:
            - The virtual extensible LAN (VXLAN) network identifier (or VXLAN segment ID) that uniquely identifies the VXLAN.
            - This parameter is updatable.
        type: int
    is_vtap_enabled:
        description:
            - Used to start or stop a `Vtap` resource.
            - "* `TRUE` directs the VTAP to start mirroring traffic.
              * `FALSE` (Default) directs the VTAP to stop mirroring traffic."
            - This parameter is updatable.
        type: bool
    traffic_mode:
        description:
            - Used to control the priority of traffic. It is an optional field. If it not passed, the value is DEFAULT
            - This parameter is updatable.
        type: str
        choices:
            - "DEFAULT"
            - "PRIORITY"
    max_packet_size:
        description:
            - The maximum size of the packets to be included in the filter.
            - This parameter is updatable.
        type: int
    source_private_endpoint_ip:
        description:
            - The IP Address of the source private endpoint.
            - This parameter is updatable.
        type: str
    source_private_endpoint_subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet that source private endpoint belongs to.
            - This parameter is updatable.
        type: str
    target_type:
        description:
            - The target type for the VTAP.
            - This parameter is updatable.
        type: str
        choices:
            - "VNIC"
            - "NETWORK_LOAD_BALANCER"
            - "IP_ADDRESS"
    source_type:
        description:
            - The source type for the VTAP.
            - This parameter is updatable.
        type: str
        choices:
            - "VNIC"
            - "SUBNET"
            - "LOAD_BALANCER"
            - "DB_SYSTEM"
            - "EXADATA_VM_CLUSTER"
            - "AUTONOMOUS_DATA_WAREHOUSE"
    vtap_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VTAP.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Vtap.
            - Use I(state=present) to create or update a Vtap.
            - Use I(state=absent) to delete a Vtap.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create vtap
  oci_network_vtap:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    source_id: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
    capture_filter_id: "ocid1.capturefilter.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    target_ip: target_ip_example
    encapsulation_protocol: VXLAN
    vxlan_network_identifier: 56
    is_vtap_enabled: true
    traffic_mode: DEFAULT
    max_packet_size: 56
    source_private_endpoint_ip: source_private_endpoint_ip_example
    source_private_endpoint_subnet_id: "ocid1.sourceprivateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx"
    target_type: VNIC
    source_type: VNIC

- name: Update vtap
  oci_network_vtap:
    # required
    vtap_id: "ocid1.vtap.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    source_id: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    target_ip: target_ip_example
    capture_filter_id: "ocid1.capturefilter.oc1..xxxxxxEXAMPLExxxxxx"
    encapsulation_protocol: VXLAN
    vxlan_network_identifier: 56
    is_vtap_enabled: true
    traffic_mode: DEFAULT
    max_packet_size: 56
    source_private_endpoint_ip: source_private_endpoint_ip_example
    source_private_endpoint_subnet_id: "ocid1.sourceprivateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx"
    target_type: VNIC
    source_type: VNIC

- name: Update vtap using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_vtap:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    source_id: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    target_ip: target_ip_example
    capture_filter_id: "ocid1.capturefilter.oc1..xxxxxxEXAMPLExxxxxx"
    encapsulation_protocol: VXLAN
    vxlan_network_identifier: 56
    is_vtap_enabled: true
    traffic_mode: DEFAULT
    max_packet_size: 56
    source_private_endpoint_ip: source_private_endpoint_ip_example
    source_private_endpoint_subnet_id: "ocid1.sourceprivateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx"
    target_type: VNIC
    source_type: VNIC

- name: Delete vtap
  oci_network_vtap:
    # required
    vtap_id: "ocid1.vtap.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete vtap using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_vtap:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
vtap:
    description:
        - Details of the Vtap resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the `Vtap` resource.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN containing the `Vtap` resource.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
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
                - The VTAP's Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The VTAP's administrative lifecycle state.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_state_details:
            description:
                - The VTAP's current running state.
            returned: on success
            type: str
            sample: RUNNING
        time_created:
            description:
                - The date and time the VTAP was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2020-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source point where packets are captured.
            returned: on success
            type: str
            sample: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
        target_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the destination resource where mirrored packets are
                  sent.
            returned: on success
            type: str
            sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
        target_ip:
            description:
                - The IP address of the destination resource where mirrored packets are sent.
            returned: on success
            type: str
            sample: target_ip_example
        capture_filter_id:
            description:
                - The capture filter's Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.capturefilter.oc1..xxxxxxEXAMPLExxxxxx"
        encapsulation_protocol:
            description:
                - Defines an encapsulation header type for the VTAP's mirrored traffic.
            returned: on success
            type: str
            sample: VXLAN
        vxlan_network_identifier:
            description:
                - The virtual extensible LAN (VXLAN) network identifier (or VXLAN segment ID) that uniquely identifies the VXLAN.
            returned: on success
            type: int
            sample: 56
        is_vtap_enabled:
            description:
                - Used to start or stop a `Vtap` resource.
                - "* `TRUE` directs the VTAP to start mirroring traffic.
                  * `FALSE` (Default) directs the VTAP to stop mirroring traffic."
            returned: on success
            type: bool
            sample: true
        source_type:
            description:
                - The source type for the VTAP.
            returned: on success
            type: str
            sample: VNIC
        traffic_mode:
            description:
                - Used to control the priority of traffic. It is an optional field. If it not passed, the value is DEFAULT
            returned: on success
            type: str
            sample: DEFAULT
        max_packet_size:
            description:
                - The maximum size of the packets to be included in the filter.
            returned: on success
            type: int
            sample: 56
        target_type:
            description:
                - The target type for the VTAP.
            returned: on success
            type: str
            sample: VNIC
        source_private_endpoint_ip:
            description:
                - The IP Address of the source private endpoint.
            returned: on success
            type: str
            sample: source_private_endpoint_ip_example
        source_private_endpoint_subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet that source private endpoint belongs to.
            returned: on success
            type: str
            sample: "ocid1.sourceprivateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_state_details": "RUNNING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
        "target_ip": "target_ip_example",
        "capture_filter_id": "ocid1.capturefilter.oc1..xxxxxxEXAMPLExxxxxx",
        "encapsulation_protocol": "VXLAN",
        "vxlan_network_identifier": 56,
        "is_vtap_enabled": true,
        "source_type": "VNIC",
        "traffic_mode": "DEFAULT",
        "max_packet_size": 56,
        "target_type": "VNIC",
        "source_private_endpoint_ip": "source_private_endpoint_ip_example",
        "source_private_endpoint_subnet_id": "ocid1.sourceprivateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateVtapDetails
    from oci.core.models import UpdateVtapDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VtapHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(VtapHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_possible_entity_types(self):
        return super(VtapHelperGen, self).get_possible_entity_types() + [
            "vtap",
            "vtaps",
            "corevtap",
            "corevtaps",
            "vtapresource",
            "vtapsresource",
            "core",
        ]

    def get_module_resource_id_param(self):
        return "vtap_id"

    def get_module_resource_id(self):
        return self.module.params.get("vtap_id")

    def get_get_fn(self):
        return self.client.get_vtap

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vtap, vtap_id=self.module.params.get("vtap_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["vcn_id", "display_name"]
            if self._use_name_as_identifier()
            else ["vcn_id", "target_id", "target_ip", "is_vtap_enabled", "display_name"]
        )

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
        return oci_common_utils.list_all_resources(self.client.list_vtaps, **kwargs)

    def get_create_model_class(self):
        return CreateVtapDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_vtap,
            call_fn_args=(),
            call_fn_kwargs=dict(create_vtap_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateVtapDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_vtap,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vtap_id=self.module.params.get("vtap_id"),
                update_vtap_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_vtap,
            call_fn_args=(),
            call_fn_kwargs=dict(vtap_id=self.module.params.get("vtap_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


VtapHelperCustom = get_custom_class("VtapHelperCustom")


class ResourceHelper(VtapHelperCustom, VtapHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            vcn_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            source_id=dict(type="str"),
            target_id=dict(type="str"),
            target_ip=dict(type="str"),
            capture_filter_id=dict(type="str"),
            encapsulation_protocol=dict(type="str", choices=["VXLAN"]),
            vxlan_network_identifier=dict(type="int"),
            is_vtap_enabled=dict(type="bool"),
            traffic_mode=dict(type="str", choices=["DEFAULT", "PRIORITY"]),
            max_packet_size=dict(type="int"),
            source_private_endpoint_ip=dict(type="str"),
            source_private_endpoint_subnet_id=dict(type="str"),
            target_type=dict(
                type="str", choices=["VNIC", "NETWORK_LOAD_BALANCER", "IP_ADDRESS"]
            ),
            source_type=dict(
                type="str",
                choices=[
                    "VNIC",
                    "SUBNET",
                    "LOAD_BALANCER",
                    "DB_SYSTEM",
                    "EXADATA_VM_CLUSTER",
                    "AUTONOMOUS_DATA_WAREHOUSE",
                ],
            ),
            vtap_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vtap",
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
