#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_file_storage_export_set
short_description: Manage an ExportSet resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an ExportSet resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    export_set_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the export set.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    display_name:
        description:
            - A user-friendly name. It does not have to be unique, and it is changeable.
              Avoid entering confidential information.
            - "Example: `My export set`"
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    max_fs_stat_bytes:
        description:
            - Controls the maximum `tbytes`, `fbytes`, and `abytes`
              values reported by `NFS FSSTAT` calls through any associated
              mount targets. This is an advanced feature. For most
              applications, use the default value. The
              `tbytes` value reported by `FSSTAT` will be
              `maxFsStatBytes`. The value of `fbytes` and `abytes` will be
              `maxFsStatBytes` minus the metered size of the file
              system. If the metered size is larger than `maxFsStatBytes`,
              then `fbytes` and `abytes` will both be '0'.
            - This parameter is updatable.
        type: int
    max_fs_stat_files:
        description:
            - Controls the maximum `ffiles`, `ffiles`, and `afiles`
              values reported by `NFS FSSTAT` calls through any associated
              mount targets. This is an advanced feature. For most
              applications, use the default value. The
              `tfiles` value reported by `FSSTAT` will be
              `maxFsStatFiles`. The value of `ffiles` and `afiles` will be
              `maxFsStatFiles` minus the metered size of the file
              system. If the metered size is larger than `maxFsStatFiles`,
              then `ffiles` and `afiles` will both be '0'.
            - This parameter is updatable.
        type: int
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the ExportSet.
            - Use I(state=present) to update an existing an ExportSet.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update export_set
  oci_file_storage_export_set:
    # required
    export_set_id: "ocid1.exportset.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    max_fs_stat_bytes: 56
    max_fs_stat_files: 56

- name: Update export_set using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_file_storage_export_set:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1

    # optional
    max_fs_stat_bytes: 56
    max_fs_stat_files: 56

"""

RETURN = """
export_set:
    description:
        - Details of the ExportSet resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain the export set is in. May be unset
                  as a blank or NULL value.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the export set.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
                - "Example: `My export set`"
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the export set.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the export set.
            returned: on success
            type: str
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
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the virtual cloud network (VCN) the export set is in.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "max_fs_stat_bytes": 56,
        "max_fs_stat_files": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.file_storage import FileStorageClient
    from oci.file_storage.models import UpdateExportSetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExportSetHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_possible_entity_types(self):
        return super(ExportSetHelperGen, self).get_possible_entity_types() + [
            "exportset",
            "exportsets",
            "fileStorageexportset",
            "fileStorageexportsets",
            "exportsetresource",
            "exportsetsresource",
            "filestorage",
        ]

    def get_module_resource_id_param(self):
        return "export_set_id"

    def get_module_resource_id(self):
        return self.module.params.get("export_set_id")

    def get_get_fn(self):
        return self.client.get_export_set

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_export_set, export_set_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_export_set,
            export_set_id=self.module.params.get("export_set_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "availability_domain",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_export_sets, **kwargs
        )

    def get_update_model_class(self):
        return UpdateExportSetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_export_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                export_set_id=self.module.params.get("export_set_id"),
                update_export_set_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


ExportSetHelperCustom = get_custom_class("ExportSetHelperCustom")


class ResourceHelper(ExportSetHelperCustom, ExportSetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            export_set_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            max_fs_stat_bytes=dict(type="int"),
            max_fs_stat_files=dict(type="int"),
            compartment_id=dict(type="str"),
            availability_domain=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="export_set",
        service_client_class=FileStorageClient,
        namespace="file_storage",
    )

    result = dict(changed=False)

    if resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
