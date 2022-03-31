#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
    - For I(state=present), creates a command or script to run on a compute instance that is managed by Oracle Cloud Agent.
    - On Linux instances, the script runs in a bash shell. On Windows instances, the
      script runs in a batch shell.
    - Commands that require administrator privileges will run only if Oracle Cloud Agent
      is running with administrator privileges.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to create the command in.
            - Required for create using I(state=present).
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    execution_time_out_in_seconds:
        description:
            - The amount of time that Oracle Cloud Agent is given to run the command on the instance before timing
              out. The timer starts when Oracle Cloud Agent starts the command. Zero means no timeout.
            - Required for create using I(state=present).
        type: int
    display_name:
        description:
            - A user-friendly name for the command. It does not have to be unique.
              Avoid entering confidential information.
            - "Example: `Database Backup Script`"
            - Required for create, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    target:
        description:
            - The target instance to run the command on.
            - Required for create using I(state=present).
        type: dict
        suboptions:
            instance_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the target instance.
                type: str
    content:
        description:
            - The contents of the command.
            - Required for create using I(state=present).
        type: dict
        suboptions:
            source:
                description:
                    - The source of the command.
                type: dict
                required: true
                suboptions:
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
                            - The Object Storage object name for the command.
                            - Required when source_type is 'OBJECT_STORAGE_TUPLE'
                        type: str
                    source_uri:
                        description:
                            - The Object Storage URL or pre-authenticated request (PAR) for the command.
                            - Required when source_type is 'OBJECT_STORAGE_URI'
                        type: str
                    source_type:
                        description:
                            - "The source type for the command. The following values are supported:"
                            - "- `TEXT` - uses a plain text command that is specified inline with the request.
                              - `OBJECT_STORAGE_URI` - imports a command from an Object Storage URL.
                              - `OBJECT_STORAGE_TUPLE` - imports a command from an Object Storage bucket."
                            - For background information about Object Storage buckets and URLs, see
                              L(Overview of Object Storage,https://docs.cloud.oracle.com/Content/Object/Concepts/objectstorageoverview.htm).
                        type: str
                        choices:
                            - "OBJECT_STORAGE_TUPLE"
                            - "OBJECT_STORAGE_URI"
                            - "TEXT"
                        default: "TEXT"
                    text:
                        description:
                            - The plain text command.
                            - Required when source_type is 'TEXT'
                        type: str
                    text_sha256:
                        description:
                            - SHA-256 checksum value of the text content.
                            - Applicable when source_type is 'TEXT'
                        type: str
            output:
                description:
                    - The output destination for the command.
                type: dict
                suboptions:
                    output_uri:
                        description:
                            - The Object Storage URL or pre-authenticated request (PAR) for the command output.
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
                            - The Object Storage object name for the command output.
                            - Required when output_type is 'OBJECT_STORAGE_TUPLE'
                        type: str
                    output_type:
                        description:
                            - "The output type for the command. The following values are supported:"
                            - "- `TEXT` - the command output is returned as plain text.
                              - `OBJECT_STORAGE_URI` - the command output is saved to an Object Storage URL.
                              - `OBJECT_STORAGE_TUPLE` - the command output is saved to an Object Storage bucket."
                            - For background information about Object Storage buckets and URLs, see
                              L(Overview of Object Storage,https://docs.cloud.oracle.com/Content/Object/Concepts/objectstorageoverview.htm).
                        type: str
                        choices:
                            - "OBJECT_STORAGE_URI"
                            - "OBJECT_STORAGE_TUPLE"
                            - "TEXT"
                        default: "TEXT"
    instance_agent_command_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the command.
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
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    execution_time_out_in_seconds: 56
    target:
      # optional
      instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
    content:
      # required
      source:
        # required
        bucket_name: bucket_name_example
        namespace_name: namespace_name_example
        object_name: object_name_example
        source_type: OBJECT_STORAGE_TUPLE

        # optional
      output:
        # required
        output_uri: output_uri_example
        output_type: OBJECT_STORAGE_URI

    # optional
    display_name: display_name_example

- name: Delete instance_agent_command
  oci_compute_instance_agent_instance_agent_command:
    # required
    instance_agent_command_id: "ocid1.instanceagentcommand.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete instance_agent_command using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_instance_agent_instance_agent_command:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
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
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the command.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the command.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The date and time the command was created, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the command was last updated, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_canceled:
            description:
                - Whether a request was made to cancel the command. Canceling a command is a best-effort attempt.
            returned: on success
            type: bool
            sample: true
        execution_time_out_in_seconds:
            description:
                - The amount of time that Oracle Cloud Agent is given to run the command on the instance before timing
                  out. The timer starts when Oracle Cloud Agent starts the command. Zero means no timeout.
            returned: on success
            type: int
            sample: 56
        target:
            description:
                - The target instance that the command runs on.
            returned: on success
            type: complex
            contains:
                instance_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the target instance.
                    returned: on success
                    type: str
                    sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
        content:
            description:
                - The contents of the command.
            returned: on success
            type: complex
            contains:
                source:
                    description:
                        - The source of the command.
                    returned: on success
                    type: complex
                    contains:
                        bucket_name:
                            description:
                                - The Object Storage bucket for the command.
                            returned: on success
                            type: str
                            sample: bucket_name_example
                        namespace_name:
                            description:
                                - The Object Storage namespace for the command.
                            returned: on success
                            type: str
                            sample: namespace_name_example
                        object_name:
                            description:
                                - The Object Storage object name for the command.
                            returned: on success
                            type: str
                            sample: object_name_example
                        source_uri:
                            description:
                                - The Object Storage URL or pre-authenticated request (PAR) for the command.
                            returned: on success
                            type: str
                            sample: source_uri_example
                        source_type:
                            description:
                                - "The source type for the command. The following values are supported:"
                                - "- `TEXT` - uses a plain text command that is specified inline with the request.
                                  - `OBJECT_STORAGE_URI` - imports a command from an Object Storage URL.
                                  - `OBJECT_STORAGE_TUPLE` - imports a command from an Object Storage bucket."
                                - For background information about Object Storage buckets and URLs, see
                                  L(Overview of Object Storage,https://docs.cloud.oracle.com/Content/Object/Concepts/objectstorageoverview.htm).
                            returned: on success
                            type: str
                            sample: TEXT
                        text:
                            description:
                                - The plain text command.
                            returned: on success
                            type: str
                            sample: text_example
                        text_sha256:
                            description:
                                - SHA-256 checksum value of the text content.
                            returned: on success
                            type: str
                            sample: text_sha256_example
                output:
                    description:
                        - The output destination for the command.
                    returned: on success
                    type: complex
                    contains:
                        bucket_name:
                            description:
                                - The Object Storage bucket for the command output.
                            returned: on success
                            type: str
                            sample: bucket_name_example
                        namespace_name:
                            description:
                                - The Object Storage namespace for the command output.
                            returned: on success
                            type: str
                            sample: namespace_name_example
                        object_name:
                            description:
                                - The Object Storage object name for the command output.
                            returned: on success
                            type: str
                            sample: object_name_example
                        output_uri:
                            description:
                                - The Object Storage URL or pre-authenticated request (PAR) for the command output.
                            returned: on success
                            type: str
                            sample: output_uri_example
                        output_type:
                            description:
                                - "The output type for the command. The following values are supported:"
                                - "- `TEXT` - the command output is returned as plain text.
                                  - `OBJECT_STORAGE_URI` - the command output is saved to an Object Storage URL.
                                  - `OBJECT_STORAGE_TUPLE` - the command output is saved to an Object Storage bucket."
                                - For background information about Object Storage buckets and URLs, see
                                  L(Overview of Object Storage,https://docs.cloud.oracle.com/Content/Object/Concepts/objectstorageoverview.htm).
                            returned: on success
                            type: str
                            sample: TEXT
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
                "bucket_name": "bucket_name_example",
                "namespace_name": "namespace_name_example",
                "object_name": "object_name_example",
                "source_uri": "source_uri_example",
                "source_type": "TEXT",
                "text": "text_example",
                "text_sha256": "text_sha256_example"
            },
            "output": {
                "bucket_name": "bucket_name_example",
                "namespace_name": "namespace_name_example",
                "object_name": "object_name_example",
                "output_uri": "output_uri_example",
                "output_type": "TEXT"
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

    def get_possible_entity_types(self):
        return super(
            InstanceAgentCommandHelperGen, self
        ).get_possible_entity_types() + [
            "instanceagentcommand",
            "instanceagentcommands",
            "computeInstanceAgentinstanceagentcommand",
            "computeInstanceAgentinstanceagentcommands",
            "instanceagentcommandresource",
            "instanceagentcommandsresource",
            "computeinstanceagent",
        ]

    def get_module_resource_id_param(self):
        return "instance_agent_command_id"

    def get_module_resource_id(self):
        return self.module.params.get("instance_agent_command_id")

    def get_get_fn(self):
        return self.client.get_instance_agent_command

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_agent_command,
            instance_agent_command_id=summary_model.instance_agent_command_id,
        ).data

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
                            bucket_name=dict(type="str"),
                            namespace_name=dict(type="str"),
                            object_name=dict(type="str"),
                            source_uri=dict(type="str"),
                            source_type=dict(
                                type="str",
                                default="TEXT",
                                choices=[
                                    "OBJECT_STORAGE_TUPLE",
                                    "OBJECT_STORAGE_URI",
                                    "TEXT",
                                ],
                            ),
                            text=dict(type="str"),
                            text_sha256=dict(type="str"),
                        ),
                    ),
                    output=dict(
                        type="dict",
                        options=dict(
                            output_uri=dict(type="str"),
                            bucket_name=dict(type="str"),
                            namespace_name=dict(type="str"),
                            object_name=dict(type="str"),
                            output_type=dict(
                                type="str",
                                default="TEXT",
                                choices=[
                                    "OBJECT_STORAGE_URI",
                                    "OBJECT_STORAGE_TUPLE",
                                    "TEXT",
                                ],
                            ),
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
