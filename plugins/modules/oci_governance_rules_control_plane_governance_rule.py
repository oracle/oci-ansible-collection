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
module: oci_governance_rules_control_plane_governance_rule
short_description: Manage a GovernanceRule resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a GovernanceRule resource in Oracle Cloud Infrastructure
    - For I(state=present), create governance rule in the root compartment only. Either relatedResourceId or template must be supplied.
    - "This resource has the following action operations in the M(oracle.oci.oci_governance_rules_control_plane_governance_rule_actions) module: retry."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the root compartment containing the governance
              rule.
            - Required for create using I(state=present).
        type: str
    type:
        description:
            - Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.
            - "Example: `QUOTA`"
            - Required for create using I(state=present).
        type: str
        choices:
            - "QUOTA"
            - "TAG"
            - "ALLOWED_REGIONS"
    creation_option:
        description:
            - The type of option used to create the governance rule, could be one of TEMPLATE or CLONE.
            - "Example: `TEMPLATE`"
            - Required for create using I(state=present).
        type: str
        choices:
            - "TEMPLATE"
            - "CLONE"
    display_name:
        description:
            - Display name of the governance rule.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Description of the governance rule.
            - This parameter is updatable.
        type: str
    template:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            name:
                description:
                    - The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.
                    - Required when type is 'TAG'
                type: str
            tags:
                description:
                    - Represents an array of tags for tag namespace.
                    - Applicable when type is 'TAG'
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - The name you assign to the tag during creation. This is the tag key definition.
                              The name must be unique within the tag namespace and cannot be changed.
                            - Required when type is 'TAG'
                        type: str
                        required: true
                    description:
                        description:
                            - The description assigned to the tag during creation.
                            - Applicable when type is 'TAG'
                        type: str
                    is_cost_tracking:
                        description:
                            - Indicates whether the tag is enabled for cost tracking.
                            - Applicable when type is 'TAG'
                        type: bool
                    validator:
                        description:
                            - ""
                            - Applicable when type is 'TAG'
                        type: dict
                        suboptions:
                            validator_type:
                                description:
                                    - "Specifies the type of validation: a static value (no validation) or a list."
                                type: str
                                choices:
                                    - "DEFAULT"
                                    - "ENUM"
                                required: true
                            values:
                                description:
                                    - The list of allowed values for a definedTag value.
                                    - Applicable when validator_type is 'ENUM'
                                type: list
                                elements: str
            tag_defaults:
                description:
                    - ""
                    - Applicable when type is 'TAG'
                type: list
                elements: dict
                suboptions:
                    tag_name:
                        description:
                            - The name of the tag. The tag default will always assign a default value for this tag name.
                            - Required when type is 'TAG'
                        type: str
                        required: true
                    value:
                        description:
                            - The default value for the tag name. This will be applied to all new resources created in the compartment.
                            - Required when type is 'TAG'
                        type: str
                        required: true
                    is_required:
                        description:
                            - If you specify that a value is required, a value is set during resource creation (either by
                              the user creating the resource or another tag default). If no value is set, resource
                              creation is blocked.
                            - "* If the `isRequired` flag is set to \\"true\\", the value is set during resource creation.
                              * If the `isRequired` flag is set to \\"false\\", the value you enter is set during resource creation."
                            - "Example: `false`"
                            - Required when type is 'TAG'
                        type: bool
                        required: true
            statements:
                description:
                    - List of quota statements.
                    - Required when type is 'QUOTA'
                type: list
                elements: str
            type:
                description:
                    - Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.
                    - "Example: `QUOTA`"
                type: str
                choices:
                    - "TAG"
                    - "QUOTA"
                    - "ALLOWED_REGIONS"
                required: true
            display_name:
                description:
                    - Display name of the quota resource.
                    - Required when type is one of ['QUOTA', 'ALLOWED_REGIONS']
                type: str
            description:
                description:
                    - Description of the tag namespace.
                type: str
            regions:
                description:
                    - List of allowed regions.
                    - Required when type is 'ALLOWED_REGIONS'
                type: list
                elements: str
    related_resource_id:
        description:
            - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the resource, which was used as a template to
              create this governance rule.
            - This parameter is updatable.
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
    governance_rule_id:
        description:
            - Unique governance rule identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the GovernanceRule.
            - Use I(state=present) to create or update a GovernanceRule.
            - Use I(state=absent) to delete a GovernanceRule.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create governance_rule
  oci_governance_rules_control_plane_governance_rule:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    type: QUOTA
    creation_option: TEMPLATE
    display_name: display_name_example
    template:
      # required
      name: name_example
      type: TAG

      # optional
      tags:
      - # required
        name: name_example

        # optional
        description: description_example
        is_cost_tracking: true
        validator:
          # required
          validator_type: DEFAULT
      tag_defaults:
      - # required
        tag_name: tag_name_example
        value: value_example
        is_required: true
      description: description_example

    # optional
    description: description_example
    related_resource_id: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update governance_rule
  oci_governance_rules_control_plane_governance_rule:
    # required
    governance_rule_id: "ocid1.governancerule.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    template:
      # required
      name: name_example
      type: TAG

      # optional
      tags:
      - # required
        name: name_example

        # optional
        description: description_example
        is_cost_tracking: true
        validator:
          # required
          validator_type: DEFAULT
      tag_defaults:
      - # required
        tag_name: tag_name_example
        value: value_example
        is_required: true
      description: description_example
    related_resource_id: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update governance_rule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_governance_rules_control_plane_governance_rule:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    template:
      # required
      name: name_example
      type: TAG

      # optional
      tags:
      - # required
        name: name_example

        # optional
        description: description_example
        is_cost_tracking: true
        validator:
          # required
          validator_type: DEFAULT
      tag_defaults:
      - # required
        tag_name: tag_name_example
        value: value_example
        is_required: true
      description: description_example
    related_resource_id: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete governance_rule
  oci_governance_rules_control_plane_governance_rule:
    # required
    governance_rule_id: "ocid1.governancerule.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete governance_rule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_governance_rules_control_plane_governance_rule:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
