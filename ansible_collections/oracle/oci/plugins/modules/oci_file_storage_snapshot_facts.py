#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_file_storage_snapshot_facts
short_description: Fetches details about one or multiple Snapshot resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Snapshot resources in Oracle Cloud Infrastructure
    - Lists snapshots of the specified file system.
    - If I(snapshot_id) is specified, the details of a single Snapshot will be returned.
version_added: "2.5"
options:
    snapshot_id:
        description:
            - The OCID of the snapshot.
            - Required to get a specific snapshot.
        type: str
        aliases: ["id"]
    file_system_id:
        description:
            - The OCID of the file system.
            - Required to list multiple snapshots.
        type: str
    lifecycle_state:
        description:
            - Filter results by the specified lifecycle state. Must be a valid
              state for the resource type.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    id:
        description:
            - Filter results by OCID. Must be an OCID of the correct type for
              the resouce type.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc', where 'asc' is
              ascending and 'desc' is descending. The default order is 'desc'
              except for numeric values.
        type: str
        choices:
            - "ASC"
            - "DESC"
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List snapshots
  oci_file_storage_snapshot_facts:
    file_system_id: ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific snapshot
  oci_file_storage_snapshot_facts:
    snapshot_id: ocid1.snapshot.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
snapshots:
    description:
        - List of Snapshot resources
    returned: on success
    type: complex
    contains:
        file_system_id:
            description:
                - The OCID of the file system from which the snapshot
                  was created.
            returned: on success
            type: string
            sample: ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx
        id:
            description:
                - The OCID of the snapshot.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of the snapshot.
            returned: on success
            type: string
            sample: CREATING
        name:
            description:
                - Name of the snapshot. This value is immutable.
                - Avoid entering confidential information.
                - "Example: `Sunday`"
            returned: on success
            type: string
            sample: Sunday
        time_created:
            description:
                - The date and time the snapshot was created, expressed
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair
                   with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "file_system_id": "ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "name": "Sunday",
        "time_created": "2016-08-25T21:10:29.600Z",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.file_storage import FileStorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SnapshotFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "snapshot_id",
        ]

    def get_required_params_for_list(self):
        return [
            "file_system_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_snapshot, snapshot_id=self.module.params.get("snapshot_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "id",
            "sort_order",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_snapshots,
            file_system_id=self.module.params.get("file_system_id"),
            **optional_kwargs
        )


SnapshotFactsHelperCustom = get_custom_class("SnapshotFactsHelperCustom")


class ResourceFactsHelper(SnapshotFactsHelperCustom, SnapshotFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            snapshot_id=dict(aliases=["id"], type="str"),
            file_system_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"],
            ),
            id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="snapshot",
        service_client_class=FileStorageClient,
        namespace="file_storage",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(snapshots=result)


if __name__ == "__main__":
    main()
