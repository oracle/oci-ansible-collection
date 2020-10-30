#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_apigateway_waas_certificate_facts
short_description: Fetches details about one or multiple WaasCertificate resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple WaasCertificate resources in Oracle Cloud Infrastructure
    - Returns a list of certificates.
    - If I(certificate_id) is specified, the details of a single WaasCertificate will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    certificate_id:
        description:
            - The ocid of the certificate.
            - Required to get a specific waas_certificate.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ocid of the compartment in which to list resources.
            - Required to list multiple waas_certificates.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state.
            - "Example: `ACTIVE` or `DELETED`"
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'. The default order depends on the sortBy value.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`).
              Default order for `timeCreated` is descending. Default order for
              `displayName` is ascending. The `displayName` sort order is case
              sensitive.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List waas_certificates
  oci_apigateway_waas_certificate_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific waas_certificate
  oci_apigateway_waas_certificate_facts:
    certificate_id: ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
waas_certificates:
    description:
        - List of WaasCertificate resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
                - "Example: `My new resource`"
            returned: on success
            type: string
            sample: My new resource
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the
                  resource is created.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        subject_names:
            description:
                - The entity to be secured by the certificate and additional host names.
            returned: on success
            type: list
            sample: []
        time_not_valid_after:
            description:
                - The date and time the certificate will expire.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        certificate:
            description:
                - The data of the leaf certificate in pem format.
            returned: on success
            type: string
            sample: certificate_example
        intermediate_certificates:
            description:
                - The intermediate certificate data associated with the certificate in pem format.
            returned: on success
            type: string
            sample: intermediate_certificates_example
        time_created:
            description:
                - The time this resource was created. An RFC3339 formatted datetime string.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time this resource was last updated. An RFC3339 formatted datetime string.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the certificate.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a
                  resource in a Failed state.
            returned: on success
            type: string
            sample: lifecycle_details_example
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
        items:
            description:
                - Certificate summaries.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                display_name:
                    description:
                        - A user-friendly name. Does not have to be unique, and it's changeable.
                          Avoid entering confidential information.
                        - "Example: `My new resource`"
                    returned: on success
                    type: string
                    sample: My new resource
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the
                          resource is created.
                    returned: on success
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
                subject_names:
                    description:
                        - The entity to be secured by the certificate and additional host names.
                    returned: on success
                    type: list
                    sample: []
                time_not_valid_after:
                    description:
                        - The date and time the certificate will expire.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                time_created:
                    description:
                        - The time this resource was created. An RFC3339 formatted datetime string.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                time_updated:
                    description:
                        - The time this resource was last updated. An RFC3339 formatted datetime string.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                lifecycle_state:
                    description:
                        - The current state of the certificate.
                    returned: on success
                    type: string
                    sample: lifecycle_state_example
                lifecycle_details:
                    description:
                        - A message describing the current state in more detail.
                          For example, can be used to provide actionable information for a
                          resource in a Failed state.
                    returned: on success
                    type: string
                    sample: lifecycle_details_example
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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "My new resource",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "subject_names": [],
        "time_not_valid_after": "2013-10-20T19:20:30+01:00",
        "certificate": "certificate_example",
        "intermediate_certificates": "intermediate_certificates_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "items": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "My new resource",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "subject_names": [],
            "time_not_valid_after": "2013-10-20T19:20:30+01:00",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "lifecycle_state": "lifecycle_state_example",
            "lifecycle_details": "lifecycle_details_example",
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}}
        }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.apigateway import ApiGatewayClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewayWaasCertificateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "certificate_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate,
            certificate_id=self.module.params.get("certificate_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_certificates,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ApigatewayWaasCertificateFactsHelperCustom = get_custom_class(
    "ApigatewayWaasCertificateFactsHelperCustom"
)


class ResourceFactsHelper(
    ApigatewayWaasCertificateFactsHelperCustom, ApigatewayWaasCertificateFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            certificate_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="waas_certificate",
        service_client_class=ApiGatewayClient,
        namespace="apigateway",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(waas_certificates=result)


if __name__ == "__main__":
    main()
