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
module: oci_file_storage_outbound_connector
short_description: Manage an OutboundConnector resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an OutboundConnector resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new outbound connector in the specified compartment.
      You can associate an outbound connector with a mount target only when
      they exist in the same availability domain.
    - For information about access control and compartments, see
      L(Overview of the IAM
      Service,https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm).
    - For information about availability domains, see L(Regions and
      Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm).
      To get a list of availability domains, use the
      `ListAvailabilityDomains` operation in the Identity and Access
      Management Service API.
    - All Oracle Cloud Infrastructure Services resources, including
      outbound connectors, get an Oracle-assigned, unique ID called an
      Oracle Cloud Identifier (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)).
      When you create a resource, you can find its OCID in the response.
      You can also retrieve a resource's OCID by using a List API operation on that resource
      type, or by viewing the resource in the Console.
    - "This resource has the following action operations in the M(oracle.oci.oci_file_storage_outbound_connector_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    availability_domain:
        description:
            - The availability domain the outbound connector is in. May be unset
              as a blank or NULL value.
            - "Example: `Uocm:PHX-AD-1`"
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the outbound connector.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    connector_type:
        description:
            - The account type of this outbound connector.
            - Required for create using I(state=present).
        type: str
        choices:
            - "LDAPBIND"
    endpoints:
        description:
            - Array of server endpoints to use when connecting with the LDAP bind account.
            - Required for create using I(state=present).
        type: list
        elements: dict
        suboptions:
            hostname:
                description:
                    - Name of the DNS server.
                type: str
                required: true
            port:
                description:
                    - Port of the DNS server.
                type: int
                required: true
    bind_distinguished_name:
        description:
            - The LDAP Distinguished Name of the bind account.
            - Required for create using I(state=present).
        type: str
    password_secret_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the password for the LDAP bind account in the Vault.
        type: str
    password_secret_version:
        description:
            - Version of the password secret in the Vault to use.
        type: int
    display_name:
        description:
            - A user-friendly name. It does not have to be unique, and it is changeable.
              Avoid entering confidential information.
            - "Example: `My outbound connector`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair
               with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    outbound_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the outbound connector.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the OutboundConnector.
            - Use I(state=present) to create or update an OutboundConnector.
            - Use I(state=absent) to delete an OutboundConnector.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create outbound_connector with connector_type = LDAPBIND
  oci_file_storage_outbound_connector:
    # required
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connector_type: LDAPBIND
    endpoints:
    - # required
      hostname: hostname_example
      port: 56
    bind_distinguished_name: bind_distinguished_name_example

    # optional
    password_secret_id: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
    password_secret_version: 56
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update outbound_connector
  oci_file_storage_outbound_connector:
    # required
    outbound_connector_id: "ocid1.outboundconnector.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update outbound_connector using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_file_storage_outbound_connector:
    # required
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete outbound_connector
  oci_file_storage_outbound_connector:
    # required
    outbound_connector_id: "ocid1.outboundconnector.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete outbound_connector using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_file_storage_outbound_connector:
    # required
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.file_storage import FileStorageClient
    from oci.file_storage.models import CreateOutboundConnectorDetails
    from oci.file_storage.models import UpdateOutboundConnectorDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OutboundConnectorHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(OutboundConnectorHelperGen, self).get_possible_entity_types() + [
            "outboundconnector",
            "outboundconnectors",
            "fileStorageoutboundconnector",
            "fileStorageoutboundconnectors",
            "outboundconnectorresource",
            "outboundconnectorsresource",
            "filestorage",
        ]

    def get_module_resource_id_param(self):
        return "outbound_connector_id"

    def get_module_resource_id(self):
        return self.module.params.get("outbound_connector_id")

    def get_get_fn(self):
        return self.client.get_outbound_connector

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_outbound_connector, outbound_connector_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_outbound_connector,
            outbound_connector_id=self.module.params.get("outbound_connector_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "availability_domain",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_outbound_connectors, **kwargs
        )

    def get_create_model_class(self):
        return CreateOutboundConnectorDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_outbound_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(create_outbound_connector_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateOutboundConnectorDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_outbound_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                outbound_connector_id=self.module.params.get("outbound_connector_id"),
                update_outbound_connector_details=update_details,
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
            call_fn=self.client.delete_outbound_connector,
            call_fn_args=(),
            call_fn_kwargs=dict(
                outbound_connector_id=self.module.params.get("outbound_connector_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


OutboundConnectorHelperCustom = get_custom_class("OutboundConnectorHelperCustom")


class ResourceHelper(OutboundConnectorHelperCustom, OutboundConnectorHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            availability_domain=dict(type="str"),
            compartment_id=dict(type="str"),
            connector_type=dict(type="str", choices=["LDAPBIND"]),
            endpoints=dict(
                type="list",
                elements="dict",
                options=dict(
                    hostname=dict(type="str", required=True),
                    port=dict(type="int", required=True),
                ),
            ),
            bind_distinguished_name=dict(type="str"),
            password_secret_id=dict(type="str"),
            password_secret_version=dict(type="int", no_log=True),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            outbound_connector_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
