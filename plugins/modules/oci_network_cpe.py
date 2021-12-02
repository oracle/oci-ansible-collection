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
module: oci_network_cpe
short_description: Manage a Cpe resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Cpe resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new virtual customer-premises equipment (CPE) object in the specified compartment. For
      more information, see L(Site-to-Site VPN Overview,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm).
    - For the purposes of access control, you must provide the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
      where you want
      the CPE to reside. Notice that the CPE doesn't have to be in the same compartment as the IPSec
      connection or other Networking Service components. If you're not sure which compartment to
      use, put the CPE in the same compartment as the DRG. For more information about
      compartments and access control, see L(Overview of the IAM Service,https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
      For information about OCIDs, see L(Resource Identifiers,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    - You must provide the public IP address of your on-premises router. See
      L(CPE Configuration,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/configuringCPE.htm).
    - "You may optionally specify a *display name* for the CPE, otherwise a default is provided. It does not have to
      be unique, and you can change it. Avoid entering confidential information."
    - "This resource has the following action operations in the M(oracle.oci.oci_network_cpe_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the CPE.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
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
    ip_address:
        description:
            - The public IP address of the on-premises router.
            - "Example: `203.0.113.2`"
            - Required for create using I(state=present).
        type: str
    cpe_device_shape_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the CPE device type. You can provide
              a value if you want to later generate CPE device configuration content for IPSec connections
              that use this CPE. You can also call L(UpdateCpe,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Cpe/UpdateCpe) later to
              provide a value. For a list of possible values, see
              L(ListCpeDeviceShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CpeDeviceShapeSummary/ListCpeDeviceShapes).
            - "For more information about generating CPE device configuration content, see:"
            - " * L(GetCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Cpe/GetCpeDeviceConfigContent)
                * L(GetIpsecCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnection/GetIpsecCpeDeviceConfigContent)
                * L(GetTunnelCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-
                us/iaas/api/#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfigContent)
                * L(GetTunnelCpeDeviceConfig,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfig)"
            - This parameter is updatable.
        type: str
    cpe_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the CPE.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Cpe.
            - Use I(state=present) to create or update a Cpe.
            - Use I(state=absent) to delete a Cpe.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create cpe
  oci_network_cpe:
    # required
    compartment_id: "ocid1.compartment.oc1..compartment_OCID"
    ip_address: 203.0.113.6

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: MyCpe
    freeform_tags: {'Department': 'Finance'}
    cpe_device_shape_id: "ocid1.cpedeviceshape.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update cpe
  oci_network_cpe:
    # required
    cpe_id: "ocid1.cpe.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: MyCpe
    freeform_tags: {'Department': 'Finance'}
    cpe_device_shape_id: "ocid1.cpedeviceshape.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update cpe using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_cpe:
    # required
    compartment_id: "ocid1.compartment.oc1..compartment_OCID"
    display_name: MyCpe

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    cpe_device_shape_id: "ocid1.cpedeviceshape.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete cpe
  oci_network_cpe:
    # required
    cpe_id: "ocid1.cpe.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete cpe using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_cpe:
    # required
    compartment_id: "ocid1.compartment.oc1..compartment_OCID"
    display_name: MyCpe
    state: absent

"""

RETURN = """
cpe:
    description:
        - Details of the Cpe resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the CPE.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
        id:
            description:
                - The CPE's Oracle ID (OCID).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        ip_address:
            description:
                - The public IP address of the on-premises router.
            returned: on success
            type: str
            sample: ip_address_example
        cpe_device_shape_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the CPE's device type.
                  The Networking service maintains a general list of CPE device types (for example,
                  Cisco ASA). For each type, Oracle provides CPE configuration content that can help
                  a network engineer configure the CPE. The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) uniquely
                  identifies the type of
                  device. To get the OCIDs for the device types on the list, see
                  L(ListCpeDeviceShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CpeDeviceShapeSummary/ListCpeDeviceShapes).
                - "For information about how to generate CPE configuration content for a
                  CPE device type, see:"
                - " * L(GetCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Cpe/GetCpeDeviceConfigContent)
                    * L(GetIpsecCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-
                    us/iaas/api/#/en/iaas/latest/IPSecConnection/GetIpsecCpeDeviceConfigContent)
                    * L(GetTunnelCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-
                    us/iaas/api/#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfigContent)
                    * L(GetTunnelCpeDeviceConfig,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/TunnelCpeDeviceConfig/GetTunnelCpeDeviceConfig)"
            returned: on success
            type: str
            sample: "ocid1.cpedeviceshape.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the CPE was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "ip_address": "ip_address_example",
        "cpe_device_shape_id": "ocid1.cpedeviceshape.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z"
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
    from oci.core.models import CreateCpeDetails
    from oci.core.models import UpdateCpeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CpeHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "cpe_id"

    def get_module_resource_id(self):
        return self.module.params.get("cpe_id")

    def get_get_fn(self):
        return self.client.get_cpe

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cpe, cpe_id=self.module.params.get("cpe_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_cpes, **kwargs)

    def get_create_model_class(self):
        return CreateCpeDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_cpe,
            call_fn_args=(),
            call_fn_kwargs=dict(create_cpe_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateCpeDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_cpe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cpe_id=self.module.params.get("cpe_id"),
                update_cpe_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_cpe,
            call_fn_args=(),
            call_fn_kwargs=dict(cpe_id=self.module.params.get("cpe_id"),),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


CpeHelperCustom = get_custom_class("CpeHelperCustom")


class ResourceHelper(CpeHelperCustom, CpeHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            ip_address=dict(type="str"),
            cpe_device_shape_id=dict(type="str"),
            cpe_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="cpe",
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
