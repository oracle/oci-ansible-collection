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
module: oci_data_connectivity_endpoint
short_description: Manage an Endpoint resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an Endpoint resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Data Connectivity Management endpoint ready to perform data connectivity.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_connectivity_endpoint_actions) module: change_compartment,
      validate_data_asset_network_reachablity."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    vcn_id:
        description:
            - VCN identifier where the subnet resides.
        type: str
    subnet_id:
        description:
            - Subnet identifier for the customer-connected databases.
        type: str
    dns_zones:
        description:
            - "The list of DNS zones to be used by the data assets to be harvested.
              Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com"
        type: list
        elements: str
    compartment_id:
        description:
            - Compartment Identifier
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type, or scope. Exists only for cross-compatibility.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    description:
        description:
            - Data Connectivity Management Registry description
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - The Data Connectivity Management registry display name; registries can be renamed.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    endpoint_size:
        description:
            - Endpoint size for reverse connection capacity.
            - This parameter is updatable.
        type: int
    nsg_ids:
        description:
            - The list of NSGs to which the private endpoint VNIC must be added.
            - This parameter is updatable.
        type: list
        elements: str
    endpoint_id:
        description:
            - DCMS endpoint ID.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    registry_id:
        description:
            - DCMS registry ID
            - This parameter is updatable.
        type: str
    is_force_operation:
        description:
            - Try to delete forcefully after drain timeout.
        type: bool
    state:
        description:
            - The state of the Endpoint.
            - Use I(state=present) to create or update an Endpoint.
            - Use I(state=absent) to delete an Endpoint.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create endpoint
  oci_data_connectivity_endpoint:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    dns_zones: [ "dns_zones_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    description: description_example
    endpoint_size: 56
    nsg_ids: [ "nsg_ids_example" ]
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update endpoint
  oci_data_connectivity_endpoint:
    # required
    endpoint_id: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    description: description_example
    display_name: display_name_example
    endpoint_size: 56
    nsg_ids: [ "nsg_ids_example" ]
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update endpoint using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_connectivity_endpoint:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    description: description_example
    endpoint_size: 56
    nsg_ids: [ "nsg_ids_example" ]
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete endpoint
  oci_data_connectivity_endpoint:
    # required
    endpoint_id: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    is_force_operation: true

- name: Delete endpoint using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_connectivity_endpoint:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
endpoint:
    description:
        - Details of the Endpoint resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        vcn_id:
            description:
                - VCN OCID where the subnet resides.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - Subnet OCID of the customer connected network where, for example, the databases reside.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        dns_zones:
            description:
                - "List of DNS zones to be used by the data assets to be harvested.
                  Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com"
            returned: on success
            type: list
            sample: []
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
        id:
            description:
                - A unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        endpoint_size:
            description:
                - Endpoint size for reverse connection capacity.
            returned: on success
            type: int
            sample: 56
        nsg_ids:
            description:
                - The list of NSGs to which the private endpoint VNIC must be added.
            returned: on success
            type: list
            sample: []
    sample: {
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "dns_zones": [],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "description": "description_example",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "state_message": "state_message_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "endpoint_size": 56,
        "nsg_ids": []
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
    from oci.data_connectivity import DataConnectivityManagementClient
    from oci.data_connectivity.models import CreateEndpointDetails
    from oci.data_connectivity.models import UpdateEndpointDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EndpointHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(EndpointHelperGen, self).get_possible_entity_types() + [
            "endpoint",
            "endpoints",
            "dataConnectivityendpoint",
            "dataConnectivityendpoints",
            "endpointresource",
            "endpointsresource",
            "dataconnectivity",
        ]

    def get_module_resource_id_param(self):
        return "endpoint_id"

    def get_module_resource_id(self):
        return self.module.params.get("endpoint_id")

    def get_get_fn(self):
        return self.client.get_endpoint

    def get_resource(self):
        optional_params = [
            "registry_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_endpoint,
            endpoint_id=self.module.params.get("endpoint_id"),
            **optional_kwargs
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["registry_id"]

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
        return oci_common_utils.list_all_resources(self.client.list_endpoints, **kwargs)

    def get_create_model_class(self):
        return CreateEndpointDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_endpoint_details=create_details,
                registry_id=self.module.params.get("registry_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateEndpointDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                endpoint_id=self.module.params.get("endpoint_id"),
                update_endpoint_details=update_details,
                registry_id=self.module.params.get("registry_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                endpoint_id=self.module.params.get("endpoint_id"),
                registry_id=self.module.params.get("registry_id"),
                is_force_operation=self.module.params.get("is_force_operation"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


EndpointHelperCustom = get_custom_class("EndpointHelperCustom")


class ResourceHelper(EndpointHelperCustom, EndpointHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            vcn_id=dict(type="str"),
            subnet_id=dict(type="str"),
            dns_zones=dict(type="list", elements="str"),
            compartment_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            endpoint_size=dict(type="int"),
            nsg_ids=dict(type="list", elements="str"),
            endpoint_id=dict(aliases=["id"], type="str"),
            registry_id=dict(type="str"),
            is_force_operation=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="endpoint",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
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
