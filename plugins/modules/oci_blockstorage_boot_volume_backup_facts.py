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
module: oci_blockstorage_boot_volume_backup_facts
short_description: Fetches details about one or multiple BootVolumeBackup resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BootVolumeBackup resources in Oracle Cloud Infrastructure
    - Lists the boot volume backups in the specified compartment. You can filter the results by boot volume.
    - If I(boot_volume_backup_id) is specified, the details of a single BootVolumeBackup will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    boot_volume_backup_id:
        description:
            - The OCID of the boot volume backup.
            - Required to get a specific boot_volume_backup.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple boot_volume_backups.
        type: str
    boot_volume_id:
        description:
            - The OCID of the boot volume.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    source_boot_volume_backup_id:
        description:
            - A filter to return only resources that originated from the given source boot volume backup.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state. The state value is
              case-insensitive.
        type: str
        choices:
            - "CREATING"
            - "AVAILABLE"
            - "TERMINATING"
            - "TERMINATED"
            - "FAULTY"
            - "REQUEST_RECEIVED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List boot_volume_backups
  oci_blockstorage_boot_volume_backup_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific boot_volume_backup
  oci_blockstorage_boot_volume_backup_facts:
    boot_volume_backup_id: ocid1.bootvolumebackup.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
boot_volume_backups:
    description:
        - List of BootVolumeBackup resources
    returned: on success
    type: complex
    contains:
        boot_volume_id:
            description:
                - The OCID of the boot volume.
            returned: on success
            type: string
            sample: ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment that contains the boot volume backup.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {}
        display_name:
            description:
                - A user-friendly name for the boot volume backup. Does not have to be unique and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        expiration_time:
            description:
                - The date and time the volume backup will expire and be automatically deleted.
                  Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339). This parameter will always be present for backups that
                  were created automatically by a scheduled-backup policy. For manually created backups,
                  it will be absent, signifying that there is no expiration time and the backup will
                  last forever until manually deleted.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of the boot volume backup.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        image_id:
            description:
                - The image OCID used to create the boot volume the backup is taken from.
            returned: on success
            type: string
            sample: ocid1.image.oc1..xxxxxxEXAMPLExxxxxx
        kms_key_id:
            description:
                - The OCID of the Key Management master encryption assigned to the boot volume backup.
                  For more information about the Key Management service and encryption keys, see
                  L(Overview of Key Management,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm) and
                  L(Using Keys,https://docs.cloud.oracle.com/Content/KeyManagement/Tasks/usingkeys.htm).
            returned: on success
            type: string
            sample: ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of a boot volume backup.
            returned: on success
            type: string
            sample: CREATING
        size_in_gbs:
            description:
                - The size of the boot volume, in GBs.
            returned: on success
            type: int
            sample: 56
        source_boot_volume_backup_id:
            description:
                - The OCID of the source boot volume backup.
            returned: on success
            type: string
            sample: ocid1.sourcebootvolumebackup.oc1..xxxxxxEXAMPLExxxxxx
        source_type:
            description:
                - Specifies whether the backup was created manually, or via scheduled backup policy.
            returned: on success
            type: string
            sample: MANUAL
        time_created:
            description:
                - The date and time the boot volume backup was created. This is the time the actual point-in-time image
                  of the volume data was taken. Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_request_received:
            description:
                - The date and time the request to create the boot volume backup was received. Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        type:
            description:
                - The type of a volume backup.
            returned: on success
            type: string
            sample: FULL
        unique_size_in_gbs:
            description:
                - The size used by the backup, in GBs. It is typically smaller than sizeInGBs, depending on the space
                  consumed on the boot volume and whether the backup is full or incremental.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "boot_volume_id": "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "display_name": "display_name_example",
        "expiration_time": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "size_in_gbs": 56,
        "source_boot_volume_backup_id": "ocid1.sourcebootvolumebackup.oc1..xxxxxxEXAMPLExxxxxx",
        "source_type": "MANUAL",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_request_received": "2013-10-20T19:20:30+01:00",
        "type": "FULL",
        "unique_size_in_gbs": 56
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import BlockstorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BootVolumeBackupFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "boot_volume_backup_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_boot_volume_backup,
            boot_volume_backup_id=self.module.params.get("boot_volume_backup_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "boot_volume_id",
            "display_name",
            "source_boot_volume_backup_id",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_boot_volume_backups,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


BootVolumeBackupFactsHelperCustom = get_custom_class(
    "BootVolumeBackupFactsHelperCustom"
)


class ResourceFactsHelper(
    BootVolumeBackupFactsHelperCustom, BootVolumeBackupFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            boot_volume_backup_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            boot_volume_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            source_boot_volume_backup_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "AVAILABLE",
                    "TERMINATING",
                    "TERMINATED",
                    "FAULTY",
                    "REQUEST_RECEIVED",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="boot_volume_backup",
        service_client_class=BlockstorageClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(boot_volume_backups=result)


if __name__ == "__main__":
    main()
