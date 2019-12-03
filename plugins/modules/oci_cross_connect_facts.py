#!/usr/bin/python
# Copyright (c) 2019, Oracle and/or its affiliates.
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
module: oci_cross_connect_facts
short_description: Fetches details of one or more OCI cross-connects
description:
     - Fetches details of a specified OCI cross-connect or all cross-connects in a specified compartment or
       cross-connect group.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which the specified cross-connect exists
        required: false
    cross_connect_group_id:
        description: Identifier of the cross-connect group under  which the specified cross-connect exists
        required: false
    cross_connect_id:
        description: Identifier of the cross-connect whose details needs to be fetched
        required: false
        aliases: ['id']
    lifecycle_state:
        description: A filter to only return resources that match the given lifecycle state.  The state value is
                     case-insensitive. Allowed values are "PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE",
                     "TERMINATING", "TERMINATED"
        required: false
        choices: ["PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_display_name_option  ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Fetch All cross-connects under a specific compartment
- name: Fetch All cross-connects under a specific compartment
  oci_cross_connect_facts:
      compartment_id: 'ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx'

# Fetch All cross-connects under a specific cross-connect Group
- name: Fetch All cross-connects under a specific cross-connect Group
  oci_cross_connect_facts:
      compartment_id: 'ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx'
      cross_connect_group_id: 'ocid1.crossconnectgroup.oc1.iad.xxxxxEXAMPLExxxxx'

# Fetch All cross-connects under a specific cross-connect Group, filtered by
# display name and lifecycle state
- name: Fetch All cross-connects under a specific cross-connect Group, filtered by display name and lifecycle state
  oci_cross_connect_facts:
      compartment_id: 'ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx'
      cross_connect_group_id: 'ocid1.crossconnectgroup.oc1.iad.xxxxxEXAMPLExxxxx'
      display_name: 'ansible-cross-connect'
      lifecycle_state: 'PROVISIOING'

# Fetch a specific cross-connect
- name: Fetch a specific cross-connect
  oci_cross_connect_facts:
      cross_connect_id: 'ocid1.crossconnect.oc1.iad.xxxxxEXAMPLExxxxx'
"""

RETURN = """
    oci_cross_connects:
        description: Attributes of the cross-connect.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The OCID of the compartment containing the cross-connect group.
                returned: always
                type: string
                sample: ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx
            cross_connect_group_id:
                description: The OCID of the cross-connect group this cross-connect belongs to (if any).
                returned: always
                type: string
                sample: ocid1.crossconnectgroup.oc1.iad.xxxxxEXAMPLExxxxx
            display_name:
                description: A user-friendly name. Does not have to be unique, and it's changeable.
                             Avoid entering confidential information.
                returned: always
                type: string
                sample: ansible-cross-connect
            id:
                description: Identifier of the cross-connect.
                returned: always
                type: string
                sample: ocid1.crossconnect.oc1.iad.xxxxxEXAMPLExxxxx
            time_created:
                description: Date and time when the cross-connect was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            lifecycle_state:
                description: The current state of the cross-connect.
                returned: always
                type: string
                sample: PROVISIONED
            location_name:
                description: The name of the FastConnect location where this cross-connect is installed.
                returned: always
                type: string
                sample: EXAMPLE LOCATION
            port_name:
                description: A string identifying the meet-me room port for this cross-connect.
                returned: always
                type: string
                sample: EXAMPLE
            port_speed_shape_name:
                description: The port speed for this cross-connect.
                returned: always
                type: string
                sample: 10 Gbps
        sample: [{
                    "compartment_id":"ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx",
                    "cross_connect_group_id":"ocid1.crossconnectgroup.oc1.iad.xxxxxEXAMPLExxxxx",
                    "display_name":"ansible-cross-connect",
                    "id":"ocid1.crossconnect.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_state":"PROVISIONING",
                    "location_name":"EXAMPLE LOCATION",
                    "port_name":"EXAMPLE PORT",
                    "port_speed_shape_name":"10 Gbps",
                    "time_created":"2018-03-03T06:55:49.463000+00:00"
                },
                {
                    "compartment_id":"ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx",
                    "cross_connect_group_id":"ocid1.crossconnectgroup.oc1.iad.xxxxxEXAMPLExxxxx",
                    "display_name":"test-cross-connect",
                    "id":"ocid1.crossconnect.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_state":"PROVISIONING",
                    "location_name":"TEST LOCATION",
                    "port_name":"TEST PORT",
                    "port_speed_shape_name":"10 Gbps",
                    "time_created":"2018-03-04T06:55:49.463000+00:00"
                }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.core import VirtualNetworkClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def list_cross_connects(virtual_network_client, module):
    result = dict(cross_connects="")
    compartment_id = module.params.get("compartment_id")
    cross_connect_id = module.params.get("cross_connect_id")
    try:
        if compartment_id:
            optional_list_method_params = [
                "display_name",
                "cross_connect_group_id",
                "lifecycle_state",
            ]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            existing_cross_connects = oci_utils.list_all_resources(
                virtual_network_client.list_cross_connects,
                compartment_id=compartment_id,
                **optional_kwargs
            )
        elif cross_connect_id:
            response = oci_utils.call_with_backoff(
                virtual_network_client.list_cross_connects,
                cross_connect_id=cross_connect_id,
            )
            existing_cross_connects = [response.data]
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    result["cross_connects"] = to_dict(existing_cross_connects)
    return result


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            cross_connect_group_id=dict(type="str", required=False),
            cross_connect_id=dict(type="str", required=False, aliases=["id"]),
            lifecycle_state=dict(
                type="str",
                required=False,
                choices=[
                    "PENDING_CUSTOMER",
                    "PROVISIONING",
                    "PROVISIONED",
                    "INACTIVE",
                    "TERMINATING",
                    "TERMINATED",
                ],
            ),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["compartment_id", "id"], ["cross_connect_group_id", "id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    result = list_cross_connects(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
