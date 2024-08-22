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
module: oci_golden_gate_deployment_facts
short_description: Fetches details about one or multiple Deployment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Deployment resources in Oracle Cloud Infrastructure
    - Lists the Deployments in a compartment.
    - If I(deployment_id) is specified, the details of a single Deployment will be returned.
version_added: "2.9.0"
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
            - The OCID of the compartment that contains the work request. Work requests should be scoped
              to the same compartment as the resource the work request affects. If the work request concerns
              multiple resources, and those resources are not in the same compartment, it is up to the service team
              to pick the primary resource whose compartment should be used.
            - Required to list multiple deployments.
        type: str
    supported_connection_type:
        description:
            - The connection type which the deployment must support.
        type: str
        choices:
            - "GOLDENGATE"
            - "KAFKA"
            - "KAFKA_SCHEMA_REGISTRY"
            - "MYSQL"
            - "JAVA_MESSAGE_SERVICE"
            - "MICROSOFT_SQLSERVER"
            - "OCI_OBJECT_STORAGE"
            - "ORACLE"
            - "AZURE_DATA_LAKE_STORAGE"
            - "POSTGRESQL"
            - "AZURE_SYNAPSE_ANALYTICS"
            - "SNOWFLAKE"
            - "AMAZON_S3"
            - "HDFS"
            - "ORACLE_NOSQL"
            - "MONGODB"
            - "AMAZON_KINESIS"
            - "AMAZON_REDSHIFT"
            - "DB2"
            - "REDIS"
            - "ELASTICSEARCH"
            - "GENERIC"
            - "GOOGLE_CLOUD_STORAGE"
            - "GOOGLE_BIGQUERY"
    assigned_connection_id:
        description:
            - The OCID of the connection which for the deployment must be assigned.
        type: str
    assignable_connection_id:
        description:
            - Return the deployments to which the specified connectionId may be assigned.
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
            - "NEEDS_ATTENTION"
            - "IN_PROGRESS"
            - "CANCELING"
            - "CANCELED"
            - "SUCCEEDED"
            - "WAITING"
    lifecycle_sub_state:
        description:
            - A filter to return only the resources that match the 'lifecycleSubState' given.
        type: str
        choices:
            - "RECOVERING"
            - "STARTING"
            - "STOPPING"
            - "MOVING"
            - "UPGRADING"
            - "RESTORING"
            - "BACKUP_IN_PROGRESS"
            - "ROLLBACK_IN_PROGRESS"
    display_name:
        description:
            - A filter to return only the resources that match the entire 'displayName' given.
        type: str
        aliases: ["name"]
    fqdn:
        description:
            - A filter to return only the resources that match the 'fqdn' given.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is
              descending.  Default order for 'displayName' is ascending. If no value is specified
              timeCreated is the default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific deployment
  oci_golden_gate_deployment_facts:
    # required
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List deployments
  oci_golden_gate_deployment_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    supported_connection_type: GOLDENGATE
    assigned_connection_id: "ocid1.assignedconnection.oc1..xxxxxxEXAMPLExxxxxx"
    assignable_connection_id: "ocid1.assignableconnection.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    lifecycle_sub_state: RECOVERING
    display_name: display_name_example
    fqdn: fqdn_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
