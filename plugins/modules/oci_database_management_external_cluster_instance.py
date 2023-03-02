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
module: oci_database_management_external_cluster_instance
short_description: Manage an ExternalClusterInstance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an ExternalClusterInstance resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_cluster_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external cluster instance.
        type: str
        aliases: ["id"]
        required: true
    external_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external connector.
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the ExternalClusterInstance.
            - Use I(state=present) to update an existing an ExternalClusterInstance.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update external_cluster_instance
  oci_database_management_external_cluster_instance:
    # required
    external_cluster_instance_id: "ocid1.externalclusterinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    external_connector_id: "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
external_cluster_instance:
    description:
        - Details of the ExternalClusterInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external cluster instance.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the cluster instance. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        component_name:
            description:
                - The name of the external cluster instance.
            returned: on success
            type: str
            sample: component_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        external_cluster_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external cluster that the cluster instance belongs
                  to.
            returned: on success
            type: str
            sample: "ocid1.externalcluster.oc1..xxxxxxEXAMPLExxxxxx"
        external_db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system that the cluster instance is a
                  part of.
            returned: on success
            type: str
            sample: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        external_db_node_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB node.
            returned: on success
            type: str
            sample: "ocid1.externaldbnode.oc1..xxxxxxEXAMPLExxxxxx"
        external_connector_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external connector.
            returned: on success
            type: str
            sample: "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx"
        host_name:
            description:
                - The name of the host on which the cluster instance is running.
            returned: on success
            type: str
            sample: host_name_example
        node_role:
            description:
                - The role of the cluster node.
            returned: on success
            type: str
            sample: HUB
        crs_base_directory:
            description:
                - The Oracle base location of Cluster Ready Services (CRS).
            returned: on success
            type: str
            sample: crs_base_directory_example
        adr_home_directory:
            description:
                - The Automatic Diagnostic Repository (ADR) home directory for the cluster instance.
            returned: on success
            type: str
            sample: adr_home_directory_example
        lifecycle_state:
            description:
                - The current lifecycle state of the external cluster instance.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the external cluster instance was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the external cluster instance was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "component_name": "component_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "external_cluster_id": "ocid1.externalcluster.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_system_id": "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_node_id": "ocid1.externaldbnode.oc1..xxxxxxEXAMPLExxxxxx",
        "external_connector_id": "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx",
        "host_name": "host_name_example",
        "node_role": "HUB",
        "crs_base_directory": "crs_base_directory_example",
        "adr_home_directory": "adr_home_directory_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
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
    from oci.database_management import DbManagementClient
    from oci.database_management.models import UpdateExternalClusterInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalClusterInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_possible_entity_types(self):
        return super(
            ExternalClusterInstanceHelperGen, self
        ).get_possible_entity_types() + [
            "externalclusterinstance",
            "externalclusterinstances",
            "databaseManagementexternalclusterinstance",
            "databaseManagementexternalclusterinstances",
            "externalclusterinstanceresource",
            "externalclusterinstancesresource",
            "databasemanagement",
        ]

    def get_module_resource_id_param(self):
        return "external_cluster_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_cluster_instance_id")

    def get_get_fn(self):
        return self.client.get_external_cluster_instance

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_cluster_instance,
            external_cluster_instance_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_cluster_instance,
            external_cluster_instance_id=self.module.params.get(
                "external_cluster_instance_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_external_cluster_instances, **kwargs
        )

    def get_update_model_class(self):
        return UpdateExternalClusterInstanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_external_cluster_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_cluster_instance_id=self.module.params.get(
                    "external_cluster_instance_id"
                ),
                update_external_cluster_instance_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ExternalClusterInstanceHelperCustom = get_custom_class(
    "ExternalClusterInstanceHelperCustom"
)


class ResourceHelper(
    ExternalClusterInstanceHelperCustom, ExternalClusterInstanceHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            external_cluster_instance_id=dict(
                aliases=["id"], type="str", required=True
            ),
            external_connector_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="external_cluster_instance",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
