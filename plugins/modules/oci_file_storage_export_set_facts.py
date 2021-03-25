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
module: oci_file_storage_export_set_facts
short_description: Fetches details about one or multiple ExportSet resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExportSet resources in Oracle Cloud Infrastructure
    - Lists the export set resources in the specified compartment.
    - If I(export_set_id) is specified, the details of a single ExportSet will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    export_set_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the export set.
            - Required to get a specific export_set.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple export_sets.
        type: str
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
            - Required to list multiple export_sets.
        type: str
    display_name:
        description:
            - A user-friendly name. It does not have to be unique, and it is changeable.
            - "Example: `My resource`"
        type: str
        aliases: ["name"]
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
    sort_by:
        description:
            - The field to sort by. You can provide either value, but not both.
              By default, when you sort by time created, results are shown
              in descending order. When you sort by display name, results are
              shown in ascending order.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc', where 'asc' is
              ascending and 'desc' is descending. The default order is 'desc'
              except for numeric values.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List export_sets
  oci_file_storage_export_set_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1

- name: Get a specific export_set
  oci_file_storage_export_set_facts:
    export_set_id: "ocid1.exportset.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
export_sets:
    description:
        - List of ExportSet resources
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain the export set is in. May be unset
                  as a blank or NULL value.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the export set.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
                - "Example: `My export set`"
            returned: on success
            type: string
            sample: My export set
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the export set.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the export set.
            returned: on success
            type: string
            sample: CREATING
        max_fs_stat_bytes:
            description:
                - Controls the maximum `tbytes`, `fbytes`, and `abytes`,
                  values reported by `NFS FSSTAT` calls through any associated
                  mount targets. This is an advanced feature. For most
                  applications, use the default value. The
                  `tbytes` value reported by `FSSTAT` will be
                  `maxFsStatBytes`. The value of `fbytes` and `abytes` will be
                  `maxFsStatBytes` minus the metered size of the file
                  system. If the metered size is larger than `maxFsStatBytes`,
                  then `fbytes` and `abytes` will both be '0'.
            returned: on success
            type: int
            sample: 56
        max_fs_stat_files:
            description:
                - Controls the maximum `tfiles`, `ffiles`, and `afiles`
                  values reported by `NFS FSSTAT` calls through any associated
                  mount targets. This is an advanced feature. For most
                  applications, use the default value. The
                  `tfiles` value reported by `FSSTAT` will be
                  `maxFsStatFiles`. The value of `ffiles` and `afiles` will be
                  `maxFsStatFiles` minus the metered size of the file
                  system. If the metered size is larger than `maxFsStatFiles`,
                  then `ffiles` and `afiles` will both be '0'.
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - The date and time the export set was created, expressed
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the virtual cloud network (VCN) the export set is in.
            returned: on success
            type: string
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "My export set",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "max_fs_stat_bytes": 56,
        "max_fs_stat_files": 56,
        "time_created": "2016-08-25T21:10:29.600Z",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
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


class ExportSetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "export_set_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "availability_domain",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_export_set,
            export_set_id=self.module.params.get("export_set_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "lifecycle_state",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_export_sets,
            compartment_id=self.module.params.get("compartment_id"),
            availability_domain=self.module.params.get("availability_domain"),
            **optional_kwargs
        )


ExportSetFactsHelperCustom = get_custom_class("ExportSetFactsHelperCustom")


class ResourceFactsHelper(ExportSetFactsHelperCustom, ExportSetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            export_set_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            availability_domain=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"],
            ),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="export_set",
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

    module.exit_json(export_sets=result)


if __name__ == "__main__":
    main()
