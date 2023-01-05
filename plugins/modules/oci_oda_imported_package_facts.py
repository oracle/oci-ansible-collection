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
module: oci_oda_imported_package_facts
short_description: Fetches details about one or multiple ImportedPackage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ImportedPackage resources in Oracle Cloud Infrastructure
    - Returns a list of summaries for imported packages in the instance.
    - If I(package_id) is specified, the details of a single ImportedPackage will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    package_id:
        description:
            - Unique Digital Assistant package identifier.
            - Required to get a specific imported_package.
        type: str
        aliases: ["id"]
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
        type: str
        required: true
    name:
        description:
            - List only the information for the package with this name. Package names are unique to a publisher and may not change.
            - "Example: `My Package`"
        type: str
    sort_order:
        description:
            - Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`.
            - The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific imported_package
  oci_oda_imported_package_facts:
    # required
    package_id: "ocid1.package.oc1..xxxxxxEXAMPLExxxxxx"
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List imported_packages
  oci_oda_imported_package_facts:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
imported_packages:
    description:
        - List of ImportedPackage resources
    returned: on success
    type: complex
    contains:
        status_message:
            description:
                - Short message explaining the status of this imported package.
                - Returned for get operation
            returned: on success
            type: str
            sample: status_message_example
        parameter_values:
            description:
                - A list of parameter values used to import the package.
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        oda_instance_id:
            description:
                - ID of the host instance.
            returned: on success
            type: str
            sample: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
        current_package_id:
            description:
                - ID of the package.
            returned: on success
            type: str
            sample: "ocid1.currentpackage.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Stable name of the package (the same across versions).
            returned: on success
            type: str
            sample: name_example
        display_name:
            description:
                - Display name of the package (can change across versions).
            returned: on success
            type: str
            sample: display_name_example
        version:
            description:
                - version of the package.
            returned: on success
            type: str
            sample: version_example
        status:
            description:
                - Status of the imported package.
            returned: on success
            type: str
            sample: READY
        time_created:
            description:
                - When the imported package was created. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - When the imported package was last updated. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type, or scope.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "status_message": "status_message_example",
        "parameter_values": {},
        "oda_instance_id": "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx",
        "current_package_id": "ocid1.currentpackage.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "display_name": "display_name_example",
        "version": "version_example",
        "status": "READY",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.oda import OdapackageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ImportedPackageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "oda_instance_id",
            "package_id",
        ]

    def get_required_params_for_list(self):
        return [
            "oda_instance_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_imported_package,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            package_id=self.module.params.get("package_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_order",
            "sort_by",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_imported_packages,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            **optional_kwargs
        )


ImportedPackageFactsHelperCustom = get_custom_class("ImportedPackageFactsHelperCustom")


class ResourceFactsHelper(
    ImportedPackageFactsHelperCustom, ImportedPackageFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            package_id=dict(aliases=["id"], type="str"),
            oda_instance_id=dict(type="str", required=True),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="imported_package",
        service_client_class=OdapackageClient,
        namespace="oda",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(imported_packages=result)


if __name__ == "__main__":
    main()
