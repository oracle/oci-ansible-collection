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
module: oci_network_allowed_ike_ip_sec_parameters_facts
short_description: Fetches details about a AllowedIkeIpSecParameters resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AllowedIkeIpSecParameters resource in Oracle Cloud Infrastructure
    - The parameters allowed for IKE IPSec tunnels.
version_added: "2.9.0"
author: Oracle (@oracle)
options: {}
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific allowed_ike_ip_sec_parameters
  oci_network_allowed_ike_ip_sec_parameters_facts:

"""

RETURN = """
allowed_ike_ip_sec_parameters:
    description:
        - AllowedIkeIpSecParameters resource
    returned: on success
    type: complex
    contains:
        allowed_phase_one_parameters:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                encryption_algorithms:
                    description:
                        - Allowed phase one encryption algorithms.
                    returned: on success
                    type: list
                    sample: []
                authentication_algorithms:
                    description:
                        - Allowed phase one authentication algorithms.
                    returned: on success
                    type: list
                    sample: []
                dh_groups:
                    description:
                        - Allowed phase one Diffie-Hellman groups.
                    returned: on success
                    type: list
                    sample: []
        allowed_phase_two_parameters:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                encryption_algorithms:
                    description:
                        - Allowed phase two encryption algorithms.
                    returned: on success
                    type: list
                    sample: []
                authentication_algorithms:
                    description:
                        - Allowed phase two authentication algorithms.
                    returned: on success
                    type: list
                    sample: []
                pfs_dh_groups:
                    description:
                        - Allowed perfect forward secrecy Diffie-Hellman groups.
                    returned: on success
                    type: list
                    sample: []
        default_phase_one_parameters:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                default_encryption_algorithms:
                    description:
                        - Default phase one encryption algorithms.
                    returned: on success
                    type: list
                    sample: []
                default_authentication_algorithms:
                    description:
                        - Default phase one authentication algorithms.
                    returned: on success
                    type: list
                    sample: []
                default_dh_groups:
                    description:
                        - Default phase one Diffie-Hellman groups.
                    returned: on success
                    type: list
                    sample: []
        default_phase_two_parameters:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                default_encryption_algorithms:
                    description:
                        - Default phase two encryption algorithms.
                    returned: on success
                    type: list
                    sample: []
                default_authentication_algorithms:
                    description:
                        - Default phase two authentication algorithms.
                    returned: on success
                    type: list
                    sample: []
                default_pfs_dh_group:
                    description:
                        - Default perfect forward secrecy Diffie-Hellman groups.
                    returned: on success
                    type: str
                    sample: default_pfs_dh_group_example
    sample: {
        "allowed_phase_one_parameters": {
            "encryption_algorithms": [],
            "authentication_algorithms": [],
            "dh_groups": []
        },
        "allowed_phase_two_parameters": {
            "encryption_algorithms": [],
            "authentication_algorithms": [],
            "pfs_dh_groups": []
        },
        "default_phase_one_parameters": {
            "default_encryption_algorithms": [],
            "default_authentication_algorithms": [],
            "default_dh_groups": []
        },
        "default_phase_two_parameters": {
            "default_encryption_algorithms": [],
            "default_authentication_algorithms": [],
            "default_pfs_dh_group": "default_pfs_dh_group_example"
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AllowedIkeIpSecParametersFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_allowed_ike_ip_sec_parameters,
        )


AllowedIkeIpSecParametersFactsHelperCustom = get_custom_class(
    "AllowedIkeIpSecParametersFactsHelperCustom"
)


class ResourceFactsHelper(
    AllowedIkeIpSecParametersFactsHelperCustom, AllowedIkeIpSecParametersFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict())

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="allowed_ike_ip_sec_parameters",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(allowed_ike_ip_sec_parameters=result)


if __name__ == "__main__":
    main()
