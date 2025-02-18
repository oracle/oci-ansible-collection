#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_file_storage_outbound_connector_actions
short_description: Perform actions on an OutboundConnector resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OutboundConnector resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves an outbound connector into a different compartment within the same tenancy.
      For information about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes)
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    outbound_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the outbound connector.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              to move the outbound connector to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the OutboundConnector.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on outbound_connector
  oci_file_storage_outbound_connector_actions:
    # required
    outbound_connector_id: "ocid1.outboundconnector.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
outbound_connector:
    description:
        - Details of the OutboundConnector resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain the outbound connector is in. May be unset
                  as a blank or NULL value.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the outbound connector.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the outbound connector.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of this outbound connector.
            returned: on success
            type: str
            sample: CREATING
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
                - "Example: `My outbound connector`"
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The date and time the outbound connector was created
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        connector_type:
            description:
                - The account type of this outbound connector.
            returned: on success
            type: str
            sample: LDAPBIND
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair
                   with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        endpoints:
            description:
                - Array of server endpoints to use when connecting with the LDAP bind account.
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - Name of the DNS server.
                    returned: on success
                    type: str
                    sample: hostname_example
                port:
                    description:
                        - Port of the DNS server.
                    returned: on success
                    type: int
                    sample: 56
        bind_distinguished_name:
            description:
                - The LDAP Distinguished Name of the account.
            returned: on success
            type: str
            sample: bind_distinguished_name_example
        password_secret_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the password for the LDAP bind account in the Vault.
            returned: on success
            type: str
            sample: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
        password_secret_version:
            description:
                - Version of the password secret in the Vault to use.
            returned: on success
            type: int
            sample: 56
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "connector_type": "LDAPBIND",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "endpoints": [{
            "hostname": "hostname_example",
            "port": 56
        }],
        "bind_distinguished_name": "bind_distinguished_name_example",
        "password_secret_id": "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx",
        "password_secret_version": 56
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.file_storage import FileStorageClient
    from oci.file_storage.models import ChangeOutboundConnectorCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OutboundConnectorActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "outbound_connector_id"

    def get_module_resource_id(self):
        return self.module.params.get("outbound_connector_id")

    def get_get_fn(self):
        return self.client.get_outbound_connector

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_outbound_connector,
            outbound_connector_id=self.module.params.get("outbound_connector_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeOutboundConnectorCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_outbound_connector_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                outbound_connector_id=self.module.params.get("outbound_connector_id"),
                change_outbound_connector_compartment_details=action_details,
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


OutboundConnectorActionsHelperCustom = get_custom_class(
    "OutboundConnectorActionsHelperCustom"
)


class ResourceHelper(
    OutboundConnectorActionsHelperCustom, OutboundConnectorActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            outbound_connector_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="outbound_connector",
        service_client_class=FileStorageClient,
        namespace="file_storage",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
