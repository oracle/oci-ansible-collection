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
module: oci_database_cloud_vm_cluster_iorm_config_facts
short_description: Fetches details about a CloudVmClusterIormConfig resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a CloudVmClusterIormConfig resource in Oracle Cloud Infrastructure
    - Gets the IORM configuration for the specified cloud VM cluster in an Exadata Cloud Service instance.
      If you have not specified an IORM configuration, the default configuration is returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    cloud_vm_cluster_id:
        description:
            - The cloud VM cluster L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific cloud_vm_cluster_iorm_config
  oci_database_cloud_vm_cluster_iorm_config_facts:
    cloud_vm_cluster_id: "ocid1.cloudvmcluster.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
cloud_vm_cluster_iorm_config:
    description:
        - CloudVmClusterIormConfig resource
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


class CloudVmClusterIormConfigFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "cloud_vm_cluster_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cloud_vm_cluster_iorm_config,
            cloud_vm_cluster_id=self.module.params.get("cloud_vm_cluster_id"),
        )


CloudVmClusterIormConfigFactsHelperCustom = get_custom_class(
    "CloudVmClusterIormConfigFactsHelperCustom"
)


class ResourceFactsHelper(
    CloudVmClusterIormConfigFactsHelperCustom, CloudVmClusterIormConfigFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(cloud_vm_cluster_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="cloud_vm_cluster_iorm_config",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(cloud_vm_cluster_iorm_config=result)


if __name__ == "__main__":
    main()
