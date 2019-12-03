#!/usr/bin/python
# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
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
module: oci_instance_console_connection
short_description: Manage Instance Console Connections in OCI
description:
    - This module allows the user to create and delete an Instance Console Connection in OCI.
version_added: "2.5"
options:
    instance_id:
        description: The OCID of the instance to create the console connection to. Required to create an instance
                     console connection.
        required: false
    public_key:
        description: The SSH public key used to authenticate the console connection. Required to create an instance
                     console connection.
        required: false
    instance_console_connection_id:
        description: The OCID of the instance console connection. Required to delete an instance console connection.
        required: false
        aliases: ['id']
    state:
        description: Create an instance console connection with I(state=present). Use I(state=absent) to delete an
                     instance console connection.
        required: false
        default: present
        choices: ['present', 'absent']
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create an instance console connection
  oci_instance_console_connection:
    instance_id: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq
    public_key: "/tmp/id_rsa.pub"

- name: Delete an instance console connection
  oci_instance_console_connection:
    id: ocid1.instanceconsoleconnection.oc1.phx.xxxxxEXAMPLExxxxx...rz3fhq
    state: absent
"""

RETURN = """
instance_console_connection:
    description: Information about the Instance Console Connection
    returned: On successful create, delete operations on instance console connections
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment to contain the console connection.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        connection_string:
            description: The SSH connection string for the console connection.
            returned: always
            type: string
            sample: "ssh -o ProxyCommand='ssh -W %h:%p -p 443
                     ocid1.instanceconsoleconnection.oc1.iad.xxxxxEXAMPLExxxxxxenxq@
                     instance-console.us-ashburn-1.oraclecloud.com' ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxxx...2ema"
        fingerprint:
            description: The SSH public key fingerprint for the console connection.
            returned: always
            type: string
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
    sample: {
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
                                          instance-console.us-ashburn-1.oraclecloud.com' -N -L localhost:5900:
                                          ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx...whsma:5900
                                          ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx...whsma"
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils
from ansible.module_utils.facts.utils import get_file_content

try:
    from oci.core.compute_client import ComputeClient
    from oci.core.models import CreateInstanceConsoleConnectionDetails

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def delete_instance_console_connection(compute_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="instance_console_connection",
        client=compute_client,
        get_fn=compute_client.get_instance_console_connection,
        kwargs_get={
            "instance_console_connection_id": module.params[
                "instance_console_connection_id"
            ]
        },
        delete_fn=compute_client.delete_instance_console_connection,
        kwargs_delete={
            "instance_console_connection_id": module.params[
                "instance_console_connection_id"
            ]
        },
        module=module,
    )
    return result


def create_instance_console_connection(compute_client, module):
    create_instance_console_connection_details = (
        CreateInstanceConsoleConnectionDetails()
    )
    for attribute in create_instance_console_connection_details.attribute_map:
        if attribute in module.params:
            setattr(
                create_instance_console_connection_details,
                attribute,
                module.params[attribute],
            )

    result = oci_utils.create_and_wait(
        resource_type="instance_console_connection",
        create_fn=compute_client.create_instance_console_connection,
        kwargs_create={
            "create_instance_console_connection_details": create_instance_console_connection_details
        },
        client=compute_client,
        get_fn=compute_client.get_instance_console_connection,
        get_param="instance_console_connection_id",
        module=module,
    )
    return result


def _get_compartment_of_instance(compute_client, instance_id):
    return oci_utils.call_with_backoff(
        compute_client.get_instance, instance_id=instance_id
    ).data.compartment_id


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            instance_id=dict(type="str", required=False),
            public_key=dict(type="str", required=False),
            instance_console_connection_id=dict(
                type="str", required=False, aliases=["id"]
            ),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[("instance_console_connection_id", "instance_id")],
        required_if=[
            ("state", "absent", ["instance_console_connection_id"]),
            ("state", "present", ["instance_id", "public_key"]),
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    state = module.params["state"]

    if state == "absent":
        result = delete_instance_console_connection(compute_client, module)

    else:
        # Replace value of `public_key` key by content of file pointed to by the `public_key` param
        module.params["public_key"] = get_file_content(module.params["public_key"])

        instance_id = module.params["instance_id"]
        kwargs_list = {
            "instance_id": instance_id,
            "compartment_id": _get_compartment_of_instance(compute_client, instance_id),
        }

        result = oci_utils.check_and_create_resource(
            resource_type="instance_console_connection",
            create_fn=create_instance_console_connection,
            kwargs_create={"compute_client": compute_client, "module": module},
            list_fn=compute_client.list_instance_console_connections,
            kwargs_list=kwargs_list,
            module=module,
            model=CreateInstanceConsoleConnectionDetails(),
            exclude_attributes=None,
        )
    module.exit_json(**result)


if __name__ == "__main__":
    main()
