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
module: oci_network_cross_connect
short_description: Manage a CrossConnect resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a CrossConnect resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new cross-connect. Oracle recommends you create each cross-connect in a
      L(CrossConnectGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CrossConnectGroup) so you can use link aggregation
      with the connection.
    - After creating the `CrossConnect` object, you need to go the FastConnect location
      and request to have the physical cable installed. For more information, see
      L(FastConnect Overview,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).
    - For the purposes of access control, you must provide the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
      compartment where you want the cross-connect to reside. If you're
      not sure which compartment to use, put the cross-connect in the
      same compartment with your VCN. For more information about
      compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
      For information about OCIDs, see
      L(Resource Identifiers,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    - "You may optionally specify a *display name* for the cross-connect.
      It does not have to be unique, and you can change it. Avoid entering confidential information."
    - "This resource has the following action operations in the M(oracle.oci.oci_network_cross_connect_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the cross-connect.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    cross_connect_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect group to put this cross-connect in.
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
    far_cross_connect_or_cross_connect_group_id:
        description:
            - If you already have an existing cross-connect or cross-connect group at this FastConnect
              location, and you want this new cross-connect to be on a different router (for the
              purposes of redundancy), provide the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of that existing cross-
              connect or
              cross-connect group.
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    location_name:
        description:
            - The name of the FastConnect location where this cross-connect will be installed.
              To get a list of the available locations, see
              L(ListCrossConnectLocations,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CrossConnectLocation/ListCrossConnectLocations).
            - "Example: `CyrusOne, Chandler, AZ`"
            - Required for create using I(state=present).
        type: str
    near_cross_connect_or_cross_connect_group_id:
        description:
            - If you already have an existing cross-connect or cross-connect group at this FastConnect
              location, and you want this new cross-connect to be on the same router, provide the
              L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of that existing cross-connect or cross-connect group.
        type: str
    port_speed_shape_name:
        description:
            - The port speed for this cross-connect. To get a list of the available port speeds, see
              L(ListCrossConnectPortSpeedShapes,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/iaas/latest/CrossConnectPortSpeedShape/ListCrossconnectPortSpeedShapes).
            - "Example: `10 Gbps`"
            - Required for create using I(state=present).
        type: str
    customer_reference_name:
        description:
            - A reference name or identifier for the physical fiber connection that this cross-connect
              uses.
            - This parameter is updatable.
        type: str
    macsec_properties:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            state:
                description:
                    - Indicates whether or not MACsec is enabled.
                    - This parameter is updatable.
                type: str
                choices:
                    - "ENABLED"
                    - "DISABLED"
                required: true
            primary_key:
                description:
                    - ""
                type: dict
                suboptions:
                    connectivity_association_name_secret_id:
                        description:
                            - Secret L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity association
                              Key Name (CKN) of this MACsec key.
                            - "NOTE: Only the latest secret version will be used."
                            - This parameter is updatable.
                        type: str
                        required: true
                    connectivity_association_key_secret_id:
                        description:
                            - Secret L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity Association
                              Key (CAK) of this MACsec key.
                            - "NOTE: Only the latest secret version will be used."
                            - This parameter is updatable.
                        type: str
                        required: true
                    connectivity_association_name_secret_version:
                        description:
                            - The secret version of the connectivity association name secret in Vault.
                            - This parameter is updatable.
                        type: int
                    connectivity_association_key_secret_version:
                        description:
                            - The secret version of the connectivityAssociationKey secret in Vault.
                            - This parameter is updatable.
                        type: int
            encryption_cipher:
                description:
                    - Type of encryption cipher suite to use for the MACsec connection.
                    - This parameter is updatable.
                type: str
                choices:
                    - "AES128_GCM"
                    - "AES128_GCM_XPN"
                    - "AES256_GCM"
                    - "AES256_GCM_XPN"
    cross_connect_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cross-connect.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    is_active:
        description:
            - Set to true to activate the cross-connect. You activate it after the physical cabling
              is complete, and you've confirmed the cross-connect's light levels are good and your side
              of the interface is up. Activation indicates to Oracle that the physical connection is ready.
            - "Example: `true`"
            - This parameter is updatable.
        type: bool
    state:
        description:
            - The state of the CrossConnect.
            - Use I(state=present) to create or update a CrossConnect.
            - Use I(state=absent) to delete a CrossConnect.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create cross_connect
  oci_network_cross_connect:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    location_name: location_name_example
    port_speed_shape_name: port_speed_shape_name_example

    # optional
    cross_connect_group_id: "ocid1.crossconnectgroup.oc1..xxxxxxEXAMPLExxxxxx"
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    far_cross_connect_or_cross_connect_group_id: "ocid1.farcrossconnectorcrossconnectgroup.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    near_cross_connect_or_cross_connect_group_id: "ocid1.nearcrossconnectorcrossconnectgroup.oc1..xxxxxxEXAMPLExxxxxx"
    customer_reference_name: customer_reference_name_example
    macsec_properties:
      # required
      state: ENABLED

      # optional
      primary_key:
        # required
        connectivity_association_name_secret_id: "ocid1.connectivityassociationnamesecret.oc1..xxxxxxEXAMPLExxxxxx"
        connectivity_association_key_secret_id: "ocid1.connectivityassociationkeysecret.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        connectivity_association_name_secret_version: 56
        connectivity_association_key_secret_version: 56
      encryption_cipher: AES128_GCM

- name: Update cross_connect
  oci_network_cross_connect:
    # required
    cross_connect_id: "ocid1.crossconnect.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    customer_reference_name: customer_reference_name_example
    macsec_properties:
      # required
      state: ENABLED

      # optional
      primary_key:
        # required
        connectivity_association_name_secret_id: "ocid1.connectivityassociationnamesecret.oc1..xxxxxxEXAMPLExxxxxx"
        connectivity_association_key_secret_id: "ocid1.connectivityassociationkeysecret.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        connectivity_association_name_secret_version: 56
        connectivity_association_key_secret_version: 56
      encryption_cipher: AES128_GCM
    is_active: true

- name: Update cross_connect using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_cross_connect:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    customer_reference_name: customer_reference_name_example
    macsec_properties:
      # required
      state: ENABLED

      # optional
      primary_key:
        # required
        connectivity_association_name_secret_id: "ocid1.connectivityassociationnamesecret.oc1..xxxxxxEXAMPLExxxxxx"
        connectivity_association_key_secret_id: "ocid1.connectivityassociationkeysecret.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        connectivity_association_name_secret_version: 56
        connectivity_association_key_secret_version: 56
      encryption_cipher: AES128_GCM
    is_active: true

- name: Delete cross_connect
  oci_network_cross_connect:
    # required
    cross_connect_id: "ocid1.crossconnect.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete cross_connect using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_cross_connect:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
cross_connect:
    description:
        - Details of the CrossConnect resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the cross-connect group.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        cross_connect_group_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect group this cross-connect belongs
                  to (if any).
            returned: on success
            type: str
            sample: "ocid1.crossconnectgroup.oc1..xxxxxxEXAMPLExxxxxx"
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
                - The cross-connect's Oracle ID (OCID).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The cross-connect's current state.
            returned: on success
            type: str
            sample: PENDING_CUSTOMER
        location_name:
            description:
                - The name of the FastConnect location where this cross-connect is installed.
            returned: on success
            type: str
            sample: location_name_example
        port_name:
            description:
                - A string identifying the meet-me room port for this cross-connect.
            returned: on success
            type: str
            sample: port_name_example
        port_speed_shape_name:
            description:
                - The port speed for this cross-connect.
                - "Example: `10 Gbps`"
            returned: on success
            type: str
            sample: port_speed_shape_name_example
        customer_reference_name:
            description:
                - A reference name or identifier for the physical fiber connection that this cross-connect
                  uses.
            returned: on success
            type: str
            sample: customer_reference_name_example
        time_created:
            description:
                - The date and time the cross-connect was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        macsec_properties:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                state:
                    description:
                        - Indicates whether or not MACsec is enabled.
                    returned: on success
                    type: str
                    sample: ENABLED
                primary_key:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        connectivity_association_name_secret_id:
                            description:
                                - Secret L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity
                                  association Key Name (CKN) of this MACsec key.
                            returned: on success
                            type: str
                            sample: "ocid1.connectivityassociationnamesecret.oc1..xxxxxxEXAMPLExxxxxx"
                        connectivity_association_name_secret_version:
                            description:
                                - The secret version of the connectivity association name secret in Vault.
                            returned: on success
                            type: int
                            sample: 56
                        connectivity_association_key_secret_id:
                            description:
                                - Secret L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity
                                  Association Key (CAK) of this MACsec key.
                            returned: on success
                            type: str
                            sample: "ocid1.connectivityassociationkeysecret.oc1..xxxxxxEXAMPLExxxxxx"
                        connectivity_association_key_secret_version:
                            description:
                                - The secret version of the `connectivityAssociationKey` secret in Vault.
                            returned: on success
                            type: int
                            sample: 56
                encryption_cipher:
                    description:
                        - Type of encryption cipher suite to use for the MACsec connection.
                    returned: on success
                    type: str
                    sample: AES128_GCM
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "cross_connect_group_id": "ocid1.crossconnectgroup.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PENDING_CUSTOMER",
        "location_name": "location_name_example",
        "port_name": "port_name_example",
        "port_speed_shape_name": "port_speed_shape_name_example",
        "customer_reference_name": "customer_reference_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "macsec_properties": {
            "state": "ENABLED",
            "primary_key": {
                "connectivity_association_name_secret_id": "ocid1.connectivityassociationnamesecret.oc1..xxxxxxEXAMPLExxxxxx",
                "connectivity_association_name_secret_version": 56,
                "connectivity_association_key_secret_id": "ocid1.connectivityassociationkeysecret.oc1..xxxxxxEXAMPLExxxxxx",
                "connectivity_association_key_secret_version": 56
            },
            "encryption_cipher": "AES128_GCM"
        }
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
    from oci.core.models import CreateCrossConnectDetails
    from oci.core.models import UpdateCrossConnectDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CrossConnectHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "cross_connect_id"

    def get_module_resource_id(self):
        return self.module.params.get("cross_connect_id")

    def get_get_fn(self):
        return self.client.get_cross_connect

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cross_connect,
            cross_connect_id=self.module.params.get("cross_connect_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["cross_connect_group_id", "display_name"]

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
            self.client.list_cross_connects, **kwargs
        )

    def get_create_model_class(self):
        return CreateCrossConnectDetails

    def get_exclude_attributes(self):
        return [
            "far_cross_connect_or_cross_connect_group_id",
            "near_cross_connect_or_cross_connect_group_id",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_cross_connect,
            call_fn_args=(),
            call_fn_kwargs=dict(create_cross_connect_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateCrossConnectDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_cross_connect,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cross_connect_id=self.module.params.get("cross_connect_id"),
                update_cross_connect_details=update_details,
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
            call_fn=self.client.delete_cross_connect,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cross_connect_id=self.module.params.get("cross_connect_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


CrossConnectHelperCustom = get_custom_class("CrossConnectHelperCustom")


class ResourceHelper(CrossConnectHelperCustom, CrossConnectHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            cross_connect_group_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            far_cross_connect_or_cross_connect_group_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            location_name=dict(type="str"),
            near_cross_connect_or_cross_connect_group_id=dict(type="str"),
            port_speed_shape_name=dict(type="str"),
            customer_reference_name=dict(type="str"),
            macsec_properties=dict(
                type="dict",
                options=dict(
                    state=dict(
                        type="str", required=True, choices=["ENABLED", "DISABLED"]
                    ),
                    primary_key=dict(
                        type="dict",
                        no_log=False,
                        options=dict(
                            connectivity_association_name_secret_id=dict(
                                type="str", required=True
                            ),
                            connectivity_association_key_secret_id=dict(
                                type="str", required=True
                            ),
                            connectivity_association_name_secret_version=dict(
                                type="int", no_log=True
                            ),
                            connectivity_association_key_secret_version=dict(
                                type="int", no_log=True
                            ),
                        ),
                    ),
                    encryption_cipher=dict(
                        type="str",
                        choices=[
                            "AES128_GCM",
                            "AES128_GCM_XPN",
                            "AES256_GCM",
                            "AES256_GCM_XPN",
                        ],
                    ),
                ),
            ),
            cross_connect_id=dict(aliases=["id"], type="str"),
            is_active=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="cross_connect",
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
