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
module: oci_opsi_operations_insights_private_endpoint
short_description: Manage an OperationsInsightsPrivateEndpoint resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an OperationsInsightsPrivateEndpoint resource in Oracle Cloud Infrastructure
    - For I(state=present), create a private endpoint resource for the tenant in Operations Insights.
      This resource will be created in customer compartment.
    - "This resource has the following action operations in the M(oracle.oci.oci_opsi_operations_insights_private_endpoint_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Private service accessed database.
            - Required for create using I(state=present).
        type: str
    vcn_id:
        description:
            - The VCN L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Private service accessed database.
            - Required for create using I(state=present).
        type: str
    subnet_id:
        description:
            - The Subnet L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Private service accessed database.
            - Required for create using I(state=present).
        type: str
    is_used_for_rac_dbs:
        description:
            - The flag to identify if private endpoint is used for rac database or not
            - Required for create using I(state=present).
        type: bool
    display_name:
        description:
            - The display name for the private endpoint. It is changeable.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - The description of the private endpoint.
            - This parameter is updatable.
        type: str
    nsg_ids:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network security groups that the private endpoint
              belongs to.
            - This parameter is updatable.
        type: list
        elements: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    operations_insights_private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Operation Insights private endpoint.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the OperationsInsightsPrivateEndpoint.
            - Use I(state=present) to create or update an OperationsInsightsPrivateEndpoint.
            - Use I(state=absent) to delete an OperationsInsightsPrivateEndpoint.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create operations_insights_private_endpoint
  oci_opsi_operations_insights_private_endpoint:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    is_used_for_rac_dbs: true
    display_name: display_name_example

    # optional
    description: description_example
    nsg_ids: [ "nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update operations_insights_private_endpoint
  oci_opsi_operations_insights_private_endpoint:
    # required
    operations_insights_private_endpoint_id: "ocid1.operationsinsightsprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    nsg_ids: [ "nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update operations_insights_private_endpoint using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_opsi_operations_insights_private_endpoint:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    nsg_ids: [ "nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete operations_insights_private_endpoint
  oci_opsi_operations_insights_private_endpoint:
    # required
    operations_insights_private_endpoint_id: "ocid1.operationsinsightsprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete operations_insights_private_endpoint using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_opsi_operations_insights_private_endpoint:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
operations_insights_private_endpoint:
    description:
        - Details of the OperationsInsightsPrivateEndpoint resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the Private service accessed database.
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
                - The compartment OCID of the Private service accessed database.
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
        private_ip:
            description:
                - The private IP addresses assigned to the private endpoint. All IP addresses will be concatenated if it is RAC DBs.
            returned: on success
            type: str
            sample: private_ip_example
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
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        private_endpoint_status_details:
            description:
                - A message describing the status of the private endpoint connection of this resource. For example, it can be used to provide actionable
                  information about the validity of the private endpoint connection.
            returned: on success
            type: str
            sample: private_endpoint_status_details_example
        is_used_for_rac_dbs:
            description:
                - The flag is to identify if private endpoint is used for rac database or not
            returned: on success
            type: bool
            sample: true
        nsg_ids:
            description:
                - The OCIDs of the network security groups that the private endpoint belongs to.
            returned: on success
            type: list
            sample: []
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
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
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
        "private_ip": "private_ip_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "private_endpoint_status_details": "private_endpoint_status_details_example",
        "is_used_for_rac_dbs": true,
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
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import CreateOperationsInsightsPrivateEndpointDetails
    from oci.opsi.models import UpdateOperationsInsightsPrivateEndpointDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OperationsInsightsPrivateEndpointHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            OperationsInsightsPrivateEndpointHelperGen, self
        ).get_possible_entity_types() + [
            "operationsinsightsprivateendpoint",
            "operationsinsightsprivateendpoints",
            "opsioperationsinsightsprivateendpoint",
            "opsioperationsinsightsprivateendpoints",
            "operationsinsightsprivateendpointresource",
            "operationsinsightsprivateendpointsresource",
            "opsi",
        ]

    def get_module_resource_id_param(self):
        return "operations_insights_private_endpoint_id"

    def get_module_resource_id(self):
        return self.module.params.get("operations_insights_private_endpoint_id")

    def get_get_fn(self):
        return self.client.get_operations_insights_private_endpoint

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_operations_insights_private_endpoint,
            operations_insights_private_endpoint_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_operations_insights_private_endpoint,
            operations_insights_private_endpoint_id=self.module.params.get(
                "operations_insights_private_endpoint_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "is_used_for_rac_dbs",
            "vcn_id",
        ]

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
            self.client.list_operations_insights_private_endpoints, **kwargs
        )

    def get_create_model_class(self):
        return CreateOperationsInsightsPrivateEndpointDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_operations_insights_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_operations_insights_private_endpoint_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateOperationsInsightsPrivateEndpointDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_operations_insights_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                operations_insights_private_endpoint_id=self.module.params.get(
                    "operations_insights_private_endpoint_id"
                ),
                update_operations_insights_private_endpoint_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_operations_insights_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                operations_insights_private_endpoint_id=self.module.params.get(
                    "operations_insights_private_endpoint_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OperationsInsightsPrivateEndpointHelperCustom = get_custom_class(
    "OperationsInsightsPrivateEndpointHelperCustom"
)


class ResourceHelper(
    OperationsInsightsPrivateEndpointHelperCustom,
    OperationsInsightsPrivateEndpointHelperGen,
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
            is_used_for_rac_dbs=dict(type="bool"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            nsg_ids=dict(type="list", elements="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            operations_insights_private_endpoint_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="operations_insights_private_endpoint",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
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
