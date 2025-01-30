#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_compute_instance_agent_instance_agent_command_execution_facts
short_description: Fetches details about one or multiple InstanceAgentCommandExecution resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple InstanceAgentCommandExecution resources in Oracle Cloud Infrastructure
    - Lists the execution details for Oracle Cloud Agent commands that run on the specified compute
      instance.
    - If I(instance_agent_command_id) is specified, the details of a single InstanceAgentCommandExecution will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    instance_agent_command_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the command.
            - Required to get a specific instance_agent_command_execution.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple instance_agent_command_executions.
        type: str
    instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the instance.
        type: str
        required: true
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              `TIMECREATED` is descending.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The `DISPLAYNAME` sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.
        type: str
        choices:
            - "ACCEPTED"
            - "IN_PROGRESS"
            - "SUCCEEDED"
            - "FAILED"
            - "TIMED_OUT"
            - "CANCELED"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific instance_agent_command_execution
  oci_compute_instance_agent_instance_agent_command_execution_facts:
    # required
    instance_agent_command_id: "ocid1.instanceagentcommand.oc1..xxxxxxEXAMPLExxxxxx"
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List instance_agent_command_executions
  oci_compute_instance_agent_instance_agent_command_execution_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: ACCEPTED

"""

RETURN = """
instance_agent_command_executions:
    description:
        - List of InstanceAgentCommandExecution resources
    returned: on success
    type: complex
    contains:
        instance_agent_command_id:
            description:
                - The OCID of the command
            returned: on success
            type: str
            sample: "ocid1.instanceagentcommand.oc1..xxxxxxEXAMPLExxxxxx"
        instance_id:
            description:
                - The OCID of the instance
            returned: on success
            type: str
            sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
        delivery_state:
            description:
                - "Specifies the command delivery state.
                   * `VISIBLE` - The command is visible to instance.
                   * `PENDING` - The command is pending ack from the instance.
                   * `ACKED` - The command has been received and acked by the instance.
                   * `ACKED_CANCELED` - The canceled command has been received and acked by the instance.
                   * `EXPIRED` - The instance has not requested for commands and its delivery has expired."
            returned: on success
            type: str
            sample: VISIBLE
        lifecycle_state:
            description:
                - "command execution life cycle state.
                  * `ACCEPTED` - The command execution has been accepted to run.
                  * `IN_PROGRESS` - The command execution is in progress.
                  * `SUCCEEDED` - The command execution is successful.
                  * `FAILED` - The command execution has failed.
                  * `TIMED_OUT` - The command execution has timedout.
                  * `CANCELED` - The command execution has canceled."
            returned: on success
            type: str
            sample: ACCEPTED
        time_created:
            description:
                - The command creation date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The command last updated at date.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        sequence_number:
            description:
                - The large non-consecutive number that Run Command Service assigns to each created command.
            returned: on success
            type: int
            sample: 56
        display_name:
            description:
                - The user friendly display name of the command.
            returned: on success
            type: str
            sample: display_name_example
        content:
            description:
                - ""
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
                        - "The output destination type for the command. The following values are supported:"
                        - "- TEXT - the command output is returned as plain text.
                          - OBJECT_STORAGE_URI - the command output is saved to an Object Storage URL.
                          - OBJECT_STORAGE_TUPLE - the command output is saved to an Object Storage bucket."
                        - For background information about Object Storage buckets and URLs, see
                          L(Overview of Object Storage,https://docs.cloud.oracle.com/Content/Object/Concepts/objectstorageoverview.htm).
                    returned: on success
                    type: str
                    sample: TEXT
                exit_code:
                    description:
                        - The exit code for the command. Exit code `0` indicates success.
                    returned: on success
                    type: int
                    sample: 56
                message:
                    description:
                        - An optional status message that Oracle Cloud Agent can populate for additional troubleshooting.
                    returned: on success
                    type: str
                    sample: message_example
                text:
                    description:
                        - The command output.
                    returned: on success
                    type: str
                    sample: text_example
                text_sha256:
                    description:
                        - SHA-256 checksum value of the text content.
                    returned: on success
                    type: str
                    sample: text_sha256_example
    sample: [{
        "instance_agent_command_id": "ocid1.instanceagentcommand.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
        "delivery_state": "VISIBLE",
        "lifecycle_state": "ACCEPTED",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "sequence_number": 56,
        "display_name": "display_name_example",
        "content": {
            "bucket_name": "bucket_name_example",
            "namespace_name": "namespace_name_example",
            "object_name": "object_name_example",
            "output_uri": "output_uri_example",
            "output_type": "TEXT",
            "exit_code": 56,
            "message": "message_example",
            "text": "text_example",
            "text_sha256": "text_sha256_example"
        }
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.compute_instance_agent import ComputeInstanceAgentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceAgentCommandExecutionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "instance_agent_command_id",
            "instance_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "instance_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_agent_command_execution,
            instance_agent_command_id=self.module.params.get(
                "instance_agent_command_id"
            ),
            instance_id=self.module.params.get("instance_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_instance_agent_command_executions,
            compartment_id=self.module.params.get("compartment_id"),
            instance_id=self.module.params.get("instance_id"),
            **optional_kwargs
        )


InstanceAgentCommandExecutionFactsHelperCustom = get_custom_class(
    "InstanceAgentCommandExecutionFactsHelperCustom"
)


class ResourceFactsHelper(
    InstanceAgentCommandExecutionFactsHelperCustom,
    InstanceAgentCommandExecutionFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            instance_agent_command_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            instance_id=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACCEPTED",
                    "IN_PROGRESS",
                    "SUCCEEDED",
                    "FAILED",
                    "TIMED_OUT",
                    "CANCELED",
                ],
            ),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="instance_agent_command_execution",
        service_client_class=ComputeInstanceAgentClient,
        namespace="compute_instance_agent",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(instance_agent_command_executions=result)


if __name__ == "__main__":
    main()
