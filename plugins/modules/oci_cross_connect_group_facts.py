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
module: oci_cross_connect_group_facts
short_description: Fetches details of one or more OCI cross-connect groups
description:
     - Fetches details of a specified OCI cross-connect group or all cross-connect groups in a specified compartment.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which the specified cross-connect group exists
        required: false
    cross_connect_group_id:
        description: Identifier of the cross-connect whose details needs to be fetched.
        required: false
        aliases: [ 'id' ]
    lifecycle_state:
        description: A filter to return only resources that match the given lifecycle state.
        required: false
        choices: ["PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_display_name_option  ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Fetch All Cross Connects Groups under a specific compartment
- name: Fetch All Cross Connects Groups under a specific compartment
  oci_cross_connect_group_facts:
      compartment_id: 'ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx'


# Fetch All cross-connect groups under a specific compartment, filtered by
# display name and lifecycle state
- name: Fetch All cross-connect groups under a specific compartment, filtered by display name and lifecycle state
  oci_cross_connect_group_facts:
      compartment_id: 'ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx'
      display_name: 'ansible-cross-connect-group'
      lifecycle_state: 'PROVISIOING'

# Fetch a specific cross-connect group
- name: Fetch a specific cross-connect group
  oci_cross_connect_group_facts:
      cross_connect_group_id: 'ocid1.crossconnectgroup.oc1.iad.xxxxxEXAMPLExxxxx'
"""

RETURN = """
    oci_cross_connect_groups:
        description: Attributes of the cross-connect group.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The OCID of the compartment containing the cross-connect group.
                returned: always
                type: string
                sample: ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx
            display_name:
                description: A user-friendly name. Does not have to be unique, and it's changeable.
                             Avoid entering confidential information.
                returned: always
                type: string
                sample: ansible-cross-connect-group
            id:
                description: Identifier of the cross-connect group.
                returned: always
                type: string
                sample: ocid1.crossconnectgroup.oc1.iad.xxxxxEXAMPLExxxxx
            time_created:
                description: Date and time when the Cross Connect was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            lifecycle_state:
                description: The current state of the Cross Connect.
                returned: always
                type: string
                sample: PROVISIONED
        sample: [{
                    "compartment_id":"ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx",
                    "display_name":"ansible-cross-connect-group",
                    "id":"ocid1.crossconnectgroup.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_state":"PROVISIONING",
                    "time_created":"2018-03-03T06:55:49.463000+00:00"
                },
                {
                    "compartment_id":"ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx",
                    "display_name":"test-cross-connect",
                    "id":"ocid1.crossconnectgroup.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_state":"PROVISIONING",
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


def list_cross_connect_groups(virtual_network_client, module):
    result = dict(cross_connect_groups="")
    compartment_id = module.params.get("compartment_id")
    cross_connect_group_id = module.params.get("cross_connect_group_id")
    try:
        if compartment_id:
            optional_list_method_params = ["display_name", "lifecycle_state"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            existing_cross_connect_groups = oci_utils.list_all_resources(
                virtual_network_client.list_cross_connect_groups,
                compartment_id=compartment_id,
                **optional_kwargs
            )
        elif cross_connect_group_id:
            response = oci_utils.call_with_backoff(
                virtual_network_client.list_cross_connect_groups,
                cross_connect_group_id=cross_connect_group_id,
            )
            existing_cross_connect_groups = [response.data]
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    result["cross_connect_groups"] = to_dict(existing_cross_connect_groups)
    return result


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            cross_connect_group_id=dict(type="str", required=False, aliases=["id"]),
            lifecycle_state=dict(
                type="str",
                required=False,
                choices=[
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
        argument_spec=module_args, mutually_exclusive=[["compartment_id", "id"]]
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    result = list_cross_connect_groups(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
