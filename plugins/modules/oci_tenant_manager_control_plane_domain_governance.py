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
module: oci_tenant_manager_control_plane_domain_governance
short_description: Manage a DomainGovernance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DomainGovernance resource in Oracle Cloud Infrastructure
    - For I(state=present), adds domain governance to a claimed domain.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - OCID of the tenancy.
            - Required for create using I(state=present).
        type: str
    domain_id:
        description:
            - OCID of the domain.
            - Required for create using I(state=present).
        type: str
    ons_topic_id:
        description:
            - The ONS topic associated with this domain governance entity.
            - Required for create using I(state=present).
        type: str
    ons_subscription_id:
        description:
            - The ONS subscription associated with this domain governance entity.
            - Required for create using I(state=present).
        type: str
    subscription_email:
        description:
            - Email address to be used to notify the user, and that the ONS subscription will be created with.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    is_governance_enabled:
        description:
            - Indicates whether governance is enabled for this domain.
            - This parameter is updatable.
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
    domain_governance_id:
        description:
            - The domain governance OCID.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DomainGovernance.
            - Use I(state=present) to create or update a DomainGovernance.
            - Use I(state=absent) to delete a DomainGovernance.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create domain_governance
  oci_tenant_manager_control_plane_domain_governance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
    ons_topic_id: "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx"
    ons_subscription_id: "ocid1.onssubscription.oc1..xxxxxxEXAMPLExxxxxx"
    subscription_email: subscription_email_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update domain_governance
  oci_tenant_manager_control_plane_domain_governance:
    # required
    domain_governance_id: "ocid1.domaingovernance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    subscription_email: subscription_email_example
    is_governance_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete domain_governance
  oci_tenant_manager_control_plane_domain_governance:
    # required
    domain_governance_id: "ocid1.domaingovernance.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
domain_governance:
    description:
        - Details of the DomainGovernance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the domain governance entity.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        owner_id:
            description:
                - The OCID of the tenancy that owns this domain governance entity.
            returned: on success
            type: str
            sample: "ocid1.owner.oc1..xxxxxxEXAMPLExxxxxx"
        domain_id:
            description:
                - The OCID of the domain associated with this domain governance entity.
            returned: on success
            type: str
            sample: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - Lifecycle state of the domain governance entity.
            returned: on success
            type: str
            sample: ACTIVE
        is_governance_enabled:
            description:
                - Indicates whether governance is enabled for this domain.
            returned: on success
            type: bool
            sample: true
        subscription_email:
            description:
                - Email address to be used to notify the user, and that the ONS subscription will be created with.
            returned: on success
            type: str
            sample: subscription_email_example
        ons_topic_id:
            description:
                - The ONS topic associated with this domain governance entity.
            returned: on success
            type: str
            sample: "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx"
        ons_subscription_id:
            description:
                - The ONS subscription associated with this domain governance entity.
            returned: on success
            type: str
            sample: "ocid1.onssubscription.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Date-time when this domain governance was created. An RFC 3339-formatted date and time string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Date-time when this domain governance was last updated. An RFC 3339-formatted date and time string.
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
        "owner_id": "ocid1.owner.oc1..xxxxxxEXAMPLExxxxxx",
        "domain_id": "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "is_governance_enabled": true,
        "subscription_email": "subscription_email_example",
        "ons_topic_id": "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx",
        "ons_subscription_id": "ocid1.onssubscription.oc1..xxxxxxEXAMPLExxxxxx",
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
    from oci.tenant_manager_control_plane import DomainGovernanceClient
    from oci.tenant_manager_control_plane.models import CreateDomainGovernanceDetails
    from oci.tenant_manager_control_plane.models import UpdateDomainGovernanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DomainGovernanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DomainGovernanceHelperGen, self).get_possible_entity_types() + [
            "domaingovernance",
            "domaingovernances",
            "tenantManagerControlPlanedomaingovernance",
            "tenantManagerControlPlanedomaingovernances",
            "domaingovernanceresource",
            "domaingovernancesresource",
            "tenantmanagercontrolplane",
        ]

    def get_module_resource_id_param(self):
        return "domain_governance_id"

    def get_module_resource_id(self):
        return self.module.params.get("domain_governance_id")

    def get_get_fn(self):
        return self.client.get_domain_governance

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_domain_governance, domain_governance_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_domain_governance,
            domain_governance_id=self.module.params.get("domain_governance_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["domain_id", "domain_governance_id"]

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
            self.client.list_domain_governances, **kwargs
        )

    def get_create_model_class(self):
        return CreateDomainGovernanceDetails

    def get_exclude_attributes(self):
        return ["compartment_id"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_domain_governance,
            call_fn_args=(),
            call_fn_kwargs=dict(create_domain_governance_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateDomainGovernanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_domain_governance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                domain_governance_id=self.module.params.get("domain_governance_id"),
                update_domain_governance_details=update_details,
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
            call_fn=self.client.delete_domain_governance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                domain_governance_id=self.module.params.get("domain_governance_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DomainGovernanceHelperCustom = get_custom_class("DomainGovernanceHelperCustom")


class ResourceHelper(DomainGovernanceHelperCustom, DomainGovernanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            domain_id=dict(type="str"),
            ons_topic_id=dict(type="str"),
            ons_subscription_id=dict(type="str"),
            subscription_email=dict(type="str"),
            is_governance_enabled=dict(type="bool"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            domain_governance_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="domain_governance",
        service_client_class=DomainGovernanceClient,
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
