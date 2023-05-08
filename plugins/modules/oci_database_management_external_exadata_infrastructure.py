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
module: oci_database_management_external_exadata_infrastructure
short_description: Manage an ExternalExadataInfrastructure resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an ExternalExadataInfrastructure resource in Oracle Cloud Infrastructure
    - "For I(state=present), creates an OCI resource for the Exadata infrastructure and enable monitoring service on the exadata infrastructure.
      The following resource/subresources are created:
        Infrastructure
        Storage server connectors
        Storage servers
        Storage grids"
    - "This resource has the following action operations in the M(oracle.oci.oci_database_management_external_exadata_infrastructure_actions) module:
      change_compartment, disable_external_exadata_infrastructure_management, discover, enable_external_exadata_infrastructure_management."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    discovery_key:
        description:
            - The unique key of the discovery request.
            - This parameter is updatable.
        type: str
    license_model:
        description:
            - The Oracle license model that applies to the database management resources.
            - This parameter is updatable.
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of compartment.
            - Required for create using I(state=present), update using I(state=present) with external_exadata_infrastructure_id present.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - The name of the Exadata infrastructure.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    db_system_ids:
        description:
            - The list of all the rac database system OCIDs.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: str
    storage_server_names:
        description:
            - The list of all the storage server names to be included for monitoering purpose. If not specified, all the storage servers associated with the
              database systems are included.
            - This parameter is updatable.
        type: list
        elements: str
    external_exadata_infrastructure_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ExternalExadataInfrastructure.
            - Use I(state=present) to create or update an ExternalExadataInfrastructure.
            - Use I(state=absent) to delete an ExternalExadataInfrastructure.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create external_exadata_infrastructure
  oci_database_management_external_exadata_infrastructure:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    db_system_ids: [ "db_system_ids_example" ]

    # optional
    discovery_key: discovery_key_example
    license_model: LICENSE_INCLUDED
    storage_server_names: [ "storage_server_names_example" ]

- name: Update external_exadata_infrastructure
  oci_database_management_external_exadata_infrastructure:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    external_exadata_infrastructure_id: "ocid1.externalexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    discovery_key: discovery_key_example
    license_model: LICENSE_INCLUDED
    display_name: display_name_example
    db_system_ids: [ "db_system_ids_example" ]
    storage_server_names: [ "storage_server_names_example" ]

- name: Update external_exadata_infrastructure using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_management_external_exadata_infrastructure:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    discovery_key: discovery_key_example
    license_model: LICENSE_INCLUDED
    db_system_ids: [ "db_system_ids_example" ]
    storage_server_names: [ "storage_server_names_example" ]

- name: Delete external_exadata_infrastructure
  oci_database_management_external_exadata_infrastructure:
    # required
    external_exadata_infrastructure_id: "ocid1.externalexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete external_exadata_infrastructure using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_management_external_exadata_infrastructure:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
