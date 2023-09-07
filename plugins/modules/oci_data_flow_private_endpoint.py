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
module: oci_data_flow_private_endpoint
short_description: Manage a PrivateEndpoint resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a PrivateEndpoint resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a private endpoint to be used by applications.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_flow_private_endpoint_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of a compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    subnet_id:
        description:
            - The OCID of a subnet.
            - Required for create using I(state=present).
        type: str
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    description:
        description:
            - A user-friendly description. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - A user-friendly name. It does not have to be unique. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    dns_zones:
        description:
            - "An array of DNS zone names.
              Example: `[ \\"app.examplecorp.com\\", \\"app.examplecorp2.com\\" ]`"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    max_host_count:
        description:
            - The maximum number of hosts to be accessed through the private endpoint. This value is used
              to calculate the relevant CIDR block and should be a multiple of 256.  If the value is not a
              multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up
              to 512.
            - This parameter is updatable.
        type: int
    nsg_ids:
        description:
            - An array of network security group OCIDs.
            - This parameter is updatable.
        type: list
        elements: str
    scan_details:
        description:
            - "An array of fqdn/port pairs used to create private endpoint. Each object is a simple key-value pair with FQDN as key and port number as value.
              [ { fqdn: \\"scan1.oracle.com\\", port: \\"1521\\"}, { fqdn: \\"scan2.oracle.com\\", port: \\"1521\\" } ]"
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            fqdn:
                description:
                    - A fully-qualified domain name (FQDN).
                type: str
            port:
                description:
                    - The port number of the FQDN
                type: str
    private_endpoint_id:
        description:
            - The unique ID for a private endpoint.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the PrivateEndpoint.
            - Use I(state=present) to create or update a PrivateEndpoint.
            - Use I(state=absent) to delete a PrivateEndpoint.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create private_endpoint
  oci_data_flow_private_endpoint:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    dns_zones: [ "dns_zones_example" ]

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    max_host_count: 56
    nsg_ids: [ "nsg_ids_example" ]
    scan_details:
    - # optional
      fqdn: fqdn_example
      port: port_example

- name: Update private_endpoint
  oci_data_flow_private_endpoint:
    # required
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    description: description_example
    display_name: display_name_example
    dns_zones: [ "dns_zones_example" ]
    freeform_tags: {'Department': 'Finance'}
    max_host_count: 56
    nsg_ids: [ "nsg_ids_example" ]
    scan_details:
    - # optional
      fqdn: fqdn_example
      port: port_example

- name: Update private_endpoint using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_flow_private_endpoint:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    description: description_example
    dns_zones: [ "dns_zones_example" ]
    freeform_tags: {'Department': 'Finance'}
    max_host_count: 56
    nsg_ids: [ "nsg_ids_example" ]
    scan_details:
    - # optional
      fqdn: fqdn_example
      port: port_example

- name: Delete private_endpoint
  oci_data_flow_private_endpoint:
    # required
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete private_endpoint using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_flow_private_endpoint:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
private_endpoint:
    description:
        - Details of the PrivateEndpoint resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        description:
            description:
                - A user-friendly description. Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - A user-friendly name. It does not have to be unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        dns_zones:
            description:
                - "An array of DNS zone names.
                  Example: `[ \\"app.examplecorp.com\\", \\"app.examplecorp2.com\\" ]`"
            returned: on success
            type: list
            sample: []
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of a private endpoint.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_details:
            description:
                - The detailed messages about the lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of this private endpoint.
            returned: on success
            type: str
            sample: CREATING
        max_host_count:
            description:
                - The maximum number of hosts to be accessed through the private endpoint. This value is used
                  to calculate the relevant CIDR block and should be a multiple of 256.  If the value is not a
                  multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up
                  to 512.
            returned: on success
            type: int
            sample: 56
        nsg_ids:
            description:
                - An array of network security group OCIDs.
            returned: on success
            type: list
            sample: []
        owner_principal_id:
            description:
                - The OCID of the user who created the resource.
            returned: on success
            type: str
            sample: "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx"
        owner_user_name:
            description:
                - The username of the user who created the resource.  If the username of the owner does not exist,
                  `null` will be returned and the caller should refer to the ownerPrincipalId value instead.
            returned: on success
            type: str
            sample: owner_user_name_example
        scan_details:
            description:
                - "An array of fqdn/port pairs used to create private endpoint. Each object is a simple key-value pair with FQDN as key and port number as
                  value.
                  [ { fqdn: \\"scan1.oracle.com\\", port: \\"1521\\"}, { fqdn: \\"scan2.oracle.com\\", port: \\"1521\\" } ]"
            returned: on success
            type: complex
            contains:
                fqdn:
                    description:
                        - A fully-qualified domain name (FQDN).
                    returned: on success
                    type: str
                    sample: fqdn_example
                port:
                    description:
                        - The port number of the FQDN
                    returned: on success
                    type: str
                    sample: port_example
        subnet_id:
            description:
                - The OCID of a subnet.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The date and time the resource was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The date and time the resource was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "description": "description_example",
        "display_name": "display_name_example",
        "dns_zones": [],
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "CREATING",
        "max_host_count": 56,
        "nsg_ids": [],
        "owner_principal_id": "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx",
        "owner_user_name": "owner_user_name_example",
        "scan_details": [{
            "fqdn": "fqdn_example",
            "port": "port_example"
        }],
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
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
    from oci.data_flow import DataFlowClient
    from oci.data_flow.models import CreatePrivateEndpointDetails
    from oci.data_flow.models import UpdatePrivateEndpointDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowPrivateEndpointHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            DataFlowPrivateEndpointHelperGen, self
        ).get_possible_entity_types() + [
            "dataflowprivateendpoint",
            "dataflowprivateendpoints",
            "dataFlowdataflowprivateendpoint",
            "dataFlowdataflowprivateendpoints",
            "dataflowprivateendpointresource",
            "dataflowprivateendpointsresource",
            "privateendpoint",
            "privateendpoints",
            "dataFlowprivateendpoint",
            "dataFlowprivateendpoints",
            "privateendpointresource",
            "privateendpointsresource",
            "dataflow",
        ]

    def get_module_resource_id_param(self):
        return "private_endpoint_id"

    def get_module_resource_id(self):
        return self.module.params.get("private_endpoint_id")

    def get_get_fn(self):
        return self.client.get_private_endpoint

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_endpoint, private_endpoint_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_endpoint,
            private_endpoint_id=self.module.params.get("private_endpoint_id"),
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
            self.client.list_private_endpoints, **kwargs
        )

    def get_create_model_class(self):
        return CreatePrivateEndpointDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(create_private_endpoint_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdatePrivateEndpointDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_private_endpoint_details=update_details,
                private_endpoint_id=self.module.params.get("private_endpoint_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                private_endpoint_id=self.module.params.get("private_endpoint_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataFlowPrivateEndpointHelperCustom = get_custom_class(
    "DataFlowPrivateEndpointHelperCustom"
)


class ResourceHelper(
    DataFlowPrivateEndpointHelperCustom, DataFlowPrivateEndpointHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            subnet_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            dns_zones=dict(type="list", elements="str"),
            freeform_tags=dict(type="dict"),
            max_host_count=dict(type="int"),
            nsg_ids=dict(type="list", elements="str"),
            scan_details=dict(
                type="list",
                elements="dict",
                options=dict(fqdn=dict(type="str"), port=dict(type="str")),
            ),
            private_endpoint_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="private_endpoint",
        service_client_class=DataFlowClient,
        namespace="data_flow",
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
