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
module: oci_integration_instance
short_description: Manage an IntegrationInstance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an IntegrationInstance resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Integration Instance.
    - "This resource has the following action operations in the M(oracle.oci.oci_integration_instance_actions) module: change_compartment,
      change_integration_instance_network_endpoint, change_private_endpoint_outbound_connection, enable_process_automation, start, stop."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment Identifier.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    idcs_at:
        description:
            - IDCS Authentication token. This is required for all realms with IDCS. Its optional as its not required for non IDCS realms.
        type: str
    consumption_model:
        description:
            - Optional parameter specifying which entitlement to use for billing purposes. Only required if the account possesses more than one entitlement.
        type: str
        choices:
            - "UCM"
            - "GOV"
            - "OIC4SAAS"
    network_endpoint_details:
        description:
            - ""
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
    shape:
        description:
            - Shape
        type: str
        choices:
            - "DEVELOPMENT"
            - "PRODUCTION"
    domain_id:
        description:
            - "The OCID of the identity domain, that will be used to determine the
              corresponding Idcs Stripe and create an Idcs application within the stripe.
              This parameter is mutually exclusive with parameter: idcsAt, i.e only one of
              two parameters should be specified."
        type: str
    display_name:
        description:
            - Integration Instance Identifier.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    integration_instance_type:
        description:
            - Standard or Enterprise type,
              Oracle Integration Generation 2 uses ENTERPRISE and STANDARD,
              Oracle Integration 3 uses ENTERPRISEX and STANDARDX
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "STANDARD"
            - "ENTERPRISE"
            - "STANDARDX"
            - "ENTERPRISEX"
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name,
              type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Usage of predefined tag keys. These predefined keys are scoped to
              namespaces.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    is_byol:
        description:
            - Bring your own license.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: bool
    message_packs:
        description:
            - The number of configured message packs
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    is_file_server_enabled:
        description:
            - The file server is enabled or not.
            - This parameter is updatable.
        type: bool
    is_visual_builder_enabled:
        description:
            - Visual Builder is enabled or not.
            - This parameter is updatable.
        type: bool
    custom_endpoint:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            hostname:
                description:
                    - A custom hostname to be used for the integration instance URL, in FQDN format.
                    - This parameter is updatable.
                type: str
                required: true
            certificate_secret_id:
                description:
                    - Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
                      All certificates should be stored in a single base64 encoded secret
                      Note the update will fail if this is not a valid certificate.
                    - This parameter is updatable.
                type: str
    alternate_custom_endpoints:
        description:
            - A list of alternate custom endpoints to be used for the integration instance URL
              (contact Oracle for alternateCustomEndpoints availability for a specific instance).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            hostname:
                description:
                    - A custom hostname to be used for the integration instance URL, in FQDN format.
                    - This parameter is updatable.
                type: str
                required: true
            certificate_secret_id:
                description:
                    - Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
                      All certificates should be stored in a single base64 encoded secret
                      Note the update will fail if this is not a valid certificate.
                    - This parameter is updatable.
                type: str
    integration_instance_id:
        description:
            - Unique Integration Instance identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the IntegrationInstance.
            - Use I(state=present) to create or update an IntegrationInstance.
            - Use I(state=absent) to delete an IntegrationInstance.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create integration_instance
  oci_integration_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    integration_instance_type: STANDARD
    is_byol: true
    message_packs: 56

    # optional
    idcs_at: idcs_at_example
    consumption_model: UCM
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
    shape: DEVELOPMENT
    domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_file_server_enabled: true
    is_visual_builder_enabled: true
    custom_endpoint:
      # required
      hostname: hostname_example

      # optional
      certificate_secret_id: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
    alternate_custom_endpoints:
    - # required
      hostname: hostname_example

      # optional
      certificate_secret_id: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update integration_instance
  oci_integration_instance:
    # required
    integration_instance_id: "ocid1.integrationinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    integration_instance_type: STANDARD
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_byol: true
    message_packs: 56
    is_file_server_enabled: true
    is_visual_builder_enabled: true
    custom_endpoint:
      # required
      hostname: hostname_example

      # optional
      certificate_secret_id: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
    alternate_custom_endpoints:
    - # required
      hostname: hostname_example

      # optional
      certificate_secret_id: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update integration_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_integration_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    integration_instance_type: STANDARD
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_byol: true
    message_packs: 56
    is_file_server_enabled: true
    is_visual_builder_enabled: true
    custom_endpoint:
      # required
      hostname: hostname_example

      # optional
      certificate_secret_id: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
    alternate_custom_endpoints:
    - # required
      hostname: hostname_example

      # optional
      certificate_secret_id: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete integration_instance
  oci_integration_instance:
    # required
    integration_instance_id: "ocid1.integrationinstance.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete integration_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_integration_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.integration import IntegrationInstanceClient
    from oci.integration.models import CreateIntegrationInstanceDetails
    from oci.integration.models import UpdateIntegrationInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IntegrationInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(IntegrationInstanceHelperGen, self).get_possible_entity_types() + [
            "integrationinstance",
            "integrationinstances",
            "integrationintegrationinstance",
            "integrationintegrationinstances",
            "integrationinstanceresource",
            "integrationinstancesresource",
            "integration",
        ]

    def get_module_resource_id_param(self):
        return "integration_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("integration_instance_id")

    def get_get_fn(self):
        return self.client.get_integration_instance

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_integration_instance,
            integration_instance_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_integration_instance,
            integration_instance_id=self.module.params.get("integration_instance_id"),
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
            self.client.list_integration_instances, **kwargs
        )

    def get_create_model_class(self):
        return CreateIntegrationInstanceDetails

    def get_exclude_attributes(self):
        return ["domain_id", "idcs_at"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_integration_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(create_integration_instance_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateIntegrationInstanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_integration_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                integration_instance_id=self.module.params.get(
                    "integration_instance_id"
                ),
                update_integration_instance_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_integration_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                integration_instance_id=self.module.params.get(
                    "integration_instance_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


IntegrationInstanceHelperCustom = get_custom_class("IntegrationInstanceHelperCustom")


class ResourceHelper(IntegrationInstanceHelperCustom, IntegrationInstanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            idcs_at=dict(type="str"),
            consumption_model=dict(type="str", choices=["UCM", "GOV", "OIC4SAAS"]),
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
            shape=dict(type="str", choices=["DEVELOPMENT", "PRODUCTION"]),
            domain_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            integration_instance_type=dict(
                type="str",
                choices=["STANDARD", "ENTERPRISE", "STANDARDX", "ENTERPRISEX"],
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            is_byol=dict(type="bool"),
            message_packs=dict(type="int"),
            is_file_server_enabled=dict(type="bool"),
            is_visual_builder_enabled=dict(type="bool"),
            custom_endpoint=dict(
                type="dict",
                options=dict(
                    hostname=dict(type="str", required=True),
                    certificate_secret_id=dict(type="str"),
                ),
            ),
            alternate_custom_endpoints=dict(
                type="list",
                elements="dict",
                options=dict(
                    hostname=dict(type="str", required=True),
                    certificate_secret_id=dict(type="str"),
                ),
            ),
            integration_instance_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
