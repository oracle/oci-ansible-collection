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
module: oci_service_mesh_ingress_gateway
short_description: Manage an IngressGateway resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an IngressGateway resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new IngressGateway.
    - "This resource has the following action operations in the M(oracle.oci.oci_service_mesh_ingress_gateway_actions) module: change_compartment."
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
            - The OCID of the service mesh in which this ingress gateway is created.
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
    hosts:
        description:
            - An array of hostnames and their listener configuration that this gateway will bind to.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - A user-friendly name for the host. The name must be unique within the same ingress gateway.
                      This name can be used in the ingress gateway route table resource to attach a route to this host.
                    - "Example: `MyExampleHost`"
                type: str
                required: true
            hostnames:
                description:
                    - "Hostnames of the host. Applicable only for HTTP and TLS_PASSTHROUGH listeners.
                      Wildcard hostnames are supported in the prefix form.
                      Examples of valid hostnames are \\"www.example.com\\", \\"*.example.com\\", \\"*.com\\"."
                type: list
                elements: str
            listeners:
                description:
                    - The listeners for the ingress gateway.
                type: list
                elements: dict
                required: true
                suboptions:
                    protocol:
                        description:
                            - Type of protocol used.
                        type: str
                        choices:
                            - "HTTP"
                            - "TLS_PASSTHROUGH"
                            - "TCP"
                        required: true
                    port:
                        description:
                            - Port on which ingress gateway is listening.
                        type: int
                        required: true
                    tls:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            mode:
                                description:
                                    - "DISABLED: Connection can only be plaintext.
                                      PERMISSIVE: Connection can be either plaintext or TLS/mTLS. If the clientValidation.trustedCaBundle property is configured
                                      for the listener, mTLS is performed and the client's certificates are validated by the gateway.
                                      TLS: Connection can only be TLS.
                                      MUTUAL_TLS: Connection can only be MTLS."
                                type: str
                                choices:
                                    - "DISABLED"
                                    - "PERMISSIVE"
                                    - "TLS"
                                    - "MUTUAL_TLS"
                                required: true
                            server_certificate:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    certificate_id:
                                        description:
                                            - The OCID of the leaf certificate resource.
                                            - Applicable when type is 'OCI_CERTIFICATES'
                                        type: str
                                    type:
                                        description:
                                            - Type of certificate.
                                        type: str
                                        choices:
                                            - "OCI_CERTIFICATES"
                                            - "LOCAL_FILE"
                                        required: true
                                    secret_name:
                                        description:
                                            - "Name of the secret.
                                              For Kubernetes this is the name of the Kubernetes secret of type tls.
                                              For other platforms the secrets must be mounted at: /etc/oci/secrets/${secretName}/tls.{key,crt}"
                                            - Applicable when type is 'LOCAL_FILE'
                                        type: str
                            client_validation:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    trusted_ca_bundle:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            secret_name:
                                                description:
                                                    - "Name of the secret.
                                                      For Kubernetes this will be the name of an opaque Kubernetes secret with key ca.crt.
                                                      For other platforms the secret must be mounted at: /etc/oci/secrets/${secretName}/ca.crt"
                                                    - Applicable when type is 'LOCAL_FILE'
                                                type: str
                                            type:
                                                description:
                                                    - Type of certificate.
                                                type: str
                                                choices:
                                                    - "LOCAL_FILE"
                                                    - "OCI_CERTIFICATES"
                                                required: true
                                            ca_bundle_id:
                                                description:
                                                    - The OCID of the CA Bundle resource.
                                                    - Applicable when type is 'OCI_CERTIFICATES'
                                                type: str
                                    subject_alternate_names:
                                        description:
                                            - A list of alternate names to verify the subject identity in the certificate presented by the client.
                                        type: list
                                        elements: str
    access_logging:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            is_enabled:
                description:
                    - Determines if the logging configuration is enabled.
                type: bool
    mtls:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            maximum_validity:
                description:
                    - The number of days the mTLS certificate is valid.  This value should be less than the Maximum Validity Duration
                      for Certificates (Days) setting on the Certificate Authority associated with this Mesh.  The certificate will
                      be automatically renewed after 2/3 of the validity period, so a certificate with a maximum validity of 45 days
                      will be renewed every 30 days.
                type: int
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
    ingress_gateway_id:
        description:
            - Unique IngressGateway identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the IngressGateway.
            - Use I(state=present) to create or update an IngressGateway.
            - Use I(state=absent) to delete an IngressGateway.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create ingress_gateway
  oci_service_mesh_ingress_gateway:
    # required
    name: name_example
    mesh_id: "ocid1.mesh.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    hosts:
    - # required
      name: name_example
      listeners:
      - # required
        protocol: HTTP
        port: 56

        # optional
        tls:
          # required
          mode: DISABLED

          # optional
          server_certificate:
            # required
            type: OCI_CERTIFICATES

            # optional
            certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
          client_validation:
            # optional
            trusted_ca_bundle:
              # required
              type: LOCAL_FILE

              # optional
              secret_name: secret_name_example
            subject_alternate_names: [ "subject_alternate_names_example" ]

      # optional
      hostnames: [ "hostnames_example" ]

    # optional
    description: description_example
    access_logging:
      # optional
      is_enabled: true
    mtls:
      # optional
      maximum_validity: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update ingress_gateway
  oci_service_mesh_ingress_gateway:
    # required
    ingress_gateway_id: "ocid1.ingressgateway.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    hosts:
    - # required
      name: name_example
      listeners:
      - # required
        protocol: HTTP
        port: 56

        # optional
        tls:
          # required
          mode: DISABLED

          # optional
          server_certificate:
            # required
            type: OCI_CERTIFICATES

            # optional
            certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
          client_validation:
            # optional
            trusted_ca_bundle:
              # required
              type: LOCAL_FILE

              # optional
              secret_name: secret_name_example
            subject_alternate_names: [ "subject_alternate_names_example" ]

      # optional
      hostnames: [ "hostnames_example" ]
    access_logging:
      # optional
      is_enabled: true
    mtls:
      # optional
      maximum_validity: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update ingress_gateway using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_service_mesh_ingress_gateway:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    hosts:
    - # required
      name: name_example
      listeners:
      - # required
        protocol: HTTP
        port: 56

        # optional
        tls:
          # required
          mode: DISABLED

          # optional
          server_certificate:
            # required
            type: OCI_CERTIFICATES

            # optional
            certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
          client_validation:
            # optional
            trusted_ca_bundle:
              # required
              type: LOCAL_FILE

              # optional
              secret_name: secret_name_example
            subject_alternate_names: [ "subject_alternate_names_example" ]

      # optional
      hostnames: [ "hostnames_example" ]
    access_logging:
      # optional
      is_enabled: true
    mtls:
      # optional
      maximum_validity: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete ingress_gateway
  oci_service_mesh_ingress_gateway:
    # required
    ingress_gateway_id: "ocid1.ingressgateway.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete ingress_gateway using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_service_mesh_ingress_gateway:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
