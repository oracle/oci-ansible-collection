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
module: oci_instance_console_connection_facts
short_description: Retrieve facts of instance_console_connections in Oracle Cloud Infrastructure
description:
    - This module retrieves information of a specified instance console connection or all instance console connections
      in the specified compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment the resource belongs to. Use I(instance_console_connection_id) to
                     retrieve a specific instance console connection.
        required: false
    instance_console_connection_id:
        description: OCID of the target instance console connection.
        required: false
        aliases: ['id']
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [oracle]
"""

EXAMPLES = """
- name: Get a list of instance_console_connections in the specified compartment
  oci_instance_console_connection_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...abcd

- name: Gets details of a specific instance console connection using its OCID
  oci_instance_console_connection_facts:
    instance_console_connection_id: ocid1.instanceconsoleconnection.oc1.iad.xxxxxEXAMPLExxxxx...3fhq
"""

RETURN = """
instance_console_connections:
    description: List of instance console connection details
    returned: always
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment to contain the console connection.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...abcd
        connection_string:
            description: The SSH connection string for the console connection.
            returned: always
            type: string
            sample: "ssh -o ProxyCommand='ssh -W %h:%p -p 443
                     ocid1.instanceconsoleconnection.oc1.iad.xxxxxEXAMPLExxxxx...enxq@
                     instance-console.us-ashburn-1.oraclecloud.com' ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx...2ema"
        fingerprint:
            description: The SSH public key fingerprint for the console connection.
            returned: always
            type: list
            sample: "d2:ac:ff:31:9c:23:79:9c:41:ba:a7:ab:e2:a6:8e:76"
        id:
            description: The OCID of the console connection.
            returned: always
            type: string
            sample: ocid1.instanceconsoleconnection.oc1.phx.xxxxxEXAMPLExxxxx...rz3fhq
        instance_id:
            description: The OCID of the instance the console connection connects to.
            returned: always
            type: string
            sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq
        lifecycle_state:
            description: The current state of the console connection.
            returned: always
            type: string
            sample: "ACTIVE"
        vnc_connection_string:
            description: The SSH connection string for the SSH tunnel used to connect to the console connection over
                         VNC.
            returned: always
            type: string
            sample: "ssh -o ProxyCommand='ssh -W %h:%p -p 443
                     ocid1.instanceconsoleconnection.oc1.iad.xxxxxEXAMPLExxxxx...iwenxq@
                     instance-console.us-ashburn-1.oraclecloud.com' -N -L
                     localhost:5900:ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx...2ema:5900
                     ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx...2ema"
    sample: [{
                "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                "connection-string": "ssh -o ProxyCommand='ssh -W %h:%p -p 443
                                      ocid1.instanceconsoleconnection.oc1.iad.xxxxxEXAMPLExxxxx...3fhq@
                                      instance-console.us-ashburn-1.oraclecloud.com'
                                      ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx...whsma",
                "defined-tags": {},
                "fingerprint": "SHA256:DlBfSLjZMvFPlOKOfN403dSSn/ywiW905oKfZvpD37Q",
                "freeform-tags": {},
                "id": "ocid1.instanceconsoleconnection.oc1.iad.xxxxxEXAMPLExxxxx...3fhq",
                "instance-id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx...hsma",
                "lifecycle-state": "ACTIVE",
                "vnc-connection-string": "ssh -o ProxyCommand='ssh -W %h:%p -p 443
                                          ocid1.instanceconsoleconnection.oc1.iad.xxxxxEXAMPLExxxxx...z3fhq@
                                          instance-console.us-ashburn-1.oraclecloud.com'
                                         -N -L localhost:5900:ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx...whsma:5900
                                         ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx...whsma"
        }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.compute_client import ComputeClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            instance_console_connection_id=dict(
                type="str", required=False, aliases=["id"]
            ),
            compartment_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["instance_console_connection_id", "compartment_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    instance_console_connection_id = module.params["instance_console_connection_id"]
    compartment_id = module.params["compartment_id"]

    try:
        if instance_console_connection_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        compute_client.get_instance_console_connection,
                        instance_console_connection_id=instance_console_connection_id,
                    ).data
                )
            ]
        elif compartment_id is not None:
            result = to_dict(
                oci_utils.list_all_resources(
                    compute_client.list_instance_console_connections,
                    compartment_id=compartment_id,
                )
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(instance_console_connections=result)


if __name__ == "__main__":
    main()
