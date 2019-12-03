#!/usr/bin/python
# Copyright (c) 2017, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_audit_configuration
short_description: Manage a Configuration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a Configuration resource in Oracle Cloud Infrastructure
version_added: "2.5"
options:
    compartment_id:
        description:
            - ID of the root compartment (tenancy)
        required: true
    retention_period_days:
        description:
            - The retention period days
        type: int
    state:
        description:
            - The state of the Configuration.
            - Use I(state=present) to update an existing a Configuration.
        required: false
        default: 'present'
        choices: ["present"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle, oracle_wait_options ]
"""

EXAMPLES = """
- name: Update configuration
  oci_audit_configuration:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    retention_period_days: 56

"""

RETURN = """
configuration:
    description:
        - Details of the Configuration resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        retention_period_days:
            description:
                - The retention period days
            returned: on success
            type: int
            sample: 56
    sample: {
        "retention_period_days": 56
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.audit import AuditClient
    from oci.audit.models import UpdateConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_configuration,
            compartment_id=self.module.params.get("compartment_id"),
        )

    def get_update_model_class(self):
        return UpdateConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_common_utils.call_with_backoff(
            self.client.update_configuration,
            compartment_id=self.module.params.get("compartment_id"),
            update_configuration_details=update_details,
        )


ConfigurationHelperCustom = get_custom_class("ConfigurationHelperCustom")


class ResourceHelper(ConfigurationHelperCustom, ConfigurationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            retention_period_days=dict(type="int"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module, resource_type="configuration", service_client_class=AuditClient
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
