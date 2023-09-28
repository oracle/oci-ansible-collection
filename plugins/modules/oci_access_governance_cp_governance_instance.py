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
module: oci_access_governance_cp_governance_instance
short_description: Manage a GovernanceInstance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a GovernanceInstance resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new GovernanceInstance.
    - "This resource has the following action operations in the M(oracle.oci.oci_access_governance_cp_governance_instance_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    tenancy_namespace:
        description:
            - The namespace for tenancy object storage.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The OCID of the compartment where the GovernanceInstance resides.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    idcs_access_token:
        description:
            - IDCS access token identifying a stripe and service administrator user.
            - Required for create using I(state=present).
        type: str
    system_tags:
        description:
            - "Usage of system tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
        type: dict
    display_name:
        description:
            - The name for the GovernanceInstance.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - The description of the GovernanceInstance.
            - This parameter is updatable.
        type: str
    license_type:
        description:
            - The licenseType being used.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "NEW_LICENSE"
            - "BRING_YOUR_OWN_LICENSE"
            - "AG_ORACLE_WORKLOADS"
            - "AG_OCI"
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    governance_instance_id:
        description:
            - The OCID of the GovernanceInstance
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the GovernanceInstance.
            - Use I(state=present) to create or update a GovernanceInstance.
            - Use I(state=absent) to delete a GovernanceInstance.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create governance_instance
  oci_access_governance_cp_governance_instance:
    # required
    tenancy_namespace: tenancy_namespace_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    idcs_access_token: idcs_access_token_example
    display_name: display_name_example
    license_type: NEW_LICENSE

    # optional
    system_tags: null
    description: description_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update governance_instance
  oci_access_governance_cp_governance_instance:
    # required
    governance_instance_id: "ocid1.governanceinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    license_type: NEW_LICENSE
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update governance_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_access_governance_cp_governance_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    license_type: NEW_LICENSE
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Delete governance_instance
  oci_access_governance_cp_governance_instance:
    # required
    governance_instance_id: "ocid1.governanceinstance.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete governance_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_access_governance_cp_governance_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
governance_instance:
    description:
        - Details of the GovernanceInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique OCID of the GovernanceInstance.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name for the GovernanceInstance.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment where the GovernanceInstance resides.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the the GovernanceInstance was created in an RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the GovernanceInstance was updated in an RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the GovernanceInstance.
            returned: on success
            type: str
            sample: CREATING
        description:
            description:
                - The description of the GovernanceInstance.
            returned: on success
            type: str
            sample: description_example
        license_type:
            description:
                - The licenseType being used.
            returned: on success
            type: str
            sample: NEW_LICENSE
        tenancy_namespace:
            description:
                - The namespace for tenancy object storage.
            returned: on success
            type: str
            sample: tenancy_namespace_example
        instance_url:
            description:
                - The access URL of the GovernanceInstance.
            returned: on success
            type: str
            sample: instance_url_example
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "description": "description_example",
        "license_type": "NEW_LICENSE",
        "tenancy_namespace": "tenancy_namespace_example",
        "instance_url": "instance_url_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
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
    from oci.access_governance_cp import AccessGovernanceCPClient
    from oci.access_governance_cp.models import CreateGovernanceInstanceDetails
    from oci.access_governance_cp.models import UpdateGovernanceInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GovernanceInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(GovernanceInstanceHelperGen, self).get_possible_entity_types() + [
            "agcsgovernanceinstance",
            "agcsgovernanceinstances",
            "accessGovernanceCpagcsgovernanceinstance",
            "accessGovernanceCpagcsgovernanceinstances",
            "agcsgovernanceinstanceresource",
            "agcsgovernanceinstancesresource",
            "governanceinstance",
            "governanceinstances",
            "accessGovernanceCpgovernanceinstance",
            "accessGovernanceCpgovernanceinstances",
            "governanceinstanceresource",
            "governanceinstancesresource",
            "accessgovernancecp",
        ]

    def get_module_resource_id_param(self):
        return "governance_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("governance_instance_id")

    def get_get_fn(self):
        return self.client.get_governance_instance

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_governance_instance,
            governance_instance_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_governance_instance,
            governance_instance_id=self.module.params.get("governance_instance_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_governance_instances, **kwargs
        )

    def get_create_model_class(self):
        return CreateGovernanceInstanceDetails

    def get_exclude_attributes(self):
        return ["idcs_access_token"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_governance_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(create_governance_instance_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateGovernanceInstanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_governance_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_governance_instance_details=update_details,
                governance_instance_id=self.module.params.get("governance_instance_id"),
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
            call_fn=self.client.delete_governance_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                governance_instance_id=self.module.params.get("governance_instance_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


GovernanceInstanceHelperCustom = get_custom_class("GovernanceInstanceHelperCustom")


class ResourceHelper(GovernanceInstanceHelperCustom, GovernanceInstanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            tenancy_namespace=dict(type="str"),
            compartment_id=dict(type="str"),
            idcs_access_token=dict(type="str", no_log=True),
            system_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            license_type=dict(
                type="str",
                choices=[
                    "NEW_LICENSE",
                    "BRING_YOUR_OWN_LICENSE",
                    "AG_ORACLE_WORKLOADS",
                    "AG_OCI",
                ],
            ),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            governance_instance_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="governance_instance",
        service_client_class=AccessGovernanceCPClient,
        namespace="access_governance_cp",
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
