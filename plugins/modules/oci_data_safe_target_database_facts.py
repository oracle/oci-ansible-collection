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
module: oci_data_safe_target_database_facts
short_description: Fetches details about one or multiple TargetDatabase resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TargetDatabase resources in Oracle Cloud Infrastructure
    - Returns the list of registered target databases in Data Safe.
    - If I(target_database_id) is specified, the details of a single TargetDatabase will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    target_database_id:
        description:
            - The OCID of the Data Safe target database.
            - Required to get a specific target_database.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - A filter to return only resources that match the specified compartment OCID.
            - Required to list multiple target_databases.
        type: str
    associated_resource_id:
        description:
            - A filter to return the target databases that are associated to the resource id passed in as a parameter value.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the specified display name.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return the target databases that matches the current state of the target database.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "NEEDS_ATTENTION"
            - "FAILED"
    database_type:
        description:
            - A filter to return target databases that match the database type of the target database.
        type: str
        choices:
            - "DATABASE_CLOUD_SERVICE"
            - "AUTONOMOUS_DATABASE"
            - "INSTALLED_DATABASE"
    infrastructure_type:
        description:
            - A filter to return target databases that match the infrastructure type of the target database.
        type: str
        choices:
            - "ORACLE_CLOUD"
            - "CLOUD_AT_CUSTOMER"
            - "ON_PREMISES"
            - "NON_ORACLE_CLOUD"
    compartment_id_in_subtree:
        description:
            - Default is false.
              When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the
              'accessLevel' setting.
        type: bool
    access_level:
        description:
            - Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED.
              Setting this to ACCESSIBLE returns only those compartments for which the
              user has INSPECT permissions directly or indirectly (permissions can be on a
              resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
        type: str
        choices:
            - "RESTRICTED"
            - "ACCESSIBLE"
    sort_order:
        description:
            - The sort order to use, either ascending (ASC) or descending (DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field used for sorting. Only one sorting order (sortOrder) can be specified.
              The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending.
              The DISPLAYNAME sort order is case sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific target_database
  oci_data_safe_target_database_facts:
    # required
    target_database_id: "ocid1.targetdatabase.oc1..xxxxxxEXAMPLExxxxxx"

- name: List target_databases
  oci_data_safe_target_database_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    target_database_id: "ocid1.targetdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    associated_resource_id: "ocid1.associatedresource.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: CREATING
    database_type: DATABASE_CLOUD_SERVICE
    infrastructure_type: ORACLE_CLOUD
    compartment_id_in_subtree: true
    access_level: RESTRICTED
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
target_databases:
    description:
        - List of TargetDatabase resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment which contains the Data Safe target database.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The OCID of the Data Safe target database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the target database in Data Safe.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The description of the target database in Data Safe.
            returned: on success
            type: str
            sample: description_example
        database_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                database_type:
                    description:
                        - The database type.
                    returned: on success
                    type: str
                    sample: DATABASE_CLOUD_SERVICE
                infrastructure_type:
                    description:
                        - The infrastructure type the database is running on.
                    returned: on success
                    type: str
                    sample: ORACLE_CLOUD
                autonomous_database_id:
                    description:
                        - The OCID of the autonomous database registered as a target database in Data Safe.
                    returned: on success
                    type: str
                    sample: "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"
                vm_cluster_id:
                    description:
                        - The OCID of the VM cluster in which the database is running.
                    returned: on success
                    type: str
                    sample: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"
                db_system_id:
                    description:
                        - The OCID of the cloud database system registered as a target database in Data Safe.
                    returned: on success
                    type: str
                    sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
                service_name:
                    description:
                        - The database service name.
                    returned: on success
                    type: str
                    sample: service_name_example
                instance_id:
                    description:
                        - The OCID of the compute instance on which the database is running.
                    returned: on success
                    type: str
                    sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
                ip_addresses:
                    description:
                        - The list of database host IP Addresses. Fully qualified domain names can be used if connectionType is 'ONPREM_CONNECTOR'.
                    returned: on success
                    type: list
                    sample: []
                listener_port:
                    description:
                        - The port number of the database listener.
                    returned: on success
                    type: int
                    sample: 56
        credentials:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                user_name:
                    description:
                        - The database user name.
                    returned: on success
                    type: str
                    sample: user_name_example
                password:
                    description:
                        - The password of the database user.
                    returned: on success
                    type: str
                    sample: example-password
        tls_config:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                status:
                    description:
                        - Status to represent whether the database connection is TLS enabled or not.
                    returned: on success
                    type: str
                    sample: ENABLED
                certificate_store_type:
                    description:
                        - The format of the certificate store.
                    returned: on success
                    type: str
                    sample: JKS
                store_password:
                    description:
                        - The password to read the trust store and key store files, if they are password protected.
                    returned: on success
                    type: str
                    sample: example-password
                trust_store_content:
                    description:
                        - Base64 encoded string of trust store file content.
                    returned: on success
                    type: str
                    sample: trust_store_content_example
                key_store_content:
                    description:
                        - Base64 encoded string of key store file content.
                    returned: on success
                    type: str
                    sample: key_store_content_example
        connection_option:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                connection_type:
                    description:
                        - "The connection type used to connect to the database. Allowed values:
                          - PRIVATE_ENDPOINT - Represents connection through private endpoint in Data Safe.
                          - ONPREM_CONNECTOR - Represents connection through on-premises connector in Data Safe."
                    returned: on success
                    type: str
                    sample: PRIVATE_ENDPOINT
                on_prem_connector_id:
                    description:
                        - The OCID of the on-premises connector.
                    returned: on success
                    type: str
                    sample: "ocid1.onpremconnector.oc1..xxxxxxEXAMPLExxxxxx"
                datasafe_private_endpoint_id:
                    description:
                        - The OCID of the Data Safe private endpoint.
                    returned: on success
                    type: str
                    sample: "ocid1.datasafeprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        associated_resource_ids:
            description:
                - The OCIDs of associated resources like Database, Data Safe private endpoint etc.
            returned: on success
            type: list
            sample: []
        lifecycle_state:
            description:
                - The current state of the target database in Data Safe.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details about the current state of the target database in Data Safe.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time of target database registration and creation in Data Safe.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time of the target database update in Data Safe.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        infrastructure_type:
            description:
                - The infrastructure type the database is running on.
                - Returned for list operation
            returned: on success
            type: str
            sample: ORACLE_CLOUD
        database_type:
            description:
                - The database type.
                - Returned for list operation
            returned: on success
            type: str
            sample: DATABASE_CLOUD_SERVICE
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "database_details": {
            "database_type": "DATABASE_CLOUD_SERVICE",
            "infrastructure_type": "ORACLE_CLOUD",
            "autonomous_database_id": "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx",
            "vm_cluster_id": "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx",
            "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
            "service_name": "service_name_example",
            "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
            "ip_addresses": [],
            "listener_port": 56
        },
        "credentials": {
            "user_name": "user_name_example",
            "password": "example-password"
        },
        "tls_config": {
            "status": "ENABLED",
            "certificate_store_type": "JKS",
            "store_password": "example-password",
            "trust_store_content": "trust_store_content_example",
            "key_store_content": "key_store_content_example"
        },
        "connection_option": {
            "connection_type": "PRIVATE_ENDPOINT",
            "on_prem_connector_id": "ocid1.onpremconnector.oc1..xxxxxxEXAMPLExxxxxx",
            "datasafe_private_endpoint_id": "ocid1.datasafeprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "associated_resource_ids": [],
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "infrastructure_type": "ORACLE_CLOUD",
        "database_type": "DATABASE_CLOUD_SERVICE"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_safe import DataSafeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeTargetDatabaseFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "target_database_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_database,
            target_database_id=self.module.params.get("target_database_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "associated_resource_id",
            "target_database_id",
            "display_name",
            "lifecycle_state",
            "database_type",
            "infrastructure_type",
            "compartment_id_in_subtree",
            "access_level",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_target_databases,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataSafeTargetDatabaseFactsHelperCustom = get_custom_class(
    "DataSafeTargetDatabaseFactsHelperCustom"
)


class ResourceFactsHelper(
    DataSafeTargetDatabaseFactsHelperCustom, DataSafeTargetDatabaseFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            target_database_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            associated_resource_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "NEEDS_ATTENTION",
                    "FAILED",
                ],
            ),
            database_type=dict(
                type="str",
                choices=[
                    "DATABASE_CLOUD_SERVICE",
                    "AUTONOMOUS_DATABASE",
                    "INSTALLED_DATABASE",
                ],
            ),
            infrastructure_type=dict(
                type="str",
                choices=[
                    "ORACLE_CLOUD",
                    "CLOUD_AT_CUSTOMER",
                    "ON_PREMISES",
                    "NON_ORACLE_CLOUD",
                ],
            ),
            compartment_id_in_subtree=dict(type="bool"),
            access_level=dict(type="str", choices=["RESTRICTED", "ACCESSIBLE"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="target_database",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(target_databases=result)


if __name__ == "__main__":
    main()
