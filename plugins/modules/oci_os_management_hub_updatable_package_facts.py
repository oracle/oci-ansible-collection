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
module: oci_os_management_hub_updatable_package_facts
short_description: Fetches details about one or multiple UpdatablePackage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple UpdatablePackage resources in Oracle Cloud Infrastructure
    - Returns a list of updatable packages for a managed instance.
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
    display_name:
        description:
            - A filter to return resources that match the given display names.
        type: list
        elements: str
    display_name_contains:
        description:
            - A filter to return resources that may partially match the given display name.
        type: str
    advisory_name:
        description:
            - The assigned erratum name. It's unique and not changeable.
            - "Example: `ELSA-2020-5804`"
        type: list
        elements: str
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
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List updatable_packages
  oci_os_management_hub_updatable_package_facts:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    classification_type: [ "SECURITY" ]
    display_name: [ "display_name_example" ]
    display_name_contains: display_name_contains_example
    advisory_name: [ "advisory_name_example" ]
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
updatable_packages:
    description:
        - List of UpdatablePackage resources
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - Package name.
            returned: on success
            type: str
            sample: display_name_example
        name:
            description:
                - Unique identifier for the package.
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
                - Version of the installed package.
            returned: on success
            type: str
            sample: version_example
        architecture:
            description:
                - The architecture for which this package was built.
            returned: on success
            type: str
            sample: X86_64
        software_sources:
            description:
                - List of software sources that provide the software package.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Software source name.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Software source description.
                    returned: on success
                    type: str
                    sample: description_example
                software_source_type:
                    description:
                        - Type of the software source.
                    returned: on success
                    type: str
                    sample: VENDOR
                is_mandatory_for_autonomous_linux:
                    description:
                        - Indicates whether this is a required software source for Autonomous Linux instances. If true, the user can't unselect it.
                    returned: on success
                    type: bool
                    sample: true
        package_classification:
            description:
                - Status of the software package.
            returned: on success
            type: str
            sample: INSTALLED
        installed_version:
            description:
                - The version of the package that is currently installed on the instance.
            returned: on success
            type: str
            sample: installed_version_example
        update_type:
            description:
                - The type of update.
            returned: on success
            type: str
            sample: SECURITY
        errata:
            description:
                - List of errata applicable to this update.
            returned: on success
            type: list
            sample: []
        related_cves:
            description:
                - List of CVEs applicable to this erratum.
            returned: on success
            type: list
            sample: []
    sample: [{
        "display_name": "display_name_example",
        "name": "name_example",
        "type": "type_example",
        "version": "version_example",
        "architecture": "X86_64",
        "software_sources": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "software_source_type": "VENDOR",
            "is_mandatory_for_autonomous_linux": true
        }],
        "package_classification": "INSTALLED",
        "installed_version": "installed_version_example",
        "update_type": "SECURITY",
        "errata": [],
        "related_cves": []
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


class OsManagementHubUpdatablePackageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_instance_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "classification_type",
            "display_name",
            "display_name_contains",
            "advisory_name",
            "compartment_id",
            "sort_order",
            "sort_by",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_managed_instance_updatable_packages,
            managed_instance_id=self.module.params.get("managed_instance_id"),
            **optional_kwargs
        )


OsManagementHubUpdatablePackageFactsHelperCustom = get_custom_class(
    "OsManagementHubUpdatablePackageFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubUpdatablePackageFactsHelperCustom,
    OsManagementHubUpdatablePackageFactsHelperGen,
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
            display_name=dict(type="list", elements="str"),
            display_name_contains=dict(type="str"),
            advisory_name=dict(type="list", elements="str"),
            compartment_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="updatable_package",
        service_client_class=ManagedInstanceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(updatable_packages=result)


if __name__ == "__main__":
    main()
