#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_identity_idp_group_mapping
short_description: Manage an IdpGroupMapping resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an IdpGroupMapping resource in Oracle Cloud Infrastructure
    - "For I(state=present), **Deprecated.** For more information, see L(Deprecated IAM Service
      APIs,https://docs.cloud.oracle.com/Content/Identity/Reference/deprecatediamapis.htm)."
    - Creates a single mapping between an IdP group and an IAM Service
      L(group,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/Group/).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    idp_group_name:
        description:
            - The name of the IdP group you want to map.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    group_id:
        description:
            - The OCID of the IAM Service L(group,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/Group/)
              you want to map to the IdP group.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    identity_provider_id:
        description:
            - The OCID of the identity provider.
        type: str
        required: true
    mapping_id:
        description:
            - The OCID of the group mapping.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the IdpGroupMapping.
            - Use I(state=present) to create or update an IdpGroupMapping.
            - Use I(state=absent) to delete an IdpGroupMapping.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create idp_group_mapping
  oci_identity_idp_group_mapping:
    # required
    idp_group_name: idp_group_name_example
    group_id: "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx"
    identity_provider_id: "ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update idp_group_mapping
  oci_identity_idp_group_mapping:
    # required
    identity_provider_id: "ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx"
    mapping_id: "ocid1.mapping.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    idp_group_name: idp_group_name_example
    group_id: "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete idp_group_mapping
  oci_identity_idp_group_mapping:
    # required
    identity_provider_id: "ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx"
    mapping_id: "ocid1.mapping.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
idp_group_mapping:
    description:
        - Details of the IdpGroupMapping resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the `IdpGroupMapping`.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        idp_id:
            description:
                - The OCID of the `IdentityProvider` this mapping belongs to.
            returned: on success
            type: str
            sample: "ocid1.idp.oc1..xxxxxxEXAMPLExxxxxx"
        idp_group_name:
            description:
                - The name of the IdP group that is mapped to the IAM Service group.
            returned: on success
            type: str
            sample: idp_group_name_example
        group_id:
            description:
                - The OCID of the IAM Service group that is mapped to the IdP group.
            returned: on success
            type: str
            sample: "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the tenancy containing the `IdentityProvider`.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Date and time the mapping was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The mapping's current state.  After creating a mapping object, make sure its `lifecycleState` changes
                  from CREATING to ACTIVE before using it.
            returned: on success
            type: str
            sample: CREATING
        inactive_status:
            description:
                - The detailed status of INACTIVE lifecycleState.
            returned: on success
            type: int
            sample: 56
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "idp_id": "ocid1.idp.oc1..xxxxxxEXAMPLExxxxxx",
        "idp_group_name": "idp_group_name_example",
        "group_id": "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "inactive_status": 56
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
    from oci.identity import IdentityClient
    from oci.identity.models import CreateIdpGroupMappingDetails
    from oci.identity.models import UpdateIdpGroupMappingDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IdpGroupMappingHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(IdpGroupMappingHelperGen, self).get_possible_entity_types() + [
            "idpgroupmapping",
            "idpgroupmappings",
            "identityidpgroupmapping",
            "identityidpgroupmappings",
            "idpgroupmappingresource",
            "idpgroupmappingsresource",
            "groupmapping",
            "groupmappings",
            "identitygroupmapping",
            "identitygroupmappings",
            "groupmappingresource",
            "groupmappingsresource",
            "identity",
        ]

    def get_module_resource_id_param(self):
        return "mapping_id"

    def get_module_resource_id(self):
        return self.module.params.get("mapping_id")

    def get_get_fn(self):
        return self.client.get_idp_group_mapping

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_idp_group_mapping,
            identity_provider_id=self.module.params.get("identity_provider_id"),
            mapping_id=self.module.params.get("mapping_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "identity_provider_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_idp_group_mappings, **kwargs
        )

    def get_create_model_class(self):
        return CreateIdpGroupMappingDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_idp_group_mapping,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_idp_group_mapping_details=create_details,
                identity_provider_id=self.module.params.get("identity_provider_id"),
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
        return UpdateIdpGroupMappingDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_idp_group_mapping,
            call_fn_args=(),
            call_fn_kwargs=dict(
                identity_provider_id=self.module.params.get("identity_provider_id"),
                mapping_id=self.module.params.get("mapping_id"),
                update_idp_group_mapping_details=update_details,
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
            call_fn=self.client.delete_idp_group_mapping,
            call_fn_args=(),
            call_fn_kwargs=dict(
                identity_provider_id=self.module.params.get("identity_provider_id"),
                mapping_id=self.module.params.get("mapping_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


IdpGroupMappingHelperCustom = get_custom_class("IdpGroupMappingHelperCustom")


class ResourceHelper(IdpGroupMappingHelperCustom, IdpGroupMappingHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            idp_group_name=dict(type="str"),
            group_id=dict(type="str"),
            identity_provider_id=dict(type="str", required=True),
            mapping_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="idp_group_mapping",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