governance_rule:
    description:
        - Details of the GovernanceRule resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the governance rule.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the root compartment containing the
                  governance rule.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Display name of the governance rule.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the governance rule.
            returned: on success
            type: str
            sample: description_example
        type:
            description:
                - Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.
                - "Example: `QUOTA`"
            returned: on success
            type: str
            sample: QUOTA
        creation_option:
            description:
                - The type of option used to create the governance rule, could be one of TEMPLATE or CLONE.
                - "Example: `TEMPLATE`"
            returned: on success
            type: str
            sample: TEMPLATE
        template:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                regions:
                    description:
                        - List of allowed regions.
                    returned: on success
                    type: list
                    sample: []
                display_name:
                    description:
                        - Display name of the allowed region resource.
                    returned: on success
                    type: str
                    sample: display_name_example
                statements:
                    description:
                        - List of quota statements.
                    returned: on success
                    type: list
                    sample: []
                type:
                    description:
                        - Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.
                        - "Example: `QUOTA`"
                    returned: on success
                    type: str
                    sample: QUOTA
                name:
                    description:
                        - The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.
                    returned: on success
                    type: str
                    sample: name_example
                description:
                    description:
                        - Description of the allowed region resource.
                    returned: on success
                    type: str
                    sample: description_example
                tags:
                    description:
                        - Represents an array of tags for tag namespace.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The name you assign to the tag during creation. This is the tag key definition.
                                  The name must be unique within the tag namespace and cannot be changed.
                            returned: on success
                            type: str
                            sample: name_example
                        description:
                            description:
                                - The description assigned to the tag during creation.
                            returned: on success
                            type: str
                            sample: description_example
                        is_cost_tracking:
                            description:
                                - Indicates whether the tag is enabled for cost tracking.
                            returned: on success
                            type: bool
                            sample: true
                        validator:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                validator_type:
                                    description:
                                        - "Specifies the type of validation: a static value (no validation) or a list."
                                    returned: on success
                                    type: str
                                    sample: ENUM
                                values:
                                    description:
                                        - The list of allowed values for a definedTag value.
                                    returned: on success
                                    type: list
                                    sample: []
                tag_defaults:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        tag_name:
                            description:
                                - The name of the tag. The tag default will always assign a default value for this tag name.
                            returned: on success
                            type: str
                            sample: tag_name_example
                        value:
                            description:
                                - The default value for the tag name. This will be applied to all new resources created in the compartment.
                            returned: on success
                            type: str
                            sample: value_example
                        is_required:
                            description:
                                - If you specify that a value is required, a value is set during resource creation (either by
                                  the user creating the resource or another tag default). If no value is set, resource
                                  creation is blocked.
                                - "* If the `isRequired` flag is set to \\"true\\", the value is set during resource creation.
                                  * If the `isRequired` flag is set to \\"false\\", the value you enter is set during resource creation."
                                - "Example: `false`"
                            returned: on success
                            type: bool
                            sample: true
        related_resource_id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the resource, which was used as a template
                  to create this governance rule.
            returned: on success
            type: str
            sample: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Date and time the governance rule was created. An RFC3339 formatted datetime string.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Date and time the governance rule was updated. An RFC3339 formatted datetime string.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the governance rule.
            returned: on success
            type: str
            sample: ACTIVE
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
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "type": "QUOTA",
        "creation_option": "TEMPLATE",
        "template": {
            "regions": [],
            "display_name": "display_name_example",
            "statements": [],
            "type": "QUOTA",
            "name": "name_example",
            "description": "description_example",
            "tags": [{
                "name": "name_example",
                "description": "description_example",
                "is_cost_tracking": true,
                "validator": {
                    "validator_type": "ENUM",
                    "values": []
                }
            }],
            "tag_defaults": [{
                "tag_name": "tag_name_example",
                "value": "value_example",
                "is_required": true
            }]
        },
        "related_resource_id": "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.governance_rules_control_plane import WorkRequestClient
    from oci.governance_rules_control_plane import GovernanceRuleClient
    from oci.governance_rules_control_plane.models import CreateGovernanceRuleDetails
    from oci.governance_rules_control_plane.models import UpdateGovernanceRuleDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GovernanceRuleHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_possible_entity_types(self):
        return super(GovernanceRuleHelperGen, self).get_possible_entity_types() + [
            "organizationsgovernancerule",
            "organizationsgovernancerules",
            "governanceRulesControlPlaneorganizationsgovernancerule",
            "governanceRulesControlPlaneorganizationsgovernancerules",
            "organizationsgovernanceruleresource",
            "organizationsgovernancerulesresource",
            "governancerule",
            "governancerules",
            "governanceRulesControlPlanegovernancerule",
            "governanceRulesControlPlanegovernancerules",
            "governanceruleresource",
            "governancerulesresource",
            "governancerulescontrolplane",
        ]

    def get_module_resource_id_param(self):
        return "governance_rule_id"

    def get_module_resource_id(self):
        return self.module.params.get("governance_rule_id")

    def get_get_fn(self):
        return self.client.get_governance_rule

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_governance_rule, governance_rule_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_governance_rule,
            governance_rule_id=self.module.params.get("governance_rule_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "compartment_id",
            "governance_rule_id",
            "display_name",
        ]

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
            self.client.list_governance_rules, **kwargs
        )

    def get_create_model_class(self):
        return CreateGovernanceRuleDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_governance_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(create_governance_rule_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateGovernanceRuleDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_governance_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                governance_rule_id=self.module.params.get("governance_rule_id"),
                update_governance_rule_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_governance_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                governance_rule_id=self.module.params.get("governance_rule_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


GovernanceRuleHelperCustom = get_custom_class("GovernanceRuleHelperCustom")


class ResourceHelper(GovernanceRuleHelperCustom, GovernanceRuleHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            type=dict(type="str", choices=["QUOTA", "TAG", "ALLOWED_REGIONS"]),
            creation_option=dict(type="str", choices=["TEMPLATE", "CLONE"]),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            template=dict(
                type="dict",
                options=dict(
                    name=dict(type="str"),
                    tags=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str", required=True),
                            description=dict(type="str"),
                            is_cost_tracking=dict(type="bool"),
                            validator=dict(
                                type="dict",
                                options=dict(
                                    validator_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["DEFAULT", "ENUM"],
                                    ),
                                    values=dict(type="list", elements="str"),
                                ),
                            ),
                        ),
                    ),
                    tag_defaults=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            tag_name=dict(type="str", required=True),
                            value=dict(type="str", required=True),
                            is_required=dict(type="bool", required=True),
                        ),
                    ),
                    statements=dict(type="list", elements="str"),
                    type=dict(
                        type="str",
                        required=True,
                        choices=["TAG", "QUOTA", "ALLOWED_REGIONS"],
                    ),
                    display_name=dict(type="str"),
                    description=dict(type="str"),
                    regions=dict(type="list", elements="str"),
                ),
            ),
            related_resource_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            governance_rule_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="governance_rule",
        service_client_class=GovernanceRuleClient,
        namespace="governance_rules_control_plane",
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
