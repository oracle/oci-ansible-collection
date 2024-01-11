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
module: oci_limits_quota_actions
short_description: Perform actions on a Quota resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Quota resource in Oracle Cloud Infrastructure
    - For I(action=add_quota_lock), adds a lock to a resource.
    - For I(action=remove_quota_lock), remove a lock from a resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    related_resource_id:
        description:
            - The resource ID that is locking this resource. Indicates that deleting this resource removes the lock.
            - Applicable only for I(action=add_quota_lock).
        type: str
    msg:
        description:
            - A message added by the lock creator. The message typically gives an
              indication of why the resource is locked.
            - Applicable only for I(action=add_quota_lock).
        type: str
        aliases: ["message"]
    quota_id:
        description:
            - The OCID of the quota.
        type: str
        aliases: ["id"]
        required: true
    type:
        description:
            - Lock type.
        type: str
        choices:
            - "FULL"
            - "DELETE"
        required: true
    action:
        description:
            - The action to perform on the Quota.
        type: str
        required: true
        choices:
            - "add_quota_lock"
            - "remove_quota_lock"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_quota_lock on quota
  oci_limits_quota_actions:
    # required
    quota_id: "ocid1.quota.oc1..xxxxxxEXAMPLExxxxxx"
    type: FULL
    action: add_quota_lock

    # optional
    related_resource_id: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
    msg: msg_example

- name: Perform action remove_quota_lock on quota
  oci_limits_quota_actions:
    # required
    quota_id: "ocid1.quota.oc1..xxxxxxEXAMPLExxxxxx"
    type: FULL
    action: remove_quota_lock

"""

RETURN = """
quota:
    description:
        - Details of the Quota resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the quota.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the resource this quota applies to.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name you assign to the quota during creation. The name must be unique across all quotas
                  in the tenancy and cannot be changed.
            returned: on success
            type: str
            sample: name_example
        statements:
            description:
                - An array of one or more quota statements written in the declarative quota statement language.
            returned: on success
            type: list
            sample: []
        locks:
            description:
                - Locks associated with this resource.
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Lock type.
                    returned: on success
                    type: str
                    sample: FULL
                related_resource_id:
                    description:
                        - The resource ID that is locking this resource. Indicates that deleting this resource removes the lock.
                    returned: on success
                    type: str
                    sample: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
                message:
                    description:
                        - A message added by the lock creator. The message typically gives an
                          indication of why the resource is locked.
                    returned: on success
                    type: str
                    sample: message_example
                time_created:
                    description:
                        - Indicates when the lock was created, in the format defined by RFC 3339.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        description:
            description:
                - The description you assign to the quota.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - "Date and time the quota was created, in the format defined by RFC 3339.
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The quota's current state. After creating a quota, make sure its `lifecycleState` is set to
                  ACTIVE before using it.
            returned: on success
            type: str
            sample: ACTIVE
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
        "name": "name_example",
        "statements": [],
        "locks": [{
            "type": "FULL",
            "related_resource_id": "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx",
            "message": "message_example",
            "time_created": "2013-10-20T19:20:30+01:00"
        }],
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.limits import QuotasClient
    from oci.limits.models import AddLockDetails
    from oci.limits.models import RemoveLockDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class QuotaActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_quota_lock
        remove_quota_lock
    """

    @staticmethod
    def get_module_resource_id_param():
        return "quota_id"

    def get_module_resource_id(self):
        return self.module.params.get("quota_id")

    def get_get_fn(self):
        return self.client.get_quota

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_quota, quota_id=self.module.params.get("quota_id"),
        )

    def add_quota_lock(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddLockDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_quota_lock,
            call_fn_args=(),
            call_fn_kwargs=dict(
                quota_id=self.module.params.get("quota_id"),
                add_lock_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def remove_quota_lock(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveLockDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_quota_lock,
            call_fn_args=(),
            call_fn_kwargs=dict(
                quota_id=self.module.params.get("quota_id"),
                remove_lock_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


QuotaActionsHelperCustom = get_custom_class("QuotaActionsHelperCustom")


class ResourceHelper(QuotaActionsHelperCustom, QuotaActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            related_resource_id=dict(type="str"),
            msg=dict(aliases=["message"], type="str"),
            quota_id=dict(aliases=["id"], type="str", required=True),
            type=dict(type="str", required=True, choices=["FULL", "DELETE"]),
            action=dict(
                type="str",
                required=True,
                choices=["add_quota_lock", "remove_quota_lock"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="quota",
        service_client_class=QuotasClient,
        namespace="limits",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
