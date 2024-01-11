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
module: oci_recovery_protected_database_actions
short_description: Perform actions on a ProtectedDatabase resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ProtectedDatabase resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a protected database resource from the existing compartment to the specified compartment. When provided, If-Match
      is checked against ETag values of the resource.
    - For I(action=fetch_protected_database_configuration), downloads the network service configuration file 'tnsnames.ora' for a specified protected database.
      Applies to user-defined recovery systems only.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the protected database should be
              moved.
            - Required for I(action=change_compartment).
        type: str
    dest:
        description:
            - The destination file path to write the output. The file will be created if it does not exist. If the file already exists, the content will be
              overwritten.
            - Required for I(action=fetch_protected_database_configuration).
        type: str
    protected_database_id:
        description:
            - The protected database OCID.
        type: str
        aliases: ["id"]
        required: true
    configuration_type:
        description:
            - Currently has four config options ALL, TNSNAMES, HOSTS and CABUNDLE. All will return a zipped folder containing the contents of both tnsnames and
              the certificateChainPem.
            - Applicable only for I(action=fetch_protected_database_configuration).
        type: str
        choices:
            - "CABUNDLE"
            - "TNSNAMES"
            - "HOSTS"
            - "ALL"
    action:
        description:
            - The action to perform on the ProtectedDatabase.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "fetch_protected_database_configuration"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on protected_database
  oci_recovery_protected_database_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    protected_database_id: "ocid1.protecteddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action fetch_protected_database_configuration on protected_database
  oci_recovery_protected_database_actions:
    # required
    dest: /tmp/myfile
    protected_database_id: "ocid1.protecteddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: fetch_protected_database_configuration

    # optional
    configuration_type: CABUNDLE

