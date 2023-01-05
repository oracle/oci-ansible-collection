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
module: oci_tenant_manager_control_plane_domain
short_description: Manage a Domain resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Domain resource in Oracle Cloud Infrastructure
    - For I(state=present), begins the registration process for claiming a domain.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - OCID of the tenancy.
            - Required for create using I(state=present).
        type: str
    domain_name:
        description:
            - The domain name.
            - Required for create using I(state=present).
        type: str
    subscription_email:
        description:
            - The email to notify the user, and that the ONS subscription will be created with.
        type: str
    is_governance_enabled:
        description:
            - Indicates whether governance should be enabled for this domain. Defaults to false.
        type: bool
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
    domain_id:
        description:
            - The domain OCID.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
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
  oci_tenant_manager_control_plane_domain:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    domain_name: domain_name_example

    # optional
    subscription_email: subscription_email_example
    is_governance_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update domain
  oci_tenant_manager_control_plane_domain:
    # required
    domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete domain
  oci_tenant_manager_control_plane_domain:
    # required
    domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
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
                - The OCID of the domain.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        domain_name:
            description:
                - The domain name.
            returned: on success
            type: str
            sample: domain_name_example
        owner_id:
            description:
                - The OCID of the tenancy that has started the registration process for this domain.
            returned: on success
            type: str
            sample: "ocid1.owner.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - Lifecycle state of the domain.
            returned: on success
            type: str
            sample: ACTIVE
        status:
            description:
                - Status of the domain.
            returned: on success
            type: str
            sample: PENDING
        txt_record:
            description:
                - The code that the owner of the domain will need to add as a TXT record to their domain.
            returned: on success
            type: str
            sample: txt_record_example
        time_created:
            description:
                - Date-time when this domain was created. An RFC 3339-formatted date and time string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Date-time when this domain was last updated. An RFC 3339-formatted date and time string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "domain_name": "domain_name_example",
        "owner_id": "ocid1.owner.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "status": "PENDING",
        "txt_record": "txt_record_example",
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
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.tenant_manager_control_plane import WorkRequestClient
    from oci.tenant_manager_control_plane import DomainClient
    from oci.tenant_manager_control_plane.models import CreateDomainDetails
    from oci.tenant_manager_control_plane.models import UpdateDomainDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DomainHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_possible_entity_types(self):
        return super(DomainHelperGen, self).get_possible_entity_types() + [
            "domain",
            "domains",
            "tenantManagerControlPlanedomain",
            "tenantManagerControlPlanedomains",
            "domainresource",
            "domainsresource",
            "tenantmanagercontrolplane",
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
        optional_list_method_params = ["domain_id"]

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
        return ["is_governance_enabled", "subscription_email", "compartment_id"]

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
            call_fn=self.client.delete_domain,
            call_fn_args=(),
            call_fn_kwargs=dict(domain_id=self.module.params.get("domain_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
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
            domain_name=dict(type="str"),
            subscription_email=dict(type="str"),
            is_governance_enabled=dict(type="bool"),
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
        service_client_class=DomainClient,
        namespace="tenant_manager_control_plane",
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
