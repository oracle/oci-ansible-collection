#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_golden_gate_deployment_actions
short_description: Perform actions on a Deployment resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Deployment resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the Deployment into a different compartment within the same tenancy.  When provided,
      If-Match is checked against ETag values of the resource.  For information about moving
      resources between compartments, see L(Moving Resources Between
      Compartments,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - For I(action=collect_deployment_diagnostic), collects the diagnostic of a Deployment. When provided, If-Match is checked against ETag values of the
      resource.
    - For I(action=deployment_wallet_exists), checks if a wallet is already present in the deployment. When provided, If-Match is checked against ETag values of
      the resource.
    - For I(action=export_deployment_wallet), export the OGG wallet from the deployment to OCI vault. When provided, If-Match is checked against ETag values of
      the resource.
    - For I(action=import_deployment_wallet), imports an OGG wallet from the OCI Vault to the Deployment. When provided, If-Match is checked against ETag values
      of the resource.
    - For I(action=start), starts a Deployment. When provided, If-Match is checked against ETag values of the resource.
    - For I(action=stop), stops a Deployment. When provided, If-Match is checked against ETag values of the resource.
    - For I(action=upgrade), upgrade a Deployment. When provided, If-Match is checked against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            - Required for I(action=change_compartment).
        type: str
    namespace_name:
        description:
            - Name of namespace that serves as a container for all of your buckets
            - Required for I(action=collect_deployment_diagnostic).
        type: str
    bucket_name:
        description:
            - Name of the bucket where the object is to be uploaded in the object storage
            - Required for I(action=collect_deployment_diagnostic).
        type: str
    diagnostic_name_prefix:
        description:
            - Prefix of the diagnostic collected and uploaded to object storage
            - Required for I(action=collect_deployment_diagnostic).
        type: str
    time_diagnostic_start:
        description:
            - The time from which the diagnostic collection should collect the logs. The format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339),
              such as `2016-08-25T21:10:29.600Z`.
            - Applicable only for I(action=collect_deployment_diagnostic).
        type: str
    time_diagnostic_end:
        description:
            - The time until which the diagnostic collection should collect the logs. The format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339),
              such as `2016-08-25T21:10:29.600Z`.
            - Applicable only for I(action=collect_deployment_diagnostic).
        type: str
    secret_name:
        description:
            - Name of the secret with which secret is shown in vault
            - Required for I(action=export_deployment_wallet).
        type: str
    vault_id:
        description:
            - Refers to the customer's vault OCID.
              If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate
              to manage secrets contained within this vault.
            - Required for I(action=export_deployment_wallet), I(action=import_deployment_wallet).
        type: str
    new_wallet_secret_id:
        description:
            - The OCID of the customer's GoldenGate Service Secret.
              If provided, it references a key that customers will be required to ensure the policies are established
              to permit GoldenGate to use this Secret.
            - Required for I(action=import_deployment_wallet).
        type: str
    wallet_backup_secret_name:
        description:
            - Name of the secret with which secret is shown in vault
            - Applicable only for I(action=import_deployment_wallet).
        type: str
    master_encryption_key_id:
        description:
            - Refers to the customer's master key OCID.
              If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.
            - Required for I(action=export_deployment_wallet).
        type: str
    description:
        description:
            - Metadata about this specific object.
            - Applicable only for I(action=export_deployment_wallet)I(action=import_deployment_wallet).
        type: str
    deployment_id:
        description:
            - A unique Deployment identifier.
        type: str
        aliases: ["id"]
        required: true
    ogg_version:
        description:
            - Version of OGG
            - Applicable only for I(action=upgrade).
            - Required when type is 'SPECIFIC_RELEASE'
        type: str
    type:
        description:
            - The type of a deployment for wallet
            - Required for I(action=deployment_wallet_exists), I(action=start), I(action=stop), I(action=upgrade).
        type: str
        choices:
            - "DEFAULT"
            - "SPECIFIC_RELEASE"
            - "CURRENT_RELEASE"
    action:
        description:
            - The action to perform on the Deployment.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "collect_deployment_diagnostic"
            - "deployment_wallet_exists"
            - "export_deployment_wallet"
            - "import_deployment_wallet"
            - "start"
            - "stop"
            - "upgrade"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on deployment
  oci_golden_gate_deployment_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action collect_deployment_diagnostic on deployment
  oci_golden_gate_deployment_actions:
    # required
    namespace_name: namespace_name_example
    bucket_name: bucket_name_example
    diagnostic_name_prefix: diagnostic_name_prefix_example
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    action: collect_deployment_diagnostic

    # optional
    time_diagnostic_start: time_diagnostic_start_example
    time_diagnostic_end: time_diagnostic_end_example

- name: Perform action deployment_wallet_exists on deployment with type = DEFAULT
  oci_golden_gate_deployment_actions:
    # required
    type: DEFAULT

