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
module: oci_integration_instance_actions
short_description: Perform actions on an IntegrationInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an IntegrationInstance resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), change the compartment for an integration instance
    - For I(action=change_integration_instance_network_endpoint), change an Integration instance network endpoint. The operation is long-running
      and creates a new WorkRequest.
    - For I(action=start), start an integration instance that was previously in an INACTIVE state
    - For I(action=stop), stop an integration instance that was previously in an ACTIVE state
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    integration_instance_id:
        description:
            - Unique Integration Instance identifier.
        type: str
        aliases: ["id"]
        required: true
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
                    - Source IP addresses or IP address ranges ingress rules.
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
                            - Source IP addresses or IP address ranges ingress rules.
                        type: list
                        elements: str
            is_integration_vcn_allowlisted:
                description:
                    - The Integration service's VCN is allow-listed to allow integrations to call back into other integrations
                type: bool
    action:
        description:
            - The action to perform on the IntegrationInstance.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "change_integration_instance_network_endpoint"
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
                - Standard or Enterprise type
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
                        - Source IP addresses or IP address ranges ingress rules.
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
                                - Source IP addresses or IP address ranges ingress rules.
                            returned: on success
                            type: list
                            sample: []
                is_integration_vcn_allowlisted:
                    description:
                        - The Integration service's VCN is allow-listed to allow integrations to call back into other integrations
                    returned: on success
                    type: bool
                    sample: true
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
            "certificate_secret_version": 56
        },
        "alternate_custom_endpoints": [{
            "hostname": "hostname_example",
            "certificate_secret_id": "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "certificate_secret_version": 56
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
        }
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.integration import IntegrationInstanceClient
    from oci.integration.models import ChangeIntegrationInstanceCompartmentDetails
    from oci.integration.models import ChangeIntegrationInstanceNetworkEndpointDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IntegrationInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        change_integration_instance_network_endpoint
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
            integration_instance_id=dict(aliases=["id"], type="str", required=True),
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
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "change_integration_instance_network_endpoint",
                    "start",
                    "stop",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

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
