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
module: oci_apm_control_plane_data_keys_facts
short_description: Fetches details about one or multiple DataKeys resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DataKeys resources in Oracle Cloud Infrastructure
    - Lists all Data Keys for the specified APM domain. The caller may filter the list by specifying the 'dataKeyType'
      query parameter.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    apm_domain_id:
        description:
            - The OCID of the APM domain
        type: str
        required: true
    data_key_type:
        description:
            - Data key type.
        type: str
        choices:
            - "PRIVATE"
            - "PUBLIC"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List data_keys
  oci_apm_control_plane_data_keys_facts:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    data_key_type: PRIVATE

"""

RETURN = """
data_keys:
    description:
        - List of DataKeys resources
    returned: on success
    type: complex
    contains:
        value:
            description:
                - Value of the Data Key.
            returned: on success
            type: str
            sample: value_example
        name:
            description:
                - Name of the Data Key. The name uniquely identifies a Data Key within an APM domain.
            returned: on success
            type: str
            sample: name_example
        type:
            description:
                - Type of the Data Key.
            returned: on success
            type: str
            sample: PRIVATE
    sample: [{
        "value": "value_example",
        "name": "name_example",
        "type": "PRIVATE"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.apm_control_plane import ApmDomainClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataKeysFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "apm_domain_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "data_key_type",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_data_keys,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            **optional_kwargs
        )


DataKeysFactsHelperCustom = get_custom_class("DataKeysFactsHelperCustom")


class ResourceFactsHelper(DataKeysFactsHelperCustom, DataKeysFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            apm_domain_id=dict(type="str", required=True),
            data_key_type=dict(type="str", choices=["PRIVATE", "PUBLIC"]),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="data_keys",
        service_client_class=ApmDomainClient,
        namespace="apm_control_plane",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(data_keys=result)


if __name__ == "__main__":
    main()
