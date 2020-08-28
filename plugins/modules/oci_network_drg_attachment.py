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
module: oci_network_drg_attachment
short_description: Manage a DrgAttachment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DrgAttachment resource in Oracle Cloud Infrastructure
    - For I(state=present), attaches the specified DRG to the specified VCN. A VCN can be attached to only one DRG at a time,
      and vice versa. The response includes a `DrgAttachment` object with its own OCID. For more
      information about DRGs, see
      L(Dynamic Routing Gateways (DRGs),https://docs.cloud.oracle.com/Content/Network/Tasks/managingDRGs.htm).
    - "You may optionally specify a *display name* for the attachment, otherwise a default is provided.
      It does not have to be unique, and you can change it. Avoid entering confidential information."
    - For the purposes of access control, the DRG attachment is automatically placed into the same compartment
      as the VCN. For more information about compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm).
version_added: "2.9"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - A user-friendly name. Does not have to be unique. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    drg_id:
        description:
            - The OCID of the DRG.
            - Required for create using I(state=present).
        type: str
    route_table_id:
        description:
            - The OCID of the route table the DRG attachment will use.
            - If you don't specify a route table here, the DRG attachment is created without an associated route
              table. The Networking service does NOT automatically associate the attached VCN's default route table
              with the DRG attachment.
            - "For information about why you would associate a route table with a DRG attachment, see:"
            - " * L(Transit Routing: Access to Multiple VCNs in Same Region,https://docs.cloud.oracle.com/Content/Network/Tasks/transitrouting.htm)
                * L(Transit Routing: Private Access to Oracle Services,https://docs.cloud.oracle.com/Content/Network/Tasks/transitroutingoracleservices.htm)"
        type: str
    vcn_id:
        description:
            - The OCID of the VCN.
            - Required for create using I(state=present).
        type: str
    drg_attachment_id:
        description:
            - The OCID of the DRG attachment.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the DrgAttachment.
            - Use I(state=present) to create or update a DrgAttachment.
            - Use I(state=absent) to delete a DrgAttachment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create drg_attachment
  oci_network_drg_attachment:
    drg_id: ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx
    vcn_id: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Update drg_attachment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_drg_attachment:
    display_name: display_name_example
    route_table_id: ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Update drg_attachment
  oci_network_drg_attachment:
    display_name: display_name_example
    route_table_id: ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx
    drg_attachment_id: ocid1.drgattachment.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete drg_attachment
  oci_network_drg_attachment:
    drg_attachment_id: ocid1.drgattachment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete drg_attachment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_drg_attachment:
    display_name: display_name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
drg_attachment:
    description:
        - Details of the DrgAttachment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment containing the DRG attachment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        drg_id:
            description:
                - The OCID of the DRG.
            returned: on success
            type: string
            sample: ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx
        id:
            description:
                - The DRG attachment's Oracle ID (OCID).
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The DRG attachment's current state.
            returned: on success
            type: string
            sample: ATTACHING
        route_table_id:
            description:
                - The OCID of the route table the DRG attachment is using.
                - "For information about why you would associate a route table with a DRG attachment, see:"
                - " * L(Transit Routing: Access to Multiple VCNs in Same Region,https://docs.cloud.oracle.com/Content/Network/Tasks/transitrouting.htm)
                    * L(Transit Routing: Private Access to Oracle
                    Services,https://docs.cloud.oracle.com/Content/Network/Tasks/transitroutingoracleservices.htm)"
            returned: on success
            type: string
            sample: ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The date and time the DRG attachment was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vcn_id:
            description:
                - The OCID of the VCN.
            returned: on success
            type: string
            sample: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "drg_id": "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ATTACHING",
        "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core.models import CreateDrgAttachmentDetails
    from oci.core.models import UpdateDrgAttachmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrgAttachmentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "drg_attachment_id"

    def get_module_resource_id(self):
        return self.module.params.get("drg_attachment_id")

    def get_get_fn(self):
        return self.client.get_drg_attachment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_drg_attachment,
            drg_attachment_id=self.module.params.get("drg_attachment_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["vcn_id", "drg_id"]

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
            self.client.list_drg_attachments, **kwargs
        )

    def get_create_model_class(self):
        return CreateDrgAttachmentDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_drg_attachment,
            call_fn_args=(),
            call_fn_kwargs=dict(create_drg_attachment_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateDrgAttachmentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_drg_attachment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_attachment_id=self.module.params.get("drg_attachment_id"),
                update_drg_attachment_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_drg_attachment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_attachment_id=self.module.params.get("drg_attachment_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


DrgAttachmentHelperCustom = get_custom_class("DrgAttachmentHelperCustom")


class ResourceHelper(DrgAttachmentHelperCustom, DrgAttachmentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            drg_id=dict(type="str"),
            route_table_id=dict(type="str"),
            vcn_id=dict(type="str"),
            drg_attachment_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="drg_attachment",
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
