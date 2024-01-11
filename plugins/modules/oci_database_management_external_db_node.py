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
module: oci_database_management_external_db_node
short_description: Manage an ExternalDbNode resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an ExternalDbNode resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_db_node_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external database node.
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
            - The state of the ExternalDbNode.
            - Use I(state=present) to update an existing an ExternalDbNode.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update external_db_node
  oci_database_management_external_db_node:
    # required
    external_db_node_id: "ocid1.externaldbnode.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    external_connector_id: "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
external_db_node:
    description:
        - Details of the ExternalDbNode resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB node.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the external DB node. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        component_name:
            description:
                - The name of the external DB node.
            returned: on success
            type: str
            sample: component_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        external_db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system that the DB node is a part of.
            returned: on success
            type: str
            sample: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        external_connector_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external connector.
            returned: on success
            type: str
            sample: "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx"
        host_name:
            description:
                - The host name for the DB node.
            returned: on success
            type: str
            sample: host_name_example
        cpu_core_count:
            description:
                - The number of CPU cores available on the DB node.
            returned: on success
            type: float
            sample: 3.4
        memory_size_in_gbs:
            description:
                - The total memory in gigabytes (GB) on the DB node.
            returned: on success
            type: float
            sample: 3.4
        additional_details:
            description:
                - "The additional details of the external DB node defined in `{\\"key\\": \\"value\\"}` format.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {}
        lifecycle_state:
            description:
                - The current lifecycle state of the external DB node.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        domain_name:
            description:
                - Name of the domain.
            returned: on success
            type: str
            sample: domain_name_example
        time_created:
            description:
                - The date and time the external DB node was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the external DB node was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "component_name": "component_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_system_id": "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "external_connector_id": "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx",
        "host_name": "host_name_example",
        "cpu_core_count": 3.4,
        "memory_size_in_gbs": 3.4,
        "additional_details": {},
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "domain_name": "domain_name_example",
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
    from oci.database_management.models import UpdateExternalDbNodeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalDbNodeHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_possible_entity_types(self):
        return super(ExternalDbNodeHelperGen, self).get_possible_entity_types() + [
            "externaldbnode",
            "externaldbnodes",
            "databaseManagementexternaldbnode",
            "databaseManagementexternaldbnodes",
            "externaldbnoderesource",
            "externaldbnodesresource",
            "databasemanagement",
        ]

    def get_module_resource_id_param(self):
        return "external_db_node_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_db_node_id")

    def get_get_fn(self):
        return self.client.get_external_db_node

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_db_node, external_db_node_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_db_node,
            external_db_node_id=self.module.params.get("external_db_node_id"),
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
            self.client.list_external_db_nodes, **kwargs
        )

    def get_update_model_class(self):
        return UpdateExternalDbNodeDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_external_db_node,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_db_node_id=self.module.params.get("external_db_node_id"),
                update_external_db_node_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ExternalDbNodeHelperCustom = get_custom_class("ExternalDbNodeHelperCustom")


class ResourceHelper(ExternalDbNodeHelperCustom, ExternalDbNodeHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            external_db_node_id=dict(aliases=["id"], type="str", required=True),
            external_connector_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="external_db_node",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
