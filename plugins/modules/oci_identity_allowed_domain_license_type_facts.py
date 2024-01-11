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
module: oci_identity_allowed_domain_license_type_facts
short_description: Fetches details about one or multiple AllowedDomainLicenseType resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AllowedDomainLicenseType resources in Oracle Cloud Infrastructure
    - (For tenancies that support identity domains) Lists the license types for identity domains supported by Oracle Cloud Infrastructure.
      (License types are also referred to as domain types.)
    - If `currentLicenseTypeName` is provided, then the request returns license types that the identity domain with the specified license
      type name can change to. Otherwise, the request returns all valid license types currently supported.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    current_license_type_name:
        description:
            - The license type of the identity domain.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List allowed_domain_license_types
  oci_identity_allowed_domain_license_type_facts:

    # optional
    current_license_type_name: current_license_type_name_example

"""

RETURN = """
allowed_domain_license_types:
    description:
        - List of AllowedDomainLicenseType resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The license type name.
                - "Example: \\"Oracle Apps Premium\\""
            returned: on success
            type: str
            sample: name_example
        license_type:
            description:
                - The license type identifier.
                - "Example: \\"oracle-apps-premium\\""
            returned: on success
            type: str
            sample: license_type_example
        description:
            description:
                - The license type description.
            returned: on success
            type: str
            sample: description_example
    sample: [{
        "name": "name_example",
        "license_type": "license_type_example",
        "description": "description_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AllowedDomainLicenseTypeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "current_license_type_name",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_allowed_domain_license_types, **optional_kwargs
        )


AllowedDomainLicenseTypeFactsHelperCustom = get_custom_class(
    "AllowedDomainLicenseTypeFactsHelperCustom"
)


class ResourceFactsHelper(
    AllowedDomainLicenseTypeFactsHelperCustom, AllowedDomainLicenseTypeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(current_license_type_name=dict(type="str"), name=dict(type="str"),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="allowed_domain_license_type",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(allowed_domain_license_types=result)


if __name__ == "__main__":
    main()
