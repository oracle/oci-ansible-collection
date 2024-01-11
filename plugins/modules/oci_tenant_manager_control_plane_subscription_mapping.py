#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_tenant_manager_control_plane_subscription_mapping
short_description: Manage a SubscriptionMapping resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a SubscriptionMapping resource in Oracle Cloud Infrastructure
    - For I(state=present), assign the tenancy record identified by the compartment ID to the given subscription ID.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - OCID of the compartment. Always a tenancy OCID.
            - Required for create using I(state=present).
        type: str
    subscription_id:
        description:
            - OCID of Subscription.
            - Required for create using I(state=present).
        type: str
    subscription_mapping_id:
        description:
            - OCID of the subscription mapping ID.
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the SubscriptionMapping.
            - Use I(state=present) to create a SubscriptionMapping.
            - Use I(state=absent) to delete a SubscriptionMapping.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create subscription_mapping
  oci_tenant_manager_control_plane_subscription_mapping:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete subscription_mapping
  oci_tenant_manager_control_plane_subscription_mapping:
    # required
    subscription_mapping_id: "ocid1.subscriptionmapping.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
subscription_mapping:
    description:
        - Details of the SubscriptionMapping resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID of the mapping between subscription and compartment identified by the tenancy.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        subscription_id:
            description:
                - OCID of the subscription.
            returned: on success
            type: str
            sample: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - OCID of the compartment. Always a tenancy OCID.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        is_explicitly_assigned:
            description:
                - Denotes if the subscription is explicity assigned to the root compartment or tenancy.
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - Lifecycle state of the subscriptionMapping.
            returned: on success
            type: str
            sample: CREATING
        time_terminated:
            description:
                - Date-time when subscription mapping was terminated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - Date-time when subscription mapping was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Date-time when subscription mapping was updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "subscription_id": "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_explicitly_assigned": true,
        "lifecycle_state": "CREATING",
        "time_terminated": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.tenant_manager_control_plane import WorkRequestClient
    from oci.tenant_manager_control_plane import SubscriptionClient
    from oci.tenant_manager_control_plane.models import CreateSubscriptionMappingDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SubscriptionMappingHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_possible_entity_types(self):
        return super(SubscriptionMappingHelperGen, self).get_possible_entity_types() + [
            "subscriptionmapping",
            "subscriptionmappings",
            "tenantManagerControlPlanesubscriptionmapping",
            "tenantManagerControlPlanesubscriptionmappings",
            "subscriptionmappingresource",
            "subscriptionmappingsresource",
            "tenantmanagercontrolplane",
        ]

    def get_module_resource_id_param(self):
        return "subscription_mapping_id"

    def get_module_resource_id(self):
        return self.module.params.get("subscription_mapping_id")

    def get_get_fn(self):
        return self.client.get_subscription_mapping

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_subscription_mapping,
            subscription_mapping_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_subscription_mapping,
            subscription_mapping_id=self.module.params.get("subscription_mapping_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "subscription_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["subscription_mapping_id", "compartment_id"]

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
            self.client.list_subscription_mappings, **kwargs
        )

    def get_create_model_class(self):
        return CreateSubscriptionMappingDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_subscription_mapping,
            call_fn_args=(),
            call_fn_kwargs=dict(create_subscription_mapping_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_subscription_mapping,
            call_fn_args=(),
            call_fn_kwargs=dict(
                subscription_mapping_id=self.module.params.get(
                    "subscription_mapping_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


SubscriptionMappingHelperCustom = get_custom_class("SubscriptionMappingHelperCustom")


class ResourceHelper(SubscriptionMappingHelperCustom, SubscriptionMappingHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            subscription_id=dict(type="str"),
            subscription_mapping_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="subscription_mapping",
        service_client_class=SubscriptionClient,
        namespace="tenant_manager_control_plane",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
