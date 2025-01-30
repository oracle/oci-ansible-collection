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
module: oci_log_analytics_entity_actions
short_description: Perform actions on a LogAnalyticsEntity resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a LogAnalyticsEntity resource in Oracle Cloud Infrastructure
    - For I(action=add_entity_association), adds association between input source log analytics entity and one or more existing destination entities.
    - For I(action=change_compartment), update the compartment of the log analytics entity with the given id.
    - For I(action=remove_entity_associations), delete association between input source log analytics entity and destination entities.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment where the log analytics entity should be moved.
            - Required for I(action=change_compartment).
        type: str
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    log_analytics_entity_id:
        description:
            - The log analytics entity OCID.
        type: str
        aliases: ["id"]
        required: true
    association_entities:
        description:
            - Destination entities OCIDs with which associations are to be added.
            - Required for I(action=add_entity_association), I(action=remove_entity_associations).
        type: list
        elements: str
    action:
        description:
            - The action to perform on the LogAnalyticsEntity.
        type: str
        required: true
        choices:
            - "add_entity_association"
            - "change_compartment"
            - "remove_entity_associations"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action add_entity_association on log_analytics_entity
  oci_log_analytics_entity_actions:
    # required
    namespace_name: namespace_name_example
    log_analytics_entity_id: "ocid1.loganalyticsentity.oc1..xxxxxxEXAMPLExxxxxx"
    association_entities: [ "association_entities_example" ]
    action: add_entity_association

- name: Perform action change_compartment on log_analytics_entity
  oci_log_analytics_entity_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_name: namespace_name_example
    log_analytics_entity_id: "ocid1.loganalyticsentity.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action remove_entity_associations on log_analytics_entity
  oci_log_analytics_entity_actions:
    # required
    namespace_name: namespace_name_example
    log_analytics_entity_id: "ocid1.loganalyticsentity.oc1..xxxxxxEXAMPLExxxxxx"
    association_entities: [ "association_entities_example" ]
    action: remove_entity_associations

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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.log_analytics import LogAnalyticsClient
    from oci.log_analytics.models import AddEntityAssociationDetails
    from oci.log_analytics.models import ChangeLogAnalyticsEntityCompartmentDetails
    from oci.log_analytics.models import RemoveEntityAssociationsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsEntityActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_entity_association
        change_compartment
        remove_entity_associations
    """

    @staticmethod
    def get_module_resource_id_param():
        return "log_analytics_entity_id"

    def get_module_resource_id(self):
        return self.module.params.get("log_analytics_entity_id")

    def get_get_fn(self):
        return self.client.get_log_analytics_entity

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_entity,
            namespace_name=self.module.params.get("namespace_name"),
            log_analytics_entity_id=self.module.params.get("log_analytics_entity_id"),
        )

    def add_entity_association(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddEntityAssociationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_entity_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                log_analytics_entity_id=self.module.params.get(
                    "log_analytics_entity_id"
                ),
                add_entity_association_details=action_details,
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeLogAnalyticsEntityCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_log_analytics_entity_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                log_analytics_entity_id=self.module.params.get(
                    "log_analytics_entity_id"
                ),
                change_log_analytics_entity_compartment_details=action_details,
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

    def remove_entity_associations(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveEntityAssociationsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_entity_associations,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                log_analytics_entity_id=self.module.params.get(
                    "log_analytics_entity_id"
                ),
                remove_entity_associations_details=action_details,
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


LogAnalyticsEntityActionsHelperCustom = get_custom_class(
    "LogAnalyticsEntityActionsHelperCustom"
)


class ResourceHelper(
    LogAnalyticsEntityActionsHelperCustom, LogAnalyticsEntityActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            namespace_name=dict(type="str", required=True),
            log_analytics_entity_id=dict(aliases=["id"], type="str", required=True),
            association_entities=dict(type="list", elements="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_entity_association",
                    "change_compartment",
                    "remove_entity_associations",
                ],
            ),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
