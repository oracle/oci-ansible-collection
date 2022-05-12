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
module: oci_service_mesh_ingress_gateway_facts
short_description: Fetches details about one or multiple IngressGateway resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple IngressGateway resources in Oracle Cloud Infrastructure
    - Returns a list of IngressGateway objects.
    - If I(ingress_gateway_id) is specified, the details of a single IngressGateway will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ingress_gateway_id:
        description:
            - Unique IngressGateway identifier.
            - Required to get a specific ingress_gateway.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple ingress_gateways.
        type: str
    name:
        description:
            - A filter to return only resources that match the entire name given.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for 'timeCreated' is descending. Default order for 'name' is ascending.
        type: str
        choices:
            - "id"
            - "timeCreated"
            - "name"
    mesh_id:
        description:
            - Unique Mesh identifier.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources that match the life cycle state given.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific ingress_gateway
  oci_service_mesh_ingress_gateway_facts:
    # required
    ingress_gateway_id: "ocid1.ingressgateway.oc1..xxxxxxEXAMPLExxxxxx"

- name: List ingress_gateways
  oci_service_mesh_ingress_gateway_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_order: ASC
    sort_by: id
    mesh_id: "ocid1.mesh.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: lifecycle_state_example

"""

RETURN = """
ingress_gateways:
    description:
        - List of IngressGateway resources
    returned: on success
    type: complex
    contains:
        hosts:
            description:
                - Array of hostnames and their listener configuration that this gateway will bind to.
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                is_enabled:
                    description:
                        - Determines if the logging configuration is enabled.
                    returned: on success
                    type: bool
                    sample: true
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
        mesh_id:
            description:
                - The OCID of the service mesh in which this ingress gateway is created.
            returned: on success
            type: str
            sample: "ocid1.mesh.oc1..xxxxxxEXAMPLExxxxxx"
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
    sample: [{
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "mesh_id": "ocid1.mesh.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.service_mesh import ServiceMeshClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IngressGatewayFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "ingress_gateway_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ingress_gateway,
            ingress_gateway_id=self.module.params.get("ingress_gateway_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_order",
            "sort_by",
            "mesh_id",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_ingress_gateways,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


IngressGatewayFactsHelperCustom = get_custom_class("IngressGatewayFactsHelperCustom")


class ResourceFactsHelper(
    IngressGatewayFactsHelperCustom, IngressGatewayFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            ingress_gateway_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["id", "timeCreated", "name"]),
            mesh_id=dict(type="str"),
            lifecycle_state=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="ingress_gateway",
        service_client_class=ServiceMeshClient,
        namespace="service_mesh",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(ingress_gateways=result)


if __name__ == "__main__":
    main()
