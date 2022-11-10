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
module: oci_rover_entitlement
short_description: Manage a RoverEntitlement resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a RoverEntitlement resource in Oracle Cloud Infrastructure
    - For I(state=present), create the Entitlement to use a Rover Device. It requires some offline process of review and signatures before request is granted.
    - "This resource has the following action operations in the M(oracle.oci.oci_rover_entitlement_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment containing the RoverEntitlement.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    tenant_id:
        description:
            - tenant Id.
            - This parameter is updatable.
        type: str
    requestor_name:
        description:
            - Requestor name for the entitlement.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    requestor_email:
        description:
            - Requestor email for the entitlement.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    entitlement_details:
        description:
            - Details about the entitlement.
            - This parameter is updatable.
        type: str
    lifecycle_state:
        description:
            - The current state of the RoverNode.
            - This parameter is updatable.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    lifecycle_state_details:
        description:
            - A property that can contain details on the lifecycle.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    system_tags:
        description:
            - "The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined
              and scoped to namespaces.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{orcl-cloud: {free-tier-retain: true}}`"
            - This parameter is updatable.
        type: dict
    rover_entitlement_id:
        description:
            - ID of the rover node or cluster entitlement
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the RoverEntitlement.
            - Use I(state=present) to create or update a RoverEntitlement.
            - Use I(state=absent) to delete a RoverEntitlement.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create rover_entitlement
  oci_rover_entitlement:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    requestor_name: requestor_name_example
    requestor_email: requestor_email_example

    # optional
    display_name: display_name_example
    tenant_id: "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx"
    entitlement_details: entitlement_details_example
    lifecycle_state: CREATING
    lifecycle_state_details: lifecycle_state_details_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Update rover_entitlement
  oci_rover_entitlement:
    # required
    rover_entitlement_id: "ocid1.roverentitlement.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    tenant_id: "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx"
    requestor_name: requestor_name_example
    requestor_email: requestor_email_example
    entitlement_details: entitlement_details_example
    lifecycle_state: CREATING
    lifecycle_state_details: lifecycle_state_details_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Update rover_entitlement using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_rover_entitlement:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    tenant_id: "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx"
    requestor_name: requestor_name_example
    requestor_email: requestor_email_example
    entitlement_details: entitlement_details_example
    lifecycle_state: CREATING
    lifecycle_state_details: lifecycle_state_details_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Delete rover_entitlement
  oci_rover_entitlement:
    # required
    rover_entitlement_id: "ocid1.roverentitlement.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete rover_entitlement using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_rover_entitlement:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
rover_entitlement:
    description:
        - Details of the RoverEntitlement resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        tenant_id:
            description:
                - tenant Id.
            returned: on success
            type: str
            sample: "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - A property that can uniquely identify the rover entitlement.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The compartment Id for the entitlement.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        requestor_name:
            description:
                - Requestor name for the entitlement.
            returned: on success
            type: str
            sample: requestor_name_example
        requestor_email:
            description:
                - Requestor email for the entitlement.
            returned: on success
            type: str
            sample: requestor_email_example
        lifecycle_state:
            description:
                - Lifecyclestate for the entitlement.
            returned: on success
            type: str
            sample: CREATING
        entitlement_details:
            description:
                - Details about the entitlement.
            returned: on success
            type: str
            sample: entitlement_details_example
        lifecycle_state_details:
            description:
                - A property that can contain details on the lifecycle.
            returned: on success
            type: str
            sample: lifecycle_state_details_example
        time_created:
            description:
                - Time of creation for the entitlement.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time when the entitlement was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is
                  predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "tenant_id": "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "requestor_name": "requestor_name_example",
        "requestor_email": "requestor_email_example",
        "lifecycle_state": "CREATING",
        "entitlement_details": "entitlement_details_example",
        "lifecycle_state_details": "lifecycle_state_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
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
    from oci.rover import RoverEntitlementClient
    from oci.rover.models import CreateRoverEntitlementDetails
    from oci.rover.models import UpdateRoverEntitlementDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RoverEntitlementHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(RoverEntitlementHelperGen, self).get_possible_entity_types() + [
            "roverentitlement",
            "roverentitlements",
            "roverroverentitlement",
            "roverroverentitlements",
            "roverentitlementresource",
            "roverentitlementsresource",
            "rover",
        ]

    def get_module_resource_id_param(self):
        return "rover_entitlement_id"

    def get_module_resource_id(self):
        return self.module.params.get("rover_entitlement_id")

    def get_get_fn(self):
        return self.client.get_rover_entitlement

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rover_entitlement,
            rover_entitlement_id=self.module.params.get("rover_entitlement_id"),
            compartment_id=self.module.params.get("compartment_id"),
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
            ["display_name"]
            if self._use_name_as_identifier()
            else ["display_name", "lifecycle_state"]
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
            self.client.list_rover_entitlements, **kwargs
        )

    def get_create_model_class(self):
        return CreateRoverEntitlementDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_rover_entitlement,
            call_fn_args=(),
            call_fn_kwargs=dict(create_rover_entitlement_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateRoverEntitlementDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_rover_entitlement,
            call_fn_args=(),
            call_fn_kwargs=dict(
                rover_entitlement_id=self.module.params.get("rover_entitlement_id"),
                update_rover_entitlement_details=update_details,
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
            call_fn=self.client.delete_rover_entitlement,
            call_fn_args=(),
            call_fn_kwargs=dict(
                rover_entitlement_id=self.module.params.get("rover_entitlement_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


RoverEntitlementHelperCustom = get_custom_class("RoverEntitlementHelperCustom")


class ResourceHelper(RoverEntitlementHelperCustom, RoverEntitlementHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            tenant_id=dict(type="str"),
            requestor_name=dict(type="str"),
            requestor_email=dict(type="str"),
            entitlement_details=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            lifecycle_state_details=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            system_tags=dict(type="dict"),
            rover_entitlement_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="rover_entitlement",
        service_client_class=RoverEntitlementClient,
        namespace="rover",
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