- name: Perform action deployment_wallet_exists on deployment with type = SPECIFIC_RELEASE
  oci_golden_gate_deployment_actions:
    # required
    type: SPECIFIC_RELEASE

- name: Perform action deployment_wallet_exists on deployment with type = CURRENT_RELEASE
  oci_golden_gate_deployment_actions:
    # required
    type: CURRENT_RELEASE

- name: Perform action export_deployment_wallet on deployment
  oci_golden_gate_deployment_actions:
    # required
    secret_name: secret_name_example
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    master_encryption_key_id: "ocid1.masterencryptionkey.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    action: export_deployment_wallet

    # optional
    description: description_example

- name: Perform action import_deployment_wallet on deployment
  oci_golden_gate_deployment_actions:
    # required
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    new_wallet_secret_id: "ocid1.newwalletsecret.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    action: import_deployment_wallet

    # optional
    wallet_backup_secret_name: wallet_backup_secret_name_example
    master_encryption_key_id: "ocid1.masterencryptionkey.oc1..xxxxxxEXAMPLExxxxxx"
    description: description_example

- name: Perform action start on deployment with type = DEFAULT
  oci_golden_gate_deployment_actions:
    # required
    type: DEFAULT

- name: Perform action start on deployment with type = SPECIFIC_RELEASE
  oci_golden_gate_deployment_actions:
    # required
    type: SPECIFIC_RELEASE

- name: Perform action start on deployment with type = CURRENT_RELEASE
  oci_golden_gate_deployment_actions:
    # required
    type: CURRENT_RELEASE

- name: Perform action stop on deployment with type = DEFAULT
  oci_golden_gate_deployment_actions:
    # required
    type: DEFAULT

- name: Perform action stop on deployment with type = SPECIFIC_RELEASE
  oci_golden_gate_deployment_actions:
    # required
    type: SPECIFIC_RELEASE

- name: Perform action stop on deployment with type = CURRENT_RELEASE
  oci_golden_gate_deployment_actions:
    # required
    type: CURRENT_RELEASE

- name: Perform action upgrade on deployment with type = DEFAULT
  oci_golden_gate_deployment_actions:
    # required
    type: DEFAULT

- name: Perform action upgrade on deployment with type = SPECIFIC_RELEASE
  oci_golden_gate_deployment_actions:
    # required
    ogg_version: ogg_version_example
    type: SPECIFIC_RELEASE

- name: Perform action upgrade on deployment with type = CURRENT_RELEASE
  oci_golden_gate_deployment_actions:
    # required
    type: CURRENT_RELEASE

