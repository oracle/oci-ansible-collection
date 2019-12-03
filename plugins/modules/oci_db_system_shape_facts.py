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
module: oci_db_system_shape_facts
short_description: Fetches details of all DB System Shapes
description:
    - Fetches details of all DB System Shapes.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment where DB Systems should be
                     created whose Shapes needs to be fetched
        required: true
    availability_domain:
        description: Availability Domain where DB Systems should belong.
        required: true
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_name_option ]
"""
EXAMPLES = """
#Fetch DB System Shapes
- name: Fetch all DB System Shapes
  oci_db_system_shape_facts:
    compartment_id: 'ocid1.compartment.aaaa'
    availability_domain: 'AD2'
"""

RETURN = """
    db_system_shapes:
        description: Attributes of the DB System Shape.
        returned: success
        type: complex
        contains:
            available_core_count:
                description: The maximum number of CPU cores that can be enabled
                             on the DB System.
                returned: always
                type: string
                sample: 4
            name:
                description: The name of the shape used for the DB System.
                returned: always
                type: string
                sample: VM.Standard1.4
            shape:
                description: Deprecated. Use name instead of shape.
                returned: always
                type: string
                sample: VM.Standard1.4

        sample: [{
                    "available_core_count":4,
                    "name":"VM.Standard1.4",
                    "shape":"VM.Standard1.4"
                },
                {
                    "available_core_count":84,
                    "name":"Exadata.Quarter1.84",
                    "shape":"Exadata.Quarter1.84"
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


def list_db_system_shapes(db_client, module):
    result = dict(db_system_shapes="")
    compartment_id = module.params.get("compartment_id")
    availability_domain = module.params.get("availability_domain")
    try:
        get_logger().debug(
            "Listing all DB System Shapes under Availability Domain %s compartment %s",
            compartment_id,
            availability_domain,
        )
        db_system_shapes = oci_utils.list_all_resources(
            db_client.list_db_system_shapes,
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            name=module.params["name"],
        )
    except ServiceError as ex:
        get_logger().error("Unable to list DB System Shapes due to %s", ex.message)
        module.fail_json(msg=ex.message)

    result["db_system_shapes"] = to_dict(db_system_shapes)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_db_system_shape_facts")
    set_logger(logger)
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_name=True)
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            availability_domain=dict(type="str", required=True),
        )
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)
    result = list_db_system_shapes(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
