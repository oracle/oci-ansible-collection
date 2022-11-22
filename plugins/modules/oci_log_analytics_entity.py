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
module: oci_log_analytics_entity
short_description: Manage a LogAnalyticsEntity resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a LogAnalyticsEntity resource in Oracle Cloud Infrastructure
    - For I(state=present), create a new log analytics entity.
    - "This resource has the following action operations in the M(oracle.oci.oci_log_analytics_entity_actions) module: add_entity_association,
      change_compartment, remove_entity_associations."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment Identifier L(OCID],https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    entity_type_name:
        description:
            - Log analytics entity type name.
            - Required for create using I(state=present).
        type: str
    cloud_resource_id:
        description:
            - The OCID of the Cloud resource which this entity is a representation of. This may be blank when the entity
              represents a non-cloud resource that the customer may have on their premises.
        type: str
    source_id:
        description:
            - This indicates the type of source. It is primarily for Enterprise Manager Repository ID.
        type: str
    name:
        description:
            - Log analytics entity name.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
    management_agent_id:
        description:
            - The OCID of the Management Agent.
            - This parameter is updatable.
        type: str
    timezone_region:
        description:
            - The timezone region of the log analytics entity.
            - This parameter is updatable.
        type: str
    hostname:
        description:
            - The hostname where the entity represented here is actually present. This would be the output one would get if
              they run `echo $HOSTNAME` on Linux or an equivalent OS command. This may be different from
              management agents host since logs may be collected remotely.
            - This parameter is updatable.
        type: str
    properties:
        description:
            - The name/value pairs for parameter values to be used in file patterns specified in log sources.
            - This parameter is updatable.
        type: dict
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
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    log_analytics_entity_id:
        description:
            - The log analytics entity OCID.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the LogAnalyticsEntity.
            - Use I(state=present) to create or update a LogAnalyticsEntity.
            - Use I(state=absent) to delete a LogAnalyticsEntity.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create log_analytics_entity
  oci_log_analytics_entity:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    entity_type_name: entity_type_name_example
    name: name_example
    namespace_name: namespace_name_example

    # optional
    cloud_resource_id: "ocid1.cloudresource.oc1..xxxxxxEXAMPLExxxxxx"
    source_id: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
    management_agent_id: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
    timezone_region: Asia/Kolkata
    hostname: hostname_example
    properties: null
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update log_analytics_entity
  oci_log_analytics_entity:
    # required
    namespace_name: namespace_name_example
    log_analytics_entity_id: "ocid1.loganalyticsentity.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    management_agent_id: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
    timezone_region: Asia/Kolkata
    hostname: hostname_example
    properties: null
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update log_analytics_entity using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_log_analytics_entity:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    namespace_name: namespace_name_example

    # optional
    management_agent_id: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
    timezone_region: Asia/Kolkata
    hostname: hostname_example
    properties: null
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete log_analytics_entity
  oci_log_analytics_entity:
    # required
    namespace_name: namespace_name_example
    log_analytics_entity_id: "ocid1.loganalyticsentity.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete log_analytics_entity using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_log_analytics_entity:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    namespace_name: namespace_name_example
    state: absent

