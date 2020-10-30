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
module: oci_database_autonomous_container_database
short_description: Manage an AutonomousContainerDatabase resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an AutonomousContainerDatabase resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an Autonomous Container Database in the specified Autonomous Exadata Infrastructure.
    - "This resource has the following action operations in the M(oci_autonomous_container_database_actions) module: restart,
      rotate_autonomous_container_database_encryption_key."
version_added: "2.9"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - The display name for the Autonomous Container Database.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    db_unique_name:
        description:
            - The `DB_UNIQUE_NAME` of the Oracle Database being backed up.
        type: str
    service_level_agreement_type:
        description:
            - The service level agreement type of the Autonomous Container Database. The default is STANDARD. For an autonomous dataguard Autonomous Container
              Database, the specified Autonomous Exadata Infrastructure must be associated with a remote Autonomous Exadata Infrastructure.
        type: str
        choices:
            - "STANDARD"
    autonomous_exadata_infrastructure_id:
        description:
            - The OCID of the Autonomous Exadata Infrastructure.
        type: str
    autonomous_vm_cluster_id:
        description:
            - The OCID of the Autonomous VM Cluster.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the Autonomous Container
              Database.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    patch_model:
        description:
            - Database Patch model preference.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "RELEASE_UPDATES"
            - "RELEASE_UPDATE_REVISIONS"
    maintenance_window_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            preference:
                description:
                    - The maintenance window scheduling preference.
                type: str
                choices:
                    - "NO_PREFERENCE"
                    - "CUSTOM_PREFERENCE"
                required: true
            months:
                description:
                    - Months during the year when maintenance should be performed.
                type: list
                suboptions:
                    name:
                        description:
                            - Name of the month of the year.
                        type: str
                        choices:
                            - "JANUARY"
                            - "FEBRUARY"
                            - "MARCH"
                            - "APRIL"
                            - "MAY"
                            - "JUNE"
                            - "JULY"
                            - "AUGUST"
                            - "SEPTEMBER"
                            - "OCTOBER"
                            - "NOVEMBER"
                            - "DECEMBER"
                        required: true
            weeks_of_month:
                description:
                    - Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a
                      duration of 7 days. Weeks start and end based on calendar dates, not days of the week.
                      For example, to allow maintenance during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2.
                      Maintenance cannot be scheduled for the fifth week of months that contain more than 28 days.
                      Note that this parameter works in conjunction with the  daysOfWeek and hoursOfDay parameters to allow you to specify specific days of the
                      week and hours that maintenance will be performed.
                type: list
            days_of_week:
                description:
                    - Days during the week when maintenance should be performed.
                type: list
                suboptions:
                    name:
                        description:
                            - Name of the day of the week.
                        type: str
                        choices:
                            - "MONDAY"
                            - "TUESDAY"
                            - "WEDNESDAY"
                            - "THURSDAY"
                            - "FRIDAY"
                            - "SATURDAY"
                            - "SUNDAY"
                        required: true
            hours_of_day:
                description:
                    - "The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are
                      - 0 - represents time slot 0:00 - 3:59 UTC - 4 - represents time slot 4:00 - 7:59 UTC - 8 - represents time slot 8:00 - 11:59 UTC - 12 -
                        represents time slot 12:00 - 15:59 UTC - 16 - represents time slot 16:00 - 19:59 UTC - 20 - represents time slot 20:00 - 23:59 UTC"
                type: list
            lead_time_in_weeks:
                description:
                    - Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to 4.
                type: int
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - This parameter is updatable.
        type: dict
    backup_config:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            backup_destination_details:
                description:
                    - Backup destination details.
                type: list
                suboptions:
                    type:
                        description:
                            - Type of the database backup destination.
                        type: str
                        choices:
                            - "NFS"
                            - "RECOVERY_APPLIANCE"
                            - "OBJECT_STORE"
                            - "LOCAL"
                        required: true
                    id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup destination.
                        type: str
                    vpc_user:
                        description:
                            - For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) user that is used to access the Recovery Appliance.
                        type: str
                    vpc_password:
                        description:
                            - For a RECOVERY_APPLIANCE backup destination, the password for the VPC user that is used to access the Recovery Appliance.
                        type: str
                    internet_proxy:
                        description:
                            - Proxy URL to connect to object store.
                        type: str
            recovery_window_in_days:
                description:
                    - Number of days between the current and the earliest point of recoverability covered by automatic backups.
                      This value applies to automatic backups. After a new automatic backup has been created, Oracle removes old automatic backups that are
                      created before the window.
                      When the value is updated, it is applied to all existing automatic backups.
                type: int
    kms_key_id:
        description:
            - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
        type: str
    kms_key_version_id:
        description:
            - The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key
              versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.
        type: str
    vault_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
              L(vault,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
        type: str
    autonomous_container_database_id:
        description:
            - The Autonomous Container Database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the AutonomousContainerDatabase.
            - Use I(state=present) to create or update an AutonomousContainerDatabase.
            - Use I(state=absent) to delete an AutonomousContainerDatabase.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create autonomous_container_database
  oci_database_autonomous_container_database:
    display_name: containerdatabases2
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    patch_model: RELEASE_UPDATES

- name: Update autonomous_container_database using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_autonomous_container_database:
    display_name: new Display name

- name: Update autonomous_container_database
  oci_database_autonomous_container_database:
    autonomous_container_database_id: ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete autonomous_container_database
  oci_database_autonomous_container_database:
    autonomous_container_database_id: ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete autonomous_container_database using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_autonomous_container_database:
    display_name: containerdatabases2
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
autonomous_container_database:
    description:
        - Details of the AutonomousContainerDatabase resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the Autonomous Container Database.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The user-provided name for the Autonomous Container Database.
            returned: on success
            type: string
            sample: display_name_example
        db_unique_name:
            description:
                - The `DB_UNIQUE_NAME` of the Oracle Database being backed up.
            returned: on success
            type: string
            sample: db_unique_name_example
        service_level_agreement_type:
            description:
                - The service level agreement type of the container database. The default is STANDARD.
            returned: on success
            type: string
            sample: STANDARD
        autonomous_exadata_infrastructure_id:
            description:
                - The OCID of the Autonomous Exadata Infrastructure.
            returned: on success
            type: string
            sample: ocid1.autonomousexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx
        autonomous_vm_cluster_id:
            description:
                - The OCID of the Autonomous VM Cluster.
            returned: on success
            type: string
            sample: ocid1.autonomousvmcluster.oc1..xxxxxxEXAMPLExxxxxx
        infrastructure_type:
            description:
                - The infrastructure type this resource belongs to.
            returned: on success
            type: string
            sample: CLOUD
        kms_key_id:
            description:
                - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
            returned: on success
            type: string
            sample: ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx
        vault_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
                  L(vault,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
            returned: on success
            type: string
            sample: ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of the Autonomous Container Database.
            returned: on success
            type: string
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState.
            returned: on success
            type: string
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the Autonomous Container Database was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        patch_model:
            description:
                - Database patch model preference.
            returned: on success
            type: string
            sample: RELEASE_UPDATES
        patch_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last patch applied on the system.
            returned: on success
            type: string
            sample: ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx
        last_maintenance_run_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last maintenance run.
            returned: on success
            type: string
            sample: ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx
        next_maintenance_run_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the next maintenance run.
            returned: on success
            type: string
            sample: ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx
        maintenance_window:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                preference:
                    description:
                        - The maintenance window scheduling preference.
                    returned: on success
                    type: string
                    sample: NO_PREFERENCE
                months:
                    description:
                        - Months during the year when maintenance should be performed.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the month of the year.
                            returned: on success
                            type: string
                            sample: JANUARY
                weeks_of_month:
                    description:
                        - Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a
                          duration of 7 days. Weeks start and end based on calendar dates, not days of the week.
                          For example, to allow maintenance during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2.
                          Maintenance cannot be scheduled for the fifth week of months that contain more than 28 days.
                          Note that this parameter works in conjunction with the  daysOfWeek and hoursOfDay parameters to allow you to specify specific days of
                          the week and hours that maintenance will be performed.
                    returned: on success
                    type: list
                    sample: []
                days_of_week:
                    description:
                        - Days during the week when maintenance should be performed.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the day of the week.
                            returned: on success
                            type: string
                            sample: MONDAY
                hours_of_day:
                    description:
                        - "The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are
                          - 0 - represents time slot 0:00 - 3:59 UTC - 4 - represents time slot 4:00 - 7:59 UTC - 8 - represents time slot 8:00 - 11:59 UTC - 12
                            - represents time slot 12:00 - 15:59 UTC - 16 - represents time slot 16:00 - 19:59 UTC - 20 - represents time slot 20:00 - 23:59
                            UTC"
                    returned: on success
                    type: list
                    sample: []
                lead_time_in_weeks:
                    description:
                        - Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to
                          4.
                    returned: on success
                    type: int
                    sample: 56
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        availability_domain:
            description:
                - The availability domain of the Autonomous Container Database.
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        db_version:
            description:
                - Oracle Database version of the Autonomous Container Database.
            returned: on success
            type: string
            sample: db_version_example
        backup_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                backup_destination_details:
                    description:
                        - Backup destination details.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - Type of the database backup destination.
                            returned: on success
                            type: string
                            sample: NFS
                        id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup destination.
                            returned: on success
                            type: string
                            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                        vpc_user:
                            description:
                                - For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) user that is used to access the Recovery
                                  Appliance.
                            returned: on success
                            type: string
                            sample: vpc_user_example
                        vpc_password:
                            description:
                                - For a RECOVERY_APPLIANCE backup destination, the password for the VPC user that is used to access the Recovery Appliance.
                            returned: on success
                            type: string
                            sample: vpc_password_example
                        internet_proxy:
                            description:
                                - Proxy URL to connect to object store.
                            returned: on success
                            type: string
                            sample: internet_proxy_example
                recovery_window_in_days:
                    description:
                        - Number of days between the current and the earliest point of recoverability covered by automatic backups.
                          This value applies to automatic backups. After a new automatic backup has been created, Oracle removes old automatic backups that are
                          created before the window.
                          When the value is updated, it is applied to all existing automatic backups.
                    returned: on success
                    type: int
                    sample: 56
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "db_unique_name": "db_unique_name_example",
        "service_level_agreement_type": "STANDARD",
        "autonomous_exadata_infrastructure_id": "ocid1.autonomousexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx",
        "autonomous_vm_cluster_id": "ocid1.autonomousvmcluster.oc1..xxxxxxEXAMPLExxxxxx",
        "infrastructure_type": "CLOUD",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "patch_model": "RELEASE_UPDATES",
        "patch_id": "ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx",
        "last_maintenance_run_id": "ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "next_maintenance_run_id": "ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "maintenance_window": {
            "preference": "NO_PREFERENCE",
            "months": [{
                "name": "JANUARY"
            }],
            "weeks_of_month": [],
            "days_of_week": [{
                "name": "MONDAY"
            }],
            "hours_of_day": [],
            "lead_time_in_weeks": 56
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "availability_domain": "Uocm:PHX-AD-1",
        "db_version": "db_version_example",
        "backup_config": {
            "backup_destination_details": [{
                "type": "NFS",
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "vpc_user": "vpc_user_example",
                "vpc_password": "vpc_password_example",
                "internet_proxy": "internet_proxy_example"
            }],
            "recovery_window_in_days": 56
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
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreateAutonomousContainerDatabaseDetails
    from oci.database.models import UpdateAutonomousContainerDatabaseDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousContainerDatabaseHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(AutonomousContainerDatabaseHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_module_resource_id_param(self):
        return "autonomous_container_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("autonomous_container_database_id")

    def get_get_fn(self):
        return self.client.get_autonomous_container_database

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_container_database,
            autonomous_container_database_id=self.module.params.get(
                "autonomous_container_database_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "autonomous_exadata_infrastructure_id",
            "autonomous_vm_cluster_id",
            "display_name",
        ]

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
            self.client.list_autonomous_container_databases, **kwargs
        )

    def get_create_model_class(self):
        return CreateAutonomousContainerDatabaseDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_autonomous_container_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_autonomous_container_database_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateAutonomousContainerDatabaseDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_autonomous_container_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_container_database_id=self.module.params.get(
                    "autonomous_container_database_id"
                ),
                update_autonomous_container_database_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.terminate_autonomous_container_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_container_database_id=self.module.params.get(
                    "autonomous_container_database_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AutonomousContainerDatabaseHelperCustom = get_custom_class(
    "AutonomousContainerDatabaseHelperCustom"
)


class ResourceHelper(
    AutonomousContainerDatabaseHelperCustom, AutonomousContainerDatabaseHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            db_unique_name=dict(type="str"),
            service_level_agreement_type=dict(type="str", choices=["STANDARD"]),
            autonomous_exadata_infrastructure_id=dict(type="str"),
            autonomous_vm_cluster_id=dict(type="str"),
            compartment_id=dict(type="str"),
            patch_model=dict(
                type="str", choices=["RELEASE_UPDATES", "RELEASE_UPDATE_REVISIONS"]
            ),
            maintenance_window_details=dict(
                type="dict",
                options=dict(
                    preference=dict(
                        type="str",
                        required=True,
                        choices=["NO_PREFERENCE", "CUSTOM_PREFERENCE"],
                    ),
                    months=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "JANUARY",
                                    "FEBRUARY",
                                    "MARCH",
                                    "APRIL",
                                    "MAY",
                                    "JUNE",
                                    "JULY",
                                    "AUGUST",
                                    "SEPTEMBER",
                                    "OCTOBER",
                                    "NOVEMBER",
                                    "DECEMBER",
                                ],
                            )
                        ),
                    ),
                    weeks_of_month=dict(type="list"),
                    days_of_week=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "MONDAY",
                                    "TUESDAY",
                                    "WEDNESDAY",
                                    "THURSDAY",
                                    "FRIDAY",
                                    "SATURDAY",
                                    "SUNDAY",
                                ],
                            )
                        ),
                    ),
                    hours_of_day=dict(type="list"),
                    lead_time_in_weeks=dict(type="int"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            backup_config=dict(
                type="dict",
                options=dict(
                    backup_destination_details=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "NFS",
                                    "RECOVERY_APPLIANCE",
                                    "OBJECT_STORE",
                                    "LOCAL",
                                ],
                            ),
                            id=dict(type="str"),
                            vpc_user=dict(type="str"),
                            vpc_password=dict(type="str", no_log=True),
                            internet_proxy=dict(type="str"),
                        ),
                    ),
                    recovery_window_in_days=dict(type="int"),
                ),
            ),
            kms_key_id=dict(type="str"),
            kms_key_version_id=dict(type="str"),
            vault_id=dict(type="str"),
            autonomous_container_database_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="autonomous_container_database",
        service_client_class=DatabaseClient,
        namespace="database",
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
