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
module: oci_database_management_db_management_private_endpoint_actions
short_description: Perform actions on a DbManagementPrivateEndpoint resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DbManagementPrivateEndpoint resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the Database Management private endpoint and its dependent resources to the specified compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_management_private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Management private endpoint.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to which the Database Management private
              endpoint needs to be moved.
        type: str
    action:
        description:
            - The action to perform on the DbManagementPrivateEndpoint.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on db_management_private_endpoint
  oci_database_management_db_management_private_endpoint_actions:
    # required
    db_management_private_endpoint_id: "ocid1.dbmanagementprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
db_management_private_endpoint:
    description:
        - Details of the DbManagementPrivateEndpoint resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Management private endpoint.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The display name of the Database Management private endpoint.
            returned: on success
            type: str
            sample: name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        is_cluster:
            description:
                - Specifies whether the Database Management private endpoint can be used for Oracle Databases in a cluster.
            returned: on success
            type: bool
            sample: true
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        private_ip:
            description:
                - The IP addresses assigned to the Database Management private endpoint.
            returned: on success
            type: str
            sample: private_ip_example
        description:
            description:
                - The description of the Database Management private endpoint.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The date and time the Database Managament private endpoint was created, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the Database Management private endpoint.
            returned: on success
            type: str
            sample: CREATING
        nsg_ids:
            description:
                - The OCIDs of the Network Security Groups to which the Database Management private endpoint belongs.
            returned: on success
            type: list
            sample: []
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cluster": true,
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "private_ip": "private_ip_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "nsg_ids": []
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient
    from oci.database_management.models import (
        ChangeDbManagementPrivateEndpointCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DbManagementPrivateEndpointActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "db_management_private_endpoint_id"

    def get_module_resource_id(self):
        return self.module.params.get("db_management_private_endpoint_id")

    def get_get_fn(self):
        return self.client.get_db_management_private_endpoint

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_management_private_endpoint,
            db_management_private_endpoint_id=self.module.params.get(
                "db_management_private_endpoint_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDbManagementPrivateEndpointCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_db_management_private_endpoint_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_management_private_endpoint_id=self.module.params.get(
                    "db_management_private_endpoint_id"
                ),
                change_db_management_private_endpoint_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


DbManagementPrivateEndpointActionsHelperCustom = get_custom_class(
    "DbManagementPrivateEndpointActionsHelperCustom"
)


class ResourceHelper(
    DbManagementPrivateEndpointActionsHelperCustom,
    DbManagementPrivateEndpointActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            db_management_private_endpoint_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="db_management_private_endpoint",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
