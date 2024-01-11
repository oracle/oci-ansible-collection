#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_application_migration_source_actions
short_description: Perform actions on a Source resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Source resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the specified source into a different compartment within the same tenancy. For information about moving resources
      between compartments, see L(Moving Resources to a Different
      Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              to move the resource to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Source.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on source
  oci_application_migration_source_actions:
    # required
    source_id: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
source:
    description:
        - Details of the Source resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the source.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The date and time at which the source was created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the source.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details about the current lifecycle state of the source.
            returned: on success
            type: str
            sample: lifecycle_details_example
        source_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                manifest:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        version:
                            description:
                                - the version of the export tool that was used to generate the manifest
                            returned: on success
                            type: str
                            sample: version_example
                        export_type:
                            description:
                                - the type of application that the export tool was executed against to generate this manifest
                            returned: on success
                            type: str
                            sample: export_type_example
                        export_details:
                            description:
                                - application specific details as parsed from various sources of the application that was exported
                            returned: on success
                            type: dict
                            sample: {}
                        timestamp:
                            description:
                                - when this manifest was generated
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        md5:
                            description:
                                - the MD5 hash of the export artifact archive that was produced by the export tool and should be used with this manifest
                            returned: on success
                            type: str
                            sample: md5_example
                        signature:
                            description:
                                - a sha1 hash of all the fields of this manifest (excluding the signature)
                            returned: on success
                            type: str
                            sample: signature_example
                namespace:
                    description:
                        - the object storage namespace where the bucket and uploaded object resides
                    returned: on success
                    type: str
                    sample: namespace_example
                bucket:
                    description:
                        - the bucket wherein the export archive exists in object storage
                    returned: on success
                    type: str
                    sample: bucket_example
                object_name:
                    description:
                        - the name of the archive as it exists in object storage
                    returned: on success
                    type: str
                    sample: object_name_example
                account_name:
                    description:
                        - "The identity domain ID of your traditional Oracle Cloud Infrastructure - Classic account."
                    returned: on success
                    type: str
                    sample: account_name_example
                type:
                    description:
                        - The type of source environment.
                    returned: on success
                    type: str
                    sample: OCIC
                region:
                    description:
                        - "The Oracle Cloud Infrastructure - Classic region from which you want to migrate your applications. For example, uscom-east-1 or
                          uscom-central-1."
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                compute_account:
                    description:
                        - If you are using an Oracle Cloud@Customer account with Identity Cloud Service (IDCS), enter the service instance ID.
                          For example, if Compute-567890123 is the account name of your Oracle Cloud@Customer Compute service entitlement,
                          then enter 567890123.
                    returned: on success
                    type: str
                    sample: compute_account_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example:
                  `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example:
                  `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "source_details": {
            "manifest": {
                "version": "version_example",
                "export_type": "export_type_example",
                "export_details": {},
                "timestamp": "2013-10-20T19:20:30+01:00",
                "md5": "md5_example",
                "signature": "signature_example"
            },
            "namespace": "namespace_example",
            "bucket": "bucket_example",
            "object_name": "object_name_example",
            "account_name": "account_name_example",
            "type": "OCIC",
            "region": "us-phoenix-1",
            "compute_account": "compute_account_example"
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.application_migration import ApplicationMigrationClient
    from oci.application_migration.models import ChangeCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SourceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "source_id"

    def get_module_resource_id(self):
        return self.module.params.get("source_id")

    def get_get_fn(self):
        return self.client.get_source

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_source, source_id=self.module.params.get("source_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_source_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                source_id=self.module.params.get("source_id"),
                change_source_compartment_details=action_details,
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


SourceActionsHelperCustom = get_custom_class("SourceActionsHelperCustom")


class ResourceHelper(SourceActionsHelperCustom, SourceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            source_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="source",
        service_client_class=ApplicationMigrationClient,
        namespace="application_migration",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
