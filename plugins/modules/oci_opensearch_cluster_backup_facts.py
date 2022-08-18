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
module: oci_opensearch_cluster_backup_facts
short_description: Fetches details about one or multiple OpensearchClusterBackup resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OpensearchClusterBackup resources in Oracle Cloud Infrastructure
    - Returns a list of OpensearchClusterBackups.
    - If I(opensearch_cluster_backup_id) is specified, the details of a single OpensearchClusterBackup will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    opensearch_cluster_backup_id:
        description:
            - unique OpensearchClusterBackup identifier
            - Required to get a specific opensearch_cluster_backup.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple opensearch_cluster_backups.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    source_opensearch_cluster_id:
        description:
            - A filter to return only resources that match the entire source cluster id given.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific opensearch_cluster_backup
  oci_opensearch_cluster_backup_facts:
    # required
    opensearch_cluster_backup_id: "ocid1.opensearchclusterbackup.oc1..xxxxxxEXAMPLExxxxxx"

- name: List opensearch_cluster_backups
  oci_opensearch_cluster_backup_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    display_name: display_name_example
    source_opensearch_cluster_id: "ocid1.sourceopensearchcluster.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
opensearch_cluster_backups:
    description:
        - List of OpensearchClusterBackup resources
    returned: on success
    type: complex
    contains:
        lifecyle_details:
            description:
                - Additional information about the current lifecycle state of the cluster backup.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecyle_details_example
        namespace:
            description:
                - The Object Storage namespace for the cluster backup.
                - Returned for get operation
            returned: on success
            type: str
            sample: namespace_example
        bucket_name:
            description:
                - The name of the Object Storage bucket for the cluster backup.
                - Returned for get operation
            returned: on success
            type: str
            sample: bucket_name_example
        prefix:
            description:
                - The prefix within the Object Storage bucket for the cluster backup.
                - Returned for get operation
            returned: on success
            type: str
            sample: prefix_example
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
        source_cluster_id:
            description:
                - The OCID of the source OpenSearch cluster for the cluster backup.
            returned: on success
            type: str
            sample: "ocid1.sourcecluster.oc1..xxxxxxEXAMPLExxxxxx"
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
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state of the cluster backup.
                - Returned for list operation
            returned: on success
            type: str
            sample: lifecycle_details_example
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
    sample: [{
        "lifecyle_details": "lifecyle_details_example",
        "namespace": "namespace_example",
        "bucket_name": "bucket_name_example",
        "prefix": "prefix_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "backup_type": "SCHEDULED",
        "source_cluster_id": "ocid1.sourcecluster.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_expired": "2013-10-20T19:20:30+01:00",
        "backup_size": 1.2,
        "source_cluster_display_name": "source_cluster_display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.opensearch import OpensearchClusterBackupClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpensearchClusterBackupFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "opensearch_cluster_backup_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_opensearch_cluster_backup,
            opensearch_cluster_backup_id=self.module.params.get(
                "opensearch_cluster_backup_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "source_opensearch_cluster_id",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_opensearch_cluster_backups,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OpensearchClusterBackupFactsHelperCustom = get_custom_class(
    "OpensearchClusterBackupFactsHelperCustom"
)


class ResourceFactsHelper(
    OpensearchClusterBackupFactsHelperCustom, OpensearchClusterBackupFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            opensearch_cluster_backup_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            source_opensearch_cluster_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="opensearch_cluster_backup",
        service_client_class=OpensearchClusterBackupClient,
        namespace="opensearch",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(opensearch_cluster_backups=result)


if __name__ == "__main__":
    main()
