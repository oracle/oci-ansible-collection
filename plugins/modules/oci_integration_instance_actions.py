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
module: oci_integration_instance_actions
short_description: Perform actions on an IntegrationInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an IntegrationInstance resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), change the compartment for an integration instance
    - For I(action=change_integration_instance_network_endpoint), change an Integration instance network endpoint. The operation is long-running
      and creates a new WorkRequest.
    - For I(action=change_private_endpoint_outbound_connection), change private endpoint outbound connection for given Integration instance. The operation is
      long-running
      and creates a new WorkRequest.
    - For I(action=enable_process_automation), enable Process Automation for given Integration Instance
    - For I(action=start), start an integration instance that was previously in an INACTIVE state
    - For I(action=stop), stop an integration instance that was previously in an ACTIVE state
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment Identifier.
            - Applicable only for I(action=change_compartment).
        type: str
    network_endpoint_details:
        description:
            - ""
            - Applicable only for I(action=change_integration_instance_network_endpoint).
        type: dict
        suboptions:
            network_endpoint_type:
                description:
                    - The type of network endpoint.
                type: str
                choices:
                    - "PUBLIC"
                required: true
            allowlisted_http_ips:
                description:
                    - "Source IP addresses or IP address ranges ingress rules. (ex: \\"168.122.59.5\\", \\"10.20.30.0/26\\")
                      An invalid IP or CIDR block will result in a 400 response."
                type: list
                elements: str
            allowlisted_http_vcns:
                description:
                    - Virtual Cloud Networks allowed to access this network endpoint.
                type: list
                elements: dict
                suboptions:
                    id:
                        description:
                            - The Virtual Cloud Network OCID.
                        type: str
                        required: true
                    allowlisted_ips:
                        description:
                            - "Source IP addresses or IP address ranges ingress rules. (ex: \\"168.122.59.5\\", \\"10.20.30.0/26\\")
                              An invalid IP or CIDR block will result in a 400 response."
                        type: list
                        elements: str
            is_integration_vcn_allowlisted:
                description:
                    - The Integration service's VCN is allow-listed to allow integrations to call back into other integrations
                type: bool
    private_endpoint_outbound_connection:
        description:
            - ""
            - Applicable only for I(action=change_private_endpoint_outbound_connection).
        type: dict
        suboptions:
            subnet_id:
                description:
                    - Customer Private Network VCN Subnet OCID. This is a required argument.
                    - Required when outbound_connection_type is 'PRIVATE_ENDPOINT'
                type: str
            nsg_ids:
                description:
                    - One or more Network security group Ids. This is an optional argument.
                    - Applicable when outbound_connection_type is 'PRIVATE_ENDPOINT'
                type: list
                elements: str
            outbound_connection_type:
                description:
                    - The type of Outbound Connection.
                type: str
                choices:
                    - "PRIVATE_ENDPOINT"
                    - "NONE"
                required: true
    integration_instance_id:
        description:
            - Unique Integration Instance identifier.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the IntegrationInstance.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "change_integration_instance_network_endpoint"
            - "change_private_endpoint_outbound_connection"
            - "enable_process_automation"
            - "start"
            - "stop"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on integration_instance
  oci_integration_instance_actions:
    # required
    integration_instance_id: "ocid1.integrationinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action change_integration_instance_network_endpoint on integration_instance
  oci_integration_instance_actions:
    # required
    integration_instance_id: "ocid1.integrationinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_integration_instance_network_endpoint

    # optional
    network_endpoint_details:
      # required
      network_endpoint_type: PUBLIC

      # optional
      allowlisted_http_ips: [ "allowlisted_http_ips_example" ]
      allowlisted_http_vcns:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        allowlisted_ips: [ "allowlisted_ips_example" ]
      is_integration_vcn_allowlisted: true

