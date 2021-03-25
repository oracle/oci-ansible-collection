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
module: oci_database_db_version_facts
short_description: Fetches details about one or multiple DbVersion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DbVersion resources in Oracle Cloud Infrastructure
    - Gets a list of supported Oracle Database versions.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    db_system_shape:
        description:
            - If provided, filters the results to the set of database versions which are supported for the given shape.
        type: str
    db_system_id:
        description:
            - The DB system L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm). If provided, filters the results to the set of
              database versions which are supported for the DB system.
        type: str
    storage_management:
        description:
            - "The DB system storage management option. Used to list database versions available for that storage manager. Valid values are:
              * ASM - Automatic storage management
              * LVM - Logical volume management"
        type: str
        choices:
            - "ASM"
            - "LVM"
    is_upgrade_supported:
        description:
            - If provided, filters the results to the set of database versions which are supported for Upgrade.
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List db_versions
  oci_database_db_version_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
db_versions:
    description:
        - List of DbVersion resources
    returned: on success
    type: complex
    contains:
        version:
            description:
                - A valid Oracle Database version.
            returned: on success
            type: string
            sample: version_example
        is_latest_for_major_version:
            description:
                - True if this version of the Oracle Database software is the latest version for a release.
            returned: on success
            type: bool
            sample: true
        supports_pdb:
            description:
                - True if this version of the Oracle Database software supports pluggable databases.
            returned: on success
            type: bool
            sample: true
        is_preview_db_version:
            description:
                - True if this version of the Oracle Database software is the preview version.
            returned: on success
            type: bool
            sample: true
        is_upgrade_supported:
            description:
                - True if this version of the Oracle Database software is supported for Upgrade.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "version": "version_example",
        "is_latest_for_major_version": true,
        "supports_pdb": true,
        "is_preview_db_version": true,
        "is_upgrade_supported": true
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


class DbVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "db_system_shape",
            "db_system_id",
            "storage_management",
            "is_upgrade_supported",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_db_versions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DbVersionFactsHelperCustom = get_custom_class("DbVersionFactsHelperCustom")


class ResourceFactsHelper(DbVersionFactsHelperCustom, DbVersionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            db_system_shape=dict(type="str"),
            db_system_id=dict(type="str"),
            storage_management=dict(type="str", choices=["ASM", "LVM"]),
            is_upgrade_supported=dict(type="bool"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="db_version",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(db_versions=result)


if __name__ == "__main__":
    main()
