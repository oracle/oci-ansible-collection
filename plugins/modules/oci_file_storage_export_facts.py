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
module: oci_file_storage_export_facts
short_description: Fetches details about one or multiple Export resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Export resources in Oracle Cloud Infrastructure
    - Lists export resources by compartment, file system, or export
      set. You must specify an export set ID, a file system ID, and
      / or a compartment ID.
    - If I(export_id) is specified, the details of a single Export will be returned.
version_added: "2.5"
options:
    export_id:
        description:
            - The OCID of the export.
            - Required to get a specific export.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
        type: str
    export_set_id:
        description:
            - The OCID of the export set.
        type: str
    file_system_id:
        description:
            - The OCID of the file system.
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
    sort_by:
        description:
            - The field to sort by. You can provide either value, but not both.
              By default, when you sort by time created, results are shown
              in descending order. When you sort by path, results are
              shown in ascending alphanumeric order.
        type: str
        choices:
            - "TIMECREATED"
            - "PATH"
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List exports
  oci_file_storage_export_facts:
    export_set_id: ocid1.exportset.oc1.phx.exampleaaaaacvbobuhqllhmfwwcotqnb4c2ylefuzaaaaa

- name: Get a specific export
  oci_file_storage_export_facts:
    export_id: ocid1.export.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
exports:
    description:
        - List of Export resources
    returned: on success
    type: complex
    contains:
        export_options:
            description:
                - Policies that apply to NFS requests made through this
                  export. `exportOptions` contains a sequential list of
                  `ClientOptions`. Each `ClientOptions` item defines the
                  export options that are applied to a specified
                  set of clients.
                - For each NFS request, the first `ClientOptions` option
                  in the list whose `source` attribute matches the source
                  IP address of the request is applied.
                - If a client source IP address does not match the `source`
                  property of any `ClientOptions` in the list, then the
                  export will be invisible to that client. This export will
                  not be returned by `MOUNTPROC_EXPORT` calls made by the client
                  and any attempt to mount or access the file system through
                  this export will result in an error.
                - "**Exports without defined `ClientOptions` are invisible to all clients.**"
                - If one export is invisible to a particular client, associated file
                  systems may still be accessible through other exports on the same
                  or different mount targets.
                  To completely deny client access to a file system, be sure that the client
                  source IP address is not included in any export for any mount target
                  associated with the file system.
            returned: on success
            type: complex
            contains:
                source:
                    description:
                        - Clients these options should apply to. Must be a either
                          single IPv4 address or single IPv4 CIDR block.
                        - "**Note:** Access will also be limited by any applicable VCN
                          security rules and the ability to route IP packets to the
                          mount target. Mount targets do not have Internet-routable IP addresses."
                    returned: on success
                    type: string
                    sample: source_example
                require_privileged_source_port:
                    description:
                        - If `true`, clients accessing the file system through this
                          export must connect from a privileged source port. If
                          unspecified, defaults to `true`.
                    returned: on success
                    type: bool
                    sample: true
                access:
                    description:
                        - Type of access to grant clients using the file system
                          through this export. If unspecified defaults to `READ_ONLY`.
                    returned: on success
                    type: string
                    sample: READ_WRITE
                identity_squash:
                    description:
                        - Used when clients accessing the file system through this export
                          have their UID and GID remapped to 'anonymousUid' and
                          'anonymousGid'. If `ALL`, all users and groups are remapped;
                          if `ROOT`, only the root user and group (UID/GID 0) are
                          remapped; if `NONE`, no remapping is done. If unspecified,
                          defaults to `ROOT`.
                    returned: on success
                    type: string
                    sample: NONE
                anonymous_uid:
                    description:
                        - UID value to remap to when squashing a client UID (see
                          identitySquash for more details.) If unspecified, defaults
                          to `65534`.
                    returned: on success
                    type: int
                    sample: 56
                anonymous_gid:
                    description:
                        - GID value to remap to when squashing a client GID (see
                          identitySquash for more details.) If unspecified defaults
                          to `65534`.
                    returned: on success
                    type: int
                    sample: 56
        export_set_id:
            description:
                - The OCID of this export's export set.
            returned: on success
            type: string
            sample: ocid1.exportset.oc1..xxxxxxEXAMPLExxxxxx
        file_system_id:
            description:
                - The OCID of this export's file system.
            returned: on success
            type: string
            sample: ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx
        id:
            description:
                - The OCID of this export.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of this export.
            returned: on success
            type: string
            sample: CREATING
        path:
            description:
                - Path used to access the associated file system.
                - Avoid entering confidential information.
                - "Example: `/accounting`"
            returned: on success
            type: string
            sample: /accounting
        time_created:
            description:
                - The date and time the export was created, expressed
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: [{
        "export_options": [{
            "source": "source_example",
            "require_privileged_source_port": true,
            "access": "READ_WRITE",
            "identity_squash": "NONE",
            "anonymous_uid": 56,
            "anonymous_gid": 56
        }],
        "export_set_id": "ocid1.exportset.oc1..xxxxxxEXAMPLExxxxxx",
        "file_system_id": "ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "path": "/accounting",
        "time_created": "2016-08-25T21:10:29.600Z"
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


class ExportFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "export_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_export, export_id=self.module.params.get("export_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "export_set_id",
            "file_system_id",
            "lifecycle_state",
            "id",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_exports, **optional_kwargs
        )


ExportFactsHelperCustom = get_custom_class("ExportFactsHelperCustom")


class ResourceFactsHelper(ExportFactsHelperCustom, ExportFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            export_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            export_set_id=dict(type="str"),
            file_system_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"],
            ),
            id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "PATH"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="export",
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

    module.exit_json(exports=result)


if __name__ == "__main__":
    main()
