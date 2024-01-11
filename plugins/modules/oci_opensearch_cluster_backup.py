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
module: oci_opensearch_cluster_backup
short_description: Manage an OpensearchClusterBackup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete an OpensearchClusterBackup resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - The name of the cluster backup.
            - Required for update using I(state=present) with opensearch_cluster_backup_id present.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    opensearch_cluster_backup_id:
        description:
            - unique OpensearchClusterBackup identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the OpensearchClusterBackup.
            - Use I(state=present) to update an existing an OpensearchClusterBackup.
            - Use I(state=absent) to delete an OpensearchClusterBackup.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update opensearch_cluster_backup
  oci_opensearch_cluster_backup:
    # required
    display_name: display_name_example
    opensearch_cluster_backup_id: "ocid1.opensearchclusterbackup.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update opensearch_cluster_backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_opensearch_cluster_backup:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete opensearch_cluster_backup
  oci_opensearch_cluster_backup:
    # required
    opensearch_cluster_backup_id: "ocid1.opensearchclusterbackup.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete opensearch_cluster_backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_opensearch_cluster_backup:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
opensearch_cluster_backup:
    description:
        - Details of the OpensearchClusterBackup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the cluster backup.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the cluster backup. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment where the cluster backup is located.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        backup_type:
            description:
                - Specifies whether the cluster backup was created manually, or automatically as a scheduled backup.
            returned: on success
            type: str
            sample: SCHEDULED
        time_created:
            description:
                - The date and time the cluster backup was created. Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the cluster backup was updated. Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the cluster backup.
            returned: on success
            type: str
            sample: CREATING
        lifecyle_details:
            description:
                - Additional information about the current lifecycle state of the cluster backup.
            returned: on success
            type: str
            sample: lifecyle_details_example
        source_cluster_id:
            description:
                - The OCID of the source OpenSearch cluster for the cluster backup.
            returned: on success
            type: str
            sample: "ocid1.sourcecluster.oc1..xxxxxxEXAMPLExxxxxx"
        namespace:
            description:
                - The Object Storage namespace for the cluster backup.
            returned: on success
            type: str
            sample: namespace_example
        bucket_name:
            description:
                - The name of the Object Storage bucket for the cluster backup.
            returned: on success
            type: str
            sample: bucket_name_example
        prefix:
            description:
                - The prefix within the Object Storage bucket for the cluster backup.
            returned: on success
            type: str
            sample: prefix_example
        time_expired:
            description:
                - The date and time the cluster backup expires. Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        backup_size:
            description:
                - The size in GB of the cluster backup.
            returned: on success
            type: float
            sample: 1.2
        source_cluster_display_name:
            description:
                - The name of the source OpenSearch cluster for the cluster backup.
            returned: on success
            type: str
            sample: source_cluster_display_name_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "backup_type": "SCHEDULED",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecyle_details": "lifecyle_details_example",
        "source_cluster_id": "ocid1.sourcecluster.oc1..xxxxxxEXAMPLExxxxxx",
        "namespace": "namespace_example",
        "bucket_name": "bucket_name_example",
        "prefix": "prefix_example",
        "time_expired": "2013-10-20T19:20:30+01:00",
        "backup_size": 1.2,
        "source_cluster_display_name": "source_cluster_display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.opensearch import OpensearchClusterBackupClient
    from oci.opensearch.models import UpdateOpensearchClusterBackupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpensearchClusterBackupHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            OpensearchClusterBackupHelperGen, self
        ).get_possible_entity_types() + [
            "opensearchclusterbackup",
            "opensearchclusterbackups",
            "opensearchopensearchclusterbackup",
            "opensearchopensearchclusterbackups",
            "opensearchclusterbackupresource",
            "opensearchclusterbackupsresource",
            "opensearch",
        ]

    def get_module_resource_id_param(self):
        return "opensearch_cluster_backup_id"

    def get_module_resource_id(self):
        return self.module.params.get("opensearch_cluster_backup_id")

    def get_get_fn(self):
        return self.client.get_opensearch_cluster_backup

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_opensearch_cluster_backup,
            opensearch_cluster_backup_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_opensearch_cluster_backup,
            opensearch_cluster_backup_id=self.module.params.get(
                "opensearch_cluster_backup_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
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
            self.client.list_opensearch_cluster_backups, **kwargs
        )

    def get_update_model_class(self):
        return UpdateOpensearchClusterBackupDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_opensearch_cluster_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opensearch_cluster_backup_id=self.module.params.get(
                    "opensearch_cluster_backup_id"
                ),
                update_opensearch_cluster_backup_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_opensearch_cluster_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opensearch_cluster_backup_id=self.module.params.get(
                    "opensearch_cluster_backup_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OpensearchClusterBackupHelperCustom = get_custom_class(
    "OpensearchClusterBackupHelperCustom"
)


class ResourceHelper(
    OpensearchClusterBackupHelperCustom, OpensearchClusterBackupHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            opensearch_cluster_backup_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="opensearch_cluster_backup",
        service_client_class=OpensearchClusterBackupClient,
        namespace="opensearch",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