ingress_gateway:
    description:
        - Details of the IngressGateway resource acted upon by the current operation
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
                - The OCID of the service mesh in which this ingress gateway is created.
            returned: on success
            type: str
            sample: "ocid1.mesh.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
        hosts:
            description:
                - Array of hostnames and their listener configuration that this gateway will bind to.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - A user-friendly name for the host. The name must be unique within the same ingress gateway.
                          This name can be used in the ingress gateway route table resource to attach a route to this host.
                        - "Example: `MyExampleHost`"
                    returned: on success
                    type: str
                    sample: name_example
                hostnames:
                    description:
                        - "Hostnames of the host. Applicable only for HTTP and TLS_PASSTHROUGH listeners.
                          Wildcard hostnames are supported in the prefix form.
                          Examples of valid hostnames are \\"www.example.com\\", \\"*.example.com\\", \\"*.com\\"."
                    returned: on success
                    type: list
                    sample: []
                listeners:
                    description:
                        - The listeners for the ingress gateway.
                    returned: on success
                    type: complex
                    contains:
                        protocol:
                            description:
                                - Type of protocol used.
                            returned: on success
                            type: str
                            sample: HTTP
                        port:
                            description:
                                - Port on which ingress gateway is listening.
                            returned: on success
                            type: int
                            sample: 56
                        tls:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                mode:
                                    description:
                                        - "DISABLED: Connection can only be plaintext.
                                          PERMISSIVE: Connection can be either plaintext or TLS/mTLS. If the clientValidation.trustedCaBundle property is
                                          configured for the listener, mTLS is performed and the client's certificates are validated by the gateway.
                                          TLS: Connection can only be TLS.
                                          MUTUAL_TLS: Connection can only be MTLS."
                                    returned: on success
                                    type: str
                                    sample: DISABLED
                                server_certificate:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        secret_name:
                                            description:
                                                - "Name of the secret.
                                                  For Kubernetes this is the name of the Kubernetes secret of type tls.
                                                  For other platforms the secrets must be mounted at: /etc/oci/secrets/${secretName}/tls.{key,crt}"
                                            returned: on success
                                            type: str
                                            sample: secret_name_example
                                        type:
                                            description:
                                                - Type of certificate.
                                            returned: on success
                                            type: str
                                            sample: OCI_CERTIFICATES
                                        certificate_id:
                                            description:
                                                - The OCID of the leaf certificate resource.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
                                client_validation:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        trusted_ca_bundle:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                secret_name:
                                                    description:
                                                        - "Name of the secret.
                                                          For Kubernetes this will be the name of an opaque Kubernetes secret with key ca.crt.
                                                          For other platforms the secret must be mounted at: /etc/oci/secrets/${secretName}/ca.crt"
                                                    returned: on success
                                                    type: str
                                                    sample: secret_name_example
                                                type:
                                                    description:
                                                        - Type of certificate.
                                                    returned: on success
                                                    type: str
                                                    sample: OCI_CERTIFICATES
                                                ca_bundle_id:
                                                    description:
                                                        - The OCID of the CA Bundle resource.
                                                    returned: on success
                                                    type: str
                                                    sample: "ocid1.cabundle.oc1..xxxxxxEXAMPLExxxxxx"
                                        subject_alternate_names:
                                            description:
                                                - A list of alternate names to verify the subject identity in the certificate presented by the client.
                                            returned: on success
                                            type: list
                                            sample: []
        mtls:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                certificate_id:
                    description:
                        - The OCID of the certificate resource that will be used for mTLS authentication with other virtual services in the mesh.
                    returned: on success
                    type: str
                    sample: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
                maximum_validity:
                    description:
                        - The number of days the mTLS certificate is valid.  This value should be less than the Maximum Validity Duration
                          for Certificates (Days) setting on the Certificate Authority associated with this Mesh.  The certificate will
                          be automatically renewed after 2/3 of the validity period, so a certificate with a maximum validity of 45 days
                          will be renewed every 30 days.
                    returned: on success
                    type: int
                    sample: 56
        access_logging:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_enabled:
                    description:
                        - Determines if the logging configuration is enabled.
                    returned: on success
                    type: bool
                    sample: true
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
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "hosts": [{
            "name": "name_example",
            "hostnames": [],
            "listeners": [{
                "protocol": "HTTP",
                "port": 56,
                "tls": {
                    "mode": "DISABLED",
                    "server_certificate": {
                        "secret_name": "secret_name_example",
                        "type": "OCI_CERTIFICATES",
                        "certificate_id": "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
                    },
                    "client_validation": {
                        "trusted_ca_bundle": {
                            "secret_name": "secret_name_example",
                            "type": "OCI_CERTIFICATES",
                            "ca_bundle_id": "ocid1.cabundle.oc1..xxxxxxEXAMPLExxxxxx"
                        },
                        "subject_alternate_names": []
                    }
                }
            }]
        }],
        "mtls": {
            "certificate_id": "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx",
            "maximum_validity": 56
        },
        "access_logging": {
            "is_enabled": true
        },
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.service_mesh import ServiceMeshClient
    from oci.service_mesh.models import CreateIngressGatewayDetails
    from oci.service_mesh.models import UpdateIngressGatewayDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IngressGatewayHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(IngressGatewayHelperGen, self).get_possible_entity_types() + [
            "ingressgateway",
            "ingressgateways",
            "serviceMeshingressgateway",
            "serviceMeshingressgateways",
            "ingressgatewayresource",
            "ingressgatewaysresource",
            "servicemesh",
        ]

    def get_module_resource_id_param(self):
        return "ingress_gateway_id"

    def get_module_resource_id(self):
        return self.module.params.get("ingress_gateway_id")

    def get_get_fn(self):
        return self.client.get_ingress_gateway

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_ingress_gateway, ingress_gateway_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ingress_gateway,
            ingress_gateway_id=self.module.params.get("ingress_gateway_id"),
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
            self.client.list_ingress_gateways, **kwargs
        )

    def get_create_model_class(self):
        return CreateIngressGatewayDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_ingress_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(create_ingress_gateway_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateIngressGatewayDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_ingress_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingress_gateway_id=self.module.params.get("ingress_gateway_id"),
                update_ingress_gateway_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_ingress_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingress_gateway_id=self.module.params.get("ingress_gateway_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


IngressGatewayHelperCustom = get_custom_class("IngressGatewayHelperCustom")


class ResourceHelper(IngressGatewayHelperCustom, IngressGatewayHelperGen):
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
            hosts=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    hostnames=dict(type="list", elements="str"),
                    listeners=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            protocol=dict(
                                type="str",
                                required=True,
                                choices=["HTTP", "TLS_PASSTHROUGH", "TCP"],
                            ),
                            port=dict(type="int", required=True),
                            tls=dict(
                                type="dict",
                                options=dict(
                                    mode=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "DISABLED",
                                            "PERMISSIVE",
                                            "TLS",
                                            "MUTUAL_TLS",
                                        ],
                                    ),
                                    server_certificate=dict(
                                        type="dict",
                                        options=dict(
                                            certificate_id=dict(type="str"),
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=[
                                                    "OCI_CERTIFICATES",
                                                    "LOCAL_FILE",
                                                ],
                                            ),
                                            secret_name=dict(type="str"),
                                        ),
                                    ),
                                    client_validation=dict(
                                        type="dict",
                                        options=dict(
                                            trusted_ca_bundle=dict(
                                                type="dict",
                                                options=dict(
                                                    secret_name=dict(type="str"),
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "LOCAL_FILE",
                                                            "OCI_CERTIFICATES",
                                                        ],
                                                    ),
                                                    ca_bundle_id=dict(type="str"),
                                                ),
                                            ),
                                            subject_alternate_names=dict(
                                                type="list", elements="str"
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            access_logging=dict(
                type="dict", options=dict(is_enabled=dict(type="bool"))
            ),
            mtls=dict(type="dict", options=dict(maximum_validity=dict(type="int"))),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            ingress_gateway_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ingress_gateway",
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
