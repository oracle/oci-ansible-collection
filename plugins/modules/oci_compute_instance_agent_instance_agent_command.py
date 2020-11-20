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
module: oci_compute_instance_agent_instance_agent_command
short_description: Manage an InstanceAgentCommand resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete an InstanceAgentCommand resource in Oracle Cloud Infrastructure
    - For I(state=present), create command for one or more managed instances
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment you want to create the command.
            - Required for create using I(state=present).
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    execution_time_out_in_seconds:
        description:
            - Command execution time limit. Zero means no timeout.
            - Required for create using I(state=present).
        type: int
    display_name:
        description:
            - "A user-friendly name for the command. It does not have to be unique.
              Avoid entering confidential information.
              Example: `Database Backup Command`"
            - Required for create, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    target:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            instance_id:
                description:
                    - The target instance OCID
                type: str
    content:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            source:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    source_type:
                        description:
                            - The source type of the command. Use `TEXT` for inlining the command. Use `OBJECT_STORAGE_TUPLE` when specifying
                              the namespace, bucket name, and object name. Use `OBJECT_STORAGE_URI` when specifying the Object Storage URL.
                        type: str
                        choices:
                            - "OBJECT_STORAGE_TUPLE"
                            - "OBJECT_STORAGE_URI"
                            - "TEXT"
                        default: "TEXT"
                    bucket_name:
                        description:
                            - The Object Storage bucket for the command.
                            - Required when source_type is 'OBJECT_STORAGE_TUPLE'
                        type: str
                    namespace_name:
                        description:
                            - The Object Storage namespace for the command.
                            - Required when source_type is 'OBJECT_STORAGE_TUPLE'
                        type: str
                    object_name:
                        description:
                            - The Object Storage name for the command.
                            - Required when source_type is 'OBJECT_STORAGE_TUPLE'
                        type: str
                    source_uri:
                        description:
                            - The Object Storage URL or PAR for the command.
                            - Required when source_type is 'OBJECT_STORAGE_URI'
                        type: str
                    text:
                        description:
                            - The plain text command.
                            - Required when source_type is 'TEXT'
                        type: str
                    text_sha256:
                        description:
                            - Sha256 checksum value of the text content
                            - Applicable when source_type is 'TEXT'
                        type: str
            output:
                description:
                    - ""
                type: dict
                suboptions:
                    output_type:
                        description:
                            - The output type of the command. Use `OBJECT_STORAGE_URI` when specifying the Object Storage URL.
                              Use `OBJECT_STORAGE_TUPLE` when specifying the namespace, bucket name, and object name.
                        type: str
                        choices:
                            - "OBJECT_STORAGE_URI"
                            - "OBJECT_STORAGE_TUPLE"
                            - "TEXT"
                        default: "TEXT"
                    output_uri:
                        description:
                            - The Object Storage URL or PAR for the command output.
                            - Required when output_type is 'OBJECT_STORAGE_URI'
                        type: str
                    bucket_name:
                        description:
                            - The Object Storage bucket for the command output.
                            - Required when output_type is 'OBJECT_STORAGE_TUPLE'
                        type: str
                    namespace_name:
                        description:
                            - The Object Storage namespace for the command output.
                            - Required when output_type is 'OBJECT_STORAGE_TUPLE'
                        type: str
                    object_name:
                        description:
                            - The Object Storage name for the command output.
                            - Required when output_type is 'OBJECT_STORAGE_TUPLE'
                        type: str
    instance_agent_command_id:
        description:
            - The OCID of the command.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the InstanceAgentCommand.
            - Use I(state=present) to create an InstanceAgentCommand.
            - Use I(state=absent) to delete an InstanceAgentCommand.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create instance_agent_command
  oci_compute_instance_agent_instance_agent_command:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    execution_time_out_in_seconds: 56

- name: Delete instance_agent_command
  oci_compute_instance_agent_instance_agent_command:
    instance_agent_command_id: ocid1.instanceagentcommand.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete instance_agent_command using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_instance_agent_instance_agent_command:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    display_name: Database Backup Command
    state: absent

