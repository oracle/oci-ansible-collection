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
module: oci_vn_monitoring_path_analyzer_test_facts
short_description: Fetches details about one or multiple PathAnalyzerTest resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PathAnalyzerTest resources in Oracle Cloud Infrastructure
    - Returns a list of all `PathAnalyzerTests` in a compartment.
    - If I(path_analyzer_test_id) is specified, the details of a single PathAnalyzerTest will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    path_analyzer_test_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the `PathAnalyzerTest` resource.
            - Required to get a specific path_analyzer_test.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple path_analyzer_tests.
        type: str
    lifecycle_state:
        description:
            - A filter that returns only resources whose `lifecycleState` matches the given `lifecycleState`.
        type: str
        choices:
            - "ACTIVE"
            - "DELETED"
    display_name:
        description:
            - A filter that returns only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific path_analyzer_test
  oci_vn_monitoring_path_analyzer_test_facts:
    # required
    path_analyzer_test_id: "ocid1.pathanalyzertest.oc1..xxxxxxEXAMPLExxxxxx"

- name: List path_analyzer_tests
  oci_vn_monitoring_path_analyzer_test_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: ACTIVE
    display_name: display_name_example
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
path_analyzer_tests:
    description:
        - List of PathAnalyzerTest resources
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
    sample: [{
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
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.vn_monitoring import VnMonitoringClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PathAnalyzerTestFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "path_analyzer_test_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_path_analyzer_test,
            path_analyzer_test_id=self.module.params.get("path_analyzer_test_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_path_analyzer_tests,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


PathAnalyzerTestFactsHelperCustom = get_custom_class(
    "PathAnalyzerTestFactsHelperCustom"
)


class ResourceFactsHelper(
    PathAnalyzerTestFactsHelperCustom, PathAnalyzerTestFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            path_analyzer_test_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED"]),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="path_analyzer_test",
        service_client_class=VnMonitoringClient,
        namespace="vn_monitoring",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(path_analyzer_tests=result)


if __name__ == "__main__":
    main()
