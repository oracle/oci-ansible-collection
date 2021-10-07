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
module: oci_compute_management_instance_pool_instance_actions
short_description: Perform actions on an InstancePoolInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an InstancePoolInstance resource in Oracle Cloud Infrastructure
    - For I(action=detach), detaches an instance from an instance pool.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    instance_pool_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.
        type: str
        aliases: ["id"]
        required: true
    instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance.
        type: str
        required: true
    is_decrement_size:
        description:
            - Whether to decrease the size of the instance pool when the instance is detached. If `true`, the
              pool size is decreased. If `false`, the pool will provision a new, replacement instance
              using the pool's instance configuration as a template. Default is `true`.
        type: bool
    is_auto_terminate:
        description:
            - Whether to permanently terminate (delete) the instance and its attached boot volume
              when detaching it from the instance pool. Default is `false`.
        type: bool
    action:
        description:
            - The action to perform on the InstancePoolInstance.
        type: str
        required: true
        choices:
            - "detach"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action detach on instance_pool_instance
  oci_compute_management_instance_pool_instance_actions:
    instance_pool_id: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
    action: detach

"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.core import ComputeManagementClient
    from oci.core.models import DetachInstancePoolInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstancePoolInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        detach
    """

    def __init__(self, *args, **kwargs):
        super(InstancePoolInstanceActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "instance_pool_id"

    def get_module_resource_id(self):
        return self.module.params.get("instance_pool_id")

    def get_get_fn(self):
        return self.client.get_instance_pool_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_pool_instance,
            instance_pool_id=self.module.params.get("instance_pool_id"),
            instance_id=self.module.params.get("instance_id"),
        )

    def detach(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetachInstancePoolInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_instance_pool_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_pool_id=self.module.params.get("instance_pool_id"),
                detach_instance_pool_instance_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


InstancePoolInstanceActionsHelperCustom = get_custom_class(
    "InstancePoolInstanceActionsHelperCustom"
)


class ResourceHelper(
    InstancePoolInstanceActionsHelperCustom, InstancePoolInstanceActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            instance_pool_id=dict(aliases=["id"], type="str", required=True),
            instance_id=dict(type="str", required=True),
            is_decrement_size=dict(type="bool"),
            is_auto_terminate=dict(type="bool"),
            action=dict(type="str", required=True, choices=["detach"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="instance_pool_instance",
        service_client_class=ComputeManagementClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
