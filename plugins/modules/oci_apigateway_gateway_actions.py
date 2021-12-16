#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_apigateway_gateway_actions
short_description: Perform actions on a Gateway resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Gateway resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), changes the gateway compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    gateway_id:
        description:
            - The ocid of the gateway.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the
              resource is created.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Gateway.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on gateway
  oci_apigateway_gateway_actions:
    # required
    gateway_id: "ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

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
                type:
                    description:
                        - Type of the Response Cache.
                    returned: on success
                    type: str
                    sample: EXTERNAL_RESP_CACHE
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
            "type": "EXTERNAL_RESP_CACHE",
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
            "send_timeout_in_ms": 56
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.apigateway import WorkRequestsClient
    from oci.apigateway import GatewayClient
    from oci.apigateway.models import ChangeGatewayCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewayGatewayActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestsClient)

    @staticmethod
    def get_module_resource_id_param():
        return "gateway_id"

    def get_module_resource_id(self):
        return self.module.params.get("gateway_id")

    def get_get_fn(self):
        return self.client.get_gateway

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_gateway, gateway_id=self.module.params.get("gateway_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeGatewayCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_gateway_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                gateway_id=self.module.params.get("gateway_id"),
                change_gateway_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ApigatewayGatewayActionsHelperCustom = get_custom_class(
    "ApigatewayGatewayActionsHelperCustom"
)


class ResourceHelper(
    ApigatewayGatewayActionsHelperCustom, ApigatewayGatewayActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            gateway_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="gateway",
        service_client_class=GatewayClient,
        namespace="apigateway",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
