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
module: oci_network_capture_filter
short_description: Manage a CaptureFilter resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a CaptureFilter resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a virtual test access point (VTAP) capture filter in the specified compartment.
    - For the purposes of access control, you must provide the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the
      compartment that contains
      the VTAP. For more information about compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
      For information about OCIDs, see L(Resource Identifiers,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    - "You may optionally specify a *display name* for the VTAP, otherwise a default is provided.
      It does not have to be unique, and you can change it."
    - "This resource has the following action operations in the M(oracle.oci.oci_network_capture_filter_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the capture filter.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    filter_type:
        description:
            - Indicates which service will use this capture filter
            - Required for create using I(state=present).
        type: str
        choices:
            - "VTAP"
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
    vtap_capture_filter_rules:
        description:
            - The set of rules governing what traffic a VTAP mirrors.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            traffic_direction:
                description:
                    - The traffic direction the VTAP is configured to mirror.
                type: str
                choices:
                    - "INGRESS"
                    - "EGRESS"
                required: true
            rule_action:
                description:
                    - Include or exclude packets meeting this definition from mirrored traffic.
                type: str
                choices:
                    - "INCLUDE"
                    - "EXCLUDE"
            source_cidr:
                description:
                    - Traffic from this CIDR block to the VTAP source will be mirrored to the VTAP target.
                type: str
            destination_cidr:
                description:
                    - Traffic sent to this CIDR block through the VTAP source will be mirrored to the VTAP target.
                type: str
            protocol:
                description:
                    - "The transport protocol used in the filter. If do not choose a protocol, all protocols will be used in the filter.
                      Supported options are:
                        * 1 = ICMP
                        * 6 = TCP
                        * 17 = UDP"
                type: str
            icmp_options:
                description:
                    - ""
                type: dict
                suboptions:
                    code:
                        description:
                            - The ICMP code (optional).
                        type: int
                    type:
                        description:
                            - The ICMP type.
                        type: int
                        required: true
            tcp_options:
                description:
                    - ""
                type: dict
                suboptions:
                    destination_port_range:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            max:
                                description:
                                    - The maximum port number, which must not be less than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number, which must not be greater than the maximum port number.
                                type: int
                                required: true
                    source_port_range:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            max:
                                description:
                                    - The maximum port number, which must not be less than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number, which must not be greater than the maximum port number.
                                type: int
                                required: true
            udp_options:
                description:
                    - ""
                type: dict
                suboptions:
                    destination_port_range:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            max:
                                description:
                                    - The maximum port number, which must not be less than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number, which must not be greater than the maximum port number.
                                type: int
                                required: true
                    source_port_range:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            max:
                                description:
                                    - The maximum port number, which must not be less than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number, which must not be greater than the maximum port number.
                                type: int
                                required: true
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    capture_filter_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the capture filter.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the CaptureFilter.
            - Use I(state=present) to create or update a CaptureFilter.
            - Use I(state=absent) to delete a CaptureFilter.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create capture_filter
  oci_network_capture_filter:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    filter_type: VTAP

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    vtap_capture_filter_rules:
    - # required
      traffic_direction: INGRESS

      # optional
      rule_action: INCLUDE
      source_cidr: source_cidr_example
      destination_cidr: destination_cidr_example
      protocol: protocol_example
      icmp_options:
        # required
        type: 56

        # optional
        code: 56
      tcp_options:
        # optional
        destination_port_range:
          # required
          max: 56
          min: 56
        source_port_range:
          # required
          max: 56
          min: 56
      udp_options:
        # optional
        destination_port_range:
          # required
          max: 56
          min: 56
        source_port_range:
          # required
          max: 56
          min: 56
    freeform_tags: {'Department': 'Finance'}

- name: Update capture_filter
  oci_network_capture_filter:
    # required
    capture_filter_id: "ocid1.capturefilter.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    vtap_capture_filter_rules:
    - # required
      traffic_direction: INGRESS

      # optional
      rule_action: INCLUDE
      source_cidr: source_cidr_example
      destination_cidr: destination_cidr_example
      protocol: protocol_example
      icmp_options:
        # required
        type: 56

        # optional
        code: 56
      tcp_options:
        # optional
        destination_port_range:
          # required
          max: 56
          min: 56
        source_port_range:
          # required
          max: 56
          min: 56
      udp_options:
        # optional
        destination_port_range:
          # required
          max: 56
          min: 56
        source_port_range:
          # required
          max: 56
          min: 56
    freeform_tags: {'Department': 'Finance'}

- name: Update capture_filter using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_capture_filter:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vtap_capture_filter_rules:
    - # required
      traffic_direction: INGRESS

      # optional
      rule_action: INCLUDE
      source_cidr: source_cidr_example
      destination_cidr: destination_cidr_example
      protocol: protocol_example
      icmp_options:
        # required
        type: 56

        # optional
        code: 56
      tcp_options:
        # optional
        destination_port_range:
          # required
          max: 56
          min: 56
        source_port_range:
          # required
          max: 56
          min: 56
      udp_options:
        # optional
        destination_port_range:
          # required
          max: 56
          min: 56
        source_port_range:
          # required
          max: 56
          min: 56
    freeform_tags: {'Department': 'Finance'}

- name: Delete capture_filter
  oci_network_capture_filter:
    # required
    capture_filter_id: "ocid1.capturefilter.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete capture_filter using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_capture_filter:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
capture_filter:
    description:
        - Details of the CaptureFilter resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the capture filter.
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
                - The capture filter's Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The capture filter's current administrative state.
            returned: on success
            type: str
            sample: PROVISIONING
        filter_type:
            description:
                - Indicates which service will use this capture filter
            returned: on success
            type: str
            sample: VTAP
        time_created:
            description:
                - The date and time the capture filter was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2021-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vtap_capture_filter_rules:
            description:
                - The set of rules governing what traffic a VTAP mirrors.
            returned: on success
            type: complex
            contains:
                traffic_direction:
                    description:
                        - The traffic direction the VTAP is configured to mirror.
                    returned: on success
                    type: str
                    sample: INGRESS
                rule_action:
                    description:
                        - Include or exclude packets meeting this definition from mirrored traffic.
                    returned: on success
                    type: str
                    sample: INCLUDE
                source_cidr:
                    description:
                        - Traffic from this CIDR block to the VTAP source will be mirrored to the VTAP target.
                    returned: on success
                    type: str
                    sample: source_cidr_example
                destination_cidr:
                    description:
                        - Traffic sent to this CIDR block through the VTAP source will be mirrored to the VTAP target.
                    returned: on success
                    type: str
                    sample: destination_cidr_example
                protocol:
                    description:
                        - "The transport protocol used in the filter. If do not choose a protocol, all protocols will be used in the filter.
                          Supported options are:
                            * 1 = ICMP
                            * 6 = TCP
                            * 17 = UDP"
                    returned: on success
                    type: str
                    sample: protocol_example
                icmp_options:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        code:
                            description:
                                - The ICMP code (optional).
                            returned: on success
                            type: int
                            sample: 56
                        type:
                            description:
                                - The ICMP type.
                            returned: on success
                            type: int
                            sample: 56
                tcp_options:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        destination_port_range:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                max:
                                    description:
                                        - The maximum port number, which must not be less than the minimum port number. To specify
                                          a single port number, set both the min and max to the same value.
                                    returned: on success
                                    type: int
                                    sample: 56
                                min:
                                    description:
                                        - The minimum port number, which must not be greater than the maximum port number.
                                    returned: on success
                                    type: int
                                    sample: 56
                        source_port_range:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                max:
                                    description:
                                        - The maximum port number, which must not be less than the minimum port number. To specify
                                          a single port number, set both the min and max to the same value.
                                    returned: on success
                                    type: int
                                    sample: 56
                                min:
                                    description:
                                        - The minimum port number, which must not be greater than the maximum port number.
                                    returned: on success
                                    type: int
                                    sample: 56
                udp_options:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        destination_port_range:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                max:
                                    description:
                                        - The maximum port number, which must not be less than the minimum port number. To specify
                                          a single port number, set both the min and max to the same value.
                                    returned: on success
                                    type: int
                                    sample: 56
                                min:
                                    description:
                                        - The minimum port number, which must not be greater than the maximum port number.
                                    returned: on success
                                    type: int
                                    sample: 56
                        source_port_range:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                max:
                                    description:
                                        - The maximum port number, which must not be less than the minimum port number. To specify
                                          a single port number, set both the min and max to the same value.
                                    returned: on success
                                    type: int
                                    sample: 56
                                min:
                                    description:
                                        - The minimum port number, which must not be greater than the maximum port number.
                                    returned: on success
                                    type: int
                                    sample: 56
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "filter_type": "VTAP",
        "time_created": "2013-10-20T19:20:30+01:00",
        "vtap_capture_filter_rules": [{
            "traffic_direction": "INGRESS",
            "rule_action": "INCLUDE",
            "source_cidr": "source_cidr_example",
            "destination_cidr": "destination_cidr_example",
            "protocol": "protocol_example",
            "icmp_options": {
                "code": 56,
                "type": 56
            },
            "tcp_options": {
                "destination_port_range": {
                    "max": 56,
                    "min": 56
                },
                "source_port_range": {
                    "max": 56,
                    "min": 56
                }
            },
            "udp_options": {
                "destination_port_range": {
                    "max": 56,
                    "min": 56
                },
                "source_port_range": {
                    "max": 56,
                    "min": 56
                }
            }
        }]
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateCaptureFilterDetails
    from oci.core.models import UpdateCaptureFilterDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CaptureFilterHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(CaptureFilterHelperGen, self).get_possible_entity_types() + [
            "capturefilter",
            "capturefilters",
            "corecapturefilter",
            "corecapturefilters",
            "capturefilterresource",
            "capturefiltersresource",
            "core",
        ]

    def get_module_resource_id_param(self):
        return "capture_filter_id"

    def get_module_resource_id(self):
        return self.module.params.get("capture_filter_id")

    def get_get_fn(self):
        return self.client.get_capture_filter

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_capture_filter,
            capture_filter_id=self.module.params.get("capture_filter_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
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
            self.client.list_capture_filters, **kwargs
        )

    def get_create_model_class(self):
        return CreateCaptureFilterDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_capture_filter,
            call_fn_args=(),
            call_fn_kwargs=dict(create_capture_filter_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateCaptureFilterDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_capture_filter,
            call_fn_args=(),
            call_fn_kwargs=dict(
                capture_filter_id=self.module.params.get("capture_filter_id"),
                update_capture_filter_details=update_details,
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
            call_fn=self.client.delete_capture_filter,
            call_fn_args=(),
            call_fn_kwargs=dict(
                capture_filter_id=self.module.params.get("capture_filter_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


CaptureFilterHelperCustom = get_custom_class("CaptureFilterHelperCustom")


class ResourceHelper(CaptureFilterHelperCustom, CaptureFilterHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            filter_type=dict(type="str", choices=["VTAP"]),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            vtap_capture_filter_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    traffic_direction=dict(
                        type="str", required=True, choices=["INGRESS", "EGRESS"]
                    ),
                    rule_action=dict(type="str", choices=["INCLUDE", "EXCLUDE"]),
                    source_cidr=dict(type="str"),
                    destination_cidr=dict(type="str"),
                    protocol=dict(type="str"),
                    icmp_options=dict(
                        type="dict",
                        options=dict(
                            code=dict(type="int"), type=dict(type="int", required=True)
                        ),
                    ),
                    tcp_options=dict(
                        type="dict",
                        options=dict(
                            destination_port_range=dict(
                                type="dict",
                                options=dict(
                                    max=dict(type="int", required=True),
                                    min=dict(type="int", required=True),
                                ),
                            ),
                            source_port_range=dict(
                                type="dict",
                                options=dict(
                                    max=dict(type="int", required=True),
                                    min=dict(type="int", required=True),
                                ),
                            ),
                        ),
                    ),
                    udp_options=dict(
                        type="dict",
                        options=dict(
                            destination_port_range=dict(
                                type="dict",
                                options=dict(
                                    max=dict(type="int", required=True),
                                    min=dict(type="int", required=True),
                                ),
                            ),
                            source_port_range=dict(
                                type="dict",
                                options=dict(
                                    max=dict(type="int", required=True),
                                    min=dict(type="int", required=True),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            capture_filter_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="capture_filter",
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
