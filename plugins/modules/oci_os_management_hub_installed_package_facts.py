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
module: oci_os_management_hub_installed_package_facts
short_description: Fetches details about one or multiple InstalledPackage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple InstalledPackage resources in Oracle Cloud Infrastructure
    - Lists installed packages on managed instances in a specified lifecycle stage. Filter the list against a variety
      of criteria including but not limited to the package name.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    lifecycle_stage_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the lifecycle stage.
        type: str
        required: true
    compartment_id:
        description:
            - The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
        type: str
    display_name:
        description:
            - A filter to return resources that match the given display names.
        type: list
        elements: str
    display_name_contains:
        description:
            - A filter to return resources that may partially match the given display name.
        type: str
    lifecycle_state:
        description:
            - A filter to return only lifecycle stages whose lifecycle state matches the given lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided.
              Default order for timeCreated is descending. Default order for displayName is ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List installed_packages
  oci_os_management_hub_installed_package_facts:
    # required
    lifecycle_stage_id: "ocid1.lifecyclestage.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: [ "display_name_example" ]
    display_name_contains: display_name_contains_example
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
installed_packages:
    description:
        - List of InstalledPackage resources
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
        time_installed:
            description:
                - The date and time the package was installed, as described in
                  L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_issued:
            description:
                - The date and time the package was issued by a providing erratum (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        "time_installed": "2013-10-20T19:20:30+01:00",
        "time_issued": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import LifecycleEnvironmentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubInstalledPackageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "lifecycle_stage_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "display_name_contains",
            "lifecycle_state",
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
            self.client.list_lifecycle_stage_installed_packages,
            lifecycle_stage_id=self.module.params.get("lifecycle_stage_id"),
            **optional_kwargs
        )


OsManagementHubInstalledPackageFactsHelperCustom = get_custom_class(
    "OsManagementHubInstalledPackageFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubInstalledPackageFactsHelperCustom,
    OsManagementHubInstalledPackageFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            lifecycle_stage_id=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            display_name=dict(type="list", elements="str"),
            display_name_contains=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
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
        resource_type="installed_package",
        service_client_class=LifecycleEnvironmentClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(installed_packages=result)


if __name__ == "__main__":
    main()
