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
module: oci_database_cloud_vm_cluster_iorm_config
short_description: Manage a CloudVmClusterIormConfig resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a CloudVmClusterIormConfig resource in Oracle Cloud Infrastructure
version_added: "2.9"
author: Oracle (@oracle)
options:
    cloud_vm_cluster_id:
        description:
            - The cloud VM cluster L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    objective:
        description:
            - "Value for the IORM objective
              Default is \\"Auto\\""
            - This parameter is updatable.
        type: str
        choices:
            - "LOW_LATENCY"
            - "HIGH_THROUGHPUT"
            - "BALANCED"
            - "AUTO"
            - "BASIC"
    db_plans:
        description:
            - Array of IORM Setting for all the database in
              this Exadata DB System
            - This parameter is updatable.
        type: list
        suboptions:
            db_name:
                description:
                    - The database name. For the default `DbPlan`, the `dbName` is `default`.
                    - This parameter is updatable.
                type: str
            share:
                description:
                    - The relative priority of this database.
                    - This parameter is updatable.
                type: int
    state:
        description:
            - The state of the CloudVmClusterIormConfig.
            - Use I(state=present) to update an existing a CloudVmClusterIormConfig.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update cloud_vm_cluster_iorm_config
  oci_database_cloud_vm_cluster_iorm_config:
    cloud_vm_cluster_id: ocid1.cloudvmcluster.oc1..xxxxxxEXAMPLExxxxxx
    objective: LOW_LATENCY

"""

RETURN = """
cloud_vm_cluster_iorm_config:
    description:
        - Details of the CloudVmClusterIormConfig resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        lifecycle_state:
            description:
                - The current state of IORM configuration for the Exadata DB system.
            returned: on success
            type: string
            sample: BOOTSTRAPPING
        lifecycle_details:
            description:
                - Additional information about the current `lifecycleState`.
            returned: on success
            type: string
            sample: lifecycle_details_example
        objective:
            description:
                - The current value for the IORM objective.
                  The default is `AUTO`.
            returned: on success
            type: string
            sample: LOW_LATENCY
        db_plans:
            description:
                - An array of IORM settings for all the database in
                  the Exadata DB system.
            returned: on success
            type: complex
            contains:
                db_name:
                    description:
                        - The database name. For the default `DbPlan`, the `dbName` is `default`.
                    returned: on success
                    type: string
                    sample: db_name_example
                share:
                    description:
                        - The relative priority of this database.
                    returned: on success
                    type: int
                    sample: 56
                flash_cache_limit:
                    description:
                        - The flash cache limit for this database. This value is internally configured based on the share value assigned to the database.
                    returned: on success
                    type: string
                    sample: flash_cache_limit_example
    sample: {
        "lifecycle_state": "BOOTSTRAPPING",
        "lifecycle_details": "lifecycle_details_example",
        "objective": "LOW_LATENCY",
        "db_plans": [{
            "db_name": "db_name_example",
            "share": 56,
            "flash_cache_limit": "flash_cache_limit_example"
        }]
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
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import ExadataIormConfigUpdateDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CloudVmClusterIormConfigHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def __init__(self, *args, **kwargs):
        super(CloudVmClusterIormConfigHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_module_resource_id_param(self):
        return "cloud_vm_cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("cloud_vm_cluster_id")

    def get_get_fn(self):
        return self.client.get_cloud_vm_cluster_iorm_config

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cloud_vm_cluster_iorm_config,
            cloud_vm_cluster_id=self.module.params.get("cloud_vm_cluster_id"),
        )

    def get_update_model_class(self):
        return ExadataIormConfigUpdateDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_cloud_vm_cluster_iorm_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cloud_vm_cluster_id=self.module.params.get("cloud_vm_cluster_id"),
                cloud_vm_cluster_iorm_config_update_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


CloudVmClusterIormConfigHelperCustom = get_custom_class(
    "CloudVmClusterIormConfigHelperCustom"
)


class ResourceHelper(
    CloudVmClusterIormConfigHelperCustom, CloudVmClusterIormConfigHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            cloud_vm_cluster_id=dict(aliases=["id"], type="str", required=True),
            objective=dict(
                type="str",
                choices=["LOW_LATENCY", "HIGH_THROUGHPUT", "BALANCED", "AUTO", "BASIC"],
            ),
            db_plans=dict(
                type="list",
                elements="dict",
                options=dict(db_name=dict(type="str"), share=dict(type="int")),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="cloud_vm_cluster_iorm_config",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
