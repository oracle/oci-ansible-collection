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
module: oci_apigateway_gateway
short_description: Manage a Gateway resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Gateway resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new gateway.
    - "This resource has the following action operations in the M(oracle.oci.oci_apigateway_gateway_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the
              resource is created.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    endpoint_type:
        description:
            - Gateway endpoint type. `PUBLIC` will have a public ip address assigned to it, while `PRIVATE` will only be
              accessible on a private IP address on the subnet.
            - "Example: `PUBLIC` or `PRIVATE`"
            - Required for create using I(state=present).
        type: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet in which
              related resources are created.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - "Example: `My new resource`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    network_security_group_ids:
        description:
            - An array of Network Security Groups OCIDs associated with this API Gateway.
            - This parameter is updatable.
        type: list
        elements: str
    certificate_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
            - This parameter is updatable.
        type: str
    response_cache_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            servers:
                description:
                    - The set of cache store members to connect to. At present only a single server is supported.
                    - Required when type is 'EXTERNAL_RESP_CACHE'
                type: list
                elements: dict
                suboptions:
                    host:
                        description:
                            - Hostname or IP address (IPv4 only) where the cache store is running.
                            - Required when type is 'EXTERNAL_RESP_CACHE'
                        type: str
                        required: true
                    port:
                        description:
                            - The port the cache store is exposed on.
                            - Required when type is 'EXTERNAL_RESP_CACHE'
                        type: int
                        required: true
            authentication_secret_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Vault Service secret resource.
                    - Required when type is 'EXTERNAL_RESP_CACHE'
                type: str
            authentication_secret_version_number:
                description:
                    - The version number of the authentication secret to use.
                    - Required when type is 'EXTERNAL_RESP_CACHE'
                type: int
            is_ssl_enabled:
                description:
                    - Defines if the connection should be over SSL.
                    - Applicable when type is 'EXTERNAL_RESP_CACHE'
                type: bool
            is_ssl_verify_disabled:
                description:
                    - Defines whether or not to uphold SSL verification.
                    - Applicable when type is 'EXTERNAL_RESP_CACHE'
                type: bool
            connect_timeout_in_ms:
                description:
                    - Defines the timeout for establishing a connection with the Response Cache.
                    - Applicable when type is 'EXTERNAL_RESP_CACHE'
                type: int
            read_timeout_in_ms:
                description:
                    - Defines the timeout for reading data from the Response Cache.
                    - Applicable when type is 'EXTERNAL_RESP_CACHE'
                type: int
            send_timeout_in_ms:
                description:
                    - Defines the timeout for transmitting data to the Response Cache.
                    - Applicable when type is 'EXTERNAL_RESP_CACHE'
                type: int
            type:
                description:
                    - Type of the Response Cache.
                type: str
                choices:
                    - "EXTERNAL_RESP_CACHE"
                    - "NONE"
                required: true
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair
              with no predefined name, type, or namespace. For more information, see
              L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see
              L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    ca_bundles:
        description:
            - An array of CA bundles that should be used on the Gateway for TLS validation.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            ca_bundle_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
                    - Applicable when type is 'CA_BUNDLE'
                type: str
            type:
                description:
                    - Type of the CA bundle
                type: str
                choices:
                    - "CA_BUNDLE"
                    - "CERTIFICATE_AUTHORITY"
                required: true
            certificate_authority_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
                    - Applicable when type is 'CERTIFICATE_AUTHORITY'
                type: str
    gateway_id:
        description:
            - The ocid of the gateway.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Gateway.
            - Use I(state=present) to create or update a Gateway.
            - Use I(state=absent) to delete a Gateway.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create gateway
  oci_apigateway_gateway:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    endpoint_type: endpoint_type_example
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    network_security_group_ids: [ "network_security_group_ids_example" ]
    certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    response_cache_details:
      # required
      servers:
      - # required
        host: host_example
        port: 56
      authentication_secret_id: "ocid1.authenticationsecret.oc1..xxxxxxEXAMPLExxxxxx"
      authentication_secret_version_number: 56
      type: EXTERNAL_RESP_CACHE

        # optional
      is_ssl_enabled: true
      is_ssl_verify_disabled: true
      connect_timeout_in_ms: 56
      read_timeout_in_ms: 56
      send_timeout_in_ms: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    ca_bundles:
    - # required
      type: CA_BUNDLE

      # optional
      ca_bundle_id: "ocid1.cabundle.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update gateway
  oci_apigateway_gateway:
    # required
    gateway_id: "ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    network_security_group_ids: [ "network_security_group_ids_example" ]
    certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    response_cache_details:
      # required
      servers:
      - # required
        host: host_example
        port: 56
      authentication_secret_id: "ocid1.authenticationsecret.oc1..xxxxxxEXAMPLExxxxxx"
      authentication_secret_version_number: 56
      type: EXTERNAL_RESP_CACHE

        # optional
      is_ssl_enabled: true
      is_ssl_verify_disabled: true
      connect_timeout_in_ms: 56
      read_timeout_in_ms: 56
      send_timeout_in_ms: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    ca_bundles:
    - # required
      type: CA_BUNDLE

      # optional
      ca_bundle_id: "ocid1.cabundle.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update gateway using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_apigateway_gateway:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    network_security_group_ids: [ "network_security_group_ids_example" ]
    certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    response_cache_details:
      # required
      servers:
      - # required
        host: host_example
        port: 56
      authentication_secret_id: "ocid1.authenticationsecret.oc1..xxxxxxEXAMPLExxxxxx"
      authentication_secret_version_number: 56
      type: EXTERNAL_RESP_CACHE

        # optional
      is_ssl_enabled: true
      is_ssl_verify_disabled: true
      connect_timeout_in_ms: 56
      read_timeout_in_ms: 56
      send_timeout_in_ms: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    ca_bundles:
    - # required
      type: CA_BUNDLE

      # optional
      ca_bundle_id: "ocid1.cabundle.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete gateway
  oci_apigateway_gateway:
    # required
    gateway_id: "ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete gateway using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_apigateway_gateway:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
