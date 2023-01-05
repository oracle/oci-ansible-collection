#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_log_analytics_storage
short_description: Manage a Storage resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a Storage resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    archiving_configuration:
        description:
            - ""
        type: dict
        required: true
        suboptions:
            active_storage_duration:
                description:
                    - This is the duration data in active storage before data is archived, as described in
                      https://en.wikipedia.org/wiki/ISO_8601#Durations.
                      The largest supported unit is D, e.g. P365D (not P1Y) or P14D (not P2W).
                    - This parameter is updatable.
                type: str
            archival_storage_duration:
                description:
                    - This is the duration before archived data is deleted from object storage, as described in
                      https://en.wikipedia.org/wiki/ISO_8601#Durations
                      The largest supported unit is D, e.g. P365D (not P1Y) or P14D (not P2W).
                    - This parameter is updatable.
                type: str
    state:
        description:
            - The state of the Storage.
            - Use I(state=present) to update an existing a Storage.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update storage
  oci_log_analytics_storage:
    # required
    namespace_name: namespace_name_example
    archiving_configuration:
      # optional
      active_storage_duration: active_storage_duration_example
      archival_storage_duration: archival_storage_duration_example

"""

RETURN = """
storage:
    description:
        - Details of the Storage resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        is_archiving_enabled:
            description:
                - This indicates if old data can be archived for a tenancy
            returned: on success
            type: bool
            sample: true
        archiving_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                active_storage_duration:
                    description:
                        - This is the duration data in active storage before data is archived, as described in
                          https://en.wikipedia.org/wiki/ISO_8601#Durations.
                          The largest supported unit is D, e.g. P365D (not P1Y) or P14D (not P2W).
                    returned: on success
                    type: str
                    sample: active_storage_duration_example
                archival_storage_duration:
                    description:
                        - This is the duration before archived data is deleted from object storage, as described in
                          https://en.wikipedia.org/wiki/ISO_8601#Durations
                          The largest supported unit is D, e.g. P365D (not P1Y) or P14D (not P2W).
                    returned: on success
                    type: str
                    sample: archival_storage_duration_example
    sample: {
        "is_archiving_enabled": true,
        "archiving_configuration": {
            "active_storage_duration": "active_storage_duration_example",
            "archival_storage_duration": "archival_storage_duration_example"
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.log_analytics import LogAnalyticsClient
    from oci.log_analytics.models import UpdateStorageDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StorageHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_possible_entity_types(self):
        return super(StorageHelperGen, self).get_possible_entity_types() + [
            "storage",
            "storages",
            "logAnalyticsstorage",
            "logAnalyticsstorages",
            "storageresource",
            "storagesresource",
            "loganalytics",
        ]

    def get_module_resource_id_param(self):
        return "namespace_name"

    def get_module_resource_id(self):
        return self.module.params.get("namespace_name")

    def get_get_fn(self):
        return self.client.get_storage

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_storage,
            namespace_name=self.module.params.get("namespace_name"),
        )

    def get_update_model_class(self):
        return UpdateStorageDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_storage,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                update_storage_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


StorageHelperCustom = get_custom_class("StorageHelperCustom")


class ResourceHelper(StorageHelperCustom, StorageHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            archiving_configuration=dict(
                type="dict",
                required=True,
                options=dict(
                    active_storage_duration=dict(type="str"),
                    archival_storage_duration=dict(type="str"),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="storage",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
