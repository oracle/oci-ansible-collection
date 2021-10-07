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
module: oci_network_drg_route_table
short_description: Manage a DrgRouteTable resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DrgRouteTable resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new DRG route table for the specified DRG. Assign the DRG route table to a DRG attachment
      using the `UpdateDrgAttachment` or `CreateDrgAttachment` operations.
    - "This resource has the following action operations in the M(oci_drg_route_table_actions) module: remove_import_drg_route_distribution."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    drg_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG the DRG route table belongs to.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    import_drg_route_distribution_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the import route distribution used to specify how incoming
              route advertisements through
              referenced attachments are inserted into the DRG route table.
            - This parameter is updatable.
        type: str
    is_ecmp_enabled:
        description:
            - If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to
              your on-premises networks, enable ECMP on the DRG route table.
            - This parameter is updatable.
        type: bool
    drg_route_table_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DrgRouteTable.
            - Use I(state=present) to create or update a DrgRouteTable.
            - Use I(state=absent) to delete a DrgRouteTable.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create drg_route_table
  oci_network_drg_route_table:
    drg_id: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update drg_route_table using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_drg_route_table:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    drg_id: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
    import_drg_route_distribution_id: "ocid1.importdrgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx"
    is_ecmp_enabled: true

- name: Update drg_route_table
  oci_network_drg_route_table:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    drg_route_table_id: "ocid1.drgroutetable.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete drg_route_table
  oci_network_drg_route_table:
    drg_route_table_id: "ocid1.drgroutetable.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete drg_route_table using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_drg_route_table:
    display_name: display_name_example
    drg_id: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
drg_route_table:
    description:
        - Details of the DrgRouteTable resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the
                  DRG route table.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment the DRG is in. The DRG route table
                  is always in the same compartment as the DRG.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        drg_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DRG the DRG that contains this route table.
            returned: on success
            type: str
            sample: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        time_created:
            description:
                - The date and time the DRG route table was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        lifecycle_state:
            description:
                - The DRG route table's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        import_drg_route_distribution_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the import route distribution used to specify how
                  incoming route advertisements from
                  referenced attachments are inserted into the DRG route table.
            returned: on success
            type: str
            sample: "ocid1.importdrgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx"
        is_ecmp_enabled:
            description:
                - If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to
                  your on-premises network, enable ECMP on the DRG route table to which these attachments
                  import routes.
            returned: on success
            type: bool
            sample: true
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "drg_id": "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "time_created": "2016-08-25T21:10:29.600Z",
        "lifecycle_state": "PROVISIONING",
        "import_drg_route_distribution_id": "ocid1.importdrgroutedistribution.oc1..xxxxxxEXAMPLExxxxxx",
        "is_ecmp_enabled": true
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateDrgRouteTableDetails
    from oci.core.models import UpdateDrgRouteTableDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrgRouteTableHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "drg_route_table_id"

    def get_module_resource_id(self):
        return self.module.params.get("drg_route_table_id")

    def get_get_fn(self):
        return self.client.get_drg_route_table

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_drg_route_table,
            drg_route_table_id=self.module.params.get("drg_route_table_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "drg_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name"]
            if self._use_name_as_identifier()
            else ["display_name", "import_drg_route_distribution_id"]
        )

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
            self.client.list_drg_route_tables, **kwargs
        )

    def get_create_model_class(self):
        return CreateDrgRouteTableDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_drg_route_table,
            call_fn_args=(),
            call_fn_kwargs=dict(create_drg_route_table_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateDrgRouteTableDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_drg_route_table,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_route_table_id=self.module.params.get("drg_route_table_id"),
                update_drg_route_table_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_drg_route_table,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_route_table_id=self.module.params.get("drg_route_table_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DrgRouteTableHelperCustom = get_custom_class("DrgRouteTableHelperCustom")


class ResourceHelper(DrgRouteTableHelperCustom, DrgRouteTableHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            drg_id=dict(type="str"),
            import_drg_route_distribution_id=dict(type="str"),
            is_ecmp_enabled=dict(type="bool"),
            drg_route_table_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="drg_route_table",
        service_client_class=VirtualNetworkClient,
        namespace="core",
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
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