gateway:
    description:
        - Details of the Gateway resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
                - "Example: `My new resource`"
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the
                  resource is created.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        endpoint_type:
            description:
                - Gateway endpoint type. `PUBLIC` will have a public ip address assigned to it, while `PRIVATE` will only be
                  accessible on a private IP address on the subnet.
                - "Example: `PUBLIC` or `PRIVATE`"
            returned: on success
            type: str
            sample: PUBLIC
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet in which
                  related resources are created.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        network_security_group_ids:
            description:
                - An array of Network Security Groups OCIDs associated with this API Gateway.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The time this resource was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time this resource was last updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the gateway.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a
                  resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        hostname:
            description:
                - The hostname for APIs deployed on the gateway.
            returned: on success
            type: str
            sample: hostname_example
        certificate_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
            returned: on success
            type: str
            sample: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
        ip_addresses:
            description:
                - An array of IP addresses associated with the gateway.
            returned: on success
            type: complex
            contains:
                ip_address:
                    description:
                        - An IP address.
                    returned: on success
                    type: str
                    sample: ip_address_example
        response_cache_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                servers:
                    description:
                        - The set of cache store members to connect to. At present only a single server is supported.
                    returned: on success
                    type: complex
                    contains:
                        host:
                            description:
                                - Hostname or IP address (IPv4 only) where the cache store is running.
                            returned: on success
                            type: str
                            sample: host_example
                        port:
                            description:
                                - The port the cache store is exposed on.
                            returned: on success
                            type: int
                            sample: 56
                authentication_secret_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Vault Service secret resource.
                    returned: on success
                    type: str
                    sample: "ocid1.authenticationsecret.oc1..xxxxxxEXAMPLExxxxxx"
                authentication_secret_version_number:
                    description:
                        - The version number of the authentication secret to use.
                    returned: on success
                    type: int
                    sample: 56
                is_ssl_enabled:
                    description:
                        - Defines if the connection should be over SSL.
                    returned: on success
                    type: bool
                    sample: true
                is_ssl_verify_disabled:
                    description:
                        - Defines whether or not to uphold SSL verification.
                    returned: on success
                    type: bool
                    sample: true
                connect_timeout_in_ms:
                    description:
                        - Defines the timeout for establishing a connection with the Response Cache.
                    returned: on success
                    type: int
                    sample: 56
                read_timeout_in_ms:
                    description:
                        - Defines the timeout for reading data from the Response Cache.
                    returned: on success
                    type: int
                    sample: 56
                send_timeout_in_ms:
                    description:
                        - Defines the timeout for transmitting data to the Response Cache.
                    returned: on success
                    type: int
                    sample: 56
                type:
                    description:
                        - Type of the Response Cache.
                    returned: on success
                    type: str
                    sample: EXTERNAL_RESP_CACHE
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair
                  with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        ca_bundles:
            description:
                - An array of CA bundles that should be used on the Gateway for TLS validation.
            returned: on success
            type: complex
            contains:
                ca_bundle_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
                    returned: on success
                    type: str
                    sample: "ocid1.cabundle.oc1..xxxxxxEXAMPLExxxxxx"
                type:
                    description:
                        - Type of the CA bundle
                    returned: on success
                    type: str
                    sample: CA_BUNDLE
                certificate_authority_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
                    returned: on success
                    type: str
                    sample: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "endpoint_type": "PUBLIC",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "network_security_group_ids": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "hostname": "hostname_example",
        "certificate_id": "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx",
        "ip_addresses": [{
            "ip_address": "ip_address_example"
        }],
        "response_cache_details": {
            "servers": [{
                "host": "host_example",
                "port": 56
            }],
            "authentication_secret_id": "ocid1.authenticationsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "authentication_secret_version_number": 56,
            "is_ssl_enabled": true,
            "is_ssl_verify_disabled": true,
            "connect_timeout_in_ms": 56,
            "read_timeout_in_ms": 56,
            "send_timeout_in_ms": 56,
            "type": "EXTERNAL_RESP_CACHE"
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "ca_bundles": [{
            "ca_bundle_id": "ocid1.cabundle.oc1..xxxxxxEXAMPLExxxxxx",
            "type": "CA_BUNDLE",
            "certificate_authority_id": "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.apigateway import WorkRequestsClient
    from oci.apigateway import GatewayClient
    from oci.apigateway.models import CreateGatewayDetails
    from oci.apigateway.models import UpdateGatewayDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewayGatewayHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestsClient)

    def get_possible_entity_types(self):
        return super(ApigatewayGatewayHelperGen, self).get_possible_entity_types() + [
            "gateway",
            "gateways",
            "apigatewaygateway",
            "apigatewaygateways",
            "gatewayresource",
            "gatewaysresource",
            "apigateway",
        ]

    def get_module_resource_id_param(self):
        return "gateway_id"

    def get_module_resource_id(self):
        return self.module.params.get("gateway_id")

    def get_get_fn(self):
        return self.client.get_gateway

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_gateway, gateway_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_gateway, gateway_id=self.module.params.get("gateway_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name"]
            if self._use_name_as_identifier()
            else ["certificate_id", "display_name"]
        )

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
        return oci_common_utils.list_all_resources(self.client.list_gateways, **kwargs)

    def get_create_model_class(self):
        return CreateGatewayDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(create_gateway_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateGatewayDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(
                gateway_id=self.module.params.get("gateway_id"),
                update_gateway_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(gateway_id=self.module.params.get("gateway_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ApigatewayGatewayHelperCustom = get_custom_class("ApigatewayGatewayHelperCustom")


class ResourceHelper(ApigatewayGatewayHelperCustom, ApigatewayGatewayHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            endpoint_type=dict(type="str"),
            subnet_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            network_security_group_ids=dict(type="list", elements="str"),
            certificate_id=dict(type="str"),
            response_cache_details=dict(
                type="dict",
                options=dict(
                    servers=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            host=dict(type="str", required=True),
                            port=dict(type="int", required=True),
                        ),
                    ),
                    authentication_secret_id=dict(type="str"),
                    authentication_secret_version_number=dict(type="int", no_log=True),
                    is_ssl_enabled=dict(type="bool"),
                    is_ssl_verify_disabled=dict(type="bool"),
                    connect_timeout_in_ms=dict(type="int"),
                    read_timeout_in_ms=dict(type="int"),
                    send_timeout_in_ms=dict(type="int"),
                    type=dict(
                        type="str",
                        required=True,
                        choices=["EXTERNAL_RESP_CACHE", "NONE"],
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            ca_bundles=dict(
                type="list",
                elements="dict",
                options=dict(
                    ca_bundle_id=dict(type="str"),
                    type=dict(
                        type="str",
                        required=True,
                        choices=["CA_BUNDLE", "CERTIFICATE_AUTHORITY"],
                    ),
                    certificate_authority_id=dict(type="str"),
                ),
            ),
            gateway_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="gateway",
        service_client_class=GatewayClient,
        namespace="apigateway",
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
