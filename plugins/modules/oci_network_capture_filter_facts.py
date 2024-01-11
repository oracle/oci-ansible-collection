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
module: oci_network_capture_filter_facts
short_description: Fetches details about one or multiple CaptureFilter resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CaptureFilter resources in Oracle Cloud Infrastructure
    - Lists the capture filters in the specified compartment.
    - If I(capture_filter_id) is specified, the details of a single CaptureFilter will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    capture_filter_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the capture filter.
            - Required to get a specific capture_filter.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple capture_filters.
        type: str
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
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only resources that match the given capture filter lifecycle state.
              The state value is case-insensitive.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "UPDATING"
            - "TERMINATING"
            - "TERMINATED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific capture_filter
  oci_network_capture_filter_facts:
    # required
    capture_filter_id: "ocid1.capturefilter.oc1..xxxxxxEXAMPLExxxxxx"

- name: List capture_filters
  oci_network_capture_filter_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: TIMECREATED
    sort_order: ASC
    display_name: display_name_example
    lifecycle_state: PROVISIONING

"""

RETURN = """
capture_filters:
    description:
        - List of CaptureFilter resources
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
    sample: [{
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
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CaptureFilterFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "capture_filter_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_capture_filter,
            capture_filter_id=self.module.params.get("capture_filter_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "display_name",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_capture_filters,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


CaptureFilterFactsHelperCustom = get_custom_class("CaptureFilterFactsHelperCustom")


class ResourceFactsHelper(CaptureFilterFactsHelperCustom, CaptureFilterFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            capture_filter_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "AVAILABLE",
                    "UPDATING",
                    "TERMINATING",
                    "TERMINATED",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="capture_filter",
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

    module.exit_json(capture_filters=result)


if __name__ == "__main__":
    main()
