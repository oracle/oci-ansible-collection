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
module: oci_identity_domain
short_description: Manage a Domain resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Domain resource in Oracle Cloud Infrastructure
    - For I(state=present), (For tenancies that support identity domains) Creates a new identity domain in the tenancy with the identity domain home in
      `homeRegion`.
      After you send your request, the temporary `lifecycleState` of this identity domain is set to CREATING and `lifecycleDetails` to UPDATING.
      When creation of the identity domain completes, this identity domain's `lifecycleState` is set to ACTIVE and `lifecycleDetails` to null.
    - To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves
      the operation's status.
    - After creating an `identity domain`, first make sure its `lifecycleState` changes from CREATING to ACTIVE before you use it.
    - "This resource has the following action operations in the M(oracle.oci.oci_identity_domain_actions) module: activate, change_compartment,
      change_domain_license_type, deactivate, enable_replication_to_region."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment where the identity domain is created.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    home_region:
        description:
            - The region's name identifier. See L(Regions and Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm)
              for the full list of supported region names.
            - "Example: `us-phoenix-1`"
            - Required for create using I(state=present).
        type: str
    license_type:
        description:
            - The license type of the identity domain.
            - Required for create using I(state=present).
        type: str
    admin_first_name:
        description:
            - The administrator's first name.
        type: str
    admin_last_name:
        description:
            - The administrator's last name.
        type: str
    admin_user_name:
        description:
            - The administrator's user name.
        type: str
    admin_email:
        description:
            - The administrator's email address.
        type: str
    is_notification_bypassed:
        description:
            - Indicates whether or not the administrator user created in the IDCS stripe would like to receive notifications like a welcome email.
              This field is required only if admin information is provided. This field is otherwise optional.
        type: bool
    is_primary_email_required:
        description:
            - Optional field to indicate whether users in the identity domain are required to have a primary email address or not. The default is true.
        type: bool
    description:
        description:
            - The identity domain description. You can have an empty description.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - The mutable display name of the identity domain.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    is_hidden_on_login:
        description:
            - Indicates whether the identity domain is hidden on the sign-in screen or not.
            - This parameter is updatable.
        type: bool
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
    domain_id:
        description:
            - The OCID of the identity domain.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Domain.
            - Use I(state=present) to create or update a Domain.
            - Use I(state=absent) to delete a Domain.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create domain
  oci_identity_domain:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    home_region: us-phoenix-1
    license_type: license_type_example
    description: description_example
    display_name: display_name_example

    # optional
    admin_first_name: admin_first_name_example
    admin_last_name: admin_last_name_example
    admin_user_name: admin_user_name_example
    admin_email: admin_email_example
    is_notification_bypassed: true
    is_primary_email_required: true
    is_hidden_on_login: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update domain
  oci_identity_domain:
    # required
    domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    is_hidden_on_login: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update domain using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_identity_domain:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    is_hidden_on_login: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete domain
  oci_identity_domain:
    # required
    domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete domain using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_identity_domain:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
domain:
    description:
        - Details of the Domain resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the identity domain.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the identity domain.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The mutable display name of the identity domain.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The identity domain description. You can have an empty description.
            returned: on success
            type: str
            sample: description_example
        url:
            description:
                - Region-agnostic identity domain URL.
            returned: on success
            type: str
            sample: url_example
        home_region_url:
            description:
                - Region-specific identity domain URL.
            returned: on success
            type: str
            sample: home_region_url_example
        home_region:
            description:
                - The home region for the identity domain.
                  See L(Regions and Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm)
                  for the full list of supported region names.
                - "Example: `us-phoenix-1`"
            returned: on success
            type: str
            sample: us-phoenix-1
        replica_regions:
            description:
                - The regions where replicas of the identity domain exist.
            returned: on success
            type: complex
            contains:
                region:
                    description:
                        - A REPLICATION_ENABLED region, e.g. us-ashburn-1.
                          See L(Regions and Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm)
                          for the full list of supported region names.
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                url:
                    description:
                        - Region-agnostic identity domain URL.
                    returned: on success
                    type: str
                    sample: url_example
                regional_url:
                    description:
                        - Region-specific identity domain URL.
                    returned: on success
                    type: str
                    sample: regional_url_example
                state:
                    description:
                        - The IDCS-replicated region state.
                    returned: on success
                    type: str
                    sample: ENABLING_REPLICATION
        type:
            description:
                - The type of the domain.
            returned: on success
            type: str
            sample: DEFAULT
        license_type:
            description:
                - The license type of the identity domain.
            returned: on success
            type: str
            sample: license_type_example
        is_hidden_on_login:
            description:
                - Indicates whether the identity domain is hidden on the sign-in screen or not.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - Date and time the identity domain was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Any additional details about the current state of the identity domain.
            returned: on success
            type: str
            sample: DEACTIVATING
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
        "display_name": "display_name_example",
        "description": "description_example",
        "url": "url_example",
        "home_region_url": "home_region_url_example",
        "home_region": "us-phoenix-1",
        "replica_regions": [{
            "region": "us-phoenix-1",
            "url": "url_example",
            "regional_url": "regional_url_example",
            "state": "ENABLING_REPLICATION"
        }],
        "type": "DEFAULT",
        "license_type": "license_type_example",
        "is_hidden_on_login": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "DEACTIVATING",
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
    from oci.identity import IdentityClient
    from oci.identity.models import CreateDomainDetails
    from oci.identity.models import UpdateDomainDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DomainHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DomainHelperGen, self).get_possible_entity_types() + [
            "domain",
            "domains",
            "identitydomain",
            "identitydomains",
            "domainresource",
            "domainsresource",
            "identity",
        ]

    def get_module_resource_id_param(self):
        return "domain_id"

    def get_module_resource_id(self):
        return self.module.params.get("domain_id")

    def get_get_fn(self):
        return self.client.get_domain

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_domain, domain_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_domain, domain_id=self.module.params.get("domain_id"),
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
            ["display_name", "license_type"]
            if self._use_name_as_identifier()
            else ["display_name", "license_type", "is_hidden_on_login"]
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
        return oci_common_utils.list_all_resources(self.client.list_domains, **kwargs)

    def get_create_model_class(self):
        return CreateDomainDetails

    def get_exclude_attributes(self):
        return [
            "admin_user_name",
            "admin_last_name",
            "admin_first_name",
            "is_notification_bypassed",
            "is_primary_email_required",
            "admin_email",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_domain,
            call_fn_args=(),
            call_fn_kwargs=dict(create_domain_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDomainDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_domain,
            call_fn_args=(),
            call_fn_kwargs=dict(
                domain_id=self.module.params.get("domain_id"),
                update_domain_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_domain,
            call_fn_args=(),
            call_fn_kwargs=dict(domain_id=self.module.params.get("domain_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DomainHelperCustom = get_custom_class("DomainHelperCustom")


class ResourceHelper(DomainHelperCustom, DomainHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            home_region=dict(type="str"),
            license_type=dict(type="str"),
            admin_first_name=dict(type="str"),
            admin_last_name=dict(type="str"),
            admin_user_name=dict(type="str"),
            admin_email=dict(type="str"),
            is_notification_bypassed=dict(type="bool", no_log=True),
            is_primary_email_required=dict(type="bool"),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            is_hidden_on_login=dict(type="bool"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            domain_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="domain",
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
