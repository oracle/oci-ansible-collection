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
module: oci_jms_fleet
short_description: Manage a Fleet resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Fleet resource in Oracle Cloud Infrastructure
    - For I(state=present), create a new Fleet using the information provided.
    - "`inventoryLog` is now a required parameter for CreateFleet API.
      Update existing applications using this API
      before July 15, 2022 to ensure the applications continue to work.
      See the L(Service Change Notice,https://docs.oracle.com/en-us/iaas/Content/servicechanges.htm#JMS) for more details.
      Migrate existing fleets using the `UpdateFleet` API to set the `inventoryLog` parameter."
    - "This resource has the following action operations in the M(oracle.oci.oci_jms_fleet_actions) module: change_compartment, disable_drs, enable_drs,
      generate_agent_deploy_script, request_crypto_analyses, request_java_migration_analyses, request_jfr_recordings, request_performance_tuning_analyses."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment of the Fleet.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - The name of the Fleet. The displayName must be unique for Fleets in the same compartment.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - The Fleet's description. If nothing is provided, the Fleet description will be null.
            - This parameter is updatable.
        type: str
    inventory_log:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            log_group_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the log group.
                type: str
                required: true
            log_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the log.
                type: str
                required: true
    operation_log:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            log_group_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the log group.
                type: str
                required: true
            log_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the log.
                type: str
                required: true
    is_advanced_features_enabled:
        description:
            - Whether or not advanced features are enabled in this Fleet.
              Deprecated, use `/fleets/{fleetId}/advanceFeatureConfiguration` API instead.
            - This parameter is updatable.
        type: bool
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`. (See L(Understanding Free-form
              Tags,https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm))."
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`. (See L(Managing Tags and Tag
              Namespaces,https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm).)"
            - This parameter is updatable.
        type: dict
    fleet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Fleet.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Fleet.
            - Use I(state=present) to create or update a Fleet.
            - Use I(state=absent) to delete a Fleet.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create fleet
  oci_jms_fleet:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    inventory_log:
      # required
      log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    operation_log:
      # required
      log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    is_advanced_features_enabled: true
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update fleet
  oci_jms_fleet:
    # required
    fleet_id: "ocid1.fleet.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    inventory_log:
      # required
      log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    operation_log:
      # required
      log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    is_advanced_features_enabled: true
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update fleet using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_jms_fleet:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    inventory_log:
      # required
      log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    operation_log:
      # required
      log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    is_advanced_features_enabled: true
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Delete fleet
  oci_jms_fleet:
    # required
    fleet_id: "ocid1.fleet.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete fleet using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_jms_fleet:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
fleet:
    description:
        - Details of the Fleet resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Fleet.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the Fleet.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The Fleet's description.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment of the Fleet.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        approximate_jre_count:
            description:
                - The approximate count of all unique Java Runtimes in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        approximate_installation_count:
            description:
                - The approximate count of all unique Java installations in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        approximate_application_count:
            description:
                - The approximate count of all unique applications in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        approximate_managed_instance_count:
            description:
                - The approximate count of all unique managed instances in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        approximate_java_server_count:
            description:
                - The approximate count of all unique Java servers in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        inventory_log:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                log_group_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the log group.
                    returned: on success
                    type: str
                    sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                log_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the log.
                    returned: on success
                    type: str
                    sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        operation_log:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                log_group_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the log group.
                    returned: on success
                    type: str
                    sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                log_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the log.
                    returned: on success
                    type: str
                    sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        is_advanced_features_enabled:
            description:
                - Whether or not advanced features are enabled in this Fleet.
                  Deprecated, use `/fleets/{fleetId}/advanceFeatureConfiguration` API instead.
            returned: on success
            type: bool
            sample: true
        is_export_setting_enabled:
            description:
                - Whether or not export setting is enabled in this Fleet.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The creation date and time of the Fleet (formatted according to L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339)).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The lifecycle state of the Fleet.
            returned: on success
            type: str
            sample: ACTIVE
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`. (See L(Understanding Free-form
                  Tags,https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm))."
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`. (See L(Managing Tags and Tag
                  Namespaces,https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm).)"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        system_tags:
            description:
                - System tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  System tags can be viewed by users, but can only be created by the system.
                - "Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "approximate_jre_count": 56,
        "approximate_installation_count": 56,
        "approximate_application_count": 56,
        "approximate_managed_instance_count": 56,
        "approximate_java_server_count": 56,
        "inventory_log": {
            "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
            "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "operation_log": {
            "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
            "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "is_advanced_features_enabled": true,
        "is_export_setting_enabled": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "system_tags": {}
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
    from oci.jms import JavaManagementServiceClient
    from oci.jms.models import CreateFleetDetails
    from oci.jms.models import UpdateFleetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FleetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(FleetHelperGen, self).get_possible_entity_types() + [
            "jmsfleet",
            "jmsfleets",
            "jmsjmsfleet",
            "jmsjmsfleets",
            "jmsfleetresource",
            "jmsfleetsresource",
            "fleet",
            "fleets",
            "fleetresource",
            "fleetsresource",
            "jms",
        ]

    def get_module_resource_id_param(self):
        return "fleet_id"

    def get_module_resource_id(self):
        return self.module.params.get("fleet_id")

    def get_get_fn(self):
        return self.client.get_fleet

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_fleet, fleet_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_fleet, fleet_id=self.module.params.get("fleet_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_fleets, **kwargs)

    def get_create_model_class(self):
        return CreateFleetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_fleet,
            call_fn_args=(),
            call_fn_kwargs=dict(create_fleet_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateFleetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_fleet,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fleet_id=self.module.params.get("fleet_id"),
                update_fleet_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_fleet,
            call_fn_args=(),
            call_fn_kwargs=dict(fleet_id=self.module.params.get("fleet_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


FleetHelperCustom = get_custom_class("FleetHelperCustom")


class ResourceHelper(FleetHelperCustom, FleetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            inventory_log=dict(
                type="dict",
                options=dict(
                    log_group_id=dict(type="str", required=True),
                    log_id=dict(type="str", required=True),
                ),
            ),
            operation_log=dict(
                type="dict",
                options=dict(
                    log_group_id=dict(type="str", required=True),
                    log_id=dict(type="str", required=True),
                ),
            ),
            is_advanced_features_enabled=dict(type="bool"),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            fleet_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="fleet",
        service_client_class=JavaManagementServiceClient,
        namespace="jms",
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
