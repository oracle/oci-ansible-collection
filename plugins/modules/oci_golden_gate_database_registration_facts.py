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
module: oci_golden_gate_database_registration_facts
short_description: Fetches details about one or multiple DatabaseRegistration resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DatabaseRegistration resources in Oracle Cloud Infrastructure
    - "Note: Deprecated. Use the /connections API instead.
      Lists the DatabaseRegistrations in the compartment."
    - If I(database_registration_id) is specified, the details of a single DatabaseRegistration will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    database_registration_id:
        description:
            - A unique DatabaseRegistration identifier.
            - Required to get a specific database_registration.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment that contains the work request. Work requests should be scoped
              to the same compartment as the resource the work request affects. If the work request concerns
              multiple resources, and those resources are not in the same compartment, it is up to the service team
              to pick the primary resource whose compartment should be used.
            - Required to list multiple database_registrations.
        type: str
    lifecycle_state:
        description:
            - A filter to return only the resources that match the 'lifecycleState' given.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "NEEDS_ATTENTION"
            - "IN_PROGRESS"
            - "CANCELING"
            - "CANCELED"
            - "SUCCEEDED"
            - "WAITING"
    display_name:
        description:
            - A filter to return only the resources that match the entire 'displayName' given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is
              descending.  Default order for 'displayName' is ascending. If no value is specified
              timeCreated is the default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific database_registration
  oci_golden_gate_database_registration_facts:
    # required
    database_registration_id: "ocid1.databaseregistration.oc1..xxxxxxEXAMPLExxxxxx"

- name: List database_registrations
  oci_golden_gate_database_registration_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
database_registrations:
    description:
        - List of DatabaseRegistration resources
    returned: on success
    type: complex
    contains:
        ip_address:
            description:
                - The private IP address in the customer's VCN of the customer's endpoint, typically a
                  database.
                - Returned for get operation
            returned: on success
            type: str
            sample: ip_address_example
        rce_private_ip:
            description:
                - A Private Endpoint IP address created in the customer's subnet.
                  A customer database can expect network traffic initiated by GoldenGate Service from this IP address.
                  It can also send network traffic to this IP address, typically in response to requests from GoldenGate Service.
                  The customer may use this IP address in Security Lists or Network Security Groups (NSG) as needed.
                - Returned for get operation
            returned: on success
            type: str
            sample: rce_private_ip_example
        vault_id:
            description:
                - Refers to the customer's vault OCID.
                  If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate
                  to manage secrets contained within this vault.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id:
            description:
                - Refers to the customer's master key OCID.
                  If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        secret_compartment_id:
            description:
                - The OCID of the compartment where the GoldenGate Secret will be created.
                  If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.secretcompartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the databaseRegistration being
                  referenced.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - An object's Display Name.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Metadata about this specific object.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the resource was created. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the resource was last updated. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - Possible lifecycle states.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Describes the object's current state in detail. For example, it can be used to provide
                  actionable information for a resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - A simple key-value pair that is applied without any predefined name, type, or scope. Exists
                  for cross-compatibility only.
                - "Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Tags defined for this resource. Each key is predefined and scoped to a namespace.
                - "Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        fqdn:
            description:
                - A three-label Fully Qualified Domain Name (FQDN) for a resource.
            returned: on success
            type: str
            sample: fqdn_example
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the target subnet of the dedicated connection.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        system_tags:
            description:
                - The system tags associated with this resource, if any. The system tags are set by Oracle
                  Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more
                  information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
        database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database being referenced.
            returned: on success
            type: str
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        username:
            description:
                - The username Oracle GoldenGate uses to connect the associated system of the given technology.
                  This username must already exist and be available by the system/application to be connected to
                  and must conform to the case sensitivty requirments defined in it.
            returned: on success
            type: str
            sample: username_example
        connection_string:
            description:
                - Connect descriptor or Easy Connect Naming method used to connect to a database.
            returned: on success
            type: str
            sample: connection_string_example
        session_mode:
            description:
                - "The mode of the database connection session to be established by the data client.
                  'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database.
                  Connection to a RAC database involves a redirection received from the SCAN listeners
                  to the database node to connect to. By default the mode would be DIRECT."
            returned: on success
            type: str
            sample: DIRECT
        alias_name:
            description:
                - Credential store alias.
            returned: on success
            type: str
            sample: alias_name_example
        secret_id:
            description:
                - The OCID of the customer's GoldenGate Service Secret.
                  If provided, it references a key that customers will be required to ensure the policies are established
                  to permit GoldenGate to use this Secret.
            returned: on success
            type: str
            sample: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "ip_address": "ip_address_example",
        "rce_private_ip": "rce_private_ip_example",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
        "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
        "secret_compartment_id": "ocid1.secretcompartment.oc1..xxxxxxEXAMPLExxxxxx",
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
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "system_tags": {},
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "username": "username_example",
        "connection_string": "connection_string_example",
        "session_mode": "DIRECT",
        "alias_name": "alias_name_example",
        "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.golden_gate import GoldenGateClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseRegistrationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "database_registration_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_registration,
            database_registration_id=self.module.params.get("database_registration_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_database_registrations,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DatabaseRegistrationFactsHelperCustom = get_custom_class(
    "DatabaseRegistrationFactsHelperCustom"
)


class ResourceFactsHelper(
    DatabaseRegistrationFactsHelperCustom, DatabaseRegistrationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            database_registration_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "NEEDS_ATTENTION",
                    "IN_PROGRESS",
                    "CANCELING",
                    "CANCELED",
                    "SUCCEEDED",
                    "WAITING",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="database_registration",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(database_registrations=result)


if __name__ == "__main__":
    main()
