#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_database_management_managed_database_facts
short_description: Fetches details about one or multiple ManagedDatabase resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagedDatabase resources in Oracle Cloud Infrastructure
    - Gets the Managed Database for a specific ID or the list of Managed Databases in a specific compartment.
      Managed Databases can be filtered based on the name parameter. Only one of the parameters, ID or name
      should be provided. If neither of these parameters is provided, all the Managed Databases in the compartment
      are listed. Managed Databases can also be filtered based on the deployment type and management option.
      If the deployment type is not specified or if it is `ONPREMISE`, then the management option is not
      considered and Managed Databases with `ADVANCED` management option are listed.
    - If I(managed_database_id) is specified, the details of a single ManagedDatabase will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
            - Required to get a specific managed_database.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple managed_databases.
        type: str
    name:
        description:
            - A filter to return only resources that match the entire name.
        type: str
    management_option:
        description:
            - A filter to return Managed Databases with the specified management option.
        type: str
        choices:
            - "BASIC"
            - "ADVANCED"
    deployment_type:
        description:
            - A filter to return Managed Databases of the specified deployment type.
        type: str
        choices:
            - "ONPREMISE"
            - "BM"
            - "VM"
            - "EXADATA"
            - "EXADATA_CC"
    sort_by:
        description:
            - The field to sort information by. Only one sortOrder can be used. The default sort order
              for 'TIMECREATED' is descending and the default sort order for 'NAME' is ascending.
              The 'NAME' sort order is case-sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "NAME"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Ascending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific managed_database
  oci_database_management_managed_database_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"

- name: List managed_databases
  oci_database_management_managed_database_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    management_option: BASIC
    deployment_type: ONPREMISE
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
managed_databases:
    description:
        - List of ManagedDatabase resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the Managed Database.
            returned: on success
            type: str
            sample: name_example
        database_type:
            description:
                - The type of Oracle Database installation.
            returned: on success
            type: str
            sample: EXTERNAL_SIDB
        database_sub_type:
            description:
                - The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.
            returned: on success
            type: str
            sample: CDB
        deployment_type:
            description:
                - The infrastructure used to deploy the Oracle Database.
            returned: on success
            type: str
            sample: ONPREMISE
        management_option:
            description:
                - The management option used when enabling Database Management.
            returned: on success
            type: str
            sample: BASIC
        is_cluster:
            description:
                - Indicates whether the Oracle Database is part of a cluster.
            returned: on success
            type: bool
            sample: true
        parent_container_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the parent Container Database
                  if Managed Database is a Pluggable Database.
            returned: on success
            type: str
            sample: "ocid1.parentcontainer.oc1..xxxxxxEXAMPLExxxxxx"
        managed_database_groups:
            description:
                - A list of Managed Database Groups that the Managed Database belongs to.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database Group.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                name:
                    description:
                        - The name of the Managed Database Group.
                    returned: on success
                    type: str
                    sample: name_example
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the Managed Database
                          Group resides.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the Managed Database was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        database_status:
            description:
                - The status of the Oracle Database. Indicates whether the status of the database
                  is UP, DOWN, or UNKNOWN at the current time.
            returned: on success
            type: str
            sample: UP
        parent_container_name:
            description:
                - The name of the parent Container Database.
            returned: on success
            type: str
            sample: parent_container_name_example
        parent_container_compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
                  in which the parent Container Database resides, if the Managed Database
                  is a Pluggable Database (PDB).
            returned: on success
            type: str
            sample: "ocid1.parentcontainercompartment.oc1..xxxxxxEXAMPLExxxxxx"
        instance_count:
            description:
                - The number of Oracle Real Application Clusters (Oracle RAC) database instances.
            returned: on success
            type: int
            sample: 56
        instance_details:
            description:
                - The details of the Oracle Real Application Clusters (Oracle RAC) database instances.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The ID of the Oracle RAC database instance.
                    returned: on success
                    type: int
                    sample: 56
                name:
                    description:
                        - The name of the Oracle RAC database instance.
                    returned: on success
                    type: str
                    sample: name_example
                host_name:
                    description:
                        - The name of the host of the Oracle RAC database instance.
                    returned: on success
                    type: str
                    sample: host_name_example
                status:
                    description:
                        - The status of the Oracle RAC database instance.
                    returned: on success
                    type: str
                    sample: UP
        pdb_count:
            description:
                - The number of PDBs in the Container Database.
            returned: on success
            type: int
            sample: 56
        pdb_status:
            description:
                - The status of the PDB in the Container Database.
            returned: on success
            type: complex
            contains:
                status:
                    description:
                        - The status of the PDBs with this count.
                    returned: on success
                    type: str
                    sample: UP
                count:
                    description:
                        - The number of PDBs with this status.
                    returned: on success
                    type: int
                    sample: 56
        additional_details:
            description:
                - "The additional details specific to a type of database defined in `{\\"key\\": \\"value\\"}` format.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "database_type": "EXTERNAL_SIDB",
        "database_sub_type": "CDB",
        "deployment_type": "ONPREMISE",
        "management_option": "BASIC",
        "is_cluster": true,
        "parent_container_id": "ocid1.parentcontainer.oc1..xxxxxxEXAMPLExxxxxx",
        "managed_database_groups": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "name": "name_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "database_status": "UP",
        "parent_container_name": "parent_container_name_example",
        "parent_container_compartment_id": "ocid1.parentcontainercompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_count": 56,
        "instance_details": [{
            "id": 56,
            "name": "name_example",
            "host_name": "host_name_example",
            "status": "UP"
        }],
        "pdb_count": 56,
        "pdb_status": [{
            "status": "UP",
            "count": 56
        }],
        "additional_details": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedDatabaseFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "managed_database_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_database,
            managed_database_id=self.module.params.get("managed_database_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "management_option",
            "deployment_type",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_managed_databases,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ManagedDatabaseFactsHelperCustom = get_custom_class("ManagedDatabaseFactsHelperCustom")


class ResourceFactsHelper(
    ManagedDatabaseFactsHelperCustom, ManagedDatabaseFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            management_option=dict(type="str", choices=["BASIC", "ADVANCED"]),
            deployment_type=dict(
                type="str", choices=["ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC"]
            ),
            sort_by=dict(type="str", choices=["TIMECREATED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="managed_database",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(managed_databases=result)


if __name__ == "__main__":
    main()
