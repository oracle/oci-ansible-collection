#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_data_safe_configuration_facts
short_description: Fetches details about a Configuration resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Configuration resource in Oracle Cloud Infrastructure
    - Gets the details of the Data Safe configuration.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - A filter to return only resources that match the specified compartment OCID.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific configuration
  oci_data_safe_configuration_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
configuration:
    description:
        - Configuration resource
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

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_safe import DataSafeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeConfigurationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return []

    def get_resource(self):
        optional_get_method_params = [
            "compartment_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_data_safe_configuration, **optional_kwargs
        )


DataSafeConfigurationFactsHelperCustom = get_custom_class(
    "DataSafeConfigurationFactsHelperCustom"
)


class ResourceFactsHelper(
    DataSafeConfigurationFactsHelperCustom, DataSafeConfigurationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(compartment_id=dict(type="str"),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="configuration",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(configuration=result)


if __name__ == "__main__":
    main()
