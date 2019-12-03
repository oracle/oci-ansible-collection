#!/usr/bin/python
# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
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
module: oci_db_version_facts
short_description: Fetches details of all DB Versions
description:
    - Fetches details of all DB Versions.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment where Database should be
                     created whose supported versions needs to be fetched
        required: true
    db_system_shape:
        description: If provided, filters the results to the set of Database
                     versions which are supported for the given shape.
        required: false
    db_system_id:
        description: The DB system OCID. If provided, filters the results to the set of database versions which are
                     supported for the DB system.
        required: false
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""
EXAMPLES = """
#Fetch All DB Versions
- name: List All DB Versions
  oci_db_version_facts:
      compartment_id: 'ocid1.compartment.aaaa'
#Fetch DB Versions of a Specific DB System Shape
- name: List DB Versions For a Specific Shape
  oci_db_version_facts:
      compartment_id: 'ocid1.compartment.aaaa'
      db_system_shape: 'VM.Standard1.4'
"""

RETURN = """
    db_system_versions:
        description: Attributes of the Database Version.
        returned: success
        type: complex
        contains:
            supports_pdb:
                description: Decides if this version of the Oracle database software supports pluggable
                             database.
                returned: always
                type: boolean
                sample: True
            version:
                description: A valid Oracle database version.
                returned: always
                type: string
                sample: 12.2.0.1
        sample: [{
                    "supports_pdb":false,
                    "version":"11.2.0.4"
                },
                {
                    "supports_pdb":true,
                    "version":"12.1.0.2"
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


def list_db_versions(db_client, module):
    result = dict(db_versions="")
    compartment_id = module.params.get("compartment_id")
    db_system_shape = module.params.get("db_system_shape")
    try:
        if db_system_shape:
            get_logger().debug(
                "Listing all DB Versions under Compartment %s filtered by DB System Shape %s",
                compartment_id,
                db_system_shape,
            )
            optional_list_method_params = ["db_system_shape", "db_system_id"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            db_versions = oci_utils.list_all_resources(
                db_client.list_db_versions,
                compartment_id=compartment_id,
                **optional_kwargs
            )
        else:
            get_logger().debug(
                "Listing all DB Versions under Compartment %s", compartment_id
            )
            db_versions = oci_utils.list_all_resources(
                db_client.list_db_versions, compartment_id=compartment_id
            )
    except ServiceError as ex:
        get_logger().error("Unable to list DB Versions due to %s", ex.message)
        module.fail_json(msg=ex.message)

    result["db_versions"] = to_dict(db_versions)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_db_version_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            db_system_shape=dict(type="str", required=False),
            db_system_id=dict(type="str", required=False),
        )
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)
    result = list_db_versions(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
