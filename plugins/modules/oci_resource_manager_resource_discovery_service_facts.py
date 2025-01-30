#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_resource_manager_resource_discovery_service_facts
short_description: Fetches details about one or multiple ResourceDiscoveryService resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ResourceDiscoveryService resources in Oracle Cloud Infrastructure
    - Returns a list of supported services for L(Resource Discovery,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resource-discovery.htm).
      For reference on service names, see the L(Terraform provider
      documentation,https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - A filter to return only resources that exist in the compartment, identified by
              L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List resource_discovery_services
  oci_resource_manager_resource_discovery_service_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
resource_discovery_services:
    description:
        - List of ResourceDiscoveryService resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - "A supported service. Example: `core`
                  For reference on service names, see the L(Terraform provider
                  documentation,https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services)."
            returned: on success
            type: str
            sample: name_example
        discovery_scope:
            description:
                - "The scope of the service as used with Resource Discovery.
                  This property determines the type of compartment OCID required: root compartment (`TENANCY`) or not (`COMPARTMENT`).
                  For example, `identity` is at the root compartment scope while `database` is at the compartment scope."
            returned: on success
            type: str
            sample: TENANCY
    sample: [{
        "name": "name_example",
        "discovery_scope": "TENANCY"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.resource_manager import ResourceManagerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResourceDiscoveryServiceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_resource_discovery_services, **optional_kwargs
        )


ResourceDiscoveryServiceFactsHelperCustom = get_custom_class(
    "ResourceDiscoveryServiceFactsHelperCustom"
)


class ResourceFactsHelper(
    ResourceDiscoveryServiceFactsHelperCustom, ResourceDiscoveryServiceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(compartment_id=dict(type="str"), name=dict(type="str"),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="resource_discovery_service",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(resource_discovery_services=result)


if __name__ == "__main__":
    main()
