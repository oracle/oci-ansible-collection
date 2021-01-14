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
module: oci_cloud_guard_configuration
short_description: Manage a Configuration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a Configuration resource in Oracle Cloud Infrastructure
version_added: "2.9"
author: Oracle (@oracle)
options:
    reporting_region:
        description:
            - The reporting region value
        type: str
        required: true
    status:
        description:
            - Status of Cloud Guard Tenant
        type: str
        choices:
            - "ENABLED"
            - "DISABLED"
        required: true
    self_manage_resources:
        description:
            - Identifies if Oracle managed resources will be created by customers.
              If no value is specified false is the default.
            - This parameter is updatable.
        type: bool
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
        required: true
    state:
        description:
            - The state of the Configuration.
            - Use I(state=present) to update an existing a Configuration.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update configuration
  oci_cloud_guard_configuration:
    reporting_region: reporting_region_example
    status: ENABLED
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
configuration:
    description:
        - Details of the Configuration resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        reporting_region:
            description:
                - The reporting region value
            returned: on success
            type: string
            sample: reporting_region_example
        status:
            description:
                - Status of Cloud Guard Tenant
            returned: on success
            type: string
            sample: ENABLED
        self_manage_resources:
            description:
                - Identifies if Oracle managed resources were created by customers
            returned: on success
            type: bool
            sample: true
    sample: {
        "reporting_region": "reporting_region_example",
        "status": "ENABLED",
        "self_manage_resources": true
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
    from oci.cloud_guard import CloudGuardClient
    from oci.cloud_guard.models import UpdateConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_get_fn(self):
        return self.client.get_configuration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_configuration,
            compartment_id=self.module.params.get("compartment_id"),
        )

    def get_update_model_class(self):
        return UpdateConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_configuration_details=update_details,
                compartment_id=self.module.params.get("compartment_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


ConfigurationHelperCustom = get_custom_class("ConfigurationHelperCustom")


class ResourceHelper(ConfigurationHelperCustom, ConfigurationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            reporting_region=dict(type="str", required=True),
            status=dict(type="str", required=True, choices=["ENABLED", "DISABLED"]),
            self_manage_resources=dict(type="bool"),
            compartment_id=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="configuration",
        service_client_class=CloudGuardClient,
        namespace="cloud_guard",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
