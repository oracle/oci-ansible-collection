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
module: oci_golden_gate_deployment
short_description: Manage a Deployment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Deployment resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Deployment.
    - "This resource has the following action operations in the M(oracle.oci.oci_golden_gate_deployment_actions) module: change_compartment, start, stop,
      upgrade."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    deployment_backup_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup being referenced.
        type: str
    deployment_type:
        description:
            - The deployment type.
            - Required for create using I(state=present).
        type: str
        choices:
            - "OGG"
    display_name:
        description:
            - An object's Display Name.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    license_model:
        description:
            - The Oracle license model that applies to a Deployment.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    description:
        description:
            - Metadata about this specific object.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Tags defined for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    nsg_ids:
        description:
            - An array of L(Network Security Group,https://docs.cloud.oracle.com/Content/Network/Concepts/networksecuritygroups.htm) OCIDs used to define
              network access for a deployment.
            - This parameter is updatable.
        type: list
        elements: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet being referenced.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    is_public:
        description:
            - True if this object is publicly available.
            - This parameter is updatable.
        type: bool
    fqdn:
        description:
            - A three-label Fully Qualified Domain Name (FQDN) for a resource.
            - This parameter is updatable.
        type: str
    cpu_core_count:
        description:
            - The Minimum number of OCPUs to be made available for this Deployment.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    is_auto_scaling_enabled:
        description:
            - Indicates if auto scaling is enabled for the Deployment's CPU core count.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: bool
    ogg_data:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            deployment_name:
                description:
                    - The name given to the GoldenGate service deployment. The name must be 1 to 32 characters long, must contain only alphanumeric characters
                      and must start with a letter.
                type: str
            admin_username:
                description:
                    - The GoldenGate deployment console username.
                    - This parameter is updatable.
                type: str
            admin_password:
                description:
                    - The password associated with the GoldenGate deployment console username. The password must be 8 to 30 characters long and must contain at
                      least 1 uppercase, 1 lowercase, 1 numeric, and 1 special character. Special characters such as '$', '^', or '?' are not allowed.
                    - This parameter is updatable.
                type: str
            certificate:
                description:
                    - A PEM-encoded SSL certificate.
                    - This parameter is updatable.
                type: str
            key:
                description:
                    - A PEM-encoded private key.
                    - This parameter is updatable.
                type: str
    deployment_id:
        description:
            - A unique Deployment identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Deployment.
            - Use I(state=present) to create or update a Deployment.
            - Use I(state=absent) to delete a Deployment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create deployment
  oci_golden_gate_deployment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_type: OGG
    display_name: display_name_example
    license_model: LICENSE_INCLUDED
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    cpu_core_count: 56
    is_auto_scaling_enabled: true

    # optional
    deployment_backup_id: "ocid1.deploymentbackup.oc1..xxxxxxEXAMPLExxxxxx"
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    nsg_ids: [ "nsg_ids_example" ]
    is_public: true
    fqdn: fqdn_example
    ogg_data:
      # optional
      deployment_name: deployment_name_example
      admin_username: admin_username_example
      admin_password: example-password
      certificate: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
      key: key_example

- name: Update deployment
  oci_golden_gate_deployment:
    # required
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    license_model: LICENSE_INCLUDED
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    nsg_ids: [ "nsg_ids_example" ]
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    is_public: true
    fqdn: fqdn_example
    cpu_core_count: 56
    is_auto_scaling_enabled: true
    ogg_data:
      # optional
      deployment_name: deployment_name_example
      admin_username: admin_username_example
      admin_password: example-password
      certificate: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
      key: key_example

- name: Update deployment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_golden_gate_deployment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    license_model: LICENSE_INCLUDED
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    nsg_ids: [ "nsg_ids_example" ]
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    is_public: true
    fqdn: fqdn_example
    cpu_core_count: 56
    is_auto_scaling_enabled: true
    ogg_data:
      # optional
      deployment_name: deployment_name_example
      admin_username: admin_username_example
      admin_password: example-password
      certificate: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
      key: key_example

- name: Delete deployment
  oci_golden_gate_deployment:
    # required
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete deployment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_golden_gate_deployment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
deployment:
    description:
        - Details of the Deployment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - An object's Display Name.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Metadata about this specific object.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_backup_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup being referenced.
            returned: on success
            type: str
            sample: "ocid1.deploymentbackup.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the resource was created. The format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339), such as
                  `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the resource was last updated. The format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339), such as
                  `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - Possible lifecycle states.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_sub_state:
            description:
                - Possible GGS lifecycle sub-states.
            returned: on success
            type: str
            sample: RECOVERING
        lifecycle_details:
            description:
                - Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed
                  state.
            returned: on success
            type: str
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
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        fqdn:
            description:
                - A three-label Fully Qualified Domain Name (FQDN) for a resource.
            returned: on success
            type: str
            sample: fqdn_example
        license_model:
            description:
                - The Oracle license model that applies to a Deployment.
            returned: on success
            type: str
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
            type: str
            sample: public_ip_address_example
        private_ip_address:
            description:
                - The private IP address in the customer's VCN representing the access point for the associated endpoint service in the GoldenGate service VCN.
            returned: on success
            type: str
            sample: private_ip_address_example
        deployment_url:
            description:
                - The URL of a resource.
            returned: on success
            type: str
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
        time_upgrade_required:
            description:
                - The date the existing version in use will no longer be considered as usable and an upgrade will be required.  This date is typically 6 months
                  after the version was released for use by GGS.  The format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339), such as
                  `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        storage_utilization_in_bytes:
            description:
                - The amount of storage being utilized (in bytes)
            returned: on success
            type: int
            sample: 56
        is_storage_utilization_limit_exceeded:
            description:
                - Indicator will be true if the amount of storage being utilized exceeds the allowable storage utilization limit.  Exceeding the limit may be an
                  indication of a misconfiguration of the deployment's GoldenGate service.
            returned: on success
            type: bool
            sample: true
        deployment_type:
            description:
                - The deployment type.
            returned: on success
            type: str
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
                    type: str
                    sample: deployment_name_example
                admin_username:
                    description:
                        - The GoldenGate deployment console username.
                    returned: on success
                    type: str
                    sample: admin_username_example
                ogg_version:
                    description:
                        - Version of OGG
                    returned: on success
                    type: str
                    sample: ogg_version_example
                certificate:
                    description:
                        - A PEM-encoded SSL certificate.
                    returned: on success
                    type: str
                    sample: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "deployment_backup_id": "ocid1.deploymentbackup.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_sub_state": "RECOVERING",
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
        "time_upgrade_required": "2013-10-20T19:20:30+01:00",
        "storage_utilization_in_bytes": 56,
        "is_storage_utilization_limit_exceeded": true,
        "deployment_type": "OGG",
        "ogg_data": {
            "deployment_name": "deployment_name_example",
            "admin_username": "admin_username_example",
            "ogg_version": "ogg_version_example",
            "certificate": "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
        }
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
    from oci.golden_gate import GoldenGateClient
    from oci.golden_gate.models import CreateDeploymentDetails
    from oci.golden_gate.models import UpdateDeploymentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeploymentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_default_module_wait_timeout(self):
        return 3600

    def get_possible_entity_types(self):
        return super(DeploymentHelperGen, self).get_possible_entity_types() + [
            "goldengatedeployment",
            "goldengatedeployments",
            "goldenGategoldengatedeployment",
            "goldenGategoldengatedeployments",
            "goldengatedeploymentresource",
            "goldengatedeploymentsresource",
            "deployment",
            "deployments",
            "goldenGatedeployment",
            "goldenGatedeployments",
            "deploymentresource",
            "deploymentsresource",
            "goldengate",
        ]

    def get_module_resource_id_param(self):
        return "deployment_id"

    def get_module_resource_id(self):
        return self.module.params.get("deployment_id")

    def get_get_fn(self):
        return self.client.get_deployment

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment, deployment_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment,
            deployment_id=self.module.params.get("deployment_id"),
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
            else ["display_name", "fqdn"]
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
        return oci_common_utils.list_all_resources(
            self.client.list_deployments, **kwargs
        )

    def get_create_model_class(self):
        return CreateDeploymentDetails

    def get_exclude_attributes(self):
        return ["ogg_data.admin_password", "ogg_data.key"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(create_deployment_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDeploymentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                update_deployment_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(deployment_id=self.module.params.get("deployment_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DeploymentHelperCustom = get_custom_class("DeploymentHelperCustom")


class ResourceHelper(DeploymentHelperCustom, DeploymentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            deployment_backup_id=dict(type="str"),
            deployment_type=dict(type="str", choices=["OGG"]),
            display_name=dict(aliases=["name"], type="str"),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            nsg_ids=dict(type="list", elements="str"),
            subnet_id=dict(type="str"),
            is_public=dict(type="bool"),
            fqdn=dict(type="str"),
            cpu_core_count=dict(type="int"),
            is_auto_scaling_enabled=dict(type="bool"),
            ogg_data=dict(
                type="dict",
                options=dict(
                    deployment_name=dict(type="str"),
                    admin_username=dict(type="str"),
                    admin_password=dict(type="str", no_log=True),
                    certificate=dict(type="str"),
                    key=dict(type="str", no_log=True),
                ),
            ),
            deployment_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deployment",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
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
