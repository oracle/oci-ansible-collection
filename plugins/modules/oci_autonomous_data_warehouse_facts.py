#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_autonomous_data_warehouse_facts
short_description: Fetches details of the OCI Autonomous Data Warehouse instances
description:
    - Fetches details of the OCI Autonomous Data Warehouse instances.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment from which details of all OCI Autonomous Data Warehouse instances
                     must be fetched
        required: false
    autonomous_data_warehouse_id:
        description: Identifier of the Autonomous Data Warehouse whose details needs to be fetched.
        required: false
        aliases: ['id']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
# Fetch Autonomous Data Warehouse
- name: List all Autonomous Data Warehouse in a compartment
  oci_autonomous_data_warehouse_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'

# Fetch Autonomous Data Warehouse, filtered by Display Name
- name: List all Autonomous Data Warehouse in a compartment, filtered by Display Name
  oci_autonomous_data_warehouse_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      display_name: 'ansible-autonoumous-data-warehouse'

# Fetch specific Autonomous Data Warehouse
- name: List a specific Autonomous Data Warehouse
  oci_autonomous_data_warehouse_facts:
      autonomous_data_warehouse_id: 'ocid1.autonomousdwdatabase.oc1..xxxxxEXAMPLExxxxx'
"""

RETURN = """
    autonomous_data_warehouse:
        description: Attributes of the Fetched Autonomous Data Warehouse.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the Autonomous Data Warehouse
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..xxxxxEXAMPLExxxxx
            connection_strings:
                description: The connection string used to connect to the Autonomous Data Warehouse.
                             The username for the Service Console is ADMIN. Use the password you entered
                             when creating the Autonomous Data Warehouse for the password value.
                returned: always
                type: dict
                sample: {"high": "EXAMPLE1.oraclecloud.com:1522/EXAMPLE1.atp.oraclecloud.com",
                         "low": "EXAMPLE2.oraclecloud.com:1522/EXAMPLE2.atp.oraclecloud.com",
                         "medium": "EXAMPLE3.oraclecloud.com:1522/EXAMPLE3.atp.oraclecloud.com"}
            cpu_core_count:
                description: The number of CPU cores to enable.
                returned: always
                type: string
                sample: 2
            time_created:
                description: Date and time when the Autonomous Data Warehouse was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            data_storage_size_in_tbs:
                description: Data storage size, in terrabytes, that is currently available to the Autonomous Data Warehouse.
                returned: always
                type: string
                sample: 2048
            id:
                description: The identifier of the Autonomous Data Warehouse
                returned: always
                type: string
                sample: ocid1.autonomousdwdatabase.oc1.xzvf..xxxxxEXAMPLExxxxx
            display_name:
                description: The user-friendly name for the Autonomous Data Warehouse.
                returned: always
                type: string
                sample: ansibleautodbwarehouse
            db_name:
                description: The database name.
                returned: always
                type: string
                sample: autodbwarehous
            license_model:
                description: The Oracle license model that applies to all the databases
                             on the Autonomous Data Warehouse
                returned: always
                type: string
                sample: LICENSE_INCLUDED
            service_console_url:
                description: The URL of the Service Console for the Autonomous Data Warehouse.
                returned: always
                type: string
                sample: https://example1.oraclecloud.com/console/index.html?
                        tenant_name=OCID1.TENANCY.OC1..xxxxxEXAMPLExxxxx
                        &database_name=AUTODBWAREHOUS&service_type=ADW
            lifecycle_details:
                description: Additional information about the current lifecycle state.
                returned: always
                type: string
                sample: details
            lifecycle_state:
                description: The current state of the Autonomous Data Warehouse.
                returned: always
                type: string
                sample: AVAILABLE

        sample: [{
                  "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                  "connection_strings":{
                                        "high":"adwc.EXAMPLE1.oraclecloud.com:1522/EXAMPLE1_autodbwarehous_high.adwc.oraclecloud.com",
                                        "low":"adwc.EXAMPLE2.oraclecloud.com:1522/EXAMPLE2_autodbwarehous_high.adwc.oraclecloud.com",
                                        "medium":"adwc.EXAMPLE3.oraclecloud.com:1522/EXAMPLE3_autodbwarehous_high.adwc.oraclecloud.com"
                                       },
                  "cpu_core_count":1,
                  "data_storage_size_in_tbs":1,
                  "db_name":"autodbwarehous",
                  "defined_tags":{
                                   "ansible_tag_namespace_integration_test_1":{
                                   "ansible_tag_1":"initial"
                                 }
                                },
                  "display_name":"ansible-autonomous-db-warehouse",
                  "freeform_tags":{
                                   "system_license":"trial"
                                  },
                  "id":"ocid1.autonomousdwdatabase.oc1.iad.xxxxxEXAMPLExxxxx",
                  "license_model":"LICENSE_INCLUDED",
                  "lifecycle_details":null,
                  "lifecycle_state":"AVAILABLE",
                  "service_console_url":"https://adwc.example1.oraclecloud.com/console/index.html?tenant_name=OCID1.TENANCY.OC1..xxxxxEXAMPLExxxxx
                                         &database_name=AUTODBWAREHOUS&service_type=ADW",
                  "time_created":"2018-09-22T16:31:47.181000+00:00"
                 },
                 {
                  "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                  "connection_strings":{
                                        "high":"adwc.EXAMPLE1.oraclecloud.com:1522/EXAMPLE1_autodbwarehous_high.adwc.oraclecloud.com",
                                        "low":"adwc.EXAMPLE2.oraclecloud.com:1522/EXAMPLE2_autodbwarehous_high.adwc.oraclecloud.com",
                                        "medium":"adwc.EXAMPLE3.oraclecloud.com:1522/EXAMPLE3_autodbwarehous_high.adwc.oraclecloud.com"
                                       },
                  "cpu_core_count":1,
                  "data_storage_size_in_tbs":1,
                  "db_name":"autodbwarehous",
                  "defined_tags":{
                                   "ansible_tag_namespace_integration_test_1":{
                                   "ansible_tag_1":"initial"
                                 }
                                },
                  "display_name":"ansible-autonomous-db-warehouse2",
                  "freeform_tags":{
                                   "system_license":"trial"
                                  },
                  "id":"ocid1.autonomousdwdatabase.oc1.iad.xxxxxEXAMPLExxxxx",
                  "license_model":"LICENSE_INCLUDED",
                  "lifecycle_details":null,
                  "lifecycle_state":"AVAILABLE",
                  "service_console_url":"https://adwc.example1.oraclecloud.com/console/index.html?tenant_name=OCID1.TENANCY.OC1..xxxxxEXAMPLExxxxx
                                         &database_name=AUTODBWAREHOUS&service_type=ADW",
                  "time_created":"2018-09-22T16:31:47.181000+00:00"
                 }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.database.database_client import DatabaseClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def list_autonomous_data_warehouses(db_client, module):
    result = dict(autonomous_data_warehouses="")
    compartment_id = module.params.get("compartment_id")
    autonomous_data_warehouse_id = module.params.get("autonomous_data_warehouse_id")
    try:
        if compartment_id:
            get_logger().debug(
                "Listing all Autonomous Data Warehouses under compartment %s",
                compartment_id,
            )
            autonomous_data_warehouses = oci_utils.list_all_resources(
                db_client.list_autonomous_data_warehouses,
                compartment_id=compartment_id,
                display_name=module.params.get("display_name"),
            )
        elif autonomous_data_warehouse_id:
            get_logger().debug(
                "Listing Autonomous Data Warehouse %s", autonomous_data_warehouse_id
            )
            response = oci_utils.call_with_backoff(
                db_client.get_autonomous_data_warehouse,
                autonomous_data_warehouse_id=autonomous_data_warehouse_id,
            )
            autonomous_data_warehouses = [response.data]
    except ServiceError as ex:
        get_logger().error(
            "Unable to list Autonomous Data Warehouse due to %s", ex.message
        )
        module.fail_json(msg=ex.message)
    result["autonomous_data_warehouses"] = to_dict(autonomous_data_warehouses)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_autonomous_data_warehouse_facts")
    set_logger(logger)

    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            autonomous_data_warehouse_id=dict(
                type="str", required=False, aliases=["id"]
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["compartment_id", "autonomous_data_warehouse_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)
    result = list_autonomous_data_warehouses(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
