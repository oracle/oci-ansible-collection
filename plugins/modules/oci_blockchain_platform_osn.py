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
module: oci_blockchain_platform_osn
short_description: Manage a BlockchainPlatformOsn resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a BlockchainPlatformOsn resource in Oracle Cloud Infrastructure
    - For I(state=present), create Blockchain Platform Osn
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    blockchain_platform_id:
        description:
            - Unique service identifier.
        type: str
        required: true
    ad:
        description:
            - Availability Domain to place new OSN
            - Required for create using I(state=present).
        type: str
    ocpu_allocation_param:
        description:
            - ""
            - Required for update using I(state=present) with osn_id present.
        type: dict
        suboptions:
            ocpu_allocation_number:
                description:
                    - Number of OCPU allocation
                type: float
                required: true
    osn_id:
        description:
            - OSN identifier.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the BlockchainPlatformOsn.
            - Use I(state=present) to create or update a BlockchainPlatformOsn.
            - Use I(state=absent) to delete a BlockchainPlatformOsn.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create blockchain_platform_osn
  oci_blockchain_platform_osn:
    # required
    blockchain_platform_id: "ocid1.blockchainplatform.oc1..xxxxxxEXAMPLExxxxxx"
    ad: ad_example

    # optional
    ocpu_allocation_param:
      # required
      ocpu_allocation_number: 3.4

- name: Update blockchain_platform_osn
  oci_blockchain_platform_osn:
    # required
    blockchain_platform_id: "ocid1.blockchainplatform.oc1..xxxxxxEXAMPLExxxxxx"
    ocpu_allocation_param:
      # required
      ocpu_allocation_number: 3.4
    osn_id: "ocid1.osn.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete blockchain_platform_osn
  oci_blockchain_platform_osn:
    # required
    blockchain_platform_id: "ocid1.blockchainplatform.oc1..xxxxxxEXAMPLExxxxxx"
    osn_id: "ocid1.osn.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
blockchain_platform_osn:
    description:
        - Details of the BlockchainPlatformOsn resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        osn_key:
            description:
                - OSN identifier
            returned: on success
            type: str
            sample: osn_key_example
        ad:
            description:
                - Availability Domain of OSN
            returned: on success
            type: str
            sample: ad_example
        ocpu_allocation_param:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                ocpu_allocation_number:
                    description:
                        - Number of OCPU allocation
                    returned: on success
                    type: float
                    sample: 3.4
        lifecycle_state:
            description:
                - The current state of the OSN.
            returned: on success
            type: str
            sample: ACTIVE
    sample: {
        "osn_key": "osn_key_example",
        "ad": "ad_example",
        "ocpu_allocation_param": {
            "ocpu_allocation_number": 3.4
        },
        "lifecycle_state": "ACTIVE"
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
    from oci.blockchain import BlockchainPlatformClient
    from oci.blockchain.models import CreateOsnDetails
    from oci.blockchain.models import UpdateOsnDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BlockchainPlatformOsnHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "osn_id"

    def get_module_resource_id(self):
        return self.module.params.get("osn_id")

    def get_get_fn(self):
        return self.client.get_osn

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_osn,
            blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
            osn_id=self.module.params.get("osn_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "blockchain_platform_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_osns, **kwargs)

    def get_create_model_class(self):
        return CreateOsnDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_osn,
            call_fn_args=(),
            call_fn_kwargs=dict(
                blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
                create_osn_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateOsnDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_osn,
            call_fn_args=(),
            call_fn_kwargs=dict(
                blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
                osn_id=self.module.params.get("osn_id"),
                update_osn_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_osn,
            call_fn_args=(),
            call_fn_kwargs=dict(
                blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
                osn_id=self.module.params.get("osn_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BlockchainPlatformOsnHelperCustom = get_custom_class(
    "BlockchainPlatformOsnHelperCustom"
)


class ResourceHelper(BlockchainPlatformOsnHelperCustom, BlockchainPlatformOsnHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            blockchain_platform_id=dict(type="str", required=True),
            ad=dict(type="str"),
            ocpu_allocation_param=dict(
                type="dict",
                options=dict(ocpu_allocation_number=dict(type="float", required=True)),
            ),
            osn_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="blockchain_platform_osn",
        service_client_class=BlockchainPlatformClient,
        namespace="blockchain",
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
