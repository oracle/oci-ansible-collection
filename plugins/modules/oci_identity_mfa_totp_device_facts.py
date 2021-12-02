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
module: oci_identity_mfa_totp_device_facts
short_description: Fetches details about one or multiple MfaTotpDevice resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple MfaTotpDevice resources in Oracle Cloud Infrastructure
    - Lists the MFA TOTP devices for the specified user. The returned object contains the device's OCID, but not
      the seed. The seed is returned only upon creation or when the IAM service regenerates the MFA seed for the device.
    - If I(mfa_totp_device_id) is specified, the details of a single MfaTotpDevice will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    user_id:
        description:
            - The OCID of the user.
        type: str
        required: true
    mfa_totp_device_id:
        description:
            - The OCID of the MFA TOTP device.
            - Required to get a specific mfa_totp_device.
        type: str
        aliases: ["id"]
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for NAME is ascending. The NAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by Availability Domain if the scope of the resource type is within a
              single Availability Domain. If you call one of these \\"List\\" operations without specifying
              an Availability Domain, the resources are grouped by Availability Domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "NAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific mfa_totp_device
  oci_identity_mfa_totp_device_facts:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    mfa_totp_device_id: "ocid1.mfatotpdevice.oc1..xxxxxxEXAMPLExxxxxx"

- name: List mfa_totp_devices
  oci_identity_mfa_totp_device_facts:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
mfa_totp_devices:
    description:
        - List of MfaTotpDevice resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the MFA TOTP Device.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        user_id:
            description:
                - The OCID of the user the MFA TOTP device belongs to.
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Date and time the `MfaTotpDevice` object was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        time_expires:
            description:
                - Date and time when this MFA TOTP device will expire, in the format defined by RFC3339.
                  Null if it never expires.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        lifecycle_state:
            description:
                - The MFA TOTP device's current state.
            returned: on success
            type: str
            sample: CREATING
        inactive_status:
            description:
                - "The detailed status of INACTIVE lifecycleState.
                  Allowed values are:
                   - 1 - SUSPENDED
                   - 2 - DISABLED
                   - 4 - BLOCKED
                   - 8 - LOCKED"
            returned: on success
            type: int
            sample: 56
        is_activated:
            description:
                - Flag to indicate if the MFA TOTP device has been activated
            returned: on success
            type: bool
            sample: true
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z",
        "time_expires": "2016-08-25T21:10:29.600Z",
        "lifecycle_state": "CREATING",
        "inactive_status": 56,
        "is_activated": true
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MfaTotpDeviceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "user_id",
            "mfa_totp_device_id",
        ]

    def get_required_params_for_list(self):
        return [
            "user_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_mfa_totp_device,
            user_id=self.module.params.get("user_id"),
            mfa_totp_device_id=self.module.params.get("mfa_totp_device_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_mfa_totp_devices,
            user_id=self.module.params.get("user_id"),
            **optional_kwargs
        )


MfaTotpDeviceFactsHelperCustom = get_custom_class("MfaTotpDeviceFactsHelperCustom")


class ResourceFactsHelper(MfaTotpDeviceFactsHelperCustom, MfaTotpDeviceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            user_id=dict(type="str", required=True),
            mfa_totp_device_id=dict(aliases=["id"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="mfa_totp_device",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(mfa_totp_devices=result)


if __name__ == "__main__":
    main()
