#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_data_safe_private_endpoint_facts
short_description: Fetches details about one or multiple DataSafePrivateEndpoint resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DataSafePrivateEndpoint resources in Oracle Cloud Infrastructure
    - Gets a list of Data Safe private endpoints.
    - If I(data_safe_private_endpoint_id) is specified, the details of a single DataSafePrivateEndpoint will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    data_safe_private_endpoint_id:
        description:
            - The OCID of the private endpoint.
            - Required to get a specific data_safe_private_endpoint.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - A filter to return only resources that match the specified compartment OCID.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the specified display name.
        type: str
        aliases: ["name"]
    vcn_id:
        description:
            - A filter to return only the private endpoints that match the specified VCN OCID.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources that match the specified lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "NA"
    sort_order:
        description:
            - The sort order to use, either ascending (ASC) or descending (DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can specify only one sort order (sortOrder). The default order for TIMECREATED is descending. The default order for
              DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List data_safe_private_endpoints
  oci_data_safe_private_endpoint_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific data_safe_private_endpoint
  oci_data_safe_private_endpoint_facts:
    data_safe_private_endpoint_id: ocid1.datasafeprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
data_safe_private_endpoints:
    description:
        - List of DataSafePrivateEndpoint resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the Data Safe private endpoint.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The display name of the private endpoint.
            returned: on success
            type: string
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        vcn_id:
            description:
                - The OCID of the VCN.
            returned: on success
            type: string
            sample: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
        subnet_id:
            description:
                - The OCID of the subnet.
            returned: on success
            type: string
            sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
        private_endpoint_id:
            description:
                - The OCID of the underlying private endpoint.
            returned: on success
            type: string
            sample: ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx
        private_endpoint_ip:
            description:
                - The private IP address of the private endpoint.
            returned: on success
            type: string
            sample: private_endpoint_ip_example
        endpoint_fqdn:
            description:
                - The three-label fully qualified domain name (FQDN) of the private endpoint. The customer VCN's DNS records are updated with this FQDN.
            returned: on success
            type: string
            sample: endpoint_fqdn_example
        description:
            description:
                - The description of the private endpoint.
            returned: on success
            type: string
            sample: description_example
        time_created:
            description:
                - The date and time the private endpoint was created, in the format defined by RFC3339.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the private endpoint.
            returned: on success
            type: string
            sample: CREATING
        nsg_ids:
            description:
                - The OCIDs of the network security groups that the private endpoint belongs to.
            returned: on success
            type: list
            sample: []
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "private_endpoint_id": "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx",
        "private_endpoint_ip": "private_endpoint_ip_example",
        "endpoint_fqdn": "endpoint_fqdn_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "nsg_ids": [],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_safe import DataSafeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafePrivateEndpointFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "data_safe_private_endpoint_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_safe_private_endpoint,
            data_safe_private_endpoint_id=self.module.params.get(
                "data_safe_private_endpoint_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "vcn_id",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_data_safe_private_endpoints, **optional_kwargs
        )


DataSafePrivateEndpointFactsHelperCustom = get_custom_class(
    "DataSafePrivateEndpointFactsHelperCustom"
)


class ResourceFactsHelper(
    DataSafePrivateEndpointFactsHelperCustom, DataSafePrivateEndpointFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            data_safe_private_endpoint_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            vcn_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "NA",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="data_safe_private_endpoint",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(data_safe_private_endpoints=result)


if __name__ == "__main__":
    main()
