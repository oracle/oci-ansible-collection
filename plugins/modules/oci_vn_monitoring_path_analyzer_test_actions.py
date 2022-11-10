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
module: oci_vn_monitoring_path_analyzer_test_actions
short_description: Perform actions on a PathAnalyzerTest resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a PathAnalyzerTest resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a `PathAnalyzerTest` resource from one compartment to another based on the identifier.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    path_analyzer_test_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the `PathAnalyzerTest` resource.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the `PathAnalyzerTest` resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the PathAnalyzerTest.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on path_analyzer_test
  oci_vn_monitoring_path_analyzer_test_actions:
    # required
    path_analyzer_test_id: "ocid1.pathanalyzertest.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
path_analyzer_test:
    description:
        - Details of the PathAnalyzerTest resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - A unique identifier established when the resource is created. The identifier can't be changed later.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the `PathAnalyzerTest` resource's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        protocol:
            description:
                - The IP protocol to use for the `PathAnalyzerTest` resource.
            returned: on success
            type: int
            sample: 56
        source_endpoint:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                instance_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compute instance.
                    returned: on success
                    type: str
                    sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
                load_balancer_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer.
                    returned: on success
                    type: str
                    sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                listener_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer listener.
                    returned: on success
                    type: str
                    sample: "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx"
                network_load_balancer_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer.
                    returned: on success
                    type: str
                    sample: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                subnet_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet containing the IP address.
                          This can be used to disambiguate which subnet is intended, in case the IP address
                          is used in more than one subnet (when there are subnets with overlapping IP ranges).
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                vlan_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN containing the IP address.
                          This can be used to disambiguate which VLAN is queried, in case the endpoint IP
                          address belongs to more than one VLAN (when there are VLANs with overlapping IP ranges).
                    returned: on success
                    type: str
                    sample: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
                type:
                    description:
                        - The type of the `Endpoint`.
                    returned: on success
                    type: str
                    sample: IP_ADDRESS
                address:
                    description:
                        - The IPv4 address of the COMPUTE_INSTANCE-type `Endpoint` object.
                    returned: on success
                    type: str
                    sample: address_example
                vnic_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VNIC attached to the compute instance.
                    returned: on success
                    type: str
                    sample: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
        destination_endpoint:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                instance_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compute instance.
                    returned: on success
                    type: str
                    sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
                load_balancer_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer.
                    returned: on success
                    type: str
                    sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                listener_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer listener.
                    returned: on success
                    type: str
                    sample: "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx"
                network_load_balancer_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer.
                    returned: on success
                    type: str
                    sample: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                subnet_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet containing the IP address.
                          This can be used to disambiguate which subnet is intended, in case the IP address
                          is used in more than one subnet (when there are subnets with overlapping IP ranges).
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                vlan_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN containing the IP address.
                          This can be used to disambiguate which VLAN is queried, in case the endpoint IP
                          address belongs to more than one VLAN (when there are VLANs with overlapping IP ranges).
                    returned: on success
                    type: str
                    sample: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
                type:
                    description:
                        - The type of the `Endpoint`.
                    returned: on success
                    type: str
                    sample: IP_ADDRESS
                address:
                    description:
                        - The IPv4 address of the COMPUTE_INSTANCE-type `Endpoint` object.
                    returned: on success
                    type: str
                    sample: address_example
                vnic_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VNIC attached to the compute instance.
                    returned: on success
                    type: str
                    sample: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
        protocol_parameters:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                icmp_code:
                    description:
                        - The L(ICMP,https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml) code.
                    returned: on success
                    type: int
                    sample: 56
                icmp_type:
                    description:
                        - The L(ICMP,https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml) type.
                    returned: on success
                    type: int
                    sample: 56
                type:
                    description:
                        - The type of the `ProtocolParameters` object.
                    returned: on success
                    type: str
                    sample: TCP
                source_port:
                    description:
                        - The source port to use in a `PathAnalyzerTest` resource.
                    returned: on success
                    type: int
                    sample: 56
                destination_port:
                    description:
                        - The destination port to use in a `PathAnalyzerTest` resource.
                    returned: on success
                    type: int
                    sample: 56
        query_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_bi_directional_analysis:
                    description:
                        - If true, a path analysis is done for both the forward and reverse routes.
                    returned: on success
                    type: bool
                    sample: true
        time_created:
            description:
                - The date and time the `PathAnalyzerTest` resource was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the `PathAnalyzerTest` resource was last updated, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the `PathAnalyzerTest` resource.
            returned: on success
            type: str
            sample: ACTIVE
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
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
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "protocol": 56,
        "source_endpoint": {
            "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
            "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
            "listener_id": "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx",
            "network_load_balancer_id": "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "vlan_id": "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx",
            "type": "IP_ADDRESS",
            "address": "address_example",
            "vnic_id": "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "destination_endpoint": {
            "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
            "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
            "listener_id": "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx",
            "network_load_balancer_id": "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "vlan_id": "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx",
            "type": "IP_ADDRESS",
            "address": "address_example",
            "vnic_id": "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "protocol_parameters": {
            "icmp_code": 56,
            "icmp_type": 56,
            "type": "TCP",
            "source_port": 56,
            "destination_port": 56
        },
        "query_options": {
            "is_bi_directional_analysis": true
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
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
    from oci.vn_monitoring import VnMonitoringClient
    from oci.vn_monitoring.models import ChangePathAnalyzerTestCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PathAnalyzerTestActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "path_analyzer_test_id"

    def get_module_resource_id(self):
        return self.module.params.get("path_analyzer_test_id")

    def get_get_fn(self):
        return self.client.get_path_analyzer_test

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_path_analyzer_test,
            path_analyzer_test_id=self.module.params.get("path_analyzer_test_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangePathAnalyzerTestCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_path_analyzer_test_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                path_analyzer_test_id=self.module.params.get("path_analyzer_test_id"),
                change_path_analyzer_test_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


PathAnalyzerTestActionsHelperCustom = get_custom_class(
    "PathAnalyzerTestActionsHelperCustom"
)


class ResourceHelper(
    PathAnalyzerTestActionsHelperCustom, PathAnalyzerTestActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            path_analyzer_test_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="path_analyzer_test",
        service_client_class=VnMonitoringClient,
        namespace="vn_monitoring",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
