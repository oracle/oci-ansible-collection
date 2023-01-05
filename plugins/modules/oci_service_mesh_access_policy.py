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
module: oci_service_mesh_access_policy
short_description: Manage an AccessPolicy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an AccessPolicy resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new AccessPolicy.
    - "This resource has the following action operations in the M(oracle.oci.oci_service_mesh_access_policy_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation.
              Avoid entering confidential information.
            - "Example: `My unique resource name`"
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    mesh_id:
        description:
            - The OCID of the service mesh in which this access policy is created.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - Description of the resource. It can be changed after creation.
              Avoid entering confidential information.
            - "Example: `This is my new resource`"
            - This parameter is updatable.
        type: str
    rules:
        description:
            - List of applicable rules
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            action:
                description:
                    - Action for the traffic between the source and the destination.
                type: str
                choices:
                    - "ALLOW"
                required: true
            source:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    virtual_service_id:
                        description:
                            - The OCID of the virtual service resource.
                            - Required when type is 'VIRTUAL_SERVICE'
                        type: str
                    hostnames:
                        description:
                            - "The hostnames of the external service. Only applicable for HTTP and HTTPS protocols.
                              Wildcard hostnames are supported in the prefix form.
                              Examples of valid hostnames are \\"www.example.com\\", \\"*.example.com\\", \\"*.com\\", \\"*\\".
                              Hostname \\"*\\" can be used to allow all hosts."
                            - Applicable when type is 'EXTERNAL_SERVICE'
                        type: list
                        elements: str
                    ip_addresses:
                        description:
                            - "The ipAddresses of the external service in CIDR notation. Only applicable for TCP protocol.
                              All requests matching the given CIDR notation will pass through.
                              In case a wildcard CIDR \\"0.0.0.0/0\\" is provided, the same port cannot be used for a virtual service communication."
                            - Applicable when type is 'EXTERNAL_SERVICE'
                        type: list
                        elements: str
                    ports:
                        description:
                            - Ports exposed by an external service. If left empty all ports will be allowed.
                            - Applicable when type is 'EXTERNAL_SERVICE'
                        type: list
                        elements: int
                    protocol:
                        description:
                            - Protocol of the external service
                            - Applicable when type is 'EXTERNAL_SERVICE'
                        type: str
                        choices:
                            - "HTTP"
                            - "HTTPS"
                            - "TCP"
                    type:
                        description:
                            - Traffic type of the target.
                        type: str
                        choices:
                            - "VIRTUAL_SERVICE"
                            - "ALL_VIRTUAL_SERVICES"
                            - "EXTERNAL_SERVICE"
                            - "INGRESS_GATEWAY"
                        required: true
                    ingress_gateway_id:
                        description:
                            - The OCID of the ingress gateway resource.
                            - Required when type is 'INGRESS_GATEWAY'
                        type: str
            destination:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    virtual_service_id:
                        description:
                            - The OCID of the virtual service resource.
                            - Required when type is 'VIRTUAL_SERVICE'
                        type: str
                    hostnames:
                        description:
                            - "The hostnames of the external service. Only applicable for HTTP and HTTPS protocols.
                              Wildcard hostnames are supported in the prefix form.
                              Examples of valid hostnames are \\"www.example.com\\", \\"*.example.com\\", \\"*.com\\", \\"*\\".
                              Hostname \\"*\\" can be used to allow all hosts."
                            - Applicable when type is 'EXTERNAL_SERVICE'
                        type: list
                        elements: str
                    ip_addresses:
                        description:
                            - "The ipAddresses of the external service in CIDR notation. Only applicable for TCP protocol.
                              All requests matching the given CIDR notation will pass through.
                              In case a wildcard CIDR \\"0.0.0.0/0\\" is provided, the same port cannot be used for a virtual service communication."
                            - Applicable when type is 'EXTERNAL_SERVICE'
                        type: list
                        elements: str
                    ports:
                        description:
                            - Ports exposed by an external service. If left empty all ports will be allowed.
                            - Applicable when type is 'EXTERNAL_SERVICE'
                        type: list
                        elements: int
                    protocol:
                        description:
                            - Protocol of the external service
                            - Applicable when type is 'EXTERNAL_SERVICE'
                        type: str
                        choices:
                            - "HTTP"
                            - "HTTPS"
                            - "TCP"
                    type:
                        description:
                            - Traffic type of the target.
                        type: str
                        choices:
                            - "VIRTUAL_SERVICE"
                            - "ALL_VIRTUAL_SERVICES"
                            - "EXTERNAL_SERVICE"
                            - "INGRESS_GATEWAY"
                        required: true
                    ingress_gateway_id:
                        description:
                            - The OCID of the ingress gateway resource.
                            - Required when type is 'INGRESS_GATEWAY'
                        type: str
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
    access_policy_id:
        description:
            - Unique AccessPolicy identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the AccessPolicy.
            - Use I(state=present) to create or update an AccessPolicy.
            - Use I(state=absent) to delete an AccessPolicy.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create access_policy
  oci_service_mesh_access_policy:
    # required
    name: name_example
    mesh_id: "ocid1.mesh.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    rules:
    - # required
      action: ALLOW
      source:
        # required
        virtual_service_id: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
        type: VIRTUAL_SERVICE
      destination:
        # required
        virtual_service_id: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
        type: VIRTUAL_SERVICE
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update access_policy
  oci_service_mesh_access_policy:
    # required
    access_policy_id: "ocid1.accesspolicy.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    rules:
    - # required
      action: ALLOW
      source:
        # required
        virtual_service_id: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
        type: VIRTUAL_SERVICE
      destination:
        # required
        virtual_service_id: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
        type: VIRTUAL_SERVICE
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update access_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_service_mesh_access_policy:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    rules:
    - # required
      action: ALLOW
      source:
        # required
        virtual_service_id: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
        type: VIRTUAL_SERVICE
      destination:
        # required
        virtual_service_id: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
        type: VIRTUAL_SERVICE
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete access_policy
  oci_service_mesh_access_policy:
    # required
    access_policy_id: "ocid1.accesspolicy.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete access_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_service_mesh_access_policy:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
