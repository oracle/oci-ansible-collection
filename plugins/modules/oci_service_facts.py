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
module: oci_service_facts
short_description: Retrieve the available services that you can access through a service gateway in this region
description:
    - This module retrieves information of a specific service or information of all the available services that you can
      access through a service gateway in this region.
options:
    service_id:
        description: The OCID of the service. I(service_id) is required to get a specific service's information.
        required: false
        aliases: [ 'id' ]
version_added: "2.5"
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_name_option ]
"""

EXAMPLES = """
- name: Get details of all the available services
  oci_service_facts:

- name: Get details of a specific service using its OCID
  oci_service_facts:
    id: "ocid1.service.oc1.phx.xxxxxEXAMPLExxxxx"

- name: Get details of a service using its name
  oci_service_facts:
    name: 'OCI IAD Object Storage'
"""

RETURN = """
services:
    description: Details of service
    returned: always
    type: complex
    contains:
        name:
            description: Name of the service.
            returned: always
            type: string
            sample: OCI IAD Object Storage
        cidr_block:
            description: A string that represents the public endpoints for the service. When you set up a route rule to
                         route traffic to the service gateway, use this value as the destination CIDR block for the
                         rule.
            returned: always
            type: string
            sample: oci-iad-objectstorage
        description:
            description: Description of the service.
            returned: always
            type: string
            sample: OCI IAD Object Storage
        id:
            description: The service's OCID.
            returned: always
            type: string
            sample: ocid1.service.oc1.phx.xxxxxEXAMPLExxxxx
    sample: [{
            "cidr_block": "oci-iad-objectstorage",
            "description": "OCI IAD Object Storage",
            "id": "ocid1.service.oc1.phx.xxxxxEXAMPLExxxxx",
            "name": "OCI IAD Object Storage"
            }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_name=True)
    module_args.update(
        dict(service_id=dict(type="str", required=False, aliases=["id"]))
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    try:
        if module.params["service_id"]:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        virtual_network_client.get_service,
                        service_id=module.params["service_id"],
                    ).data
                )
            ]
        else:
            result = to_dict(
                oci_utils.list_all_resources(
                    virtual_network_client.list_services, name=module.params["name"]
                )
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(services=result)


if __name__ == "__main__":
    main()
