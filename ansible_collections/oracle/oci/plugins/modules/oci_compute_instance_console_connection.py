#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_compute_instance_console_connection
short_description: Manage an InstanceConsoleConnection resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete an InstanceConsoleConnection resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new console connection to the specified instance.
      After the console connection has been created and is available,
      you connect to the console using SSH.
    - For more information about console access, see L(Accessing the Console,https://docs.cloud.oracle.com/Content/Compute/References/serialconsole.htm).
version_added: "2.5"
options:
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    instance_id:
        description:
            - The OCID of the instance to create the console connection to.
            - Required for create using I(state=present).
        type: str
    public_key:
        description:
            - The SSH public key used to authenticate the console connection.
            - Required for create using I(state=present).
        type: str
    instance_console_connection_id:
        description:
            - The OCID of the instance console connection.
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
        type: str
    state:
        description:
            - The state of the InstanceConsoleConnection.
            - Use I(state=present) to create an InstanceConsoleConnection.
            - Use I(state=absent) to delete an InstanceConsoleConnection.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create instance_console_connection
  oci_compute_instance_console_connection:
    instance_id: ocid1.instance.oc1.phx.unique_ID
    compartment_id: ocid1.compartment.oc1.phx.unique_ID
    public_key: ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz...

- name: Delete instance_console_connection
  oci_compute_instance_console_connection:
    instance_console_connection_id: ocid1.instanceconsoleconnection.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
instance_console_connection:
    description:
        - Details of the InstanceConsoleConnection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment to contain the console connection.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        connection_string:
            description:
                - The SSH connection string for the console connection.
            returned: on success
            type: string
            sample: connection_string_example
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        fingerprint:
            description:
                - The SSH public key fingerprint for the console connection.
            returned: on success
            type: string
            sample: fingerprint_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of the console connection.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        instance_id:
            description:
                - The OCID of the instance the console connection connects to.
            returned: on success
            type: string
            sample: ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of the console connection.
            returned: on success
            type: string
            sample: ACTIVE
        vnc_connection_string:
            description:
                - The SSH connection string for the SSH tunnel used to
                  connect to the console connection over VNC.
            returned: on success
            type: string
            sample: vnc_connection_string_example
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_string": "connection_string_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "fingerprint": "fingerprint_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "vnc_connection_string": "vnc_connection_string_example"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeClient
    from oci.core.models import CreateInstanceConsoleConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceConsoleConnectionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_module_resource_id_param(self):
        return "instance_console_connection_id"

    def get_module_resource_id(self):
        return self.module.params.get("instance_console_connection_id")

    def get_get_fn(self):
        return self.client.get_instance_console_connection

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_console_connection,
            instance_console_connection_id=self.module.params.get(
                "instance_console_connection_id"
            ),
        )

    def list_resources(self):
        required_list_method_params = [
            "compartment_id",
        ]

        optional_list_method_params = [
            "instance_id",
        ]

        required_kwargs = dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

        return oci_common_utils.list_all_resources(
            self.client.list_instance_console_connections, **kwargs
        )

    def get_create_model_class(self):
        return CreateInstanceConsoleConnectionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_instance_console_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_instance_console_connection_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_instance_console_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_console_connection_id=self.module.params.get(
                    "instance_console_connection_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


InstanceConsoleConnectionHelperCustom = get_custom_class(
    "InstanceConsoleConnectionHelperCustom"
)


class ResourceHelper(
    InstanceConsoleConnectionHelperCustom, InstanceConsoleConnectionHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            instance_id=dict(type="str"),
            public_key=dict(type="str"),
            instance_console_connection_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="instance_console_connection",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
