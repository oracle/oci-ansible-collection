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
module: oci_database_data_guard_association
short_description: Manage a DataGuardAssociation resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a DataGuardAssociation resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Data Guard association.  A Data Guard association represents the replication relationship between the
      specified database and a peer database. For more information, see L(Using Oracle Data
      Guard,https://docs.cloud.oracle.com/Content/Database/Tasks/usingdataguard.htm).
    - All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID
      called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response.
      You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the
      resource in the Console. For more information, see
      L(Resource Identifiers,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
    - "This resource has the following action operations in the M(oci_data_guard_association_actions) module: failover, reinstate, switchover."
version_added: "2.9"
author: Oracle (@oracle)
options:
    database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    database_admin_password:
        description:
            - A strong password for the `SYS`, `SYSTEM`, and `PDB Admin` users to apply during standby creation.
            - "The password must contain no fewer than nine characters and include:"
            - "* At least two uppercase characters."
            - "* At least two lowercase characters."
            - "* At least two numeric characters."
            - "* At least two special characters. Valid special characters include \\"_\\", \\"#\\", and \\"-\\" only."
            - "**The password MUST be the same as the primary admin password.**"
        type: str
        required: true
    protection_mode:
        description:
            - The protection mode to set up between the primary and standby databases. For more information, see
              L(Oracle Data Guard Protection Modes,http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)
              in the Oracle Data Guard documentation.
            - "**IMPORTANT** - The only protection mode currently supported by the Database service is MAXIMUM_PERFORMANCE."
        type: str
        choices:
            - "MAXIMUM_AVAILABILITY"
            - "MAXIMUM_PERFORMANCE"
            - "MAXIMUM_PROTECTION"
        required: true
    transport_type:
        description:
            - "The redo transport type to use for this Data Guard association.  Valid values depend on the specified `protectionMode`:"
            - "* MAXIMUM_AVAILABILITY - SYNC or FASTSYNC
              * MAXIMUM_PERFORMANCE - ASYNC
              * MAXIMUM_PROTECTION - SYNC"
            - For more information, see
              L(Redo Transport Services,http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400)
              in the Oracle Data Guard documentation.
            - "**IMPORTANT** - The only transport type currently supported by the Database service is ASYNC."
        type: str
        choices:
            - "SYNC"
            - "ASYNC"
            - "FASTSYNC"
        required: true
    creation_type:
        description:
            - Specifies whether to create the peer database in an existing DB system or in a new DB system.
        type: str
        choices:
            - "NewDbSystem"
            - "ExistingVmCluster"
            - "ExistingDbSystem"
        required: true
    display_name:
        description:
            - The user-friendly name of the DB system that will contain the the standby database. The display name does not have to be unique.
            - Applicable when creation_type is 'NewDbSystem'
        type: str
        aliases: ["name"]
    availability_domain:
        description:
            - "The name of the availability domain that the standby database DB system will be located in. For example- \\"Uocm:PHX-AD-1\\"."
            - Applicable when creation_type is 'NewDbSystem'
        type: str
    shape:
        description:
            - The virtual machine DB system shape to launch for the standby database in the Data Guard association. The shape determines the number of CPU cores
              and the amount of memory available for the DB system.
              Only virtual machine shapes are valid options. If you do not supply this parameter, the default shape is the shape of the primary DB system.
            - To get a list of all shapes, use the L(ListDbSystemShapes,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/database/20160918/DbSystemShapeSummary/ListDbSystemShapes) operation.
            - Applicable when creation_type is 'NewDbSystem'
        type: str
    subnet_id:
        description:
            - "The OCID of the subnet the DB system is associated with.
              **Subnet Restrictions:**
              - For 1- and 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.16.16/28"
            - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
              Specifying an overlapping subnet will cause the private interconnect to malfunction.
              This restriction applies to both the client subnet and backup subnet.
            - Applicable when creation_type is 'NewDbSystem'
        type: str
    nsg_ids:
        description:
            - "A list of the L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that this
              resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs,
              see L(Security Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm).
              **NsgIds restrictions:**
              - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty."
            - Applicable when creation_type is 'NewDbSystem'
        type: list
    backup_network_nsg_ids:
        description:
            - A list of the L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that the
              backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more
              information about NSGs, see L(Security Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm). Applicable only to Exadata
              systems.
            - Applicable when creation_type is 'NewDbSystem'
        type: list
    hostname:
        description:
            - The hostname for the DB node.
            - Applicable when creation_type is 'NewDbSystem'
        type: str
    peer_vm_cluster_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM Cluster in which to create the standby database.
              You must supply this value if creationType is `ExistingVmCluster`.
            - Applicable when creation_type is 'ExistingVmCluster'
        type: str
    peer_db_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system in which to create the standby database.
              You must supply this value if creationType is `ExistingDbSystem`.
            - Applicable when creation_type is 'ExistingDbSystem'
        type: str
    state:
        description:
            - The state of the DataGuardAssociation.
            - Use I(state=present) to create a DataGuardAssociation.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create data_guard_association
  oci_database_data_guard_association:
    database_id: ocid1.database.oc1..xxxxxxEXAMPLExxxxxx
    database_admin_password: database_admin_password_example
    protection_mode: MAXIMUM_AVAILABILITY
    transport_type: SYNC
    creation_type: ExistingDbSystem

"""

RETURN = """
data_guard_association:
    description:
        - Details of the DataGuardAssociation resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Data Guard association.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the reporting database.
            returned: on success
            type: string
            sample: ocid1.database.oc1..xxxxxxEXAMPLExxxxxx
        role:
            description:
                - The role of the reporting database in this Data Guard association.
            returned: on success
            type: string
            sample: PRIMARY
        lifecycle_state:
            description:
                - The current state of the Data Guard association.
            returned: on success
            type: string
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState, if available.
            returned: on success
            type: string
            sample: lifecycle_details_example
        peer_db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system containing the associated
                  peer database.
            returned: on success
            type: string
            sample: ocid1.peerdbsystem.oc1..xxxxxxEXAMPLExxxxxx
        peer_db_home_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Home containing the associated peer
                  database.
            returned: on success
            type: string
            sample: ocid1.peerdbhome.oc1..xxxxxxEXAMPLExxxxxx
        peer_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the associated peer database.
            returned: on success
            type: string
            sample: ocid1.peerdatabase.oc1..xxxxxxEXAMPLExxxxxx
        peer_data_guard_association_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the peer database's Data Guard association.
            returned: on success
            type: string
            sample: ocid1.peerdataguardassociation.oc1..xxxxxxEXAMPLExxxxxx
        peer_role:
            description:
                - The role of the peer database in this Data Guard association.
            returned: on success
            type: string
            sample: PRIMARY
        apply_lag:
            description:
                - The lag time between updates to the primary database and application of the redo data on the standby database,
                  as computed by the reporting database.
                - "Example: `9 seconds`"
            returned: on success
            type: string
            sample: 9 seconds
        apply_rate:
            description:
                - The rate at which redo logs are synced between the associated databases.
                - "Example: `180 Mb per second`"
            returned: on success
            type: string
            sample: 180 Mb per second
        protection_mode:
            description:
                - The protection mode of this Data Guard association. For more information, see
                  L(Oracle Data Guard Protection Modes,http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)
                  in the Oracle Data Guard documentation.
            returned: on success
            type: string
            sample: MAXIMUM_AVAILABILITY
        transport_type:
            description:
                - The redo transport type used by this Data Guard association.  For more information, see
                  L(Redo Transport Services,http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400)
                  in the Oracle Data Guard documentation.
            returned: on success
            type: string
            sample: SYNC
        time_created:
            description:
                - The date and time the Data Guard association was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "role": "PRIMARY",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "peer_db_system_id": "ocid1.peerdbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_db_home_id": "ocid1.peerdbhome.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_database_id": "ocid1.peerdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_data_guard_association_id": "ocid1.peerdataguardassociation.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_role": "PRIMARY",
        "apply_lag": "9 seconds",
        "apply_rate": "180 Mb per second",
        "protection_mode": "MAXIMUM_AVAILABILITY",
        "transport_type": "SYNC",
        "time_created": "2013-10-20T19:20:30+01:00"
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
    from oci.database.models import CreateDataGuardAssociationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataGuardAssociationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get and list"""

    def __init__(self, *args, **kwargs):
        super(DataGuardAssociationHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_get_fn(self):
        return self.client.get_data_guard_association

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_guard_association,
            database_id=self.module.params.get("database_id"),
            data_guard_association_id=self.module.params.get(
                "data_guard_association_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "database_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_data_guard_associations, **kwargs
        )

    def get_create_model_class(self):
        return CreateDataGuardAssociationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_data_guard_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_id=self.module.params.get("database_id"),
                create_data_guard_association_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataGuardAssociationHelperCustom = get_custom_class("DataGuardAssociationHelperCustom")


class ResourceHelper(DataGuardAssociationHelperCustom, DataGuardAssociationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            database_id=dict(type="str", required=True),
            database_admin_password=dict(type="str", required=True, no_log=True),
            protection_mode=dict(
                type="str",
                required=True,
                choices=[
                    "MAXIMUM_AVAILABILITY",
                    "MAXIMUM_PERFORMANCE",
                    "MAXIMUM_PROTECTION",
                ],
            ),
            transport_type=dict(
                type="str", required=True, choices=["SYNC", "ASYNC", "FASTSYNC"]
            ),
            creation_type=dict(
                type="str",
                required=True,
                choices=["NewDbSystem", "ExistingVmCluster", "ExistingDbSystem"],
            ),
            display_name=dict(aliases=["name"], type="str"),
            availability_domain=dict(type="str"),
            shape=dict(type="str"),
            subnet_id=dict(type="str"),
            nsg_ids=dict(type="list"),
            backup_network_nsg_ids=dict(type="list"),
            hostname=dict(type="str"),
            peer_vm_cluster_id=dict(type="str"),
            peer_db_system_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="data_guard_association",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
