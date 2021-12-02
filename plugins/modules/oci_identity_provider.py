#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_identity_provider
short_description: Manage an IdentityProvider resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an IdentityProvider resource in Oracle Cloud Infrastructure
    - "For I(state=present), **Deprecated.** For more information, see L(Deprecated IAM Service
      APIs,https://docs.cloud.oracle.com/Content/Identity/Reference/deprecatediamapis.htm)."
    - Creates a new identity provider in your tenancy. For more information, see
      L(Identity Providers and Federation,https://docs.cloud.oracle.com/Content/Identity/Concepts/federation.htm).
    - You must specify your tenancy's OCID as the compartment ID in the request object.
      Remember that the tenancy is simply the root compartment. For information about
      OCIDs, see L(Resource Identifiers,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
    - "You must also specify a *name* for the `IdentityProvider`, which must be unique
      across all `IdentityProvider` objects in your tenancy and cannot be changed."
    - "You must also specify a *description* for the `IdentityProvider` (although
      it can be an empty string). It does not have to be unique, and you can change
      it anytime with
      L(UpdateIdentityProvider,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/IdentityProvider/UpdateIdentityProvider)."
    - After you send your request, the new object's `lifecycleState` will temporarily
      be CREATING. Before using the object, first make sure its `lifecycleState` has
      changed to ACTIVE.
    - "This resource has the following action operations in the M(oracle.oci.oci_identity_provider_actions) module: reset_idp_scim_client."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of your tenancy.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    name:
        description:
            - The name you assign to the `IdentityProvider` during creation.
              The name must be unique across all `IdentityProvider` objects in the
              tenancy and cannot be changed.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - The description you assign to the `IdentityProvider` during creation.
              Does not have to be unique, and it's changeable.
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when protocol is 'SAML2'
        type: str
    product_type:
        description:
            - The identity provider service or product.
              Supported identity providers are Oracle Identity Cloud Service (IDCS) and Microsoft
              Active Directory Federation Services (ADFS).
            - "Example: `IDCS`"
            - Required for create using I(state=present).
        type: str
        choices:
            - "IDCS"
            - "ADFS"
    protocol:
        description:
            - The protocol used for federation.
            - "Example: `SAML2`"
            - Required for create using I(state=present), update using I(state=present) with identity_provider_id present.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        choices:
            - "SAML2"
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
    metadata_url:
        description:
            - The URL for retrieving the identity provider's metadata,
              which contains information required for federating.
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when protocol is 'SAML2'
        type: str
    metadata:
        description:
            - The XML that contains the information required for federating.
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when protocol is 'SAML2'
        type: str
    freeform_attributes:
        description:
            - "Extra name value pairs associated with this identity provider.
              Example: `{\\"clientId\\": \\"app_sf3kdjf3\\"}`"
            - This parameter is updatable.
        type: dict
    identity_provider_id:
        description:
            - The OCID of the identity provider.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the IdentityProvider.
            - Use I(state=present) to create or update an IdentityProvider.
            - Use I(state=absent) to delete an IdentityProvider.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create identity_provider with protocol = SAML2
  oci_identity_provider:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    product_type: IDCS
    protocol: SAML2

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    metadata_url: metadata_url_example
    metadata: metadata_example
    freeform_attributes: null

- name: Update identity_provider with protocol = SAML2
  oci_identity_provider:
    # required
    protocol: SAML2

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    metadata_url: metadata_url_example
    metadata: metadata_example
    freeform_attributes: null

- name: Update identity_provider using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with protocol = SAML2
  oci_identity_provider:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    protocol: SAML2

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    metadata_url: metadata_url_example
    metadata: metadata_example
    freeform_attributes: null

- name: Delete identity_provider
  oci_identity_provider:
    # required
    identity_provider_id: "ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete identity_provider using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with protocol = SAML2
  oci_identity_provider:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    protocol: SAML2

"""

RETURN = """
identity_provider:
    description:
        - Details of the IdentityProvider resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the `IdentityProvider`.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the tenancy containing the `IdentityProvider`.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name you assign to the `IdentityProvider` during creation. The name
                  must be unique across all `IdentityProvider` objects in the tenancy and
                  cannot be changed. This is the name federated users see when choosing
                  which identity provider to use when signing in to the Oracle Cloud Infrastructure
                  Console.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - The description you assign to the `IdentityProvider` during creation. Does
                  not have to be unique, and it's changeable.
            returned: on success
            type: str
            sample: description_example
        product_type:
            description:
                - The identity provider service or product.
                  Supported identity providers are Oracle Identity Cloud Service (IDCS) and Microsoft
                  Active Directory Federation Services (ADFS).
                - "Allowed values are:
                  - `ADFS`
                  - `IDCS`"
                - "Example: `IDCS`"
            returned: on success
            type: str
            sample: IDCS
        time_created:
            description:
                - Date and time the `IdentityProvider` was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        lifecycle_state:
            description:
                - The current state. After creating an `IdentityProvider`, make sure its
                  `lifecycleState` changes from CREATING to ACTIVE before using it.
            returned: on success
            type: str
            sample: CREATING
        inactive_status:
            description:
                - The detailed status of INACTIVE lifecycleState.
            returned: on success
            type: int
            sample: 56
        protocol:
            description:
                - "The protocol used for federation. Allowed value: `SAML2`."
                - "Example: `SAML2`"
            returned: on success
            type: str
            sample: SAML2
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
        metadata_url:
            description:
                - The URL for retrieving the identity provider's metadata, which
                  contains information required for federating.
            returned: on success
            type: str
            sample: metadata_url_example
        metadata:
            description:
                - The XML that contains the information required for federating Identity with SAML2 Identity Provider.
            returned: on success
            type: str
            sample: metadata_example
        signing_certificate:
            description:
                - The identity provider's signing certificate used by the IAM Service
                  to validate the SAML2 token.
            returned: on success
            type: str
            sample: signing_certificate_example
        redirect_url:
            description:
                - The URL to redirect federated users to for authentication with the
                  identity provider.
            returned: on success
            type: str
            sample: redirect_url_example
        freeform_attributes:
            description:
                - "Extra name value pairs associated with this identity provider.
                  Example: `{\\"clientId\\": \\"app_sf3kdjf3\\"}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "product_type": "IDCS",
        "time_created": "2016-08-25T21:10:29.600Z",
        "lifecycle_state": "CREATING",
        "inactive_status": 56,
        "protocol": "SAML2",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "metadata_url": "metadata_url_example",
        "metadata": "metadata_example",
        "signing_certificate": "signing_certificate_example",
        "redirect_url": "redirect_url_example",
        "freeform_attributes": {}
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
    from oci.identity import IdentityClient
    from oci.identity.models import CreateIdentityProviderDetails
    from oci.identity.models import UpdateIdentityProviderDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IdentityProviderHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "identity_provider_id"

    def get_module_resource_id(self):
        return self.module.params.get("identity_provider_id")

    def get_get_fn(self):
        return self.client.get_identity_provider

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_identity_provider,
            identity_provider_id=self.module.params.get("identity_provider_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "protocol",
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
        return oci_common_utils.list_all_resources(
            self.client.list_identity_providers, **kwargs
        )

    def get_create_model_class(self):
        return CreateIdentityProviderDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_identity_provider,
            call_fn_args=(),
            call_fn_kwargs=dict(create_identity_provider_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateIdentityProviderDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_identity_provider,
            call_fn_args=(),
            call_fn_kwargs=dict(
                identity_provider_id=self.module.params.get("identity_provider_id"),
                update_identity_provider_details=update_details,
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
            call_fn=self.client.delete_identity_provider,
            call_fn_args=(),
            call_fn_kwargs=dict(
                identity_provider_id=self.module.params.get("identity_provider_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


IdentityProviderHelperCustom = get_custom_class("IdentityProviderHelperCustom")


class ResourceHelper(IdentityProviderHelperCustom, IdentityProviderHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            description=dict(type="str"),
            product_type=dict(type="str", choices=["IDCS", "ADFS"]),
            protocol=dict(type="str", choices=["SAML2"]),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            metadata_url=dict(type="str"),
            metadata=dict(type="str"),
            freeform_attributes=dict(type="dict"),
            identity_provider_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="identity_provider",
        service_client_class=IdentityClient,
        namespace="identity",
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
