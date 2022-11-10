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
module: oci_loggingingestion_log_entry_actions
short_description: Perform actions on a LogEntry resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a LogEntry resource in Oracle Cloud Infrastructure
    - For I(action=put_logs), this API allows ingesting logs associated with a logId. A success
      response implies the data has been accepted.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    log_id:
        description:
            - OCID of a log to work with.
        type: str
        aliases: ["id"]
        required: true
    specversion:
        description:
            - "Required for identifying the version of the data format being used.
              Permitted values include: \\"1.0\\""
        type: str
        required: true
    log_entry_batches:
        description:
            - List of log-batches. Each batch has a single source, type and subject.
        type: list
        elements: dict
        required: true
        suboptions:
            entries:
                description:
                    - List of data entries.
                type: list
                elements: dict
                required: true
                suboptions:
                    data:
                        description:
                            - The log entry content.
                        type: str
                        required: true
                    id:
                        description:
                            - UUID uniquely representing this logEntry. This is not an OCID related
                              to any oracle resource.
                        type: str
                        required: true
                    time:
                        description:
                            - Optional. The timestamp associated with the log entry. An RFC3339-formatted date-time string with milliseconds precision.
                              If unspecified, defaults to PutLogsDetails.defaultlogentrytime.
                        type: str
            source:
                description:
                    - "Source of the logs that generated the message. This could be the
                      instance name, hostname, or the source used to read the event. For example, \\"ServerA\\"."
                type: str
                required: true
            type:
                description:
                    - "This field signifies the type of logs being ingested.
                      For example: ServerA.requestLogs."
                type: str
                required: true
            subject:
                description:
                    - "This optional field is useful for specifying the specific sub-resource
                      or input file used to read the event.
                      For example: \\"/var/log/application.log\\"."
                type: str
            defaultlogentrytime:
                description:
                    - The timestamp for all log entries in this batch. This can be
                      considered as the default timestamp for each entry, unless it is
                      overwritten by the entry time. An RFC3339-formatted date-time string
                      with milliseconds precision.
                type: str
                required: true
    timestamp_opc_agent_processing:
        description:
            - Effective timestamp, for when the agent started processing the log
              segment being sent. An RFC3339-formatted date-time string with milliseconds precision.
        type: str
    opc_agent_version:
        description:
            - Version of the agent sending the request.
        type: str
    action:
        description:
            - The action to perform on the LogEntry.
        type: str
        required: true
        choices:
            - "put_logs"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action put_logs on log_entry
  oci_loggingingestion_log_entry_actions:
    # required
    log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    specversion: specversion_example
    log_entry_batches:
    - # required
      entries:
      - # required
        data: data_example
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        time: time_example
      source: source_example
      type: type_example
      defaultlogentrytime: defaultlogentrytime_example

      # optional
      subject: subject_example
    action: put_logs

    # optional
    timestamp_opc_agent_processing: 2013-10-20T19:20:30+01:00
    opc_agent_version: opc_agent_version_example

"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.loggingingestion import LoggingClient
    from oci.loggingingestion.models import PutLogsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogEntryActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        put_logs
    """

    @staticmethod
    def get_module_resource_id_param():
        return "log_id"

    def get_module_resource_id(self):
        return self.module.params.get("log_id")

    def put_logs(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, PutLogsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.put_logs,
            call_fn_args=(),
            call_fn_kwargs=dict(
                log_id=self.module.params.get("log_id"),
                put_logs_details=action_details,
                timestamp_opc_agent_processing=self.module.params.get(
                    "timestamp_opc_agent_processing"
                ),
                opc_agent_version=self.module.params.get("opc_agent_version"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


LogEntryActionsHelperCustom = get_custom_class("LogEntryActionsHelperCustom")


class ResourceHelper(LogEntryActionsHelperCustom, LogEntryActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            log_id=dict(aliases=["id"], type="str", required=True),
            specversion=dict(type="str", required=True),
            log_entry_batches=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    entries=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            data=dict(type="str", required=True),
                            id=dict(type="str", required=True),
                            time=dict(type="str"),
                        ),
                    ),
                    source=dict(type="str", required=True),
                    type=dict(type="str", required=True),
                    subject=dict(type="str"),
                    defaultlogentrytime=dict(type="str", required=True),
                ),
            ),
            timestamp_opc_agent_processing=dict(type="str"),
            opc_agent_version=dict(type="str"),
            action=dict(type="str", required=True, choices=["put_logs"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="log_entry",
        service_client_class=LoggingClient,
        namespace="loggingingestion",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