- name: Perform action change_private_endpoint_outbound_connection on integration_instance
  oci_integration_instance_actions:
    # required
    integration_instance_id: "ocid1.integrationinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_private_endpoint_outbound_connection

    # optional
    private_endpoint_outbound_connection:
      # required
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
      outbound_connection_type: PRIVATE_ENDPOINT

      # optional
      nsg_ids: [ "nsg_ids_example" ]

- name: Perform action enable_process_automation on integration_instance
  oci_integration_instance_actions:
    # required
    integration_instance_id: "ocid1.integrationinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: enable_process_automation

- name: Perform action start on integration_instance
  oci_integration_instance_actions:
    # required
    integration_instance_id: "ocid1.integrationinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: start

- name: Perform action stop on integration_instance
  oci_integration_instance_actions:
    # required
    integration_instance_id: "ocid1.integrationinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: stop

"""

RETURN = """
integration_instance:
    description:
        - Details of the IntegrationInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Integration Instance Identifier, can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        integration_instance_type:
            description:
                - Standard or Enterprise type,
                  Oracle Integration Generation 2 uses ENTERPRISE and STANDARD,
                  Oracle Integration 3 uses ENTERPRISEX and STANDARDX
            returned: on success
            type: str
            sample: STANDARD
        time_created:
            description:
                - The time the the IntegrationInstance was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the IntegrationInstance was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the integration instance.
            returned: on success
            type: str
            sample: CREATING
        state_message:
            description:
                - An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: state_message_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name,
                  type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to
                  namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        is_byol:
            description:
                - Bring your own license.
            returned: on success
            type: bool
            sample: true
        instance_url:
            description:
                - The Integration Instance URL.
            returned: on success
            type: str
            sample: instance_url_example
        message_packs:
            description:
                - The number of configured message packs (if any)
            returned: on success
            type: int
            sample: 56
        is_file_server_enabled:
            description:
                - The file server is enabled or not.
            returned: on success
            type: bool
            sample: true
        is_visual_builder_enabled:
            description:
                - VisualBuilder is enabled or not.
            returned: on success
            type: bool
            sample: true
        custom_endpoint:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - A custom hostname to be used for the integration instance URL, in FQDN format.
                    returned: on success
                    type: str
                    sample: hostname_example
                certificate_secret_id:
                    description:
                        - Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
                    returned: on success
                    type: str
                    sample: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
                certificate_secret_version:
                    description:
                        - The secret version used for the certificate-secret-id (if certificate-secret-id is specified).
                    returned: on success
                    type: int
                    sample: 56
                alias:
                    description:
                        - When creating the DNS CNAME record for the custom hostname, this value must be specified in the rdata.
                    returned: on success
                    type: str
                    sample: alias_example
        alternate_custom_endpoints:
            description:
                - A list of alternate custom endpoints used for the integration instance URL.
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - A custom hostname to be used for the integration instance URL, in FQDN format.
                    returned: on success
                    type: str
                    sample: hostname_example
                certificate_secret_id:
                    description:
                        - Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
                    returned: on success
                    type: str
                    sample: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
                certificate_secret_version:
                    description:
                        - The secret version used for the certificate-secret-id (if certificate-secret-id is specified).
                    returned: on success
                    type: int
                    sample: 56
                alias:
                    description:
                        - When creating the DNS CNAME record for the custom hostname, this value must be specified in the rdata.
                    returned: on success
                    type: str
                    sample: alias_example
        consumption_model:
            description:
                - The entitlement used for billing purposes.
            returned: on success
            type: str
            sample: UCM
        network_endpoint_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                network_endpoint_type:
                    description:
                        - The type of network endpoint.
                    returned: on success
                    type: str
                    sample: PUBLIC
                allowlisted_http_ips:
                    description:
                        - "Source IP addresses or IP address ranges ingress rules. (ex: \\"168.122.59.5\\", \\"10.20.30.0/26\\")
                          An invalid IP or CIDR block will result in a 400 response."
                    returned: on success
                    type: list
                    sample: []
                allowlisted_http_vcns:
                    description:
                        - Virtual Cloud Networks allowed to access this network endpoint.
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The Virtual Cloud Network OCID.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        allowlisted_ips:
                            description:
                                - "Source IP addresses or IP address ranges ingress rules. (ex: \\"168.122.59.5\\", \\"10.20.30.0/26\\")
                                  An invalid IP or CIDR block will result in a 400 response."
                            returned: on success
                            type: list
                            sample: []
                is_integration_vcn_allowlisted:
                    description:
                        - The Integration service's VCN is allow-listed to allow integrations to call back into other integrations
                    returned: on success
                    type: bool
                    sample: true
        idcs_info:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                idcs_app_location_url:
                    description:
                        - URL for the location of the IDCS Application (used by IDCS APIs)
                    returned: on success
                    type: str
                    sample: idcs_app_location_url_example
                idcs_app_display_name:
                    description:
                        - The IDCS application display name associated with the instance
                    returned: on success
                    type: str
                    sample: idcs_app_display_name_example
                idcs_app_id:
                    description:
                        - The IDCS application ID associated with the instance
                    returned: on success
                    type: str
                    sample: "ocid1.idcsapp.oc1..xxxxxxEXAMPLExxxxxx"
                idcs_app_name:
                    description:
                        - The IDCS application name associated with the instance
                    returned: on success
                    type: str
                    sample: idcs_app_name_example
                instance_primary_audience_url:
                    description:
                        - "The URL used as the primary audience for integration flows in this instance
                          type: string"
                    returned: on success
                    type: str
                    sample: instance_primary_audience_url_example
        attachments:
            description:
                - A list of associated attachments to other services
            returned: on success
            type: complex
            contains:
                target_role:
                    description:
                        - "The role of the target attachment.
                             * `PARENT` - The target instance is the parent of this attachment.
                             * `CHILD` - The target instance is the child of this attachment."
                    returned: on success
                    type: str
                    sample: PARENT
                is_implicit:
                    description:
                        - "* If role == `PARENT`, the attached instance was created by this service instance
                          * If role == `CHILD`, this instance was created from attached instance on behalf of a user"
                    returned: on success
                    type: bool
                    sample: true
                target_id:
                    description:
                        - The OCID of the target instance (which could be any other OCI PaaS/SaaS resource), to which this instance is attached.
                    returned: on success
                    type: str
                    sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
                target_instance_url:
                    description:
                        - The dataplane instance URL of the attached instance
                    returned: on success
                    type: str
                    sample: target_instance_url_example
                target_service_type:
                    description:
                        - "The type of the target instance, such as \\"FUSION\\"."
                    returned: on success
                    type: str
                    sample: target_service_type_example
        shape:
            description:
                - Shape
            returned: on success
            type: str
            sample: DEVELOPMENT
        private_endpoint_outbound_connection:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                outbound_connection_type:
                    description:
                        - The type of Outbound Connection.
                    returned: on success
                    type: str
                    sample: PRIVATE_ENDPOINT
                subnet_id:
                    description:
                        - Customer Private Network VCN Subnet OCID. This is a required argument.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                nsg_ids:
                    description:
                        - One or more Network security group Ids. This is an optional argument.
                    returned: on success
                    type: list
                    sample: []
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "integration_instance_type": "STANDARD",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "state_message": "state_message_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "is_byol": true,
        "instance_url": "instance_url_example",
        "message_packs": 56,
        "is_file_server_enabled": true,
        "is_visual_builder_enabled": true,
        "custom_endpoint": {
            "hostname": "hostname_example",
            "certificate_secret_id": "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "certificate_secret_version": 56,
            "alias": "alias_example"
        },
        "alternate_custom_endpoints": [{
            "hostname": "hostname_example",
            "certificate_secret_id": "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "certificate_secret_version": 56,
            "alias": "alias_example"
        }],
        "consumption_model": "UCM",
        "network_endpoint_details": {
            "network_endpoint_type": "PUBLIC",
            "allowlisted_http_ips": [],
            "allowlisted_http_vcns": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "allowlisted_ips": []
            }],
            "is_integration_vcn_allowlisted": true
        },
        "idcs_info": {
            "idcs_app_location_url": "idcs_app_location_url_example",
            "idcs_app_display_name": "idcs_app_display_name_example",
            "idcs_app_id": "ocid1.idcsapp.oc1..xxxxxxEXAMPLExxxxxx",
            "idcs_app_name": "idcs_app_name_example",
            "instance_primary_audience_url": "instance_primary_audience_url_example"
        },
        "attachments": [{
            "target_role": "PARENT",
            "is_implicit": true,
            "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
            "target_instance_url": "target_instance_url_example",
            "target_service_type": "target_service_type_example"
        }],
        "shape": "DEVELOPMENT",
        "private_endpoint_outbound_connection": {
            "outbound_connection_type": "PRIVATE_ENDPOINT",
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "nsg_ids": []
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.integration import IntegrationInstanceClient
    from oci.integration.models import ChangeIntegrationInstanceCompartmentDetails
    from oci.integration.models import ChangeIntegrationInstanceNetworkEndpointDetails
    from oci.integration.models import ChangePrivateEndpointOutboundConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IntegrationInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        change_integration_instance_network_endpoint
        change_private_endpoint_outbound_connection
        enable_process_automation
        start
        stop
    """

    @staticmethod
    def get_module_resource_id_param():
        return "integration_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("integration_instance_id")

    def get_get_fn(self):
        return self.client.get_integration_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_integration_instance,
            integration_instance_id=self.module.params.get("integration_instance_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeIntegrationInstanceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_integration_instance_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                integration_instance_id=self.module.params.get(
                    "integration_instance_id"
                ),
                change_integration_instance_compartment_details=action_details,
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

    def change_integration_instance_network_endpoint(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeIntegrationInstanceNetworkEndpointDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_integration_instance_network_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                integration_instance_id=self.module.params.get(
                    "integration_instance_id"
                ),
                change_integration_instance_network_endpoint_details=action_details,
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

    def change_private_endpoint_outbound_connection(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangePrivateEndpointOutboundConnectionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_private_endpoint_outbound_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                integration_instance_id=self.module.params.get(
                    "integration_instance_id"
                ),
                change_private_endpoint_outbound_connection_details=action_details,
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

    def enable_process_automation(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_process_automation,
            call_fn_args=(),
            call_fn_kwargs=dict(
                integration_instance_id=self.module.params.get(
                    "integration_instance_id"
                ),
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

    def start(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_integration_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                integration_instance_id=self.module.params.get(
                    "integration_instance_id"
                ),
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

    def stop(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_integration_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                integration_instance_id=self.module.params.get(
                    "integration_instance_id"
                ),
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


IntegrationInstanceActionsHelperCustom = get_custom_class(
    "IntegrationInstanceActionsHelperCustom"
)


class ResourceHelper(
    IntegrationInstanceActionsHelperCustom, IntegrationInstanceActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            network_endpoint_details=dict(
                type="dict",
                options=dict(
                    network_endpoint_type=dict(
                        type="str", required=True, choices=["PUBLIC"]
                    ),
                    allowlisted_http_ips=dict(type="list", elements="str"),
                    allowlisted_http_vcns=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            id=dict(type="str", required=True),
                            allowlisted_ips=dict(type="list", elements="str"),
                        ),
                    ),
                    is_integration_vcn_allowlisted=dict(type="bool"),
                ),
            ),
            private_endpoint_outbound_connection=dict(
                type="dict",
                options=dict(
                    subnet_id=dict(type="str"),
                    nsg_ids=dict(type="list", elements="str"),
                    outbound_connection_type=dict(
                        type="str", required=True, choices=["PRIVATE_ENDPOINT", "NONE"]
                    ),
                ),
            ),
            integration_instance_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "change_integration_instance_network_endpoint",
                    "change_private_endpoint_outbound_connection",
                    "enable_process_automation",
                    "start",
                    "stop",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="integration_instance",
        service_client_class=IntegrationInstanceClient,
        namespace="integration",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
