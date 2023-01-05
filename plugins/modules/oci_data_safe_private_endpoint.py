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
module: oci_data_safe_private_endpoint
short_description: Manage a DataSafePrivateEndpoint resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DataSafePrivateEndpoint resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Data Safe private endpoint.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_safe_private_endpoint_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    vcn_id:
        description:
            - The OCID of the VCN.
            - Required for create using I(state=present).
        type: str
    subnet_id:
        description:
            - The OCID of the subnet.
            - Required for create using I(state=present).
        type: str
    private_endpoint_ip:
        description:
            - The private IP address of the private endpoint.
        type: str
    display_name:
        description:
            - The display name for the private endpoint. The name does not have to be unique, and it's changeable.
            - Required for create using I(state=present), update using I(state=present) with data_safe_private_endpoint_id present.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    description:
        description:
            - The description of the private endpoint.
            - This parameter is updatable.
        type: str
    nsg_ids:
        description:
            - The OCIDs of the network security groups that the private endpoint belongs to.
            - This parameter is updatable.
        type: list
        elements: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
              L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    data_safe_private_endpoint_id:
        description:
            - The OCID of the private endpoint.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DataSafePrivateEndpoint.
            - Use I(state=present) to create or update a DataSafePrivateEndpoint.
            - Use I(state=absent) to delete a DataSafePrivateEndpoint.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create data_safe_private_endpoint
  oci_data_safe_private_endpoint:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    private_endpoint_ip: private_endpoint_ip_example
    description: description_example
    nsg_ids: [ "nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update data_safe_private_endpoint
  oci_data_safe_private_endpoint:
    # required
    display_name: display_name_example
    data_safe_private_endpoint_id: "ocid1.datasafeprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    nsg_ids: [ "nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update data_safe_private_endpoint using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_safe_private_endpoint:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    nsg_ids: [ "nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete data_safe_private_endpoint
  oci_data_safe_private_endpoint:
    # required
    data_safe_private_endpoint_id: "ocid1.datasafeprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete data_safe_private_endpoint using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_safe_private_endpoint:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
data_safe_private_endpoint:
    description:
        - Details of the DataSafePrivateEndpoint resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the Data Safe private endpoint.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the private endpoint.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        vcn_id:
            description:
                - The OCID of the VCN.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The OCID of the subnet.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        private_endpoint_id:
            description:
                - The OCID of the underlying private endpoint.
            returned: on success
            type: str
            sample: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        private_endpoint_ip:
            description:
                - The private IP address of the private endpoint.
            returned: on success
            type: str
            sample: private_endpoint_ip_example
        endpoint_fqdn:
            description:
                - The three-label fully qualified domain name (FQDN) of the private endpoint. The customer VCN's DNS records are updated with this FQDN.
            returned: on success
            type: str
            sample: endpoint_fqdn_example
        description:
            description:
                - The description of the private endpoint.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The date and time the private endpoint was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the private endpoint.
            returned: on success
            type: str
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
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
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
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.data_safe import DataSafeClient
    from oci.data_safe.models import CreateDataSafePrivateEndpointDetails
    from oci.data_safe.models import UpdateDataSafePrivateEndpointDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafePrivateEndpointHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            DataSafePrivateEndpointHelperGen, self
        ).get_possible_entity_types() + [
            "datasafeprivateendpoint",
            "datasafeprivateendpoints",
            "dataSafedatasafeprivateendpoint",
            "dataSafedatasafeprivateendpoints",
            "datasafeprivateendpointresource",
            "datasafeprivateendpointsresource",
            "datasafe",
        ]

    def get_module_resource_id_param(self):
        return "data_safe_private_endpoint_id"

    def get_module_resource_id(self):
        return self.module.params.get("data_safe_private_endpoint_id")

    def get_get_fn(self):
        return self.client.get_data_safe_private_endpoint

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_safe_private_endpoint,
            data_safe_private_endpoint_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_safe_private_endpoint,
            data_safe_private_endpoint_id=self.module.params.get(
                "data_safe_private_endpoint_id"
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
        optional_list_method_params = ["display_name", "vcn_id"]

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
            self.client.list_data_safe_private_endpoints, **kwargs
        )

    def get_create_model_class(self):
        return CreateDataSafePrivateEndpointDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_data_safe_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_data_safe_private_endpoint_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDataSafePrivateEndpointDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_data_safe_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                data_safe_private_endpoint_id=self.module.params.get(
                    "data_safe_private_endpoint_id"
                ),
                update_data_safe_private_endpoint_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_data_safe_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                data_safe_private_endpoint_id=self.module.params.get(
                    "data_safe_private_endpoint_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataSafePrivateEndpointHelperCustom = get_custom_class(
    "DataSafePrivateEndpointHelperCustom"
)


class ResourceHelper(
    DataSafePrivateEndpointHelperCustom, DataSafePrivateEndpointHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            vcn_id=dict(type="str"),
            subnet_id=dict(type="str"),
            private_endpoint_ip=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            nsg_ids=dict(type="list", elements="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            data_safe_private_endpoint_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="data_safe_private_endpoint",
        service_client_class=DataSafeClient,
        namespace="data_safe",
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
