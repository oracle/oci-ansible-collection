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
module: oci_vbs_inst_vbs_instance
short_description: Manage a VbsInstance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a VbsInstance resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new VbsInstance.
    - "This resource has the following action operations in the M(oracle.oci.oci_vbs_inst_vbs_instance_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment Identifier
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    name:
        description:
            - Service Instance Name
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    idcs_access_token:
        description:
            - IDCS personal acceess token identifying IDCS user and stripe for the VBS service
        type: str
    display_name:
        description:
            - Display Name
            - Required for create using I(state=present), update using I(state=present) with vbs_instance_id present.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    is_resource_usage_agreement_granted:
        description:
            - Whether VBS is authorized to create and use resources in the customer tenancy
            - This parameter is updatable.
        type: bool
    resource_compartment_id:
        description:
            - Compartment where VBS may create additional resources for the service instance
            - This parameter is updatable.
        type: str
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
    vbs_instance_id:
        description:
            - unique VbsInstance identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the VbsInstance.
            - Use I(state=present) to create or update a VbsInstance.
            - Use I(state=absent) to delete a VbsInstance.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create vbs_instance
  oci_vbs_inst_vbs_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    display_name: display_name_example

    # optional
    idcs_access_token: idcs_access_token_example
    is_resource_usage_agreement_granted: true
    resource_compartment_id: "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update vbs_instance
  oci_vbs_inst_vbs_instance:
    # required
    display_name: display_name_example
    vbs_instance_id: "ocid1.vbsinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_resource_usage_agreement_granted: true
    resource_compartment_id: "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update vbs_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_vbs_inst_vbs_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    display_name: display_name_example

    # optional
    is_resource_usage_agreement_granted: true
    resource_compartment_id: "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete vbs_instance
  oci_vbs_inst_vbs_instance:
    # required
    vbs_instance_id: "ocid1.vbsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete vbs_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_vbs_inst_vbs_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    display_name: display_name_example
    state: absent

"""

RETURN = """
vbs_instance:
    description:
        - Details of the VbsInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Service instance name (unique identifier)
            returned: on success
            type: str
            sample: name_example
        display_name:
            description:
                - Service instance display name
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment of the service instance
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        is_resource_usage_agreement_granted:
            description:
                - Whether the VBS service instance owner explicitly approved VBS to create and use resources in the customer tenancy
            returned: on success
            type: bool
            sample: true
        resource_compartment_id:
            description:
                - Compartment where VBS may create additional resources for the service instance
            returned: on success
            type: str
            sample: "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx"
        vbs_access_url:
            description:
                - Public web URL for accessing the VBS service instance
            returned: on success
            type: str
            sample: vbs_access_url_example
        time_created:
            description:
                - The time the the VbsInstance was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the VbsInstance was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the VbsInstance.
            returned: on success
            type: str
            sample: CREATING
        lifecyle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecyle_details_example
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
        "name": "name_example",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_resource_usage_agreement_granted": true,
        "resource_compartment_id": "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "vbs_access_url": "vbs_access_url_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecyle_details": "lifecyle_details_example",
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
    from oci.vbs_inst import VbsInstanceClient
    from oci.vbs_inst.models import CreateVbsInstanceDetails
    from oci.vbs_inst.models import UpdateVbsInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VbsInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(VbsInstanceHelperGen, self).get_possible_entity_types() + [
            "service",
            "services",
            "vbsInstservice",
            "vbsInstservices",
            "serviceresource",
            "servicesresource",
            "vbsinstance",
            "vbsinstances",
            "vbsInstvbsinstance",
            "vbsInstvbsinstances",
            "vbsinstanceresource",
            "vbsinstancesresource",
            "vbsinst",
        ]

    def get_module_resource_id_param(self):
        return "vbs_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("vbs_instance_id")

    def get_get_fn(self):
        return self.client.get_vbs_instance

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_vbs_instance, vbs_instance_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vbs_instance,
            vbs_instance_id=self.module.params.get("vbs_instance_id"),
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
        return oci_common_utils.list_all_resources(
            self.client.list_vbs_instances, **kwargs
        )

    def get_create_model_class(self):
        return CreateVbsInstanceDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_vbs_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_vbs_instance_details=create_details,
                idcs_access_token=self.module.params.get("idcs_access_token"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateVbsInstanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_vbs_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vbs_instance_id=self.module.params.get("vbs_instance_id"),
                update_vbs_instance_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_vbs_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vbs_instance_id=self.module.params.get("vbs_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


VbsInstanceHelperCustom = get_custom_class("VbsInstanceHelperCustom")


class ResourceHelper(VbsInstanceHelperCustom, VbsInstanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            idcs_access_token=dict(type="str", no_log=True),
            display_name=dict(type="str"),
            is_resource_usage_agreement_granted=dict(type="bool"),
            resource_compartment_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            vbs_instance_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vbs_instance",
        service_client_class=VbsInstanceClient,
        namespace="vbs_inst",
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
