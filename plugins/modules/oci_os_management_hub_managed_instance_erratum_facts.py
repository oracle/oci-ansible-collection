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
module: oci_os_management_hub_managed_instance_erratum_facts
short_description: Fetches details about one or multiple ManagedInstanceErratum resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagedInstanceErratum resources in Oracle Cloud Infrastructure
    - Returns a list of applicable errata on the managed instance.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance.
        type: str
        required: true
    classification_type:
        description:
            - A filter to return only packages that match the given update classification type.
        type: list
        elements: str
        choices:
            - "SECURITY"
            - "BUGFIX"
            - "ENHANCEMENT"
            - "OTHER"
    name:
        description:
            - The assigned erratum name. It's unique and not changeable.
            - "Example: `ELSA-2020-5804`"
        type: list
        elements: str
    name_contains:
        description:
            - A filter to return resources that may partially match the erratum name given.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort errata by. Only one sort order may be provided. Default order for timeIssued is descending. Default order for name is ascending.
              If no value is specified timeIssued is default.
        type: str
        choices:
            - "timeIssued"
            - "name"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List managed_instance_erratums
  oci_os_management_hub_managed_instance_erratum_facts:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    classification_type: [ "SECURITY" ]
    name: [ "name_example" ]
    name_contains: name_contains_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeIssued

"""

RETURN = """
managed_instance_erratums:
    description:
        - List of ManagedInstanceErratum resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The identifier of the erratum.
            returned: on success
            type: str
            sample: name_example
        advisory_type:
            description:
                - The advisory type of the erratum.
            returned: on success
            type: str
            sample: SECURITY
        time_issued:
            description:
                - The date and time the package was issued by a providing erratum (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        synopsis:
            description:
                - A summary description of the erratum.
            returned: on success
            type: str
            sample: synopsis_example
        related_cves:
            description:
                - The list of CVEs applicable to this erratum.
            returned: on success
            type: list
            sample: []
        packages:
            description:
                - The list of packages affected by this erratum.
            returned: on success
            type: complex
            contains:
                display_name:
                    description:
                        - Full package name in NERVA format. This value should be unique.
                    returned: on success
                    type: str
                    sample: display_name_example
                name:
                    description:
                        - The name of the software package.
                    returned: on success
                    type: str
                    sample: name_example
                type:
                    description:
                        - Type of the package.
                    returned: on success
                    type: str
                    sample: type_example
                version:
                    description:
                        - The version of the software package.
                    returned: on success
                    type: str
                    sample: version_example
                architecture:
                    description:
                        - The CPU architecture type for which this package was built.
                    returned: on success
                    type: str
                    sample: X86_64
    sample: [{
        "name": "name_example",
        "advisory_type": "SECURITY",
        "time_issued": "2013-10-20T19:20:30+01:00",
        "synopsis": "synopsis_example",
        "related_cves": [],
        "packages": [{
            "display_name": "display_name_example",
            "name": "name_example",
            "type": "type_example",
            "version": "version_example",
            "architecture": "X86_64"
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
    from oci.os_management_hub import ManagedInstanceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedInstanceErratumFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_instance_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "classification_type",
            "name",
            "name_contains",
            "compartment_id",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_managed_instance_errata,
            managed_instance_id=self.module.params.get("managed_instance_id"),
            **optional_kwargs
        )


ManagedInstanceErratumFactsHelperCustom = get_custom_class(
    "ManagedInstanceErratumFactsHelperCustom"
)


class ResourceFactsHelper(
    ManagedInstanceErratumFactsHelperCustom, ManagedInstanceErratumFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_instance_id=dict(type="str", required=True),
            classification_type=dict(
                type="list",
                elements="str",
                choices=["SECURITY", "BUGFIX", "ENHANCEMENT", "OTHER"],
            ),
            name=dict(type="list", elements="str"),
            name_contains=dict(type="str"),
            compartment_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeIssued", "name"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="managed_instance_erratum",
        service_client_class=ManagedInstanceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(managed_instance_erratums=result)


if __name__ == "__main__":
    main()