access_policy:
    description:
        - Details of the AccessPolicy resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation.
                  Avoid entering confidential information.
                - "Example: `My unique resource name`"
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - Description of the resource. It can be changed after creation.
                  Avoid entering confidential information.
                - "Example: `This is my new resource`"
            returned: on success
            type: str
            sample: description_example
        mesh_id:
            description:
                - The OCID of the service mesh in which this access policy is created.
            returned: on success
            type: str
            sample: "ocid1.mesh.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        rules:
            description:
                - List of applicable rules.
            returned: on success
            type: complex
            contains:
                action:
                    description:
                        - Action for the traffic between the source and the destination.
                    returned: on success
                    type: str
                    sample: ALLOW
                source:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        hostnames:
                            description:
                                - "The hostnames of the external service. Only applicable for HTTP and HTTPS protocols.
                                  Wildcard hostnames are supported in the prefix form.
                                  Examples of valid hostnames are \\"www.example.com\\", \\"*.example.com\\", \\"*.com\\", \\"*\\".
                                  Hostname \\"*\\" can be used to allow all hosts."
                            returned: on success
                            type: list
                            sample: []
                        ip_addresses:
                            description:
                                - "The ipAddresses of the external service in CIDR notation. Only applicable for TCP protocol.
                                  All requests matching the given CIDR notation will pass through.
                                  In case a wildcard CIDR \\"0.0.0.0/0\\" is provided, the same port cannot be used for a virtual service communication."
                            returned: on success
                            type: list
                            sample: []
                        ports:
                            description:
                                - Ports exposed by an external service. If left empty all ports will be allowed.
                            returned: on success
                            type: list
                            sample: []
                        protocol:
                            description:
                                - Protocol of the external service
                            returned: on success
                            type: str
                            sample: HTTP
                        ingress_gateway_id:
                            description:
                                - The OCID of the ingress gateway resource.
                            returned: on success
                            type: str
                            sample: "ocid1.ingressgateway.oc1..xxxxxxEXAMPLExxxxxx"
                        type:
                            description:
                                - Traffic type of the target.
                            returned: on success
                            type: str
                            sample: ALL_VIRTUAL_SERVICES
                        virtual_service_id:
                            description:
                                - The OCID of the virtual service resource.
                            returned: on success
                            type: str
                            sample: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
                destination:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        hostnames:
                            description:
                                - "The hostnames of the external service. Only applicable for HTTP and HTTPS protocols.
                                  Wildcard hostnames are supported in the prefix form.
                                  Examples of valid hostnames are \\"www.example.com\\", \\"*.example.com\\", \\"*.com\\", \\"*\\".
                                  Hostname \\"*\\" can be used to allow all hosts."
                            returned: on success
                            type: list
                            sample: []
                        ip_addresses:
                            description:
                                - "The ipAddresses of the external service in CIDR notation. Only applicable for TCP protocol.
                                  All requests matching the given CIDR notation will pass through.
                                  In case a wildcard CIDR \\"0.0.0.0/0\\" is provided, the same port cannot be used for a virtual service communication."
                            returned: on success
                            type: list
                            sample: []
                        ports:
                            description:
                                - Ports exposed by an external service. If left empty all ports will be allowed.
                            returned: on success
                            type: list
                            sample: []
                        protocol:
                            description:
                                - Protocol of the external service
                            returned: on success
                            type: str
                            sample: HTTP
                        ingress_gateway_id:
                            description:
                                - The OCID of the ingress gateway resource.
                            returned: on success
                            type: str
                            sample: "ocid1.ingressgateway.oc1..xxxxxxEXAMPLExxxxxx"
                        type:
                            description:
                                - Traffic type of the target.
                            returned: on success
                            type: str
                            sample: ALL_VIRTUAL_SERVICES
                        virtual_service_id:
                            description:
                                - The OCID of the virtual service resource.
                            returned: on success
                            type: str
                            sample: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time when this resource was created in an RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when this resource was updated in an RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Resource.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
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
        "name": "name_example",
        "description": "description_example",
        "mesh_id": "ocid1.mesh.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "rules": [{
            "action": "ALLOW",
            "source": {
                "hostnames": [],
                "ip_addresses": [],
                "ports": [],
                "protocol": "HTTP",
                "ingress_gateway_id": "ocid1.ingressgateway.oc1..xxxxxxEXAMPLExxxxxx",
                "type": "ALL_VIRTUAL_SERVICES",
                "virtual_service_id": "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "destination": {
                "hostnames": [],
                "ip_addresses": [],
                "ports": [],
                "protocol": "HTTP",
                "ingress_gateway_id": "ocid1.ingressgateway.oc1..xxxxxxEXAMPLExxxxxx",
                "type": "ALL_VIRTUAL_SERVICES",
                "virtual_service_id": "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
            }
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
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
    from oci.service_mesh import ServiceMeshClient
    from oci.service_mesh.models import CreateAccessPolicyDetails
    from oci.service_mesh.models import UpdateAccessPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AccessPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(AccessPolicyHelperGen, self).get_possible_entity_types() + [
            "accesspolicy",
            "accesspolicies",
            "serviceMeshaccesspolicy",
            "serviceMeshaccesspolicies",
            "accesspolicyresource",
            "accesspoliciesresource",
            "servicemesh",
        ]

    def get_module_resource_id_param(self):
        return "access_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("access_policy_id")

    def get_get_fn(self):
        return self.client.get_access_policy

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_access_policy, access_policy_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_access_policy,
            access_policy_id=self.module.params.get("access_policy_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name", "mesh_id"]

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
            self.client.list_access_policies, **kwargs
        )

    def get_create_model_class(self):
        return CreateAccessPolicyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_access_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(create_access_policy_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateAccessPolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_access_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                access_policy_id=self.module.params.get("access_policy_id"),
                update_access_policy_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_access_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                access_policy_id=self.module.params.get("access_policy_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AccessPolicyHelperCustom = get_custom_class("AccessPolicyHelperCustom")


class ResourceHelper(AccessPolicyHelperCustom, AccessPolicyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            mesh_id=dict(type="str"),
            compartment_id=dict(type="str"),
            description=dict(type="str"),
            rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    action=dict(type="str", required=True, choices=["ALLOW"]),
                    source=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            virtual_service_id=dict(type="str"),
                            hostnames=dict(type="list", elements="str"),
                            ip_addresses=dict(type="list", elements="str"),
                            ports=dict(type="list", elements="int"),
                            protocol=dict(type="str", choices=["HTTP", "HTTPS", "TCP"]),
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "VIRTUAL_SERVICE",
                                    "ALL_VIRTUAL_SERVICES",
                                    "EXTERNAL_SERVICE",
                                    "INGRESS_GATEWAY",
                                ],
                            ),
                            ingress_gateway_id=dict(type="str"),
                        ),
                    ),
                    destination=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            virtual_service_id=dict(type="str"),
                            hostnames=dict(type="list", elements="str"),
                            ip_addresses=dict(type="list", elements="str"),
                            ports=dict(type="list", elements="int"),
                            protocol=dict(type="str", choices=["HTTP", "HTTPS", "TCP"]),
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "VIRTUAL_SERVICE",
                                    "ALL_VIRTUAL_SERVICES",
                                    "EXTERNAL_SERVICE",
                                    "INGRESS_GATEWAY",
                                ],
                            ),
                            ingress_gateway_id=dict(type="str"),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            access_policy_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="access_policy",
        service_client_class=ServiceMeshClient,
        namespace="service_mesh",
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
