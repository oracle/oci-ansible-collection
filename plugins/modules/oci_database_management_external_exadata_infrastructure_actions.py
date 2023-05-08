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
module: oci_database_management_external_exadata_infrastructure_actions
short_description: Perform actions on an ExternalExadataInfrastructure resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an ExternalExadataInfrastructure resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the Exadata infrastructure  and its related resources (storage server, storage server connectors and storage
      server grid) to the specified compartment.
    - For I(action=disable_external_exadata_infrastructure_management), disables Database Management service for the Exadata infrastructure specified by
      externalExadataInfrastructureId.
      It covers the following components
                Exadata infrastructure
                Exadata storage grid
                Exadata storage server
      Database systems within the Exdata infrastructure will not be impacted and should be disabled explicitly if needed.
    - For I(action=enable_external_exadata_infrastructure_management), enables Database Management service for the exadata infrastructure specified by
      externalExadataInfrastructureId. It covers the following
      components
        Exadata infrastructure
        Exadata storage grid
        Exadata storage server
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
              compartment to move the Exadata infrastructure and related components to.
            - Required for I(action=change_compartment).
        type: str
    external_exadata_infrastructure_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
        type: str
        aliases: ["id"]
        required: true
    license_model:
        description:
            - The Oracle license model.
            - Required for I(action=enable_external_exadata_infrastructure_management).
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    action:
        description:
            - The action to perform on the ExternalExadataInfrastructure.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "disable_external_exadata_infrastructure_management"
            - "enable_external_exadata_infrastructure_management"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on external_exadata_infrastructure
  oci_database_management_external_exadata_infrastructure_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    external_exadata_infrastructure_id: "ocid1.externalexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action disable_external_exadata_infrastructure_management on external_exadata_infrastructure
  oci_database_management_external_exadata_infrastructure_actions:
    # required
    external_exadata_infrastructure_id: "ocid1.externalexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    action: disable_external_exadata_infrastructure_management

- name: Perform action enable_external_exadata_infrastructure_management on external_exadata_infrastructure
  oci_database_management_external_exadata_infrastructure_actions:
    # required
    external_exadata_infrastructure_id: "ocid1.externalexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    license_model: LICENSE_INCLUDED
    action: enable_external_exadata_infrastructure_management

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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient
    from oci.database_management.models import (
        ChangeExternalExadataInfrastructureCompartmentDetails,
    )
    from oci.database_management.models import (
        EnableExternalExadataInfrastructureManagementDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalExadataInfrastructureActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        disable_external_exadata_infrastructure_management
        enable_external_exadata_infrastructure_management
    """

    @staticmethod
    def get_module_resource_id_param():
        return "external_exadata_infrastructure_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_exadata_infrastructure_id")

    def get_get_fn(self):
        return self.client.get_external_exadata_infrastructure

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_exadata_infrastructure,
            external_exadata_infrastructure_id=self.module.params.get(
                "external_exadata_infrastructure_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeExternalExadataInfrastructureCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_external_exadata_infrastructure_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_exadata_infrastructure_id=self.module.params.get(
                    "external_exadata_infrastructure_id"
                ),
                change_external_exadata_infrastructure_compartment_details=action_details,
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

    def disable_external_exadata_infrastructure_management(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_external_exadata_infrastructure_management,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_exadata_infrastructure_id=self.module.params.get(
                    "external_exadata_infrastructure_id"
                ),
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

    def enable_external_exadata_infrastructure_management(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, EnableExternalExadataInfrastructureManagementDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_external_exadata_infrastructure_management,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_exadata_infrastructure_id=self.module.params.get(
                    "external_exadata_infrastructure_id"
                ),
                enable_external_exadata_infrastructure_management_details=action_details,
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


ExternalExadataInfrastructureActionsHelperCustom = get_custom_class(
    "ExternalExadataInfrastructureActionsHelperCustom"
)


class ResourceHelper(
    ExternalExadataInfrastructureActionsHelperCustom,
    ExternalExadataInfrastructureActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            external_exadata_infrastructure_id=dict(
                aliases=["id"], type="str", required=True
            ),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "disable_external_exadata_infrastructure_management",
                    "enable_external_exadata_infrastructure_management",
                ],
            ),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
