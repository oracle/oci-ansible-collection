#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_golden_gate_deployment_facts
short_description: Fetches details about one or multiple Deployment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Deployment resources in Oracle Cloud Infrastructure
    - Lists the Deployments in a compartment.
    - If I(deployment_id) is specified, the details of a single Deployment will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    deployment_id:
        description:
            - A unique Deployment identifier.
            - Required to get a specific deployment.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple deployments.
        type: str
    lifecycle_state:
        description:
            - A filter to return only the resources that match the 'lifecycleState' given.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only the resources that match the entire 'displayName' given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending.  Default order for 'displayName' is
              ascending. If no value is specified timeCreated is the default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List deployments
  oci_golden_gate_deployment_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific deployment
  oci_golden_gate_deployment_facts:
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
deployments:
    description:
        - List of Deployment resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - An object's Display Name.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - Metadata about this specific object.
            returned: on success
            type: string
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_backup_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup being referenced.
            returned: on success
            type: string
            sample: "ocid1.deploymentbackup.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the resource was created. The format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339), such as
                  `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time the resource was last updated. The format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339), such as
                  `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - Possible lifecycle states.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed
                  state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - "A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Tags defined for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        is_healthy:
            description:
                - True if all of the aggregate resources are working correctly.
            returned: on success
            type: bool
            sample: true
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet being referenced.
            returned: on success
            type: string
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        fqdn:
            description:
                - A three-label Fully Qualified Domain Name (FQDN) for a resource.
            returned: on success
            type: string
            sample: fqdn_example
        license_model:
            description:
                - The Oracle license model that applies to a Deployment.
            returned: on success
            type: string
            sample: LICENSE_INCLUDED
        cpu_core_count:
            description:
                - The Minimum number of OCPUs to be made available for this Deployment.
            returned: on success
            type: int
            sample: 56
        is_auto_scaling_enabled:
            description:
                - Indicates if auto scaling is enabled for the Deployment's CPU core count.
            returned: on success
            type: bool
            sample: true
        nsg_ids:
            description:
                - An array of L(Network Security Group,https://docs.cloud.oracle.com/Content/Network/Concepts/networksecuritygroups.htm) OCIDs used to define
                  network access for a deployment.
            returned: on success
            type: list
            sample: []
        is_public:
            description:
                - True if this object is publicly available.
            returned: on success
            type: bool
            sample: true
        public_ip_address:
            description:
                - The public IP address representing the access point for the Deployment.
            returned: on success
            type: string
            sample: public_ip_address_example
        private_ip_address:
            description:
                - The private IP address in the customer's VCN representing the access point for the associated endpoint service in the GoldenGate service VCN.
            returned: on success
            type: string
            sample: private_ip_address_example
        deployment_url:
            description:
                - The URL of a resource.
            returned: on success
            type: string
            sample: deployment_url_example
        system_tags:
            description:
                - "The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is
                  predefined and scoped to namespaces.  For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
        is_latest_version:
            description:
                - Indicates if the resource is the the latest available version.
            returned: on success
            type: bool
            sample: true
        deployment_type:
            description:
                - The deployment type.
            returned: on success
            type: string
            sample: OGG
        ogg_data:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                deployment_name:
                    description:
                        - The name given to the GoldenGate service deployment. The name must be 1 to 32 characters long, must contain only alphanumeric
                          characters and must start with a letter.
                    returned: on success
                    type: string
                    sample: deployment_name_example
                admin_username:
                    description:
                        - The GoldenGate deployment console username.
                    returned: on success
                    type: string
                    sample: oggadmin
                certificate:
                    description:
                        - A PEM-encoded SSL certificate.
                    returned: on success
                    type: string
                    sample: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "deployment_backup_id": "ocid1.deploymentbackup.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "is_healthy": true,
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "fqdn": "fqdn_example",
        "license_model": "LICENSE_INCLUDED",
        "cpu_core_count": 56,
        "is_auto_scaling_enabled": true,
        "nsg_ids": [],
        "is_public": true,
        "public_ip_address": "public_ip_address_example",
        "private_ip_address": "private_ip_address_example",
        "deployment_url": "deployment_url_example",
        "system_tags": {},
        "is_latest_version": true,
        "deployment_type": "OGG",
        "ogg_data": {
            "deployment_name": "deployment_name_example",
            "admin_username": "oggadmin",
            "certificate": "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
        }
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.golden_gate import GoldenGateClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeploymentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "deployment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment,
            deployment_id=self.module.params.get("deployment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_deployments,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DeploymentFactsHelperCustom = get_custom_class("DeploymentFactsHelperCustom")


class ResourceFactsHelper(DeploymentFactsHelperCustom, DeploymentFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            deployment_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="deployment",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(deployments=result)


if __name__ == "__main__":
    main()
