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
module: oci_marketplace_accepted_agreement
short_description: Manage an AcceptedAgreement resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an AcceptedAgreement resource in Oracle Cloud Infrastructure
    - For I(state=present), accepts a terms of use agreement for a specific package version of a listing. You must accept all
      terms of use for a package before you can deploy the package.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The unique identifier for the compartment where the agreement will be accepted.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    listing_id:
        description:
            - The unique identifier for the listing associated with the agreement.
            - Required for create using I(state=present).
        type: str
    package_version:
        description:
            - The package version associated with the agreement.
            - Required for create using I(state=present).
        type: str
    agreement_id:
        description:
            - The agreement to accept.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - A display name for the accepted agreement.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    defined_tags:
        description:
            - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    accepted_agreement_id:
        description:
            - The unique identifier for the accepted terms of use agreement.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    signature:
        description:
            - A signature generated for the listing package agreements that you can retrieve
              with L(GetAgreement,https://docs.cloud.oracle.com/api/#/en/marketplace/20181001/Agreement/GetAgreement).
            - Required for create using I(state=present).
        type: str
    state:
        description:
            - The state of the AcceptedAgreement.
            - Use I(state=present) to create or update an AcceptedAgreement.
            - Use I(state=absent) to delete an AcceptedAgreement.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create accepted_agreement
  oci_marketplace_accepted_agreement:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    listing_id: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
    package_version: package_version_example
    agreement_id: "ocid1.agreement.oc1..xxxxxxEXAMPLExxxxxx"
    signature: signature_example

    # optional
    display_name: display_name_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update accepted_agreement
  oci_marketplace_accepted_agreement:
    # required
    accepted_agreement_id: "ocid1.acceptedagreement.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update accepted_agreement using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_marketplace_accepted_agreement:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Delete accepted_agreement
  oci_marketplace_accepted_agreement:
    # required
    accepted_agreement_id: "ocid1.acceptedagreement.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    signature: signature_example

- name: Delete accepted_agreement using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_marketplace_accepted_agreement:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
accepted_agreement:
    description:
        - Details of the AcceptedAgreement resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique identifier for the acceptance of the agreement within a specific compartment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A display name for the accepted agreement.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The unique identifier for the compartment where the agreement was accepted.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        listing_id:
            description:
                - The unique identifier for the listing associated with the agreement.
            returned: on success
            type: str
            sample: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
        package_version:
            description:
                - The package version associated with the agreement.
            returned: on success
            type: str
            sample: package_version_example
        agreement_id:
            description:
                - The unique identifier for the terms of use agreement itself.
            returned: on success
            type: str
            sample: "ocid1.agreement.oc1..xxxxxxEXAMPLExxxxxx"
        time_accepted:
            description:
                - The time the agreement was accepted.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        defined_tags:
            description:
                - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "listing_id": "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx",
        "package_version": "package_version_example",
        "agreement_id": "ocid1.agreement.oc1..xxxxxxEXAMPLExxxxxx",
        "time_accepted": "2013-10-20T19:20:30+01:00",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'}
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
    from oci.marketplace import MarketplaceClient
    from oci.marketplace.models import CreateAcceptedAgreementDetails
    from oci.marketplace.models import UpdateAcceptedAgreementDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AcceptedAgreementHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(AcceptedAgreementHelperGen, self).get_possible_entity_types() + [
            "acceptedagreement",
            "acceptedagreements",
            "marketplaceacceptedagreement",
            "marketplaceacceptedagreements",
            "acceptedagreementresource",
            "acceptedagreementsresource",
            "marketplace",
        ]

    def get_module_resource_id_param(self):
        return "accepted_agreement_id"

    def get_module_resource_id(self):
        return self.module.params.get("accepted_agreement_id")

    def get_get_fn(self):
        return self.client.get_accepted_agreement

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_accepted_agreement, accepted_agreement_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_accepted_agreement,
            accepted_agreement_id=self.module.params.get("accepted_agreement_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "display_name",
            "listing_id",
            "package_version",
            "accepted_agreement_id",
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
            self.client.list_accepted_agreements, **kwargs
        )

    def get_create_model_class(self):
        return CreateAcceptedAgreementDetails

    def get_exclude_attributes(self):
        return ["signature"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_accepted_agreement,
            call_fn_args=(),
            call_fn_kwargs=dict(create_accepted_agreement_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateAcceptedAgreementDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_accepted_agreement,
            call_fn_args=(),
            call_fn_kwargs=dict(
                accepted_agreement_id=self.module.params.get("accepted_agreement_id"),
                update_accepted_agreement_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_accepted_agreement,
            call_fn_args=(),
            call_fn_kwargs=dict(
                accepted_agreement_id=self.module.params.get("accepted_agreement_id"),
                signature=self.module.params.get("signature"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


AcceptedAgreementHelperCustom = get_custom_class("AcceptedAgreementHelperCustom")


class ResourceHelper(AcceptedAgreementHelperCustom, AcceptedAgreementHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            listing_id=dict(type="str"),
            package_version=dict(type="str"),
            agreement_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            accepted_agreement_id=dict(aliases=["id"], type="str"),
            signature=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="accepted_agreement",
        service_client_class=MarketplaceClient,
        namespace="marketplace",
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
