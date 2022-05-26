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
module: oci_sch_service_connector_facts
short_description: Fetches details about one or multiple ServiceConnector resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ServiceConnector resources in Oracle Cloud Infrastructure
    - Lists service connectors in the specified compartment.
    - If I(service_connector_id) is specified, the details of a single ServiceConnector will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    service_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the service connector.
            - Required to get a specific service_connector.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment for this request.
            - Required to list multiple service_connectors.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state.
            - "Example: `ACTIVE`"
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
            - "Example: `example_service_connector`"
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for `timeCreated` is descending.
              Default order for `displayName` is ascending. If no value is specified `timeCreated` is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific service_connector
  oci_sch_service_connector_facts:
    # required
    service_connector_id: "ocid1.serviceconnector.oc1..xxxxxxEXAMPLExxxxxx"

- name: List service_connectors
  oci_sch_service_connector_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
service_connectors:
    description:
        - List of ServiceConnector resources
    returned: on success
    type: complex
    contains:
        lifecyle_details:
            description:
                - A message describing the current state in more detail.
                  For example, the message might provide actionable
                  information for a resource in a `FAILED` state.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecyle_details_example
        source:
            description:
                - ""
                - Returned for get operation
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
                monitoring_sources:
                    description:
                        - The list of metric namespaces to retrieve data from.
                    returned: on success
                    type: complex
                    contains:
                        compartment_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the
                                  metric namespaces you want to use for the Monitoring source.
                            returned: on success
                            type: str
                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                        namespace_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                kind:
                                    description:
                                        - The type discriminator.
                                    returned: on success
                                    type: str
                                    sample: selected
                                namespaces:
                                    description:
                                        - The namespaces for the compartment-specific list.
                                    returned: on success
                                    type: complex
                                    contains:
                                        namespace:
                                            description:
                                                - The source service or application to use when querying for metric data points. Must begin with `oci_`.
                                                - "Example: `oci_computeagent`"
                                            returned: on success
                                            type: str
                                            sample: namespace_example
                                        metrics:
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
                                                    sample: all
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
                - Returned for get operation
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
                - Returned for get operation
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
                                          selectors,https://jmespath.org/specification.html): expression with dot and index operator (`.` and `L(]`).
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
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, the message might provide actionable
                  information for a resource in a `FAILED` state.
                - Returned for list operation
            returned: on success
            type: str
            sample: lifecycle_details_example
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
    sample: [{
        "lifecyle_details": "lifecyle_details_example",
        "source": {
            "log_sources": [{
                "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
                "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
            }],
            "monitoring_sources": [{
                "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                "namespace_details": {
                    "kind": "selected",
                    "namespaces": [{
                        "namespace": "namespace_example",
                        "metrics": {
                            "kind": "all"
                        }
                    }]
                }
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.sch import ServiceConnectorClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ServiceConnectorFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "service_connector_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_service_connector,
            service_connector_id=self.module.params.get("service_connector_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_service_connectors,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ServiceConnectorFactsHelperCustom = get_custom_class(
    "ServiceConnectorFactsHelperCustom"
)


class ResourceFactsHelper(
    ServiceConnectorFactsHelperCustom, ServiceConnectorFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            service_connector_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="service_connector",
        service_client_class=ServiceConnectorClient,
        namespace="sch",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(service_connectors=result)


if __name__ == "__main__":
    main()