deployments:
    description:
        - List of Deployment resources
    returned: on success
    type: complex
    contains:
        deployment_backup_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup being referenced.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.deploymentbackup.oc1..xxxxxxEXAMPLExxxxxx"
        is_healthy:
            description:
                - True if all of the aggregate resources are working correctly.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        nsg_ids:
            description:
                - An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        ogg_data:
            description:
                - ""
                - Returned for get operation
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
                        - The base64 encoded content of the PEM file containing the SSL certificate.
                    returned: on success
                    type: str
                    sample: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
                credential_store:
                    description:
                        - The type of credential store for OGG.
                    returned: on success
                    type: str
                    sample: GOLDENGATE
                identity_domain_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Identity Domain when IAM credential store is
                          used.
                    returned: on success
                    type: str
                    sample: "ocid1.identitydomain.oc1..xxxxxxEXAMPLExxxxxx"
                password_secret_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Secret where the deployment password is
                          stored.
                    returned: on success
                    type: str
                    sample: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_diagnostic_data:
            description:
                - ""
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        next_maintenance_action_type:
            description:
                - Type of the next maintenance.
                - Returned for get operation
            returned: on success
            type: str
            sample: UPGRADE
        next_maintenance_description:
            description:
                - Description of the next maintenance.
                - Returned for get operation
            returned: on success
            type: str
            sample: next_maintenance_description_example
        maintenance_configuration:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                is_interim_release_auto_upgrade_enabled:
                    description:
                        - By default auto upgrade for interim releases are not enabled. If auto-upgrade is enabled for interim release,
                          you have to specify interimReleaseUpgradePeriodInDays too.
                    returned: on success
                    type: bool
                    sample: true
                interim_release_upgrade_period_in_days:
                    description:
                        - Defines auto upgrade period for interim releases. This period must be shorter or equal to bundle release upgrade period.
                    returned: on success
                    type: int
                    sample: 56
                bundle_release_upgrade_period_in_days:
                    description:
                        - Defines auto upgrade period for bundle releases. Manually configured period cannot be longer than service defined period for bundle
                          releases.
                          This period must be shorter or equal to major release upgrade period. Not passing this field during create will equate to using the
                          service default.
                    returned: on success
                    type: int
                    sample: 56
                major_release_upgrade_period_in_days:
                    description:
                        - Defines auto upgrade period for major releases. Manually configured period cannot be longer than service defined period for major
                          releases.
                          Not passing this field during create will equate to using the service default.
                    returned: on success
                    type: int
                    sample: 56
                security_patch_upgrade_period_in_days:
                    description:
                        - Defines auto upgrade period for releases with security fix. Manually configured period cannot be longer than service defined period
                          for security releases.
                          Not passing this field during create will equate to using the service default.
                    returned: on success
                    type: int
                    sample: 56
        time_ogg_version_supported_until:
            description:
                - The time until OGG version is supported. After this date has passed OGG version will not be available anymore. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        ingress_ips:
            description:
                - List of ingress IP addresses from where the GoldenGate deployment connects to this connection's privateIp.
                  Customers may optionally set up ingress security rules to restrict traffic from these IP addresses.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                ingress_ip:
                    description:
                        - A Private Endpoint IPv4 or IPv6 Address created in the customer's subnet.
                    returned: on success
                    type: str
                    sample: ingress_ip_example
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
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet of the deployment's private endpoint.
                  The subnet must be a private subnet. For backward compatibility, public subnets are allowed until May 31 2025,
                  after which the private subnet will be enforced.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        load_balancer_subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a public subnet in the customer tenancy.
                  Can be provided only for public deployments. If provided, the loadbalancer will be created in this subnet instead of the service tenancy.
                  For backward compatibility, this is an optional property. It will become mandatory for public deployments after October 1, 2024.
            returned: on success
            type: str
            sample: "ocid1.loadbalancersubnet.oc1..xxxxxxEXAMPLExxxxxx"
        load_balancer_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the loadbalancer in the customer's subnet.
                  The loadbalancer of the public deployment created in the customer subnet.
            returned: on success
            type: str
            sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
        license_model:
            description:
                - The Oracle license model that applies to a Deployment.
            returned: on success
            type: str
            sample: LICENSE_INCLUDED
        fqdn:
            description:
                - A three-label Fully Qualified Domain Name (FQDN) for a resource.
            returned: on success
            type: str
            sample: fqdn_example
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
        deployment_type:
            description:
                - "The type of deployment, which can be any one of the Allowed values.
                  NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes.
                      Its use is discouraged in favor of 'DATABASE_ORACLE'."
            returned: on success
            type: str
            sample: OGG
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
        locks:
            description:
                - Locks associated with this resource.
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Type of the lock.
                    returned: on success
                    type: str
                    sample: FULL
                related_resource_id:
                    description:
                        - The id of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.
                    returned: on success
                    type: str
                    sample: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
                message:
                    description:
                        - A message added by the creator of the lock. This is typically used to give an
                          indication of why the resource is locked.
                    returned: on success
                    type: str
                    sample: message_example
                time_created:
                    description:
                        - When the lock was created.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "deployment_backup_id": "ocid1.deploymentbackup.oc1..xxxxxxEXAMPLExxxxxx",
        "is_healthy": true,
        "nsg_ids": [],
        "ogg_data": {
            "deployment_name": "deployment_name_example",
            "admin_username": "admin_username_example",
            "ogg_version": "ogg_version_example",
            "certificate": "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----",
            "credential_store": "GOLDENGATE",
            "identity_domain_id": "ocid1.identitydomain.oc1..xxxxxxEXAMPLExxxxxx",
            "password_secret_id": "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
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
        "next_maintenance_description": "next_maintenance_description_example",
        "maintenance_configuration": {
            "is_interim_release_auto_upgrade_enabled": true,
            "interim_release_upgrade_period_in_days": 56,
            "bundle_release_upgrade_period_in_days": 56,
            "major_release_upgrade_period_in_days": 56,
            "security_patch_upgrade_period_in_days": 56
        },
        "time_ogg_version_supported_until": "2013-10-20T19:20:30+01:00",
        "ingress_ips": [{
            "ingress_ip": "ingress_ip_example"
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_sub_state": "RECOVERING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "load_balancer_subnet_id": "ocid1.loadbalancersubnet.oc1..xxxxxxEXAMPLExxxxxx",
        "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
        "license_model": "LICENSE_INCLUDED",
        "fqdn": "fqdn_example",
        "cpu_core_count": 56,
        "is_auto_scaling_enabled": true,
        "is_public": true,
        "public_ip_address": "public_ip_address_example",
        "private_ip_address": "private_ip_address_example",
        "deployment_url": "deployment_url_example",
        "system_tags": {},
        "is_latest_version": true,
        "time_upgrade_required": "2013-10-20T19:20:30+01:00",
        "deployment_type": "OGG",
        "storage_utilization_in_bytes": 56,
        "is_storage_utilization_limit_exceeded": true,
        "locks": [{
            "type": "FULL",
            "related_resource_id": "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx",
            "message": "message_example",
            "time_created": "2013-10-20T19:20:30+01:00"
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
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
            "supported_connection_type",
            "assigned_connection_id",
            "assignable_connection_id",
            "lifecycle_state",
            "lifecycle_sub_state",
            "display_name",
            "fqdn",
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
            supported_connection_type=dict(
                type="str",
                choices=[
                    "GOLDENGATE",
                    "KAFKA",
                    "KAFKA_SCHEMA_REGISTRY",
                    "MYSQL",
                    "JAVA_MESSAGE_SERVICE",
                    "MICROSOFT_SQLSERVER",
                    "OCI_OBJECT_STORAGE",
                    "ORACLE",
                    "AZURE_DATA_LAKE_STORAGE",
                    "POSTGRESQL",
                    "AZURE_SYNAPSE_ANALYTICS",
                    "SNOWFLAKE",
                    "AMAZON_S3",
                    "HDFS",
                    "ORACLE_NOSQL",
                    "MONGODB",
                    "AMAZON_KINESIS",
                    "AMAZON_REDSHIFT",
                    "DB2",
                    "REDIS",
                    "ELASTICSEARCH",
                    "GENERIC",
                    "GOOGLE_CLOUD_STORAGE",
                    "GOOGLE_BIGQUERY",
                ],
            ),
            assigned_connection_id=dict(type="str"),
            assignable_connection_id=dict(type="str"),
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
                    "NEEDS_ATTENTION",
                    "IN_PROGRESS",
                    "CANCELING",
                    "CANCELED",
                    "SUCCEEDED",
                    "WAITING",
                ],
            ),
            lifecycle_sub_state=dict(
                type="str",
                choices=[
                    "RECOVERING",
                    "STARTING",
                    "STOPPING",
                    "MOVING",
                    "UPGRADING",
                    "RESTORING",
                    "BACKUP_IN_PROGRESS",
                    "ROLLBACK_IN_PROGRESS",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            fqdn=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

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
