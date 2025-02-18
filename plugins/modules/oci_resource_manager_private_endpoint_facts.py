#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_resource_manager_private_endpoint_facts
short_description: Fetches details about one or multiple PrivateEndpoint resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PrivateEndpoint resources in Oracle Cloud Infrastructure
    - "Lists private endpoints according to the specified filter.
      - For `compartmentId`, lists all private endpoints in the matching compartment.
      - For `privateEndpointId`, lists the matching private endpoint."
    - If I(private_endpoint_id) is specified, the details of a single PrivateEndpoint will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - A filter to return only resources that exist in the compartment, identified by
              L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: str
    private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the private endpoint.
            - Required to get a specific private_endpoint.
        type: str
        aliases: ["id"]
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
              Use this filter to list a resource by name.
              Requires `sortBy` set to `DISPLAYNAME`.
              Alternatively, when you know the resource OCID, use the related Get operation.
        type: str
        aliases: ["name"]
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
        type: str
    sort_by:
        description:
            - The field to use when sorting returned resources.
              By default, `TIMECREATED` is ordered descending.
              By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific private_endpoint
  oci_resource_manager_private_endpoint_facts:
    # required
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

- name: List private_endpoints
  oci_resource_manager_private_endpoint_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
private_endpoints:
    description:
        - List of PrivateEndpoint resources
    returned: on success
    type: complex
    contains:
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet within the VCN for the private endpoint.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        source_ips:
            description:
                - The source IP addresses that Resource Manager uses to connect to your network. Automatically assigned by Resource Manager.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        nsg_id_list:
            description:
                - The L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of
                  L(network security groups (NSGs),https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)
                  for the private endpoint.
                  Order does not matter.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the private endpoint.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing this private endpoint.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the private endpoint. Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN for the private endpoint.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        is_used_with_configuration_source_provider:
            description:
                - When `true`, allows the private endpoint to be used with a configuration source provider.
            returned: on success
            type: bool
            sample: true
        dns_zones:
            description:
                - "DNS zones to use for accessing private Git servers.
                  For private Git server instructions, see
                  L(Private Git Server,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#private-git).
                  Specify DNS fully qualified domain names (FQDNs); DNS Proxy forwards related DNS FQDN queries to the consumer DNS resolver.
                  For DNS FQDNs not specified, queries go to service provider VCN resolver.
                  Example: `abc.oraclevcn.com`"
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - "The date and time at which the private endpoint was created.
                  Format is defined by RFC3339.
                  Example: `2020-11-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the private endpoint.
            returned: on success
            type: str
            sample: ACTIVE
        freeform_tags:
            description:
                - "Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "source_ips": [],
        "nsg_id_list": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "is_used_with_configuration_source_provider": true,
        "dns_zones": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.resource_manager import ResourceManagerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PrivateEndpointFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "private_endpoint_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_endpoint,
            private_endpoint_id=self.module.params.get("private_endpoint_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "private_endpoint_id",
            "display_name",
            "vcn_id",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_private_endpoints, **optional_kwargs
        )


PrivateEndpointFactsHelperCustom = get_custom_class("PrivateEndpointFactsHelperCustom")


class ResourceFactsHelper(
    PrivateEndpointFactsHelperCustom, PrivateEndpointFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            private_endpoint_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            vcn_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="private_endpoint",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(private_endpoints=result)


if __name__ == "__main__":
    main()
