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
module: oci_os_management_erratum_facts
short_description: Fetches details about a Erratum resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Erratum resource in Oracle Cloud Infrastructure
    - Returns a specific erratum.
version_added: "2.9"
author: Oracle (@oracle)
options:
    erratum_id:
        description:
            - The OCID of the erratum.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: Get a specific erratum
  oci_os_management_erratum_facts:
    erratum_id: "ocid1.erratum.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
erratum:
    description:
        - Erratum resource
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Advisory name
            returned: on success
            type: string
            sample: name_example
        id:
            description:
                - OCID for the Erratum.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - OCID for the Compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        synopsis:
            description:
                - Summary description of the erratum.
            returned: on success
            type: string
            sample: synopsis_example
        issued:
            description:
                - date the erratum was issued
            returned: on success
            type: string
            sample: issued_example
        description:
            description:
                - Details describing the erratum.
            returned: on success
            type: string
            sample: description_example
        updated:
            description:
                - most recent date the erratum was updated
            returned: on success
            type: string
            sample: updated_example
        advisory_type:
            description:
                - Type of the erratum.
            returned: on success
            type: string
            sample: SECURITY
        _from:
            description:
                - Information specifying from where the erratum was release.
            returned: on success
            type: string
            sample: _from_example
        solution:
            description:
                - Information describing how the erratum can be resolved.
            returned: on success
            type: string
            sample: solution_example
        references:
            description:
                - Information describing how to find more information about the erratum.
            returned: on success
            type: string
            sample: references_example
        affected_instances:
            description:
                - list of managed instances  to this erratum
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - unique identifier that is immutable on creation
                    returned: on success
                    type: string
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User friendly name
                    returned: on success
                    type: string
                    sample: display_name_example
        related_cves:
            description:
                - list of CVEs applicable to this erratum
            returned: on success
            type: list
            sample: []
        software_sources:
            description:
                - list of Software Sources
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - unique identifier that is immutable on creation
                    returned: on success
                    type: string
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User friendly name
                    returned: on success
                    type: string
                    sample: display_name_example
        packages:
            description:
                - list of Packages affected by this erratum
            returned: on success
            type: complex
            contains:
                display_name:
                    description:
                        - Package name
                    returned: on success
                    type: string
                    sample: display_name_example
                name:
                    description:
                        - "Unique identifier for the package. NOTE - This is not an OCID"
                    returned: on success
                    type: string
                    sample: name_example
                type:
                    description:
                        - Type of the package
                    returned: on success
                    type: string
                    sample: type_example
                version:
                    description:
                        - Version of the package
                    returned: on success
                    type: string
                    sample: version_example
                architecture:
                    description:
                        - the architecture for which this software was built
                    returned: on success
                    type: string
                    sample: architecture_example
                checksum:
                    description:
                        - checksum of the package
                    returned: on success
                    type: string
                    sample: checksum_example
                checksum_type:
                    description:
                        - type of the checksum
                    returned: on success
                    type: string
                    sample: checksum_type_example
    sample: {
        "name": "name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "synopsis": "synopsis_example",
        "issued": "issued_example",
        "description": "description_example",
        "updated": "updated_example",
        "advisory_type": "SECURITY",
        "_from": "_from_example",
        "solution": "solution_example",
        "references": "references_example",
        "affected_instances": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "related_cves": [],
        "software_sources": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "packages": [{
            "display_name": "display_name_example",
            "name": "name_example",
            "type": "type_example",
            "version": "version_example",
            "architecture": "architecture_example",
            "checksum": "checksum_example",
            "checksum_type": "checksum_type_example"
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.os_management import OsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ErratumFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "erratum_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_erratum, erratum_id=self.module.params.get("erratum_id"),
        )


ErratumFactsHelperCustom = get_custom_class("ErratumFactsHelperCustom")


class ResourceFactsHelper(ErratumFactsHelperCustom, ErratumFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            erratum_id=dict(aliases=["id"], type="str", required=True),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="erratum",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(erratum=result)


if __name__ == "__main__":
    main()
