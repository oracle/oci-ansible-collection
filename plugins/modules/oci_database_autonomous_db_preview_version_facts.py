#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_database_autonomous_db_preview_version_facts
short_description: Fetches details about one or multiple AutonomousDbPreviewVersion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AutonomousDbPreviewVersion resources in Oracle Cloud Infrastructure
    - Gets a list of supported Autonomous Database versions. Note that preview version software is only available for
      databases with L(shared Exadata infrastructure,https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for DBWORKLOAD is ascending.
            - "**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "DBWORKLOAD"
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
- name: List autonomous_db_preview_versions
  oci_database_autonomous_db_preview_version_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
autonomous_db_preview_versions:
    description:
        - List of AutonomousDbPreviewVersion resources
    returned: on success
    type: complex
    contains:
        version:
            description:
                - A valid Autonomous Database preview version.
            returned: on success
            type: str
            sample: version_example
        time_preview_begin:
            description:
                - The date and time when the preview version availability begins.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_preview_end:
            description:
                - The date and time when the preview version availability ends.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        db_workload:
            description:
                - "The Autonomous Database workload type. The following values are valid:"
                - "- OLTP - indicates an Autonomous Transaction Processing database
                  - DW - indicates an Autonomous Data Warehouse database
                  - AJD - indicates an Autonomous JSON Database
                  - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type."
            returned: on success
            type: str
            sample: OLTP
        details:
            description:
                - A URL that points to a detailed description of the preview version.
            returned: on success
            type: str
            sample: details_example
    sample: [{
        "version": "version_example",
        "time_preview_begin": "2013-10-20T19:20:30+01:00",
        "time_preview_end": "2013-10-20T19:20:30+01:00",
        "db_workload": "OLTP",
        "details": "details_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousDbPreviewVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_autonomous_db_preview_versions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AutonomousDbPreviewVersionFactsHelperCustom = get_custom_class(
    "AutonomousDbPreviewVersionFactsHelperCustom"
)


class ResourceFactsHelper(
    AutonomousDbPreviewVersionFactsHelperCustom,
    AutonomousDbPreviewVersionFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["DBWORKLOAD"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="autonomous_db_preview_version",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(autonomous_db_preview_versions=result)


if __name__ == "__main__":
    main()
