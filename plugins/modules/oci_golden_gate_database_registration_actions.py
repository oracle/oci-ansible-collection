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
module: oci_golden_gate_database_registration_actions
short_description: Perform actions on a DatabaseRegistration resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DatabaseRegistration resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the DatabaseRegistration into a different compartment within the same tenancy. When provided, If-Match is checked
      against ETag values of the resource.  For information about moving resources between compartments, see L(Moving Resources Between
      Compartments,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9"
author: Oracle (@oracle)
options:
    database_registration_id:
        description:
            - A unique DatabaseRegistration identifier.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
        type: str
        required: true
    action:
        description:
            - The action to perform on the DatabaseRegistration.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on database_registration
  oci_golden_gate_database_registration_actions:
    database_registration_id: "ocid1.databaseregistration.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
database_registration:
    description:
        - Details of the DatabaseRegistration resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the databaseRegistration being referenced.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - An object's Display Name.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - Metadata about this specific object.
            returned: on success
            type: string
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the resource was created. The format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339), such as
                  `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time the resource was last updated. The format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339), such as
                  `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - Possible lifecycle states.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed
                  state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - "A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Tags defined for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        fqdn:
            description:
                - A three-label Fully Qualified Domain Name (FQDN) for a resource.
            returned: on success
            type: string
            sample: fqdn_example
        ip_address:
            description:
                - The private IP address in the customer's VCN of the customer's endpoint, typically a database.
            returned: on success
            type: string
            sample: ip_address_example
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet being referenced.
            returned: on success
            type: string
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database being referenced.
            returned: on success
            type: string
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        rce_private_ip:
            description:
                - A Private Endpoint IP Address created in the customer's subnet.  A customer database can expect network traffic initiated by GGS from this IP
                  address and send network traffic to this IP address, typically in response to requests from GGS (OGG).  The customer may utilize this IP
                  address in Security Lists or Network Security Groups (NSG) as needed.
            returned: on success
            type: string
            sample: rce_private_ip_example
        system_tags:
            description:
                - "The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is
                  predefined and scoped to namespaces.  For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
        username:
            description:
                - The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the
                  database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.
            returned: on success
            type: string
            sample: username_example
        connection_string:
            description:
                - Connect descriptor or Easy Connect Naming method that Oracle GoldenGate uses to connect to a database.
            returned: on success
            type: string
            sample: connection_string_example
        alias_name:
            description:
                - Credential store alias.
            returned: on success
            type: string
            sample: alias_name_example
        vault_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the customer vault being referenced. If provided, this
                  will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage
                  secrets contained within this vault.
            returned: on success
            type: string
            sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id:
            description:
                - "The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the customer \\"Master\\" key being referenced. If
                  provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate
                  Service to utilize this key to manage secrets."
            returned: on success
            type: string
            sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        secret_compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment where the the GGS Secret will be
                  created. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the
                  GoldenGate Service to utilize this Compartment in which to create a Secret.
            returned: on success
            type: string
            sample: "ocid1.secretcompartment.oc1..xxxxxxEXAMPLExxxxxx"
        secret_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the customer GGS Secret being referenced. If provided,
                  this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to
                  utilize this Secret
            returned: on success
            type: string
            sample: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "fqdn": "fqdn_example",
        "ip_address": "ip_address_example",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "rce_private_ip": "rce_private_ip_example",
        "system_tags": {},
        "username": "username_example",
        "connection_string": "connection_string_example",
        "alias_name": "alias_name_example",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
        "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
        "secret_compartment_id": "ocid1.secretcompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.golden_gate import GoldenGateClient
    from oci.golden_gate.models import ChangeDatabaseRegistrationCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseRegistrationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "database_registration_id"

    def get_module_resource_id(self):
        return self.module.params.get("database_registration_id")

    def get_get_fn(self):
        return self.client.get_database_registration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_registration,
            database_registration_id=self.module.params.get("database_registration_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDatabaseRegistrationCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_database_registration_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_registration_id=self.module.params.get(
                    "database_registration_id"
                ),
                change_database_registration_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DatabaseRegistrationActionsHelperCustom = get_custom_class(
    "DatabaseRegistrationActionsHelperCustom"
)


class ResourceHelper(
    DatabaseRegistrationActionsHelperCustom, DatabaseRegistrationActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            database_registration_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="database_registration",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
