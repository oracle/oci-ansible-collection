#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_streaming_connect_harness
short_description: Manage a ConnectHarness resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ConnectHarness resource in Oracle Cloud Infrastructure
    - For I(state=present), starts the provisioning of a new connect harness.
      To track the progress of the provisioning, you can periodically call L(GetConnectHarness].
      In the response, the `lifecycleState` parameter of the [ConnectHarness,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/streaming/20180418/ConnectHarness/) object tells you its current state.
version_added: "2.9"
author: Oracle (@oracle)
options:
    name:
        description:
            - The name of the connect harness. Avoid entering confidential information.
            - "Example: `JDBCConnector`"
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment that contains the connect harness.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for
              cross-compatibility only.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    connect_harness_id:
        description:
            - The OCID of the connect harness.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ConnectHarness.
            - Use I(state=present) to create or update a ConnectHarness.
            - Use I(state=absent) to delete a ConnectHarness.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create connect_harness
  oci_streaming_connect_harness:
    compartment_id: ocid1.tenancy.oc1..exampleasgadvsw7l6cvb4fhssurjqs4irbkzma3wc2fauxv4novazj5guta
    name: mynewconnectharness

- name: Update connect_harness using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_streaming_connect_harness:
    name: mynewconnectharness
    compartment_id: ocid1.tenancy.oc1..exampleasgadvsw7l6cvb4fhssurjqs4irbkzma3wc2fauxv4novazj5guta
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update connect_harness
  oci_streaming_connect_harness:
    connect_harness_id: ocid1.connectharness.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete connect_harness
  oci_streaming_connect_harness:
    connect_harness_id: ocid1.connectharness.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete connect_harness using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_streaming_connect_harness:
    name: mynewconnectharness
    compartment_id: ocid1.tenancy.oc1..exampleasgadvsw7l6cvb4fhssurjqs4irbkzma3wc2fauxv4novazj5guta
    state: absent

"""

RETURN = """
connect_harness:
    description:
        - Details of the ConnectHarness resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the connect harness. Avoid entering confidential information.
                - "Example: `JDBCConnector`"
            returned: on success
            type: string
            sample: TelemetryEvents
        id:
            description:
                - The OCID of the connect harness.
            returned: on success
            type: string
            sample: ocid1.connectharness.realm.region.mnopqr789
        compartment_id:
            description:
                - The OCID of the compartment that contains the connect harness.
            returned: on success
            type: string
            sample: ocid1.compartment.realm.region.zxcvbn432765
        lifecycle_state:
            description:
                - The current state of the connect harness.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_state_details:
            description:
                - Any additional details about the current state of the connect harness.
            returned: on success
            type: string
            sample: lifecycle_state_details_example
        time_created:
            description:
                - The date and time the connect harness was created, expressed in in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2018-04-20T00:00:07.405Z`"
            returned: on success
            type: string
            sample: 2018-04-20T00:00:07.405Z
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-
                  compatibility only.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}'"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "name": "TelemetryEvents",
        "id": "ocid1.connectharness.realm.region.mnopqr789",
        "compartment_id": "ocid1.compartment.realm.region.zxcvbn432765",
        "lifecycle_state": "CREATING",
        "lifecycle_state_details": "lifecycle_state_details_example",
        "time_created": "2018-04-20T00:00:07.405Z",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.streaming import StreamAdminClient
    from oci.streaming.models import CreateConnectHarnessDetails
    from oci.streaming.models import UpdateConnectHarnessDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConnectHarnessHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "connect_harness_id"

    def get_module_resource_id(self):
        return self.module.params.get("connect_harness_id")

    def get_get_fn(self):
        return self.client.get_connect_harness

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connect_harness,
            connect_harness_id=self.module.params.get("connect_harness_id"),
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
            self.client.list_connect_harnesses, **kwargs
        )

    def get_create_model_class(self):
        return CreateConnectHarnessDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_connect_harness,
            call_fn_args=(),
            call_fn_kwargs=dict(create_connect_harness_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateConnectHarnessDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_connect_harness,
            call_fn_args=(),
            call_fn_kwargs=dict(
                connect_harness_id=self.module.params.get("connect_harness_id"),
                update_connect_harness_details=update_details,
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
            call_fn=self.client.delete_connect_harness,
            call_fn_args=(),
            call_fn_kwargs=dict(
                connect_harness_id=self.module.params.get("connect_harness_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ConnectHarnessHelperCustom = get_custom_class("ConnectHarnessHelperCustom")


class ResourceHelper(ConnectHarnessHelperCustom, ConnectHarnessHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            compartment_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            connect_harness_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="connect_harness",
        service_client_class=StreamAdminClient,
        namespace="streaming",
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