"""

RETURN = """
log_analytics_entity:
    description:
        - Details of the LogAnalyticsEntity resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The log analytics entity OCID. This ID is a reference used by log analytics features and it represents
                  a resource that is provisioned and managed by the customer on their premises or on the cloud.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Log analytics entity name.
            returned: on success
            type: str
            sample: name_example
        compartment_id:
            description:
                - Compartment Identifier L(OCID],https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        entity_type_name:
            description:
                - Log analytics entity type name.
            returned: on success
            type: str
            sample: entity_type_name_example
        entity_type_internal_name:
            description:
                - Internal name for the log analytics entity type.
            returned: on success
            type: str
            sample: entity_type_internal_name_example
        lifecycle_state:
            description:
                - The current state of the log analytics entity.
            returned: on success
            type: str
            sample: ACTIVE
        lifecycle_details:
            description:
                - lifecycleDetails has additional information regarding substeps such as management agent plugin deployment.
            returned: on success
            type: str
            sample: lifecycle_details_example
        management_agent_id:
            description:
                - The OCID of the Management Agent.
            returned: on success
            type: str
            sample: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
        management_agent_display_name:
            description:
                - Management agent (management-agents resource kind) display name
            returned: on success
            type: str
            sample: management_agent_display_name_example
        management_agent_compartment_id:
            description:
                - Management agent (management-agents resource kind) compartment OCID
            returned: on success
            type: str
            sample: "ocid1.managementagentcompartment.oc1..xxxxxxEXAMPLExxxxxx"
        timezone_region:
            description:
                - The timezone region of the log analytics entity.
            returned: on success
            type: str
            sample: Asia/Kolkata
        properties:
            description:
                - The name/value pairs for parameter values to be used in file patterns specified in log sources.
            returned: on success
            type: dict
            sample: {}
        creation_source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Source that auto-created the entity.
                    returned: on success
                    type: str
                    sample: EM_BRIDGE
                details:
                    description:
                        - This will provide additional details for source of auto-creation. For example, if entity is auto-created
                          by enterprise manager bridge, this field provides additional detail on enterprise manager that contributed
                          to the entity auto-creation.
                    returned: on success
                    type: str
                    sample: details_example
        time_created:
            description:
                - The date and time the resource was created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the resource was last updated, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        are_logs_collected:
            description:
                - The Boolean flag to indicate if logs are collected for an entity for log analytics usage.
            returned: on success
            type: bool
            sample: true
        cloud_resource_id:
            description:
                - The OCID of the Cloud resource which this entity is a representation of. This may be blank when the entity
                  represents a non-cloud resource that the customer may have on their premises.
            returned: on success
            type: str
            sample: "ocid1.cloudresource.oc1..xxxxxxEXAMPLExxxxxx"
        hostname:
            description:
                - The hostname where the entity represented here is actually present. This would be the output one would get if
                  they run `echo $HOSTNAME` on Linux or an equivalent OS command. This may be different from
                  management agents host since logs may be collected remotely.
            returned: on success
            type: str
            sample: hostname_example
        source_id:
            description:
                - This indicates the type of source. It is primarily for Enterprise Manager Repository ID.
            returned: on success
            type: str
            sample: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "entity_type_name": "entity_type_name_example",
        "entity_type_internal_name": "entity_type_internal_name_example",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "management_agent_id": "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx",
        "management_agent_display_name": "management_agent_display_name_example",
        "management_agent_compartment_id": "ocid1.managementagentcompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "timezone_region": "Asia/Kolkata",
        "properties": {},
        "creation_source": {
            "type": "EM_BRIDGE",
            "details": "details_example"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "are_logs_collected": true,
        "cloud_resource_id": "ocid1.cloudresource.oc1..xxxxxxEXAMPLExxxxxx",
        "hostname": "hostname_example",
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.log_analytics import LogAnalyticsClient
    from oci.log_analytics.models import CreateLogAnalyticsEntityDetails
    from oci.log_analytics.models import UpdateLogAnalyticsEntityDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsEntityHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(LogAnalyticsEntityHelperGen, self).get_possible_entity_types() + [
            "loganalyticsentity",
            "loganalyticsentities",
            "logAnalyticsloganalyticsentity",
            "logAnalyticsloganalyticsentities",
            "loganalyticsentityresource",
            "loganalyticsentitiesresource",
            "loganalytics",
        ]

    def get_module_resource_id_param(self):
        return "log_analytics_entity_id"

    def get_module_resource_id(self):
        return self.module.params.get("log_analytics_entity_id")

    def get_get_fn(self):
        return self.client.get_log_analytics_entity

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_entity,
            log_analytics_entity_id=summary_model.id,
            namespace_name=self.module.params.get("namespace_name"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_entity,
            namespace_name=self.module.params.get("namespace_name"),
            log_analytics_entity_id=self.module.params.get("log_analytics_entity_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "namespace_name",
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["name", "cloud_resource_id", "source_id"]
            if self._use_name_as_identifier()
            else ["name", "cloud_resource_id", "hostname", "source_id"]
        )

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
            self.client.list_log_analytics_entities, **kwargs
        )

    def get_create_model_class(self):
        return CreateLogAnalyticsEntityDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_log_analytics_entity,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                create_log_analytics_entity_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateLogAnalyticsEntityDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_log_analytics_entity,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                log_analytics_entity_id=self.module.params.get(
                    "log_analytics_entity_id"
                ),
                update_log_analytics_entity_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_log_analytics_entity,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                log_analytics_entity_id=self.module.params.get(
                    "log_analytics_entity_id"
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


LogAnalyticsEntityHelperCustom = get_custom_class("LogAnalyticsEntityHelperCustom")


class ResourceHelper(LogAnalyticsEntityHelperCustom, LogAnalyticsEntityHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            entity_type_name=dict(type="str"),
            cloud_resource_id=dict(type="str"),
            source_id=dict(type="str"),
            name=dict(type="str"),
            management_agent_id=dict(type="str"),
            timezone_region=dict(type="str"),
            hostname=dict(type="str"),
            properties=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            namespace_name=dict(type="str", required=True),
            log_analytics_entity_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="log_analytics_entity",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
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
