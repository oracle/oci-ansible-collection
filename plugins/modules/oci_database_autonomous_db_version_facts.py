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
module: oci_database_autonomous_db_version_facts
short_description: Fetches details about one or multiple AutonomousDbVersion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AutonomousDbVersion resources in Oracle Cloud Infrastructure
    - Gets a list of supported Autonomous Database versions.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    db_workload:
        description:
            - A filter to return only autonomous database resources that match the specified workload type.
        type: str
        choices:
            - "OLTP"
            - "DW"
            - "AJD"
            - "APEX"
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
- name: List autonomous_db_versions
  oci_database_autonomous_db_version_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    db_workload: OLTP
    sort_order: ASC

"""

RETURN = """
autonomous_db_versions:
    description:
        - List of AutonomousDbVersion resources
    returned: on success
    type: complex
    contains:
        version:
            description:
                - A valid Oracle Database version for Autonomous Database.
            returned: on success
            type: str
            sample: version_example
        db_workload:
            description:
                - "The Autonomous Database workload type. The following values are valid:"
                - "- OLTP - indicates an Autonomous Transaction Processing database
                  - DW - indicates an Autonomous Data Warehouse database
                  - AJD - indicates an Autonomous JSON Database
                  - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type."
                - "This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel,
                  adminPassword, whitelistedIps, isMTLSConnectionRequired, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations,
                  dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier."
            returned: on success
            type: str
            sample: OLTP
        is_dedicated:
            description:
                - True if the database uses L(dedicated Exadata infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html).
            returned: on success
            type: bool
            sample: true
        details:
            description:
                - A URL that points to a detailed description of the Autonomous Database version.
            returned: on success
            type: str
            sample: details_example
        is_free_tier_enabled:
            description:
                - True if this version of the Oracle Database software can be used for Always-Free Autonomous Databases.
            returned: on success
            type: bool
            sample: true
        is_paid_enabled:
            description:
                - True if this version of the Oracle Database software has payments enabled.
            returned: on success
            type: bool
            sample: true
        is_default_for_free:
            description:
                - True if this version of the Oracle Database software's default is free.
            returned: on success
            type: bool
            sample: true
        is_default_for_paid:
            description:
                - True if this version of the Oracle Database software's default is paid.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "version": "version_example",
        "db_workload": "OLTP",
        "is_dedicated": true,
        "details": "details_example",
        "is_free_tier_enabled": true,
        "is_paid_enabled": true,
        "is_default_for_free": true,
        "is_default_for_paid": true
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


class AutonomousDbVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "db_workload",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_autonomous_db_versions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AutonomousDbVersionFactsHelperCustom = get_custom_class(
    "AutonomousDbVersionFactsHelperCustom"
)


class ResourceFactsHelper(
    AutonomousDbVersionFactsHelperCustom, AutonomousDbVersionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            db_workload=dict(type="str", choices=["OLTP", "DW", "AJD", "APEX"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="autonomous_db_version",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(autonomous_db_versions=result)


if __name__ == "__main__":
    main()
