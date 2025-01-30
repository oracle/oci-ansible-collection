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
module: oci_mysql_version_facts
short_description: Fetches details about one or multiple Version resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Version resources in Oracle Cloud Infrastructure
    - Get a list of supported and available MySQL database major versions.
    - The list is sorted by version family.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List versions
  oci_mysql_version_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
versions:
    description:
        - List of Version resources
    returned: on success
    type: complex
    contains:
        version_family:
            description:
                - A descriptive summary of a group of versions.
            returned: on success
            type: str
            sample: version_family_example
        versions:
            description:
                - The list of supported MySQL Versions.
            returned: on success
            type: complex
            contains:
                version:
                    description:
                        - The specific version identifier
                    returned: on success
                    type: str
                    sample: version_example
                description:
                    description:
                        - A link to a page describing the version.
                    returned: on success
                    type: str
                    sample: description_example
    sample: [{
        "version_family": "version_family_example",
        "versions": [{
            "version": "version_example",
            "description": "description_example"
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.mysql import MysqlaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_versions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


MysqlVersionFactsHelperCustom = get_custom_class("MysqlVersionFactsHelperCustom")


class ResourceFactsHelper(MysqlVersionFactsHelperCustom, MysqlVersionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(compartment_id=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="version",
        service_client_class=MysqlaasClient,
        namespace="mysql",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(versions=result)


if __name__ == "__main__":
    main()
