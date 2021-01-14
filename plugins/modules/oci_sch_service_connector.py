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
module: oci_sch_service_connector
short_description: Manage a ServiceConnector resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ServiceConnector resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new service connector in the specified compartment.
      A service connector is a logically defined flow for moving data from
      a source service to a destination service in Oracle Cloud Infrastructure.
      For general information about service connectors, see
      L(Service Connector Hub Overview,https://docs.cloud.oracle.com/iaas/Content/service-connector-hub/overview.htm).
    - For purposes of access control, you must provide the
      L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where
      you want the service connector to reside. Notice that the service connector
      doesn't have to be in the same compartment as the source or target services.
      For information about access control and compartments, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
    - After you send your request, the new service connector's state is temporarily
      CREATING. When the state changes to ACTIVE, data begins transferring from the
      source service to the target service. For instructions on deactivating and
      activating service connectors, see
      L(To activate or deactivate a service connector,https://docs.cloud.oracle.com/iaas/Content/service-connector-hub/overview.htm).
    - "This resource has the following action operations in the M(oci_service_connector_actions) module: activate, deactivate."
version_added: "2.9"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - A user-friendly name. It does not have to be unique, and it is changeable.
              Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the
              comparment to create the service connector in.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - The description of the resource. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    source:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            kind:
                description:
                    - The type descriminator.
                type: str
                choices:
                    - "logging"
                required: true
            log_sources:
                description:
                    - The resources affected by this work request.
                type: list
                required: true
                suboptions:
                    compartment_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the log
                              source.
                        type: str
                        required: true
                    log_group_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the log group.
                        type: str
                    log_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the log.
                        type: str
    tasks:
        description:
            - The list of tasks.
            - This parameter is updatable.
        type: list
        suboptions:
            kind:
                description:
                    - The type descriminator.
                type: str
                choices:
                    - "logRule"
                required: true
            condition:
                description:
                    - A filter or mask to limit the source used in the flow defined by the service connector.
                type: str
                required: true
    target:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            kind:
                description:
                    - The type descriminator.
                type: str
                choices:
                    - "notifications"
                    - "objectStorage"
                    - "monitoring"
                    - "functions"
                    - "streaming"
                required: true
            topic_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the topic.
                    - Required when kind is 'notifications'
                type: str
            namespace:
                description:
                    - The namespace.
                    - Applicable when kind is 'objectStorage'
                type: str
            bucket_name:
                description:
                    - The name of the bucket. Avoid entering confidential information.
                    - Required when kind is 'objectStorage'
                type: str
            object_name_prefix:
                description:
                    - The prefix of the objects. Avoid entering confidential information.
                    - Applicable when kind is 'objectStorage'
                type: str
            compartment_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the metric.
                    - Required when kind is 'monitoring'
                type: str
            metric_namespace:
                description:
                    - The namespace of the metric.
                    - "Example: `oci_computeagent`"
                    - Required when kind is 'monitoring'
                type: str
            metric:
                description:
                    - The name of the metric.
                    - "Example: `CpuUtilization`"
                    - Required when kind is 'monitoring'
                type: str
            function_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the function.
                    - Required when kind is 'functions'
                type: str
            stream_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stream.
                    - Required when kind is 'streaming'
                type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    service_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the service connector.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ServiceConnector.
            - Use I(state=present) to create or update a ServiceConnector.
            - Use I(state=absent) to delete a ServiceConnector.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create service_connector
  oci_sch_service_connector:
    display_name: display_name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    source:
      kind: logging
      log_sources:
      - compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    target:
      kind: notifications

- name: Update service_connector using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_sch_service_connector:
    display_name: display_name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    description: description_example
    source:
      kind: logging
      log_sources:
      - compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    tasks:
    - kind: logRule
      condition: condition_example
    target:
      kind: notifications
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update service_connector
  oci_sch_service_connector:
    display_name: display_name_example
    description: description_example
    service_connector_id: ocid1.serviceconnector.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete service_connector
  oci_sch_service_connector:
    service_connector_id: ocid1.serviceconnector.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete service_connector using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_sch_service_connector:
    display_name: display_name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

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
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
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
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
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
                            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
                        log_group_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the log group.
                            returned: on success
                            type: string
                            sample: ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx
                        log_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the log.
                            returned: on success
                            type: string
                            sample: ocid1.log.oc1..xxxxxxEXAMPLExxxxxx
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
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the metric.
                    returned: on success
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
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
                    sample: ocid1.function.oc1..xxxxxxEXAMPLExxxxxx
                stream_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stream.
                    returned: on success
                    type: string
                    sample: ocid1.stream.oc1..xxxxxxEXAMPLExxxxxx
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
            "namespace": "namespace_example",
            "bucket_name": "bucket_name_example",
            "object_name_prefix": "object_name_prefix_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "metric_namespace": "oci_computeagent",
            "metric": "CpuUtilization",
            "function_id": "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx",
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.sch import ServiceConnectorClient
    from oci.sch.models import CreateServiceConnectorDetails
    from oci.sch.models import UpdateServiceConnectorDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ServiceConnectorHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_service_connectors, **kwargs
        )

    def get_create_model_class(self):
        return CreateServiceConnectorDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_service_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(create_service_connector_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateServiceConnectorDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_service_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                service_connector_id=self.module.params.get("service_connector_id"),
                update_service_connector_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_service_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                service_connector_id=self.module.params.get("service_connector_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ServiceConnectorHelperCustom = get_custom_class("ServiceConnectorHelperCustom")


class ResourceHelper(ServiceConnectorHelperCustom, ServiceConnectorHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            compartment_id=dict(type="str"),
            description=dict(type="str"),
            source=dict(
                type="dict",
                options=dict(
                    kind=dict(type="str", required=True, choices=["logging"]),
                    log_sources=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            compartment_id=dict(type="str", required=True),
                            log_group_id=dict(type="str"),
                            log_id=dict(type="str"),
                        ),
                    ),
                ),
            ),
            tasks=dict(
                type="list",
                elements="dict",
                options=dict(
                    kind=dict(type="str", required=True, choices=["logRule"]),
                    condition=dict(type="str", required=True),
                ),
            ),
            target=dict(
                type="dict",
                options=dict(
                    kind=dict(
                        type="str",
                        required=True,
                        choices=[
                            "notifications",
                            "objectStorage",
                            "monitoring",
                            "functions",
                            "streaming",
                        ],
                    ),
                    topic_id=dict(type="str"),
                    namespace=dict(type="str"),
                    bucket_name=dict(type="str"),
                    object_name_prefix=dict(type="str"),
                    compartment_id=dict(type="str"),
                    metric_namespace=dict(type="str"),
                    metric=dict(type="str"),
                    function_id=dict(type="str"),
                    stream_id=dict(type="str"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            service_connector_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