"""

RETURN = """
instance_agent_command:
    description:
        - Details of the InstanceAgentCommand resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The command OCID
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment the command is created in.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The user friendly display name of the command.
            returned: on success
            type: string
            sample: display_name_example
        time_created:
            description:
                - the time command was created at.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - the time command was updated at.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        is_canceled:
            description:
                - Whether the command has been requested to be canceled.
            returned: on success
            type: bool
            sample: true
        execution_time_out_in_seconds:
            description:
                - Command execution time limit that the instance agent will honor when executing the command inside the instance. This timer starts when the
                  instance agent starts the commond. Zero means no timeout.
            returned: on success
            type: int
            sample: 56
        target:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                instance_id:
                    description:
                        - The target instance OCID
                    returned: on success
                    type: string
                    sample: ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx
        content:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                source:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        source_type:
                            description:
                                - The source type of the command. Use `TEXT` for inlining the command. Use `OBJECT_STORAGE_TUPLE` when specifying
                                  the namespace, bucket name, and object name. Use `OBJECT_STORAGE_URI` when specifying the Object Storage URL.
                            returned: on success
                            type: string
                            sample: TEXT
                        bucket_name:
                            description:
                                - The Object Storage bucket for the command.
                            returned: on success
                            type: string
                            sample: bucket_name_example
                        namespace_name:
                            description:
                                - The Object Storage namespace for the command.
                            returned: on success
                            type: string
                            sample: namespace_name_example
                        object_name:
                            description:
                                - The Object Storage name for the command.
                            returned: on success
                            type: string
                            sample: object_name_example
                        source_uri:
                            description:
                                - The Object Storage URL or PAR for the command.
                            returned: on success
                            type: string
                            sample: source_uri_example
                        text:
                            description:
                                - The plain text command.
                            returned: on success
                            type: string
                            sample: text_example
                        text_sha256:
                            description:
                                - Sha256 checksum value of the text content
                            returned: on success
                            type: string
                            sample: text_sha256_example
                output:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        output_type:
                            description:
                                - The output type of the command. Use `OBJECT_STORAGE_URI` when specifying the Object Storage URL.
                                  Use `OBJECT_STORAGE_TUPLE` when specifying the namespace, bucket name, and object name.
                            returned: on success
                            type: string
                            sample: TEXT
                        output_uri:
                            description:
                                - The Object Storage URL or PAR for the command output.
                            returned: on success
                            type: string
                            sample: output_uri_example
                        bucket_name:
                            description:
                                - The Object Storage bucket for the command output.
                            returned: on success
                            type: string
                            sample: bucket_name_example
                        namespace_name:
                            description:
                                - The Object Storage namespace for the command output.
                            returned: on success
                            type: string
                            sample: namespace_name_example
                        object_name:
                            description:
                                - The Object Storage name for the command output.
                            returned: on success
                            type: string
                            sample: object_name_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "is_canceled": true,
        "execution_time_out_in_seconds": 56,
        "target": {
            "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "content": {
            "source": {
                "source_type": "TEXT",
                "bucket_name": "bucket_name_example",
                "namespace_name": "namespace_name_example",
                "object_name": "object_name_example",
                "source_uri": "source_uri_example",
                "text": "text_example",
                "text_sha256": "text_sha256_example"
            },
            "output": {
                "output_type": "TEXT",
                "output_uri": "output_uri_example",
                "bucket_name": "bucket_name_example",
                "namespace_name": "namespace_name_example",
                "object_name": "object_name_example"
            }
        }
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
    from oci.compute_instance_agent import ComputeInstanceAgentClient
    from oci.compute_instance_agent.models import CreateInstanceAgentCommandDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceAgentCommandHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_module_resource_id_param(self):
        return "instance_agent_command_id"

    def get_module_resource_id(self):
        return self.module.params.get("instance_agent_command_id")

    def get_get_fn(self):
        return self.client.get_instance_agent_command

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_agent_command,
            instance_agent_command_id=self.module.params.get(
                "instance_agent_command_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_instance_agent_commands, **kwargs
        )

    def get_create_model_class(self):
        return CreateInstanceAgentCommandDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_instance_agent_command,
            call_fn_args=(),
            call_fn_kwargs=dict(create_instance_agent_command_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_instance_agent_command,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_agent_command_id=self.module.params.get(
                    "instance_agent_command_id"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


InstanceAgentCommandHelperCustom = get_custom_class("InstanceAgentCommandHelperCustom")


class ResourceHelper(InstanceAgentCommandHelperCustom, InstanceAgentCommandHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            execution_time_out_in_seconds=dict(type="int"),
            display_name=dict(aliases=["name"], type="str"),
            target=dict(type="dict", options=dict(instance_id=dict(type="str"))),
            content=dict(
                type="dict",
                options=dict(
                    source=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            source_type=dict(
                                type="str",
                                default="TEXT",
                                choices=[
                                    "OBJECT_STORAGE_TUPLE",
                                    "OBJECT_STORAGE_URI",
                                    "TEXT",
                                ],
                            ),
                            bucket_name=dict(type="str"),
                            namespace_name=dict(type="str"),
                            object_name=dict(type="str"),
                            source_uri=dict(type="str"),
                            text=dict(type="str"),
                            text_sha256=dict(type="str"),
                        ),
                    ),
                    output=dict(
                        type="dict",
                        options=dict(
                            output_type=dict(
                                type="str",
                                default="TEXT",
                                choices=[
                                    "OBJECT_STORAGE_URI",
                                    "OBJECT_STORAGE_TUPLE",
                                    "TEXT",
                                ],
                            ),
                            output_uri=dict(type="str"),
                            bucket_name=dict(type="str"),
                            namespace_name=dict(type="str"),
                            object_name=dict(type="str"),
                        ),
                    ),
                ),
            ),
            instance_agent_command_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="instance_agent_command",
        service_client_class=ComputeInstanceAgentClient,
        namespace="compute_instance_agent",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
