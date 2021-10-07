#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_mysql_heat_wave_cluster
short_description: Manage a HeatWaveCluster resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete a HeatWaveCluster resource in Oracle Cloud Infrastructure
    - "This resource has the following action operations in the M(oci_heat_wave_cluster_actions) module: add, restart, start, stop."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_system_id:
        description:
            - The DB System L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    shape_name:
        description:
            - A change to the shape of the nodes in the HeatWave cluster will
              result in the entire cluster being torn down and re-created with
              Compute instances of the new Shape. This may result in significant
              downtime for the analytics capability while the HeatWave cluster is
              re-provisioned.
            - This parameter is updatable.
        type: str
    cluster_size:
        description:
            - A change to the number of nodes in the HeatWave cluster will result
              in the entire cluster being torn down and re-created with the new
              cluster of nodes. This may result in a significant downtime for the
              analytics capability while the HeatWave cluster is
              re-provisioned.
            - This parameter is updatable.
        type: int
    state:
        description:
            - The state of the HeatWaveCluster.
            - Use I(state=present) to update an existing a HeatWaveCluster.
            - Use I(state=absent) to delete a HeatWaveCluster.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update heat_wave_cluster
  oci_mysql_heat_wave_cluster:
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    shape_name: shape_name_example

- name: Delete heat_wave_cluster
  oci_mysql_heat_wave_cluster:
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
heat_wave_cluster:
    description:
        - Details of the HeatWaveCluster resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        db_system_id:
            description:
                - The OCID of the parent DB System this HeatWave cluster is attached to.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        shape_name:
            description:
                - "The shape determines resources to allocate to the HeatWave
                  nodes - CPU cores, memory."
            returned: on success
            type: str
            sample: shape_name_example
        cluster_size:
            description:
                - The number of analytics-processing compute instances, of the
                  specified shape, in the HeatWave cluster.
            returned: on success
            type: int
            sample: 56
        cluster_nodes:
            description:
                - A HeatWave node is a compute host that is part of a HeatWave cluster.
            returned: on success
            type: complex
            contains:
                node_id:
                    description:
                        - The ID of the node within MySQL HeatWave cluster.
                    returned: on success
                    type: str
                    sample: "ocid1.node.oc1..xxxxxxEXAMPLExxxxxx"
                lifecycle_state:
                    description:
                        - The current state of the MySQL HeatWave node.
                    returned: on success
                    type: str
                    sample: CREATING
                time_created:
                    description:
                        - The date and time the MySQL HeatWave node was created,
                          as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The date and time the MySQL HeatWave node was updated,
                          as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the HeatWave cluster.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the HeatWave cluster was created,
                  as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the HeatWave cluster was last updated,
                  as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "shape_name": "shape_name_example",
        "cluster_size": 56,
        "cluster_nodes": [{
            "node_id": "ocid1.node.oc1..xxxxxxEXAMPLExxxxxx",
            "lifecycle_state": "CREATING",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00"
        }],
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.mysql import WorkRequestsClient
    from oci.mysql import DbSystemClient
    from oci.mysql.models import UpdateHeatWaveClusterDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlHeatWaveClusterHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestsClient)

    def get_module_resource_id_param(self):
        return "db_system_id"

    def get_module_resource_id(self):
        return self.module.params.get("db_system_id")

    def get_get_fn(self):
        return self.client.get_heat_wave_cluster

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_heat_wave_cluster,
            db_system_id=self.module.params.get("db_system_id"),
        )

    def get_update_model_class(self):
        return UpdateHeatWaveClusterDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_heat_wave_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_system_id=self.module.params.get("db_system_id"),
                update_heat_wave_cluster_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_heat_wave_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(db_system_id=self.module.params.get("db_system_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MysqlHeatWaveClusterHelperCustom = get_custom_class("MysqlHeatWaveClusterHelperCustom")


class ResourceHelper(MysqlHeatWaveClusterHelperCustom, MysqlHeatWaveClusterHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            db_system_id=dict(aliases=["id"], type="str", required=True),
            shape_name=dict(type="str"),
            cluster_size=dict(type="int"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="heat_wave_cluster",
        service_client_class=DbSystemClient,
        namespace="mysql",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
