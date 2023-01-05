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
module: oci_data_safe_configuration
short_description: Manage a Configuration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a Configuration resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    is_enabled:
        description:
            - Indicates if Data Safe is enabled.
        type: bool
        required: true
    compartment_id:
        description:
            - A filter to return only resources that match the specified compartment OCID.
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the Configuration.
            - Use I(state=present) to update an existing a Configuration.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update configuration
  oci_data_safe_configuration:
    # required
    is_enabled: true

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
configuration:
    description:
        - Details of the Configuration resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        is_enabled:
            description:
                - Indicates if Data Safe is enabled.
            returned: on success
            type: bool
            sample: true
        url:
            description:
                - The URL of the Data Safe service.
            returned: on success
            type: str
            sample: url_example
        compartment_id:
            description:
                - The OCID of the tenancy used to enable Data Safe.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_enabled:
            description:
                - The date and time Data Safe was enabled, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of Data Safe.
            returned: on success
            type: str
            sample: CREATING
        data_safe_nat_gateway_ip_address:
            description:
                - The Oracle Data Safe's NAT Gateway IP Address.
            returned: on success
            type: str
            sample: data_safe_nat_gateway_ip_address_example
        global_settings:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_paid_usage:
                    description:
                        - The paid usage option chosen by the customer admin.
                    returned: on success
                    type: bool
                    sample: true
                online_retention_period:
                    description:
                        - The online retention period in months.
                    returned: on success
                    type: int
                    sample: 56
                offline_retention_period:
                    description:
                        - The offline retention period in months.
                    returned: on success
                    type: int
                    sample: 56
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "is_enabled": true,
        "url": "url_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_enabled": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "data_safe_nat_gateway_ip_address": "data_safe_nat_gateway_ip_address_example",
        "global_settings": {
            "is_paid_usage": true,
            "online_retention_period": 56,
            "offline_retention_period": 56
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.data_safe import DataSafeClient
    from oci.data_safe.models import EnableDataSafeConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_possible_entity_types(self):
        return super(
            DataSafeConfigurationHelperGen, self
        ).get_possible_entity_types() + [
            "configuration",
            "configurations",
            "dataSafeconfiguration",
            "dataSafeconfigurations",
            "configurationresource",
            "configurationsresource",
            "datasafe",
        ]

    def get_get_fn(self):
        return self.client.get_data_safe_configuration

    def get_resource(self):
        optional_params = [
            "compartment_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_data_safe_configuration, **optional_kwargs
        )

    def get_update_model_class(self):
        return EnableDataSafeConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_data_safe_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                enable_data_safe_configuration_details=update_details,
                compartment_id=self.module.params.get("compartment_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataSafeConfigurationHelperCustom = get_custom_class(
    "DataSafeConfigurationHelperCustom"
)


class ResourceHelper(DataSafeConfigurationHelperCustom, DataSafeConfigurationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            is_enabled=dict(type="bool", required=True),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="configuration",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
