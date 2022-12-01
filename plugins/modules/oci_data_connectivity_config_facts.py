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
module: oci_data_connectivity_config_facts
short_description: Fetches details about a Config resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Config resource in Oracle Cloud Infrastructure
    - This endpoint is used to fetch connector-specific engine configurations.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    registry_id:
        description:
            - The registry OCID.
        type: str
        required: true
    connection_key:
        description:
            - The connection key.
        type: str
        required: true
    engine_type_query_param:
        description:
            - Specifies the runtime engine for the bulk read/write operation. Default is SPARK.
        type: str
        choices:
            - "SPARK"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific config
  oci_data_connectivity_config_facts:
    # required
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    connection_key: connection_key_example

    # optional
    engine_type_query_param: SPARK

"""

RETURN = """
config:
    description:
        - Config resource
    returned: on success
    type: complex
    contains:
        config_map:
            description:
                - "The connector-specific engine configurations configuration represented in a key-value map. Example - \\"spark.sql.catalogImplementation\\",
                  \\"hive\\""
            returned: on success
            type: dict
            sample: {}
    sample: {
        "config_map": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_connectivity import DataConnectivityManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConfigFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "registry_id",
            "connection_key",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "engine_type_query_param",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_engine_configurations,
            registry_id=self.module.params.get("registry_id"),
            connection_key=self.module.params.get("connection_key"),
            **optional_kwargs
        )


ConfigFactsHelperCustom = get_custom_class("ConfigFactsHelperCustom")


class ResourceFactsHelper(ConfigFactsHelperCustom, ConfigFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            registry_id=dict(type="str", required=True),
            connection_key=dict(type="str", required=True, no_log=True),
            engine_type_query_param=dict(type="str", choices=["SPARK"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="config",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(config=result)


if __name__ == "__main__":
    main()
