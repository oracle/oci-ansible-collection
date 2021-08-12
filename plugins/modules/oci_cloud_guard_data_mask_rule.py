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
module: oci_cloud_guard_data_mask_rule
short_description: Manage a DataMaskRule resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DataMaskRule resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Data Mask Rule Definition
version_added: "2.9"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - Data Mask Rule name
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    compartment_id:
        description:
            - Compartment Identifier where the resource is created
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable.
        type: str
    description:
        description:
            - The Data Mask Rule description.
        type: str
    iam_group_id:
        description:
            - IAM Group id associated with the data mask rule
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    target_selected:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            kind:
                description:
                    - Target selection.
                type: str
                choices:
                    - "ALL"
                    - "TARGETTYPES"
                    - "TARGETIDS"
                required: true
            values:
                description:
                    - Types of Targets
                    - Applicable when kind is one of ['TARGETTYPES', 'TARGETIDS']
                type: list
                choices:
                    - "COMPARTMENT"
                    - "ERPCLOUD"
                    - "HCMCLOUD"
    data_mask_categories:
        description:
            - Data Mask Categories
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        choices:
            - "ACTOR"
            - "PII"
            - "PHI"
            - "FINANCIAL"
            - "LOCATION"
            - "CUSTOM"
    data_mask_rule_status:
        description:
            - The status of the dataMaskRule.
            - This parameter is updatable.
        type: str
        choices:
            - "ENABLED"
            - "DISABLED"
    lifecycle_state:
        description:
            - The current state of the DataMaskRule.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
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
    data_mask_rule_id:
        description:
            - OCID of dataMaskRule
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DataMaskRule.
            - Use I(state=present) to create or update a DataMaskRule.
            - Use I(state=absent) to delete a DataMaskRule.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create data_mask_rule
  oci_cloud_guard_data_mask_rule:
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    iam_group_id: "ocid1.iamgroup.oc1..xxxxxxEXAMPLExxxxxx"
    target_selected:
      kind: ALL

- name: Update data_mask_rule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_guard_data_mask_rule:
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    iam_group_id: "ocid1.iamgroup.oc1..xxxxxxEXAMPLExxxxxx"
    target_selected:
      kind: ALL
    data_mask_rule_status: ENABLED
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update data_mask_rule
  oci_cloud_guard_data_mask_rule:
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    data_mask_rule_id: "ocid1.datamaskrule.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete data_mask_rule
  oci_cloud_guard_data_mask_rule:
    data_mask_rule_id: "ocid1.datamaskrule.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete data_mask_rule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_guard_data_mask_rule:
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
data_mask_rule:
    description:
        - Details of the DataMaskRule resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Data Mask Rule Identifier, can be renamed
            returned: on success
            type: string
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier where the resource is created
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - The data mask rule description.
            returned: on success
            type: string
            sample: description_example
        iam_group_id:
            description:
                - IAM Group id associated with the data mask rule
            returned: on success
            type: string
            sample: "ocid1.iamgroup.oc1..xxxxxxEXAMPLExxxxxx"
        target_selected:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                kind:
                    description:
                        - Target selection.
                    returned: on success
                    type: string
                    sample: ALL
                values:
                    description:
                        - Ids of Target
                    returned: on success
                    type: list
                    sample: []
        data_mask_categories:
            description:
                - Data Mask Categories
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The date and time the target was created. Format defined by RFC3339.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The date and time the target was updated. Format defined by RFC3339.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        data_mask_rule_status:
            description:
                - The status of the dataMaskRule.
            returned: on success
            type: string
            sample: ENABLED
        lifecycle_state:
            description:
                - The current state of the DataMaskRule.
            returned: on success
            type: string
            sample: CREATING
        lifecyle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: string
            sample: lifecyle_details_example
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
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "iam_group_id": "ocid1.iamgroup.oc1..xxxxxxEXAMPLExxxxxx",
        "target_selected": {
            "kind": "ALL",
            "values": []
        },
        "data_mask_categories": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "data_mask_rule_status": "ENABLED",
        "lifecycle_state": "CREATING",
        "lifecyle_details": "lifecyle_details_example",
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
    from oci.cloud_guard import CloudGuardClient
    from oci.cloud_guard.models import CreateDataMaskRuleDetails
    from oci.cloud_guard.models import UpdateDataMaskRuleDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataMaskRuleHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "data_mask_rule_id"

    def get_module_resource_id(self):
        return self.module.params.get("data_mask_rule_id")

    def get_get_fn(self):
        return self.client.get_data_mask_rule

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_mask_rule,
            data_mask_rule_id=self.module.params.get("data_mask_rule_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name", "lifecycle_state"]
            if self._use_name_as_identifier()
            else [
                "display_name",
                "lifecycle_state",
                "data_mask_rule_status",
                "iam_group_id",
            ]
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
            self.client.list_data_mask_rules, **kwargs
        )

    def get_create_model_class(self):
        return CreateDataMaskRuleDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_data_mask_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(create_data_mask_rule_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateDataMaskRuleDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_data_mask_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                data_mask_rule_id=self.module.params.get("data_mask_rule_id"),
                update_data_mask_rule_details=update_details,
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
            call_fn=self.client.delete_data_mask_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                data_mask_rule_id=self.module.params.get("data_mask_rule_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DataMaskRuleHelperCustom = get_custom_class("DataMaskRuleHelperCustom")


class ResourceHelper(DataMaskRuleHelperCustom, DataMaskRuleHelperGen):
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
            iam_group_id=dict(type="str"),
            target_selected=dict(
                type="dict",
                options=dict(
                    kind=dict(
                        type="str",
                        required=True,
                        choices=["ALL", "TARGETTYPES", "TARGETIDS"],
                    ),
                    values=dict(
                        type="list", choices=["COMPARTMENT", "ERPCLOUD", "HCMCLOUD"]
                    ),
                ),
            ),
            data_mask_categories=dict(
                type="list",
                choices=["ACTOR", "PII", "PHI", "FINANCIAL", "LOCATION", "CUSTOM"],
            ),
            data_mask_rule_status=dict(type="str", choices=["ENABLED", "DISABLED"]),
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
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            data_mask_rule_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="data_mask_rule",
        service_client_class=CloudGuardClient,
        namespace="cloud_guard",
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
