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
module: oci_data_connectivity_endpoint_facts
short_description: Fetches details about one or multiple Endpoint resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Endpoint resources in Oracle Cloud Infrastructure
    - Returns a list of Data Connectivity Management endpoints.
    - If I(endpoint_id) is specified, the details of a single Endpoint will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    endpoint_id:
        description:
            - DCMS endpoint ID.
            - Required to get a specific endpoint.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment containing the resources you want to list.
            - Required to list multiple endpoints.
        type: str
    registry_id:
        description:
            - DCMS registry ID
        type: str
    name:
        description:
            - Used to filter by the name of the object.
        type: str
    lifecycle_state:
        description:
            - Lifecycle state of the resource.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "STARTING"
            - "STOPPING"
            - "STOPPED"
    sort_order:
        description:
            - Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - This parameter allows users to specify a sort field. Default sort order is the descending order of `timeCreated` (most recently created objects at
              the top). Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in
              descending order).
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
            - "TIMEUPDATED"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific endpoint
  oci_data_connectivity_endpoint_facts:
    # required
    endpoint_id: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"

- name: List endpoints
  oci_data_connectivity_endpoint_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
endpoints:
    description:
        - List of Endpoint resources
    returned: on success
    type: complex
    contains:
        vcn_id:
            description:
                - VCN OCID where the subnet resides.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - Subnet OCID of the customer connected network where, for example, the databases reside.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        dns_zones:
            description:
                - "List of DNS zones to be used by the data assets to be harvested.
                  Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com"
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        endpoint_size:
            description:
                - Endpoint size for reverse connection capacity.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        nsg_ids:
            description:
                - The list of NSGs to which the private endpoint VNIC must be added.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        id:
            description:
                - A unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Registry description
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - The Data Connectivity Management Registry display name; registries can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Time when the Data Connectivity Management registry was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time when the Data Connectivity Management registry was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type, or scope. Exists only for cross-compatibility.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        lifecycle_state:
            description:
                - "Lifecycle states for registries in the Data Connectivity Management Service.
                  CREATING - The resource is being created and may not be usable until the entire metadata is defined.
                  UPDATING - The resource is being updated and may not be usable until all changes are commited.
                  DELETING - The resource is being deleted and might require deep cleanup of children.
                  ACTIVE   - The resource is valid and available for access.
                  INACTIVE - The resource might be incomplete in its definition or might have been made unavailable for
                           administrative reasons.
                  DELETED  - The resource has been deleted and isn't available.
                  FAILED   - The resource is in a failed state due to validation or other errors."
            returned: on success
            type: str
            sample: CREATING
        state_message:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: state_message_example
    sample: [{
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "dns_zones": [],
        "endpoint_size": 56,
        "nsg_ids": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "lifecycle_state": "CREATING",
        "state_message": "state_message_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_connectivity import DataConnectivityManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EndpointFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "endpoint_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "registry_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_endpoint,
            endpoint_id=self.module.params.get("endpoint_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "registry_id",
            "name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_endpoints,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


EndpointFactsHelperCustom = get_custom_class("EndpointFactsHelperCustom")


class ResourceFactsHelper(EndpointFactsHelperCustom, EndpointFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            endpoint_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            registry_id=dict(type="str"),
            name=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "STARTING",
                    "STOPPING",
                    "STOPPED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str", choices=["TIMECREATED", "DISPLAYNAME", "TIMEUPDATED"]
            ),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="endpoint",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(endpoints=result)


if __name__ == "__main__":
    main()
