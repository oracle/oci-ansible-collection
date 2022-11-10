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
module: oci_limits_quota
short_description: Manage a Quota resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Quota resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new quota with the details supplied.
    - "This resource has the following action operations in the M(oracle.oci.oci_limits_quota_actions) module: add_quota_lock, remove_quota_lock."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment containing the resource this quota applies to.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    name:
        description:
            - The name you assign to the quota during creation. The name must be unique across all quotas
              in the tenancy and cannot be changed.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    locks:
        description:
            - Locks associated with this resource.
        type: list
        elements: dict
        suboptions:
            type:
                description:
                    - Lock type.
                type: str
                choices:
                    - "FULL"
                    - "DELETE"
                required: true
            related_resource_id:
                description:
                    - The resource ID that is locking this resource. Indicates that deleting this resource removes the lock.
                type: str
            message:
                description:
                    - A message added by the lock creator. The message typically gives an
                      indication of why the resource is locked.
                type: str
    description:
        description:
            - The description you assign to the quota.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    statements:
        description:
            - An array of quota statements written in the declarative quota statement language.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    quota_id:
        description:
            - The OCID of the quota.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    is_lock_override:
        description:
            - Whether to override locks (if any exist).
            - This parameter is updatable.
        type: bool
    state:
        description:
            - The state of the Quota.
            - Use I(state=present) to create or update a Quota.
            - Use I(state=absent) to delete a Quota.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create quota
  oci_limits_quota:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    description: description_example
    statements: [ "statements_example" ]

    # optional
    locks:
    - # required
      type: FULL

      # optional
      related_resource_id: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
      message: message_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update quota
  oci_limits_quota:
    # required
    quota_id: "ocid1.quota.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    statements: [ "statements_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_lock_override: true

- name: Update quota using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_limits_quota:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    description: description_example
    statements: [ "statements_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_lock_override: true

- name: Delete quota
  oci_limits_quota:
    # required
    quota_id: "ocid1.quota.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    is_lock_override: true

- name: Delete quota using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_limits_quota:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    state: absent

"""

RETURN = """
quota:
    description:
        - Details of the Quota resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the quota.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the resource this quota applies to.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name you assign to the quota during creation. The name must be unique across all quotas
                  in the tenancy and cannot be changed.
            returned: on success
            type: str
            sample: name_example
        statements:
            description:
                - An array of one or more quota statements written in the declarative quota statement language.
            returned: on success
            type: list
            sample: []
        locks:
            description:
                - Locks associated with this resource.
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Lock type.
                    returned: on success
                    type: str
                    sample: FULL
                related_resource_id:
                    description:
                        - The resource ID that is locking this resource. Indicates that deleting this resource removes the lock.
                    returned: on success
                    type: str
                    sample: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
                message:
                    description:
                        - A message added by the lock creator. The message typically gives an
                          indication of why the resource is locked.
                    returned: on success
                    type: str
                    sample: message_example
                time_created:
                    description:
                        - Indicates when the lock was created, in the format defined by RFC 3339.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        description:
            description:
                - The description you assign to the quota.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - "Date and time the quota was created, in the format defined by RFC 3339.
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The quota's current state. After creating a quota, make sure its `lifecycleState` is set to
                  ACTIVE before using it.
            returned: on success
            type: str
            sample: ACTIVE
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "statements": [],
        "locks": [{
            "type": "FULL",
            "related_resource_id": "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx",
            "message": "message_example",
            "time_created": "2013-10-20T19:20:30+01:00"
        }],
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
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
    from oci.limits import QuotasClient
    from oci.limits.models import CreateQuotaDetails
    from oci.limits.models import UpdateQuotaDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class QuotaHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(QuotaHelperGen, self).get_possible_entity_types() + [
            "quota",
            "quotas",
            "limitsquota",
            "limitsquotas",
            "quotaresource",
            "quotasresource",
            "limits",
        ]

    def get_module_resource_id_param(self):
        return "quota_id"

    def get_module_resource_id(self):
        return self.module.params.get("quota_id")

    def get_get_fn(self):
        return self.client.get_quota

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_quota, quota_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_quota, quota_id=self.module.params.get("quota_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

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
        return oci_common_utils.list_all_resources(self.client.list_quotas, **kwargs)

    def get_create_model_class(self):
        return CreateQuotaDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_quota,
            call_fn_args=(),
            call_fn_kwargs=dict(create_quota_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateQuotaDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_quota,
            call_fn_args=(),
            call_fn_kwargs=dict(
                quota_id=self.module.params.get("quota_id"),
                update_quota_details=update_details,
                is_lock_override=self.module.params.get("is_lock_override"),
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
            call_fn=self.client.delete_quota,
            call_fn_args=(),
            call_fn_kwargs=dict(
                quota_id=self.module.params.get("quota_id"),
                is_lock_override=self.module.params.get("is_lock_override"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


QuotaHelperCustom = get_custom_class("QuotaHelperCustom")


class ResourceHelper(QuotaHelperCustom, QuotaHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            locks=dict(
                type="list",
                elements="dict",
                options=dict(
                    type=dict(type="str", required=True, choices=["FULL", "DELETE"]),
                    related_resource_id=dict(type="str"),
                    message=dict(type="str"),
                ),
            ),
            description=dict(type="str"),
            statements=dict(type="list", elements="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            quota_id=dict(aliases=["id"], type="str"),
            is_lock_override=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="quota",
        service_client_class=QuotasClient,
        namespace="limits",
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
