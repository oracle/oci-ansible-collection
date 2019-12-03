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
module: oci_console_history
short_description: Manage console histories for compute instances in OCI
description:
    - This module allows the user to capture and delete most recent serial console data (console history) for a
      specific compute instance in OCI. By default, during capture of a console history, this module waits until the
      console history is captured (ie lifecycle_state reaches SUCCEEDED (or FAILED)). If you would like to return
      immediately without waiting for the console history's capture to be completed, use I(wait=False).
version_added: "2.5"
options:
    name:
        description: A user-friendly name. Does not have to be unique, and it's changeable.
        required: false
        aliases: ['display_name']
    instance_id:
        description: The OCID of the instance to get the console history from. Required to capture a console history.
        required: false
    instance_console_history_id:
        description: The OCID of the console history. Required to delete a console history.
        required: false
        aliases: ['id']
    state:
        description: Create a console history with I(state=present). Use I(state=absent) to delete an
                     console history.
        required: false
        default: present
        choices: ['present', 'absent']
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create a console history
  oci_console_history:
    instance_id: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq
    name: my_instance_1_console_history

- name: Update the display name of a specific console history
  oci_console_history:
    id: ocid1.consolehistory.oc1.iad.xxxxxEXAMPLExxxxx...tc7a
    name: my_old_instance_1_console_history

- name: Delete a console history
  oci_console_history:
    id: ocid1.consolehistory.oc1.iad.xxxxxEXAMPLExxxxx...tc7a
    state: absent
"""

RETURN = """
console_history:
    description: Information about the console history of an OCI compute instance
    returned: On successful capture, delete operations on console histories
    type: complex
    contains:
        availability_domain:
            description: The availability domain of an instance.
            returned: always
            type: string
            sample: Uocm:PHX-AD-1
        compartment_id:
            description: The OCID of the compartment.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...2bla"
        defined_tags:
            description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: always
            type: string
            sample: '{"Operations": {"CostCenter": "42"}}'
        display_name:
            description: A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering
                         confidential information.
            returned: always
            type: string
            sample: "My console history metadata"
        freeform_tags:
            description: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                         type, or namespace.
            returned: always
            type: string
            sample: '{"Department": "Finance"}'
        id:
            description: The OCID of the console history metadata object.
            returned: always
            type: string
            sample: "ocid1.consolehistory.oc1.iad.xxxxxEXAMPLExxxxx...tc7a"
        instance_id:
            description: The OCID of the instance this console history was fetched from.
            returned: always
            type: string
            sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq
        lifecycle_state:
            description: The current state of the console history.
            returned: always
            type: string
            sample: "ACTIVE"
        time_created:
            description: The date and time the history was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: "2016-08-25T21:10:29.600Z"
    sample: {
                "availability-domain": "IwGV:US-ASHBURN-AD-3",
                "compartment-id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...2bla",
                "defined-tags": {},
                "display-name": "consolehistory20181105135801",
                "freeform-tags": {},
                "id": "ocid1.consolehistory.oc1.iad.xxxxxEXAMPLExxxxx...tc7a",
                "instance-id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx...he5q",
                "lifecycle-state": "REQUESTED",
                "time-created": "2018-11-05T13:58:01.944000+00:00"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.compute_client import ComputeClient
    from oci.core.models import (
        CaptureConsoleHistoryDetails,
        UpdateConsoleHistoryDetails,
    )

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def delete_console_history(compute_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="console_history",
        client=compute_client,
        get_fn=compute_client.get_console_history,
        kwargs_get={
            "instance_console_history_id": module.params["instance_console_history_id"]
        },
        delete_fn=compute_client.delete_console_history,
        kwargs_delete={
            "instance_console_history_id": module.params["instance_console_history_id"]
        },
        module=module,
    )
    return result


def update_console_history(compute_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type="console_history",
        client=compute_client,
        get_fn=compute_client.get_console_history,
        kwargs_get={
            "instance_console_history_id": module.params["instance_console_history_id"]
        },
        update_fn=compute_client.update_console_history,
        primitive_params_update=["instance_console_history_id"],
        kwargs_non_primitive_update={
            UpdateConsoleHistoryDetails: "update_console_history_details"
        },
        module=module,
        update_attributes=UpdateConsoleHistoryDetails().attribute_map.keys(),
    )
    return result


def capture_console_history(compute_client, module):
    capture_console_history_details = CaptureConsoleHistoryDetails()
    for attribute in capture_console_history_details.attribute_map:
        if attribute in module.params:
            setattr(
                capture_console_history_details, attribute, module.params[attribute]
            )

    result = oci_utils.create_and_wait(
        resource_type="console_history",
        create_fn=compute_client.capture_console_history,
        kwargs_create={
            "capture_console_history_details": capture_console_history_details
        },
        client=compute_client,
        get_fn=compute_client.get_console_history,
        get_param="instance_console_history_id",
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
            name=dict(type="str", required=False, aliases=["display_name"]),
            instance_console_history_id=dict(
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
        mutually_exclusive=[("console_history_id", "instance_id")],
        required_if=[("state", "absent", ["instance_console_history_id"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    state = module.params["state"]

    if state == "absent":
        result = delete_console_history(compute_client, module)

    else:
        console_history_id = module.params["instance_console_history_id"]
        if console_history_id is not None:
            # Update service gateway details.
            result = update_console_history(compute_client, module)
        else:
            instance_id = module.params["instance_id"]

            kwargs_list = {
                "instance_id": instance_id,
                "compartment_id": _get_compartment_of_instance(
                    compute_client, instance_id
                ),
            }

            result = oci_utils.check_and_create_resource(
                resource_type="console_history",
                create_fn=capture_console_history,
                kwargs_create={"compute_client": compute_client, "module": module},
                list_fn=compute_client.list_console_histories,
                kwargs_list=kwargs_list,
                module=module,
                model=CaptureConsoleHistoryDetails(),
            )
    module.exit_json(**result)


if __name__ == "__main__":
    main()
