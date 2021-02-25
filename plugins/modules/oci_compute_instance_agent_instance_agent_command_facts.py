#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_compute_instance_agent_instance_agent_command_facts
short_description: Fetches details about one or multiple InstanceAgentCommand resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple InstanceAgentCommand resources in Oracle Cloud Infrastructure
    - Lists the Oracle Cloud Agent commands issued in a compartment.
    - If I(instance_agent_command_id) is specified, the details of a single InstanceAgentCommand will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    instance_agent_command_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the command.
            - Required to get a specific instance_agent_command.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple instance_agent_commands.
        type: str
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
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List instance_agent_commands
  oci_compute_instance_agent_instance_agent_command_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific instance_agent_command
  oci_compute_instance_agent_instance_agent_command_facts:
    instance_agent_command_id: ocid1.instanceagentcommand.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
instance_agent_commands:
    description:
        - List of InstanceAgentCommand resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the command.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the command.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - A user-friendly name. Does not have to be unique. Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        time_created:
            description:
                - The date and time the command was created, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The date and time the command was last updated, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
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
                    type: string
                    sample: ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx
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
                        source_type:
                            description:
                                - "The source type for the command. The following values are supported:"
                                - "- `TEXT` - uses a plain text command that is specified inline with the request.
                                  - `OBJECT_STORAGE_URI` - imports a command from an Object Storage URL.
                                  - `OBJECT_STORAGE_TUPLE` - imports a command from an Object Storage bucket."
                                - For background information about Object Storage buckets and URLs, see
                                  L(Overview of Object Storage,https://docs.cloud.oracle.com/Content/Object/Concepts/objectstorageoverview.htm).
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
                                - The Object Storage object name for the command.
                            returned: on success
                            type: string
                            sample: object_name_example
                        source_uri:
                            description:
                                - The Object Storage URL or pre-authenticated request (PAR) for the command.
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
                                - SHA-256 checksum value of the text content.
                            returned: on success
                            type: string
                            sample: text_sha256_example
                output:
                    description:
                        - The output destination for the command.
                    returned: on success
                    type: complex
                    contains:
                        output_type:
                            description:
                                - "The output type for the command. The following values are supported:"
                                - "- `TEXT` - the command output is returned as plain text.
                                  - `OBJECT_STORAGE_URI` - the command output is saved to an Object Storage URL.
                                  - `OBJECT_STORAGE_TUPLE` - the command output is saved to an Object Storage bucket."
                                - For background information about Object Storage buckets and URLs, see
                                  L(Overview of Object Storage,https://docs.cloud.oracle.com/Content/Object/Concepts/objectstorageoverview.htm).
                            returned: on success
                            type: string
                            sample: TEXT
                        output_uri:
                            description:
                                - The Object Storage URL or pre-authenticated request (PAR) for the command output.
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
                                - The Object Storage object name for the command output.
                            returned: on success
                            type: string
                            sample: object_name_example
        instance_agent_command_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the command.
            returned: on success
            type: string
            sample: ocid1.instanceagentcommand.oc1..xxxxxxEXAMPLExxxxxx
    sample: [{
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
        },
        "instance_agent_command_id": "ocid1.instanceagentcommand.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.compute_instance_agent import ComputeInstanceAgentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceAgentCommandFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "instance_agent_command_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_agent_command,
            instance_agent_command_id=self.module.params.get(
                "instance_agent_command_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_instance_agent_commands,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


InstanceAgentCommandFactsHelperCustom = get_custom_class(
    "InstanceAgentCommandFactsHelperCustom"
)


class ResourceFactsHelper(
    InstanceAgentCommandFactsHelperCustom, InstanceAgentCommandFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            instance_agent_command_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="instance_agent_command",
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

    module.exit_json(instance_agent_commands=result)


if __name__ == "__main__":
    main()