external_exadata_infrastructure:
    description:
        - Details of the ExternalExadataInfrastructure resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - "The name of the resource. English letters, numbers, \\"-\\", \\"_\\" and \\".\\" only."
            returned: on success
            type: str
            sample: display_name_example
        version:
            description:
                - The version of the resource.
            returned: on success
            type: str
            sample: version_example
        internal_id:
            description:
                - The internal ID.
            returned: on success
            type: str
            sample: "ocid1.internal.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - The status of the entity.
            returned: on success
            type: str
            sample: status_example
        lifecycle_state:
            description:
                - The current lifecycle state of the database resource.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The timestamp of the creation.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The timestamp of the last update.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - The details of the lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        additional_details:
            description:
                - "The additional details of the resource defined in `{\\"key\\": \\"value\\"}` format.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {}
        resource_type:
            description:
                - The type of resource.
            returned: on success
            type: str
            sample: INFRASTRUCTURE_SUMMARY
        rack_size:
            description:
                - The rack size of the Exadata infrastructure.
            returned: on success
            type: str
            sample: FULL
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        license_model:
            description:
                - The Oracle license model that applies to the database management resources.
            returned: on success
            type: str
            sample: LICENSE_INCLUDED
        storage_grid:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata resource.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - "The name of the resource. English letters, numbers, \\"-\\", \\"_\\" and \\".\\" only."
                    returned: on success
                    type: str
                    sample: display_name_example
                version:
                    description:
                        - The version of the resource.
                    returned: on success
                    type: str
                    sample: version_example
                internal_id:
                    description:
                        - The internal ID.
                    returned: on success
                    type: str
                    sample: "ocid1.internal.oc1..xxxxxxEXAMPLExxxxxx"
                status:
                    description:
                        - The status of the entity.
                    returned: on success
                    type: str
                    sample: status_example
                lifecycle_state:
                    description:
                        - The current lifecycle state of the database resource.
                    returned: on success
                    type: str
                    sample: CREATING
                time_created:
                    description:
                        - The timestamp of the creation.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The timestamp of the last update.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                lifecycle_details:
                    description:
                        - The details of the lifecycle state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                additional_details:
                    description:
                        - "The additional details of the resource defined in `{\\"key\\": \\"value\\"}` format.
                          Example: `{\\"bar-key\\": \\"value\\"}`"
                    returned: on success
                    type: dict
                    sample: {}
                resource_type:
                    description:
                        - The type of resource.
                    returned: on success
                    type: str
                    sample: INFRASTRUCTURE_SUMMARY
                server_count:
                    description:
                        - The number of the storage servers in the Exadata infrastructure.
                    returned: on success
                    type: float
                    sample: 10
        database_systems:
            description:
                - A list of database systems.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata resource.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - "The name of the resource. English letters, numbers, \\"-\\", \\"_\\" and \\".\\" only."
                    returned: on success
                    type: str
                    sample: display_name_example
                version:
                    description:
                        - The version of the resource.
                    returned: on success
                    type: str
                    sample: version_example
                internal_id:
                    description:
                        - The internal ID.
                    returned: on success
                    type: str
                    sample: "ocid1.internal.oc1..xxxxxxEXAMPLExxxxxx"
                status:
                    description:
                        - The status of the entity.
                    returned: on success
                    type: str
                    sample: status_example
                lifecycle_state:
                    description:
                        - The current lifecycle state of the database resource.
                    returned: on success
                    type: str
                    sample: CREATING
                time_created:
                    description:
                        - The timestamp of the creation.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The timestamp of the last update.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                lifecycle_details:
                    description:
                        - The details of the lifecycle state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                additional_details:
                    description:
                        - "The additional details of the resource defined in `{\\"key\\": \\"value\\"}` format.
                          Example: `{\\"bar-key\\": \\"value\\"}`"
                    returned: on success
                    type: dict
                    sample: {}
                resource_type:
                    description:
                        - The type of resource.
                    returned: on success
                    type: str
                    sample: INFRASTRUCTURE_SUMMARY
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of compartment.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                license_model:
                    description:
                        - The Oracle license model that applies to the database management resources.
                    returned: on success
                    type: str
                    sample: LICENSE_INCLUDED
        database_compartments:
            description:
                - The list of L(OCIDs],https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartments
            returned: on success
            type: list
            sample: []
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "version": "version_example",
        "internal_id": "ocid1.internal.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "status_example",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "additional_details": {},
        "resource_type": "INFRASTRUCTURE_SUMMARY",
        "rack_size": "FULL",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "license_model": "LICENSE_INCLUDED",
        "storage_grid": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "version": "version_example",
            "internal_id": "ocid1.internal.oc1..xxxxxxEXAMPLExxxxxx",
            "status": "status_example",
            "lifecycle_state": "CREATING",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "lifecycle_details": "lifecycle_details_example",
            "additional_details": {},
            "resource_type": "INFRASTRUCTURE_SUMMARY",
            "server_count": 10
        },
        "database_systems": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "version": "version_example",
            "internal_id": "ocid1.internal.oc1..xxxxxxEXAMPLExxxxxx",
            "status": "status_example",
            "lifecycle_state": "CREATING",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "lifecycle_details": "lifecycle_details_example",
            "additional_details": {},
            "resource_type": "INFRASTRUCTURE_SUMMARY",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "license_model": "LICENSE_INCLUDED"
        }],
        "database_compartments": []
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
    from oci.database_management.models import (
        CreateExternalExadataInfrastructureDetails,
    )
    from oci.database_management.models import (
        UpdateExternalExadataInfrastructureDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalExadataInfrastructureHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            ExternalExadataInfrastructureHelperGen, self
        ).get_possible_entity_types() + [
            "externalexadatainfrastructure",
            "externalexadatainfrastructures",
            "databaseManagementexternalexadatainfrastructure",
            "databaseManagementexternalexadatainfrastructures",
            "externalexadatainfrastructureresource",
            "externalexadatainfrastructuresresource",
            "databasemanagement",
        ]

    def get_module_resource_id_param(self):
        return "external_exadata_infrastructure_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_exadata_infrastructure_id")

    def get_get_fn(self):
        return self.client.get_external_exadata_infrastructure

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_exadata_infrastructure,
            external_exadata_infrastructure_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_exadata_infrastructure,
            external_exadata_infrastructure_id=self.module.params.get(
                "external_exadata_infrastructure_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
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
            self.client.list_external_exadata_infrastructures, **kwargs
        )

    def get_create_model_class(self):
        return CreateExternalExadataInfrastructureDetails

    def get_exclude_attributes(self):
        return ["storage_server_names", "discovery_key", "db_system_ids"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_external_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_external_exadata_infrastructure_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateExternalExadataInfrastructureDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_external_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_exadata_infrastructure_id=self.module.params.get(
                    "external_exadata_infrastructure_id"
                ),
                update_external_exadata_infrastructure_details=update_details,
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
            call_fn=self.client.delete_external_exadata_infrastructure,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_exadata_infrastructure_id=self.module.params.get(
                    "external_exadata_infrastructure_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ExternalExadataInfrastructureHelperCustom = get_custom_class(
    "ExternalExadataInfrastructureHelperCustom"
)


class ResourceHelper(
    ExternalExadataInfrastructureHelperCustom, ExternalExadataInfrastructureHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            discovery_key=dict(type="str", no_log=True),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            db_system_ids=dict(type="list", elements="str"),
            storage_server_names=dict(type="list", elements="str"),
            external_exadata_infrastructure_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="external_exadata_infrastructure",
        service_client_class=DbManagementClient,
        namespace="database_management",
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
