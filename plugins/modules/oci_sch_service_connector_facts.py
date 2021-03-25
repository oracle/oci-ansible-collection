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
module: oci_sch_service_connector_facts
short_description: Fetches details about one or multiple ServiceConnector resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ServiceConnector resources in Oracle Cloud Infrastructure
    - Lists service connectors in the specified compartment.
    - If I(service_connector_id) is specified, the details of a single ServiceConnector will be returned.
version_added: "2.9"
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
- name: List service_connectors
  oci_sch_service_connector_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific service_connector
  oci_sch_service_connector_facts:
    service_connector_id: "ocid1.serviceconnector.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
service_connectors:
    description:
        - List of ServiceConnector resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the service connector.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - The description of the resource. Avoid entering confidential information.
            returned: on success
            type: string
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the service connector.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The date and time when the service connector was created.
                  Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2020-01-25T21:10:29.600Z
        time_updated:
            description:
                - "The date and time when the service connector was updated.
                  Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2020-01-25T21:10:29.600Z
        lifecycle_state:
            description:
                - The current state of the service connector.
            returned: on success
            type: string
            sample: CREATING
        lifecyle_details:
            description:
                - A message describing the current state in more detail.
                  For example, the message might provide actionable
                  information for a resource in a `FAILED` state.
            returned: on success
            type: string
            sample: lifecyle_details_example
        source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                kind:
                    description:
                        - The type descriminator.
                    returned: on success
                    type: string
                    sample: logging
                log_sources:
                    description:
                        - The resources affected by this work request.
                    returned: on success
                    type: complex
                    contains:
                        compartment_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the log
                                  source.
                            returned: on success
                            type: string
                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                        log_group_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the log group.
                            returned: on success
                            type: string
                            sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                        log_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the log.
                            returned: on success
                            type: string
                            sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        tasks:
            description:
                - The list of tasks.
            returned: on success
            type: complex
            contains:
                kind:
                    description:
                        - The type descriminator.
                    returned: on success
                    type: string
                    sample: logRule
                condition:
                    description:
                        - A filter or mask to limit the source used in the flow defined by the service connector.
                    returned: on success
                    type: string
                    sample: condition_example
        target:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                kind:
                    description:
                        - The type descriminator.
                    returned: on success
                    type: string
                    sample: notifications
                topic_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the topic.
                    returned: on success
                    type: string
                    sample: ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx
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
                    type: string
                    sample: namespace_example
                bucket_name:
                    description:
                        - The name of the bucket. Avoid entering confidential information.
                    returned: on success
                    type: string
                    sample: bucket_name_example
                object_name_prefix:
                    description:
                        - The prefix of the objects. Avoid entering confidential information.
                    returned: on success
                    type: string
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
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the metric.
                    returned: on success
                    type: string
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                metric_namespace:
                    description:
                        - The namespace of the metric.
                        - "Example: `oci_computeagent`"
                    returned: on success
                    type: string
                    sample: oci_computeagent
                metric:
                    description:
                        - The name of the metric.
                        - "Example: `CpuUtilization`"
                    returned: on success
                    type: string
                    sample: CpuUtilization
                function_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the function.
                    returned: on success
                    type: string
                    sample: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
                log_group_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Logging Analytics log group.
                    returned: on success
                    type: string
                    sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                stream_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stream.
                    returned: on success
                    type: string
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
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, the message might provide actionable
                  information for a resource in a `FAILED` state.
            returned: on success
            type: string
            sample: lifecycle_details_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2020-01-25T21:10:29.600Z",
        "time_updated": "2020-01-25T21:10:29.600Z",
        "lifecycle_state": "CREATING",
        "lifecyle_details": "lifecyle_details_example",
        "source": {
            "kind": "logging",
            "log_sources": [{
                "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
                "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        },
        "tasks": [{
            "kind": "logRule",
            "condition": "condition_example"
        }],
        "target": {
            "kind": "notifications",
            "topic_id": "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx",
            "enable_formatted_messaging": true,
            "namespace": "namespace_example",
            "bucket_name": "bucket_name_example",
            "object_name_prefix": "object_name_prefix_example",
            "batch_rollover_size_in_mbs": 56,
            "batch_rollover_time_in_ms": 56,
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "metric_namespace": "oci_computeagent",
            "metric": "CpuUtilization",
            "function_id": "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx",
            "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
            "stream_id": "ocid1.stream.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "lifecycle_details": "lifecycle_details_example"
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