"""

RETURN = """
protected_database:
    description:
        - Details of the ProtectedDatabase resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the protected database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The protected database name. You can change the displayName. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment that contains the protected database.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        db_unique_name:
            description:
                - The dbUniqueName for the protected database in Recovery Service. You cannot change the unique name.
            returned: on success
            type: str
            sample: db_unique_name_example
        vpc_user_name:
            description:
                - The virtual private catalog (VPC) user credentials that authenticates the protected database to access Recovery Service.
            returned: on success
            type: str
            sample: vpc_user_name_example
        database_size:
            description:
                - "The size of the protected database. XS - Less than 5GB, S - 5GB to 50GB, M - 50GB to 500GB, L - 500GB to 1TB, XL - 1TB to 5TB, XXL - Greater
                  than 5TB."
            returned: on success
            type: str
            sample: XS
        protection_policy_id:
            description:
                - The OCID of the protection policy associated with the protected database.
            returned: on success
            type: str
            sample: "ocid1.protectionpolicy.oc1..xxxxxxEXAMPLExxxxxx"
        recovery_service_subnets:
            description:
                - List of recovery service subnet resources associated with the protected database.
            returned: on success
            type: complex
            contains:
                recovery_service_subnet_id:
                    description:
                        - Recovery Service Subnet Identifier.
                    returned: on success
                    type: str
                    sample: "ocid1.recoveryservicesubnet.oc1..xxxxxxEXAMPLExxxxxx"
                lifecycle_state:
                    description:
                        - The current state of the Recovery Service Subnet.
                    returned: on success
                    type: str
                    sample: CREATING
        database_id:
            description:
                - The OCID of the protected database.
            returned: on success
            type: str
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        database_size_in_gbs:
            description:
                - The size of the database in GBs, in gigabytes.
            returned: on success
            type: int
            sample: 56
        change_rate:
            description:
                - The percentage of data changes that exist in the database between successive incremental backups.
            returned: on success
            type: float
            sample: 1.2
        compression_ratio:
            description:
                - The compression ratio of the protected database. The compression ratio represents the ratio of compressed block size to expanded block size.
            returned: on success
            type: float
            sample: 1.2
        is_redo_logs_shipped:
            description:
                - The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected
                  database to Recovery Service.
                  Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups.
                  For this to be effective, additional
                  configuration is needed on client side.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - "An RFC3339 formatted datetime string that indicates the created time for a protected database. For example: '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "An RFC3339 formatted datetime string that indicates the last updated time for a protected database. For example: '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Protected Database.
            returned: on success
            type: str
            sample: CREATING
        health:
            description:
                - "Indicates the protection status of the database. Allowed values are:
                   - HEALTHY
                   - WARNING
                   - ALERT"
                - "A 'HEALTHY' status indicates that Recovery Service can ensure database recovery to any point in time within the entire recovery window. The
                  potential data loss exposure since the last backup is:
                   - Less than 10 seconds, if Real-time data protection is enabled
                   - Less than 70 minutes if Real-time data protection is disabled"
                - "A 'WARNING' status indicates that Recovery Service can ensure database recovery within the current recovery window - 1 day. The potential
                  data loss exposure since the last backup is:
                   - Greater than 10 seconds, if Real-time data protection is enabled
                   - Greater than 60 minutes, if if Real-time data protection is disabled"
                - An 'ALERT' status indicates that Recovery Service cannot recover the database within the current recovery window.
            returned: on success
            type: str
            sample: PROTECTED
        is_read_only_resource:
            description:
                - Indicates whether the protected database is created by Recovery Service or created manually.
                  Set to <b>TRUE</b> for a service-defined protected database. When you enable the OCI-managed automatic backups option for a database and set
                  Recovery Service as the backup destination, then Recovery Service creates the associated protected database resource.
                  Set to <b>FALSE</b> for a user-defined protected database.
            returned: on success
            type: bool
            sample: true
        lifecycle_details:
            description:
                - Detailed description about the current lifecycle state of the protected database. For example, it can be used to provide actionable
                  information for a resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        health_details:
            description:
                - A message describing the current health of the protected database.
            returned: on success
            type: str
            sample: health_details_example
        metrics:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                backup_space_used_in_gbs:
                    description:
                        - Backup storage space, in gigabytes, utilized by the protected database. Oracle charges for the total storage used.
                    returned: on success
                    type: float
                    sample: 3.4
                backup_space_estimate_in_gbs:
                    description:
                        - The estimated backup storage space, in gigabytes, required to meet the recovery window goal, including foot print and backups for the
                          protected database.
                    returned: on success
                    type: float
                    sample: 3.4
                unprotected_window_in_seconds:
                    description:
                        - This is the time window when there is data loss exposure. The point after which recovery is impossible unless additional redo is
                          available.
                          This is the time we received the last backup or last redo-log shipped.
                    returned: on success
                    type: float
                    sample: 3.4
                db_size_in_gbs:
                    description:
                        - The estimated space, in gigabytes, consumed by the protected database. The database size is based on the size of the data files in the
                          catalog, and does not include archive logs.
                    returned: on success
                    type: float
                    sample: 3.4
                is_redo_logs_enabled:
                    description:
                        - The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the
                          protected database to Recovery Service.
                          Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log
                          backups.
                    returned: on success
                    type: bool
                    sample: true
                retention_period_in_days:
                    description:
                        - The maximum number of days to retain backups for a protected database.
                    returned: on success
                    type: float
                    sample: 3.4
                current_retention_period_in_seconds:
                    description:
                        - Number of seconds backups are currently retained for this database.
                    returned: on success
                    type: float
                    sample: 3.4
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
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`. For more information, see L(Resource Tags,https://docs.oracle.com/en-
                  us/iaas/Content/General/Concepts/resourcetags.htm)"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`. For more information, see L(Resource Tags,https://docs.oracle.com/en-
                  us/iaas/Content/General/Concepts/resourcetags.htm)"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "db_unique_name": "db_unique_name_example",
        "vpc_user_name": "vpc_user_name_example",
        "database_size": "XS",
        "protection_policy_id": "ocid1.protectionpolicy.oc1..xxxxxxEXAMPLExxxxxx",
        "recovery_service_subnets": [{
            "recovery_service_subnet_id": "ocid1.recoveryservicesubnet.oc1..xxxxxxEXAMPLExxxxxx",
            "lifecycle_state": "CREATING"
        }],
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "database_size_in_gbs": 56,
        "change_rate": 1.2,
        "compression_ratio": 1.2,
        "is_redo_logs_shipped": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "health": "PROTECTED",
        "is_read_only_resource": true,
        "lifecycle_details": "lifecycle_details_example",
        "health_details": "health_details_example",
        "metrics": {
            "backup_space_used_in_gbs": 3.4,
            "backup_space_estimate_in_gbs": 3.4,
            "unprotected_window_in_seconds": 3.4,
            "db_size_in_gbs": 3.4,
            "is_redo_logs_enabled": true,
            "retention_period_in_days": 3.4,
            "current_retention_period_in_seconds": 3.4
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible.module_utils._text import to_bytes
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
    from oci.recovery import DatabaseRecoveryClient
    from oci.recovery.models import ChangeProtectedDatabaseCompartmentDetails
    from oci.recovery.models import FetchProtectedDatabaseConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProtectedDatabaseActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        fetch_protected_database_configuration
    """

    @staticmethod
    def get_module_resource_id_param():
        return "protected_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("protected_database_id")

    def get_get_fn(self):
        return self.client.get_protected_database

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_protected_database,
            protected_database_id=self.module.params.get("protected_database_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeProtectedDatabaseCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_protected_database_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                protected_database_id=self.module.params.get("protected_database_id"),
                change_protected_database_compartment_details=action_details,
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

    def fetch_protected_database_configuration(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, FetchProtectedDatabaseConfigurationDetails
        )
        response = oci_wait_utils.call_and_wait(
            call_fn=self.client.fetch_protected_database_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                protected_database_id=self.module.params.get("protected_database_id"),
                fetch_protected_database_configuration_details=action_details,
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
        dest = self.module.params.get("dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None


ProtectedDatabaseActionsHelperCustom = get_custom_class(
    "ProtectedDatabaseActionsHelperCustom"
)


class ResourceHelper(
    ProtectedDatabaseActionsHelperCustom, ProtectedDatabaseActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            dest=dict(type="str"),
            protected_database_id=dict(aliases=["id"], type="str", required=True),
            configuration_type=dict(
                type="str", choices=["CABUNDLE", "TNSNAMES", "HOSTS", "ALL"]
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "fetch_protected_database_configuration",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="protected_database",
        service_client_class=DatabaseRecoveryClient,
        namespace="recovery",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
