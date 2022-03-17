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
module: oci_sch_service_connector_actions
short_description: Perform actions on a ServiceConnector resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ServiceConnector resource in Oracle Cloud Infrastructure
    - For I(action=activate), activates the specified service connector.
      After you send your request, the service connector's state is temporarily
      UPDATING. When the state changes to ACTIVE, data begins transferring from the
      source service to the target service. For instructions on activating service
      connectors, see
      L(To activate a service connector,https://docs.cloud.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#activate).
    - For I(action=change_compartment), moves a service connector into a different compartment within the same tenancy.
      For information about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
      When provided, If-Match is checked against ETag values of the resource.
    - For I(action=deactivate), deactivates the specified service connector.
      After you send your request, the service connector's state is temporarily
      UPDATING and any data transfer stops. The state then changes to INACTIVE.
      For instructions on deactivating service connectors, see
      L(To deactivate a service connector,https://docs.cloud.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#deactivate).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    service_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the service connector.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment
              to move the service connector to.
            - Required for I(action=change_compartment).
        type: str
    action:
        description:
            - The action to perform on the ServiceConnector.
        type: str
        required: true
        choices:
            - "activate"
            - "change_compartment"
            - "deactivate"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action activate on service_connector
  oci_sch_service_connector_actions:
    # required
    service_connector_id: "ocid1.serviceconnector.oc1..xxxxxxEXAMPLExxxxxx"
    action: activate

- name: Perform action change_compartment on service_connector
  oci_sch_service_connector_actions:
    # required
    service_connector_id: "ocid1.serviceconnector.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action deactivate on service_connector
  oci_sch_service_connector_actions:
    # required
    service_connector_id: "ocid1.serviceconnector.oc1..xxxxxxEXAMPLExxxxxx"
    action: deactivate

"""

RETURN = """
service_connector:
    description:
        - Details of the ServiceConnector resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the service connector.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The description of the resource. Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the service connector.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The date and time when the service connector was created.
                  Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The date and time when the service connector was updated.
                  Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the service connector.
            returned: on success
            type: str
            sample: CREATING
        lifecyle_details:
            description:
                - A message describing the current state in more detail.
                  For example, the message might provide actionable
                  information for a resource in a `FAILED` state.
            returned: on success
            type: str
            sample: lifecyle_details_example
        source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                log_sources:
                    description:
                        - The logs for this Logging source.
                    returned: on success
                    type: complex
                    contains:
                        compartment_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the log
                                  source.
                            returned: on success
                            type: str
                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                        log_group_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the log group.
                            returned: on success
                            type: str
                            sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                        log_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the log.
                            returned: on success
                            type: str
                            sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
                kind:
                    description:
                        - The type descriminator.
                    returned: on success
                    type: str
                    sample: logging
                stream_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stream.
                    returned: on success
                    type: str
                    sample: "ocid1.stream.oc1..xxxxxxEXAMPLExxxxxx"
                cursor:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        kind:
                            description:
                                - The type descriminator.
                            returned: on success
                            type: str
                            sample: LATEST
        tasks:
            description:
                - The list of tasks.
            returned: on success
            type: complex
            contains:
                function_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the function to be used as a task.
                    returned: on success
                    type: str
                    sample: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
                batch_size_in_kbs:
                    description:
                        - Size limit (kilobytes) for batch sent to invoke the function.
                    returned: on success
                    type: int
                    sample: 56
                batch_time_in_sec:
                    description:
                        - Time limit (seconds) for batch sent to invoke the function.
                    returned: on success
                    type: int
                    sample: 56
                kind:
                    description:
                        - The type descriminator.
                    returned: on success
                    type: str
                    sample: function
                condition:
                    description:
                        - A filter or mask to limit the source used in the flow defined by the service connector.
                    returned: on success
                    type: str
                    sample: condition_example
        target:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                function_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the function.
                    returned: on success
                    type: str
                    sample: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
                log_group_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Logging Analytics log group.
                    returned: on success
                    type: str
                    sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the metric.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                metric_namespace:
                    description:
                        - The namespace of the metric.
                        - "Example: `oci_computeagent`"
                    returned: on success
                    type: str
                    sample: metric_namespace_example
                metric:
                    description:
                        - The name of the metric.
                        - "Example: `CpuUtilization`"
                    returned: on success
                    type: str
                    sample: metric_example
                dimensions:
                    description:
                        - List of dimension names and values.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - "Dimension key. A valid dimension key includes only printable ASCII, excluding periods (.) and spaces.
                                  Custom dimension keys are acceptable. Avoid entering confidential information.
                                  Due to use by Service Connector Hub, the following dimension names are reserved: `connectorId`, `connectorName`,
                                  `connectorSourceType`.
                                  For information on valid dimension keys and values, see L(MetricDataDetails Reference,https://docs.cloud.oracle.com/en-
                                  us/iaas/api/#/en/monitoring/latest/datatypes/MetricDataDetails).
                                  Example: `type`"
                            returned: on success
                            type: str
                            sample: name_example
                        dimension_value:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                path:
                                    description:
                                        - "The location to use for deriving the dimension value (evaluated).
                                          The path must start with `logContent` in an acceptable notation style with supported L(JMESPath
                                          selectors,https://jmespath.org/specification.html): expression with dot and index operator (`.`, and `L(]`).
                                          Example with dot notation: `logContent.data`
                                          Example with index notation: `logContent.data[0].content`
                                          For information on valid dimension keys and values, see [MetricDataDetails Reference,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/monitoring/latest/datatypes/MetricDataDetails).
                                          The returned value depends on the results of evaluation.
                                          If the evaluated value is valid, then the evaluated value is returned without double quotes. (Any front or trailing
                                          double quotes are trimmed before returning the value. For example, the evaluated value `\\"compartmentId\\"` is
                                          returned as `compartmentId`.)
                                          If the evaluated value is invalid, then the returned value is `SCH_EVAL_INVALID_VALUE`.
                                          If the evaluated value is empty, then the returned value is `SCH_EVAL_VALUE_EMPTY`."
                                    returned: on success
                                    type: str
                                    sample: path_example
                                kind:
                                    description:
                                        - "The type of dimension value: static or evaluated."
                                    returned: on success
                                    type: str
                                    sample: jmesPath
                                value:
                                    description:
                                        - The data extracted from the specified dimension value (passed as-is). Unicode characters only.
                                          For information on valid dimension keys and values, see L(MetricDataDetails
                                          Reference,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/monitoring/latest/datatypes/MetricDataDetails).
                                    returned: on success
                                    type: str
                                    sample: value_example
                topic_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the topic.
                    returned: on success
                    type: str
                    sample: "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx"
                enable_formatted_messaging:
                    description:
                        - Whether to apply a simplified, user-friendly format to the message. Applies only when friendly formatting is supported by the service
                          connector source and the subscription protocol.
                        - "Example: `true`"
                    returned: on success
                    type: bool
                    sample: true
                namespace:
                    description:
                        - The namespace.
                    returned: on success
                    type: str
                    sample: namespace_example
                bucket_name:
                    description:
                        - The name of the bucket. Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: bucket_name_example
                object_name_prefix:
                    description:
                        - The prefix of the objects. Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: object_name_prefix_example
                batch_rollover_size_in_mbs:
                    description:
                        - The batch rollover size in megabytes.
                    returned: on success
                    type: int
                    sample: 56
                batch_rollover_time_in_ms:
                    description:
                        - The batch rollover time in milliseconds.
                    returned: on success
                    type: int
                    sample: 56
                kind:
                    description:
                        - The type descriminator.
                    returned: on success
                    type: str
                    sample: functions
                stream_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stream.
                    returned: on success
                    type: str
                    sample: "ocid1.stream.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is
                  predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecyle_details": "lifecyle_details_example",
        "source": {
            "log_sources": [{
                "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
                "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
            }],
            "kind": "logging",
            "stream_id": "ocid1.stream.oc1..xxxxxxEXAMPLExxxxxx",
            "cursor": {
                "kind": "LATEST"
            }
        },
        "tasks": [{
            "function_id": "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx",
            "batch_size_in_kbs": 56,
            "batch_time_in_sec": 56,
            "kind": "function",
            "condition": "condition_example"
        }],
        "target": {
            "function_id": "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx",
            "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "metric_namespace": "metric_namespace_example",
            "metric": "metric_example",
            "dimensions": [{
                "name": "name_example",
                "dimension_value": {
                    "path": "path_example",
                    "kind": "jmesPath",
                    "value": "value_example"
                }
            }],
            "topic_id": "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx",
            "enable_formatted_messaging": true,
            "namespace": "namespace_example",
            "bucket_name": "bucket_name_example",
            "object_name_prefix": "object_name_prefix_example",
            "batch_rollover_size_in_mbs": 56,
            "batch_rollover_time_in_ms": 56,
            "kind": "functions",
            "stream_id": "ocid1.stream.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.sch import ServiceConnectorClient
    from oci.sch.models import ChangeServiceConnectorCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ServiceConnectorActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        activate
        change_compartment
        deactivate
    """

    @staticmethod
    def get_module_resource_id_param():
        return "service_connector_id"

    def get_module_resource_id(self):
        return self.module.params.get("service_connector_id")

    def get_get_fn(self):
        return self.client.get_service_connector

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_service_connector,
            service_connector_id=self.module.params.get("service_connector_id"),
        )

    def activate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.activate_service_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                service_connector_id=self.module.params.get("service_connector_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeServiceConnectorCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_service_connector_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                service_connector_id=self.module.params.get("service_connector_id"),
                change_service_connector_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def deactivate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.deactivate_service_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                service_connector_id=self.module.params.get("service_connector_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ServiceConnectorActionsHelperCustom = get_custom_class(
    "ServiceConnectorActionsHelperCustom"
)


class ResourceHelper(
    ServiceConnectorActionsHelperCustom, ServiceConnectorActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            service_connector_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=["activate", "change_compartment", "deactivate"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="service_connector",
        service_client_class=ServiceConnectorClient,
        namespace="sch",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
