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
module: oci_recovery_service_subnet
short_description: Manage a RecoveryServiceSubnet resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a RecoveryServiceSubnet resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Recovery Service Subnet.
    - "This resource has the following action operations in the M(oracle.oci.oci_recovery_service_subnet_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    subnet_id:
        description:
            - The OCID of the subnet associated with the recovery service subnet. You can create a single backup network per virtual cloud network (VCN).
            - Required for create using I(state=present).
        type: str
    vcn_id:
        description:
            - The OCID of the virtual cloud network (VCN) that contains the recovery service subnet. You can create a single recovery service subnet per VCN.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The compartment OCID.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - A user-provided name for the recovery service subnet. The 'displayName' does not have to be unique, and it can be modified. Avoid entering
              confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`. For more information, see L(Resource Tags,https://docs.oracle.com/en-
              us/iaas/Content/General/Concepts/resourcetags.htm)"
            - This parameter is updatable.
        type: dict
    recovery_service_subnet_id:
        description:
            - The recovery service subnet OCID.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the RecoveryServiceSubnet.
            - Use I(state=present) to create or update a RecoveryServiceSubnet.
            - Use I(state=absent) to delete a RecoveryServiceSubnet.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create recovery_service_subnet
  oci_recovery_service_subnet:
    # required
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update recovery_service_subnet
  oci_recovery_service_subnet:
    # required
    recovery_service_subnet_id: "ocid1.recoveryservicesubnet.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update recovery_service_subnet using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_recovery_service_subnet:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete recovery_service_subnet
  oci_recovery_service_subnet:
    # required
    recovery_service_subnet_id: "ocid1.recoveryservicesubnet.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete recovery_service_subnet using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_recovery_service_subnet:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
recovery_service_subnet:
    description:
        - Details of the RecoveryServiceSubnet resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The recovery service subnet OCID.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-provided name for the recovery service subnet.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The compartment OCID.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        vcn_id:
            description:
                - VCN Identifier.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The OCID of the subnet used as the recovery service subnet.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "An RFC3339 formatted datetime string that indicates the last created time for a recovery service subnet. For example:
                  '2020-05-22T21:10:29.600Z'."
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "An RFC3339 formatted datetime string that indicates the last updated time for a recovery service subnet. For example:
                  '2020-05-22T21:10:29.600Z'."
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - "The current state of the recovery service subnet.
                  Allowed values are:
                    - CREATING
                    - UPDATING
                    - ACTIVE
                    - DELETING
                    - DELETED
                    - FAILED"
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Detailed description about the current lifecycle state of the recovery service subnet. For example, it can be used to provide actionable
                  information for a resource in a Failed state
            returned: on success
            type: str
            sample: lifecycle_details_example
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
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`. For more information, see L(Resource Tags,https://docs.oracle.com/en-
                  us/iaas/Content/General/Concepts/resourcetags.htm)"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`. For more information, see L(Resource Tags,https://docs.oracle.com/en-
                  us/iaas/Content/General/Concepts/resourcetags.htm)"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
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
    from oci.recovery import DatabaseRecoveryClient
    from oci.recovery.models import CreateRecoveryServiceSubnetDetails
    from oci.recovery.models import UpdateRecoveryServiceSubnetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RecoveryServiceSubnetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            RecoveryServiceSubnetHelperGen, self
        ).get_possible_entity_types() + [
            "recoveryservicesubnet",
            "recoveryservicesubnets",
            "recoveryrecoveryservicesubnet",
            "recoveryrecoveryservicesubnets",
            "recoveryservicesubnetresource",
            "recoveryservicesubnetsresource",
            "recovery",
        ]

    def get_module_resource_id_param(self):
        return "recovery_service_subnet_id"

    def get_module_resource_id(self):
        return self.module.params.get("recovery_service_subnet_id")

    def get_get_fn(self):
        return self.client.get_recovery_service_subnet

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_recovery_service_subnet,
            recovery_service_subnet_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_recovery_service_subnet,
            recovery_service_subnet_id=self.module.params.get(
                "recovery_service_subnet_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name", "vcn_id"]

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
            self.client.list_recovery_service_subnets, **kwargs
        )

    def get_create_model_class(self):
        return CreateRecoveryServiceSubnetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_recovery_service_subnet,
            call_fn_args=(),
            call_fn_kwargs=dict(create_recovery_service_subnet_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateRecoveryServiceSubnetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_recovery_service_subnet,
            call_fn_args=(),
            call_fn_kwargs=dict(
                recovery_service_subnet_id=self.module.params.get(
                    "recovery_service_subnet_id"
                ),
                update_recovery_service_subnet_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_recovery_service_subnet,
            call_fn_args=(),
            call_fn_kwargs=dict(
                recovery_service_subnet_id=self.module.params.get(
                    "recovery_service_subnet_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


RecoveryServiceSubnetHelperCustom = get_custom_class(
    "RecoveryServiceSubnetHelperCustom"
)


class ResourceHelper(RecoveryServiceSubnetHelperCustom, RecoveryServiceSubnetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            subnet_id=dict(type="str"),
            vcn_id=dict(type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            recovery_service_subnet_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="recovery_service_subnet",
        service_client_class=DatabaseRecoveryClient,
        namespace="recovery",
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