"""

RETURN = """
deployment_wallet_exists_response_details:
    description:
        - Details of the Deployment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        is_ogg_wallet_exists:
            description:
                - Indicates if the wallet is present in the deployment container
            returned: on success
            type: bool
            sample: true
    sample: {
        "is_ogg_wallet_exists": true
    }

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
                - The time the resource was created. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the resource was last updated. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
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
                - Describes the object's current state in detail. For example, it can be used to provide
                  actionable information for a resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - A simple key-value pair that is applied without any predefined name, type, or scope. Exists
                  for cross-compatibility only.
                - "Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Tags defined for this resource. Each key is predefined and scoped to a namespace.
                - "Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
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
                - An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.
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
                - The private IP address in the customer's VCN representing the access point for the
                  associated endpoint service in the GoldenGate service VCN.
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
                - The system tags associated with this resource, if any. The system tags are set by Oracle
                  Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more
                  information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{orcl-cloud: {free-tier-retain: true}}`"
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
                - "Note: Deprecated: Use timeOfNextMaintenance instead, or related upgrade records
                  to check, when deployment will be forced to upgrade to a newer version.
                  Old description:
                  The date the existing version in use will no longer be considered as usable
                  and an upgrade will be required.  This date is typically 6 months after the
                  version was released for use by GGS.  The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`."
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
                - "The type of deployment, which can be any one of the Allowed values.
                  NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes.
                      Its use is discouraged in favor of 'DATABASE_ORACLE'."
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
                        - The name given to the GoldenGate service deployment.
                          The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.
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
        deployment_diagnostic_data:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                namespace_name:
                    description:
                        - Name of namespace that serves as a container for all of your buckets
                    returned: on success
                    type: str
                    sample: namespace_name_example
                bucket_name:
                    description:
                        - Name of the bucket where the object is to be uploaded in the object storage
                    returned: on success
                    type: str
                    sample: bucket_name_example
                object_name:
                    description:
                        - Name of the diagnostic collected and uploaded to object storage
                    returned: on success
                    type: str
                    sample: object_name_example
                diagnostic_state:
                    description:
                        - The state of the deployment diagnostic collection.
                    returned: on success
                    type: str
                    sample: IN_PROGRESS
                time_diagnostic_start:
                    description:
                        - The time from which the diagnostic collection should collect the logs. The format is defined by
                          L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_diagnostic_end:
                    description:
                        - The time until which the diagnostic collection should collect the logs. The format is defined by
                          L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        maintenance_window:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                day:
                    description:
                        - Days of the week.
                    returned: on success
                    type: str
                    sample: MONDAY
                start_hour:
                    description:
                        - Start hour for maintenance period. Hour is in UTC.
                    returned: on success
                    type: int
                    sample: 56
        time_of_next_maintenance:
            description:
                - The time of next maintenance schedule. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        next_maintenance_action_type:
            description:
                - Type of the next maintenance.
            returned: on success
            type: str
            sample: UPGRADE
        next_maintenance_description:
            description:
                - Description of the next maintenance.
            returned: on success
            type: str
            sample: next_maintenance_description_example
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
        },
        "deployment_diagnostic_data": {
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example",
            "object_name": "object_name_example",
            "diagnostic_state": "IN_PROGRESS",
            "time_diagnostic_start": "2013-10-20T19:20:30+01:00",
            "time_diagnostic_end": "2013-10-20T19:20:30+01:00"
        },
        "maintenance_window": {
            "day": "MONDAY",
            "start_hour": 56
        },
        "time_of_next_maintenance": "2013-10-20T19:20:30+01:00",
        "next_maintenance_action_type": "UPGRADE",
        "next_maintenance_description": "next_maintenance_description_example"
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
    from oci.golden_gate import GoldenGateClient
    from oci.golden_gate.models import ChangeDeploymentCompartmentDetails
    from oci.golden_gate.models import CollectDeploymentDiagnosticDetails
    from oci.golden_gate.models import DeploymentWalletExistsDetails
    from oci.golden_gate.models import ExportDeploymentWalletDetails
    from oci.golden_gate.models import ImportDeploymentWalletDetails
    from oci.golden_gate.models import StartDeploymentDetails
    from oci.golden_gate.models import StopDeploymentDetails
    from oci.golden_gate.models import UpgradeDeploymentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeploymentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        collect_deployment_diagnostic
        deployment_wallet_exists
        export_deployment_wallet
        import_deployment_wallet
        start
        stop
        upgrade
    """

    @staticmethod
    def get_module_resource_id_param():
        return "deployment_id"

    def get_module_resource_id(self):
        return self.module.params.get("deployment_id")

    def get_get_fn(self):
        return self.client.get_deployment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment,
            deployment_id=self.module.params.get("deployment_id"),
        )

    def get_response_field_name(self, action):
        response_fields = dict(
            stop="deployment",
            start="deployment",
            collect_deployment_diagnostic="deployment",
            deployment_wallet_exists="deployment_wallet_exists_response_details",
            export_deployment_wallet="deployment",
            import_deployment_wallet="deployment",
            upgrade="deployment",
            change_compartment="deployment",
        )
        return response_fields.get(action, "deployment")

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDeploymentCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_deployment_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                change_deployment_compartment_details=action_details,
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

    def collect_deployment_diagnostic(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CollectDeploymentDiagnosticDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.collect_deployment_diagnostic,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                collect_deployment_diagnostic_details=action_details,
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

    def deployment_wallet_exists(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DeploymentWalletExistsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.deployment_wallet_exists,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                deployment_wallet_exists_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def export_deployment_wallet(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ExportDeploymentWalletDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.export_deployment_wallet,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                export_deployment_wallet_details=action_details,
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

    def import_deployment_wallet(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ImportDeploymentWalletDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.import_deployment_wallet,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                import_deployment_wallet_details=action_details,
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
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, StartDeploymentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                start_deployment_details=action_details,
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
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, StopDeploymentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                stop_deployment_details=action_details,
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

    def upgrade(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpgradeDeploymentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.upgrade_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                upgrade_deployment_details=action_details,
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


DeploymentActionsHelperCustom = get_custom_class("DeploymentActionsHelperCustom")


class ResourceHelper(DeploymentActionsHelperCustom, DeploymentActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            namespace_name=dict(type="str"),
            bucket_name=dict(type="str"),
            diagnostic_name_prefix=dict(type="str"),
            time_diagnostic_start=dict(type="str"),
            time_diagnostic_end=dict(type="str"),
            secret_name=dict(type="str"),
            vault_id=dict(type="str"),
            new_wallet_secret_id=dict(type="str"),
            wallet_backup_secret_name=dict(type="str"),
            master_encryption_key_id=dict(type="str"),
            description=dict(type="str"),
            deployment_id=dict(aliases=["id"], type="str", required=True),
            ogg_version=dict(type="str"),
            type=dict(
                type="str", choices=["DEFAULT", "SPECIFIC_RELEASE", "CURRENT_RELEASE"]
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "collect_deployment_diagnostic",
                    "deployment_wallet_exists",
                    "export_deployment_wallet",
                    "import_deployment_wallet",
                    "start",
                    "stop",
                    "upgrade",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deployment",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
