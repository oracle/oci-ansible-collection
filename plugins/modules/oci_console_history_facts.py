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
module: oci_console_history_facts
short_description: Retrieve facts of console histories in Oracle Cloud Infrastructure
description:
    - This module retrieves information of a specified console history or all console histories
      in the specified compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment the resource belongs to. Use I(instance_console_history_id) to
                     retrieve a specific console history.
        required: false
    instance_id:
        description: The OCID of the instance.
        required: false
    instance_console_history_id:
        description: OCID of the target console history.
        required: false
        aliases: ['id']
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [oracle]
"""

EXAMPLES = """
- name: Get a list of console_histories in the specified compartment
  oci_console_history_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...abcd

- name: Get a list of console_histories in the specified compartment for a specific instance
  oci_console_history_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...abcd
    instance_id: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq

- name: Gets details of a specific console history using its OCID
  oci_console_history_facts:
    instance_console_history_id: ocid1.consolehistory.oc1.iad.xxxxxEXAMPLExxxxx...tc7a
"""

RETURN = """
console_histories:
    description: List of console history details
    returned: always
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
    sample: [{
                "availability-domain": "IwGV:US-ASHBURN-AD-3",
                "compartment-id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...2bla",
                "defined-tags": {},
                "display-name": "consolehistory20181105135801",
                "freeform-tags": {},
                "id": "ocid1.consolehistory.oc1.iad.xxxxxEXAMPLExxxxx...tc7a",
                "instance-id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx...he5q",
                "lifecycle-state": "REQUESTED",
                "time-created": "2018-11-05T13:58:01.944000+00:00"
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
            instance_console_history_id=dict(
                type="str", required=False, aliases=["id"]
            ),
            compartment_id=dict(type="str", required=False),
            instance_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["instance_console_history_id", "compartment_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    instance_console_history_id = module.params["instance_console_history_id"]
    compartment_id = module.params["compartment_id"]

    try:
        if instance_console_history_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        compute_client.get_console_history,
                        instance_console_history_id=instance_console_history_id,
                    ).data
                )
            ]
        elif compartment_id is not None:
            optional_list_method_params = ["instance_id"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            result = to_dict(
                oci_utils.list_all_resources(
                    compute_client.list_console_histories,
                    compartment_id=compartment_id,
                    **optional_kwargs
                )
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(console_histories=result)


if __name__ == "__main__":
    main()
