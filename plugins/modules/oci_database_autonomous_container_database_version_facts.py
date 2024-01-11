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
module: oci_database_autonomous_container_database_version_facts
short_description: Fetches details about one or multiple AutonomousContainerDatabaseVersion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AutonomousContainerDatabaseVersion resources in Oracle Cloud Infrastructure
    - Gets a list of supported Autonomous Container Database versions.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    service_component:
        description:
            - The service component to use, either ADBD or EXACC.
        type: str
        choices:
            - "ADBD"
            - "EXACC"
        required: true
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List autonomous_container_database_versions
  oci_database_autonomous_container_database_version_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    service_component: ADBD

    # optional
    sort_order: ASC

"""

RETURN = """
autonomous_container_database_versions:
    description:
        - List of AutonomousContainerDatabaseVersion resources
    returned: on success
    type: complex
    contains:
        version:
            description:
                - A valid Oracle Database version for provisioning an Autonomous Container Database.
            returned: on success
            type: str
            sample: version_example
        details:
            description:
                - A URL that points to a detailed description of the Autonomous Container Database version.
            returned: on success
            type: str
            sample: details_example
        supported_apps:
            description:
                - The list of applications supported for the given version.
            returned: on success
            type: complex
            contains:
                release_date:
                    description:
                        - The Autonomous Container Database version release date.
                    returned: on success
                    type: str
                    sample: release_date_example
                end_of_support:
                    description:
                        - The Autonomous Container Database version end of support date.
                    returned: on success
                    type: str
                    sample: end_of_support_example
                supported_app_name:
                    description:
                        - The name of the supported application.
                    returned: on success
                    type: str
                    sample: supported_app_name_example
                is_certified:
                    description:
                        - Indicates if the image is certified.
                    returned: on success
                    type: bool
                    sample: true
    sample: [{
        "version": "version_example",
        "details": "details_example",
        "supported_apps": [{
            "release_date": "release_date_example",
            "end_of_support": "end_of_support_example",
            "supported_app_name": "supported_app_name_example",
            "is_certified": true
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
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousContainerDatabaseVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "service_component",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_autonomous_container_database_versions,
            compartment_id=self.module.params.get("compartment_id"),
            service_component=self.module.params.get("service_component"),
            **optional_kwargs
        )


AutonomousContainerDatabaseVersionFactsHelperCustom = get_custom_class(
    "AutonomousContainerDatabaseVersionFactsHelperCustom"
)


class ResourceFactsHelper(
    AutonomousContainerDatabaseVersionFactsHelperCustom,
    AutonomousContainerDatabaseVersionFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            service_component=dict(
                type="str", required=True, choices=["ADBD", "EXACC"]
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="autonomous_container_database_version",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(autonomous_container_database_versions=result)


if __name__ == "__main__":
    main()
